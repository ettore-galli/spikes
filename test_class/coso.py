class CosoBase:
    def __init__(self, a, b, c) -> None:
        [self.a, self.b, self.c, self.qwerty] = [a, b, c, a + 2 * b + 3 * c]
 

    def descrivi(self):
        return f"{self.a}, {self.b}, {self.c} -> {self.qwerty}"


class CosoSpecifico(CosoBase):
    def descrivi(self):
        return f"({self.a} {self.b} {self.c}) ====> ({self.qwerty})"


if __name__ == "__main__":
    cb = CosoBase(1, 2, 3)
    assert cb.descrivi() == "1, 2, 3 -> 14"
    print(cb.descrivi())

    cs = CosoSpecifico(1, 2, 3)
    assert cs.descrivi() == "(1 2 3) ====> (14)"
    print(cs.descrivi())
