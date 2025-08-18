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

"""
    File: ControlsManager.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for changing and toggling the keybinds while in game.
"""

import pygame


class Controls:
    """
        Represents the Toggle functions for the keybinds in Laser Fighter.

        Pointers:
            _screen (ScreenUpdate()): Pointer to the current displayed screen and the screen changing functions.
            _settings (Settings()): Pointer to the current game settings.
            _controls_toggle (ControlsToggle()): Pointer to the current keybinds.
            _refresh (Refresh()): Pointer to the game refresh variables.

        Attributes:
            _scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode

            _go_right_key_alert (int): Determines of the go right keybind conflicts with any other keybind
            _go_left_key_alert (int): Determines if the go left keybind conflicts with any other keybind.
            _shoot_key_alert (int): Determines if the shoot keybind conflicts with any other keybind.
            _jump_key_alert (int): Determines if the jump keybind conflicts with any other keybind.
    """

    def __init__(self,
                 pop_up,
                 settings,
                 controls_toggle,
                 refresh,
                 scale_factor,
                 scale_factor_x,
                 scale_factor_y
    ):
        """
            Initializes all of the pointers necessary for the Controls Manager.

            :param settings: Pointer to the current game settings.
            :type settings: Settings()

            :param controls_toggle: Pointer to the current keybinds.
            :type controls_toggle: ControlsToggle()

            :param refresh: Pointer to the game refresh variables.
            :type refresh: Refresh()

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode.
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode.
            :type scale_factor_y: float
        """

        self._pop_up = pop_up
        self._settings = settings
        self._controls_toggle = controls_toggle
        self._refresh = refresh

        self._scale_factor = scale_factor
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self.new_key = None
        self.update_type = -1
        self.listening = False
        self.active_control_button = -1

        self._go_right_key_alert = 0
        self._go_left_key_alert = 0
        self._shoot_key_alert = 0
        self._jump_key_alert = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._settings
        del self._controls_toggle
        del self._refresh
        del self._scale_factor_x
        del self._scale_factor_y
        del self.active_control_button
        del self._go_right_key_alert
        del self._go_left_key_alert
        del self._shoot_key_alert
        del self._jump_key_alert

    @property
    def go_right_key_alert(self):
        """go_right_key_alert getter"""
        return self._go_right_key_alert

    @go_right_key_alert.setter
    def go_right_key_alert(self, value):
        """go_right_key_alert setter"""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if value != 0 and value != 1:
            raise ValueError("Value must be 0 or 1.")
        self._go_right_key_alert = value

    @property
    def go_left_key_alert(self):
        """go_left_key_alert getter"""
        return self._go_left_key_alert

    @go_left_key_alert.setter
    def go_left_key_alert(self, value):
        """go_left_key_alert setter"""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if value != 0 and value != 1:
            raise ValueError("Value must be 0 or 1.")
        self._go_left_key_alert = value

    @property
    def shoot_key_alert(self):
        """shoot_key_alert getter"""
        return self._shoot_key_alert

    @shoot_key_alert.setter
    def shoot_key_alert(self, value):
        """shoot_key_alert setter"""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if value != 0 and value != 1:
            raise ValueError("Value must be 0 or 1.")
        self._shoot_key_alert = value

    @property
    def jump_key_alert(self):
        """jump_key_alert getter"""
        return self._jump_key_alert

    @jump_key_alert.setter
    def jump_key_alert(self, value):
        """jump_key_alert setter"""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if value != 0 and value != 1:
            raise ValueError("Value must be 0 or 1.")
        self._jump_key_alert = value

    def change_go_right_key(self):
        """
            Used to change the keybind for going right.

            :return: None
        """

        self.execute_control_setting(0)

    def change_go_left_key(self):
        """
            Used to change the keybind for going left.

            :return: None
        """

        self.execute_control_setting(1)

    def change_shoot_key(self):
        """
            Used to change the keybind for shooting the player laser.

            :return: None
        """

        self.execute_control_setting(2)

    def change_jump_key(self):
        """
            Used to change the keybind for jumping.

            :return: None
        """

        self.execute_control_setting(3)

    def execute_control_setting(self, type):
        """
            Actaully executes the keybind change given by the "type" parameter.

            :param type: The type of keybind change to be executed.
            :type type: int

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        self.active_control_button = type
        self._refresh.refresh_button = 1

        self.listening = True
        self.update_type = type

        return

    def update_controls(self, type):
        if isinstance(self.new_key, int):
            key_str = pygame.key.name(self.new_key)
        else:
            key_str = str(self.new_key)

        key_str = key_str.strip().lower().replace(" ", "_")

        if type == 0:
            current_key = self._controls_toggle.go_right_key
        elif type == 1:
            current_key = self._controls_toggle.go_left_key
        elif type == 2:
            current_key = self._controls_toggle.shoot_key
        elif type == 3:
            current_key = self._controls_toggle.jump_key
        else:
            return

        key_backup = current_key

        if type == 0:
            self._controls_toggle.go_right_key = key_str
        elif type == 1:
            self._controls_toggle.go_left_key = key_str
        elif type == 2:
            self._controls_toggle.shoot_key = key_str
        else:
            self._controls_toggle.jump_key = key_str

        conflict = False
        keys = [
            self._controls_toggle.go_right_key,
            self._controls_toggle.go_left_key,
            self._controls_toggle.shoot_key,
            self._controls_toggle.jump_key
        ]
        if len(set(keys)) != 4:
            conflict = True

        if conflict:
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()

            confirm_text = [
                "Your current",
                "configuration may",
                "conflict with other",
                "controls! Do you",
                "want to keep it?",
            ]

            self._pop_up.spawn_pop_up(
                icon="warning",
                text=confirm_text,
                type=1,
                on_yes=self.keep_conflicting_controls,
                on_no=lambda: self.revert_conflicting_controls(type, key_backup)
            )

        self._controls_toggle.save()

        self.new_key = None
        self.update_type = -1
        self.active_control_button = -1
        self._refresh.refresh_button = 1

    def keep_conflicting_controls(self):
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        for pu in self._pop_up.pop_up_on_screen_list:
            pu.remove()
        self._pop_up.pop_up_on_screen_list.clear()

        self._controls_toggle.save()

        self.new_key = None
        self.update_type = -1
        self.active_control_button = -1
        self._refresh.refresh_button = 1

    def revert_conflicting_controls(self, type, key_backup):
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        for pu in self._pop_up.pop_up_on_screen_list:
            pu.remove()
        self._pop_up.pop_up_on_screen_list.clear()

        if type == 0:
            self._controls_toggle.go_right_key = key_backup
        elif type == 1:
            self._controls_toggle.go_left_key = key_backup
        elif type == 2:
            self._controls_toggle.shoot_key = key_backup
        else:
            self._controls_toggle.jump_key = key_backup

        self._controls_toggle.save()

        self.new_key = None
        self.update_type = -1
        self.active_control_button = -1
        self._refresh.refresh_button = 1
