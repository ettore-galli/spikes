from abc import ABC, abstractclassmethod
from functools import reduce
from typing import List, Optional


class Contatto(ABC):
    @abstractclassmethod
    def get_numeri(self) -> List[str]:
        ...


class Nominativo(Contatto):
    def __init__(self, numero: str) -> None:
        super().__init__()
        self.numero = numero
        self.contatti = None

    def get_numeri(self) -> List[str]:
        return [self.numero]


class Gruppo(Contatto):
    def __init__(self, contatti: Optional[List[Contatto]] = None) -> None:
        super().__init__()
        self.numero = None
        self.contatti = contatti

    def get_numeri(self) -> List[str]:
        return reduce(lambda acc, cur: acc + cur.get_numeri(), self.contatti, [])


if __name__ == "__main__":
    amici = Gruppo(contatti=[Nominativo("1111111"), Nominativo("2222222")])
    parenti = Gruppo(contatti=[Nominativo("3333333"), Nominativo("4444444")])
    tutti = Gruppo(contatti=[amici, parenti, Nominativo("123123")])
    universo = Gruppo(contatti=[tutti, Nominativo("999999999999")])

    print(tutti.get_numeri())
    print(universo.get_numeri())
