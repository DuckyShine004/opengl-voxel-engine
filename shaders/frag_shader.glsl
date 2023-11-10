#version 460 core

struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;

    float shine;
};

struct Light {
    vec3 direction;
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

in GS_OUT {
    vec3 fragPos;
    vec3 offsetPos;

    float fragTexIndex;

    vec2 fragTexCoord;
    vec3 normal;
} fs_in;

out vec4 FragColor;

uniform float fogStart;
uniform float fogEnd;

uniform vec3 cameraPos;
uniform vec4 fogColor;

uniform Material material;
uniform Light light;

uniform sampler2DArray ourTextureArray;

void main() {
    // Ambient
    vec3 ambient = light.ambient * material.ambient;

    // Diffuse
    vec3 norm = normalize(fs_in.normal);

    // Point light
    vec3 lightDir = normalize(light.position - fs_in.offsetPos);

    // Directional light
    //vec3 lightDir = normalize(-light.direction);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = light.diffuse * (diff * material.diffuse);

    // Specular
    vec3 viewDir = normalize(cameraPos - fs_in.offsetPos);
    vec3 reflectDir = reflect(-lightDir, norm); 
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shine);
    vec3 specular = light.specular * (spec * material.specular); 

    vec3 phong = ambient + diffuse + specular;

    // Fog
    float distance = length(fs_in.offsetPos - cameraPos);
    float fogFactor = clamp((fogEnd - distance) / (fogEnd - fogStart), 0.0, 1.0);

    // Texture sampling
    vec4 texColor = texture(ourTextureArray, vec3(fs_in.fragTexCoord, fs_in.fragTexIndex));
    vec3 color = phong * texColor.rgb;

    color = mix(fogColor.rgb, color, fogFactor);

    FragColor = vec4(color, 1.0);

    // Debugging
    // FragColor = vec4((fs_in.normal + 1.0) / 2.0, 1.0);
}