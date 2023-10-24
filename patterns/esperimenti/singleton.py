from __future__ import annotations


class SingleOne:
    __instance__: SingleOne = None

    # def __init__(self) -> None:
    #     raise Exception("Cannot instantiate directly")

    @classmethod
    def get_instance(cls) -> SingleOne:
        if cls.__instance__ is None:
            cls.__instance__ = SingleOne()
        return cls.__instance__

    def set_alfa(self, alfa: float):
        self.alfa = alfa


if __name__ == "__main__":
    s1 = SingleOne.get_instance()
    s2 = SingleOne.get_instance()

    s1.set_alfa(3.14)
    print(s1.alfa, s2.alfa)
