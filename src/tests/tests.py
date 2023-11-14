import numpy
import glm

from OpenGL.GL import *

from manager.texture_manager import TextureManager
from constants.shape_constants import CUBE_VERTICES, CUBE_INDICES, CUBE_UVS
import random
from world.terrain import Terrain
from constants.shape_constants import TEXTURE_WIDTH, TEXTURE_HEIGHT
from utility.utility import Utility

from utility.buffer import Buffer

class Tests:
    @staticmethod
    def test_light_cube():
        texture_array = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D_ARRAY, texture_array)

        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        depth = 3

        texture_data_1 = TextureManager.get_texture("grass")
        texture_data_2 = TextureManager.get_texture("dirt")
        texture_data_3 = TextureManager.get_texture("stone")

        glTexImage3D(GL_TEXTURE_2D_ARRAY, 0, GL_RGBA, TEXTURE_WIDTH, TEXTURE_HEIGHT, depth, 0, GL_RGBA, GL_UNSIGNED_BYTE, None)

        offset_depth = 0
        glTexSubImage3D(GL_TEXTURE_2D_ARRAY, 0, 0, 0, offset_depth, TEXTURE_WIDTH, TEXTURE_HEIGHT, 1, GL_RGBA, GL_UNSIGNED_BYTE, texture_data_1)
        offset_depth += 1
        glTexSubImage3D(GL_TEXTURE_2D_ARRAY, 0, 0, 0, offset_depth, TEXTURE_WIDTH, TEXTURE_HEIGHT, 1, GL_RGBA, GL_UNSIGNED_BYTE, texture_data_2)
        offset_depth += 1
        glTexSubImage3D(GL_TEXTURE_2D_ARRAY, 0, 0, 0, offset_depth, TEXTURE_WIDTH, TEXTURE_HEIGHT, 1, GL_RGBA, GL_UNSIGNED_BYTE, texture_data_3)

        vertices = CUBE_VERTICES
        indices = CUBE_INDICES
        uvs = CUBE_UVS

        # Generate the vertex array object
        vao  = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = Buffer(vertices, GL_ARRAY_BUFFER, location=0)
        uv_vbo = Buffer(uvs, GL_ARRAY_BUFFER, location=3)
        ebo = Buffer(indices, GL_ELEMENT_ARRAY_BUFFER)

        positions, textures = Terrain.set_chunk()

        # Instancing buffers
        ibo = Buffer(positions, GL_ARRAY_BUFFER, location=1, instancing=True)
        tbo = Buffer(textures, GL_ARRAY_BUFFER, location=2, instancing=True)

        return vao, len(positions), texture_array