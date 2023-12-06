import numpy as np
from pytest import approx

from perceptron.perceptron import (
    averaged_perceptron,
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
