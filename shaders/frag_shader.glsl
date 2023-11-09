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

in vec3 fragPos;
in vec3 offsetPos;
in float fragTexIndex;
in vec2 fragTexCoord;
in vec3 Normal;

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
    vec3 norm = normalize(Normal);

    // Point light
    vec3 lightDir = normalize(light.position - offsetPos);

    // Directional light
    // vec3 lightDir = normalize(-light.direction);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = light.diffuse * (diff * material.diffuse);

    // Specular
    vec3 viewDir = normalize(cameraPos - offsetPos);
    vec3 reflectDir = reflect(-lightDir, norm); 
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shine);
    vec3 specular = light.specular * (spec * material.specular); 

    vec3 phong = ambient + diffuse + specular;

    float distance = length(offsetPos - cameraPos);
    float fogFactor = clamp((fogEnd - distance) / (fogEnd - fogStart), 0.0, 1.0);

    vec4 texColor = texture(ourTextureArray, vec3(fragTexCoord, fragTexIndex));
    vec3 color = phong * texColor.rgb;

    color = mix(fogColor.rgb, color, fogFactor);

    FragColor = vec4(color, 1.0);
}