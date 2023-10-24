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
        return "tricolore.jpg"


class BandieraTedesca(Bandiera):
    def get_icon(self) -> str:
        return "<tedesca>.jpg"


class SalutoItaliano(Saluto):
    def get_text(self) -> str:
        return "ciao"


class SalutoTedesco(Saluto):
    def get_text(self) -> str:
        return "hallo"


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


class PaginaItalianaTedesca(ABC):
    def get_bandiera(self) -> Bandiera:
        return BandieraTedesca()

    def get_saluto(self) -> Saluto:
        return SalutoTedesco()


if __name__ == "__main__":
    crea_pagina_italiana = PaginaItalianaFactory()
    crea_pagina_tedesca = PaginaItalianaTedesca()

    creator: List[PaginaFactory]
    for creator in [crea_pagina_italiana, crea_pagina_tedesca]:
        print(creator.get_bandiera().get_icon(), creator.get_saluto().get_text())
