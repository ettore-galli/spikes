from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Lettura:
    consumo: float
    unita: str

    def __str__(self):
        return f"{self.consumo} {self.unita}"


class Reader(ABC):
    um = None

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
    um = "smc"

    def __init__(self) -> None:
        super().__init__()
        self.consumo = 8
        # self.underlying_reader = reader

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.consumo, unita=self.um)


class H20LettureReader(Reader):
    um = "litri"

    def __init__(self) -> None:
        super().__init__()
        self.consumo = 7
        # self.underlying_reader = reader

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.consumo, unita=self.um)


class ElLettureReader(Reader):
    um = "KWh"

    def __init__(self) -> None:
        super().__init__()
        self.consumo = 11
        # self.underlying_reader = reader

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.consumo, unita=self.um)


class GasLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return GasLettureReader()


class H2OLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return H20LettureReader()


class ElLettureReaderCreator(ReaderCreator):
    def create_reader(self) -> Reader:
        return ElLettureReader()


class GeneralFileReader(ABC):
    @abstractmethod
    def consumo(self) -> float:
        ...


# TBD
class PlainTextReader(GeneralFileReader):
    def consumo(self) -> float:
        return 8


# TBD
class XmlReader(GeneralFileReader):
    def consumo(self) -> float:
        return 7


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
