"""
https://code.activestate.com/recipes/577749-experiment-with-kaprekars-routine/
http://en.wikipedia.org/wiki/6174_(number)
"""


def get_reversed_number_digits(number: int, assumed_base=10):
    digits = []
    residual = number
    while True:
        digits.append(residual % assumed_base)
        if residual < assumed_base:
            break
        residual = residual // assumed_base

    return digits


def perform_kaprekar_step(number: int, assumed_digits: int = 4, assumed_base=10):

    digits = get_reversed_number_digits(number, assumed_base=assumed_base)
    upper = sum(
        [
            d * (10 ** (assumed_digits - 1 - id))
            for id, d in enumerate(sorted(digits, reverse=True))
        ]
    )
    lower = sum(
        [d * (10 ** (assumed_digits - 1 - id)) for id, d in enumerate(sorted(digits))]
    )
    return upper - lower


def perform_kaprekar_loop(
    number: int, assumed_digits: int = 4, assumed_base=10, max_iterations=1000
):
    steps = []
    step_result = number
    while (
        step_result := perform_kaprekar_step(
            number=step_result, assumed_digits=assumed_digits, assumed_base=assumed_base
        )
    ) != (steps[-1] if steps else []):
        if len(steps) > max_iterations:
            return steps, False
        steps.append(step_result)

    return steps, True


def make_loop():
    return {
        n: perform_kaprekar_loop(number=n, assumed_digits=4) for n in range(1000, 10000)
    }


if __name__ == "__main__":
    for number, sequence_result in make_loop().items():
        sequence, did_converge = sequence_result
        if did_converge:
            print(f"{number}: SUCCESS: {sequence}")
        else:
            print(f"{number}: FAIL: ...{sequence[-3:]}")
