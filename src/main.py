from __future__ import annotations

from OpenGL.GL import *

from manager.shader_manager import ShaderManager

import glfw

class App:
	def __init__(self):
		self.__shader_manager: ShaderManager
		self.__window: GLFWWindow

	def initialize(self) -> None:
		self.__initialize_window()
		self.__shader_manager = ShaderManager()

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

		self.__window = glfw.create_window(800, 800, "window", None, None)

		# Make the current context the application window 
		glfw.make_context_current(self.__window)

		# Enable v-sync
		glfw.swap_interval(1)

		# Generate the vertex array object
		vao = GLuint()

		glGenVertexArrays(1, vao)
		glBindVertexArray(vao)

	def __process_inputs(self) -> None:
		if glfw.get_key(self.__window, glfw.KEY_ESCAPE) == glfw.PRESS:
			glfw.set_window_should_close(self.__window, True)

	def __display(self) -> None:
		"""Updates the display on every frame."""
		glPointSize(30)
		glDrawArrays(GL_POINTS, 0, 1)
		
		# glClearColor(0.0, 0.0, 0.0, 1.0)
		# glClear(GL_COLOR_BUFFER_BIT)

	def run(self):
		self.__shader_manager.use_shader_program()

		# Update the window while it is not closed
		while not glfw.window_should_close(self.__window):
			self.__display()
			self.__process_inputs()

			glfw.swap_buffers(self.__window)
			glfw.poll_events()

		glfw.destroy_window(self.__window)
		glfw.terminate()
		exit(0)

if __name__ == '__main__':
	# Create the driver code
	app = App()

	# Initialize the application
	app.initialize()

	# Run the application
	app.run()
