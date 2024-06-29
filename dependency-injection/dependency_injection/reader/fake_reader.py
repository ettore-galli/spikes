from typing import List

from dependency_injection.reader.reader_base import BaseFileReader


class FakeDataFileReader(BaseFileReader):
    def read_data(self, file: str) -> List[str]:
        _ = file
        return ["aaa", "bbb", "ccc"]
