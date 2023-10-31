"""Summary."""
from __future__ import annotations

import ctypes

from OpenGL.GL import *
from glfw import *

from manager.shader_manager import ShaderManager
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
        if not init():
            print("glfw failed to initialize!")
            exit(1)

        # Setup OpenGL hints and create the window
        window_hint(CONTEXT_VERSION_MINOR, 4)
        window_hint(CONTEXT_VERSION_MAJOR, 4)
        window_hint(OPENGL_PROFILE, OPENGL_CORE_PROFILE)

        self.__window = create_window(800, 800, "window", None, None)

        # Make the current context the application window
        make_context_current(self.__window)

        # Enable v-sync
        swap_interval(1)

    def test(self):
        # Create a new instance of triangle
        triangle = Triangle()
        vertices = triangle.get_vertices()

        # Generate the vertex array object
        vao = GLuint()

        glGenVertexArrays(1, vao)
        glBindVertexArray(vao)


        # Create the vertex buffer object
        vbo = GLuint()

        # Generate buffers for OpenGL to use
        glGenBuffers(1, vbo)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Setup the vertex attribute pointer
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Use the shader program before rendering anything
        self.__shader_manager.use_shader_program()

        glBindVertexArray(vao)

    def __process_inputs(self) -> None:
        """Summary."""
        if get_key(self.__window, KEY_ESCAPE) == PRESS:
            set_window_should_close(self.__window, True)

    def __display(self) -> None:
        """Updates the display on every frame."""
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # glClearColor(0.0, 0.0, 0.0, 1.0)
        # glClear(GL_COLOR_BUFFER_BIT)

    def run(self):
        """Summary."""


        # Update the window while it is not closed
        while not window_should_close(self.__window):
            self.__process_inputs()

            self.__display()

            swap_buffers(self.__window)
            poll_events()

        destroy_window(self.__window)
        terminate()
        exit(0)


if __name__ == "__main__":
    # Create the driver code
    app = App()

    # Initialize the application
    app.initialize()

    # Run the application
    app.run()
