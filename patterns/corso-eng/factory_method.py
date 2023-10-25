from abc import ABC, abstractmethod
from dataclasses import dataclass


class GeneralFileReader(ABC):
    def __init__(self, file) -> None:
        self.file = file

    @abstractmethod
    def consumo(self) -> float:
        ...


class BaseReader(GeneralFileReader):
    def consumo(self) -> float:
        return -1


# TBD
class PlainTextReader(GeneralFileReader):
    def consumo(self) -> float:
        with open(self.file) as data_file:
            consumo = float(data_file.read())
            return consumo  # Antipattern "fiducia"


# TBD
class XmlReader(GeneralFileReader):
    def consumo(self) -> float:
        with open(self.file) as data_file:
            raw_data = str(data_file.read())
            consumo = float(raw_data[1:-1])
            return consumo  # Antipattern "fiducia"


@dataclass
class Lettura:
    consumo: float
    unita: str

    def __str__(self):
        return f"{self.consumo} {self.unita}"


class Reader(ABC):
    def __init__(self) -> None:
        self.underlying_reader = BaseReader("data/empty.txt")

    @abstractmethod
    def has_next_lettura(self) -> bool:
        ...

    @abstractmethod
    def get_next_lettura(self) -> Lettura:
        ...


class ReaderCreator(ABC):
    @abstractmethod
    def create_reader(self, data_file) -> Reader:
        ...


def get_reader_from_file(file) -> GeneralFileReader:
    return XmlReader(file) if "X" in file else PlainTextReader(file)


class GasLettureReader(Reader):
    def __init__(self, file) -> None:
        super().__init__()
        self.um = "smc"
        self.underlying_reader = get_reader_from_file(file)

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class H20LettureReader(Reader):
    def __init__(self, file) -> None:
        super().__init__()
        self.um = "litri"
        self.underlying_reader = get_reader_from_file(file)

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class ElLettureReader(Reader):
    def __init__(self, file) -> None:
        super().__init__()
        self.um = "KWh"
        self.underlying_reader = get_reader_from_file(file)

    def has_next_lettura(self) -> bool:
        return True

    def get_next_lettura(self) -> Lettura:
        return Lettura(consumo=self.underlying_reader.consumo(), unita=self.um)


class GasLettureReaderCreator(ReaderCreator):
    def create_reader(self, data_file) -> Reader:
        return GasLettureReader(data_file)


class H2OLettureReaderCreator(ReaderCreator):
    def create_reader(self, data_file) -> Reader:
        return H20LettureReader(data_file)


class ElLettureReaderCreator(ReaderCreator):
    def create_reader(self, data_file) -> Reader:
        return ElLettureReader(data_file)


if __name__ == "__main__":
    config = [
        (GasLettureReaderCreator, PlainTextReader),
        (GasLettureReaderCreator, XmlReader),
    ]

    readers = [
        GasLettureReaderCreator().create_reader("data/GAS.txt"),
        H2OLettureReaderCreator().create_reader("data/H2O.txt"),
        ElLettureReaderCreator().create_reader("data/ELE.txt"),
        ElLettureReaderCreator().create_reader("data/ELE-X.txt"),
    ]

    for reader in readers:
        if reader.has_next_lettura():
            print(reader.get_next_lettura())
