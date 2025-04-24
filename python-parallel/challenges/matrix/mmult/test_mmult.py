from pytest import mark
from challenges.matrix.mmult.mmult import (
    Matrix,
    direct_matrix_multiplication,
    extract_matrix_rows,
    extract_matrix_columns,
    multiprocessing_matrix_multiplication,
    perform_dot_product,
)


def test_extract_rows():
    matrix: Matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0, 0, 1],
    ]

    assert extract_matrix_rows(matrix) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0, 0, 1],
    ]


def test_extract_matrix_columns():
    matrix: Matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0, 9, 1],
    ]

    assert extract_matrix_columns(matrix) == [[1, 4, 7, 0], [2, 5, 8, 9], [3, 6, 9, 1]]


def test_perform_dot_product():
    assert perform_dot_product([1, 2, 3], [2, 2, 1]) == 9


MULTIPLICATION_TEST_CASES = [
    (
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
        [
            [1, 2],
            [1, 2],
            [1, 2],
        ],
        [
            [6, 12],
            [15, 30],
        ],
    ),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100],
            [110, 120, 130, 140, 150],
            [160, 170, 180, 190, 200],
        ],
        [
            [1100, 1200, 1300, 1400, 1500],
            [2460, 2720, 2980, 3240, 3500],
            [3820, 4240, 4660, 5080, 5500],
        ],
    ),
]


@mark.parametrize(["matrix_a", "matrix_b", "product"], MULTIPLICATION_TEST_CASES)
def test_direct_matrix_multiplication(matrix_a, matrix_b, product):
    assert direct_matrix_multiplication(matrix_a, matrix_b) == product


@mark.parametrize(["matrix_a", "matrix_b", "product"], MULTIPLICATION_TEST_CASES)
def test_multiprocessing_matrix_multiplication(matrix_a, matrix_b, product):
    assert multiprocessing_matrix_multiplication(matrix_a, matrix_b) == product
