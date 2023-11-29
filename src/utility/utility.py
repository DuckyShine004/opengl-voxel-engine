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

    @staticmethod
    def lerp(value: float, minimum: float, maximum: float) -> float:
        """Lerps the given value between the two ranges: minimum and maximum.
        
        Args:
            value (float): The value to be lerped.
            minimum (float): The lower bound.
            maximum (float): The upper bound.
        
        Returns:
            float: The lerped value.
        """

        return minimum + (maximum - minimum) * value
    
    @staticmethod
    def smoothstep(value : float, minimum: float, maximum: float) -> float:
        """Smoothly lerps the givel value between the two ranges: minimum and maximum.
        
        Args:
            value (float): The value to be smoothstepped.
            minimum (float): The lower bound.
            maximum (float): The upper bound.
        
        Returns:
            float: The smoothstepped value.
        """

        return Utility.lerp(value * value * (3 - 2 * value), minimum, maximum)