from dataclasses import dataclass
from typing import Callable


def transform(value):
    return value / 2 if value % 2 == 0 else value * 3 + 1


Function1D = Callable[[float], float]


@dataclass(frozen=True)
class GDMinimumResult:
    x: float
    y: float


def parabola(value: float) -> float:
    return value**2 - 2


def parabolad1(value: float) -> float:
    return 2 * value


def gd_minimum(
    fun: Function1D,
    fun_derivative: Function1D,
    eta: float,
    epsilon: float,
    x_initial_guess: float,
) -> GDMinimumResult:
    x = x_initial_guess
    while True:
        deri = fun_derivative(x)
        x -= eta * deri
        if deri < epsilon:
            break
    return GDMinimumResult(x, fun(x))


class Looper:
    def __init__(self, transformer, stop_predicate, initial) -> None:
        self.transformer = transformer
        self.stop_predicate = stop_predicate
        self.status = initial

    def with_input(self, step_input):
        return Looper(
            transformer=self.transformer,
            stop_predicate=self.stop_predicate,
            initial=step_input,
        )

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop_predicate(self.status):
            raise StopIteration

        self.status = self.transformer(self.status)

        return self.status


if __name__ == "__main__":
    myiter = Looper(transform_input, lambda status: status == 0, 1)
    while True:
        # step_input = float(input("Enter a value: "))
        # print(next(myiter.with_input(step_input=step_input)))
        print(next(myiter))
