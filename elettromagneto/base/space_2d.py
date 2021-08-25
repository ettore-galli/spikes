from typing import List, Tuple, Dict, Any, Optional

import attr

Point2D = Tuple[float, float]

SpaceRange2D = List[List[Point2D]]


@attr.s
class ScalarValue:
    value: float = attr.ib()


ScalarSpace2D = Dict[Point2D, ScalarValue]


@attr.s
class ScalarSource:
    point: Point2D = attr.ib()
    value: float = attr.ib()


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
        self.scalar_sources: List[ScalarSource] = []

    def set_scalar_value(self, point: Point2D, value: ScalarValue):
        self.values[point] = value

    def get_scalar_value(self, point: Point2D, fallback: Optional[ScalarValue] = None) -> ScalarValue:
        return self.values.get(point, fallback)

    def add_scalar_source(self, source: ScalarSource):
        self.scalar_sources.append(source)

    def get_all_sources(self) -> List[ScalarSource]:
        return self.scalar_sources

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
    def radius(a: Tuple, b: Tuple):
        return sum([(ta - tb) ** 2 for ta, tb in zip(a, b)]) ** 0.5
