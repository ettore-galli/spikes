from typing import List, Tuple

from sandbox.plot2d import plot2dmesh

EPSILON_ZERO: float = 8.854e-12

import math


class ChargeSpace:
    def __init__(self, x_points: int, y_points: int, x_scale: float, y_scale: float):
        self.x_points = x_points
        self.y_points = y_points
        self.x_scale = x_scale
        self.y_scale = y_scale

        self.grid: List[List[List]] = self.create_grid(
            x_points, y_points, x_scale, y_scale
        )
        self.charges: List[Tuple[float, float, float]] = []

    def set_charges(self, charges: List[Tuple[float, float, float]]):
        self.charges = charges

    @staticmethod
    def create_grid(
        x_points: int, y_points: int, x_scale: float, y_scale: float
    ) -> List[List[List[float]]]:
        return [
            [
                [
                    ChargeSpace.point_coordinate(x_scale, xp, x_points),
                    ChargeSpace.point_coordinate(y_scale, yp, y_points),
                    0,
                ]
                for xp in range(x_points)
            ]
            for yp in range(y_points)
        ]

    @staticmethod
    def point_coordinate(scale: float, p: int, p_points: int):
        return p * (scale / (p_points - 1)) - scale / 2

    @staticmethod
    def single_charge_potential(charge: float, radius: float) -> float:
        return charge / (4 * math.pi * EPSILON_ZERO * radius)

    @staticmethod
    def radius(a: Tuple[float, float], b: Tuple[float, float]):
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

    def calculate_potential(self):
        minimum_radius = 2 * max(
            self.x_scale / self.x_points, self.y_scale / self.y_points
        )
        for grid_row in self.grid:
            for grid_point in grid_row:
                potential = 0
                for charge in self.charges:
                    r = self.radius(grid_point[:2], charge[:2])
                    if r > minimum_radius:
                        potential += self.single_charge_potential(charge[2], r)
                    else:
                        potential = 0
                grid_point[2] = potential

    def get_min_max_grid(self) -> Tuple[float, float, List[List[float]]]:
        min_pot = self.grid[0][0][2]
        max_pot = self.grid[0][0][2]
        grid = []
        for grid_row in self.grid:
            row = []
            for grid_point in grid_row:
                value = grid_point[2]
                row.append(value)
                if value < min_pot:
                    min_pot = value
                if value > max_pot:
                    max_pot = value
            grid.append(row)
        return min_pot, max_pot, grid

    def render_potential_ascii(self) -> str:
        # scale = (
        #    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        # )
        scale = " .:-=+*#%@"
        min_pot, max_pot, grid = self.get_min_max_grid()
        pots = ""
        for grid_row in grid:
            for value in grid_row:
                render_pot = int(
                    (len(scale) - 1) * (value - min_pot) / (max_pot - min_pot)
                )
                pots += str(scale[render_pot])
            pots += "\n"
        return pots

    def render_potential(self) -> str:

        min_pot, max_pot, grid = self.get_min_max_grid()
        plot2dmesh(grid)


def potential_calculation_workflow():
    cs = ChargeSpace(300, 300, 0.7, 0.7)
    # cs.set_charges([(-0.031, 0, -1), (0.031, 0, 1), (0, -0.031, -1), (0, 0.031, +1)])
    cs.set_charges(
        [
            (-0.031, -0.01, -1),
            (-0.031, 0, -1),
            (-0.021, 0.01, -1),
            (-0.031, -0.01, 1),
            (0.031, 0, 1),
            (0.021, 0.01, 1),
        ]
    )
    cs.calculate_potential()
    cs.render_potential()
    print(cs.render_potential_ascii())


if __name__ == "__main__":
    potential_calculation_workflow()
