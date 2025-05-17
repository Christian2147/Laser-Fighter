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
    File: InterfaceSelect.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for the button selector.
    The selector is used to determine which button/slot is currently "in action" as in selected in the
        configurations eyes.
"""

import turtle
from setup.TextureSetup import SLOT_SELECTOR_TEXTURE
from setup.TextureSetup import TAB_SELECTOR_TEXTURE


class Selector:
    """
        Represents the selector object in Laser Fighter.

        Attributes:
            selector (turtle.Turtle()): The selector sprite
            type (string): The type of selector

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, scale_factor_x, scale_factor_y):
        self.selector = turtle.Turtle()
        # Ensure that the turtle does not draw lines on the screen while moving
        self.selector.penup()
        if type == "Tab":
            self.selector.shape(TAB_SELECTOR_TEXTURE)
            self.selector.goto(-603.5 * scale_factor_x, 150 * scale_factor_y)
        else:
            self.selector.shape(SLOT_SELECTOR_TEXTURE)
            self.selector.goto(-427 * scale_factor_x, 95.5 * scale_factor_y)

        self.type = type

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.selector.clear()
        del self.selector
        del self.type

    def reinstate_to_tab(self):
        """
            Reuses the existing sprite to spawn a tab selector on the screen.

            :return: None
        """

        self.selector.shape(TAB_SELECTOR_TEXTURE)
        self.selector.goto(-603.5 * self.scale_factor_x, 150 * self.scale_factor_y)
        self.selector.showturtle()

        # Set the type to "Tab"
        self.type = "Tab"

    def reinstate_to_slot(self):
        """
             Reuses the existing sprite to spawn a slot selector on the screen.

             :return: None
         """

        self.selector.shape(SLOT_SELECTOR_TEXTURE)
        self.selector.goto(-427 * self.scale_factor_x, 95.5 * self.scale_factor_y)
        self.selector.showturtle()

        # Set the type to "Slot"
        self.type = "Slot"

    def get_selector(self):
        """
            Returns the selector sprite so its class attributes can be accessed.

            :return: selector: the selector sprite
            :type: turtle.Turtle()
        """

        return self.selector

    def get_type(self):
        """
            Returns the type of the given selector.

            :return: type: the type of the given selector
            :type: string
        """

        return self.type

    def remove(self):
        """
            Removes the given selector from the screen.

            :return: None
        """

        self.selector.hideturtle()

    def new_select(self, x, y):
        """
            Moves the selector over a new button based on the new x and y coordinates.

            :param x: The x-coordinate of the new button
            :type x: float

            :param y: The y-coordinate of the new button
            :type y: float

            :return: None
        """

        self.selector.goto(x, y)
