import pytest

from csvclean import string_distance, tuple_distance, number_distance


@pytest.mark.parametrize(
    "candidate, reference, expected_distance",
    [
        ("mela", "pera", 2),
        ("bana", "banana", 2),
        ("mela", "pippo", 5),
        ("giovannino", "giovannina", 1),
    ],
)
def test_string_distance(candidate, reference, expected_distance):
    assert string_distance(candidate, reference) == expected_distance


@pytest.mark.parametrize(
    "candidate, reference, expected_distance",
    [
        (17, 34, 0.5),
        (17, 18, 0.05555555555555555),
    ],
)
def test_number_distance(candidate, reference, expected_distance):
    assert number_distance(candidate, reference) == expected_distance


@pytest.mark.parametrize(
    "candidate, reference, expected_distance",
    [
        ((17, "aa"), (34, "ab"), 1.5),
    ],
)
def test_tuple_distance(candidate, reference, expected_distance):
    assert tuple_distance(candidate, reference) == expected_distance
