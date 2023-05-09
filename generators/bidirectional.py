def printer():
    while True:
        text = yield
        print(f": {text} #")


def echoer():
    while True:
        text = yield f": {text} #"


if __name__ == "__main__":
    # prt = printer()
    # next(prt)
    # prt.send("asdasdasd")
    # prt.send("qwewqeqwe")
    # prt.send("zxczxczzx")

    echo = echoer()
    next(echo)
    for text in ["aaa", "bbb", "ccc"]:
        print(echo.send(text))
