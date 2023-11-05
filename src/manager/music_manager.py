from __future__ import annotations

import os
import random
import pygame

from constants.file_constants import MUSIC_LOCATION

class MusicManager:
    """The MusicManager class manages events related to music.

    Attributes:
    __music_path - a private variable which stores the path to our
    source of music.
    __music_list - a private variable which stores the list of all
    music in the music directory.
    __music_poll - a private variable which stores the number of
    music in the music directory.
    """

    def __init__(self) -> None:
        self.__music_list = os.listdir(MUSIC_LOCATION)
        self.__music_poll = len(self.__music_list) - 1

    def play_music(self) -> None:
        if not pygame.mixer.music.get_busy():
            music_rand = random.randint(0, self.__music_poll)
            music_path = MUSIC_LOCATION + self.__music_list[music_rand]

            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()

            print("Now playing: " + ''.join(self.__music_list[music_rand]))