"""This module aims to create a way for the user to create buffer."""
from __future__ import annotations

from OpenGL.GL import *


class Buffer:
    """The Buffer class allows the user to create a buffer, and allows them to
    access the necessary buffer methods."""

    def __init__(
        self,
        data: numpy.ndarray,
        target: int,
        location: Optional[int] = -1,
        instancing: Optional[bool] = False,
    ) -> None:
        """The Buffer's constructor will call the initialize method which will
        initialize the buffer.

        Args:
            data (numpy.ndarray): The data being sent to the buffer.
            target (int): The GL target mode.
            location (int, optional): The location of the buffer.
            instancing (bool, optional): Instancing mode.
        """

        self.__buffer = glGenBuffers(1)

        self.__data = data
        self.__location = location
        self.__target = target
        self.__instancing = instancing

        self.__initialize()

    def __initialize(self) -> None:
        """Intializes the buffer."""

        self.bind_buffer_data(self.__target, self.__data, self.__buffer)
        self.send_buffer_data(self.__data, self.__location, self.__instancing)

    def bind_buffer_data(self, target: int, data: numpy.ndarray, buffer: int) -> None:
        """Bind the data to the specified buffer.

        Args:
            target (int): The GL target mode.
            data (numpy.ndarray): The data that we want to bind to the buffer.
            buffer (int): The buffer we want the data to be binded to.
        """

        glBindBuffer(target, buffer)
        glBufferData(target, data, GL_STATIC_DRAW)

    def send_buffer_data(self, data: numpy.ndarray, location: int, instancing: bool) -> None:
        """Send the data to the buffer after binding it. Additionally, the size
        must be given to the buffer to let the GPU know the size of the data.
        This will be calculated inside of this method.

        Args:
            data (numpy.ndarray): The data that we want to send to the buffer.
            location (int): The location of the buffer.
            instancing (bool): Instancing mode.
        """

        if location == -1:
            return

        size = data.shape[1] if len(data.shape) > 1 else 1

        glVertexAttribPointer(location, size, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(location)

        if instancing:
            glVertexAttribDivisor(location, 1)
