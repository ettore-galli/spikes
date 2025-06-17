import sys
from typing import Callable, Tuple

STANDARD_DELTA = 100 * sys.float_info.min


def solve_dicotomic_monotonically_increasing(
    function: Callable[[float], float],
    target: float,
    x_domain: Tuple[float, float],
    delta: float = STANDARD_DELTA,
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


def solve_dicotomic_monotonically_decreasing(
    function: Callable[[float], float],
    target: float,
    x_domain: Tuple[float, float],
    delta: float = STANDARD_DELTA,
):
    return solve_dicotomic_monotonically_increasing(
        function=lambda x: -function(x),
        target=-target,
        x_domain=x_domain,
        delta=delta,
    )
