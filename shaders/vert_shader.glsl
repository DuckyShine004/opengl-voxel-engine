#version 460 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aOffset;
layout (location = 2) in float aTexIndex;
layout (location = 3) in vec2 aTexCoord;

out VS_OUT {
    vec3 pos;
    vec3 offsetPos;
    float texIndex;
    vec2 texCoord;
} vs_out;

uniform mat4 view;
uniform mat4 projection;

void main() {
    gl_Position = projection * view * vec4(aPos + aOffset, 1.0);

    vs_out.pos = aPos;
    vs_out.offsetPos = aPos + aOffset;
    vs_out.texIndex = aTexIndex;
    vs_out.texCoord = aTexCoord;
}