from typing import Callable


def memoize(fun: Callable):
    nmap = {}

    def _memoized(*args):
        argset = tuple(args)
        if argset in nmap:
            print(f"Using saved params {argset}")
            return nmap.get(argset)

        result = fun(*args)
        nmap[argset] = result
        return result

    return _memoized


def longsum(a, b):
    s = a
    for _ in range(b):
        s += 1
    return s


mlongsum = memoize(longsum)

if __name__ == "__main__":
    for a, b in [(1, 7), (100, 400), (1, 8), (1, 7), (100, 400), (3, 4)]:
        print(mlongsum(a, b))
