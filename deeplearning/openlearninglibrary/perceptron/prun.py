# pylint: skip-file
# flake8: noqa
# type: ignore
from perceptron import (
    averaged_perceptron,
    eval_learning_alg,
    eval_learning_alg_same,
)
from hw2code import (
    gen_flipped_lin_separable,
)


def case_1():
    attempts = 10
    num_points = 50
    n_test = num_points // 2
    n_train = num_points - n_test
    datagen = gen_flipped_lin_separable(num_points=num_points, pflip=0.25)
    scores = []
    for _ in range(attempts):
        scores.append(
            eval_learning_alg(
                learner=averaged_perceptron,
                data_gen=datagen,
                n_train=n_train,
                n_test=n_test,
                it=10,
            )
        )
    score = sum(scores) / len(scores)
    print(score)


def case_2():
    attempts = 100
    num_points = 20

    datagen = gen_flipped_lin_separable(num_points=num_points, pflip=0.25)
    scores = []

    for i in range(attempts):
        scores.append(
            eval_learning_alg_same(
                learner=averaged_perceptron,
                data_gen=datagen,
                n_data=num_points,
                it=10,
            )
        )
        score = sum(scores) / len(scores)
        print(f"Attempt {i + 1}: score = {scores[-1]}; avg={score}")
    print(score)


if __name__ == "__main__":
    print("----- HW2 -----")
    case_2()
