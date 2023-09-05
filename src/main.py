from __future__ import annotations

from OpenGL.GL import *

from manager.shader import ShaderManager

import glfw

def display() -> None:
	""" Updates the display on every frame. """
	
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT)

def main() -> None:
	""" The main driver code. """

	# Initialize glfw
	if not glfw.init():
		print("glfw failed to initialize!")
		exit(1)

	# Setup OpenGL hints and create the window
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 4)
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

	window = glfw.create_window(800, 800, "window", None, None)

	# Make the current context the application window 
	glfw.make_context_current(window)

	# Enable v-sync
	glfw.swap_interval(1)

	shader_manager = ShaderManager()

	# Update the window while it is not closed
	while not glfw.window_should_close(window):
		display()
		glfw.swap_buffers(window)
		glfw.poll_events()

	glfw.destroy_window(window)
	glfw.terminate()
	exit(0)

if __name__ == '__main__':
	main()