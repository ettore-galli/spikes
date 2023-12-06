import numpy as np
from pytest import approx

from perceptron.perceptron import (
    averaged_perceptron,
    eval_classifier,
    perceptron,
    Data,
    Labels,
    Params,
    Hook,
    Theta,
    ThetaZero,
)


def plot_classifier(theta: Theta, theta_0=ThetaZero):
    print(theta, theta_0)


def test_perceptron():
    data: Data = np.array([[2, 3, 9, 12], [5, 1, 6, 5]])
    labels: Labels = np.array([[1, -1, 1, -1]])
    params: Params = {"T": 100}
    hook: Hook = plot_classifier
    classifier = perceptron(data=data, labels=labels, params=params, hook=hook)

    print([x.tolist() for x in classifier])

    np.array_equal(classifier[0], np.array([-9.0, 18.0]))
    assert classifier[1] == approx(2.0)


def test_averaged_perceptron():
    data: Data = np.array([[2, 3, 9, 12], [5, 1, 6, 5]])
    labels: Labels = np.array([[1, -1, 1, -1]])
    params: Params = {"T": 100}
    hook: Hook = plot_classifier
    classifier = averaged_perceptron(data=data, labels=labels, params=params, hook=hook)

    print([x.tolist() for x in classifier])

    np.array_equal(classifier[0], np.array([-9.0, 18.0]))
    assert classifier[1] == approx(1.9425)


def test_eval_classifier():
    data_train: Data = np.array([[2, 3, 9, 12], [5, 1, 6, 5]])
    labels_train: Labels = np.array([[1, -1, 1, -1]])
    data_test: Data = np.array([[2, 3, 9, 12], [5, 1, 6, 5]])
    labels_test: Labels = np.array([[1, -1, 1, 1]])

    assert eval_classifier(
        learner=perceptron,
        data_train=data_train,
        labels_train=labels_train,
        data_test=data_test,
        labels_test=labels_test,
    ) == approx(0.75)
