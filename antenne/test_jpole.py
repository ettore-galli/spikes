from antenne.jpole import calc_quarter_range


def test_calc_quarter_range():
    assert calc_quarter_range(top_value=0.3, number_of_points=10) == [
        0.0,
        0.03,
        0.06,
        0.09,
        0.12,
        0.15,
        0.18,
        0.21,
        0.24,
        0.27,
        0.3,
    ]
