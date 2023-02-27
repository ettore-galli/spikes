from datetime import datetime
from random import random
import math
import statistics
from threading import Thread
from time import sleep
from typing import Callable

from dsp_series_2d import show_data_2d, NumericType


def runsTest(l, l_median):

    runs, n1, n2 = 0, 0, 0

    # Checking for start of new run
    for i in range(len(l)):

        # no. of runs
        if (l[i] >= l_median and l[i - 1] < l_median) or (
            l[i] < l_median and l[i - 1] >= l_median
        ):
            runs += 1

        # no. of positive values
        if (l[i]) >= l_median:
            n1 += 1

        # no. of negative values
        else:
            n2 += 1

    runs_exp = ((2 * n1 * n2) / (n1 + n2)) + 1
    stan_dev = math.sqrt(
        (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))
    )

    z = (runs - runs_exp) / stan_dev

    return z


# Making a list of 100 random numbers


class RandomProcess:
    MOD = 1000000
    POWER_MOD = 7

    def __init__(self) -> None:
        self.rand: NumericType = 0
        self.power = 1
        self.is_used: bool = False

    def set_next_number(self):
        rnd_root = datetime.now().microsecond ** (2 + self.power)
        pow_root = rnd_root
        self.current_random_setter(rnd_root % self.MOD, pow_root % self.POWER_MOD)

    def rand_worker(self):
        while True:
            self.set_next_number()

    def current_random_setter(self, rand: NumericType, power: int):
        self.rand = rand
        self.power = power

    def start_random_thread(self):
        r_thread = Thread(target=self.rand_worker, daemon=True)
        r_thread.start()

    def get_current_random(self) -> NumericType:
        if not self.is_used:
            self.set_next_number()
        return self.rand


N = 1024

l1 = []
for i in range(N):
    l1.append(random())

# l = [(i + 1) % (N / 10) + (N / 10) * random() for i in range(N)]

rp = RandomProcess()
rp.start_random_thread()

l2 = [rp.get_current_random() for _ in range(N)]

# l_median = statistics.median(l)
# Z = abs(runsTest(l, l_median))
# print("Z-statistic= ", Z)

show_data_2d(l1)
show_data_2d(l2)
