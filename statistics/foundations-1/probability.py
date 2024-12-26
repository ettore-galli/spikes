import functools
import math
from typing import Dict, List, Tuple


def permutazioni(n):
    return math.factorial(n)


def permutazioni_x_n(x, n):
    return math.factorial(n) / math.factorial(n - x)


def combinazioni(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def factorial_range(n: int) -> Dict[int, int]:
    return {term: 1 for term in range(1, n + 1)}


def combine_powers(terms: List[Dict[int, int]]) -> Dict[int, int]:
    if len(terms) < 2:
        return terms
    if len(terms) == 2:
        return {
            **{
                base: (exp + terms[0].get(base, 0))
                for base, exp in terms[1].items()
                if base in terms[0]
            },
            **{base: exp for base, exp in terms[0].items() if base not in terms[1]},
            **{base: exp for base, exp in terms[1].items() if base not in terms[0]},
        }
    return combine_powers([terms[0], combine_powers(terms[1:])])


# def multi_factorial_fraction(multiplers: List[int], dividers: List[int]) -> float:

#     multipliers_terms = [factorial_range(n) for n in multiplers]

#     dividers_terms = [factorial_range(n) for n in dividers]
