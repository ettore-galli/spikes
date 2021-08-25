from typing import List


def ascii_plot_2d(values: List[List[float]]) -> None:
    pass


def plot2dmesh(values) -> None:
    import matplotlib.pyplot as plt
    # plt.pcolormesh(values)
    # plt.pcolor(values)
    plt.contour(values, levels=200)
    plt.show()


if __name__ == '__main__':
    pass
    '''
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
    '''
