from __future__ import annotations

import random
import ctypes
import sys

from math import floor, sin, cos, pi

class PerlinNoise:

    @staticmethod
    def initialize(seed: float) -> None:
        random.seed(seed)

    def get_interpolation(a0: float, a1: float, w: float) -> float:
        return (a1 - a0) * ((w * (w * 6.0 - 15.0) + 10.0) * w * w * w) + a0

    @staticmethod
    def get_random_gradient(ix: int, iy: int) -> Tuple[float, float]:
        w = 8 * ctypes.sizeof(ctypes.c_uint)
        s = w // 2

        a = ix 
        b = iy

        a *= 3284157443

        b ^= a << s | a >> w-s
        b *= 1911520717

        a ^= b << s | b >> w-s
        a *= 2048419325;

        _random = a * (pi / sys.maxsize)

        return (cos(_random), sin(_random))

    @staticmethod
    def get_dot_gradient(ix: int, iy: int, x: float, y: float) -> float:
        gradient = PerlinNoise.get_random_gradient(ix, iy)

        dx = x - float(ix)
        dy = y - float(iy)

        return dx * gradient[0] + dy * gradient[1]

    @staticmethod
    def get_noise(x: float, y: float, frequency: Optional[float] = 0.20, amplitude: Optional[float] = 5.0) -> int:
        x *= frequency
        y *= frequency

        x0 = floor(x)
        x1 = x0 + 1
        y0 = floor(y)
        y1 = y0 + 1

        sx = x - float(x0)
        sy = y - float(y0)

        n0 = PerlinNoise.get_dot_gradient(x0, y0, x, y)
        n1 = PerlinNoise.get_dot_gradient(x1, y0, x, y)
        ix0 = PerlinNoise.get_interpolation(n0, n1, sx)

        n0 = PerlinNoise.get_dot_gradient(x0, y1, x, y)
        n1 = PerlinNoise.get_dot_gradient(x1, y1, x, y)
        ix1 = PerlinNoise.get_interpolation(n0, n1, sx)

        value = PerlinNoise.get_interpolation(ix0, ix1, sy)
        value = int(value * amplitude)

        return value