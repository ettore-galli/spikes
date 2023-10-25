from __future__ import annotations
from abc import ABC, abstractclassmethod

from functools import reduce
from typing import List, Optional


class Personaggio(ABC):
    def __init__(self, nome, genere="M") -> None:
        self.nome = nome
        self.genere = genere

    def combatti(
        self, opponente: Personaggio
    ) -> int:  # 1 = ho vinto; 0=Pari; -1 = Ho perso
        print(f"{self.nome} ({self.genere}): Combattendo contro {opponente}")
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


class Umano(Personaggio):
    def combatti(self, opponente: Personaggio) -> int:
        super().combatti(opponente=opponente)
        _ = Personaggio
        return -1


class PersonaggioEsperto(Personaggio):
    def __init__(self, personaggio_base) -> None:
        super().__init__(nome=personaggio_base.nome)
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
        print(f"{self.nome} ({self.genere}): Facendo una magia")


if __name__ == "__main__":
    uomo = Umano(nome="A")
    altro_uomo = Umano("B")

    mago = Stregone(personaggio_base=uomo)

    sacerdote = Sacerdote(personaggio_base=altro_uomo)

    terzo_uomo = Umano("C")
    strega = Stregone(Umano("Giovannina", genere="F"))
    tuttologo = Sacerdote(
        personaggio_base=Stregone(personaggio_base=terzo_uomo),
    )

    print(mago.combatti(terzo_uomo))
    print(uomo.combatti(sacerdote))
    print(tuttologo.combatti(altro_uomo))
    print(mago.fai_magia())
    print(sacerdote.intercedi(Divinita()))
    print(strega.fai_magia())
