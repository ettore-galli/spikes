from decimal import Decimal
from typing import List, Tuple

NumericType = float | Decimal


def render_data_point(
    value, data_range: NumericType, data_min: NumericType, scale: List[str]
) -> str:
    scale_index = int((value - data_min) * (len(scale) - 1) / data_range)
    return scale[scale_index]


def block_gray_scale() -> List[str]:
    # U+2591	░	Light shade
    # U+2592	▒	Medium shade
    # U+2593	▓	Dark shade
    # U+2588	█	Full block
    return ["\u2588", "\u2593", "\u2592", "\u2591", " "]


def render_data_2d(
    data: List[float | Decimal], repr_scale: List[str] = block_gray_scale()
) -> Tuple[NumericType, NumericType, List[List[int]]]:
    data_min = min(*data)
    data_max = max(*data)
    data_range = data_max - data_min if data_max > data_min else 1
    data_length = len(data)
    chunk_length = int(data_length**0.5)
    n_chunks = int(len(data) / chunk_length + 1)
    chunks = [data[i * chunk_length : (i + 1) * chunk_length] for i in range(n_chunks)]
    return [
        [render_data_point(value, data_range, data_min, repr_scale) for value in chunk]
        for chunk in chunks
    ]


def show_data_2d(data):
    for row in render_data_2d(data):
        print("".join(col * 2 for col in row))
