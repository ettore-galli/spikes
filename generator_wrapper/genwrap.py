def source():
    for i in range(100):
        yield {"id": i, "descr": f"item {i}"}

def wrapper(generator):
    list_accumulator = []
    for item in generator:
        list_accumulator.append(item)
        yield item
    return list_accumulator

def consumer():
    for item in wrapper(source()):
        print(item)


if __name__ == "__main__":
    consumer()
