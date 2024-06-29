from typing import Callable
from functools import partial, wraps


def decora(decoranda: Callable[[int, int], int]) -> Callable[[int], int]:
    @wraps(decoranda)
    def decorata(x: int):
        return decoranda(1, x)

    return decorata


@decora
def somma(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    # print(somma(8))
    print(partial(somma, 1)(5))
    # print(decora(somma)(5))
