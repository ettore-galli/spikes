# zoom_matrix = [[0 for _ in range(fontw_z)] for _ in range(fonth_z)]

# def render_submatrix(c, r, scale):
#     return [[1 for _ in range(scale)] for _ in range(scale)]

# def replace_in_matrix(matrix, r, c, submatrix):
#     return [[ "*" if r<=c_i< for c_i, element in enumerate(row)] for r_i, row in enumerate(matrix)]


from typing import Any, List


def render_matrix(matrix):
    for row in matrix:
        rendered = " ".join([str(item) for item in row])
        print(rendered)


def replace_in_matrix(matrix, r, c, submatrix):
    return [
        [
            submatrix[r_i - r][c_i - c]
            if r <= r_i < r + len(submatrix) and c <= c_i < c + len(submatrix[0])
            else element
            for c_i, element in enumerate(row)
        ]
        for r_i, row in enumerate(matrix)
    ]


def create_matrix(rows: int, cols: int, fill: Any = 0) -> List[List[Any]]:
    return [[fill for _ in range(cols)] for _ in range(rows)]


if __name__ == "__main__":
    stars66 = create_matrix(6, 6, "*")
    render_matrix(stars66)

    print(" * ")

    plus23 = create_matrix(2, 3, "+")
    render_matrix(plus23)

    print(" = ")

    replaced = replace_in_matrix(stars66, 1, 2, plus23)
    render_matrix(replaced)
