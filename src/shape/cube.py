from __future__ import annotations

import numpy

from shape.shape import Shape


class Cube(Shape):
    @staticmethod
    def get_vertices(position: Optional[Tuple[float, float, float]] = (0.0, 0.0, 0.0), size: Optional[float] = 0.5) -> List[float]:
        w = h = d = size

        x = position[0]
        y = position[1]
        z = position[2]

        vertices = numpy.array(
            [
                [-w + x, -h + y, d + z],
                [w + x, -h + y, d + z],
                [w + x, h + y, d + z],
                [-w + x, h + y, d + z],
                [-w + x, -h + y, -d + z],
                [w + x, -h + y, -d + z],
                [w + x, h + y, -d + z],
                [-w + x, h + y, -d + z],
            ],
            dtype="float32",
        )

        return vertices
