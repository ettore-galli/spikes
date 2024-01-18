from functools import partial

from iterfun.gradient_descent.gd_base import GDMinimumInput

from iterfun.gradient_descent.gd_calc import (
    gd_minimum,
    parabola,
    parabolad1,
)
from iterfun.gradient_descent.gd_plot import (
    init_plot_environment,
    iteration_callback,
    persist_plot,
)


if __name__ == "__main__":
    plot_env = init_plot_environment()

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
    persist_plot()
    print(result)
