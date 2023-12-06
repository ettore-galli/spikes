import numpy as np
from pytest import approx

from perceptron.perceptron import (
    averaged_perceptron,
    eval_classifier,
    eval_learning_alg,
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


def test_eval_learning_alg():
    data_train = np.array(
        [
            [
                -2.04297103,
                -1.85361169,
                -2.65467827,
                -1.23013149,
                -0.31934782,
                1.33112127,
                2.3297942,
                1.47705445,
                -1.9733787,
                -2.35476882,
            ],
            [
                -2.1071566,
                -3.06450052,
                -3.43898434,
                0.71320285,
                1.51214693,
                4.14295175,
                4.73681233,
                -2.80366981,
                1.56182223,
                0.07061724,
            ],
        ]
    )

    labels_train = np.array([[-1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0]])

    data_test = np.array(
        [
            [
                -4.97193554,
                3.49851995,
                4.00302943,
                0.83369183,
                0.41371989,
                4.37614714,
                1.03536965,
                1.2354608,
                -0.7933465,
                -3.85456759,
            ],
            [
                -0.92053415,
                -3.61953464,
                0.39577344,
                -3.03202474,
                -4.90408303,
                -0.10239158,
                -1.35546287,
                1.31372748,
                -1.97924525,
                -3.72545813,
            ],
        ]
    )
    labels_test = np.array([[-1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]])

    def make_gen_data():
        progress = {"step": 0}

        def gen_data(size):
            _ = size
            gendata = (
                (data_train, labels_train)
                if progress["step"] == 0
                else (data_test, labels_test)
            )

            progress["step"] += 1
            return gendata

        return gen_data

    assert eval_learning_alg(
        learner=perceptron, data_gen=make_gen_data(), n_train=5, n_test=5, it=10
    ) == approx(0.55999999999999994)
