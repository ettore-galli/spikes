from __future__ import annotations
from abc import ABC, abstractmethod


class Modo(ABC):
    def __init__(self, context: Orologio) -> None:
        self.context: Orologio = context

    @abstractmethod
    def pulsante_modo(self):
        ...

    @abstractmethod
    def pulsante_change(self):
        ...


class ModoNormale(Modo):
    descr = "NORM"

    def pulsante_modo(self):
        self.context.set_modo(ModoModificaOre(self.context))

    def pulsante_change(self):
        self.context.set_luce()


class ModoModificaOre(Modo):
    descr = "CHG H"

    def pulsante_modo(self):
        self.context.set_modo(ModoModificaMinuti(self.context))

    def pulsante_change(self):
        self.context.inc_ore()


class ModoModificaMinuti(Modo):
    descr = "CHG M"

    def pulsante_modo(self):
        self.context.set_modo(ModoNormale(self.context))

    def pulsante_change(self):
        self.context.inc_minuti()


class Orologio:
    def __init__(self) -> None:
        self.modo: Modo = ModoNormale(self)
        self.luce: bool = False
        self.ore: int = 0
        self.minuti: int = 0

    def set_modo(self, modo: Modo):
        self.modo = modo

    def set_luce(self):
        self.luce = not self.luce

    def inc_ore(self):
        self.ore = (self.ore + 1) % 60

    def inc_minuti(self):
        self.minuti = (self.minuti + 1) % 60

    def pulsante_modo(self):
        self.modo.pulsante_modo()

    def pulsante_change(self):
        self.modo.pulsante_change()

    def __str__(self) -> str:
        return f"{self.ore} : {self.minuti} {self.modo.descr} {'>>> <<<' if self.luce else ''}"


if __name__ == "__main__":
    orologio = Orologio()
    print(orologio)

    orologio.pulsante_change()
    print(orologio)

    orologio.pulsante_change()
    print(orologio)

    orologio.pulsante_modo()
    print(orologio)

    for i in range(7):
        orologio.pulsante_change()
    print(orologio)

    orologio.pulsante_modo()
    print(orologio)

    for i in range(21):
        orologio.pulsante_change()
    print(orologio)

    orologio.pulsante_modo()
    print(orologio)
