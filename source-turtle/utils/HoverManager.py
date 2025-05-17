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
    File: Hover.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for the hover detection on buttons.
    Whenever the cursor is hovering over a specific button, a yellow highlight is created around the button frame.
"""


class Hover:
    """
        Represents the hover effect on buttons in Laser Fighter.

        Pointers:
            _screen (ScreenUpdate()): A pointer to the screen updater.
            _button (SpawnButton()): A pointer to the button container.
    """

    def __init__(self, screen, button):
        """
            Holds the function for the hover effect on buttons in Laser Fighter.

            :param screen: A pointer to the screen updater
            :type screen: ScreenUpdate()

            :param button: A pointer to the button container
            :type button: SpawnButton()
        """

        self._screen = screen
        self._button = button

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._screen
        del self._button

    def hover(self, event):
        """
            Change the color of the button text to yellow when the mouse is hovering over it.
            It also changes the colors to red/orange for the control buttons based on if there is a keybind conflict or
                not.

            :param event: Holds the current position of the cursor on the screen
            :type event: tkinter.Event()

            :return: None
        """

        # Extract x and y coordinate of the cursor
        a, b = event.x, event.y
        # Update button highlight as needed based on the cursors position
        if self._screen.mode == "Title_Mode":
            for bu in self._button.buttons_on_screen_list:
                bu.update_highlight(a, b)
        if self._screen.mode == "Machine_Mode" or self._screen.mode == "Alien_Mode" or self._screen.mode == "Stats" or self._screen.mode == "Shop":
            for bu in self._button.buttons_on_screen_list:
                self._button.button_update = bu.update_highlight(a, b)
        if self._screen.mode == "Settings":
            for bu in self._button.buttons_on_screen_list:
                if bu.type == "Regular_Settings_And_Controls":
                    if bu.id == 1:
                        self._button.button_update = bu.update_highlight(a, b)
                    else:
                        bu.update_highlight(a, b)
                else:
                    bu.update_highlight(a, b)
        if self._screen.mode == "Controls":
            for bu in self._button.buttons_on_screen_list:
                if bu.type == "Regular_Settings_And_Controls":
                    if bu.id == 1:
                        self._button.button_update = bu.update_highlight(a, b)
                    else:
                        bu.update_highlight(a, b)
                elif bu.type == "Controls_Toggle":
                    bu.update_highlight(a, b)
