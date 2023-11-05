#version 460 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aOffset;

out vec3 fragPos;
out vec3 offsetPos;

uniform mat4 view;
uniform mat4 projection;

void main() {
	gl_Position = projection * view * vec4(aPos + aOffset, 1.0f);
	fragPos = aPos;
	offsetPos = aPos + aOffset;
}