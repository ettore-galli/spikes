from dependency_injection.di.di import dependency
from dependency_injection.reader.reader_base import BaseFileReader


@dependency.inject_dependencies
def display_file_content(file_reader: BaseFileReader, file: str) -> None:
    for index, row in enumerate(file_reader.read_data(file=file)):
        print(f"{index}: {row}")
