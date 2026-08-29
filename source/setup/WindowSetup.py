# Copyright (C) [2026] [Christian Marinkovich]
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
import ctypes
from setup.ConfigurationSetup import settings


class GameWindow:
    """
        Represents the application window.

        Attributes:
            base_width (int): The base width of the window before scaling.
            base_height (int): The base height of the window before scaling.
            fullscreen (bool): Whether the window is initialized in fullscreen mode.

            scale_factor (float): The general scale factor applied in fullscreen mode.
            scale_factor_X (float): The scale factor for the x-axis in fullscreen mode.
            scale_factor_Y (float): The scale factor for the y-axis in fullscreen mode.

            display_info (pygame.display.Info): Object containing details about the
                current display (resolution, hardware flags, etc.).
            current_screen_width (int): The detected width of the current screen.
            current_screen_height (int): The detected height of the current screen.

            screen (pygame.Surface): The active Pygame surface used for rendering.
            REFRESH_RATE (int): The monitor’s refresh rate, detected from the system.
            TARGET_FPS (int): The target frames per second, equal to REFRESH_RATE.
            CLOCK (pygame.time.Clock): Pygame clock object used to control frame rate.
            MONITOR_DELAY (float): The time (in seconds) for a single frame, calculated
                as 1 / TARGET_FPS.
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameWindow, cls).__new__(cls)
        return cls._instance

    def __init__(self, base_width=1280, base_height=720):
        """
            Initialized the game window

            :param base_width: The base width of the screen
            :type base_width: int

            :param base_height: The base height of the screen
            :type base_height: int
        """

        if GameWindow._initialized:
            return

        GameWindow._initialized = True

        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            pass

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
        """
            Initializes the pygame window

            :return: pygame.screen
        """

        # If fullscreen mode is on
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
            # What if the aspect ratio is not 16/9?
            # With the code above, that would cause the text to go off the screen, we need to take the width of the
            #   screen and manually find its height if it had a 16/9 aspect ratio. Then, we use that in our
            #   calculations for the universal scale factor (used for text).
            # Finding aspect ratio:
            decimal_aspect_ratio = 1 / (self.current_screen_width / self.current_screen_height)
            # If it is above the target (9/16) then we need to adjust
            if decimal_aspect_ratio > 0.5625:
                # Find the new scale factor based off the 16-9 height of the width
                new_screen_height = self.current_screen_width * 9 / 16
                self.scale_factor = new_screen_height / self.base_height
        else:
            screen = pygame.display.set_mode((self.base_width, self.base_height))
            self.current_screen_width = self.base_width
            self.current_screen_height = self.base_height

        pygame.display.set_caption("Laser Fighter")
        return screen

    def _set_icon(self):
        """
            Sets the proper icon for the pygame window.

            :return: None
        """

        icon_surface = pygame.image.load("icon/Icon.png")
        pygame.display.set_icon(icon_surface)

    def _load_and_blit_background(self):
        """
            Sets the proper background for the pygame window.

            :return: None
        """

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
        """
            Retrieves the refresh rate of the current monitor

            :return: settings.DisplayFrequency
            :type: int
        """

        display_device = win32api.EnumDisplayDevices(None, 0)
        settings = win32api.EnumDisplaySettings(display_device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
        return settings.DisplayFrequency
