import os
import time
import tempfile


def create_return():
    with tempfile.TemporaryDirectory() as output_directory:
        fqn = os.path.join(output_directory, "myfile.txt")
        with open(fqn, "w") as outfile:
            outfile.write("Hello, world!")

        time.sleep(5)

        return open(fqn, "r")


def main():
    print(create_return().readlines())


if __name__ == "__main__":
    main()
