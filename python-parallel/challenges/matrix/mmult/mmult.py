import multiprocessing
from typing import List


MatrixRow = List[float]
MatrixColumn = List[float]
Matrix = List[MatrixRow]


class ArraySizeMismatch(Exception): ...


def extract_matrix_rows(matrix: Matrix) -> List[MatrixRow]:
    return [row for row in matrix]


def extract_matrix_columns(matrix: Matrix) -> List[MatrixColumn]:
    return [[row[index] for row in matrix] for index in range(len(matrix[0]))]


def perform_dot_product(row: MatrixRow, column: MatrixColumn):
    return sum(
        [
            row_element * column_element
            for row_element, column_element in zip(row, column)
        ]
    )


def direct_matrix_multiplication(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    return [
        [
            perform_dot_product(row, column)
            for column in extract_matrix_columns(matrix_b)
        ]
        for row in extract_matrix_rows(matrix_a)
    ]


def multiprocessing_matrix_multiplication(
    matrix_a: Matrix, matrix_b: Matrix, pool_size: int = 10
) -> Matrix:

    with multiprocessing.Pool(processes=pool_size) as pool:

        return [
            pool.starmap(
                perform_dot_product,
                ([(row, column) for column in extract_matrix_columns(matrix_b)]),
            )
            for row in extract_matrix_rows(matrix_a)
        ]
