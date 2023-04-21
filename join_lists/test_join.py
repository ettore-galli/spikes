from typing import Any, Callable, Iterable

from join_lists.join import join


def test_join():
    finite_iterable_a: Iterable[Any] = [
        {"A": 1, "X": "aaa"},
        {"A": 2, "X": "bbb"},
        {"A": 3, "X": "ccc"},
    ]
    finite_iterable_b: Iterable[Any] = [
        {"A": 1, "Z": "qqqqqq"},
        {"A": 3, "Z": "wwwwww"},
        {"A": 4, "Z": "eeeeee"},
    ]
    join_key_a: Callable[[Any], Any] = lambda item: item.get("A")
    join_key_b: Callable[[Any], Any] = lambda item: item.get("A")

    expected_join: Iterable[Any] = [
        {"A": 1, "X": "aaa", "Z": "qqqqqq"},
        {"A": 2, "X": "bbb"},
        {"A": 3, "X": "ccc", "Z": "wwwwww"},
    ]

    assert (
        join(finite_iterable_a, finite_iterable_b, join_key_a, join_key_b)
        == expected_join
    )
