from __future__ import annotations

import numpy

class Utility:
	@staticmethod
	def clamp(value: float, minimum: float, maximum: float) -> float:
		return max(min(value, maximum), minimum)

	@staticmethod
	def get_cube_normals(vertices: numpy.ndarray, indices: numpy.ndarray) -> numpy.ndarray:
		normals = numpy.zeros(vertices.shape, dtype=numpy.float32)
    
	    for i, j, k in indices:
	        edge1 = vertices[j] - vertices[i]
	        edge2 = vertices[k] - vertices[i]

	        normal = numpy.cross(edge1, edge2)
	        normal = normal / numpy.linalg.norm(normal)

	        normals[i] = normal
	        normals[j] = normal
	        normals[k] = normal
	        
	    return normals

