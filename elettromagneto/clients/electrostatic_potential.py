from elettromagneto.base.space_2d import ScalarSource
from elettromagneto.draw.plot2d import plot2dmesh, plot2contour
from elettromagneto.potential.potential import ElectrostaticPotentialsSpace2D


def potential_calculation_workflow():
    electrostatic_space = ElectrostaticPotentialsSpace2D(
        x_points=300, y_points=300, x_from=-0.7, x_to=0.7, y_from=-0.7, y_to=0.7
    )
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, -0.01), -1))
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, 0), -1))
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, 0.01), -1))

    electrostatic_space.add_scalar_source(ScalarSource((0.03, -0.01), 1))
    electrostatic_space.add_scalar_source(ScalarSource((0.03, 0), 1))
    electrostatic_space.add_scalar_source(ScalarSource((0.03, 0.01), 1))

    electrostatic_space.calculate_potentials()

    potentials = electrostatic_space.get_scalar_field_as_float_matrix()
    plot2dmesh(potentials)
    plot2contour(potentials)


if __name__ == "__main__":
    potential_calculation_workflow()
