import numpy as np
from pytest import approx


from perceptron.perceptron_1 import (
    ClassifierCalculationResult,
    classifier,
    make_initial_hypotesis,
    perceptron_data_loop,
    perceptron_learning_algorithm,
    perform_classifier_calculation,
    score,
    update_classifier,
)


def test_classifier():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(hypotesis=h1, test_x=data)
    expected = np.array([-1, 1, 1, -1])

    np.testing.assert_array_equal(results, expected)


def test_classifier_single_sample():
    data = np.array([1, 3])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    results = classifier(hypotesis=h1, test_x=data)
    expected = -1

    np.testing.assert_array_equal(results, expected)


def test_score():
    data = np.array([[1, 3], [1, 1], [5, 4], [6, 7]])
    labels = np.array([1, 1, -1, -1])

    th = np.array([1, -1])
    th0 = 0.9

    h1 = (th, th0)

    result = score(hypotesis=h1, test_x=data, test_y=labels)
    expected = 0.5
    assert result == approx(expected)


def test_make_initial_hypotesis():
    assert make_initial_hypotesis(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    ) == (approx(np.array([0, 0, 0])), approx(0))


def test_update_classifier():
    assert update_classifier(
        hypotesis=(np.array([0, 0]), 0), sample=np.array([-1, 1]), label=1
    ) == (approx(np.array([-1, 1])), approx(1))


def test_perform_classifier_calculation():
    assert perform_classifier_calculation(
        hypotesis=(np.array([1, 2]), 10), sample=np.array([3, 4]), label=1
    ) == ClassifierCalculationResult(result=21, labeled_result=1, is_mistake=False)
    assert perform_classifier_calculation(
        hypotesis=(np.array([1, 2]), 10), sample=np.array([3, 4]), label=-1
    ) == ClassifierCalculationResult(result=21, labeled_result=1, is_mistake=True)


def test_perceptron_data_loop():
    data = np.array([[1, 1], [0, 1], [-1.5, 1]])
    labels = np.array([1, -1, 1])
    hypotesis_ini = (np.array([0, 0]), 0)

    hypotesis, errors, _ = perceptron_data_loop(
        initial_hypotesis=hypotesis_ini, test_x=data, test_y=labels
    )
    expected = (np.array([-0.5, 1]), 0)

    assert errors == 3

    np.testing.assert_array_equal(hypotesis[0], expected[0])


def test_perceptron_learning_algorithm():
    data = np.array([[1, -1], [0, 1], [-1.5, -1]])
    labels = np.array([1, -1, 1])

    hypotesis, errors, history = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected = (np.array([-0.5, -2]), 0)

    assert errors == 2
    np.testing.assert_array_equal(hypotesis[0], expected[0])

    want_history = [
        np.array([1.0, -1.0]),
        np.array([-0.5, -2.0]),
    ]
    got_history = [item[0] for item in history]
    for got, want in zip(got_history, want_history):
        np.testing.assert_array_equal(got, want)


def test_perceptron_learning_algorithm_case_2():
    data = np.array([[0, 1], [-1.5, -1], [1, -1]])
    labels = np.array([-1, 1, 1])

    hypotesis, errors, history = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected = (np.array([0, -1.0]), 0)

    assert errors == 1
    np.testing.assert_array_equal(hypotesis[0], expected[0])

    want_history = [
        np.array([0, -1.0]),
    ]
    got_history = [item[0] for item in history]

    for got, want in zip(got_history, want_history):
        np.testing.assert_array_equal(got, want)


def test_perceptron_learning_algorithm_case_3():
    data = np.array([[1, -1], [0, 1], [-10, -1]])
    labels = np.array([1, -1, 1])

    hypotesis, errors, history = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected = (np.array([-0.5, -2]), 0)

    assert errors == 6

    got_history = [item[0] for item in history]
    print(got_history)
    np.testing.assert_array_equal(hypotesis[0], expected[0])

    want_history = [
        np.array([1.0, -1.0]),
        np.array([-9.0, -2.0]),
        np.array([-8.0, -3.0]),
        np.array([-7.0, -4.0]),
        np.array([-6.0, -5.0]),
        np.array([-5.0, -6.0]),
    ]

    for got, want in zip(got_history, want_history):
        np.testing.assert_array_equal(got, want)


def test_perceptron_learning_algorithm_case_4():
    data = np.array([[0, 1], [-10, -1], [1, -1]])
    labels = np.array([-1, 1, 1])

    hypotesis, errors, history = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected = (np.array([0.0, -1.0]), 0)

    assert errors == 1

    got_history = [item[0] for item in history]
    print(got_history)
    np.testing.assert_array_equal(hypotesis[0], expected[0])

    want_history = [
        np.array([0.0, -1.0]),
    ]

    for got, want in zip(got_history, want_history):
        np.testing.assert_array_equal(got, want)


def test_perceptron_learning_algorithm_case_5():
    data = np.array([[1, -1], [0, 1], [-1.5, -1]])
    labels = np.array([1, -1, 1])

    hypotesis, errors, history = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=1000, initial_h=(np.array([0, -2]), 0)
    )
    expected = (np.array([0, -2]), 0)

    assert errors == 0

    got_history = [item[0] for item in history]
    print(got_history)
    np.testing.assert_array_equal(hypotesis[0], expected[0])
