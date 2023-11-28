def dot(v1, v2):
    return sum([ax * bx for ax, bx in zip(v1, v2)])


def col(M, index):
    return [row[index] for row in M]


def array_mult(A, B):
    return [[dot(row, col(B, idx)) for idx in range(len(B[0]))] for row in A]


if __name__ == "__main__":
    M1 = [[1, 2, 3], [-2, 3, 7]]
    M2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    assert col(M1, 1) == [2, 3]

    mult_res = array_mult(M1, M2)
    assert mult_res == [[1, 2, 3], [-2, 3, 7]]

    M3 = [[1], [0], [-1]]
    assert array_mult(M1, M3) == [[-2], [-9]]
