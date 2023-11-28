from typing import List, Tuple, Union
import numpy as np

RawDataFormat = List[List[Union[int, float]]]
RawSeparatorsFormat = List[Tuple[List[Union[int, float]], Union[int, float]]]

FeaturesFormat = np.ndarray
TargetFormat = np.ndarray
ThetasFormat = np.ndarray
ThetaZerosFormat = np.ndarray


def best_separator_2(data, labels, ths, th0s):
    scores = np.sum(
        np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1, keepdims=True
    )
    maxscore = np.argmax(scores)

    return np.array([ths[:, maxscore]]).T, np.array([th0s])[:, maxscore : maxscore + 1]


def prepare_input(
    raw_data: RawDataFormat,
) -> Tuple[FeaturesFormat, TargetFormat]:
    return (
        np.array([item[:-1] for item in raw_data]),
        np.array([item[-1:] for item in raw_data]),
    )


def prepare_separators(
    raw_separators: RawSeparatorsFormat,
) -> Tuple[ThetasFormat, ThetaZerosFormat]:
    return (
        np.array([item[0] for item in raw_separators]),
        np.array([np.array([item[1]]) for item in raw_separators]),
    )


def debug_shapes(
    data: np.ndarray, labels: np.ndarray, ths: np.ndarray, th0s: np.ndarray
):
    return [
        f"data    : {np.shape(data)}",
        f"labels  : {np.shape(labels)}",
        f"ths     : {np.shape(ths)}",
        f"th0s    : {np.shape(th0s)}",
    ]


def print_rows(rows: List[str]):
    for row in rows:
        print(row)


def best_separator(data, labels, ths, th0s):
    scores = np.sum(
        np.sign(np.dot(ths, data.T) + th0s) == labels.T, axis=1, keepdims=True
    )
    maxscore = np.argmax(scores)

    return ths[maxscore], th0s[maxscore]


if __name__ == "__main__":
    raw_data: RawDataFormat = [
        [1, 2, -1],
        [1, 3, -1],
        [5, 1, 1],
        [1, -1, 1],
        [2, -1, 1],
    ]

    data, labels = prepare_input(raw_data=raw_data)

    raw_separators: RawSeparatorsFormat = [
        ([1, 1], 10),
        ([2, 2], 9),
        ([3, 3], 8),
        ([4, -4], 7),
        ([5, -5], 6),
        ([6.65, -6.2564], 5.234),
        ([7, -7], 4),
        ([8, -1], 3),
        ([9, -1], 2),
        ([10, -1], 1),
    ]

    ths, th0s = prepare_separators(raw_separators=raw_separators)

    print_rows(debug_shapes(data=data, labels=labels, ths=ths, th0s=th0s))

    print("----- data")
    print(repr(data))
    print("----- labels")
    print(repr(labels))
    print("----- ths")
    print(repr(ths))
    print("----- th0s")
    print(repr(th0s))

    print(best_separator(data, labels, ths, th0s))
