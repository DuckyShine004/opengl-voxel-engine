import numpy

# Cube
CUBE_INDICES = numpy.array(
    [
        [0, 1, 2],
        [2, 3, 0],
        [1, 5, 6],
        [6, 2, 1],
        [7, 6, 5],
        [5, 4, 7],
        [4, 0, 3],
        [3, 7, 4],
        [4, 5, 1],
        [1, 0, 4],
        [3, 2, 6],
        [6, 7, 3],
    ],
    dtype="uint32",
)

CUBE_COLORS = numpy.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
    ],
    dtype="float32",
)

CUBE_TEXTURE_COORDINATES = numpy.array([0,0,1,0,1,1,0,1], dtype = "float32")
