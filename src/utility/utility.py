from __future__ import annotations

import numpy

from numba import njit

class Utility:
    @staticmethod
    def clamp(value: float, minimum: float, maximum: float) -> float:
        return max(min(value, maximum), minimum)

    @staticmethod
    @njit
    def get_cube_normals(vertices: numpy.ndarray, indices: numpy.ndarray) -> numpy.ndarray:
        normals = numpy.zeros(vertices.shape, dtype=numpy.float32)
        count = numpy.zeros(len(vertices), dtype=int)

        for i, j, k in indices:
            edge1 = vertices[j] - vertices[i]
            edge2 = vertices[k] - vertices[i]

            normal = numpy.cross(edge1, edge2)
            normal = normal / numpy.linalg.norm(normal)

            # Accumulate the normals for each vertex
            normals[i] += normal
            normals[j] += normal
            normals[k] += normal

            # Count how many times we've added a normal to these vertices
            count[i] += 1
            count[j] += 1
            count[k] += 1

        # Normalize the accumulated normals and divide by the count to get the average
        for idx in range(len(normals)):
            if count[idx] > 0:
                normals[idx] = normals[idx] / count[idx]
                normals[idx] = normals[idx] / numpy.linalg.norm(normals[idx])

        return normals

