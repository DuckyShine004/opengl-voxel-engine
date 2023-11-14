"""The Camera class allows the user to freely move around the global space."""

from __future__ import annotations

import glm
import glfw

from math import sin, cos

from utility.utility import Utility

from constants.application_constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CAMERA_SPEED,
    CAMERA_SENSITIVITY,
    CAMERA_FAR_CLIP,
    CAMERA_NEAR_CLIP,
    CAMERA_INITIAL_YAW,
    CAMERA_INITIAL_PITCH,
    CAMERA_PERSPECTIVE_FOV,
    CAMERA_PITCH_LIMIT,
)


class Camera(object):

    """A camera object that manages the camera properties."""

    def __init__(self, position: glm.vec3 = glm.vec3(0.0, 0.0, 0.0)) -> None:
        """Initialize the Camera class.

        Args:
            position (glm.vec3, optional): The position at which the camera should be instantiated.
        """
        self.__width = SCREEN_WIDTH
        self.__height = SCREEN_HEIGHT

        self.__position = position

        self.__view = glm.mat4(1.0)
        self.__projection = glm.mat4(1.0)

        self.__front = glm.vec3(0.0, 0.0, -1.0)
        self.__up = glm.vec3(0.0, 1.0, 0.0)

        self.__last_frame = 0.0

        self.__yaw = CAMERA_INITIAL_YAW
        self.__pitch = CAMERA_INITIAL_PITCH

        self.__last_mouse_x = SCREEN_HEIGHT // 2
        self.__last_mouse_y = SCREEN_HEIGHT // 2

        self.__is_fullscreen = False

    def update(self, shader_manager: ShaderManager, window: glfw.GLFWwindow, time: float) -> None:
        """Update the camera, all-in-one method.

        Args:
            shader_manager (ShaderManager): The shader manager instance.
            window (glfw.GLFWwindow): The window object.
            time (float): The time elapsed.
        """

        self.__process_inputs(window, time)
        self.__update_projection_matrix()
        self.__view = glm.lookAt(self.__position, self.__position + self.__front, self.__up)

        shader_manager.set_vector_3("cameraPos", self.__position)

        shader_manager.set_matrix_float_4("view", self.__view)
        shader_manager.set_matrix_float_4("projection", self.__projection)

    def get_position(self) -> glm.vec3:
        """Return the position of the camera.

        Returns:
            glm.vec3: The position of the camera.
        """

        return self.__position

    def set_width(self, width: float) -> None:
        self.__width = width

    def set_height(self, height: float) -> None:
        self.__height = height

    def __update_projection_matrix(self) -> None:
        """Update the projection matrix."""

        aspect_ratio = self.__width / self.__height

        self.__projection = glm.perspective(
            glm.radians(CAMERA_PERSPECTIVE_FOV), aspect_ratio, CAMERA_NEAR_CLIP, CAMERA_FAR_CLIP
        )

    def __get_local_time(self, time: float) -> float:
        """Return the time between the current frame and the last frame.

        Args:
            time (float): The time elapsed.

        Returns:
            float: The time between the current frame and the last frame.
        """

        delta_time = time - self.__last_frame
        self.__last_frame = time

        return delta_time

    def __process_inputs(self, window: glfw.GLFWwindow, time: float) -> None:
        """Process all peripheral related inputs.

        Args:
            window (glfw.GLFWwindow): The window object.
            time (float): The time elapsed.
        """

        self.__keyboard_callback(window, time)
        glfw.set_cursor_pos_callback(window, self.__mouse_callback)

    def __keyboard_callback(self, window: glfw.GLFWwindow, time: float) -> None:
        """Handle the keyboard callbacks. This includes updating the camera's
        position.

        Args:
            window (glfw.GLFWwindow): The window object.
            time (float): The time elapsed.
        """

        speed = CAMERA_SPEED * self.__get_local_time(time)

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.__position += speed * self.__front

        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.__position -= speed * self.__front

        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.__position -= glm.normalize(glm.cross(self.__front, self.__up)) * speed

        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.__position += glm.normalize(glm.cross(self.__front, self.__up)) * speed

        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.__position += speed * self.__up

        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.__position -= speed * self.__up

    def __mouse_callback(
        self, window: glfw.GLFWwindow, current_mouse_x: float, current_mouse_y: float
    ) -> None:
        """Handle the mouse callback event.

        Args:
            window (glfw.GLFWwindow): The window object.
            current_mouse_x (float): The mouse's current x coordinate.
            current_mouse_y (float): The mouse's current y coordinate.
        """

        offset_mouse_x = (current_mouse_x - self.__last_mouse_x) * CAMERA_SENSITIVITY
        offset_mouse_y = (self.__last_mouse_y - current_mouse_y) * CAMERA_SENSITIVITY

        self.__last_mouse_x = current_mouse_x
        self.__last_mouse_y = current_mouse_y

        self.__update_direction(offset_mouse_x, offset_mouse_y)

    def __update_direction(self, offset_mouse_x: float, offset_mouse_y: float) -> None:
        """Update the camera's direction. This will update the rotation of the
        camera based on the user's mouse movement.

        Args:
            offset_mouse_x (float): The mouse's y coordinate offset.
            offset_mouse_y (float): The mouse's x coordinate offset.
        """

        self.__yaw += offset_mouse_x
        self.__pitch += offset_mouse_y

        self.__pitch = Utility.clamp(self.__pitch, -CAMERA_PITCH_LIMIT, CAMERA_PITCH_LIMIT)

        direction = glm.vec3(
            cos(glm.radians(self.__yaw)) * cos(glm.radians(self.__pitch)),
            sin(glm.radians(self.__pitch)),
            sin(glm.radians(self.__yaw)) * cos(glm.radians(self.__pitch)),
        )

        self.__front = glm.normalize(direction)
