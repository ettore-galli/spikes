from typing import Type
from depencency_injection.reader.reader_base import BaseFileReader


def display_file_content(file_reader: Type[BaseFileReader], file: str) -> None:
    for index, row in enumerate(file_reader().read_data(file=file)):
        print(f"{index}: {row}")
