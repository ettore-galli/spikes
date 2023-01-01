from functools import partial
from typing import Tuple


def modulo(cx: float, cy: float):
    return (cx**2 + cy**2) ** 0.5


def iteration_formula(x: float, y: float, cx: float, cy: float) -> Tuple[float, float]:
    return (x**2 - y**2 + cx, 2 * x * y + cy)


def iterations(cx: float, cy: float, max_iters: int, bailout: float) -> int:

    value = (0, 0)

    for iterations in range(max_iters):

        value = iteration_formula(*value, cx, cy)

        if modulo(*value) > bailout:
            return iterations

    return max_iters


def render_num_iters(max_iters: int, iterations: int) -> str:
    return str(int(9 * iterations / max_iters))


def render_on_off(max_iters: int, iterations: int) -> str:
    return "*" if iterations / max_iters > 0.9 else " "


def render_scale(max_iters: int, iterations: int) -> str:
    grayscale = "@%#*+=."
    scale_grade = int((len(grayscale) - 1) * iterations / max_iters)
    return grayscale[::-1][scale_grade]


min_x = -60
max_x = 30
min_y = -30
max_y = 30

max_iters: int = 1000
bailout: float = 7

render_pixel = partial(render_scale, max_iters)

mandelbrot = [
    [iterations(0.04 * x, 0.04 * y, max_iters, bailout) for x in range(min_x, max_x)]
    for y in range(min_y, max_y)
]

rendered = [[render_pixel(value) for value in line] for line in mandelbrot]

for line in rendered:
    print("".join(line))
