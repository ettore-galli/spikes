from dataclasses import dataclass
from typing import Any, Callable, Iterable, Optional

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


def test_join_classes():
    @dataclass
    class AClass:
        a: int
        x: str

    @dataclass
    class BClass:
        a: int
        z: str

    @dataclass
    class JoinedClass:
        a: int
        x: Optional[str]
        z: Optional[str]

    finite_iterable_a: Iterable[Any] = [
        AClass(1, "aaa"),
        AClass(2, "bbb"),
        AClass(3, "ccc"),
    ]
    finite_iterable_b: Iterable[Any] = [
        BClass(1, "qqqqqq"),
        BClass(3, "wwwwww"),
        BClass(4, "eeeeee"),
    ]
    join_key_a: Callable[[Any], Any] = lambda item: item.a
    join_key_b: Callable[[Any], Any] = lambda item: item.a

    def combineAB(item_a: AClass, item_b: Optional[BClass]) -> JoinedClass:
        return (
            JoinedClass(item_a.a, item_a.x, item_b.z)
            if item_b
            else JoinedClass(item_a.a, item_a.x, None)
        )

    expected_join: Iterable[Any] = [
        JoinedClass(1, "aaa", "qqqqqq"),
        JoinedClass(2, "bbb", None),
        JoinedClass(3, "ccc", "wwwwww"),
    ]

    assert (
        join(
            finite_iterable_a,
            finite_iterable_b,
            join_key_a,
            join_key_b,
            combiner=combineAB,
        )
        == expected_join
    )
