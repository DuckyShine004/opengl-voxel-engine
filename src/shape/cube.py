from __future__ import annotations

import numpy

from shape.shape import Shape


class Cube(Shape):
    @staticmethod
    def get_vertices(
        position: Optional[Tuple[float, float, float]] = (0.0, 0.0, 0.0),
        size: Optional[float] = 0.5,
    ) -> List[float]:
        w = h = d = size

        x = position[0]
        y = position[1]
        z = position[2]

        # Vertices for each face
        vertices = numpy.array(
            [
                # Front face
                [-w + x, -h + y, d + z],
                [w + x, -h + y, d + z],
                [w + x, h + y, d + z],
                [-w + x, h + y, d + z],
                # Right face
                [w + x, -h + y, d + z],
                [w + x, -h + y, -d + z],
                [w + x, h + y, -d + z],
                [w + x, h + y, d + z],
                # Top face
                [-w + x, h + y, d + z],
                [w + x, h + y, d + z],
                [w + x, h + y, -d + z],
                [-w + x, h + y, -d + z],
                # Bottom face
                [-w + x, -h + y, -d + z],
                [w + x, -h + y, -d + z],
                [w + x, -h + y, d + z],
                [-w + x, -h + y, d + z],
                # Left face
                [-w + x, -h + y, -d + z],
                [-w + x, -h + y, d + z],
                [-w + x, h + y, d + z],
                [-w + x, h + y, -d + z],
                # Back face
                [w + x, -h + y, -d + z],
                [-w + x, -h + y, -d + z],
                [-w + x, h + y, -d + z],
                [w + x, h + y, -d + z],
            ],
            dtype="float32",
        )
        #         vertices = numpy.array(
        #     [
        #         [0, size, 0],
        #         [0, 0, 0],
        #         [size, size, 0],
        #         [size, 0, 0],

        #         [0, 0, size],
        #         [size, 0, size],
        #         [0, size, size],
        #         [size, size, size],

        #         [0, size, 0],
        #         [size, size, 0],

        #         [0, size, 0],
        #         [0, size, size],

        #         [size, size, 0],
        #         [size, size, size]
        #     ],
        #     dtype="float32",
        # )

        return vertices
