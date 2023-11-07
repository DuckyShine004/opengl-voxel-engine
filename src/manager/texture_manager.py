from __future__ import annotations

import numpy

from OpenGL.GL import *

from PIL import Image

from constants.file_constants import TEXTURE_LOCATION
from constants.shape_constants import TEXTURE_WIDTH, TEXTURE_HEIGHT

class TextureManager:
    # @staticmethod
    # def get_texture(texture_type: str) -> GLuint:
    #     filenames = TextureManager.get_filenames(texture_type)

    #     texture = glGenTextures(1)
    #     glBindTexture(GL_TEXTURE_CUBE_MAP, texture)

    #     for i, filename in enumerate(filenames):
    #         image = Image.open(filename)
    #         image_data = numpy.array(list(image.getdata()), dtype="uint8")

    #         glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGB, TEXTURE_WIDTH, TEXTURE_HEIGHT, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    #     # For pixelated effect we use the nearest filtering option
    #     glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    #     glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #     glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
    #     glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    #     glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

    #     # Generate the texture mipmaps
    #     glGenerateMipmap(GL_TEXTURE_CUBE_MAP)

    #     return texture

    @staticmethod
    def get_texture(texture_type: str) -> numpy.ndarray:
        filename = TextureManager.get_filename(texture_type)
        image = Image.open(filename)
        texture_data = numpy.array(image.convert("RGBA"), dtype = "uint8")

        return texture_data

    @staticmethod
    def get_filename(texture_type: str) -> List[str]:
        texture_location = TEXTURE_LOCATION + texture_type + '/'
        filename = texture_location + texture_type + "_atlas.png"

        return filename

