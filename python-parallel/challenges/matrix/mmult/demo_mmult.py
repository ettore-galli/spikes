from datetime import datetime, timedelta
import multiprocessing
from random import random
import sys

from challenges.matrix.mmult.mmult import (
    direct_matrix_multiplication,
    inplace_direct_matrix_multiplication,
    multiprocessing_matrix_multiplication,
    multiprocessing_matrix_multiplication_optimized,
)


def log_timing(name: str, delta: timedelta, pool_size: int):
    print(f"{name.ljust(20)} {str(delta).rjust(20)} pool size: {pool_size}")


def perform_mult_demo(base_size: int):

    A_MATRIX_SIZE = (base_size, base_size)
    B_MATRIX_SIZE = (base_size, base_size)

    A = [[random() for _ in range(A_MATRIX_SIZE[1])] for _ in range(A_MATRIX_SIZE[0])]
    B = [[random() for _ in range(B_MATRIX_SIZE[1])] for _ in range(B_MATRIX_SIZE[0])]

    t0 = datetime.now()

    direct = direct_matrix_multiplication(A, B)

    t1 = datetime.now()

    direct_time = t1 - t0

    log_timing("Direct", direct_time, 0)

    # --------------------------------------------------

    ti0 = datetime.now()

    _ = inplace_direct_matrix_multiplication(A, B)

    ti1 = datetime.now()

    direct_inplace_time = ti1 - ti0

    log_timing("Direct n-place", direct_inplace_time, 0)

    # --------------------------------------------------

    pool_size = multiprocessing.cpu_count()

    tpm0 = datetime.now()
    multi_pool = multiprocessing_matrix_multiplication(
        A, B, pool_size=multiprocessing.cpu_count()
    )
    tpm1 = datetime.now()

    assert multi_pool == direct

    parallel_time_opt = tpm1 - tpm0

    log_timing("Parallel pool", parallel_time_opt, pool_size)

    # --------------------------------------------------

    pool_size = multiprocessing.cpu_count()

    tpo0 = datetime.now()
    multi_optimized = multiprocessing_matrix_multiplication_optimized(
        A, B, pool_size=multiprocessing.cpu_count()
    )
    tp01 = datetime.now()

    assert multi_optimized == direct

    parallel_time_opt = tp01 - tpo0

    log_timing("Parallel optimized", parallel_time_opt, pool_size)


if __name__ == "__main__":
    base_size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    perform_mult_demo(base_size=base_size)
