from decimal import Decimal
from typing import List


class RPNCalc:
    def __init__(self) -> None:
        self.stack: List[Decimal] = []
        self.error: bool = False

    def acknowledge_error(self):
        self.error = False

    def clear(self):
        self.stack.clear()

    def enter(self, candidate: str):
        try:
            self.stack.append(Decimal(candidate))
        except ValueError:
            self.error = True

    def sum(self):
        if len(self.stack) >= 2:
            second = self.stack.pop()
            first = self.stack.pop()
            print(first, second)
            self.stack.append(first + second)
        else:
            self.error = True

    def result(self) -> Decimal | None:
        return self.stack[-1] if len(self.stack) > 0 else None
