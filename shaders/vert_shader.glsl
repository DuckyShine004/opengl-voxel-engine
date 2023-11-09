#version 460 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aOffset;
layout (location = 2) in float aTexIndex;
layout (location = 3) in vec2 aTexCoord;
layout (location = 4) in vec3 aNormal;

out vec3 fragPos;
out vec3 offsetPos;
out float fragTexIndex;
out vec2 fragTexCoord;
out vec3 Normal;

uniform mat4 view;
uniform mat4 projection;

void main() {
	gl_Position = projection * view * vec4(aPos + aOffset, 1.0);
	fragPos = aPos;
	offsetPos = aPos + aOffset;
	fragTexIndex = aTexIndex;
	fragTexCoord = aTexCoord;
	Normal = aNormal;
}