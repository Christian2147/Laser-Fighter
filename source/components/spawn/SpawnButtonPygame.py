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
    File: SpawnAlien.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for Aliens in Laser Fighter.
    These classes are used to access all 4 types of Aliens.
"""

from components.gui.InterfaceButtonPygame import Button


class SpawnButton:
    """
        Represents the Button container in Laser Fighter.

        Attributes:
            buttons_on_screen_list (list): Contains all of the button sprites currently visible/active on the screen.
            current_button_index (int): Stores the number of buttons currently active and visible on the screen.

            button_update (int): Used for the main menu button when being hovered over (Main Menu Button Can be in
                different locations depending on the screen)
            clickable (int): Used to ensure that certain buttons can be clicked right away when the screen is changed
                (Without the mouse needing to move at all)
            buy_button_pressed (int): Determines if the buy button in the shop side panel has been pressed or not

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Buttons in Laser Fighter.
            Also creates any other necessary variables for the button object.

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.buttons_on_screen_list = []
        self.current_button_index = 0

        self.button_update = 0
        self.clickable = 0
        self.buy_button_pressed = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.buttons_on_screen_list
        del self.current_button_index
        del self.button_update
        del self.clickable
        del self.buy_button_pressed

    def spawn_button(self, type, id, page=None):
        """
            Spawns a button on the screen using the button class.

            :param type: The type of button to create
            :type type: string

            :param id: The id of the button to create
            :type id: int

            :param page: The current page being displayed (Only applies to the Shop Slot)
            :type page: string

            :return: None
        """

        # Create a new button object
        if type != "Shop_Slot" and type != "Power_Up_Slot" and type != "Gadget_Slot":
            button = Button(type, id, self.scale_factor, self.scale_factor_x, self.scale_factor_y)
        else:
            # The page the user is on is needed for the Shop Slot
            button = Button(type, id, self.scale_factor, self.scale_factor_x, self.scale_factor_y, page=page)
        self.buttons_on_screen_list.append(button)
        self.current_button_index = self.current_button_index + 1
