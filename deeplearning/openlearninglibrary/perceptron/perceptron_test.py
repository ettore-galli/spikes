import numpy as np

from perceptron.perceptron import (
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
    data: Data = np.array([[1, 1, 2, 2], [-1, 1, -1, 1]])
    labels: Labels = np.array(
        [
            1,
            1,
            -1,
            -1,
        ]
    )
    params: Params = {"T": 100000}
    hook: Hook = plot_classifier
    classifier = perceptron(data=data, labels=labels, params=params, hook=hook)
    np.array_equal(classifier[0], np.array([-3, 4, 0]))
