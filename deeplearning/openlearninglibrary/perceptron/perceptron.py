from typing import Tuple
import numpy as np


Dataset = np.ndarray
Features = np.ndarray
Labels = np.ndarray


def linear_classifier(x, th, th0):
    return np.sign(np.dot(x, th) + th0)


Hypotesis = Tuple[np.ndarray, float]


def classifier(h: Hypotesis, test_x: Features) -> np.ndarray:
    theta, theta_0 = h
    results = np.dot(theta, test_x.T) + theta_0
    labelled_results = np.sign(results)

    return labelled_results


if __name__ == "__main__":
    pass
