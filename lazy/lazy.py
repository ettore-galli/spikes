from functools import partial


def funzione_chiamata(parametro_1, parametro_2):
    print(parametro_1, parametro_2)


def get_p1():
    print("getting p1")
    return "P1"


def get_p2():
    print("getting p2")
    return "P2"


def chiamante():
    print("PRE")
    funzione_chiamata(parametro_1=get_p1(), parametro_2=get_p2())
    print("POST")


def lazy_call(func, **kwargs):
    # Crea un wrapper che valuta i callable al momento della chiamata
    evaluated_kwargs = {k: (v() if callable(v) else v) for k, v in kwargs.items()}
    return func(**evaluated_kwargs)


def chiamante_lazy():
    print("PRE (lazy)")
    lazy_call(funzione_chiamata, parametro_1=get_p1(), parametro_2=get_p2())
    print("POST (lazy)")


if __name__ == "__main__":
    chiamante()
    chiamante_lazy()
