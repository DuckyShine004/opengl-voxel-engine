from __future__ import annotations

from OpenGL.GL import *

class Buffer:
    def __init__(self):
        self.__buffer = glGenBuffers(1)

    def bind_buffer_data(self, target, data):
        glBindBuffer(target, self.__buffer)
        glBufferData(target, data, GL_STATIC_DRAW)

    def send_buffer_data(self, index, size, instancing=False):
        glVertexAttribPointer(index, size, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(index)

        if instancing:
            glVertexAttribDivisor(index, 1)