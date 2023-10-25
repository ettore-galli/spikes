from abc import ABC, abstractmethod


class Noleggio(ABC):
    @abstractmethod
    def inizia_noleggio(self) -> str:
        ...


class Auto(ABC):
    @abstractmethod
    def descrizione(self) -> str:
        ...


class Utilitaria(ABC):
    def descrizione(self) -> str:
        return "panda"


class Lusso(ABC):
    def descrizione(self) -> str:
        return "rolls royce"


class Minivan(ABC):
    def descrizione(self) -> str:
        return "quanti siete? dove andate? un 'Fiorino'"


class NoleggioPrivato(Noleggio):
    def __init__(self, automobile: Auto) -> None:
        super().__init__()
        self.automobile = automobile

    def inizia_noleggio(self) -> str:
        return f"Iniziato noleggio privato di {self.automobile.descrizione()}"


class NoleggioConducente(Noleggio):
    def __init__(self, automobile: Auto) -> None:
        super().__init__()
        self.automobile = automobile

    def inizia_noleggio(self) -> str:
        return f"Iniziato noleggio con conducente di {self.automobile.descrizione()}"


if __name__ == "__main__":
    for noleggio_class in [NoleggioConducente, NoleggioPrivato]:
        for automobile in [Utilitaria, Lusso, Minivan]:
            noleggio: Noleggio = noleggio_class(automobile=automobile())
            print(noleggio.inizia_noleggio())
