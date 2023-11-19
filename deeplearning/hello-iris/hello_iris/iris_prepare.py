from typing import List, Optional, Tuple, Union
import csv

import numpy as np


def float_or_none(candidate: str) -> Optional[float]:
    try:
        return float(candidate)
    except ValueError:
        return None


def prepare_row(
    data_row: List[str],
) -> Tuple[Union[float, None, str], ...]:
    return tuple(float_or_none(item) for item in data_row[:-1]) + (data_row[-1],)


def load_iris_data(iris_data_file: str) -> np.ndarray:
    with open(iris_data_file, newline="", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return np.array([prepare_row(row) for row in reader])


def prepare_iris_data(iris_data_file: str):
    return load_iris_data(iris_data_file)
