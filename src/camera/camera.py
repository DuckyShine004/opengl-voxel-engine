from __future__ import annotations

import glm
import glfw

class Camera:


    def __init__(self, camera_speed: float = 2.5) -> None:
        self.__position = glm.vec3(0.0, 0.0, 3.0)
        self.__speed = camera_speed

        self.__model = glm.mat4(1.0)
        self.__view = glm.mat4(1.0)
        self.__projection = glm.mat4(1.0)

        self.__front = glm.vec3(0.0, 0.0, -1.0)
        self.__up = glm.vec3(0.0, 1.0, 0.0)

        self.__last_frame = 0.0
        
    def update(self, shader_manager: ShaderManager, window, time: float) -> None:
        self.__process_inputs(window, time)

        self.__projection = glm.perspective(glm.radians(45.0), 800.0 / 600.0, 0.1, 100.0)
        self.__view = glm.lookAt(self.__position, self.__position + self.__front, self.__up)

        shader_manager.set_matrix_float_4_location("view_matrix", self.__view)
        shader_manager.set_matrix_float_4_location("projection_matrix", self.__projection)
        shader_manager.set_matrix_float_4_location("model_matrix", self.__model)

    def __get_local_time(self, time: float) -> None:
        delta_time = time - self.__last_frame
        self.__last_frame = time

        return delta_time

    def __process_inputs(self, window, time: float) -> None:
        speed = self.__speed * self.__get_local_time(time)

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        if (glfw.get_key(window, glfw.KEY_W) == glfw.PRESS):
            self.__position += speed * self.__front

        if (glfw.get_key(window, glfw.KEY_S) == glfw.PRESS):
            self.__position -= speed * self.__front

        if (glfw.get_key(window, glfw.KEY_A) == glfw.PRESS):
            self.__position -= glm.normalize(glm.cross(self.__front, self.__up)) * speed

        if (glfw.get_key(window, glfw.KEY_D) == glfw.PRESS):
            self.__position += glm.normalize(glm.cross(self.__front, self.__up)) * speed

