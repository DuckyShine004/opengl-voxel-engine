from __future__ import annotations

class Utility:
	@staticmethod
	def clamp(value: float, minimum: float, maximum: float) -> float:
		return max(min(value, maximum), minimum)