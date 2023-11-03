from __future__ import annotations

import numpy

from OpenGL.GL import *

from PIL import Image

class TextureManager:
	@staticmethod
	def get_texture(filename: str) -> GLuint:
		image = Image.open(filename)
		image = image.transpose(Image.FLIP_TOP_BOTTOM)
		image_data = numpy.array(list(image.getdata()), dtype = "uint8")
		width, height = image.size[0], image.size[1]

		texture = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, texture)

		# For pixelated effect we use the nearest filtering option
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

		# Generate the texture and mipmaps, format should be set to RGBA
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
		glGenerateMipmap(GL_TEXTURE_2D)

		return texture


	@staticmethod
	def get_image_data(filename: str) -> _ArrayType:
		image = Image.open(filename)
		image_data = numpy.array(list(image.getdata()), dtype = "int8")

		return image_data

