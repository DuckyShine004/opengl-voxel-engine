"""Summary."""
from __future__ import annotations

import glfw
import ctypes
import numpy

from OpenGL.GL import *
from math import sin, cos

from manager.shader_manager import ShaderManager
from manager.shape_manager import ShapeManager
from shape.triangle import Triangle


class App:

    """Summary."""

    def __init__(self) -> None:
        """Summary."""
        self.__shader_manager: ShaderManager
        self.__window: GLFWWindow

    def initialize(self) -> None:
        """Summary."""
        self.__initialize_window()
        self.__shader_manager = ShaderManager()
        self.test()

    def __initialize_window(self) -> None:
        """The main driver code."""

        # Initialize glfw
        if not glfw.init():
            print("glfw failed to initialize!")
            exit(1)

        # Setup OpenGL hints and create the window
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.__window = glfw.create_window(800, 800, "window", None, None)

        # Make the current context the application window
        glfw.make_context_current(self.__window)

        # Enable v-sync
        glfw.swap_interval(1)

    def test(self):
        # Create a new instance of triangle
        triangle = Triangle()
        vertices = triangle.get_vertices()

        indices = numpy.array([0, 1, 3, 1, 2, 3], dtype="uint32")

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
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

    def __process_inputs(self) -> None:
        """Summary."""
        if glfw.get_key(self.__window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(self.__window, True)

    def __display(self) -> None:
        """Updates the display on every frame."""
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        time_value = glfw.get_time()
        green_value = sin(time_value) / 2.5
        self.__shader_manager.set_float_4_location("ourColor", 0.0, green_value, 0.0, 1.0)

        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, ctypes.c_void_p(0))

    def run(self):
        """Run the OpenGL application that was created."""
        self.__shader_manager.use_shader_program()
        ShapeManager.set_draw_mode_fill(False)

        while not glfw.window_should_close(self.__window):
            self.__process_inputs()

            self.__display()

            glfw.swap_buffers(self.__window)
            glfw.poll_events()

        glfw.destroy_window(self.__window)
        glfw.terminate()
        exit(0)


if __name__ == "__main__":
    # Create the driver code
    app = App()

    # Initialize the application
    app.initialize()

    # Run the application
    app.run()
