from typing import Generator, Iterable, Tuple


def mult_tab(top=1000) -> Generator[Tuple[int], None, None]:
    for base in range(1, top):
        yield [base * digit for digit in range(1, 10)]


def format_mult_tab(source: Iterable[int]) -> Iterable[str]:
    pattern = "{:6d} " * 9
    for line in source:
        formatted = pattern.format(*line)
        yield formatted


if __name__ == "__main__":
    for line in format_mult_tab(mult_tab()):
        print(line)
