def printer():
    while True:
        text = yield
        print(f": {text} #")


def echoer():

    echo = None

    while True:
        text = yield echo
        echo = f": {text} #"


if __name__ == "__main__":
    # prt = printer()
    # next(prt)
    # prt.send("asdasdasd")
    # prt.send("qwewqeqwe")
    # prt.send("zxczxczzx")

    echo = echoer()
    print(dir(echo))
    next(echo)

    for text in ["aaa", "bbb", "ccc", "💥💥💥"]:
        print(echo.send(text))

    for _ in text in echo:
        for text in ["aaa", "bbb", "ccc", "💥💥💥"]:
            print(echo.send(text))