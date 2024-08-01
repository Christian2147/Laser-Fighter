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

import ctypes
import pygame


class SettingsToggle:
    def __init__(self, window, screen, button, settings, refresh, scale_factor_x, scale_factor_y):
        self._window = window
        self._screen = screen
        self._button = button
        self._settings = settings
        self._refresh = refresh
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self._fullscreen_toggled = 0

    def __del__(self):
        del self._window
        del self._screen
        del self._button
        del self._settings
        del self._refresh
        del self._scale_factor_x
        del self._scale_factor_y
        del self._fullscreen_toggled

    @property
    def fullscreen_toggled(self) -> int:
        return self._fullscreen_toggled

    @fullscreen_toggled.setter
    def fullscreen_toggled(self, value: int) -> None:
        if isinstance(value, int):
            self._fullscreen_toggled = value
        else:
            raise ValueError("fullscreen_toggled must be a integer")

    def toggle_button_sound(self, x, y):
        """
            Used to toggle the button sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 165 * self._scale_factor_y) and (y < 226 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                self._settings.button_sound = 0
            else:
                self._settings.button_sound = 1
            self.execute_setting_function()

    def toggle_player_shooting_sound(self, x, y):
        """
            Used to toggle the button sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 85 * self._scale_factor_y) and (y < 146 * self._scale_factor_y):
            if self._settings.player_shooting_sound == 1:
                self._settings.player_shooting_sound = 0
            else:
                self._settings.player_shooting_sound = 1
            self.execute_setting_function()

    def toggle_enemy_shooting_sound(self, x, y):
        """
            Used to toggle the button sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 5 * self._scale_factor_y) and (y < 66 * self._scale_factor_y):
            if self._settings.enemy_shooting_sound == 1:
                self._settings.enemy_shooting_sound = 0
            else:
                self._settings.enemy_shooting_sound = 1
            self.execute_setting_function()

    def toggle_player_death_sound(self, x, y):
        """
            Used to toggle the player death sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > -75 * self._scale_factor_y) and (y < -14 * self._scale_factor_y):
            if self._settings.player_death_sound == 1:
                self._settings.player_death_sound = 0
            else:
                self._settings.player_death_sound = 1
            self.execute_setting_function()

    def toggle_enemy_death_sound(self, x, y):
        """
            Used to toggle the enemy death sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > -155 * self._scale_factor_y) and (y < -94 * self._scale_factor_y):
            if self._settings.enemy_death_sound == 1:
                self._settings.enemy_death_sound = 0
            else:
                self._settings.enemy_death_sound = 1
            self.execute_setting_function()

    def toggle_player_hit_sound(self, x, y):
        """
            Used to toggle the player hit sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > -235 * self._scale_factor_y) and (y < -174 * self._scale_factor_y):
            if self._settings.player_hit_sound == 1:
                self._settings.player_hit_sound = 0
            else:
                self._settings.player_hit_sound = 1
            self.execute_setting_function()

    def toggle_enemy_hit_sound(self, x, y):
        """
            Used to toggle the enemy hit sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > -315 * self._scale_factor_y) and (y < -254 * self._scale_factor_y):
            if self._settings.enemy_hit_sound == 1:
                self._settings.enemy_hit_sound = 0
            else:
                self._settings.enemy_hit_sound = 1
            self.execute_setting_function()

    def toggle_power_up_pickup_sound(self, x, y):
        """
            Used to toggle the power up pickup sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > 165 * self._scale_factor_y) and (y < 226 * self._scale_factor_y):
            if self._settings.power_up_pickup_sound == 1:
                self._settings.power_up_pickup_sound = 0
            else:
                self._settings.power_up_pickup_sound = 1
            self.execute_setting_function()

    def toggle_power_up_spawn_sound(self, x, y):
        """
            Used to toggle the power up spawn sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > 85 * self._scale_factor_y) and (y < 146 * self._scale_factor_y):
            if self._settings.power_up_spawn_sound == 1:
                self._settings.power_up_spawn_sound = 0
            else:
                self._settings.power_up_spawn_sound = 1
            self.execute_setting_function()

    def toggle_coin_pick_up_sound(self, x, y):
        """
            Used to toggle the coin pick up sound on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > 5 * self._scale_factor_y) and (
                y < 66 * self._scale_factor_y):
            if self._settings.coin_pickup_sound == 1:
                self._settings.coin_pickup_sound = 0
            else:
                self._settings.coin_pickup_sound = 1
            self.execute_setting_function()

    def toggle_fullscreen(self, x, y):
        """
            Used to toggle fullscreen on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -75 * self._scale_factor_y) and (y < -14 * self._scale_factor_y):
            # Button sound is played
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # If fullscreen was originally off
            if self._settings.fullscreen == 0 and self._fullscreen_toggled == 0:
                # Warn the player about the effects of performance
                message_output = ctypes.windll.user32.MessageBoxW(0, "Enabling fullscreen may cause a performance drop and expose your game to bugs. Are you sure you want to enable fullscreen?", "Warning!", 4 + 48)
                # If the player says yes
                if message_output != 7:
                    # Toggle fullscreen
                    self._settings.toggle_fullscreen()
                    # Alert the game of a needed restart
                    if self._fullscreen_toggled == 0:
                        self._fullscreen_toggled = 1
                        self._screen.updated_controls = 1
                    else:
                        self._fullscreen_toggled = 0
                        self._screen.updated_controls = 0
            # If fullscreen was originally on
            else:
                # Turn it off like normal, but a restart is still required
                self._settings.toggle_fullscreen()
                if self._fullscreen_toggled == 0:
                    self._fullscreen_toggled = 1
                    self._screen.updated_controls = 1
                else:
                    self._fullscreen_toggled = 0
                    self._screen.updated_controls = 0
            self._refresh.refresh_button = 1
            self._refresh.refresh_indicator = 1

    def toggle_vsync(self, x, y):
        """
            Used to toggle VSync on and off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -155 * self._scale_factor_y) and (
                y < -94 * self._scale_factor_y):
            # If VSync was originally off
            if self._settings.vsync == 0:
                # Warn the user about effects on performance
                message_output = ctypes.windll.user32.MessageBoxW(0, "Turning on VSync may lower performance. Are you sure you want to enable VSync?", "Warning!", 4 + 48)
                # If the user selects yes
                if message_output != 7:
                    # Toggle VSync
                    if self._settings.vsync == 1:
                        self._settings.vsync = 0
                    else:
                        self._settings.vsync = 1
                        self.execute_setting_function()
            # If VSync was originally on
            else:
                # Toggle like normal
                if self._settings.vsync == 1:
                    self._settings.vsync = 0
                else:
                    self._settings.vsync = 1
                self.execute_setting_function()

    def execute_setting_function(self):
        """
            Used to actually execute the toggle based on the parameter "type".

            :return: None
        """

        # Button sound is played
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # The configuration file is updated
        self._settings.save()
        self._refresh.refresh_button = 1
        self._refresh.refresh_indicator = 1
