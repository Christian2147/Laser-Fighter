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

import pygame


class PriceLabel(pygame.sprite.Sprite):
    """
        Represents the price label in Laser Fighter.

        Attributes:
            price_label (turtle.Turtle()): The price label icon sprite
            id (int): The id of the current price label
    """

    def __init__(self, id, x, y, textures):
        """
            Creates a price label icon and places it on the screen.

            :param id: The id of the current price label
            :type id: int

            :param x: The x-coordinate of the new price label
            :type x: float

            :param y: The y-coordinate of the new price label
            :type y: float
        """

        super().__init__()
        self.image = textures.COIN_INDICATOR
        self.rect = self.image.get_rect()
        self.rect.center = (int(x), int(y))
        self.price_label_visible = 1

        self.id = id

        self._textures = textures

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        del self

    def get_price_label(self):
        """
            Returns the price label icon so its class attributes can be accessed.

            :return: price_label: the price label icon
            :type: turtle.Turtle()
        """

        return self

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

        self.price_label_visible = 0
