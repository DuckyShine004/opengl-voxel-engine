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
        vbo = Buffer()
        vbo.bind_buffer_data(GL_ARRAY_BUFFER, vertices)
        vbo.send_buffer_data(0, 3)

        uv_vbo = Buffer()
        uv_vbo.bind_buffer_data(GL_ARRAY_BUFFER, uvs)
        uv_vbo.send_buffer_data(3, 2)

        # Generate the element buffer object
        ebo = Buffer()
        ebo.bind_buffer_data(GL_ELEMENT_ARRAY_BUFFER, indices)

        positions, textures = Terrain.set_chunk()

        ibo = Buffer()
        ibo.bind_buffer_data(GL_ARRAY_BUFFER, positions)
        ibo.send_buffer_data(1, 3, instancing=True)

        tbo = Buffer()
        tbo.bind_buffer_data(GL_ARRAY_BUFFER, textures)
        tbo.send_buffer_data(2, 1, instancing=True)
        
        return vao, len(positions), texture_array