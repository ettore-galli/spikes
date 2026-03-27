from dataclasses import dataclass
from math import pi, tan
from typing import List, Tuple


@dataclass
class PhysicalSpecs:
    z_stub_line: complex
    z_half_pole: complex
    stub_length_guess: float


@dataclass
class DesignResults:
    pole_stub_impedance: complex
    short_stub_impedance: complex
    feed_point_impedance: complex


def line_impedance_tranformation(
    z_line: complex, z_load: complex, wavelength_fraction: float
) -> complex:
    return (
        z_line
        * (z_load + 1j * z_line * tan(2 * pi * wavelength_fraction))
        / (z_line + 1j * z_load * tan(2 * pi * wavelength_fraction))
    )


def parallel(z_first: complex, z_second: complex) -> complex:
    return (z_first * z_second) / (z_first + z_second)


def calculate_resulting_parameters(
    antenna_specs: PhysicalSpecs, pole_stub_length: float, short_stub_length: float
) -> DesignResults:
    stub_impedance: complex = line_impedance_tranformation(
        z_line=antenna_specs.z_stub_line,
        z_load=0.0,
        wavelength_fraction=short_stub_length,
    )

    pole_impedance: complex = line_impedance_tranformation(
        z_line=antenna_specs.z_stub_line,
        z_load=antenna_specs.z_half_pole,
        wavelength_fraction=pole_stub_length,
    )

    return DesignResults(
        pole_stub_impedance=pole_impedance,
        short_stub_impedance=stub_impedance,
        feed_point_impedance=parallel(pole_impedance, stub_impedance),
    )


def calculate_optimal_design(antenna_specs: PhysicalSpecs) -> DesignResults:
    pass


def calc_quarter_range(top_value: float = 25.0, number_of_points=20) -> List[float]:
    zero_quarter_range: List[float] = [
        top_value * (x / (number_of_points) / 100) for x in range(number_of_points + 1)
    ]
    return zero_quarter_range


def calculate_j_pole_feed_impedance(
    antenna_specs: PhysicalSpecs,
) -> Tuple[List[float], List[DesignResults]]:

    stub_length_range = calc_quarter_range(top_value=25)

    results = [
        calculate_resulting_parameters(
            antenna_specs=antenna_specs,
            pole_stub_length=x,
            short_stub_length=antenna_specs.stub_length_guess - x,
        )
        for x in stub_length_range
    ]

    return stub_length_range, results


def plot(
    title: str,
    ascissa: List[float],
    data: List[float],
):

    half_axis = 30
    zero_point = "|"
    data_range = max(abs(min(*data)), abs(max(*data))) or 1

    def calc_range_space(value: float):
        return int(half_axis * (abs(value)) / (data_range))

    print(f"\n{title}\n")

    for ascissa_value, data_value in zip(ascissa, data):
        value_plot = f"{round(data_value, 1)}".rjust(10)
        ascissa_plot = f"{round(ascissa_value, 3)}".rjust(10)
        stars_plot = "*" * calc_range_space(data_value)
        plot_axis = (
            stars_plot.rjust(half_axis) + zero_point + "".ljust(half_axis)
            if data_value < 0
            else "".rjust(half_axis) + zero_point + stars_plot.ljust(half_axis)
        )

        print(ascissa_plot, value_plot, plot_axis)


def j_pole_workflow():
    stub_length_range: List[float]
    results: List[DesignResults]
    stub_length_range, results = calculate_j_pole_feed_impedance(
        antenna_specs=PhysicalSpecs(
            z_half_pole=3000, z_stub_line=300, stub_length_guess=0.25
        )
    )

    plot(
        "feed real",
        stub_length_range,
        [result.feed_point_impedance.real for result in results],
    )
    plot(
        "feed imag",
        stub_length_range,
        [result.feed_point_impedance.imag for result in results],
    )

    plot(
        "stub imag",
        stub_length_range,
        [result.short_stub_impedance.imag for result in results],
    )
    plot(
        "pole imag",
        stub_length_range,
        [result.pole_stub_impedance.imag for result in results],
    )


if __name__ == "__main__":
    j_pole_workflow()
