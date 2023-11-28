"""Shape constants, like texture constants and voxel / cube constants, and
chunk constants.

Attributes:
    AMPLITUDE (int): The amplitude of the noise value.
    CHUNK_HEIGHT (int): The chunk height.
    CHUNK_SIZE (int): The width and length of a chunk.
    CUBE_INDICES (TYPE): The cube's indices.
    CUBE_UVS (TYPE): The cube's UVs.
    CUBE_VERTICES (TYPE): The cube's vertices.
    EXPONENT (float): The exponential value for the noise.
    FREQUENCY (int): The frequency for the noise.
    OCTAVES (int): The number of noise sampling octaves.
    PERSISTENCE (float): The persistence value of the noise.
    TEXTURE_HEIGHT (int): The height of the texture.
    TEXTURE_WIDTH (int): The width of the texture.
    UV_HEIGHT (TYPE): The height of each sub texture in UV coordinates.
    UV_WIDTH (TYPE): The width of each sub texture in UV coordinates.
"""

import numpy

# Textures
TEXTURE_WIDTH = 64
TEXTURE_HEIGHT = 48

# UVs
UV_WIDTH = 1.0 / 4
UV_HEIGHT = 1.0 / 3

# Cube
CUBE_VERTICES = numpy.array(
    [
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [0.5, -0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, 0.5, 0.5],
        [0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
    ],
    dtype="float32",
)

CUBE_INDICES = numpy.array(
    [
        [0, 2, 1],  # front
        [1, 2, 3],
        [4, 5, 6],  # back
        [5, 7, 6],
        [6, 7, 8],  # top
        [7, 9, 8],
        [1, 3, 4],  # bottom
        [3, 5, 4],
        [1, 11, 10],  # left
        [1, 4, 11],
        [3, 12, 5],  # right
        [5, 12, 13],
    ],
    dtype="uint32",
)

CUBE_UVS = numpy.array(
    [
        [0 * UV_WIDTH, 2 * UV_HEIGHT],
        [1 * UV_WIDTH, 2 * UV_HEIGHT],
        [0 * UV_WIDTH, 1 * UV_HEIGHT],
        [1 * UV_WIDTH, 1 * UV_HEIGHT],
        [2 * UV_WIDTH, 2 * UV_HEIGHT],
        [2 * UV_WIDTH, 1 * UV_HEIGHT],
        [3 * UV_WIDTH, 2 * UV_HEIGHT],
        [3 * UV_WIDTH, 1 * UV_HEIGHT],
        [4 * UV_WIDTH, 2 * UV_HEIGHT],
        [4 * UV_WIDTH, 1 * UV_HEIGHT],
        [1 * UV_WIDTH, 3 * UV_HEIGHT],
        [2 * UV_WIDTH, 3 * UV_HEIGHT],
        [1 * UV_WIDTH, 0 * UV_HEIGHT],
        [2 * UV_WIDTH, 0 * UV_HEIGHT],
    ],
    dtype="float32",
)

# Chunk
CHUNK_SIZE = 16
CHUNK_HEIGHT = 256

# Noise
FREQUENCY = 50
AMPLITUDE = 10
OCTAVES = 4
EXPONENT = 1.70
PERSISTENCE = 0.30
