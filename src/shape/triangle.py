"""Summary."""
from __future__ import annotations

import numpy

from shape.shape import Shape


class Triangle(Shape):
    @staticmethod
    def get_vertices(
        position: Optional[Tuple[float, float, float]] = (0.0, 0.0, 0.0),
        size: Optional[float] = 0.5,
    ) -> List[float]:
        w = h = size

        x = position[0]
        y = position[1]
        z = position[2]

        vertices = numpy.array(
            [
                [w + x, h + y, 0.0],
                [w + x, -h + y, 0.0],
                [-w + x, -h + y, 0.0],
                [-w + x, h + y, 0.0],
            ],
            dtype="float32",
        )

        return vertices
