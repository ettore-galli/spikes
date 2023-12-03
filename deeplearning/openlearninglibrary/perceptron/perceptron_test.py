import numpy as np
from pytest import approx

from perceptron.perceptron import classifier, score


def test_classifier():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(h=h1, test_x=data)
    expected = np.array([-1, 1, 1, -1])

    np.testing.assert_array_equal(results, expected)


def test_score():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])
    labels = np.array([1, 1, -1, -1])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    result = score(h=h1, test_x=data, test_y=labels)
    expected = 0.5
    assert result == approx(expected)
