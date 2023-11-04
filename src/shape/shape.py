from __future__ import annotations

from abc import ABC, abstractmethod

class Shape(ABC):

	@staticmethod
	@abstractmethod
	def get_vertices(position: Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> List[float]:
		pass