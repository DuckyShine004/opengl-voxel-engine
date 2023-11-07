#version 460 core

in vec3 offsetPos;
in float fragTexIndex;
in vec2 fragTexCoord;

out vec4 FragColor;

uniform float fogStart;
uniform float fogEnd;

uniform vec3 cameraPos;
uniform vec4 fogColor;

uniform sampler2DArray ourTextureArray;

void main() {
    float distance = length(offsetPos - cameraPos);
    float fogFactor = clamp((fogEnd - distance) / (fogEnd - fogStart), 0.0, 1.0);

    vec4 texColor = texture(ourTextureArray, vec3(fragTexCoord, fragTexIndex));

    FragColor = mix(fogColor, texColor, fogFactor);
}