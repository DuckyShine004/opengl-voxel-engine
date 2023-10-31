"""Summary."""
from __future__ import annotations

from constants.shape_constants import LOCAL_POSITION

class Triangle:

	"""A triangle is a set of vertices. This class provides a way to create a triangle - the get method should return the set of three vertex coordinates that define the triangle.
	
	Attributes:
	    x (float): the local x position of the triangle.
	    y (float): the local y position of the triangle.
	    z (float): the local z position of the triangle.
	"""
	
	def __init__(self):
		"""The constructor of the triangle."""
		self.__vertices = []

		self.x = LOCAL_POSITION[0]
		self.y = LOCAL_POSITION[1]
		self.z = LOCAL_POSITION[2]

	@staticmethod
	def add_vertex(x: float, y: float, z: float, depth: int = 1) -> None:
		"""Add triangle at the specified vertex coordinates. The size is specified by
  the depth parameter.

  Args:
      x (float): the x coordinate of the triangle.
      y (float): the y coordinate of the triangle.
      z (float): the z coordinate of the triangle.
      depth (int, optional): the size of the triangle.
  """
		self.__add_vertex(x, y, z, depth, depth)

	@staticmethod
	def get_vertices() -> List[float]:
		return get

	def __add_vertex(self, x: float, y: float, z: float, w: int, h: int) -> None:
		"""Add triangle at the specified vertex coordinates. The size is specified by
  the depth parameter.

  Args:
      x (int): the x coordinate of the triangle.
      y (int): the y coordinate of the triangle.
      z (int): the z coordinate of the triangle.
      w (int): the width of the triangle.
      h (int): the height of the triangle.
  """
		dx = x + self.x
		dy = y + self.y
		dz = z + self.z






