from ctypes import c_double
import multiprocessing
from typing import Any, List


MatrixRow = List[float]
MatrixColumn = List[float]
Matrix = List[MatrixRow]


class ArraySizeMismatch(Exception): ...


def extract_matrix_rows(matrix: Matrix) -> List[MatrixRow]:
    return [row for row in matrix]


def extract_matrix_columns(matrix: Matrix) -> List[MatrixColumn]:
    return [[row[index] for row in matrix] for index in range(len(matrix[0]))]


def perform_dot_product(row: MatrixRow, column: MatrixColumn) -> float:
    return sum(
        [
            row_element * column_element
            for row_element, column_element in zip(row, column)
        ]
    )


def direct_matrix_multiplication(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    return [
        [
            sum(
                [
                    row_element * column_element
                    for row_element, column_element in zip(row, column)
                ]
            )
            for column in extract_matrix_columns(matrix_b)
        ]
        for row in extract_matrix_rows(matrix_a)
    ]


def inplace_direct_matrix_multiplication(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    matrix_a_rows = len(matrix_a)
    matrix_a_cols = len(matrix_a[0])
    matrix_b_cols = len(matrix_b[0])

    result = [[0.0] * matrix_b_cols for _ in range(matrix_a_rows)]

    for a_row_id in range(matrix_a_rows):
        for b_col_id in range(matrix_b_cols):
            for a_col_id in range(matrix_a_cols):
                result[a_row_id][b_col_id] += (
                    matrix_a[a_row_id][a_col_id] * matrix_b[a_col_id][b_col_id]
                )

    return result


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


def split_into_chunks(iterable: List[Any], chunk_size: int) -> List[List[Any]]:
    return [
        iterable[k * chunk_size : (k + 1) * chunk_size]
        for k in range(1 + len(iterable) // chunk_size)
        if k * chunk_size < len(iterable)
    ]


def direct_matrix_multiplication_to_array(
    matrix_a: Matrix,
    matrix_b: Matrix,
    result_row_index: int,
    result_array,
) -> None:

    result_cols = len(matrix_b[0])
    for row_id, row in enumerate(extract_matrix_rows(matrix_a)):
        for col_id, column in enumerate(extract_matrix_columns(matrix_b)):
            result_array[result_row_index + row_id * result_cols + col_id] = sum(
                [
                    row_element * column_element
                    for row_element, column_element in zip(row, column)
                ]
            )


def multiprocessing_matrix_multiplication_optimized(
    matrix_a: Matrix, matrix_b: Matrix, pool_size: int = 10
) -> Matrix:

    result = []
    result_rows = len(matrix_a)
    result_cols = len(matrix_b[0])

    result_array = multiprocessing.RawArray(c_double, result_rows * result_cols)

    processes = []

    chunk_size = 1 + len(matrix_a) // pool_size

    for chunk_index, chunk in enumerate(split_into_chunks(matrix_a, chunk_size)):
        result_row_index = chunk_index * chunk_size * result_cols
        processes.append(
            multiprocessing.Process(
                target=direct_matrix_multiplication_to_array,
                args=(chunk, matrix_b, result_row_index, result_array),
            )
        )

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    for r in range(0, result_rows):
        result.append(result_array[r * result_cols : (r + 1) * result_cols])

    return result
