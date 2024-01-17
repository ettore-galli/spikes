import numpy as np


def row_average_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (m,1) array where each entry is the average of a row
    """
    avg = np.average(x, axis=1)
    return avg.reshape(avg.shape[0], 1)


def col_average_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (n,1) array where each entry is the average of a column
    """
    avg = np.average(x, axis=0)
    return avg.reshape(avg.shape[0], 1)


import numpy as np


def top_bottom_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (2,1) array where the first entry is the average of the
    top half of the image = rows 0 to floor(m/2) [exclusive]
    and the second entry is the average of the bottom half of the image
    = rows floor(m/2) [inclusive] to m
    """
    m = x.shape[0]
    top = np.average(x[: int(m / 2)])
    bottom = np.average(x[int(m / 2) :])
    return np.array([[top, bottom]]).reshape(2, 1)


def use_row_average_features():
    data = np.array([[1, 2, 3], [3, 9, 2]])
    print(row_average_features(data))
    print(col_average_features(data))
    data = np.array([[1, 2, 3], [3, 9, 2], [2, 1, 9]])
    print(top_bottom_features(data))


if __name__ == "__main__":
    use_row_average_features()
