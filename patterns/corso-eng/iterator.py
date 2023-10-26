class Looper:
    def __init__(self, lista) -> None:
        self.lista = lista
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = self.lista[self.pointer]
        self.pointer = (self.pointer + 1) % len(self.lista)
        return item


if __name__ == "__main__":
    for item in Looper(lista=["A", "B", "C", "D"]):
        print(item)
