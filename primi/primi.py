import math
from typing import Dict, List, Tuple


def build_prime(m: int, n: int) -> int:
    return 2 * (36 * m**2 + 18 * m + 4 * n**2 + 2 * n + 3) - 1


def mcd_m_n(m: int, n: int) -> int:
    return math.gcd(m, n)


def is_mcd_m_n_one(m: int, n: int) -> bool:
    return mcd_m_n(4 * n + 1, 4 * m + 1) == 1


def is_12_5(p_candidate: int) -> bool:
    return (p_candidate - 5) % 12 == 0


def build_12_5_p(x_value: int):
    return 12 * x_value + 5


def build_m_range(x_value: int) -> Tuple[int, int]:
    # 72* m**2 + 36 * m  - 12*x  = 0
    delta = 36**2 + 4 * 72 * 12 * x_value
    m1 = (-36 - delta**0.5) / (2 * 72)
    m2 = (-36 + delta**0.5) / (2 * 72)
    return (m1, m2)


def hunt_primes(x_range: Tuple[int, int]) -> List[int]:

    candidates: Dict[int, List[Tuple[int, int]]] = {}

    for x_value in range(*x_range):
        p_value = build_12_5_p(x_value)

        for n_value in range(*n_range):

            p_value = build_prime(m=m_value, n=n_value)

            if is_12_5(p_candidate=p_value):
                if p_value not in candidates:
                    candidates[p_value] = []
                candidates[p_value].append((m_value, n_value))

    return [
        (p_candidate, compositions[0])
        for p_candidate, compositions in candidates.items()
        if (
            len(compositions) == 1
            and is_mcd_m_n_one(m=compositions[0][0], n=compositions[0][1])
        )
    ]


if __name__ == "__main__":
    print(build_m_range(30))
    # print(hunt_primes(m_range=(0, 10), n_range=(0, 10)))
