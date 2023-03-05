from typing import Union
from decimal import Decimal

NumericType = Union[int, float, Decimal]

candidate = "Hello, world!"

print(isinstance(candidate, NumericType))
