DATA = [
    {"id": 1},
    {"id": 2},
    {"id": 3},
    {"id": 4},
    {"id": 5},
]

# https://medium.com/analytics-vidhya/building-a-data-pipeline-with-python-generators-a80a4d19019e

def add_color(data):
    for d in data:
        yield item_add_color(d)


def add_shape(data):
    for d in data:
        yield item_add_shape(d)


def item_add_color(item):
    return {**item, "color": "red" if item["id"] % 2 == 0 else "blue"}


def item_add_shape(item):
    return {**item, "shape": "round" if item["id"] % 3 == 0 else "square"}


def pipeline(data, processors):
    pipe = processors[0](data)
    for p in processors[1:]:
        pipe = p(pipe)
    return pipe


if __name__ == '__main__':
    print(
        list(
            add_shape(add_color(DATA))
        )
    )

    print("-" * 80)

    colored = add_color(DATA)
    shaped = add_shape(colored)
    print(
        list(shaped)
    )

    print("-" * 80)

    print(
        list(
            pipeline(DATA, [add_color, add_shape])
        )
    )
