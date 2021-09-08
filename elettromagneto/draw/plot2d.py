def render_2d_ascii(grid) -> str:
    scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # scale = " .:-=+*#%@"
    pots = ""
    for grid_row in grid:
        for value in grid_row:
            render_pot = int((len(scale) - 1) * value)
            pots += str(scale[render_pot])
        pots += "\n"
    return pots


def plot2dascii(values) -> None:
    print(render_2d_ascii(values))


def plot2dmesh(values) -> None:
    import matplotlib.pyplot as plt

    plt.pcolormesh(values)
    plt.show()


def plot2dcontour(values) -> None:
    import matplotlib.pyplot as plt

    plt.contour(values, levels=200)
    plt.show()


def plotquiver(u, v) -> None:
    import matplotlib.pyplot as plt

    plt.quiver(u, v)
    plt.show()

if __name__ == "__main__":
    pass
    """
    import matplotlib.pyplot as plt

    # x axis values
    x = [1, 2, 3]
    # corresponding y axis values
    y = [2, 4, 1]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    plt.pcolormesh([[1,1,2,1,1],
                    [1, 1, 2, 1, 1],
                    [1, 1, 2, 1, 1],
                    [1, 1, 2, 1, 1],
                    [1, 1, 2, 1, 1]
                    ])
    # function to show the plot
    plt.show()
    """
