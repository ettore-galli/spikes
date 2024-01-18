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


def parabola(value: float) -> float:
    return value**2 - 2


def parabolad1(value: float) -> float:
    return 2 * value


def gd_minimum(gd_minimum_input: GDMinimumInput) -> GDMinimumResult:
    x = gd_minimum_input.x_initial_guess
    iterations = 0
    while True:
        iterations += 1

        deri = gd_minimum_input.fun_derivative(x)
        x -= gd_minimum_input.eta * deri

        if gd_minimum_input.iteration_callback:
            gd_minimum_input.iteration_callback(x, deri, iterations)

        if deri < gd_minimum_input.epsilon:
            break

    return GDMinimumResult(x, gd_minimum_input.fun(x), iterations)
