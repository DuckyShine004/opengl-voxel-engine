from __future__ import annotations

from numba import njit

from world.noise import get_noise_2d, get_noise_3d

class Terrain:
	@staticmethod
	@njit
	def get_height(x: float, y: float, exp: float = 1.7, persistence: float = 0.3) -> float:
		noise_value = 0.0
		amplitude_sum = 0.0

		for i in range(4):
			amplitude = pow(2, i)
			frequency = 1.0 / amplitude

			dx = persistence * frequency * x
			dy = persistence * frequency * y

			dh = get_noise_2d(dx, dy) / 2.0 + 0.5

			noise_value += amplitude * dh

			amplitude_sum += amplitude

		return int(pow(noise_value * 0.95, exp)) - (2 * amplitude_sum)
