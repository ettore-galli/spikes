import sys


if __name__ == "__main__":
    for id, line in enumerate(sys.stdin):
        if line.strip() == "stop":
            break
        # print(f">> {line}")
        sys.stdout.write(f"{str(id).rjust(5, '_')}: {line} ")
