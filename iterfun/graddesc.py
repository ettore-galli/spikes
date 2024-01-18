from functools import partial
from threading import Thread
from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

from dataclasses import dataclass
from typing import Callable, List, Optional


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
    iteration_callback: Optional[Callable] = None,
) -> GDMinimumResult:
    x = x_initial_guess
    iterations = 0
    while True:
        iterations += 1
        deri = fun_derivative(x)
        x -= eta * deri
        if iteration_callback:
            iteration_callback(x, deri, iterations)
        if deri < epsilon:
            break
    return GDMinimumResult(x, fun(x), iterations)


def interval(max_x: float, n_points: int) -> List[float]:
    return [-max_x + 2 * max_x * i / n_points for i in range(n_points)]


def iteration_callback(plot_environment: Axes, x, dy_dx, iterations):
    import time

    print(x, dy_dx, iterations)

    def line_through_point(m, xp, yp, x):
        return m * (x - xp) + yp

    tangent = partial(line_through_point, dy_dx, x, parabola(x))

    plot_functions(plot_environment, [parabola, parabolad1, tangent])

    plt.pause(0.3)


def plot_functions(plot_environment: Axes, functions: List[Function1D]):
    N = 500
    max_x = 5

    x = interval(max_x=max_x, n_points=N)

    for fun in functions:
        plot_environment.plot(x, [fun(value) for value in x])


def init_plot_environment() -> Axes:
    plt.ion()

    _, spl = plt.subplots()

    spl.set_title("Gradient descent")
    spl.grid(visible=True)

    return spl


def persist_plot() -> None:
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    plot_environment = init_plot_environment()

    result = gd_minimum(
        fun=parabola,
        fun_derivative=parabolad1,
        eta=0.1,
        epsilon=0.3,
        x_initial_guess=4,
        iteration_callback=partial(iteration_callback, plot_environment),
    )
    persist_plot()
    print(result)
