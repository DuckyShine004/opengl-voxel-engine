"""This module provides a way to access useful utilities."""

from __future__ import annotations

import numpy

from numba import njit


class Utility:

    """Provides an interface to call useful methods."""

    @staticmethod
    def clamp(value: float, minimum: float, maximum: float) -> float:
        """Clamps the given value between two ranges: minimum and maximum.

        Args:
            value (float): The value to be clamped.
            minimum (float): The lower bound.
            maximum (float): The upper bound.

        Returns:
            float: The clamped value.
        """

        return max(min(value, maximum), minimum)
