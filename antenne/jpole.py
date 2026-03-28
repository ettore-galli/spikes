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
    stub_length: float
    feed_point: float


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
    antenna_specs: PhysicalSpecs, feed_point: float
) -> DesignResults:
    stub_impedance: complex = line_impedance_tranformation(
        z_line=antenna_specs.z_stub_line,
        z_load=0.0,
        wavelength_fraction=feed_point,
    )

    pole_impedance: complex = line_impedance_tranformation(
        z_line=antenna_specs.z_stub_line,
        z_load=antenna_specs.z_half_pole,
        wavelength_fraction=antenna_specs.stub_length_guess - feed_point,
    )

    feed_point_impedance: complex = parallel(pole_impedance, stub_impedance)

    return DesignResults(
        pole_stub_impedance=pole_impedance,
        short_stub_impedance=stub_impedance,
        feed_point_impedance=feed_point_impedance,
        stub_length=antenna_specs.stub_length_guess,
        feed_point=feed_point,
    )


def calculate_optimal_design(antenna_specs: PhysicalSpecs) -> DesignResults:
    pass


def calc_quarter_range(top_value: float = 0.25, number_of_points=100) -> List[float]:
    step_size: float = top_value / number_of_points
    zero_quarter_range: List[float] = [
        (step) * step_size for step in range(number_of_points + 1)
    ]
    return zero_quarter_range


def calculate_j_pole_feed_impedance(
    antenna_specs: PhysicalSpecs,
) -> Tuple[List[float], List[DesignResults]]:

    feed_point_range: List[float] = calc_quarter_range(
        top_value=antenna_specs.stub_length_guess / 5.0
    )

    results = [
        calculate_resulting_parameters(
            antenna_specs=antenna_specs,
            feed_point=x,
        )
        for x in feed_point_range
    ]

    return feed_point_range, results


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


def res_table(
    results: List[DesignResults],
    feed_point_decimals=3,
    value_decimals=2,
    rjust_space=15,
    debug=False,
):

    def build_table_line(values: List[str]) -> str:
        return "|".join(values)

    print(
        build_table_line(
            [
                column.rjust(rjust_space)
                for column in (
                    [
                        "stub length",
                        "feed point",
                        "stub_real_plot",
                        "stub_imag_plot",
                        "pole_imag_plot",
                        "pole_imag_plot",
                        "feed_real_plot",
                        "feed_imag_plot",
                    ]
                    if debug
                    else [
                        "stub length",
                        "feed point",
                        "feed_real_plot",
                        "feed_imag_plot",
                    ]
                )
            ]
        )
    )

    for data_item in results:
        stub_length_plot = f"{round(data_item.stub_length, feed_point_decimals)}".rjust(
            rjust_space
        )

        feed_point_plot = f"{round(data_item.feed_point, feed_point_decimals)}".rjust(
            rjust_space
        )

        stub_real_plot = (
            f"{round(data_item.short_stub_impedance.real, value_decimals)}".rjust(
                rjust_space
            )
        )
        stub_imag_plot = (
            f"{round(data_item.short_stub_impedance.imag, value_decimals)}".rjust(
                rjust_space
            )
        )
        pole_real_plot = (
            f"{round(data_item.pole_stub_impedance.real, value_decimals)}".rjust(
                rjust_space
            )
        )
        pole_imag_plot = (
            f"{round(data_item.pole_stub_impedance.imag, value_decimals)}".rjust(
                rjust_space
            )
        )
        feed_real_plot = (
            f"{round(data_item.feed_point_impedance.real, value_decimals)}".rjust(
                rjust_space
            )
        )
        feed_imag_plot = (
            f"{round(data_item.feed_point_impedance.imag, value_decimals)}".rjust(
                rjust_space
            )
        )

        print(
            build_table_line(
                [
                    stub_length_plot,
                    feed_point_plot,
                    stub_real_plot,
                    stub_imag_plot,
                    pole_real_plot,
                    pole_imag_plot,
                    feed_real_plot,
                    feed_imag_plot,
                ]
                if debug
                else [
                    stub_length_plot,
                    feed_point_plot,
                    feed_real_plot,
                    feed_imag_plot,
                ]
            )
        )


def all_plots(stub_length_range: List[float], results: List[DesignResults]):
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
        "stub real",
        stub_length_range,
        [result.short_stub_impedance.real for result in results],
    )

    plot(
        "stub imag",
        stub_length_range,
        [result.short_stub_impedance.imag for result in results],
    )

    plot(
        "pole real",
        stub_length_range,
        [result.pole_stub_impedance.real for result in results],
    )

    plot(
        "pole imag",
        stub_length_range,
        [result.pole_stub_impedance.imag for result in results],
    )


def j_pole_workflow():
    stub_length_range: List[float]
    results: List[DesignResults]
    stub_length_range, results = calculate_j_pole_feed_impedance(
        antenna_specs=PhysicalSpecs(
            z_half_pole=3000, z_stub_line=300, stub_length_guess=0.2685
        )
    )

    all_plots(stub_length_range=stub_length_range, results=results)
    res_table(stub_length_range=stub_length_range, results=results)


def j_pole_finder(
    stub_min: float = 0.23,
    stub_max: float = 0.27,
    stub_points: int = 1000,
    real_part_target: float = 50.0,
    real_part_delta: float = 1.0,
    imag_part_abs_threshold: float = 1.0,
) -> List[DesignResults]:

    result_candidates: List[DesignResults] = []

    stub_length_guess_range = [
        stub_min + idx * (stub_max - stub_min) / stub_points
        for idx in range(stub_points)
    ]

    for stub_length_guess in stub_length_guess_range:
        _, results = calculate_j_pole_feed_impedance(
            antenna_specs=PhysicalSpecs(
                z_half_pole=3000, z_stub_line=300, stub_length_guess=stub_length_guess
            )
        )
        for result in results:
            if (
                real_part_target - real_part_delta
                < result.feed_point_impedance.real
                < real_part_target + real_part_delta
            ):
                if abs(result.feed_point_impedance.imag) < imag_part_abs_threshold:
                    result_candidates.append(result)

    return result_candidates


if __name__ == "__main__":
    results = j_pole_finder()
    res_table(results=results)
