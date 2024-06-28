from typing import List

from depencency_injection.reader.reader_base import BaseFileReader


class DataFileReader(BaseFileReader):
    def read_data(self, file: str) -> List[str]:
        with open(file, "r", encoding="utf-8") as data_file:
            return data_file.readlines()
