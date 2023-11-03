from __future__ import annotations

import glm
import glfw

class Camera:


    def __init__(self, camera_speed: float = 2.5) -> None:
        self.__position = glm.vec3(0.0, 0.0, 0.0)
        self.__speed = camera_speed

        self.__front = glm.vec3(0.0, 0.0, -1.0)
        self.__up = glm.vec3(0.0, 1.0, 0.0)

        self.__last_frame = 0.0
        
    def update(self, shader_manager: ShaderManager) -> None:
        self.__view = glm.lookat(self.__position, self.__position + self.__front, self.__up)

        # Update the uniform matrix locations after updating the matrices
        self.__shader_manager.set_matrix_float_4_location("view_matrix", view)
        self.__shader_manager.set_matrix_float_4_location("projection_matrix", projection)
        self.__shader_manager.set_matrix_float_4_location("model_matrix", model)

    def __get_local_time(self, time: float) -> None:
        delta_time = time - self.__last_frame
        self.__last_frame = time

        return delta_time

    def __process_inputs(self, window, time: float) -> None:
        self.__speed *= __get_local_time(time)

        if (glfwGetKey(window, glfw.KEY_W) == glfw.PRESS):
            self.__position += self.__speed * self.__front

        if (glfwGetKey(window, glfw.KEY_S) == glfw.PRESS):
            self.__position -= self.__speed * self.__front

        if (glfwGetKey(window, glfw.KEY_A) == glfw.PRESS):
            self.__position -= glm.normalize(glm.cross(self.__front, self.__up)) * self.__speed

        if (glfwGetKey(window, glfw.GLFW_KEY_D) == glfw.GLFW_PRESS):
            self.__position += glm.normalize(glm.cross(self.__front, self.__up)) * self.__speed

