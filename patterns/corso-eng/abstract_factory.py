from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Saluto(ABC):
    @abstractmethod
    def get_text(self) -> str:
        ...


class Bandiera(ABC):
    @abstractmethod
    def get_icon(self) -> str:
        ...


class BandieraItaliana(Bandiera):
    def get_icon(self) -> str:
        return "[|||]"


class BandieraTedesca(Bandiera):
    def get_icon(self) -> str:
        return "[oOo]"


class BandieraInglese(Bandiera):
    def get_icon(self) -> str:
        return "[xXx]"


class SalutoItaliano(Saluto):
    def get_text(self) -> str:
        return "Benvenuto"


class SalutoTedesco(Saluto):
    def get_text(self) -> str:
        return "Welcome"


class SalutoInglese(Saluto):
    def get_text(self) -> str:
        return "Wilkommen"


class PaginaFactory(ABC):
    @abstractmethod
    def get_bandiera(self) -> Bandiera:
        ...

    @abstractmethod
    def get_saluto(self) -> Saluto:
        ...


class PaginaItalianaFactory(ABC):
    def get_bandiera(self) -> Bandiera:
        return BandieraItaliana()

    def get_saluto(self) -> Saluto:
        return SalutoItaliano()


class PaginaTedescaFactory(ABC):
    def get_bandiera(self) -> Bandiera:
        return BandieraTedesca()

    def get_saluto(self) -> Saluto:
        return SalutoTedesco()


class PaginaIngleseFactory(ABC):
    def get_bandiera(self) -> Bandiera:
        return BandieraInglese()

    def get_saluto(self) -> Saluto:
        return SalutoInglese()


if __name__ == "__main__":
    creators: List[PaginaFactory] = [
        PaginaItalianaFactory(),
        PaginaTedescaFactory(),
        PaginaIngleseFactory(),
    ]

    for creator in creators:
        print(creator.get_bandiera().get_icon(), creator.get_saluto().get_text())
