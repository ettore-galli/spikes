from elettromagneto.base.space_2d import ScalarSource
from elettromagneto.draw.plot2d import (
    plot2dmesh,
    plot2dcontour,
    plot2dascii,
    plotquiver, streamplot,
)
from elettromagneto.electrostatic_field.electrostatic_field import (
    ElectrostaticFieldSpace2D,
)


def field_calculation_workflow():
    electrostatic_space = ElectrostaticFieldSpace2D(
        x_points=30, y_points=30, x_from=-0.5, x_to=0.5, y_from=-0.5, y_to=0.5
    )
    # electrostatic_space.add_scalar_source(ScalarSource((-0.03, -0.01), -1))
    electrostatic_space.add_scalar_source(ScalarSource((-0.1, 0), -1))
    # electrostatic_space.add_scalar_source(ScalarSource((-0.03, 0.01), -1))

    # electrostatic_space.add_scalar_source(ScalarSource((0, 0), 1))

    # electrostatic_space.add_scalar_source(ScalarSource((0.03, -0.01), 1))
    electrostatic_space.add_scalar_source(ScalarSource((0.1, 0), 1))
    # electrostatic_space.add_scalar_source(ScalarSource((0.03, 0.01), 1))

    electrostatic_space.calculate_field()

    field = electrostatic_space.get_vector_field_matrices(
        export_nice_values=False
    )

    print(field)
    u, v = field
    x, y = electrostatic_space.get_x_y_grid()
    # plot2dmesh(field)
    # plot2dcontour(potentials)
    # plot2dascii(field)
    streamplot(x, y, u, v)



if __name__ == "__main__":
    field_calculation_workflow()
