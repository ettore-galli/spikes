from probability import (
    combinazioni,
    combine_powers,
    factorial_range,
    multi_factorial_fraction,
    permutazioni,
    permutazioni_x_n,
)


def test_permutazioni():
    assert permutazioni(5) == 120
    assert permutazioni_x_n(3, 8) == 336


def test_combinazioni():
    assert combinazioni(12, 4) == 495
    assert combinazioni(10, 2) == 45
    assert combinazioni(5, 2) == 10


def test_factorial_range():
    assert factorial_range(7) == {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
    }


def test_combine_powers():
    assert combine_powers([{1: 1, 2: 3, 3: 2, 4: 1}, {2: 3, 4: 3}]) == {
        1: 1,
        2: 6,
        3: 2,
        4: 4,
    }
    assert combine_powers([{1: 1, 2: 3, 3: 2, 4: 1}, {2: 3, 4: 3}, {2: 1, 3: 1}]) == {
        1: 1,
        2: 7,
        3: 3,
        4: 4,
    }


def test_multi_factorial_fraction():
    assert multi_factorial_fraction([10], [8, 2]) == 45.0
