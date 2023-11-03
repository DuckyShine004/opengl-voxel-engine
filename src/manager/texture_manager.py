from __future__ import annotations

import numpy

from OpenGL.GL import *

from PIL import Image

class TextureManager:
	@staticmethod
	def get_texture(filename: str) -> None:

		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

	@staticmethod
	def get_image_data(filename: str) -> _ArrayType:
		image = Image.open(filename)
		image_data = numpy.array(list(image.getdata()), dtype = "int8")

		return image_data

