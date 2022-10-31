from typing import Tuple


def my_function(cosi: Tuple[str, float, float], x: str):
    print(cosi)
    print(x)


if __name__ == '__main__':
    my_function(cosi=("a", 1.0, 2.0), x="ciao")
