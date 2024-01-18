from dataclasses import dataclass
from typing import Callable, Optional


Function1D = Callable[[float], float]


@dataclass(frozen=True)
class GDMinimumResult:
    x: float
    y: float
    iterations: int


@dataclass(frozen=True)
class GDMinimumInput:
    fun: Function1D
    fun_derivative: Function1D
    eta: float
    epsilon: float
    x_initial_guess: float
    iteration_callback: Optional[Callable] = None
