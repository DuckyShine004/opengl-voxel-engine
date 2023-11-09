import numpy
import glm

from OpenGL.GL import *

from manager.texture_manager import TextureManager
from constants.shape_constants import CUBE_VERTICES, CUBE_INDICES, CUBE_UVS
import random
from world.terrain import Terrain
from constants.shape_constants import TEXTURE_WIDTH, TEXTURE_HEIGHT
from utility.utility import Utility

class Tests:
    @staticmethod
    def test_textured_cube():
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
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        uv_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, uv_vbo)
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
        glVertexAttribPointer(3, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(3)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

        rand_seed = random.randint(10000, 99999)
        frq = 50
        cfrq = 20
        amp = 10

        cthreshold = 0.425

        translations = []


        for x in range(64):
            for z in range(64):
                y = Terrain.get_height((x / frq) * amp, (z / frq) * amp)
                translations.append((glm.vec3(x,y,z), 0))

                for d in range(64):
                    if d <= 5:
                        translations.append((glm.vec3(x,y-d-1, z), 1))
                    else:
                        translations.append((glm.vec3(x,y-d-1, z), 2))

        voxel_positions = numpy.array([translation[0] for translation in translations], dtype = "float32")

        instance_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, voxel_positions, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribDivisor(1, 1)

        texture_indices = numpy.array([translation[1] for translation in translations], dtype = "float32")
        texture_indices_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, texture_indices_vbo)
        glBufferData(GL_ARRAY_BUFFER, texture_indices, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)
        glVertexAttribDivisor(2, 1)
        
        return vao, len(voxel_positions), texture_array

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

        normals = Utility.get_cube_normals(vertices, indices)

        # Generate the vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        uv_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, uv_vbo)
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
        glVertexAttribPointer(3, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(3)

        normal_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, normal_vbo)
        glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(4)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

        rand_seed = random.randint(10000, 99999)
        frq = 50
        cfrq = 20
        amp = 10

        cthreshold = 0.425

        translations = []

        for x in range(64):
            for z in range(64):
                y = Terrain.get_height((x / frq) * amp, (z / frq) * amp)
                translations.append((glm.vec3(x,y,z), 0))

                for d in range(10):
                    if d <= 5:
                        translations.append((glm.vec3(x,y-d-1, z), 1))
                    else:
                        translations.append((glm.vec3(x,y-d-1, z), 2))

        voxel_positions = numpy.array([translation[0] for translation in translations], dtype = "float32")

        instance_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, voxel_positions, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribDivisor(1, 1)

        texture_indices = numpy.array([translation[1] for translation in translations], dtype = "float32")
        texture_indices_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, texture_indices_vbo)
        glBufferData(GL_ARRAY_BUFFER, texture_indices, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)
        glVertexAttribDivisor(2, 1)
        
        return vao, len(voxel_positions), texture_array