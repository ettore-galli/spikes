from typing import Tuple
from sample_statistics import (
    confidence_interval,
    mean,
    sample_cross_correlation,
    sample_stddev,
    sample_variance,
    variance,
)


def test_mean():
    assert mean([2, 3]) == 2.5


def test_variance():
    assert variance([2, 3, 3, 4]) == 0.5


def round_tuple(data: Tuple[float], decimals=2) -> Tuple[float]:
    return tuple(round(item, decimals) for item in data)


def test_sample_variance():
    assert round(sample_variance([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]), 2) == 3.33


def test_sample_stddev():
    assert round(sample_stddev([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]), 2) == 1.83


def test_confidence_interval():
    sample = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]
    ci = confidence_interval(sample=sample)
    assert round_tuple(ci) == (3.01, 4.99)


def test_sample_cross_correlation():
    sample_a = [1, 2, 3]
    sample_b = [1, 1.5, 1.8]
    assert round(sample_cross_correlation(sample_a, sample_b), 4) == 0.9897
    assert round(sample_cross_correlation([0, 1, 2, 3], [0, 9, 18, 27]), 4) == 1.000
