from abc import ABC, abstractmethod


class FactoryPatternProduct(ABC):
    ...


class FactoryPatternCreator(ABC):
    ...


class Pet(FactoryPatternProduct):
    @abstractmethod
    def fai_verso(self) -> str:
        ...


class Dog(Pet):
    def fai_verso(self) -> str:
        return "Woof"


class Cat(Pet):
    def fai_verso(self) -> str:
        return "Meow"


class PetCreator(FactoryPatternCreator):
    @staticmethod
    @abstractmethod
    def create() -> Pet:
        ...


class DogCreator(PetCreator):
    @staticmethod
    def create() -> Pet:
        return Dog()


class CatCreator(PetCreator):
    @staticmethod
    def create() -> Pet:
        return Cat()


if __name__ == "__main__":
    print(DogCreator.create().fai_verso(), CatCreator.create().fai_verso())
