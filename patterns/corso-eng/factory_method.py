from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Lettura:
    consumo: float
    unita: str

    def __str__(self):
        return f"{self.consumo} {self.unita}"


@dataclass
class DatiLettura:
    consumo: float
    unita: str


class Reader(ABC):
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
    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=13, unita="smc")


class H20LettureReader(Reader):
    # def __init__(self) -> None:
    #     super().__init__()
    #     self.underlying_reader = reader

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=7, unita="litri")


class ElLettureReader(Reader):
    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=7, unita="Kwh")


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
    def read(self) -> DatiLettura:
        ...


class PlainTextReader(GeneralFileReader):
    def read(self, file) -> DatiLettura:
        return DatiLettura(consumo=7, unita="Kwh")


class XmlReader(GeneralFileReader):
    def read(self, file) -> DatiLettura:
        return DatiLettura(consumo=17, unita="Kwh")


if __name__ == "__main__":
    readers = [
        GasLettureReaderCreator().create_reader(),
        H2OLettureReaderCreator().create_reader(),
        ElLettureReaderCreator().create_reader(),
    ]

    for reader in readers:
        if reader.has_next_lettura():
            print(reader.get_next_lettura())
