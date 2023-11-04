"""Summary."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Shape(ABC):

    """The abstract class shape is a parent class which all other polygons
    should reference.

    This is because, if a a shape becomes unidentifiable, we can always
    refer to the shape as a polygon.
    """

    @staticmethod
    @abstractmethod
    def get_vertices(
        position: Optional[Tuple[float, float, float]] = (0.0, 0.0, 0.0),
        size: Optional[float] = 0.5,
    ) -> numpy.array:
        """Return a numpy array of vertices.

        Args:
            position (Optional[Tuple[float, float, float]], optional): The position of the shape.
            size (Optional[float], optional): The size of the shape
        """
        pass
