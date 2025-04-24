from datetime import datetime
from random import random

from challenges.matrix.mmult.mmult import (
    Matrix,
    direct_matrix_multiplication,
    multiprocessing_matrix_multiplication,
)


def perform_mult_demo():
    A_MATRIX_SIZE = (500, 500)
    B_MATRIX_SIZE = (500, 500)

    A = [
        [int(1000 * random()) for _ in range(A_MATRIX_SIZE[1])]
        for _ in range(A_MATRIX_SIZE[0])
    ]
    B = [
        [int(1000 * random()) for _ in range(B_MATRIX_SIZE[1])]
        for _ in range(B_MATRIX_SIZE[0])
    ]

    t0 = datetime.now()

    a_times_b_direct = direct_matrix_multiplication(A, B)

    t1 = datetime.now()

    a_times_b_parallel = multiprocessing_matrix_multiplication(A, B)

    t2 = datetime.now()

    direct_time = t1 - t0
    parallel_time = t2 - t1

    print(f"Direct   : {direct_time}")
    print(f"Parallel : {parallel_time}")


if __name__ == "__main__":
    perform_mult_demo()
