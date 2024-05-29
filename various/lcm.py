import functools
import itertools
import math
from typing import Dict


def factors(n):
    return [2] + list(range(3, n, 2))


def is_prime(n):
    return all(n % d != 0 for d in factors(n) if d < n)


def first_primes(n):
    return [candidate for candidate in factors(n) if is_prime(candidate)]


def accumulate(residual: int, factors: Dict, factor: int):
    def add_factor(factors: Dict, factor: int):
        return (
            {**factors, **{factor: 1}}
            if factor not in factors
            else {**factors, **{factor: factors[factor] + 1}}
        )

     
    partial = (
        (
            residual // factor,
            add_factor(factors, factor),
        )
        if residual % factor == 0
        else (residual, factors)
    )
    print(partial, factor)



    return functools.reduce(

    )


def decompose(n):
    return list(
        functools.reduce(
            lambda cur, factor: accumulate(cur[0], cur[1], factor),
            first_primes(n),
            (n, {}),
        ),
    )


def lcm(n):
    return functools.reduce(
        lambda factors, curfactors: (
            factors + [cf for cf in curfactors if cf not in factors]
        ),
        [decompose(k) for k in range(1, n + 1)],
        [],
    )


def main():
    # print(is_prime(12), is_prime(13))
    # print(first_primes(12))
    # for n in [2, 3, 12]:
    #     print(f"decompose {n}, {decompose(n)}")
    # print(lcm(12))
    print(math.lcm(*list(range(1,13))))


if __name__ == "__main__":
    main()
