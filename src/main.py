"""Summary."""
from __future__ import annotations

import glfw
import ctypes
import numpy
import glm

from OpenGL.GL import *

from math import sin, cos

from manager.shader_manager import ShaderManager
from manager.shape_manager import ShapeManager
from manager.texture_manager import TextureManager
from tests.tests import Tests
from camera.camera import Camera

from constants.file_constants import TEXTURE_LOCATION

class App:

    """Summary."""

    def __init__(self) -> None:
        """Summary."""
        self.__shader_manager: ShaderManager
        self.__window: GLFWWindow
        self.__camera: Camera

    def initialize(self) -> None:
        """Summary."""
        self.__initialize_window()
        self.__shader_manager = ShaderManager()
        self.__camera = Camera()

        self.__vao = Tests.test_cube()

        print(self.__vao)

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

        self.__window = glfw.create_window(1080, 720, "window", None, None)

        # Make the current context the application window
        glfw.make_context_current(self.__window)

        # Enable v-sync
        glfw.swap_interval(1)

    def __display(self) -> None:
        """Updates the display on every frame."""
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # for x in range(10):
        #     for z in range(10):
        #         model = glm.mat4(1.0)
        #         model = glm.translate(model, glm.vec3(x, 0, z))
        #         self.__shader_manager.set_matrix_float_4_location("model_matrix", model)

        #         glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, ctypes.c_void_p(0))
        glBindVertexArray(self.__vao)
        glDrawElementsInstanced(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None, 100)
        glBindVertexArray(0)

    def run(self):
        """Run the OpenGL application that was created."""
        self.__shader_manager.use_shader_program()
        glfw.set_input_mode(self.__window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        glEnable(GL_DEPTH_TEST); 

        while not glfw.window_should_close(self.__window):
            self.__camera.update(self.__shader_manager, self.__window, glfw.get_time())
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
