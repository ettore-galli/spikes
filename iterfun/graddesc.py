from dataclasses import dataclass
from typing import Callable


Function1D = Callable[[float], float]


@dataclass(frozen=True)
class GDMinimumResult:
    x: float
    y: float
    iterations: int


def parabola(value: float) -> float:
    return value**2 - 2


def parabolad1(value: float) -> float:
    return 2 * value


def gd_minimum(
    fun: Function1D,
    fun_derivative: Function1D,
    eta: float,
    epsilon: float,
    x_initial_guess: float,
) -> GDMinimumResult:
    x = x_initial_guess
    iterations = 0
    while True:
        iterations += 1
        deri = fun_derivative(x)
        x -= eta * deri
        if deri < epsilon:
            break
    return GDMinimumResult(x, fun(x), iterations)


if __name__ == "__main__":
    result = gd_minimum(
        fun=parabola,
        fun_derivative=parabolad1,
        eta=0.1,
        epsilon=0.0000001,
        x_initial_guess=4,
    )
    print(result)
