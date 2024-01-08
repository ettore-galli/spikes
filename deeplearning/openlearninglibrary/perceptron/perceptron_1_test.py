import numpy as np
from pytest import approx


from perceptron.perceptron_1 import (
    ClassifierCalculationResult,
    PerceptronLearningResult,
    PerceptronLearningResultError,
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

    learning_result = perceptron_data_loop(
        initial_hypotesis=hypotesis_ini, test_x=data, test_y=labels
    )

    expected_learning_result = PerceptronLearningResult(
        hypotesis=(np.array([-0.5, 1]), 1),
        errors=[
            PerceptronLearningResultError(sample=np.array([1.0, 1.0]), label=1),
            PerceptronLearningResultError(sample=np.array([0.0, 1.0]), label=-1),
            PerceptronLearningResultError(sample=np.array([-1.5, 1.0]), label=1),
        ],
        history=[
            (np.array([1.0, 1.0]), 1),
            (np.array([1.0, 0.0]), 0),
            (np.array([-0.5, 1.0]), 1),
        ],
    )

    np.testing.assert_array_equal(
        learning_result.hypotesis[0], expected_learning_result.hypotesis[0]
    )
    assert learning_result.hypotesis[1] == expected_learning_result.hypotesis[1]

    assert len(learning_result.errors) == len(expected_learning_result.errors)

    for res, exp in zip(learning_result.history, expected_learning_result.history):
        np.testing.assert_array_equal(res[0], exp[0])
        np.testing.assert_array_equal(res[1], exp[1])


def test_perceptron_learning_algorithm():
    data = np.array([[1, -1], [0, 1], [-1.5, -1]])
    labels = np.array([1, -1, 1])

    perceptron_result = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10
    )
    expected_classifier = (np.array([1, -2]), 0)

    assert len(perceptron_result.errors) == 2
    np.testing.assert_array_equal(
        perceptron_result.hypotesis[0], expected_classifier[0]
    )
    np.testing.assert_array_equal(
        perceptron_result.hypotesis[1], expected_classifier[1]
    )
    print(perceptron_result.history)
    want_history = [
        (np.array([1.0, -1.0]), 1),
        (np.array([1, -2.0]), 0),
    ]
    got_history = perceptron_result.history
    for got, want in zip(got_history, want_history):
        np.testing.assert_array_equal(got[0], want[0])
        np.testing.assert_array_equal(got[1], want[1])


def test_perceptron_3_1():
    data = np.array([[-3, 2], [-1, 1], [-1, -1], [2, 2], [1, -1]])
    labels = np.array([1, -1, -1, -1, -1])

    perceptron_result = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=100
    )

    print("----- errors -----")
    for error in perceptron_result.errors:
        print(error)

    print("----- classifier -----")
    print(perceptron_result.hypotesis)

    expected_classifier = (np.array([-2.0, 0.0]), -5)

    np.testing.assert_array_equal(
        perceptron_result.hypotesis[0], expected_classifier[0]
    )
    np.testing.assert_array_equal(
        perceptron_result.hypotesis[1], expected_classifier[1]
    )


def print_results(results: PerceptronLearningResult, label: str):
    print(f"\n===== {label} =====")
    print("----- errors:")
    for error in results.errors:
        print(error)
    print("----- history:")
    for step in results.history:
        print(step)
    print("----- classifier:")
    print(results.hypotesis)


def test_perceptron_and():
    data = np.array(
        [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ]
    )
    labels = np.array([-1, -1, -1, -1, -1, -1, -1, 1])

    perceptron_result = perceptron_learning_algorithm(
        test_x=data, test_y=labels, tau=10000
    )

    print_results(perceptron_result, "results 1")

    expected_classifier = (np.array([4.0, 3.0, 2.0]), -8)

    np.testing.assert_array_equal(
        perceptron_result.hypotesis[0], expected_classifier[0]
    )
    np.testing.assert_array_equal(
        perceptron_result.hypotesis[1], expected_classifier[1]
    )
