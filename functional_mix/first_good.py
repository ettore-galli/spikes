from decimal import Decimal
from functools import reduce
from typing import Callable, Dict, Iterable, List, Optional, Type, TypeVar, cast


U = TypeVar("U")
V = TypeVar("V")


def evaluate_when(
    func: Callable[[U], V],
    iterable: Iterable[U],
    item_process_pred: Callable[[U], bool],
    result_process_pred: Callable[[V], bool],
    default: V,
) -> V:

    for item in iterable:
        if item_process_pred(item):
            result: V = func(item)
            if result_process_pred(result):
                return result

    return default


def get_first_good(elements: List[int]) -> Optional[Decimal]:
    x: Optional[Decimal] = None

    for element in elements:
        if element % 2 == 0:
            x = Decimal("3.14") * Decimal(element)

    return x


def get_first_good_fun(elements: List[int]) -> Optional[Decimal]:
    return evaluate_when(
        func=lambda cur: Decimal("3.14") * Decimal(cur),
        iterable=elements,
        item_process_pred=lambda cur: cur % 2 == 0,
        result_process_pred=lambda _: True,
        default=0.01,
    )


def get_first_good_fun_2(elements: List[int]) -> Optional[Decimal]:
    return evaluate_when(
        func=lambda cur: {1: Decimal("3.14") * Decimal(cur["A"])},
        iterable=elements,
        item_process_pred=lambda cur: cur["A"] % 2 == 0,
        result_process_pred=lambda _: True,
        default=0.01,
    )


if __name__ == "__main__":
    print(get_first_good([1, 2, 3]))
    print(get_first_good_fun([1, 2, 3]))
    print(get_first_good_fun_2([{"A": 1}, {"A": 2}, {"A": 3}]))
