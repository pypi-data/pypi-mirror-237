# mypy: disable-error-code="import"
"""Defines the API for Gaussian diffusion.

This is largely take from `here <https://github.com/tonyduan/diffusion>`_.

This module can be used to train a Gaussian diffusion model as follows.

.. code-block:: python

    # Instantiate the beta schedule and diffusion module.
    betas = get_diffusion_beta_schedule("linear", 1000)
    diff = GaussianDiffusion(betas)

    # Pseudo-training loop.
    for _ in range(1000):
        images = ds[index]  # Get some image from the dataset
        loss = diff.loss(images, model)
        loss.backward()
        optimizer.step()

    # Sample from the model.
    init_noise = torch.randn_like(images)
    generated = diff.sample(model, init_noise)
    show_image(generated[-1])

Choices for the beta schedule are:

- ``"linear"``: Linearly increasing beta.
- ``"quad"``: Quadratically increasing beta.
- ``"warmup"``: Linearly increasing beta with a warmup period.
- ``"const"``: Constant beta.
- ``"cosine"``: Cosine annealing schedule.
- ``"jsd"``: Jensen-Shannon divergence schedule.
"""

import math
from pathlib import Path
from typing import Callable, Literal, cast, get_args

import torch
from torch import Tensor, nn

from ml.tasks.losses.loss import loss_fn
from ml.tasks.ode import ODESolverType, get_ode_solver

DiffusionLossFn = Literal["mse", "l1", "pseudo-huber"]
DiffusionPredMode = Literal["pred_x_0", "pred_eps", "pred_v"]
SigmaType = Literal["upper_bound", "lower_bound"]
DiffusionBetaSchedule = Literal["linear", "quad", "warmup", "const", "cosine", "jsd"]


def _warmup_beta_schedule(
    beta_start: float,
    beta_end: float,
    num_timesteps: int,
    warmup: float,
    dtype: torch.dtype = torch.float32,
) -> Tensor:
    betas = beta_end * torch.ones(num_timesteps, dtype=dtype)
    warmup_time = int(num_timesteps * warmup)
    betas[:warmup_time] = torch.linspace(beta_start, beta_end, warmup_time, dtype=dtype)
    return betas


def _cosine_beta_schedule(
    num_timesteps: int,
    offset: float = 0.008,
    dtype: torch.dtype = torch.float32,
) -> Tensor:
    rng = torch.arange(num_timesteps, dtype=dtype)
    f_t = torch.cos((rng / (num_timesteps - 1) + offset) / (1 + offset) * math.pi / 2) ** 2
    bar_alpha = f_t / f_t[0]
    beta = torch.zeros_like(bar_alpha)
    beta[1:] = (1 - (bar_alpha[1:] / bar_alpha[:-1])).clip(0, 0.999)
    return beta


def cast_beta_schedule(schedule: str) -> DiffusionBetaSchedule:
    assert schedule in get_args(DiffusionBetaSchedule), f"Unknown schedule type: {schedule}"
    return cast(DiffusionBetaSchedule, schedule)


def get_diffusion_beta_schedule(
    schedule: DiffusionBetaSchedule,
    num_timesteps: int,
    *,
    beta_start: float = 0.0001,
    beta_end: float = 0.02,
    warmup: float = 0.1,
    cosine_offset: float = 0.008,
    dtype: torch.dtype = torch.float32,
) -> Tensor:
    """Returns a beta schedule for the given schedule type.

    Args:
        schedule: The schedule type.
        num_timesteps: The total number of timesteps.
        beta_start: The initial beta value, for linear, quad, and warmup
            schedules.
        beta_end: The final beta value, for linear, quad, warmup and const
            schedules.
        warmup: The fraction of timesteps to use for the warmup schedule
            (between 0 and 1).
        cosine_offset: The cosine offset, for cosine schedules.
        dtype: The dtype of the returned tensor.

    Returns:
        The beta schedule, a tensor with shape ``(num_timesteps)``.
    """
    match schedule:
        case "linear":
            return torch.linspace(beta_start, beta_end, num_timesteps, dtype=dtype)
        case "quad":
            return torch.linspace(beta_start**0.5, beta_end**0.5, num_timesteps, dtype=dtype) ** 2
        case "warmup":
            return _warmup_beta_schedule(beta_start, beta_end, num_timesteps, warmup, dtype=dtype)
        case "const":
            return torch.full((num_timesteps,), beta_end, dtype=dtype)
        case "cosine":
            return _cosine_beta_schedule(num_timesteps, cosine_offset, dtype=dtype)
        case "jsd":
            return torch.linspace(num_timesteps, 1, num_timesteps, dtype=dtype) ** -1.0
        case _:
            raise NotImplementedError(f"Unknown schedule type: {schedule}")


class GaussianDiffusion(nn.Module):
    """Defines a module which provides utility functions for Gaussian diffusion.

    Parameters:
        betas: The beta values for each timestep, provided by the function
            :func:`get_diffusion_beta_schedule`.
        pred_mode: The prediction mode, which determines what the model should
            predict. Can be one of:

            - ``"pred_x_0"``: Predicts the initial noise.
            - ``"pred_eps"``: Predicts the noise at the current timestep.
            - ``"pred_v"``: Predicts the velocity of the noise.

        loss: The type of loss to use. Can be one of:

                - ``"mse"``: Mean squared error.
                - ``"l1"``: Mean absolute error.

        sigma_type: The type of sigma to use. Can be one of:

                - ``"upper_bound"``: The upper bound of the posterior noise.
                - ``"lower_bound"``: The lower bound of the posterior noise.
    """

    __constants__ = ["num_timesteps", "pred_mode", "sigma_type"]

    def __init__(
        self,
        betas: Tensor,
        pred_mode: DiffusionPredMode = "pred_x_0",
        loss: DiffusionLossFn = "mse",
        sigma_type: SigmaType = "upper_bound",
        solver: ODESolverType = "euler",
    ) -> None:
        super().__init__()

        assert betas.dim() == 1

        self.num_timesteps = betas.shape[0] - 1
        self.pred_mode = pred_mode
        self.sigma_type = sigma_type
        self.loss_fn = loss_fn(loss)

        assert not (betas < 0).any(), "Betas must be non-negative."
        assert not (betas > 1).any(), "Betas must be less than or equal to 1."

        bar_alpha = torch.cumprod(1.0 - betas, dim=0)
        self.register_buffer("bar_alpha", bar_alpha, persistent=False)

        # The ODE solver to use.
        self.solver = get_ode_solver(solver)

    bar_alpha: Tensor

    def loss(self, model: Callable[[Tensor, Tensor], Tensor], x: Tensor) -> Tensor:
        """Computes the loss for a given sample.

        Args:
            model: The model forward process, which takes a tensor with the
                same shape as the input data plus a timestep and returns the
                predicted noise or target, with shape ``(*)``.
            x: The input data, with shape ``(*)``

        Returns:
            The loss, with shape ``(*)``.
        """
        bsz = x.shape[0]
        t_sample = torch.randint(1, self.num_timesteps + 1, size=(bsz,), device=x.device)
        eps = torch.randn_like(x)
        bar_alpha = self.bar_alpha[t_sample].view(-1, *[1] * (x.dim() - 1)).expand(x.shape)
        x_t = torch.sqrt(bar_alpha) * x + torch.sqrt(1 - bar_alpha) * eps
        pred_target = model(x_t, t_sample)
        match self.pred_mode:
            case "pred_x_0":
                gt_target = x
            case "pred_eps":
                gt_target = eps
            case "pred_v":
                gt_target = torch.sqrt(bar_alpha) * eps - torch.sqrt(1 - bar_alpha) * x
            case _:
                raise NotImplementedError(f"Unknown pred_mode: {self.pred_mode}")
        return self.loss_fn(pred_target, gt_target)

    @torch.no_grad()
    def partial_sample(
        self,
        model: Callable[[Tensor, Tensor], Tensor],
        reference_sample: Tensor,
        start_percent: float,
        sampling_timesteps: int | None = None,
    ) -> Tensor:
        """Samples from the model, starting from a given reference sample.

        Partial sampling takes a reference sample, adds some noise to it, then
        denoises the sample using the model. This can be used for doing
        style transfer, where the reference sample is the source image which
        the model redirects to look more like some target style.

        Args:
            model: The model forward process, which takes a tensor with the
                same shape as the input data plus a timestep and returns the
                predicted noise or target, with shape ``(*)``.
            reference_sample: The reference sample, with shape ``(*)``.
            start_percent: The percentage of timesteps to start sampling from.
            sampling_timesteps: The number of timesteps to sample for. If
                ``None``, then the full number of timesteps will be used.

        Returns:
            The samples, with shape ``(sampling_timesteps + 1, *)``.
        """
        assert 0.0 <= start_percent <= 1.0
        num_timesteps = round(self.num_timesteps * start_percent)
        scalar_t_start = num_timesteps
        noise = torch.randn_like(reference_sample)
        bar_alpha = self.bar_alpha[scalar_t_start].view(-1, *[1] * (noise.dim() - 1)).expand(noise.shape)
        x = torch.sqrt(bar_alpha) * reference_sample + torch.sqrt(1 - bar_alpha) * noise
        return self._sample_common(
            model=model,
            x=x,
            sampling_timesteps=sampling_timesteps,
            start_percent=start_percent,
        )

    @torch.no_grad()
    def sample(
        self,
        model: Callable[[Tensor, Tensor], Tensor],
        shape: tuple[int, ...],
        device: torch.device,
        sampling_timesteps: int | None = None,
    ) -> Tensor:
        """Samples from the model.

        Args:
            model: The model forward process, which takes a tensor with the
                same shape as the input data plus a timestep and returns the
                predicted noise or target, with shape ``(*)``.
            shape: The shape of the samples.
            device: The device to put the samples on.
            sampling_timesteps: The number of timesteps to sample for. If
                ``None``, then the full number of timesteps will be used.

        Returns:
            The samples, with shape ``(sampling_timesteps + 1, *)``.
        """
        return self._sample_common(
            model=model,
            x=torch.randn(shape, device=device),
            sampling_timesteps=sampling_timesteps,
            start_percent=0.0,
        )

    @torch.no_grad()
    def _get_bar_alpha(self, t: int, x: Tensor) -> tuple[Tensor, Tensor]:
        t_tensor = torch.empty((x.shape[0],), dtype=torch.int64, device=x.device).fill_(t)
        bar_alpha = self.bar_alpha[t_tensor].view(-1, *[1] * (x.dim() - 1)).expand(x.shape)
        return t_tensor, bar_alpha

    @torch.no_grad()
    def _sample_step(
        self,
        model: Callable[[Tensor, Tensor], Tensor],
        x: Tensor,
        scalar_t_start: int,
        scalar_t_end: int,
    ) -> Tensor:
        t_start, bar_alpha_start = self._get_bar_alpha(scalar_t_start, x)
        _, bar_alpha_end = self._get_bar_alpha(scalar_t_end, x)

        # Use model to predict x_0.
        match self.pred_mode:
            case "pred_x_0":
                pred_x_0 = model(x, t_start)
            case "pred_eps":
                pred_eps = model(x, t_start)
                pred_x_0 = (x - torch.sqrt(1 - bar_alpha_start) * pred_eps) / torch.sqrt(bar_alpha_start)
            case "pred_v":
                pred_v = model(x, t_start)
                pred_x_0 = torch.sqrt(bar_alpha_start) * x - torch.sqrt(1 - bar_alpha_start) * pred_v
            case _:
                raise AssertionError(f"Invalid {self.pred_mode=}.")

        # Forward model posterior mean given x_0, x_t
        # When t_start = t_end + 1, bar_alpha_start / bar_alpha_end = 1 / alpha_end
        lhs = (1 - bar_alpha_end) * torch.sqrt(bar_alpha_start / bar_alpha_end) * x
        rhs = torch.sqrt(bar_alpha_end) * (1 - bar_alpha_start / bar_alpha_end) * pred_x_0
        x_next = (rhs + lhs) / (1 - bar_alpha_start)

        return x_next

    @torch.no_grad()
    def _add_noise(self, x: Tensor, scalar_t_start: int, scalar_t_end: int) -> Tensor:
        _, bar_alpha_start = self._get_bar_alpha(scalar_t_start, x)
        _, bar_alpha_end = self._get_bar_alpha(scalar_t_end, x)

        # Forward model posterior noise
        match self.sigma_type:
            case "upper_bound":
                std = torch.sqrt(1 - bar_alpha_start / bar_alpha_end)
                noise = std * torch.randn_like(x)
            case "lower_bound":
                std = torch.sqrt((1 - bar_alpha_start / bar_alpha_end) * (1 - bar_alpha_end) / (1 - bar_alpha_start))
                noise = std * torch.randn_like(x)
            case _:
                raise AssertionError(f"Invalid {self.sigma_type=}.")
        return x + noise

    @torch.no_grad()
    def _sample_common(
        self,
        model: Callable[[Tensor, Tensor], Tensor],
        x: Tensor,
        sampling_timesteps: int | None = None,
        start_percent: float = 0.0,
    ) -> Tensor:
        assert 0.0 <= start_percent <= 1.0

        sampling_timesteps = self.num_timesteps if sampling_timesteps is None else sampling_timesteps
        assert 1 <= sampling_timesteps <= self.num_timesteps

        # Start sampling at `start_percent` instead of at zero.
        num_timesteps = round(self.num_timesteps * (1 - start_percent))
        sampling_timesteps = round(sampling_timesteps * (1 - start_percent))

        subseq = torch.linspace(num_timesteps, 0, sampling_timesteps + 1).round()
        samples = torch.empty((sampling_timesteps + 1, *x.shape), device=x.device)
        samples[-1] = x

        for idx, (t_start, t_end) in enumerate(zip(subseq[:-1], subseq[1:])):
            x = self._sample_step(model, x, t_start, t_end)
            if t_end != 0:
                x = self._add_noise(x, t_start, t_end)
            samples[-1 - idx - 1] = x
        return samples


def plot_schedules(*, num_timesteps: int = 100, output_file: str | Path | None = None) -> None:
    """Plots all of the schedules together on one graph.

    Args:
        num_timesteps: The number of timesteps to plot
        output_file: The file to save the plot to. If ``None``, then the plot
            will be shown instead.
    """
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Please install matplotlib to use this script: `pip install matplotlib`") from e

    # Computes the beta values for each schedule.
    schedules = get_args(DiffusionBetaSchedule)
    ts = torch.arange(num_timesteps)
    betas = torch.empty((len(schedules), num_timesteps))
    stds = torch.empty((len(schedules), num_timesteps - 1))
    for i, schedule in enumerate(schedules):
        betas[i] = beta = get_diffusion_beta_schedule(schedule, num_timesteps=num_timesteps)
        bar_alpha = torch.cumprod(1.0 - beta, dim=0)
        frac = bar_alpha[1:] / bar_alpha[:-1]
        std = torch.sqrt(1 - frac)
        stds[i] = std

    plt.figure(figsize=(8, 12))

    # Plots the Beta schedule values.
    plt.subplot(2, 1, 1)
    for i, schedule in enumerate(schedules):
        plt.plot(ts, betas[i], label=schedule)
    plt.legend()
    plt.title("Betas")
    plt.xlabel("Time")
    plt.ylabel("Beta")
    plt.yscale("log")
    plt.grid(True)

    # Plots the corresponding sigma values.
    plt.subplot(2, 1, 2)
    for i, schedule in enumerate(schedules):
        plt.plot(ts[:-1], stds[i], label=schedule)
    plt.legend()
    plt.title("Standard Deviations")
    plt.xlabel("Time")
    plt.ylabel("Standard Deviation")
    plt.grid(True)

    plt.tight_layout()
    if output_file is None:
        plt.show()
    else:
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_file)


if __name__ == "__main__":
    # python -m ml.tasks.diffusion
    plot_schedules()
