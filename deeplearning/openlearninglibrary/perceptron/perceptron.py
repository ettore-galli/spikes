from typing import Tuple
import numpy as np


Dataset = np.ndarray
Features = np.ndarray
Labels = np.ndarray


Hypotesis = Tuple[np.ndarray, float]


def classifier(h: Hypotesis, test_x: Features) -> np.ndarray:
    theta, theta_0 = h
    results = np.dot(theta, test_x.T) + theta_0
    labelled_results = np.sign(results)

    return labelled_results


def score(h: Hypotesis, test_x: Features, test_y: Labels) -> float:
    labelled_results = classifier(h=h, test_x=test_x)
    matching = labelled_results == test_y
    return np.count_nonzero(matching) / matching.size


if __name__ == "__main__":
    pass
