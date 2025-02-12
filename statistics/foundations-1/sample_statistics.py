import functools
import math
from typing import Dict, List, Tuple

Sample = List[float]


def mean(sample: Sample) -> float:
    return sum(sample) / len(sample) if len(sample) > 0 else 0


def sum_difference_mean(sample: Sample):
    mu = mean(sample=sample)
    return sum([(x - mu) ** 2 for x in sample])


def cross_difference_mean(sample_a: Sample, sample_b: Sample):
    mu_a = mean(sample=sample_a)
    mu_b = mean(sample=sample_b)
    return sum([(xa - mu_a) * (xb - mu_b) for xa, xb in zip(sample_a, sample_b)])


def sample_variance(sample: Sample) -> float:
    N = len(sample)
    return sum_difference_mean(sample=sample) / (N - 1)


def sample_stddev(sample: Sample) -> float:
    return sample_variance(sample) ** 0.5


def variance(sample: Sample) -> float:
    return mean(sample=[x**2 for x in sample]) - mean(sample=sample) ** 2


def confidence_interval(sample: Sample, z_score: float = 1.96) -> Tuple[float, float]:
    sample_mean = mean(sample=sample)
    stddev = sample_stddev(sample=sample)
    sqrt_n = len(sample) ** 0.5
    standard_error = stddev / sqrt_n

    return (
        sample_mean - z_score * standard_error,
        sample_mean + z_score * standard_error,
    )


def sample_cross_correlation(sample_a: Sample, sample_b: Sample) -> float:
    return cross_difference_mean(sample_a=sample_a, sample_b=sample_b) / (
        (sum_difference_mean(sample=sample_a) * sum_difference_mean(sample=sample_b))
        ** 0.5
    )
