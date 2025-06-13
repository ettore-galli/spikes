from various.dicotomic import solve_dicotomic_monotonically_increasing


def test_solve_dicotomic_monotonically_increasing():
    delta = 0.0001
    expected_x = 2
    x = solve_dicotomic_monotonically_increasing(
        function=lambda x: x**3, target=8, x_domain=(-1000, 1000), delta=delta
    )

    assert abs(x - expected_x) < delta
