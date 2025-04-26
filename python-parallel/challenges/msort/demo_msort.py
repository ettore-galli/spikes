from datetime import datetime, timedelta
import multiprocessing
from random import random
import sys

from challenges.msort.msort import (
    merge_sort,
)


def log_timing(name: str, delta: timedelta, pool_size: int):
    print(f"{name.ljust(20)} {str(delta).rjust(20)} pool size: {pool_size}")


def perform_sort_demo(base_size: int):

    SOURCE = [random() for _ in range(base_size)]

    t0 = datetime.now()

    _ = merge_sort(SOURCE)

    t1 = datetime.now()

    direct_time = t1 - t0

    log_timing("Base implementation", direct_time, 0)

    # --------------------------------------------------

    pool_size = multiprocessing.cpu_count() - 1

    # --------------------------------------------------

    # tp0 = datetime.now()
    # tp1 = datetime.now()

    parallel_time = direct_time
    log_timing("Parallel optimized", parallel_time, pool_size)

    # --------------------------------------------------

    print("Speedup", direct_time / parallel_time)


if __name__ == "__main__":
    base_size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    perform_sort_demo(base_size=base_size)
