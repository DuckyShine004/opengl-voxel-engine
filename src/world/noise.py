from __future__ import annotations

import sys
import random

from numba import njit

from opensimplex.internals import _noise2, _noise3, _init

perm, perm_grad_index3 = _init(seed=random.randint(0, sys.maxsize))

@njit(cache=True)
def get_noise_2d(x: float, y: float):
	return _noise2(x, y, perm)

@njit(cache=True)
def get_noise_3d(x: float, y: float, z: float) -> float:
	return _noise3(x, y, z, perm, perm_grad_index3)