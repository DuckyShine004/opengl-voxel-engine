from OpenGL.GL import *

from constants.file_constants import SHADER_LOCATION

class ShaderManager:
	def __init__(self) -> None:
		self.__vert_shader: int
		self.__frag_shader: int

		self.__vert_shader_source: str
		self.__frag_shader_source: str

		self.__shader_program_id: int

		self.__create_shader_program()

	def __get_shaders(self):
		self.__vert_shader = glCreateShader(GL_VERTEX_SHADER)
		self.__frag_shader = glCreateShader(GL_FRAGMENT_SHADER)

		vert_shader_location = SHADER_LOCATION + "vert_shader.glsl"
		frag_shader_location = SHADER_LOCATION + "frag_shader.glsl"

		with open(vert_shader_location, 'r') as vert_file:
			self.__vert_shader_source = vert_file.read()

		with open(frag_shader_location, 'r') as frag_file:
			self.__frag_shader_source = frag_file.read()

	def __compile_shaders(self) -> None:
		glShaderSource(self.__vert_shader, self.__vert_shader_source)
		glShaderSource(self.__frag_shader, self.__frag_shader_source)

		glCompileShader(self.__vert_shader)
		glCompileShader(self.__frag_shader)

	def __attach_shaders(self) -> None:
		self.__shader_program_id = glCreateProgram()

		glAttachShader(self.__shader_program_id, self.__vert_shader)
		glAttachShader(self.__shader_program_id, self.__frag_shader)

		glLinkProgram(self.__shader_program_id)

	def __create_shader_program(self) -> None:
		self.__get_shaders()
		self.__compile_shaders()
		self.__attach_shaders()

	def get_shader_program(self) -> None:
		return self.__shader_program_id


