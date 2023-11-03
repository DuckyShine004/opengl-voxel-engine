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
    CAMERA_PITCH_LIMIT
)


class Camera:
    def __init__(self, position: glm.vec3 = glm.vec3(0.0, 0.0, 0.0)) -> None:
        self.__position = position

        self.__model = glm.mat4(1.0)
        self.__view = glm.mat4(1.0)
        self.__projection = glm.mat4(1.0)

        self.__front = glm.vec3(0.0, 0.0, -1.0)
        self.__up = glm.vec3(0.0, 1.0, 0.0)

        self.__last_frame = 0.0

        self.__is_first_mouse = True

        self.__yaw = CAMERA_INITIAL_YAW
        self.__pitch = CAMERA_INITIAL_PITCH

        self.__last_mouse_x = SCREEN_HEIGHT // 2
        self.__last_mouse_y = SCREEN_HEIGHT // 2

    def update(self, shader_manager: ShaderManager, window: glfw.GLFWwindow, time: float) -> None:
        self.__process_inputs(window, time)
        self.__update_projection_matrix()
        self.__view = glm.lookAt(self.__position, self.__position + self.__front, self.__up)

        shader_manager.set_matrix_float_4_location("view_matrix", self.__view)
        shader_manager.set_matrix_float_4_location("projection_matrix", self.__projection)
        shader_manager.set_matrix_float_4_location("model_matrix", self.__model)

    def __update_projection_matrix(self) -> None:
        aspect_ratio = SCREEN_WIDTH / SCREEN_HEIGHT

        self.__projection = glm.perspective(
            glm.radians(CAMERA_PERSPECTIVE_FOV), aspect_ratio, CAMERA_NEAR_CLIP, CAMERA_FAR_CLIP
        )

    def __get_local_time(self, time: float) -> float:
        delta_time = time - self.__last_frame
        self.__last_frame = time

        return delta_time

    def __process_inputs(self, window: glfw.GLFWwindow, time: float) -> None:
        self.__keyboard_callback(window, time)
        glfw.set_cursor_pos_callback(window, self.__mouse_callback)

    def __keyboard_callback(self, window: glfw.GLFWwindow, time: float) -> None:
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

    def __mouse_callback(
        self, window: glfw.GLFWwindow, current_mouse_x: float, current_mouse_y: float
    ) -> None:
        offset_mouse_x = (current_mouse_x - self.__last_mouse_x) * CAMERA_SENSITIVITY
        offset_mouse_y = (self.__last_mouse_y - current_mouse_y) * CAMERA_SENSITIVITY

        self.__last_mouse_x = current_mouse_x
        self.__last_mouse_y = current_mouse_y

        self.__update_direction(offset_mouse_x, offset_mouse_y)

    def __update_direction(self, offset_mouse_x: float, offset_mouse_y: float) -> None:
        self.__yaw += offset_mouse_x
        self.__pitch += offset_mouse_y

        self.__pitch = Utility.clamp(self.__pitch, -CAMERA_PITCH_LIMIT, CAMERA_PITCH_LIMIT)

        direction = glm.vec3(
            cos(glm.radians(self.__yaw)) * cos(glm.radians(self.__pitch)),
            sin(glm.radians(self.__pitch)),
            sin(glm.radians(self.__yaw)) * cos(glm.radians(self.__pitch)),
        )

        self.__front = glm.normalize(direction)
