from abc import ABC, abstractmethod
from datetime import datetime


class Dipendente(ABC):
    @abstractmethod
    def get_nome(self) -> str:
        ...

    @abstractmethod
    def get_cognome(self) -> str:
        ...

    @abstractmethod
    def get_data_nascita(self) -> datetime:
        ...

    @abstractmethod
    def get_stipendio_annuale(self) -> float:
        ...


class Impiegato(Dipendente):
    def __init__(self, nome, cognome, data_nascita, stipendio_annuale) -> None:
        super().__init__()
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.stipendio_annuale = stipendio_annuale

    def get_nome(self) -> str:
        return self.nome

    def get_cognome(self) -> str:
        return self.cognome

    def get_data_nascita(self) -> datetime:
        return self.data_nascita

    def get_stipendio_annuale(self) -> float:
        return self.stipendio_annuale


class Lavoratore(ABC):
    @abstractmethod
    def get_nominativo(self) -> str:
        ...

    @abstractmethod
    def get_eta(self) -> int:
        ...

    @abstractmethod
    def get_stipendio_giornaliero(self) -> float:
        ...


class DipendenteLavoratoreAdapter(Lavoratore):
    def __init__(self, dipendente: Dipendente) -> None:
        super().__init__()
        self.dipendente: Dipendente = dipendente

    def get_nominativo(self) -> str:
        return f"{self.dipendente.get_cognome()} {self.dipendente.get_nome()}"

    def get_eta(self) -> int:
        return (datetime.now() - self.dipendente.get_data_nascita()).days / 365

    def get_stipendio_giornaliero(self) -> float:
        return self.dipendente.get_stipendio_annuale() / 365


if __name__ == "__main__":
    ettore: Impiegato = Impiegato("Ettore", "Galli", datetime(1972, 11, 2), 366)
    ettore_lavoratore = DipendenteLavoratoreAdapter(dipendente=ettore)
    print(
        ettore_lavoratore.get_nominativo(),
        ettore_lavoratore.get_eta(),
        ettore_lavoratore.get_stipendio_giornaliero(),
    )
