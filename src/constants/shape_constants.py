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
CHUNK_SIZE = 64
CHUNK_HEIGHT = 256
FREQUENCY = 50
AMPLITUDE = 10