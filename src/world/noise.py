"""This module initializes and optimizes the opensimplex noise module."""
from __future__ import annotations

import sys
import random

from numba import njit

from opensimplex.internals import _noise2, _noise3, _init

perm, perm_grad_index3 = _init(seed=random.randint(0, sys.maxsize))


@njit(cache=True)
def get_noise_2d(x: float, y: float) -> float:
    """Return the 2d noise value. Most likely used to generate a height map
    value.

    Args:
        x (float): The x coordinate.
        y (float): The y coordinate.

    Returns:
        float: The 2d noise value.
    """

    return _noise2(x, y, perm)


@njit(cache=True)
def get_noise_3d(x: float, y: float, z: float) -> float:
    """Return the 3d noise value. Most likely used to compute which voxels are
    needed in the context of cave generation.

    Args:
        x (float): The x coordinate.
        y (float): The y coordinate.
        z (float): The z coordinate.

    Returns:
        float: The 3d noise value.
    """

    return _noise3(x, y, z, perm, perm_grad_index3)
