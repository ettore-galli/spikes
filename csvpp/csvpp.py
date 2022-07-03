import csv
import sys
from typing import Any, Iterable, List, Optional


def read_csv_content(input_file: str) -> List[List[str]]:
    with open(input_file, newline="") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        csv_reader = csv.reader(csvfile, dialect=dialect)
        return [row for row in csv_reader]


def calculate_column_widths(data: List[List[str]]) -> List[int]:
    return [max(len(item) for item in column) for column in list(zip(*data))]


def is_numeric(item: Any) -> bool:
    try:
        float(item)
        return True
    except ValueError:
        return False


def infer_if_data_is_numeric(data: List[List[str]]) -> List[bool]:
    return [
        all(
            is_numeric(item)
            for item in column[1:]
            if item is not None and len(str(item).strip()) > 0
        )
        for column in list(zip(*data))
    ]


def render_line_item(item: Any, length: int, is_numeric: bool) -> str:
    return str(item).rjust(length, " ") if is_numeric else str(item).ljust(length, " ")


def render_csv_line(
    row: List[Any], column_widths: List[int], column_is_numeric: List[bool]
):
    return [
        render_line_item(str(item), length, is_numeric)
        for item, length, is_numeric in zip(row, column_widths, column_is_numeric)
    ]


def render_pretty_print(input_file: str, column_separator="|") -> Iterable[List[str]]:
    csv_content = read_csv_content(input_file=input_file)
    column_widths = calculate_column_widths(data=csv_content)
    column_is_numeric = infer_if_data_is_numeric(data=csv_content)
    for line in csv_content:
        yield column_separator.join(
            render_csv_line(line, column_widths, column_is_numeric)
        )


def show_pretty_print(input_file: str) -> None:
    for line in render_pretty_print(input_file=input_file):
        print(line)


if __name__ == "__main__":
    input_file = sys.argv[1]
    show_pretty_print(input_file)
