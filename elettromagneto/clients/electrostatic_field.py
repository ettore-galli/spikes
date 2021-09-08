from elettromagneto.base.space_2d import ScalarSource
from elettromagneto.draw.plot2d import plot2dmesh, plot2dcontour, plot2dascii
from elettromagneto.electrostatic_field.electrostatic_field import ElectrostaticPotentialsSpace2D


def field_calculation_workflow():
    electrostatic_space = ElectrostaticPotentialsSpace2D(
        x_points=200, y_points=200, x_from=-0.5, x_to=0.5, y_from=-0.5, y_to=0.5
    )
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, -0.01), -1))
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, 0), -1))
    electrostatic_space.add_scalar_source(ScalarSource((-0.03, 0.01), -1))

    electrostatic_space.add_scalar_source(ScalarSource((0.03, -0.01), 1))
    electrostatic_space.add_scalar_source(ScalarSource((0.03, 0), 1))
    electrostatic_space.add_scalar_source(ScalarSource((0.03, 0.01), 1))

    electrostatic_space.calculate_field()

    field = electrostatic_space.get_vector_field()

    print(field)
    # plot2dmesh(potentials)
    # plot2dcontour(potentials)
    plot2dascii(field)


if __name__ == "__main__":
    field_calculation_workflow()
