#version 430 core

in vec3 fragPos;

out vec4 FragColor;

uniform samplerCube ourCubeMap;

void main() {
	vec3 direction = normalize(fragPos);
	FragColor = texture(ourCubeMap, direction);
}