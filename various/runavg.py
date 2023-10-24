from typing import Generator, Iterable, List, Tuple


def running_average(
    samples: Iterable[float],
) -> Generator[Tuple[float, float], None, None]:
    avg: float = 0
    for idx, sample in enumerate(samples):
        avg = (avg * idx + sample) / (idx + 1)
        yield avg


if __name__ == "__main__":
    data: List[float] = [
        1,
        4,
        3,
        5,
        2,
        4,
        5,
        2,
        5,
        3,
        5,
        6,
        7,
        11,
        4,
        3,
        2,
        3,
        4,
        5,
        6,
        7,
        6,
        4,
        4,
        3,
    ]
    print("=====")
    for avg in running_average(data):
        print(avg)
    print("---")
    print(sum(data) / len(data))
