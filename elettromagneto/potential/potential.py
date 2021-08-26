import math

from elettromagneto.base.physical_constants import EPSILON_ZERO
from elettromagneto.base.space_2d import Space2D, ScalarValue


class ElectrostaticPotentialsSpace2D(Space2D):
    @staticmethod
    def single_charge_potential(charge: float, radius: float) -> float:
        return charge / (4 * math.pi * EPSILON_ZERO * radius)

    def calculate_potentials(self):
        minimum_radius = 2 * max(
            self.x_scale / self.x_points, self.y_scale / self.y_points
        )
        for grid_row in self.grid:
            for grid_point in grid_row:
                potential_value = 0
                for charge in self.get_all_sources():
                    radius = Space2D.distance(grid_point, charge.point)
                    if radius > minimum_radius:
                        potential_value += self.single_charge_potential(
                            charge.value, radius
                        )
                    else:
                        potential_value = 0

                self.set_scalar_value(grid_point, ScalarValue(potential_value))
