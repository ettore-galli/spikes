from typing import List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from iterfun.gradient_descent.gd_base import Function1D


def interval(max_x: float, n_points: int) -> List[float]:
    return [-max_x + 2 * max_x * i / n_points for i in range(n_points)]


def plot_functions(plot_environment: Axes, functions: List[Function1D]):
    number_of_points = 500
    max_x = 5

    x = interval(max_x=max_x, n_points=number_of_points)

    for fun in functions:
        return plot_environment.plot(x, [fun(value) for value in x])


def init_plot_environment() -> Axes:
    plt.ion()

    _, spl = plt.subplots()

    spl.set_title("Gradient descent")
    spl.grid(visible=True)

    return spl


def persist_plot() -> None:
    plt.ioff()
    plt.show()
