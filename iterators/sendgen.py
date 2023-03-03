import contextlib


def data_printer(prefix):
    item = None
    try:
        while True:
            item = yield item
            print(f"{prefix} {item}")
    finally:
        print("*END")


def sender():
    printer = data_printer("===>")
    next(printer)

    for n in range(100):
        printer.send(n)

    printer.close()


@contextlib.contextmanager
def output_writer_a(file):
    with open(file, "w") as outfile:

        def writedata(data):
            outfile.write(f"* {data}")

        yield writedata


@contextlib.contextmanager
def output_writer_b(file):
    with open(file, "w") as outfile:

        def writedata(data):
            outfile.write(f">> {data}")

        yield writedata


@contextlib.contextmanager
def null_writer():
    def writedata(data):
        print(f"null->{data}")

    yield writedata


def multiwriter(w1, w2):
    w1("a1\n")
    w1("a2\n")
    w2("b1\n")
    w2("b2\n")
    w1("a3\n")
    w2("b3\n")


def process_write(file_a, file_b):
    with (output_writer_a(file_a) if file_a else null_writer()) as wrt_a, (
        output_writer_b(file_b) if file_b else null_writer()
    ) as wrt_b:
        multiwriter(wrt_a, wrt_b)


if __name__ == "__main__":
    file_a = None  # "./output/file-a.txt"
    file_b = "./output/file-b.txt"

    process_write(file_a, file_b)
