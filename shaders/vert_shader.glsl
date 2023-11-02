#version 430 core

layout (location = 0) in vec3 aPos;

out vec4 vertColor;

void main(void) {
	gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
	vertColor = vec4(1.0, 1.0, 1.0, 1.0);
}