import numpy
import glm

from OpenGL.GL import *

from shape.triangle import Triangle
from shape.cube import Cube
from manager.shape_manager import ShapeManager
from manager.texture_manager import TextureManager
from constants.shape_constants import CUBE_INDICES, CUBE_COLORS
from utility.perlin_noise import PerlinNoise
from perlin import Perlin
import noise
import random

class Tests:
    @staticmethod
    def test_rainbow_triangle():
        triangle = Triangle()
        vertices = triangle.get_vertices()

        indices = numpy.array([0, 1, 3, 1, 2, 3], dtype="uint32")
        colors = numpy.array([1, 0, 0, 0, 1, 0, 0, 0, 1], dtype="float32")

        # Generate the vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        color_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Setup the vertex attribute pointer for layout location 0 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Setup the color attribute pointer for layout location 1 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)

    @staticmethod
    def test_textured_triangle():
        vertices = Triangle.get_vertices()

        TextureManager.get_texture(BLOCK_LOCATION)

        indices = numpy.array([0, 1, 3, 1, 2, 3], dtype="uint32")
        colors = numpy.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0], dtype="float32")
        textures = numpy.array([1,1,1,0,0,0,0,1], dtype="float32")

        # Generate the vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        color_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)

        texture_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, texture_vbo)
        glBufferData(GL_ARRAY_BUFFER, textures.nbytes, textures, GL_STATIC_DRAW)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Setup the vertex attribute pointer for layout location 0 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Setup the color attribute pointer for layout location 1 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)

        # Setup the texture attribute pointer for layout location 2 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, texture_vbo)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)

    @staticmethod
    def test_cube():
        ShapeManager.set_draw_mode_fill(False)
        vertices = Cube.get_vertices()

        indices = CUBE_INDICES
        colors = CUBE_COLORS

        # Generate the vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        color_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Setup the vertex attribute pointer for layout location 0 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Setup the color attribute pointer for layout location 1 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)

        translations = []
        noise = Perlin(10)

        for x in range(100):
            for z in range(100):
                y = noise.two(x, z)
                translations.append(glm.vec3(x, y, z))

        translations = numpy.array(translations, dtype = "float32")

        instance_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, translations.nbytes, translations, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)
        glVertexAttribDivisor(2, 1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return vao

    @staticmethod
    def test_textured_cube():
        ShapeManager.set_draw_mode_fill(True)
        vertices = Cube.get_vertices()

        TextureManager.bind_texture("grass")

        indices = CUBE_INDICES

        # Generate the vertex array object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Generate the vertex buffer object for OpenGL to use
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Generate the element buffer object
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Setup the vertex attribute pointer for layout location 0 in the vertex shader
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        rand_seed = random.randint(10000, 99999)
        frq = 50
        cfrq = 20
        amp = 10

        cthreshold = 0.425

        translations = []
        pnoise = Perlin(10)

        for x in range(64):
            for z in range(64):
                y = int(noise.snoise2((x + rand_seed) / frq, (z + rand_seed) / frq) * amp)
                noise_value_3d = noise.snoise3((x + rand_seed) / frq, (y + rand_seed) / frq, (z + rand_seed) / frq)
                can_spawn_voxel = noise_value_3d <= cthreshold

                if can_spawn_voxel:
                    translations.append(glm.vec3(x,y,z))

                for d in range(y - 1, -64, -1):
                    if (d > y - 5):
                        noise_value_3d = noise.snoise3((x + rand_seed) / cfrq, (d + rand_seed) / cfrq, (z + rand_seed) / cfrq)
                        can_spawn_voxel = noise_value_3d <= cthreshold

                        if can_spawn_voxel:
                            translations.append(glm.vec3(x,d,z))

                    else:
                        noise_value_3d = noise.snoise3((x + rand_seed) / cfrq, (d + rand_seed) / cfrq, (z + rand_seed) / cfrq)
                        can_spawn_voxel = noise_value_3d <= cthreshold

                        if can_spawn_voxel:
                            translations.append(glm.vec3(x,d,z))



        translations = numpy.array(translations, dtype = "float32")



        instance_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, translations.nbytes, translations, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribDivisor(1, 1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return vao, len(translations)