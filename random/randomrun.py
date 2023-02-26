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
    NOISE_MOD = 31

    def __init__(self) -> None:
        self.rand: NumericType = 0
        self.noise: int = 0

    def rand_worker(self, current_random_setter: Callable[[NumericType], None]):
        while True:
            self.set_noise()
            current_random_setter(random())

    def set_noise(self):
        self.noise = (self.noise + self.rand) % self.NOISE_MOD

    def current_random_setter(self, rnd: NumericType):
        self.rand = rnd
        self.set_noise()

    def start_random_thread(self):
        r_thread = Thread(
            target=self.rand_worker, args=[self.current_random_setter], daemon=True
        )
        r_thread.start()

    def get_current_random(self) -> NumericType:
        return self.rand * (self.noise + 1) / self.NOISE_MOD


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
