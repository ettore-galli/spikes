import math
import functools


def gamma_integrand(t, z):
    return t ** (z - 1) * math.exp(-t)


def gamma(z, dt=0.001, infinity=100000):
    return functools.reduce(
        lambda acc, cur: acc + gamma_integrand(t=cur * dt, z=z) * dt, range(infinity), 0
    )


if __name__ == "__main__":
    print(gamma(6))
