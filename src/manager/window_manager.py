from __future__ import annotations

import glfw

from src.constants.application_constants import SCREEN_WIDTH, SCREEN_HEIGHT


class WindowManager:
    def __init__(self, window):
        self.__window = window

        self.__prev_key_e_state = glfw.RELEASE
        self.__prev_key_f_state = glfw.RELEASE

        self.__is_fullscreen = False

    def update(self):
        current_key_e_state = glfw.get_key(self.__window, glfw.KEY_E)
        current_key_f_state = glfw.get_key(self.__window, glfw.KEY_F)

        if current_key_e_state == glfw.PRESS and self.__prev_key_e_state == glfw.RELEASE:
            self.__toggle_cursor_mode()

        if current_key_f_state == glfw.PRESS and self.__prev_key_f_state == glfw.RELEASE:
            self.__toggle_fullscreen()

        self.__prev_key_e_state = current_key_e_state
        self.__prev_key_f_state = current_key_f_state

    def __toggle_cursor_mode(self) -> None:
        cursor_mode = glfw.get_input_mode(self.__window, glfw.CURSOR)

        if cursor_mode == glfw.CURSOR_DISABLED:
            glfw.set_input_mode(self.__window, glfw.CURSOR, glfw.CURSOR_NORMAL)
        else:
            glfw.set_input_mode(self.__window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    def __toggle_fullscreen(self):
        primary_monitor = glfw.get_primary_monitor()
        video_mode = glfw.get_video_mode(primary_monitor)

        x_resolution = video_mode.size.width
        y_resolution = video_mode.size.height

        refresh_rate = video_mode.refresh_rate

        if self.__is_fullscreen:
            glfw.set_window_monitor(self.__window, None, 100, 100, SCREEN_WIDTH, SCREEN_HEIGHT, 0)
        else:
            glfw.set_window_monitor(
                self.__window, primary_monitor, 0, 0, x_resolution, y_resolution, refresh_rate
            )

        self.__is_fullscreen = not self.__is_fullscreen
