"""Defines some components for dealing with ordinary differential equations."""

from abc import ABC, abstractmethod
from typing import Callable, Literal, cast, get_args

import torch
from torch import Tensor

ODESolverType = Literal["euler", "heun", "rk4"]


def cast_solver_type(s: str) -> ODESolverType:
    assert s in get_args(ODESolverType), f"Unknown solver {s}"
    return cast(ODESolverType, s)


class BaseODESolver(ABC):
    @abstractmethod
    def step(self, samples: Tensor, t: Tensor, next_t: Tensor, func: Callable[[Tensor, Tensor], Tensor]) -> Tensor:
        """Steps the current state forward in time.

        Args:
            samples: The current samples, with shape ``(*, N)``.
            t: The current time step, with shape ``(N)``.
            next_t: The next time step, with shape ``(N)``.
            func: The function to use to compute the derivative, with signature
                ``(samples, t) -> deriv``.

        Returns:
            The next sample, with shape ``(*, N)``.
        """

    def __call__(self, samples: Tensor, t: Tensor, next_t: Tensor, func: Callable[[Tensor, Tensor], Tensor]) -> Tensor:
        return self.step(samples, t, next_t, func)


class EulerODESolver(BaseODESolver):
    """The Euler method for solving ODEs."""

    @torch.no_grad()
    def step(self, samples: Tensor, t: Tensor, next_t: Tensor, func: Callable[[Tensor, Tensor], Tensor]) -> Tensor:
        dt = next_t - t
        return samples + func(samples, t) * dt.unsqueeze(-1)


class HeunODESolver(BaseODESolver):
    """The Heun method for solving ODEs."""

    @torch.no_grad()
    def step(self, samples: Tensor, t: Tensor, next_t: Tensor, func: Callable[[Tensor, Tensor], Tensor]) -> Tensor:
        dt = next_t - t
        k1 = func(samples, t)
        k2 = func(samples + dt * k1, t + dt)
        return samples + dt.unsqueeze(-1) * (k1 + k2) / 2


class RK4ODESolver(BaseODESolver):
    """The fourth-order Runge-Kutta method for solving ODEs."""

    @torch.no_grad()
    def step(self, samples: Tensor, t: Tensor, next_t: Tensor, func: Callable[[Tensor, Tensor], Tensor]) -> Tensor:
        dt = next_t - t
        k1 = func(samples, t)
        k2 = func(samples + dt * k1 / 2, t + dt / 2)
        k3 = func(samples + dt * k2 / 2, t + dt / 2)
        k4 = func(samples + dt * k3, t + dt)
        return samples + dt.unsqueeze(-1) * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def get_ode_solver(s: ODESolverType) -> BaseODESolver:
    """Returns an ODE solver for a given key.

    Args:
        s: The solver key to retrieve.

    Returns:
        The solver object.
    """
    match s:
        case "euler":
            return EulerODESolver()
        case "heun":
            return HeunODESolver()
        case "rk4":
            return RK4ODESolver()
