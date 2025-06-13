from typing import Callable, Tuple


def solve_dicotomic_monotonically_increasing(
    function: Callable[[float], float],
    target: float,
    x_domain: Tuple[float, float],
    delta: float = 0.001,
):
    bottom, top = x_domain

    ascissa = (top + bottom) / 2
    value = function(ascissa)

    while abs(value - target) > delta:
        ascissa = (top + bottom) / 2
        value = function(ascissa)

        if value < target:
            bottom = ascissa
        else:
            top = ascissa

    return ascissa
