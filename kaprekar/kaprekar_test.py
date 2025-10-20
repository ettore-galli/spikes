from pytest import mark

from kaprekar.kaprekar import (
    get_reversed_number_digits,
    perform_kaprekar_loop,
    perform_kaprekar_step,
)


@mark.parametrize(
    "number, assumed_base, expected",
    [
        (1728, 10, [8, 2, 7, 1]),
        (47, 10, [7, 4]),
        (123456789, 10, [9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ],
)
def test_get_reversed_number_digits(number, assumed_base, expected):
    assert (
        get_reversed_number_digits(number=number, assumed_base=assumed_base) == expected
    )


@mark.parametrize(
    "number, assumed_digits, assumed_base, expected",
    [
        (1728, 4, 10, 7443),
        (3215, 4, 10, 4086),
    ],
)
def test_perform_kaprekar_step(number, assumed_digits, assumed_base, expected):
    assert (
        perform_kaprekar_step(
            number=number, assumed_digits=assumed_digits, assumed_base=assumed_base
        )
        == expected
    )


@mark.parametrize(
    "number, assumed_digits, assumed_base, expected",
    [
        (9962, 4, 10, ([7263, 5265, 3996, 6264, 4176, 6174], True)),
    ],
)
def test_perform_kaprekar_loop(number, assumed_digits, assumed_base, expected):
    assert (
        perform_kaprekar_loop(
            number=number, assumed_digits=assumed_digits, assumed_base=assumed_base
        )
        == expected
    )
