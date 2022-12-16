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


max_iters: int = 200
bailout: float = 1.3

mandelbrot = [
    [iterations(0.04 * x, 0.04 * y, max_iters, bailout) for x in range(-50, 30)]
    for y in range(-30, 30)
]

rendered = [[str(int(9 * value / max_iters)) for value in line] for line in mandelbrot]

for line in rendered:
    print("".join(line))
