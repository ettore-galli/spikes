from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple
import numpy as np


Dataset = np.ndarray
Features = np.ndarray
Labels = np.ndarray
SampleFeatures = np.ndarray
SampleLabel = float

Hypotesis = Tuple[np.ndarray, float]
Errors = int


@dataclass(frozen=True)
class ClassifierCalculationResult:
    result: float
    labeled_result: float
    is_mistake: bool


@dataclass(frozen=True)
class PerceptronLearningResultError:
    sample: SampleFeatures
    label: SampleLabel


@dataclass(frozen=True)
class PerceptronLearningResult:
    hypotesis: Hypotesis
    errors: List[PerceptronLearningResultError]
    history: List[Hypotesis]

    def has_errors(self) -> bool:
        return len(self.errors) != 0

    def add_loop_results(
        self,
        loop_results: PerceptronLearningResult,
    ) -> PerceptronLearningResult:
        return PerceptronLearningResult(
            hypotesis=loop_results.hypotesis,
            errors=self.errors + loop_results.errors,
            history=self.history + loop_results.history,
        )


def classifier(hypotesis: Hypotesis, test_x: Features) -> np.ndarray:
    theta, theta_0 = hypotesis
    results = np.dot(theta, test_x.T) + theta_0
    labelled_results = np.sign(results)

    return labelled_results


def score(hypotesis: Hypotesis, test_x: Features, test_y: Labels) -> float:
    labelled_results = classifier(hypotesis=hypotesis, test_x=test_x)
    matching = labelled_results == test_y
    return np.count_nonzero(matching) / matching.size


def make_initial_hypotesis(test_x: Features) -> Hypotesis:
    return np.zeros(test_x.shape[1]), 0


def update_classifier(
    hypotesis: Hypotesis, sample: SampleFeatures, label: SampleLabel
) -> Hypotesis:
    theta, theta_0 = hypotesis
    return theta + label * sample, theta_0 + label


def perform_classifier_calculation(
    hypotesis: Hypotesis, sample: SampleFeatures, label: SampleLabel
) -> ClassifierCalculationResult:
    theta, theta_0 = hypotesis

    result = np.dot(theta, sample) + theta_0
    result_for_error = label * result

    return ClassifierCalculationResult(
        result=result, labeled_result=np.sign(result), is_mistake=result_for_error <= 0
    )


def perceptron_data_loop(
    initial_hypotesis: Hypotesis, test_x: Features, test_y: Labels
) -> PerceptronLearningResult:
    hypotesis: Hypotesis = initial_hypotesis
    errors: List[PerceptronLearningResultError] = []
    history: List[Hypotesis] = []

    for sample, label in zip(test_x, test_y):
        classifier_result: ClassifierCalculationResult = perform_classifier_calculation(
            hypotesis=hypotesis, sample=sample, label=label
        )

        if classifier_result.is_mistake:
            hypotesis = update_classifier(
                hypotesis=hypotesis, sample=sample, label=label
            )
            errors.append(PerceptronLearningResultError(sample=sample, label=label))
            history.append(hypotesis)

    return PerceptronLearningResult(hypotesis=hypotesis, errors=errors, history=history)


def perceptron_learning_algorithm(
    test_x: Features, test_y: Labels, tau: int, initial_h: Optional[Hypotesis] = None
) -> PerceptronLearningResult:
    global_hypotesis = (
        make_initial_hypotesis(test_x=test_x) if initial_h is None else initial_h
    )

    global_perceptron_result = PerceptronLearningResult(
        hypotesis=global_hypotesis, errors=[], history=[]
    )

    for _ in range(tau):
        loop_perceptron_result = perceptron_data_loop(
            initial_hypotesis=global_perceptron_result.hypotesis,
            test_x=test_x,
            test_y=test_y,
        )
        global_perceptron_result = global_perceptron_result.add_loop_results(
            loop_results=loop_perceptron_result
        )

        if not loop_perceptron_result.has_errors():
            break

    return global_perceptron_result
