import turtle


# https://www.youtube.com/watch?v=kMBj2fp52tA


def turtle_loop(until: int, *rules) -> None:
    for i in range(20000):
        for rule in rules:
            rule(i)


def r1(i: int):
    distance = 10
    angle = 11 * i
    turtle.forward(distance)
    turtle.right(angle)


def r2(i: int):
    distance = 10
    angle = -11 + 5 * (100 * i) / 100
    turtle.forward(distance)
    turtle.right(angle)


def r3(i: int):
    distance = 5 + i % 10
    angle = (distance - 3) * i
    turtle.forward(distance)
    turtle.right(angle)


def r4(i: int):
    distance = 4
    angle = -180 + i % 360
    turtle.forward(distance)
    turtle.right(angle)


def r5(i: int):
    distance = 4
    angle = -180 + i % 360
    turtle.forward(distance)
    turtle.right(angle)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.position()

    turtle_loop(20000, r5)

    turtle.done()
