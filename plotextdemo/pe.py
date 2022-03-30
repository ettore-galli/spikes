# https://github.com/piccolomo/plotext

def p1():
    import plotext as plt

    y = plt.sin()  # sinusoidal signal
    plt.scatter(y)
    plt.title("Scatter Plot")
    plt.show()


def p2():
    import plotext as plt

    cols, rows = 200, 45
    p = 1
    matrix = [
        [(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)]
        for r in range(rows)
    ]

    plt.matrix_plot(matrix)
    plt.plotsize(cols, rows)
    plt.title("Matrix Plot")
    plt.show()


def p3():
    import plotext as plt

    path = plt.file.join_paths(plt.file.script_folder(), "foto.jpg")

    size = [100, 30]
    size = plt.image_plot(path, size=size, keep_ratio=True)

    plt.plotsize(*size)
    plt.title("Mona Lisa")
    plt.show()


if __name__ == "__main__":
    p3()
