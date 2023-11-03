from __future__ import annotations

import numpy

from OpenGL.GL import *

from PIL import Image

class TextureManager:
	@staticmethod
	def get_texture(filename: str) -> GLuint:
		image_data = TextureManager.get_image_data(filename)
		width, height = numpy.shape(image_data)

		texture = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, texture)

		# For pixelated effect we use the nearest filtering option
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

		# Generate the texture and mipmaps
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
		glGenerateMipmap(GL_TEXTURE_2D)

		return texture


	@staticmethod
	def get_image_data(filename: str) -> _ArrayType:
		image = Image.open(filename)
		image_data = numpy.array(list(image.getdata()), dtype = "int8")

		return image_data

