from __future__ import annotations

import numpy

from shape.shape import Shape


class Cube(Shape):
    VERTICES = numpy.array([-1.0], dtype="float32")
    INDICES = numpy.array([-1.0], dtype="float32")

    @staticmethod
    def get_vertices(self):
        ...
