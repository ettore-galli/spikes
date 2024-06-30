from kink import inject

from dependency_injection.di.di import dependency
from dependency_injection.reader.reader_base import BaseFileReader


def display_file_content(file_reader: BaseFileReader, file: str) -> None:
    for index, row in enumerate(file_reader.read_data(file=file)):
        print(f"* {index}: {row}")


display_file_content_process = dependency.inject_dependencies(display_file_content)

dependency.inject_dependencies(display_file_content)


@inject
def display_file_content_injected(file_reader: BaseFileReader, file: str) -> None:
    for index, row in enumerate(file_reader.read_data(file=file)):
        print(f"- {index}: {row}")
