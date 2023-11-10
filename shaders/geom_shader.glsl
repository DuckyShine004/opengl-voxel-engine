#version 460 core

layout (triangles) in;
layout (triangle_strip, max_vertices = 3) out;

in VS_OUT {
    vec3 pos;
    vec3 offsetPos;
    float texIndex;
    vec2 texCoord;
} gs_in[];

out GS_OUT {
    vec3 fragPos;
    vec3 offsetPos;
    float fragTexIndex;
    vec2 fragTexCoord;
    vec3 normal;
} gs_out;

void main() {
    vec3 edge1 = gs_in[1].pos - gs_in[0].pos;
    vec3 edge2 = gs_in[2].pos - gs_in[0].pos;

    vec3 normal = normalize(cross(edge1, edge2));

    for (int i = 0; i < 3; ++i) {
        gs_out.fragPos = gs_in[i].pos;
        gs_out.offsetPos = gs_in[i].offsetPos;
        gs_out.fragTexIndex = gs_in[i].texIndex;
        gs_out.fragTexCoord = gs_in[i].texCoord;
        gs_out.normal = normal;
        
        gl_Position = gl_in[i].gl_Position;

        EmitVertex();
    }

    EndPrimitive();
}