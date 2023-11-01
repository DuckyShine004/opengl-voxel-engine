"""Summary."""
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
        self.__vert_shader: int
        self.__frag_shader: int

        self.__vert_shader_source: str
        self.__frag_shader_source: str

        self.__shader_program_id: int

        self.__create_shader_program()

    def __get_shaders(self):
        """Get the vertex shader and fragment shaders in the form of a
        string."""
        self.__vert_shader = glCreateShader(GL_VERTEX_SHADER)
        self.__frag_shader = glCreateShader(GL_FRAGMENT_SHADER)

        vert_shader_location = SHADER_LOCATION + "vert_shader.glsl"
        frag_shader_location = SHADER_LOCATION + "frag_shader.glsl"

        with open(vert_shader_location, "r") as vert_file:
            self.__vert_shader_source = vert_file.read()

        with open(frag_shader_location, "r") as frag_file:
            self.__frag_shader_source = frag_file.read()

    def __compile_shaders(self) -> None:
        """Compile the vertex and fragment shaders."""
        glShaderSource(self.__vert_shader, self.__vert_shader_source)
        glShaderSource(self.__frag_shader, self.__frag_shader_source)

        glCompileShader(self.__vert_shader)
        glCompileShader(self.__frag_shader)

    def __attach_shaders(self) -> None:
        """Attach the shaders to the shader program.

        This includes linking the program with the shaders. It is also
        important that we delete the shaders after the linking with the
        program.
        """
        self.__shader_program_id = glCreateProgram()

        glAttachShader(self.__shader_program_id, self.__vert_shader)
        glAttachShader(self.__shader_program_id, self.__frag_shader)

        glLinkProgram(self.__shader_program_id)

        glDeleteShader(self.__vert_shader)
        glDeleteShader(self.__frag_shader)

    def __create_shader_program(self) -> None:
        """Create the OpenGL pipeline for the rendering engine to work."""
        self.__get_shaders()
        self.__compile_shaders()
        self.__attach_shaders()

    def use_shader_program(self) -> None:
        """Use the shader program."""
        glUseProgram(self.__shader_program_id)
