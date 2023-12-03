import math
import numpy as np


def myfunction(v):
    return math.sin(v[0]) + v[1]


if __name__ == "__main__":
    M = np.array([[0, math.pi / 2, math.pi, 3 * math.pi / 2], [10, 20, 30, 40]])

    result_1 = (lambda v: (1000 * v[0] + v[1]))(M)
    result_2 = np.apply_along_axis(myfunction, 0, M)

    print("\n***** M\n", M, np.shape(M))
    print("\n***** result 1\n", result_1, np.shape(result_1))
    print("\n***** result 2\n", result_2, np.shape(result_2))

