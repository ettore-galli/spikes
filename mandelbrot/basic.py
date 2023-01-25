def in_set(cx, cy, iters=1000):

    value = (0, 0)
    for _ in range(iters):
        x, y = value
        value = (x**2 - y**2 + cx, 2 * x * y + cy)
        if value[0] ** 2 + value[1] ** 2 > 10:
            return False
    return True


mandelbrot = [
    ["*" if in_set(0.04 * x, 0.04 * y) else " " for x in range(-50, 30)]
    for y in range(-30, 30)
]

for line in mandelbrot:
    print("".join(line))
