from datetime import datetime, timedelta
import multiprocessing
from random import random
import sys

from challenges.msort.msort import (
    merge_sort,
    merge_sort_mp,
)


def log_timing(name: str, delta: timedelta, pool_size: int):
    print(f"{name.ljust(20)} {str(delta).rjust(20)} pool size: {pool_size}")


def perform_sort_demo(base_size: int, multiprocessing_threshold: int):

    SOURCE = [random() for _ in range(base_size)]

    t0 = datetime.now()

    _ = merge_sort(SOURCE)

    t1 = datetime.now()

    direct_time = t1 - t0

    log_timing("Base implementation", direct_time, 0)

    # --------------------------------------------------

    pool_size = multiprocessing.cpu_count() - 1

    # --------------------------------------------------

    tp0 = datetime.now()

    _ = merge_sort_mp(SOURCE, multiprocessing_threshold)

    tp1 = datetime.now()

    parallel_time = tp1 - tp0

    log_timing("Parallel", parallel_time, pool_size)

    # --------------------------------------------------

    print("Speedup", direct_time / parallel_time)


if __name__ == "__main__":
    base_size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    multiprocessing_threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    perform_sort_demo(
        base_size=base_size, multiprocessing_threshold=multiprocessing_threshold
    )
