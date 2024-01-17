import itertools
import functools
import operator
from typing import Any
import numpy as np
from code_for_hw3_part1 import *
import code_for_hw3_part2 as hw3


def rv(value_list):
    return np.array([value_list])


def cv(value_list):
    return np.transpose(rv(value_list))


def mul(seq):
    return functools.reduce(operator.mul, seq, 1)


def str_mul(seq):
    return functools.reduce(lambda acc, cur: f"{acc}{cur}" if acc else cur, seq, "")


# Perceptron algorithm with offset.
# data is dimension d by n
# labels is dimension 1 by n
# T is a positive integer number of steps to run
def perceptron(data, labels, params={}, hook=None):
    # if T not in params, default to 100
    T = params.get("T", 50)
    (d, n) = data.shape

    theta = np.zeros((d, 1))
    theta_0 = np.zeros((1, 1))
    for t in range(T):
        for i in range(n):
            x = data[:, i : i + 1]
            y = labels[:, i : i + 1]
            if y * positive(x, theta, theta_0) <= 0.0:
                theta = theta + y * x
                theta_0 = theta_0 + y
                if hook:
                    hook((theta, theta_0))
    return theta, theta_0


def averaged_perceptron(data, labels, params={}, hook=None):
    T = params.get("T", 100)
    (d, n) = data.shape

    theta = np.zeros((d, 1))
    theta_0 = np.zeros((1, 1))
    theta_sum = theta.copy()
    theta_0_sum = theta_0.copy()
    for _ in range(T):
        for i in range(n):
            x = data[:, i : i + 1]
            y = labels[:, i : i + 1]
            if y * positive(x, theta, theta_0) <= 0.0:
                theta = theta + y * x
                theta_0 = theta_0 + y
                if hook:
                    hook((theta, theta_0))
            theta_sum = theta_sum + theta
            theta_0_sum = theta_0_sum + theta_0
    theta_avg = theta_sum / (T * n)
    theta_0_avg = theta_0_sum / (T * n)
    if hook:
        hook((theta_avg, theta_0_avg))
    return theta_avg, theta_0_avg


def eval_classifier(learner, data_train, labels_train, data_test, labels_test):
    th, th0 = learner(data_train, labels_train)
    return score(data_test, labels_test, th, th0) / data_test.shape[1]


def positive(x, th, th0):
    return np.sign(th.T @ x + th0)


def score(data, labels, th, th0):
    return np.sum(positive(data, th, th0) == labels)


def make_polynomial_feature_fun(order, multiplier_aggregator):
    # raw_features is d by n
    # return is k by n where k = sum_{i = 0}^order  multichoose(d, i)
    def f(raw_features):
        d, n = raw_features.shape
        result = []  # list of column vectors
        for j in range(n):
            features = []
            for o in range(order + 1):
                index_tuples = itertools.combinations_with_replacement(range(d), o)
                for it in index_tuples:
                    features.append(
                        multiplier_aggregator(raw_features[i, j] for i in it)
                    )
            result.append(cv(features))
        return np.hstack(result)

    return f


def test_linear_classifier_with_features(
    dataFun, learner, feature_fun, draw=True, refresh=True, pause=True, iterations=100
):
    raw_data, labels = dataFun()
    data = feature_fun(raw_data) if feature_fun else raw_data
    if draw:

        def hook(params):
            ax = plot_data(raw_data, labels)  # create plot axis on each iteration
            (th, th0) = params
            predictor = lambda x1, x2: int(positive(feature_fun(cv([x1, x2])), th, th0))
            plot_nonlin_sep(predictor, ax=ax)
            plot_data(raw_data, labels, ax)
            plt.show()  # force plot to push to the colab notebook and be displayed
            print("th", th.T, "th0", th0)
            if pause:
                input("press enter here to continue:")

    else:
        hook = None
    th, th0 = learner(data, labels, hook=hook, params={"T": iterations})
    if hook:
        hook((th, th0))
    final_score = int(score(data, labels, th, th0))

    samples = raw_data.shape[1]
    print("Final score", final_score)
    print(f"Final score %: {final_score} / {samples} =  {100.0*final_score/samples} %")
    print("Params", np.transpose(th), th0)


def test_with_features(dataFun, order=2, draw=True, pause=True, iterations=100):
    test_linear_classifier_with_features(
        dataFun,  # data
        perceptron,  # learner
        make_polynomial_feature_fun(
            order=order, multiplier_aggregator=mul
        ),  # feature maker
        draw=draw,
        pause=pause,
        iterations=iterations,
    )


def test_with_features_exercise():
    test_with_features(
        dataFun=xor_more,
        order=3,
        draw=False,
        pause=True,
        iterations=10000,
    )


def auto_data_exercise():
    auto_data = hw3.load_auto_data(path_data="./data/auto-mpg.tsv")
    features_a = [
        ("cylinders", hw3.raw),
        ("displacement", hw3.raw),
        ("horsepower", hw3.raw),
        ("weight", hw3.raw),
        ("acceleration", hw3.raw),
        ("origin", hw3.raw),
    ]
    features_b = [
        ("cylinders", hw3.one_hot),
        ("displacement", hw3.standard),
        ("horsepower", hw3.standard),
        ("weight", hw3.standard),
        ("acceleration", hw3.standard),
        ("origin", hw3.one_hot),
    ]

    # ---------
    T = 10
    features_used = features_b

    # ---------
    def learner_perceptron(
        data: Any, labels: Any, params: Any = {"T": T}, hook: Any | None = None
    ):
        return perceptron(data=data, labels=labels, params=params, hook=hook)

    def learner_averaged_perceptron(
        data: Any, labels: Any, params: Any = {"T": T}, hook: Any | None = None
    ):
        return averaged_perceptron(data=data, labels=labels, params=params, hook=hook)

    data, labels = hw3.auto_data_and_labels(auto_data=auto_data, features=features_used)

    results = [
        hw3.xval_learning_alg(learner=learner, data=data, labels=labels, k=10)
        for learner in [learner_perceptron, learner_averaged_perceptron]
    ]
    print(results)
    print("~" * 70)

    data_b, labels_b = hw3.auto_data_and_labels(
        auto_data=auto_data, features=features_b
    )

    classifier = averaged_perceptron(
        data=data_b, labels=labels_b, hook=None, params={"T": 1}
    )
    for row in range(data_b.shape[0]):
        print(data_b[row][:6])

    print(classifier)


if __name__ == "__main__":
    auto_data_exercise()
