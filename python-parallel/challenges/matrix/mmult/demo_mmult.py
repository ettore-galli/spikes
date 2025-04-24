from datetime import datetime
from random import random

from challenges.matrix.mmult.mmult import (
    direct_matrix_multiplication,
    inplace_direct_matrix_multiplication,
    multiprocessing_matrix_multiplication,
)


def perform_mult_demo():
    BASE_SIZE = 100
    A_MATRIX_SIZE = (BASE_SIZE, BASE_SIZE)
    B_MATRIX_SIZE = (BASE_SIZE, BASE_SIZE)

    A = [[random() for _ in range(A_MATRIX_SIZE[1])] for _ in range(A_MATRIX_SIZE[0])]
    B = [[random() for _ in range(B_MATRIX_SIZE[1])] for _ in range(B_MATRIX_SIZE[0])]

    t0 = datetime.now()

    a_times_b_direct = direct_matrix_multiplication(A, B)

    t1 = datetime.now()

    direct_time = t1 - t0

    print(f"Direct           : {direct_time}")

    ti0 = datetime.now()

    a_times_b_direct_inplace = inplace_direct_matrix_multiplication(A, B)

    ti1 = datetime.now()

    direct_inplace_time = ti1 - ti0

    print(f"Direct in-place  : {direct_inplace_time}")

    for i in range(1, BASE_SIZE, int(BASE_SIZE / 20)):

        pool_size = int(BASE_SIZE / i)

        tp0 = datetime.now()
        a_times_b_parallel = multiprocessing_matrix_multiplication(
            A, B, pool_size=pool_size
        )

        tp1 = datetime.now()

        parallel_time = tp1 - tp0

        assert a_times_b_direct == a_times_b_parallel
        assert a_times_b_direct == a_times_b_direct_inplace

        print(f"Parallel : {parallel_time} [pool_size = {pool_size}]")


if __name__ == "__main__":
    perform_mult_demo()
