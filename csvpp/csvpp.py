import csv
import sys
from typing import Any, Iterable, List


def read_csv_content(input_file: str) -> List[List[str]]:
    with open(input_file, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        return [row for row in csv_reader]


def calculate_column_widths(data: List[List[str]]) -> List[int]:
    return [max(len(item) for item in column) for column in list(zip(*data))]


def render_csv_line(row: List[Any], column_widths: List[int]):
    return [str(item).ljust(length, " ") for item, length in zip(row, column_widths)]


def render_pretty_print(input_file: str, column_separator="|") -> Iterable[List[str]]:
    csv_content = read_csv_content(input_file=input_file)
    column_widths = calculate_column_widths(data=csv_content)

    for line in read_csv_content(input_file=input_file):
        yield column_separator.join(render_csv_line(line, column_widths))


def show_pretty_print(input_file: str) -> None:
    for line in render_pretty_print(input_file=input_file):
        print(line)


if __name__ == "__main__":
    input_file = sys.argv[1]
    show_pretty_print(input_file)
