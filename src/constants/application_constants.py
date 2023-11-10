"""This module provides all of the necessary constants for the application.

Attributes:
    BACKGROUND_COLOR (tuple): The background color.
    CAMERA_FAR_CLIP (float): The camera's far value.
    CAMERA_INITIAL_PITCH (float): The camera's initial pitch value.
    CAMERA_INITIAL_YAW (float): The camera's initial yaw value.
    CAMERA_NEAR_CLIP (float): The camera's near value.
    CAMERA_PERSPECTIVE_FOV (float): The camera's FOV value.
    CAMERA_PITCH_LIMIT (float): The pitch limit.
    CAMERA_SENSITIVITY (float): The camera's sensitivity.
    CAMERA_SPEED (float): The camera's speed.
    SCREEN_HEIGHT (int): The screen's height.
    SCREEN_WIDTH (int): The screen's width.
"""

# Display
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0.50, 0.70, 1.00, 1.00)

# Camera
CAMERA_SPEED = 10.00
CAMERA_SENSITIVITY = 0.05
CAMERA_FAR_CLIP = 100.00
CAMERA_NEAR_CLIP = 0.10
CAMERA_PERSPECTIVE_FOV = 45.00
CAMERA_INITIAL_YAW = -90.00
CAMERA_INITIAL_PITCH = 0.00
CAMERA_PITCH_LIMIT = 89.00
