from typing import Callable, Tuple
import numpy as np


Data = np.ndarray
Labels = np.ndarray
Params = dict

Theta = np.ndarray
ThetaZero = float

Hook = Callable[[Theta, ThetaZero], None]


def perceptron(
    data: Data, labels: Labels, params: Params, hook: Hook
) -> Tuple[Theta, ThetaZero]:
    theta = np.zeros(data.shape[0])
    theta_0 = 0

    for _ in range(params.get("T", 10)):
        mistakes_happened: bool = False

        for sample, label in zip(data.T, labels):
            result = np.dot(theta, sample) + theta_0
            margin = label * result

            if margin <= 0:
                mistakes_happened = True
                theta += label * sample
                theta_0 += label
                hook(theta, theta_0)

        if not mistakes_happened:
            break

    return theta, theta_0
