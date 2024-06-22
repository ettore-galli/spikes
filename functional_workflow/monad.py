from __future__ import annotations

from typing import Optional, Any, Callable, Dict, TypeVar, Generic


P = TypeVar("P")
C = TypeVar("C")


class Monad(Generic[P, C]):
    def __init__(
        self,
        payload: P,
        config: C,
        success: bool = True,
        message: Optional[str] = None,
    ):
        self.payload = payload
        self.config = config
        self.success = success
        self.message = message

    @staticmethod
    def unit(value):
        return Monad(payload=value)

    def bind(self, f: Callable[[P], Monad[P, C]]) -> Monad:
        if not self.success:
            return self
        try:
            return f(self.payload)

        except Exception as exception:
            return Monad(
                payload=self.payload,
                config=self.config,
                success=False,
                message=str(exception),
            )

    def __rshift__(self, other):
        return self.bind(other)


def read_input() -> Monad:
    return Monad[str, Dict](payload=input(), config={})


def read_other(previous: str) -> Monad:
    return Monad[str, Dict](payload=previous + " - " + input(), config={})


def transform(data: str) -> Monad:
    return Monad[str, Dict](payload=f"<<{data}>>", config={})


if __name__ == "__main__":

    main = read_input() >> transform >> transform >> read_other >> transform

    print(main.payload)
