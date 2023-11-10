"""The shader manager will manager anything related to shaders."""

from __future__ import annotations

import glm

from OpenGL.GL import *

from constants.file_constants import SHADER_LOCATION


class ShaderManager:

    """The shader manager will manage all events related to shaders.

    For example, we might want to create a shader program.
    """

    def __init__(self) -> None:
        """Initialize the shader manager.

        It is highly advised that there only exists a single instance of
        shader manager at any time. This should be defined in the sub-
        main program.
        """

        self.__vert_shader: int = None
        self.__frag_shader: int = None
        self.__geom_shader: int = None

        self.__vert_shader_source: str = None
        self.__frag_shader_source: str = None
        self.__geom_shader_source: str = None

        self.__shader_program_id: int = None

        self.__create_shader_program()

    def __check_shader_compile_status(self, shader: int) -> None:
        """Check if the shader had compiled successfully.

        Args:
            shader (int): The shader.

        Raises:
            RuntimeError: The runtime error, due to errors in compiling the shader.
        """

        status = glGetShaderiv(shader, GL_COMPILE_STATUS)

        if not status:
            error_log = glGetShaderInfoLog(shader).decode()
            raise RuntimeError(f"Shader compilation failed:\n{error_log}")

    def __check_program_linking_status(self) -> None:
        """Check if the program had linked successfully.

        Raises:
            RuntimeError: The runtime error, due to errors in linking.
        """

        status = glGetProgramiv(self.__shader_program_id, GL_LINK_STATUS)

        if not status:
            error_log = glGetProgramInfoLog(self.__shader_program_id).decode()
            raise RuntimeError(f"Shader compilation failed:\n{error_log}")

    def __set_shaders(self):
        """Set the vertex, fragment and geometry shaders in the form of a
        string."""

        self.__vert_shader = glCreateShader(GL_VERTEX_SHADER)
        self.__frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        self.__geom_shader = glCreateShader(GL_GEOMETRY_SHADER)

        vert_shader_location = SHADER_LOCATION + "vert_shader.glsl"
        frag_shader_location = SHADER_LOCATION + "frag_shader.glsl"
        geom_shader_location = SHADER_LOCATION + "geom_shader.glsl"

        with open(vert_shader_location, "r") as vert_file:
            self.__vert_shader_source = vert_file.read()

        with open(frag_shader_location, "r") as frag_file:
            self.__frag_shader_source = frag_file.read()

        with open(geom_shader_location, "r") as geom_file:
            self.__geom_shader_source = geom_file.read()

    def __compile_shaders(self) -> None:
        """Compile the vertex, fragment, and geometry shaders."""

        glShaderSource(self.__vert_shader, self.__vert_shader_source)
        glShaderSource(self.__frag_shader, self.__frag_shader_source)
        glShaderSource(self.__geom_shader, self.__geom_shader_source)

        glCompileShader(self.__vert_shader)
        self.__check_shader_compile_status(self.__vert_shader)

        glCompileShader(self.__frag_shader)
        self.__check_shader_compile_status(self.__frag_shader)

        glCompileShader(self.__geom_shader)
        self.__check_shader_compile_status(self.__geom_shader)

    def __attach_shaders(self) -> None:
        """Attach the shaders to the shader program.

        This includes linking the program with the shaders. It is also
        important that we delete the shaders after the linking with the
        program.
        """

        self.__shader_program_id = glCreateProgram()

        glAttachShader(self.__shader_program_id, self.__vert_shader)
        glAttachShader(self.__shader_program_id, self.__frag_shader)
        glAttachShader(self.__shader_program_id, self.__geom_shader)

        glLinkProgram(self.__shader_program_id)
        self.__check_program_linking_status()

        glDeleteShader(self.__vert_shader)
        glDeleteShader(self.__frag_shader)
        glDeleteShader(self.__geom_shader)

    def __create_shader_program(self) -> None:
        """Create the OpenGL pipeline for the rendering engine to work."""

        self.__set_shaders()
        self.__compile_shaders()
        self.__attach_shaders()

    def set_integer_1(self, name: str, value: int) -> None:
        """Set an integer variable's value based on the uniform variable's
        name.

        Args:
            name (str): The uniform variable's name.
            value (int): Value of integer.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniform1i(location, value)

    def set_float_1(self, name: str, value: float) -> None:
        """Set a float variable's value based on the uniform variable's name.

        Args:
            name (str): The uniform variable's name.
            value (float): Value of float.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniform1f(location, value)

    def set_float_3(self, name: str, v0: float, v1: float, v2: float) -> None:
        """Set a vector 3 component's values based on the uniform variable's
        name.

        Args:
            name (str): The uniform variable's name.
            v0 (float): Value of index 0.
            v1 (float): Value of index 1.
            v2 (float): Value of index 2.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniform3f(location, v0, v1, v2)

    def set_float_4(self, name: str, v0: float, v1: float, v2: float, v3: float) -> None:
        """Set a vector 4 component's values based on the uniform variable's
        name.

        Args:
            name (str): The uniform variable's name.
            v0 (float): Value of index 0.
            v1 (float): Value of index 1.
            v2 (float): Value of index 2.
            v3 (float): Value of index 3.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniform4f(location, v0, v1, v2, v3)

    def set_vector_3(self, name: str, value: glm.vec3) -> None:
        """Set a vector 3 component's values based on the uniform variable's
        name.

        Args:
            name (str): The uniform variable's name.
            value (glm.vec3): The vector 3 component.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniform3fv(location, 1, glm.value_ptr(value))

    def set_matrix_float_4(self, name: str, value: glm.mat4) -> None:
        """Set a matrix 4 component's values based on the uniform variable's
        name.

        Args:
            name (str): The uniform variable's name.
            value (glm.mat4): The matrix 4 component.
        """

        location = glGetUniformLocation(self.__shader_program_id, name)
        glUniformMatrix4fv(location, 1, GL_FALSE, glm.value_ptr(value))

    def use_shader_program(self) -> None:
        """Use the shader program."""

        glUseProgram(self.__shader_program_id)
