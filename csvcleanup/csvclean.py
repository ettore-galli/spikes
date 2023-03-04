import csv
from decimal import Decimal
import functools
from typing import Dict, List, Tuple, Union, Any, Generator, Iterable

NumericType = Union[int, float, Decimal]


def build_data_tuple(record: Dict, fields: List[str]) -> Tuple:
    return tuple(str(record.get(key, "")) for key in fields)


def read_csv_data(input_file: str) -> Generator[Dict, None, None]:
    with open(input_file, encoding="utf-8", newline="\n") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter="|", dialect="unix")
        for row in csv_reader:
            yield row


def find_minimum_distance_versus_data(
    sample: Tuple, current_data: List[Tuple]
) -> Tuple[float, Tuple]:
    if len(current_data) == 0:
        return (0, ())

    def reducer(acc, cur):

        distance = tuple_distance(sample, cur)

        if len(acc) == 0 or distance < acc[0]:
            return (distance, cur)

        return acc

    return functools.reduce(reducer, current_data, ())


def restrict_data_set(
    data_stream: Generator[Dict, None, None],
    relevant_data_fields: List[str],
    distance_threshold: float,
) -> Generator[Dict, None, None]:

    restricted_data_map = {}

    for record in data_stream:

        relevant_data_key = build_data_tuple(record=record, fields=relevant_data_fields)

        if relevant_data_key not in restricted_data_map:

            distance: float
            similar: Tuple
            distance, similar = find_minimum_distance_versus_data(
                relevant_data_key, list(restricted_data_map.keys())
            )
            print(
                record,
                "*" if distance > distance_threshold else "-",
                distance,
                relevant_data_key,
                similar,
            )

            if len(restricted_data_map) == 0 or (distance > distance_threshold):
                restricted_data_map[relevant_data_key] = record
                yield record


def string_distance(candidate: str, reference: str) -> float:
    common_len = min(len(candidate), len(reference))
    base_distance = abs(len(candidate) - len(reference))
    common_distance = sum(
        [
            1 if cmp[0] != cmp[1] else 0
            for cmp in zip(candidate[:common_len], reference[:common_len])
        ]
    )
    return base_distance + common_distance


def number_distance(candidate: NumericType, reference: NumericType) -> float:
    return abs(candidate - reference) / max(abs(candidate), abs(reference))


def is_numeric_couple(couple: Tuple[Any, Any]) -> bool:
    return isinstance(couple[0], NumericType) and isinstance(couple[1], NumericType)


def tuple_distance(candidate: Tuple, reference: Tuple) -> float:
    return (
        sum(
            (
                number_distance(*couple)
                if is_numeric_couple(couple)
                else string_distance(*couple)
            )
            ** 2
            for couple in zip(candidate, reference)
        )
        ** 0.5
    )


if __name__ == "__main__":

    restricted = list(
        restrict_data_set(
            data_stream=read_csv_data(input_file="./data/example1.csv"),
            relevant_data_fields=["a", "b", "c", "d"],
            distance_threshold=3,
        )
    )
    for item in restricted:
        print(item)
