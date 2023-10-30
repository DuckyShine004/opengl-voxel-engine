from __future__ import annotations

from OpenGL.GL import *
from glfw import *

from manager.shader_manager import ShaderManager

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
		if not init():
			print("glfw failed to initialize!")
			exit(1)

		# Setup OpenGL hints and create the window
		window_hint(CONTEXT_VERSION_MINOR, 4)
		window_hint(CONTEXT_VERSION_MAJOR, 4)
		window_hint(OPENGL_PROFILE, OPENGL_CORE_PROFILE)

		self.__window = create_window(800, 800, "window", None, None)

		# Make the current context the application window 
		make_context_current(self.__window)

		# Enable v-sync
		swap_interval(1)

		# Generate the vertex array object
		vao = GLuint()

		glGenVertexArrays(1, vao)
		glBindVertexArray(vao)

	def __process_inputs(self) -> None:
		if get_key(self.__window, KEY_ESCAPE) == PRESS:
			set_window_should_close(self.__window, True)

	def __display(self) -> None:
		"""Updates the display on every frame."""
		glPointSize(30)
		glDrawArrays(GL_POINTS, 0, 1)
		
		# glClearColor(0.0, 0.0, 0.0, 1.0)
		# glClear(GL_COLOR_BUFFER_BIT)

	def run(self):
		self.__shader_manager.use_shader_program()

		# Update the window while it is not closed
		while not window_should_close(self.__window):
			self.__process_inputs()

			self.__display()

			swap_buffers(self.__window)
			poll_events()

		destroy_window(self.__window)
		terminate()
		exit(0)

if __name__ == '__main__':
	# Create the driver code
	app = App()

	# Initialize the application
	app.initialize()

	# Run the application
	app.run()
