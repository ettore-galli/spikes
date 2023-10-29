from abc import ABC, abstractmethod
from dataclasses import dataclass


class GeneralInputReader(ABC):
    @abstractmethod
    def get_temperature(self) -> float:
        ...


class FileReader(GeneralInputReader):
    def __init__(self, file) -> None:
        super().__init__()
        self.file = file

    def get_temperature(self) -> float:
        with open(self.file) as te:
            temp = float(te.read())
            return temp


class ConsoleReader(GeneralInputReader):
    def get_temperature(self) -> float:
        temp_raw = input("Temperatura: ")
        temp = float(temp_raw)
        return temp


class ReaderCreator(ABC):
    @abstractmethod
    def get_temperature_reader(self) -> GeneralInputReader:
        ...


class ConsoleReaderCreator(ReaderCreator):
    def get_temperature_reader(self) -> GeneralInputReader:
        return ConsoleReader()


class FileReaderCreator(ReaderCreator):
    def get_temperature_reader(self) -> GeneralInputReader:
        return FileReader("./data/temperatura.txt")


class Converter:
    def __init__(self, reader) -> None:
        self.reader: GeneralInputReader = reader

    def get_converted_temperature(self) -> float:
        return self.reader.get_temperature() * 9 / 5 + 32


if __name__ == "__main__":
    readers = [
        ConsoleReaderCreator().get_temperature_reader(),
        FileReaderCreator().get_temperature_reader(),
    ]

    for reader in readers:
        converted_temp = Converter(reader=reader).get_converted_temperature()
        print(converted_temp)
