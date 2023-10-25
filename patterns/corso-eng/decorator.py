from __future__ import annotations
from abc import ABC, abstractclassmethod

from functools import reduce
from typing import List, Optional


class Personaggio(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome

    def combatti(
        self, opponente: Personaggio
    ) -> int:  # 1 = ho vinto; 0=Pari; -1 = Ho perso
        print(f"{self.nome}: Combattendo contro {opponente}")
        return -1

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.nome}"


class Elfo(Personaggio):
    def combatti(self, opponente: Personaggio) -> int:
        super().combatti(opponente=opponente)
        _ = Personaggio
        return 1


class Nano(Personaggio):
    def combatti(self, opponente: Personaggio) -> int:
        super().combatti(opponente=opponente)
        _ = Personaggio
        return 0


class Uomo(Personaggio):
    def combatti(self, opponente: Personaggio) -> int:
        super().combatti(opponente=opponente)
        _ = Personaggio
        return -1


class PersonaggioEsperto(Personaggio):
    def __init__(self, nome, personaggio_base) -> None:
        super().__init__(nome=nome)
        self.personaggio_base = personaggio_base

    def combatti(self, opponente: Personaggio) -> int:
        super().combatti(opponente=opponente)


class Divinita:
    ...


class Sacerdote(PersonaggioEsperto):
    def intercedi(self, divinita: Divinita) -> str:
        _ = divinita
        return "..."


class Stregone(PersonaggioEsperto):
    def fai_magia(self) -> str:
        return "abracadabra."


if __name__ == "__main__":
    uomo = Uomo(nome="A")
    altro_uomo = Uomo("B")

    mago = Stregone(nome="Il Mago", personaggio_base=uomo)

    sacerdote = Sacerdote(nome="Gran Sacerdote", personaggio_base=altro_uomo)

    terzo_uomo = Uomo("C")
    tuttologo = Sacerdote(
        nome="Tuttofare",
        personaggio_base=Stregone(nome=".", personaggio_base=terzo_uomo),
    )

    print(mago.combatti(terzo_uomo))
    print(uomo.combatti(sacerdote))
    print(tuttologo.combatti(altro_uomo))
    print(mago.fai_magia())
    print(sacerdote.intercedi(Divinita()))
