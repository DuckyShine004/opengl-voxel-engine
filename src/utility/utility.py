from __future__ import annotations

import numpy

from numba import njit

class Utility:
    @staticmethod
    def clamp(value: float, minimum: float, maximum: float) -> float:
        return max(min(value, maximum), minimum)

