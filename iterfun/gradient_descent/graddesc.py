from functools import partial
from typing import List

import matplotlib.pyplot as plt

from iterfun.gradient_descent.gd_base import GDMinimumInput

from iterfun.gradient_descent.gd_calc import (
    gd_minimum,
    parabola,
    parabolad1,
)
from iterfun.gradient_descent.gd_plot import (
    GDPlotEnvironment,
    interval,
)


def print_iteration_data(x, dy_dx, iterations) -> None:
    print(f"It. {iterations}\t: x: {x:.5f}\t  dy/dx: {dy_dx:.5f}")


def build_plot_domain() -> List[float]:
    number_of_points = 500
    max_x = 5
    return interval(max_x=max_x, n_points=number_of_points)


def iteration_callback(plot_environment: GDPlotEnvironment, x, dy_dx, iterations):
    print_iteration_data(x, dy_dx, iterations)

    def line_through_point(m, xp, yp, x):
        return m * (x - xp) + yp

    tangent = partial(line_through_point, dy_dx, x, parabola(x))

    plot_environment.plot_replace_functions([tangent], build_plot_domain())

    plt.pause(0.3)


if __name__ == "__main__":
    plot_env = GDPlotEnvironment()
    plot_env.plot_functions([parabola], build_plot_domain())

    result = gd_minimum(
        gd_minimum_input=GDMinimumInput(
            fun=parabola,
            fun_derivative=parabolad1,
            eta=0.1,
            epsilon=0.1,
            x_initial_guess=4,
            iteration_callback=partial(iteration_callback, plot_env),
        )
    )
    plot_env.persist_plot()
    print(result)
