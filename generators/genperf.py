from datetime import datetime

BASE = [1, 2, 3, 4] * 100

N=10000

def try_generators():
    not_in_domain = 0
    for n in range(N):
        domain = (item for item in BASE)
        if n not in domain:
            not_in_domain += n


def try_list():
    not_in_domain = 0
    for n in range(N):
        domain = [item for item in BASE]
        if n not in domain:
            not_in_domain += n


if __name__ == "__main__":
    t0 = datetime.now()

    try_generators()

    t1 = datetime.now()

    try_list()

    t2 = datetime.now()

    print("generatori", t1 - t0)
    print("liste", t2 - t1)
