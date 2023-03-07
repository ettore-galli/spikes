from typing import List


def crea_matrice(size: int, stars: int):
    return [
        [
            1 if i < stars or size - i < (stars + 1) or j < stars or size - j < (stars + 1) else 0
            for i in range(size)
        ]
        for j in range(size)
    ]


def render_matrice(matrice: List[List[int]]):
    for row in matrice:
        print("".join([str(item) for item in row]))


if __name__ == "__main__":

    render_matrice(crea_matrice(size=4, stars=0))

    render_matrice(crea_matrice(size=4, stars=1))

    render_matrice(crea_matrice(size=12, stars=3))

    render_matrice(crea_matrice(size=15, stars=1))
