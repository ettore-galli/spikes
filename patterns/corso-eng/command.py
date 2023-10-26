from abc import ABC, abstractmethod
from typing import List

class Edificio(ABC):
    ...

class Abitazione(Edificio):
    def __init__(self, locali: int, bagni: int, giardino: bool) -> None:
        self.locali = locali
        self.bagni = bagni
        self.giardino = giardino

    def __str__(self) -> str:
        return f"Abitazione {self.locali} {self.bagni} {self.giardino}"


class Imbianchino:
    @staticmethod
    def esegui_tinteggiatura(abitazione, colore):
        print("tinteggiaura", abitazione, colore)

    @staticmethod
    def esegui_tappezzeria(abitazione, tipo_scelto):
        print("tappezzeria", abitazione, tipo_scelto)


class Muratore:
    @staticmethod
    def esegui_muratura_bagno(abitazione, piastrelle, sanitari):
        print("muratura bagno", abitazione, piastrelle, sanitari)


class Idraulico:
    @staticmethod
    def esegui_impianti_bagno(abitazione):
        print("impianti bagno", abitazione)


class Giardiniere:
    @staticmethod
    def esegui_giardino(abitazione):
        print("giardino", abitazione)


class Comando(ABC):
    def __init__(self, abitazione: Abitazione) -> None:
        self.abitazione = abitazione

    @abstractmethod
    def esegui(self):
        ...


class Tinteggiatura(Comando):
    def __init__(self, abitazione: Abitazione, colore) -> None:
        super().__init__(abitazione)
        self.colore = colore

    def esegui(self):
        Imbianchino().esegui_tinteggiatura(self.abitazione, self.colore)


class CostruzioneBagno(Comando):
    def __init__(self, abitazione: Abitazione, colore, piastrelle, sanitari) -> None:
        super().__init__(abitazione)
        self.colore = colore
        self.piastrelle = piastrelle
        self.sanitari = sanitari

    def esegui(self):
        Muratore().esegui_muratura_bagno(
            self.abitazione, self.piastrelle, self.sanitari
        )
        Idraulico().esegui_impianti_bagno(self.abitazione)
        Imbianchino().esegui_tinteggiatura(self.abitazione, self.colore)


class Tappezzatura(Comando):
    def __init__(self, abitazione: Abitazione, tipo_scelto) -> None:
        super().__init__(abitazione)
        self.tipo_scelto = tipo_scelto

    def esegui(self):
        Imbianchino().esegui_tappezzeria(self.abitazione, self.tipo_scelto)


class CostruzioneGiardino(Comando):
    def esegui(self):
        Giardiniere().esegui_giardino(self.abitazione)


class ImpresaEdile:
    def esegui_lavori(self, lavori: List[Comando]):
        for lavoro in lavori:
            lavoro.esegui()


if __name__ == "__main__":
    casa = Abitazione(3, 1, True)
    impresa = ImpresaEdile()

    lavori = [
        CostruzioneBagno(casa, "giallo", "ceramica verde", "ideal standard"),
        Tappezzatura(casa, "a fiori"),
        CostruzioneBagno(casa, "verde", "mosaico bisazza", "jacuzzi"),
        CostruzioneGiardino(casa),
    ]

    impresa.esegui_lavori(lavori)
