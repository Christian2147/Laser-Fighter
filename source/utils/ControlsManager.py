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

from tkinter import messagebox
import pygame


class Controls:
    """
        Represents the Toggle functions for the keybinds in Laser Fighter.

        Pointers:
            _window (turtle.Screen()): Pointer to the application window.
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

    def __init__(self, window, screen, settings, controls_toggle, refresh, scale_factor_x, scale_factor_y):
        """
            Initializes all of the pointers necessary for the Controls Manager.

            :param window: Pointer to the application window.
            :type window: turtle.Screen()

            :param screen: Pointer to the current displayed screen and the screen changing functions.
            :type screen: ScreenUpdate()

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

        self._window = window
        self._screen = screen
        self._settings = settings
        self._controls_toggle = controls_toggle
        self._refresh = refresh

        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self._go_right_key_alert = 0
        self._go_left_key_alert = 0
        self._shoot_key_alert = 0
        self._jump_key_alert = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._window
        del self._screen
        del self._settings
        del self._controls_toggle
        del self._refresh
        del self._scale_factor_x
        del self._scale_factor_y
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

    def change_go_right_key(self, x, y):
        """
            Used to change the keybind for going right.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 165 * self._scale_factor_y) and (y < 226 * self._scale_factor_y):
            self.execute_control_setting(0)

    def change_go_left_key(self, x, y):
        """
            Used to change the keybind for going left.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 85 * self._scale_factor_y) and (y < 146 * self._scale_factor_y):
            self.execute_control_setting(1)

    def change_shoot_key(self, x, y):
        """
            Used to change the keybind for shooting the player laser.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > 5 * self._scale_factor_y) and (y < 66 * self._scale_factor_y):
            self.execute_control_setting(2)

    def change_jump_key(self, x, y):
        """
            Used to change the keybind for jumping.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -612 * self._scale_factor_x) and (x < -40 * self._scale_factor_x) and (y > -75 * self._scale_factor_y) and (y < -14 * self._scale_factor_y):
            self.execute_control_setting(3)

    def execute_control_setting(self, type):
        """
            Actaully executes the keybind change given by the "type" parameter.

            :param type: The type of keybind change to be executed.
            :type type: int

            :return: None
        """

        key_1 = 0
        # "type" parameter as a string
        type_string = ""
        # Go right key
        if type == 0:
            key_1 = self._controls_toggle.go_right_key
            type_string = "Go Right"
        # Go left key
        elif type == 1:
            key_1 = self._controls_toggle.go_left_key
            type_string = "Go Left"
        # Shoot key
        elif type == 2:
            key_1 = self._controls_toggle.shoot_key
            type_string = "Shoot"
        # Jump key
        elif type == 3:
            key_1 = self._controls_toggle.jump_key
            type_string = "Jump"
        # Play the button click sound
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Backup the original keybind
        key_backup = key_1
        # Set "key_2" to whatever the user inputted into the textbox
        key_2 = self._window.textinput("{}".format(type_string), "Insert new key here:")
        # If the user inputted a space, display "space"
        if key_2 == " ":
            key_2 = "space"
        # Listen for new keybinds
        self._window.listen()
        # If the new keybind exists and is different from the one before, the keybind setting need to be updated
        if key_2 != None and key_2 != key_backup:
            # If the new keybind input is invalid (enter key or multiple charecters)
            if (len(key_2) > 1 and key_2 != "space") or key_2 == "":
                # Let the user know through an error
                messagebox.showerror("Invalid Input!", "That is an invalid input!")
            # if it is valid
            else:
                # Update the keybind in the backup ini file.
                self._controls_toggle.key_check[type] = key_2
                self._controls_toggle.save_check()
                key_1 = key_2
                # Check for keybind conflicts for each keybind individually
                if type == 0:
                    self._controls_toggle.go_right_key = key_1
                    if self._controls_toggle.go_right_key != self._controls_toggle.go_left_key and \
                            self._controls_toggle.go_right_key != self._controls_toggle.shoot_key and \
                            self._controls_toggle.go_right_key != self._controls_toggle.jump_key:
                        self._go_right_key_alert = 0
                    else:
                        self._go_right_key_alert = 1
                    key_alert = self._go_right_key_alert
                elif type == 1:
                    self._controls_toggle.go_left_key = key_1
                    if self._controls_toggle.go_left_key != self._controls_toggle.go_right_key and \
                            self._controls_toggle.go_left_key != self._controls_toggle.shoot_key and \
                            self._controls_toggle.go_left_key != self._controls_toggle.jump_key:
                        self._go_left_key_alert = 0
                    else:
                        self._go_left_key_alert = 1
                    key_alert = self._go_left_key_alert
                elif type == 2:
                    self._controls_toggle.shoot_key = key_1
                    if self._controls_toggle.shoot_key != self._controls_toggle.go_right_key and \
                            self._controls_toggle.shoot_key != self._controls_toggle.go_left_key and \
                            self._controls_toggle.shoot_key != self._controls_toggle.jump_key:
                        self._shoot_key_alert = 0
                    else:
                        self._shoot_key_alert = 1
                    key_alert = self._shoot_key_alert
                else:
                    self._controls_toggle.jump_key = key_1
                    if self._controls_toggle.jump_key != self._controls_toggle.go_right_key and \
                            self._controls_toggle.jump_key != self._controls_toggle.go_left_key and \
                            self._controls_toggle.jump_key != self._controls_toggle.shoot_key:
                        self._jump_key_alert = 0
                    else:
                        self._jump_key_alert = 1
                    key_alert = self._jump_key_alert
                # If there is a conflict
                if key_alert == 1:
                    # Alert the user about the conflict
                    message_output = messagebox.askyesno("Conflict!", "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", icon='warning')
                    # If the user wants to go back
                    if not message_output:
                        # Reinstate the old keybinds and update the backup keybind file
                        key_1 = key_backup
                        key_2 = key_backup
                        self._controls_toggle.key_check[type] = key_2
                        self._controls_toggle.save_check()
                        if type == 0:
                            self._controls_toggle.go_right_key = key_1
                        elif type == 1:
                            self._controls_toggle.go_left_key = key_1
                        elif type == 2:
                            self._controls_toggle.shoot_key = key_1
                        else:
                            self._controls_toggle.jump_key = key_1
                    # If the user wants to keep the controls
                    else:
                        # Update the main config file to confirm the changes
                        self._controls_toggle.save()
                        # Alert that a restart is needed for changes to take effect
                        self._screen.updated_controls = 1
                else:
                    # If there are no conflicts, update the main config file like normal.
                    self._controls_toggle.save()
                    # Alert that a restart is needed for changes to take effect
                    self._screen.updated_controls = 1
        # Refresh all the buttons on the screen
        self._refresh.refresh_button = 1
