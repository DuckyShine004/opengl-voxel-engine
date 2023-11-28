"""Summary."""
from __future__ import annotations

import glfw
import ctypes
import numpy
import glm
import pygame
import cProfile
import pstats

from OpenGL.GL import *

from math import sin, cos

from src.manager.shader_manager import ShaderManager
from src.manager.texture_manager import TextureManager
from tests.tests import Tests
from src.camera.camera import Camera
from src.manager.music_manager import MusicManager
from src.manager.window_manager import WindowManager

from src.constants.application_constants import BACKGROUND_COLOR
from src.constants.file_constants import PROFILE_NAME

from src.constants.light_constants import (
    MATERIAL_AMBIENCE,
    MATERIAL_DIFFUSE,
    MATERIAL_SPECULAR,
    MATERIAL_SHINE,
    LIGHT_DIRECTION,
    LIGHT_POSITION,
    LIGHT_AMBIENCE,
    LIGHT_DIFFUSE,
    LIGHT_SPECULAR,
)


class App:

    """Summary."""

    def __init__(self) -> None:
        """Summary."""
        self.__shader_manager: ShaderManager
        self.__music_manager: MusicManager
        self.__window: GLFWWindow
        self.__camera: __camer
        self.__window_manager: WindowManager

    def initialize(self) -> None:
        """Summary."""
        self.__initialize_window()
        self.__shader_manager = ShaderManager()
        self.__music_manager = MusicManager()
        self.__camera = Camera()
        self.__window_manager = WindowManager(self.__window)

        self.__vao, self.__translations, self.__texture_array = Tests.test_light_cube()

    def __on_resize_callback(self, window, width, height):
        glViewport(0, 0, width, height)

        self.__camera.set_width(width)
        self.__camera.set_height(height)

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

        # Create a full-screen window with the monitor's resolution
        self.__window = glfw.create_window(1080, 720, "Minecraft", None, None)

        # Make the current context the application window
        glfw.make_context_current(self.__window)

        # Enable v-sync
        glfw.swap_interval(1)

    def __display(self) -> None:
        """Updates the display on every frame."""
        glClearColor(*BACKGROUND_COLOR)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBindTexture(GL_TEXTURE_2D_ARRAY, self.__texture_array)
        glBindVertexArray(self.__vao)
        glDrawElementsInstanced(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None, self.__translations)
        glBindVertexArray(0)

    def run(self):
        """Run the OpenGL application that was created."""
        self.__shader_manager.use_shader_program()

        glfw.set_input_mode(self.__window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_framebuffer_size_callback(self.__window, self.__on_resize_callback)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        self.__shader_manager.set_float_4("fogColor", *BACKGROUND_COLOR)
        self.__shader_manager.set_float_1("fogStart", 10.0)
        self.__shader_manager.set_float_1("fogEnd", 50.0)

        self.__shader_manager.set_float_3("material.ambient", *MATERIAL_AMBIENCE)
        self.__shader_manager.set_float_3("material.diffuse", *MATERIAL_DIFFUSE)
        self.__shader_manager.set_float_3("material.specular", *MATERIAL_SPECULAR)
        self.__shader_manager.set_float_1("material.shine", MATERIAL_SHINE)

        self.__shader_manager.set_float_3("light.direction", *LIGHT_DIRECTION)
        self.__shader_manager.set_float_3("light.position", *LIGHT_POSITION)
        self.__shader_manager.set_float_3("light.ambient", *LIGHT_AMBIENCE)
        self.__shader_manager.set_float_3("light.diffuse", *LIGHT_DIFFUSE)
        self.__shader_manager.set_float_3("light.specular", *LIGHT_SPECULAR)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D_ARRAY, self.__texture_array)
        self.__shader_manager.set_integer_1("ourTextureArray", 0)

        while not glfw.window_should_close(self.__window):
            self.__window_manager.update()
            self.__camera.update(self.__shader_manager, self.__window, glfw.get_time())
            self.__display()
            self.__music_manager.play_music()

            glfw.swap_buffers(self.__window)
            glfw.poll_events()

        glfw.destroy_window(self.__window)
        glfw.terminate()

def main() -> None:
    app = App()

    # Initialize the application
    app.initialize()

    # Run the application
    app.run()
 
if __name__ == "__main__":
    with cProfile.Profile() as profile:
        main()

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=PROFILE_NAME)