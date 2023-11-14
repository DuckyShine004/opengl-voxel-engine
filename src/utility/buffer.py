from __future__ import annotations

from OpenGL.GL import *


class Buffer:
    def __init__(
        self, data: numpy.ndarray, target: int, location: int = -1, instancing: bool = False
    ) -> None:
        self.__buffer = glGenBuffers(1)

        self.__data = data
        self.__location = location
        self.__target = target
        self.__instancing = instancing

        self.__initialize()

    def __initialize(self) -> None:
        self.bind_buffer_data(self.__target, self.__data, self.__buffer)
        self.send_buffer_data(self.__data, self.__location, self.__instancing)

    def bind_buffer_data(self, target: int, data: numpy.ndarray, buffer: int) -> None:
        glBindBuffer(target, buffer)
        glBufferData(target, data, GL_STATIC_DRAW)

    def send_buffer_data(self, data: numpy.ndarray, location: int, instancing: bool) -> None:
        if location == -1:
            return

        size = data.shape[1] if len(data.shape) > 1 else 1

        glVertexAttribPointer(location, size, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(location)

        if instancing:
            glVertexAttribDivisor(location, 1)
