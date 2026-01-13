def myfun(x):
    print("----------")
    print(x + 1)
    print("----------")


class myLazy:
    def __init__(self, val):
        self._val = val

    def value(self):
        return self._val
    
    def __repr__(self):
        return self._val


if __name__ == "__main__":
    myfun(3)
    myfun(myLazy(4))
