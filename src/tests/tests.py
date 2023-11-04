import numpy

from OpenGL.GL import *

from shape.triangle import Triangle
from manager.texture_manager import TextureManager
from constants.file_constants import TEXTURE_LOCATION

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

        TextureManager.get_texture(TEXTURE_LOCATION)

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