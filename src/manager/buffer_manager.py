from __future__ import annotations

from OpenGL.GL import *

class BufferManager:

    @staticmethod
    def get_vertex_array():
        vertex_array = glGenVertexArrays(1)
        glBindVertexArray(vertex_array)

        return vertex_array
    
    @staticmethod
    def get_buffer():
        buffer = glGenBuffers(1)

        return bufferarray

    @staticmethod    
    def bind_buffer_data(self, buffer, data, target):
        glBindBuffer(target, buffer)
        glBufferData(target, data, GL_STATIC_DRAW)

    @staticmethod
    def send_buffer_data(self, index, size, instancing=False):
        glVertexAttribPointer(index, size, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(index)

        if instancing:
            glVertexAttribDivisor(index, 1)
