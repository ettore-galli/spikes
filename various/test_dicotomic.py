from various.dicotomic import (
    solve_dicotomic_monotonically_decreasing,
    solve_dicotomic_monotonically_increasing,
)


def test_solve_dicotomic_monotonically_increasing():
    expected_x = 2
    x = solve_dicotomic_monotonically_increasing(
        function=lambda x: x**3, target=8, x_domain=(-1000, 1000)
    )

    assert abs(x - expected_x) < 0.0001


def test_solve_dicotomic_monotonically_decreasing():
    expected_x = 4
    x = solve_dicotomic_monotonically_decreasing(
        function=lambda x: 1 / x, target=0.25, x_domain=(0.000001, 1000)
    )

    assert abs(x - expected_x) < 0.0001
