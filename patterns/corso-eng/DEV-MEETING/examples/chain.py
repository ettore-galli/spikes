from __future__ import annotations
from abc import ABC, abstractmethod
import math
from typing import Optional, Union

Number = Union[int, float]


class PowerHandler(ABC):
    def __init__(self, next: Optional[PowerHandler] = None) -> None:
        super().__init__()
        self.set_next(next)

    def set_next(self, next: Optional[PowerHandler]):
        self.next = next

    @abstractmethod
    def compute_power(self, base: Number, exponent: Number) -> Number:
        ...


class RepeatedMultiplicationsHandler(PowerHandler):
    def compute_power(self, base: Number, exponent: Number) -> Number:
        if isinstance(exponent, int) and exponent < 10:
            power: float = 1
            for _ in range(exponent):
                power = power * base
            print(f"Handled by {self.__class__.__name__}")
            return power

        return self.next.compute_power(base, exponent)


class MathPowHandler(PowerHandler):
    def compute_power(self, base: Number, exponent: Number) -> Number:
        if base < 1000000 and exponent < 50:
            print(f"Handled by {self.__class__.__name__}")
            return math.pow(base, exponent)

        return self.next.compute_power(base, exponent)


class BigNumbersHandler(PowerHandler):
    def compute_power(self, base: Number, exponent: Number) -> Number:
        print(f"Handled by {self.__class__.__name__}")
        lower = int(base) ** int(exponent)
        upper = int(base + 1) ** int(exponent + 1)
        return (lower + upper) // 2


def power(base: Number, exponent: Number) -> Number:
    handler_1 = RepeatedMultiplicationsHandler()
    handler_2 = MathPowHandler()
    handler_3 = BigNumbersHandler()
    handler_1.set_next(handler_2)
    handler_2.set_next(handler_3)
    return handler_1.compute_power(base, exponent)


if __name__ == "__main__":
    print(power(2, 3))
    print(power(11, 12))
    print(power(111111.4, 51.8))
