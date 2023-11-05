#version 430 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;
layout (location = 2) in vec3 aOffset;
layout (location = 3) in vec2 aTexCoord;

out vec3 ourColor;
out vec2 texCoord;

uniform mat4 view_matrix;
uniform mat4 projection_matrix;

void main() {
	gl_Position = projection_matrix * view_matrix * vec4(aPos + aOffset, 1.0f);
	ourColor = aColor;
	texCoord = aTexCoord;
}