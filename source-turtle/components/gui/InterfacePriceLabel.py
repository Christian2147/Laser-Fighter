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
    File: InterfacePriceLabel.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for the price label.
    The price label is the little coin icon next to the displayed price of the item in a shop slot/power up slot.
"""

import turtle
from setup.TextureSetup import COIN_INDICATOR_TEXTURE


class PriceLabel:
    """
        Represents the price label in Laser Fighter.

        Attributes:
            price_label (turtle.Turtle()): The price label icon sprite
            id (int): The id of the current price label
    """

    def __init__(self, id, x, y):
        """
            Creates a price label icon and places it on the screen.

            :param id: The id of the current price label
            :type id: int

            :param x: The x-coordinate of the new price label
            :type x: float

            :param y: The y-coordinate of the new price label
            :type y: float
        """

        self.price_label = turtle.Turtle()
        # Ensure that the turtle does not draw lines on the screen while moving
        self.price_label.penup()
        self.price_label.shape(COIN_INDICATOR_TEXTURE)
        self.price_label.goto(x, y)

        self.id = id

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.price_label.clear()
        del self.price_label

    def reinstate(self, id, x, y):
        """
            Reuses the existing sprite to spawn a price label on the screen at the specified location with the
                specified id.

            :param id: The id of the current price label
            :type id: int

            :param x: The x-coordinate of the new price label
            :type x: float

            :param y: The y-coordinate of the new price label
            :type y: float

            :return: None
        """

        self.price_label.goto(x, y)
        self.price_label.showturtle()

        self.id = id

    def get_price_label(self):
        """
            Returns the price label icon so its class attributes can be accessed.

            :return: price_label: the price label icon
            :type: turtle.Turtle()
        """

        return self.price_label

    def get_id(self):
        """
            Returns the current id of the price label.

            :return: id: The current id of the price label
            :type: int
        """

        return self.id

    def remove(self):
        """
            Removes the price label from the screen.

            :return: None
        """

        self.price_label.hideturtle()
