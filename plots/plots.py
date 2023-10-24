import math
from typing import Iterable, List
import matplotlib.pyplot as plt


def sine(samples: int, freq: float, amplitude=1):
    return [
        amplitude * math.sin(freq * 2 * math.pi * (i / samples)) for i in range(samples)
    ]


def combine(waves: List[Iterable[float]]):
    return [sum(values_tuple) for values_tuple in zip(*waves)]


def plots():
    N = 1000
    H = 2
    harmonics = [
        sine(samples=N, freq=2 * n + 1, amplitude=1 / (2 * n + 1)) for n in range(H)
    ]
    wave = combine(harmonics)
    for harmonic in harmonics:
        plt.plot(harmonic, color="lightgray")
    plt.plot(wave, color='black')
    plt.ylabel("Wave")
    plt.show()


if __name__ == "__main__":
    plots()
