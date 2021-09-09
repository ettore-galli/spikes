import math
from typing import List, Tuple, Dict, Optional

import attr

Point2D = Tuple[float, float]
SpaceRange2D = List[List[Point2D]]

ScalarValue = float
VectorValue2D = Tuple[float, float]


ScalarSpace2D = Dict[Point2D, ScalarValue]
VectorSpace2D = Dict[Point2D, VectorValue2D]


@attr.s
class ScalarSource:
    point: Point2D = attr.ib()
    value: float = attr.ib()


@attr.s
class ScalarField:
    min_value: ScalarValue = attr.ib()
    max_value: ScalarValue = attr.ib()
    values: List[List[ScalarValue]] = attr.ib()


@attr.s
class VectorField:
    values: List[List[ScalarValue]] = attr.ib()


class Space2D:
    def __init__(
        self,
        x_points: int,
        y_points: int,
        x_from: float,
        x_to: float,
        y_from: float,
        y_to: float,
    ):
        self.x_points = x_points
        self.y_points = y_points
        self.x_from = x_from
        self.x_to = x_to
        self.y_from = y_from
        self.y_to = y_to
        self.x_scale = x_to - x_from
        self.y_scale = y_to - y_from

        self.grid: SpaceRange2D = self.create_grid(
            x_from, x_to, y_from, y_to, x_points, y_points
        )
        self.values: ScalarSpace2D = {}
        self.vectors: VectorSpace2D = {}
        self.scalar_sources: List[ScalarSource] = []

    def set_scalar_value(self, point: Point2D, value: ScalarValue):
        self.values[point] = value

    def set_vector_value(self, point: Point2D, value: VectorValue2D):
        self.vectors[point] = value

    def get_scalar_value(
        self, point: Point2D, fallback: Optional[ScalarValue] = 0
    ) -> ScalarValue:
        return self.values.get(point, fallback)

    def get_vector_value(
        self,
        point: Point2D,
        fallback: Optional[VectorValue2D] = (0, 0),
    ) -> VectorValue2D:
        return self.vectors.get(point, fallback)

    def add_scalar_source(self, source: ScalarSource):
        self.scalar_sources.append(source)

    def get_all_sources(self) -> List[ScalarSource]:
        return self.scalar_sources

    def get_scalar_field(
        self,
        fallback_value: ScalarValue = 0,
        normalize: bool = False,
    ) -> ScalarField:
        min_value: ScalarValue = self.get_scalar_value(self.grid[0][0])
        max_value: ScalarValue = self.get_scalar_value(self.grid[0][0])
        scalar_field_values = []
        for grid_row in self.grid:
            row = []
            for grid_point in grid_row:
                scalar_value = self.get_scalar_value(grid_point)
                row.append(scalar_value)
                if scalar_value < min_value:
                    min_value = scalar_value
                if scalar_value > max_value:
                    max_value = scalar_value
            scalar_field_values.append(row)

        scalar_field = ScalarField(
            min_value=min_value, max_value=max_value, values=scalar_field_values
        )
        if normalize:
            return self.normalize_scalar_field(scalar_field)

        return scalar_field

    def get_vector_field(self, fallback_value: VectorValue2D = (0, 0)):
        vector_field_values = []
        for grid_row in self.grid:
            row = []
            for grid_point in grid_row:
                vector_value = self.get_vector_value(
                    grid_point, fallback=fallback_value
                )
                row.append(vector_value)
            vector_field_values.append(row)
        return vector_field_values

    def get_vector_field_matrices(
        self,
        fallback_value: Tuple[float, float] = (0, 0),
        export_nice_values: bool = False,
    ):
        field = self.get_vector_field(fallback_value=fallback_value)
        return [
            [
                [
                    Space2D.nice_value(point[i]) if export_nice_values else point[i]
                    for point in row
                ]
                for row in field
            ]
            for i in [0, 1]
        ]

    def get_x_y_grid(self):
        return [[[point[i] for point in row] for row in self.grid] for i in [0, 1]]

    @staticmethod
    def normalize_scalar_field(scalar_field: ScalarField) -> ScalarField:
        values_range: float = scalar_field.max_value - scalar_field.min_value
        return ScalarField(
            min_value=scalar_field.min_value,
            max_value=scalar_field.max_value,
            values=[
                [
                    (scalar_value - scalar_field.min_value) / values_range
                    for scalar_value in row
                ]
                for row in scalar_field.values
            ],
        )

    @staticmethod
    def nice_value(rough: float) -> float:
        return (-1 if rough < 0 else 1) * (
            abs(rough) if abs(rough) < 1 else 1 + math.log(abs(rough))
        )

    @staticmethod
    def create_grid(
        x_from: float,
        x_to: float,
        y_from: float,
        y_to: float,
        x_points: int,
        y_points: int,
    ) -> SpaceRange2D:
        return [
            [
                (
                    Space2D.point_coordinate(x_from, x_to, xp, x_points),
                    Space2D.point_coordinate(y_from, y_to, yp, y_points),
                )
                for xp in range(x_points)
            ]
            for yp in range(y_points)
        ]

    @staticmethod
    def point_coordinate(p_from: float, p_to: float, p_i: int, p_points: int):
        return p_from + p_i * (p_to - p_from) / (p_points - 1)

    @staticmethod
    def distance(a: Tuple, b: Tuple):
        return sum([(ta - tb) ** 2 for ta, tb in zip(a, b)]) ** 0.5

    @staticmethod
    def projection(v: float, a: Tuple[float, float], b: Tuple[float, float]):
        radius = Space2D.distance(a, b)
        return [v * (tb - ta) / radius for tb, ta in zip(b, a)]

    @staticmethod
    def sum_vectors(va: Tuple[float, float], vb: Tuple[float, float]):
        return list(map(sum, zip(va, vb)))
