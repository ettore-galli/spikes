import numpy as np

from perceptron.perceptron import classifier


def test_classifier():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(h=h1, test_x=data)
    expected = np.array([-1, 1, 1, -1])

    np.testing.assert_array_equal(results, expected)
