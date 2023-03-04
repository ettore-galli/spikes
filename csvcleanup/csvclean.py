import csv
from decimal import Decimal
from typing import Dict, List, Tuple, Union, Any, Generator

NumericType = Union[int, float, Decimal]


def build_data_dict(record: Dict, key_fields: List[str]) -> Tuple:
    return tuple(str(record.get(key, "")) for key in key_fields)


def read_csv_data(input_file: str) -> Generator[Dict, None, None]:
    with open(input_file, encoding="utf-8", newline="\n") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter="|", dialect="unix")
        for row in csv_reader:
            yield row


def restrict_data_set(
    data_stream: Generator[Dict, None, None],
    key_fields: List[str],
    relevant_data_fields: List[str],
) -> Generator[Dict, None, None]:
    for record in data_stream:
        print(record)


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
    return sum(
        number_distance(*couple)
        if is_numeric_couple(couple)
        else string_distance(*couple)
        for couple in zip(candidate, reference)
    )


if __name__ == "__main__":
    restrict_data_set(
        data_stream=read_csv_data(input_file="./data/example1.csv"),
        key_fields=["id"],
        relevant_data_fields=["a", "b", "c"],
    )
