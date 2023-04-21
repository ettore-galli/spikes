from typing import Any, Callable, Dict, Iterable, List, Optional
from functools import reduce


def dict_combiner(item_a: Dict, item_b: Optional[Dict]) -> Dict:
    return {**item_a, **item_b} if item_b else item_a


def join(
    finite_iterable_a: Iterable[Any],
    finite_iterable_b: Iterable[Any],
    join_key_a: Callable[[Any], Any],
    join_key_b: Callable[[Any], Any],
    combiner: Callable[[Any, Optional[Any]], Any] = dict_combiner,
    null_b: Any = {},
) -> List[Any]:
    iterable_b_map: Dict[Any, Any] = reduce(
        lambda acc, cur: {
            **acc,
            **{join_key_b(cur): acc.get(join_key_b(cur), []) + [cur]},
        },
        finite_iterable_b,
        {},
    )

    return [
        combiner(item_a, item_b)
        for item_a in finite_iterable_a
        for item_b in iterable_b_map.get(join_key_a(item_a), [null_b])
    ]


if __name__ == "__main__":
    pass
