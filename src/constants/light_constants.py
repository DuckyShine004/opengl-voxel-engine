"""This module essentially provides constant values for anything related to
lighting.

Attributes:
    LIGHT_AMBIENCE (tuple): The light's ambience vector.
    LIGHT_DIFFUSE (tuple): The light's diffuse vector.
    LIGHT_DIRECTION (tuple): The light's direction vector.
    LIGHT_POSITION (tuple): The light's position vector.
    LIGHT_SPECULAR (tuple): The light's specular vector.
    MATERIAL_AMBIENCE (tuple): The material's ambience vector.
    MATERIAL_DIFFUSE (tuple): The material's diffuse vector.
    MATERIAL_SHINE (float): The material's shine value.
    MATERIAL_SPECULAR (tuple): The material's specular vector.
"""

import math

# Material lighting
MATERIAL_AMBIENCE = (1.00, 1.00, 1.00)
MATERIAL_DIFFUSE = (1.00, 1.00, 1.00)
MATERIAL_SPECULAR = (0.50, 0.50, 0.50)
MATERIAL_SHINE = 16.00

# Light source lighting
LIGHT_DIRECTION = (1.00, -1.00, -1.00)
LIGHT_POSITION = (32.00, 100.00, 32.00)
LIGHT_AMBIENCE = (0.80, 0.80, 0.80)
LIGHT_DIFFUSE = (0.50, 0.50, 0.50)
LIGHT_SPECULAR = (1.00, 1.00, 1.00)
