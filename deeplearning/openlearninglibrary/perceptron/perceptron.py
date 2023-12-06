from typing import Callable, Tuple, Optional
import numpy as np


Data = np.ndarray
Labels = np.ndarray
Params = dict

Theta = np.ndarray
ThetaZero = float

Hook = Callable[[Theta, ThetaZero], None]


def perceptron(
    data: Data, labels: Labels, params: Params, hook: Optional[Hook] = None
) -> Tuple[np.ndarray, np.ndarray]:
    dimension = data.shape[0]
    theta = np.zeros(dimension)
    theta_0 = 0

    for _ in range(params.get("T", 10)):
        mistakes_happened: bool = False

        for sample, label in zip(data.T, labels.T):
            result = np.dot(theta, sample) + theta_0
            margin = label * result

            if margin <= 0:
                mistakes_happened = True
                theta += label * sample
                theta_0 += label
                if hook:
                    hook(theta, theta_0)

        if not mistakes_happened:
            break

    return theta.reshape((dimension, 1)), np.array([theta_0])


def averaged_perceptron(
    data: Data, labels: Labels, params: Params, hook: Optional[Hook] = None
) -> Tuple[np.ndarray, np.ndarray]:
    dimension = data.shape[0]
    theta = np.zeros(dimension)
    theta_0 = 0
    theta_avg = np.zeros(dimension)
    theta_0_avg = 0
    number_of_runs = 0
    for _ in range(params.get("T", 10)):
        for sample, label in zip(data.T, labels.T):
            result = np.dot(theta, sample) + theta_0
            margin = label * result

            if margin <= 0:
                theta += label * sample
                theta_0 += label
                if hook:
                    hook(theta, theta_0)
            theta_avg += theta
            theta_0_avg += theta_0
            number_of_runs += 1

    return (theta_avg / number_of_runs).reshape((dimension, 1)), np.array(
        [theta_0_avg / number_of_runs]
    )
