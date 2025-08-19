# Copyright (C) [2024] [Christian Marinkovich]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# This file sets up the application window and initializes all necessary processes

"""
    File: WindowSetup.py
    Author: Christian Marinkovich
    Date: 2024-07-06
    Description:
    This file contains the script to initialize the screen and start the game.
    First, a window is created a deployed. After that, all the textures are loaded into the game. The FPS is also
    set up here.
    If fullscreen is toggled, all the textures are scaled.
"""

import win32api
import win32con
import pygame
from setup.ConfigurationSetup import settings


class GameWindow:
    _instance = None  # static private variable
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameWindow, cls).__new__(cls)
        return cls._instance

    def __init__(self, base_width=1280, base_height=720):
        if GameWindow._initialized:
            return

        GameWindow._initialized = True

        pygame.init()
        pygame.mixer.init()

        self.base_width = base_width
        self.base_height = base_height
        self.fullscreen = settings.fullscreen == 1

        self.scale_factor = 1
        self.scale_factor_X = 1
        self.scale_factor_Y = 1

        self.display_info = pygame.display.Info()
        self.current_screen_width = self.display_info.current_w
        self.current_screen_height = self.display_info.current_h

        self.screen = self._initialize_window()
        self._set_icon()
        self._load_and_blit_background()

        self.REFRESH_RATE = self._get_refresh_rate()
        self.TARGET_FPS = self.REFRESH_RATE
        self.CLOCK = pygame.time.Clock()
        self.MONITOR_DELAY = 1.0 / self.TARGET_FPS

    def _initialize_window(self):
        if self.fullscreen:
            screen = pygame.display.set_mode((self.current_screen_width, self.current_screen_height), pygame.FULLSCREEN)

            # Calculate scale factors
            if self.current_screen_height < self.current_screen_width:
                self.scale_factor = self.current_screen_height / self.base_height
            else:
                self.scale_factor = self.current_screen_width / self.base_width

            self.scale_factor_X = self.current_screen_width / self.base_width
            self.scale_factor_Y = self.current_screen_height / self.base_height

            # Aspect ratio adjustment
            decimal_aspect_ratio = 1 / (self.current_screen_width / self.current_screen_height)
            if decimal_aspect_ratio > 0.5625:  # 9/16
                new_screen_height = self.current_screen_width * 9 / 16
                self.scale_factor = new_screen_height / self.base_height
        else:
            screen = pygame.display.set_mode((self.base_width, self.base_height))
            self.current_screen_width = self.base_width
            self.current_screen_height = self.base_height

        pygame.display.set_caption("Laser Fighter")
        return screen

    def _set_icon(self):
        icon_surface = pygame.image.load("icon/Icon.png")
        pygame.display.set_icon(icon_surface)

    def _load_and_blit_background(self):
        background_path = "textures/background/Shooting_Game_Background.png"

        # Load image into memory
        background_image = pygame.image.load(background_path).convert()

        # Compute scaled dimensions
        new_width = int(background_image.get_width() * self.scale_factor_X)
        new_height = int(background_image.get_height() * self.scale_factor_Y)

        # Scale in memory (no saving to disk)
        self.bg_surface = pygame.transform.scale(background_image, (new_width, new_height))

        # Optionally flip the screen, though this doesn't do anything here unless you've drawn to the screen
        pygame.display.flip()

    def _get_refresh_rate(self):
        display_device = win32api.EnumDisplayDevices(None, 0)
        settings = win32api.EnumDisplaySettings(display_device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
        return settings.DisplayFrequency
