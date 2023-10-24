from abc import ABC, abstractmethod
from dataclasses import dataclass


class GeneralFileReader(ABC):
    @abstractmethod
    def consumo(self) -> float:
        ...


class BaseReader(GeneralFileReader):
    def consumo(self) -> float:
        from datetime import datetime

        return 100 + datetime.now().second


# TBD
class PlainTextReader(GeneralFileReader):
    def consumo(self) -> float:
        return 8


# TBD
class XmlReader(GeneralFileReader):
    def consumo(self) -> float:
        return 7


@dataclass
class Lettura:
    consumo: float
    unita: str

    def __str__(self):
        return f"{self.consumo} {self.unita}"


class Reader(ABC):
    def __init__(self) -> None:
        self.underlying_reader = BaseReader()

    @abstractmethod
    def has_next_lettura(self) -> bool:
        ...

    @abstractmethod
    def get_next_lettura(self) -> Lettura:
        ...


class ReaderCreator(ABC):
    @abstractmethod
    def create_reader(self) -> Reader:
        ...


class GasLettureReader(Reader):
    def __init__(self) -> None:
        super().__init__()
        self.um = "smc"

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class H20LettureReader(Reader):
    def __init__(self) -> None:
        super().__init__()
        self.um = "litri"

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class ElLettureReader(Reader):
    def __init__(self) -> None:
        super().__init__()
        self.um = "KWh"

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class GasLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return GasLettureReader()


class H2OLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return H20LettureReader()


class ElLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return ElLettureReader()


if __name__ == "__main__":
    config = [
        (GasLettureReaderCreator, PlainTextReader),
        (GasLettureReaderCreator, XmlReader),
    ]

    readers = [
        GasLettureReaderCreator().create_reader(),
        H2OLettureReaderCreator().create_reader(),
        ElLettureReaderCreator().create_reader(),
    ]

    for reader in readers:
        if reader.has_next_lettura():
            print(reader.get_next_lettura())
