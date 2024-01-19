from typing import List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from iterfun.gradient_descent.gd_base import Function1D


def interval(max_x: float, n_points: int) -> List[float]:
    return [-max_x + 2 * max_x * i / n_points for i in range(n_points)]


class GDPlotEnvironment:
    def __init__(self) -> None:
        self.plot_environment: Axes = self.init_plot_environment()
        self.currrent_function_plot = None

    def plot_functions(self, functions: List[Function1D], domain):
        for fun in functions:
            return self.plot_environment.plot(domain, [fun(value) for value in domain])

    def plot_replace_functions(self, functions: List[Function1D], domain):
        if self.currrent_function_plot is not None:
            for item in self.currrent_function_plot:
                item.remove()
        self.currrent_function_plot = self.plot_functions(
            functions=functions, domain=domain
        )

    def init_plot_environment(self) -> Axes:
        plt.ion()

        _, spl = plt.subplots()

        spl.set_title("Gradient descent")
        spl.grid(visible=True)

        return spl

    def persist_plot(self) -> None:
        plt.ioff()
        plt.show()
