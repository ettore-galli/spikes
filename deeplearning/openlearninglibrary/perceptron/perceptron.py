from typing import Tuple
import numpy as np


Dataset = np.ndarray
Features = np.ndarray
Labels = np.ndarray
SampleFeatures = np.ndarray
SampleLabel = float

Hypotesis = Tuple[np.ndarray, float]
Errors = int


def classifier(h: Hypotesis, test_x: Features) -> np.ndarray:
    theta, theta_0 = h
    results = np.dot(theta, test_x.T) + theta_0
    labelled_results = np.sign(results)

    return labelled_results


def score(h: Hypotesis, test_x: Features, test_y: Labels) -> float:
    labelled_results = classifier(h=h, test_x=test_x)
    matching = labelled_results == test_y
    return np.count_nonzero(matching) / matching.size


def initial_hypotesis(test_x: Features) -> Hypotesis:
    return np.zeros(test_x.shape[1]), 0


def update_classifier(
    h: Hypotesis, test_x: SampleFeatures, test_y: SampleLabel
) -> Hypotesis:
    theta, theta_0 = h
    return theta + test_y * test_x, theta_0


def perceptron_data_loop(
    hypotesis: Hypotesis, test_x: Features, test_y: Labels
) -> Tuple[Hypotesis, Errors]:
    errors = 0
    for sample, label in zip(test_x, test_y):
        result = classifier(h=hypotesis, test_x=sample)
        print("prec", hypotesis)
        if label * result <= 0:
            hypotesis = update_classifier(h=hypotesis, test_x=sample, test_y=label)
            errors += 1
        print("post", hypotesis)
    return hypotesis, errors


def perceptron_learning_algorithm(
    test_x: Features, test_y: Labels, tau: int
) -> Tuple[Hypotesis, Errors]:
    hypotesis = initial_hypotesis(test_x=test_x)

    global_errors = 0

    for _ in range(tau):
        hypotesis, errors = perceptron_data_loop(
            hypotesis=hypotesis, test_x=test_x, test_y=test_y
        )
        global_errors += errors

        if errors == 0:
            break

    return hypotesis, global_errors


if __name__ == "__main__":
    pass
