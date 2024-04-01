import contextlib


class OutputWriter:
    def __init__(self, filename) -> None:
        self.filename: str = filename
        self.lines: int = 0
        self.out = open(self.filename, "w")

    def __del__(self):
        self.out.close()

    def write_line(self, data):
        self.out.write(data)
        self.lines += 1


def write_data(writer: OutputWriter):
    writer.write_line("Hello, world 1\n")
    writer.write_line("Hello, world 2\n")
    writer.write_line("Hello, world 3\n")
    print(f"from inside: {writer.lines}")


def main():
    filename = "./output/example.txt"
    writer: OutputWriter = OutputWriter(filename)
    write_data(writer=writer)
    print(f"from outside: {writer.lines}")


if __name__ == "__main__":
    main()
