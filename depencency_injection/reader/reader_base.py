from abc import ABC, abstractmethod
from typing import List


class BaseFileReader(ABC):
    @abstractmethod
    def read_data(self, file: str) -> List[str]:
        pass
