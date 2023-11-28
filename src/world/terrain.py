"""This module is essentially utilised for terrain management.

It is not a manager itself because this is not a generic manager class.
"""
from __future__ import annotations

import glm
import numpy

from numba import njit

from src.world.noise import get_noise_2d, get_noise_3d

from src.constants.shape_constants import (
    CHUNK_SIZE,
    CHUNK_HEIGHT,
    FREQUENCY,
    AMPLITUDE,
    OCTAVES,
    EXPONENT,
    PERSISTENCE,
)


@njit
def _get_height(x: float, y: float) -> float:
    """Returns the height map for the given x, y coordinates. The parameters
    can be adjusted to get the desired height map, or terrain. Utilises the
    performance boost from the njit decorator.

    Args:
        x (float): The x coordinate for noise sampling.
        y (float): The y coordinate for noise sampling.

    Returns:
        float: The noise value.
    """

    noise_value = 0.0
    amplitude_sum = 0.0

    for i in range(OCTAVES):
        amplitude = pow(2, i)
        frequency = 1.0 / amplitude

        dx = PERSISTENCE * frequency * x
        dy = PERSISTENCE * frequency * y

        dh = get_noise_2d(dx, dy) / 2.0 + 0.5

        noise_value += amplitude * dh

        amplitude_sum += amplitude

    return int(pow(noise_value * 0.95, EXPONENT)) - (2 * amplitude_sum)


@njit
def _set_chunk() -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Sets the chunk for the given x, and z positions. If the chunk has
    already been set, then we simply return nothing. Utilises the performance
    boost from the njit decorator.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]: Returns two values, the voxel position data,
        and the voxel texture data.
    """

    voxel_data = []

    for x in range(CHUNK_SIZE * 4):
        for z in range(CHUNK_SIZE * 4):
            dx = AMPLITUDE * (x / FREQUENCY)
            dz = AMPLITUDE * (z / FREQUENCY)

            y = _get_height(dx, dz)

            voxel_data.append(((x, y, z), 0))

            for d in range(64):
                dy = y - d - 1

                if d <= 5:
                    voxel_data.append(((x, dy, z), 1))
                else:
                    voxel_data.append(((x, dy, z), 2))

    position_data = numpy.array([voxel_datum[0] for voxel_datum in voxel_data], dtype="float32")
    texture_data = numpy.array([voxel_datum[1] for voxel_datum in voxel_data], dtype="float32")

    return position_data, texture_data


class Terrain:

    """The Terrain class will handle all things related to terrain."""

    @staticmethod
    def get_height(x: float, y: float) -> float:
        """Returns the height map for the given x, y coordinates. The
        parameters can be adjusted to get the desired height map, or terrain.

        Args:
            x (float): The x coordinate for noise sampling.
            y (float): The y coordinate for noise sampling.

        Returns:
            float: The noise value.
        """

        return _get_height(x, y)

    @staticmethod
    def set_chunk() -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Sets the chunk for the given x, and z positions. If the chunk has
        already been set, then we simply return nothing.

        Returns:
            Tuple[numpy.ndarray, numpy.ndarray]: Returns two values, the voxel position data,
            and the voxel texture data.
        """

        return _set_chunk()
