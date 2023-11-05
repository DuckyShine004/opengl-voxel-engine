#version 460 core

in vec3 fragPos;
in vec3 offsetPos;

out vec4 FragColor;

uniform float fogStart;
uniform float fogEnd;

uniform vec3 cameraPos;
uniform vec4 fogColor;

uniform samplerCube ourCubeMap;

void main() {
    float distance = length(offsetPos - cameraPos);
    float fogFactor = clamp((fogEnd - distance) / (fogEnd - fogStart), 0.0, 1.0);

    vec3 direction = normalize(fragPos);
    vec4 texColor = texture(ourCubeMap, direction);

    FragColor = mix(fogColor, texColor, fogFactor);
}