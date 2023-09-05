from OpenGL.GL import *

class ShaderManager:
	def __init__(self) -> None:
		self.__vert_shader = glCreateShader(GL_VERTEX_SHADER)
		self.__frag_shader = glCreateShader(GL_FRAGMENT_SHADER)

		self.__vert_shader_source = None
		self.__frag_shader_source = None

		self.__shader_program = glCreateProgram()

		self.__create_shader_program()

	def __get_shaders(self, shader_location):
		vert_shader_location = shader_location + "vert_shader.glsl"
		frag_shader_location = shader_location + "frag_shader.glsl"

		with open(vert_shader_location, 'r') as vert_file:
			self.__vert_shader_source = vert_file.read()

		with open(frag_shader_location, 'r') as frag_file:
			self.__frag_shader_source = frag_file.read()

	def __compiler_shaders(self) -> None:
		glShaderSource(self.__vert_shader, 1, self.__vert_shader_source, None)
		glShaderSource(self.__frag_shader, 1, self.__frag_shader_source, None)

		glCompileShader(self.__vert_shader)
		glCompileShader(self.__frag_shader)

	def __attach_shaders(self):
		glAttachShader(self.__shader_program, self.__vert_shader)
		glAttachShader(self.__shader_program, self.__frag_shader)

		glLinkProgram(self.__shader_program)

	def __create_shader_program():
		self.__get_shaders()
		self.__compile_shaders()
		self.__attach_shaders()

	def get_shader_program():
		return self.shader_program


