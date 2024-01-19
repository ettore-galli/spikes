from functools import partial

import matplotlib.pyplot as plt

from iterfun.gradient_descent.gd_base import GDMinimumInput

from iterfun.gradient_descent.gd_calc import (
    gd_minimum,
    parabola,
    parabolad1,
)
from iterfun.gradient_descent.gd_plot import (
    GDPlotEnvironment,
)


def print_iteration_data(x, dy_dx, iterations) -> None:
    print(f"It. {iterations}\t: x: {x:.5f}\t  dy/dx: {dy_dx:.5f}")


def iteration_callback(plot_environment: GDPlotEnvironment, x, dy_dx, iterations):
    print_iteration_data(x, dy_dx, iterations)

    def line_through_point(m, xp, yp, x):
        return m * (x - xp) + yp

    tangent = partial(line_through_point, dy_dx, x, parabola(x))

    plot_environment.plot_functions([tangent])

    plt.pause(0.3)


if __name__ == "__main__":
    plot_env = GDPlotEnvironment()
    plot_env.plot_functions([parabola])

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
