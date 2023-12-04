import numpy as np
from pytest import approx


from perceptron.perceptron import (
    classifier,
    initial_hypotesis,
    perceptron_data_loop,
    perceptron_learning_algorithm,
    score,
    update_classifier,
)


def test_classifier():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(h=h1, test_x=data)
    expected = np.array([-1, 1, 1, -1])

    np.testing.assert_array_equal(results, expected)


def test_classifier_single_sample():
    data = np.array([1, 3])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(h=h1, test_x=data)
    expected = -1

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


def test_initial_hypotesis():
    assert initial_hypotesis(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    ) == (approx(np.array([0, 0, 0])), approx(0))


def test_update_classifier():
    assert update_classifier(
        h=(np.array([0, 0]), 0), test_x=np.array([-1, 1]), test_y=1
    ) == (approx(np.array([-1, 1])), approx(0))


def test_perceptron_data_loop():
    data = np.array([[1, 1], [0, 1], [-1.5, 1]])
    labels = np.array([1, -1, 1])
    hypotesis_ini = (np.array([0, 0]), 0)

    hypotesis, errors = perceptron_data_loop(
        hypotesis=hypotesis_ini, test_x=data, test_y=labels
    )
    expected = (np.array([-0.5, 1]), 0)

    assert errors == 3
    np.testing.assert_array_equal(hypotesis[0], expected[0])


def test_perceptron_learning_algorithm():
    data = np.array([[1, -1], [0, 1], [-1.5, -1]])
    labels = np.array([1, -1, 1])

    hypotesis, errors = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected = (np.array([-0.5, -2]), 0)

    assert errors == 2
    np.testing.assert_array_equal(hypotesis[0], expected[0])
