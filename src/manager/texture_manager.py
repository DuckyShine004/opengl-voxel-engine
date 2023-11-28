"""This module is useful for managing textures."""

from __future__ import annotations

import numpy

from OpenGL.GL import *

from PIL import Image

from src.constants.file_constants import TEXTURE_LOCATION
from src.constants.shape_constants import TEXTURE_WIDTH, TEXTURE_HEIGHT


class TextureManager:

    """A class interface which allows users to call useful texture manager
    methods without creating an instance."""

    @staticmethod
    def get_texture(texture_type: str) -> numpy.ndarray:
        """Return the texture data for the given texture type.

        Args:
            texture_type (str): the type of texture.

        Returns:
            numpy.ndarray: A numpy array of texture data.
        """

        filename = TextureManager.get_filename(texture_type)
        image = Image.open(filename)
        texture_data = numpy.array(image.convert("RGBA"), dtype="uint8")

        return texture_data

    @staticmethod
    def get_filename(texture_type: str) -> str:
        """Return the full filename for the given texture type.

        Args:
            texture_type (str): The type of texture.

        Returns:
            str: The full filename path.
        """

        texture_location = TEXTURE_LOCATION + texture_type + "/"
        filename = texture_location + texture_type + "_atlas.png"

        return filename
