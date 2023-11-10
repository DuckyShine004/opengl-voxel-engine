"""This module is essentially utilised for terrain management.

It is not a manager itself because this is not a generic manager class.
"""
from __future__ import annotations

from numba import njit

from world.noise import get_noise_2d, get_noise_3d

from constants.shape_constants import CHUNK_SIZE, CHUNK_HEIGHT, FREQUENCY, AMPLITUDE


class Terrain:

    """The Terrain class will handle all things related to terrain."""

    @staticmethod
    @njit
    def get_height(x: float, y: float, exp: float = 1.7, persistence: float = 0.3) -> float:
        """Returns the height map for the given x, y coordinates. The
        parameters can be adjusted to get the desired height map, or terrain.

        Args:
            x (float): The x coordinate for noise sampling.
            y (float): The y coordinate for noise sampling.
            exp (float, optional): The exponential value which exponentiates the noise value.
            persistence (float, optional): How detailed we want the terrain to be.

        Returns:
            float: The noise value.
        """

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

    @staticmethod
    @njit
    def set_chunk() -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Sets the chunk for the given x, and z positions. If the chunk has
        already been set, then we simply return nothing.

        Returns:
            Tuple[numpy.ndarray, numpy.ndarray]: Returns two values, the voxel position data,
            and the voxel texture data.
        """

        voxel_data = []

        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                dx = AMPLITUDE * (x / FREQUENCY)
                dz = AMPLITUDE * (z / FREQUENCY)

                y = Terrain.get_height(dx, dz)

                translations.append((glm.vec3(x, y, z), 0))

                for d in range(10):
                    dy = y - d - 1

                    if d <= 5:
                        translations.append((glm.vec3(x, dy, z), 1))
                    else:
                        translations.append((glm.vec3(x, dy, z), 2))

        position_data = numpy.array([voxel_data[0] for voxel_datum in voxel_data], dtype="float32")
        texture_data = numpy.array([voxel_data[1] for voxel_datum in voxel_data], dtype="float32")

        return position_data, texture_data
