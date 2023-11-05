#version 430 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aOffset;

out vec3 fragPos;

uniform mat4 view_matrix;
uniform mat4 projection_matrix;

void main() {
	gl_Position = projection_matrix * view_matrix * vec4(aPos + aOffset, 1.0f);
	fragPos = aPos;
}