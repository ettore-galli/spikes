from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class ImpiegatoBase(ABC):
    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def store(self):
        ...


class Impiegato(ImpiegatoBase):
    def __init__(self) -> None:
        self.nome: Optional[str] = None
        self.reparto: Optional[str] = None
        self.stipendio: Optional[float] = None

    def load(self):
        self.nome: str = "Ettore"
        self.reparto: str = "IT"
        self.stipendio: float = "10000000000000000000"
        print("Data loaded")

    def get_data(self):
        return f"{self.nome} {self.reparto} {self.stipendio}"

    def update_data(self, nome, reparto, stipendio):
        print(f"Updating: {nome, reparto, stipendio}")
        self.nome = nome
        self.reparto = reparto
        self.stipendio = stipendio

    def store(self):
        print(f"Storing {self.nome}{self.reparto}{str(self.stipendio)}")


class ImpiegatoProxy(ImpiegatoBase):
    def __init__(self) -> None:
        self.impiegato = Impiegato()
        self.footprint = []

    def get_data(self):
        return self.impiegato.get_data()

    def load(self):
        if not self.impiegato.nome:
            self.impiegato.load()
            self.footprint = [
                self.impiegato.nome,
                self.impiegato.reparto,
                self.impiegato.stipendio,
            ]

    def update_data(self, nome, reparto, stipendio):
        self.impiegato.update_data(nome, reparto, stipendio)

    def _has_changed(self) -> bool:
        return [
            self.impiegato.nome,
            self.impiegato.reparto,
            self.impiegato.stipendio,
        ] != self.footprint

    def store(self):
        if self._has_changed():
            self.impiegato.store()
            self.impiegato.load()


if __name__ == "__main__":
    ip = ImpiegatoProxy()
    ip.load()
    ip.load()
    ip.load()
    ip.load()

    print(ip.get_data())

    ip.update_data("Ettore", "IT", "29834723894729374238947984273")

    ip.store()
    ip.store()
    ip.store()
    ip.store()
    ip.store()
    ip.store()
    ip.store()
    ip.store()
    ip.store()
