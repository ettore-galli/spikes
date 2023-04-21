from typing import Any, Callable, Iterable
from functools import reduce


def join(
    finite_iterable_a: Iterable[Any],
    finite_iterable_b: Iterable[Any],
    join_key_a: Callable[[Any], Any],
    join_key_b: Callable[[Any], Any],
):
    iterable_b_map = reduce(
        lambda acc, cur: {
            **acc,
            **{join_key_b(cur): acc.get(join_key_b(cur), []) + [cur]},
        },
        finite_iterable_b,
        {},
    )

    return [
        {**item_a, **joined_b}
        for item_a in finite_iterable_a
        for joined_b in iterable_b_map.get(join_key_a(item_a), [{}])
    ]


if __name__ == "__main__":
    pass
