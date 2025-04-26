from random import randint
from typing import List
from pytest import mark

from challenges.msort.msort import ListElement, merge_sort


@mark.parametrize(
    ["unsorted", "expected_sorted"],
    [
        ([3, 6, 4, 1, 9], [1, 3, 4, 6, 9]),
        (
            [
                2,
                22,
                17,
                25,
                7,
                20,
                5,
                16,
                29,
                5,
                22,
                26,
                5,
                26,
                13,
                28,
                8,
                16,
                6,
                7,
                23,
                16,
                30,
                6,
                6,
                29,
                1,
                26,
                24,
                24,
            ],
            [
                1,
                2,
                5,
                5,
                5,
                6,
                6,
                6,
                7,
                7,
                8,
                13,
                16,
                16,
                16,
                17,
                20,
                22,
                22,
                23,
                24,
                24,
                25,
                26,
                26,
                26,
                28,
                29,
                29,
                30,
            ],
        ),
    ],
)
def test_merge_sort(unsorted, expected_sorted):
    assert merge_sort(unsorted) == expected_sorted


def test_merge_sort_extended():
    size = 100
    unsorted: List[ListElement] = [int(randint(1, size)) for _ in range(size)]
    expected_sorted = sorted(unsorted)
    assert merge_sort(unsorted) == expected_sorted
