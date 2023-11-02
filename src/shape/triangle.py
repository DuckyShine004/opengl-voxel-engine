"""Summary."""
from __future__ import annotations

import numpy

from constants.shape_constants import LOCAL_POSITION


class Triangle:
    """A triangle is a set of vertices. This class provides a way to create a triangle - the get method should return the set of three vertex coordinates that define the triangle.

    Attributes:
        x (float): the local x position of the triangle.
        y (float): the local y position of the triangle.
        z (float): the local z position of the triangle.
    """

    def __init__(
        self, position: Tuple[float, float, float] = (0.0, 0.0, 0.0), size: float = 1.0
    ) -> None:
        """The constructor of the triangle."""
        self.__x = LOCAL_POSITION[0]
        self.__y = LOCAL_POSITION[1]
        self.__z = LOCAL_POSITION[2]

        self.__vertices = self.__get_vertices(position, size)

    def get_vertices(self) -> List[float]:
        return self.__vertices

    def __get_vertices(
        self, position: Tuple[float, float, float], size: float
    ) -> List[float]:
        """Add triangle at the specified vertex coordinates. The size is specified by
        the size parameter.

        Args:
            x (float): the x coordinate of the triangle.
            y (float): the y coordinate of the triangle.
            z (float): the z coordinate of the triangle.
            size (float, optional): the size of the triangle.

            #TODO: Remember to rotate the triangles for the mesh
        """
        x, y, z = position

        w = h = d = size

        dx = x + self.__x
        dy = y + self.__y
        dz = z + self.__z

        # vertices = numpy.array([
        #     dx    , dy    , dz    ,
        #     dx + w, dy    , dz    ,
        #     dx    , dy + h, dz
        # ], dtype = "float32")

        # vertices = numpy.array(
        #     [0.5, 0.5, 0.0, 0.5, -0.5, 0.0, -0.5, -0.5, 0.0, -0.5, 0.5, 0.0],
        #     dtype="float32",
        # )

        vertices = numpy.array([0.5, -0.5, 0.0, -0.5, -0.5, 0.0, 0.0, 0.5, 0.0], dtype="float32")

        return vertices
