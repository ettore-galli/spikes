class Iterante:
    def __init__(self):
        self.elements = ["cicci", "pippo", 265, False, "q"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.elements):
            next_element = self.elements[self.index]
            self.index += 1
            return next_element
        raise StopIteration


if __name__ == "__main__":
    it = Iterante()
 
    for x in it:
        print(x)
