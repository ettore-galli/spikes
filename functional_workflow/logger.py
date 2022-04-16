from typing import Generator


def read_input(input_file_name: str) -> Generator[str, None, None]:
    with open(input_file_name, 'r') as input_file:
        yield input_file.readline()
