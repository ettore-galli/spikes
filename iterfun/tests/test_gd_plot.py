from functools import partial


def test_partial_application():
    def line_through_point(m, xp, yp, x):
        return m * (x - xp) + yp

    tangent = partial(line_through_point, 3, 4, 5)

    assert tangent(3) == 2
