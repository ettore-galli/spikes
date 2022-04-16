from typing import List, Optional


def read_input(input_file_name: str) -> Optional[List[str]]:
    with open(input_file_name, 'r') as input_file:
        return input_file.readlines()
