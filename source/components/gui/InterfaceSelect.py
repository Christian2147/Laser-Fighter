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

import pygame


class Selector(pygame.sprite.Sprite):
    """
        Represents the selector object in Laser Fighter.

        Attributes:
            type (string): The type of selector

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, textures, scale_factor_x, scale_factor_y):
        """
            Creates a selector object and places it on the screen.

            :param type: Determines the type of selector to create (Tab or Slot)
            :type type: String

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        if type == "Tab":
            self.image = textures.TAB_SELECTOR
            self.rect = self.image.get_rect()
            self.rect.center = (int(36.5 * scale_factor_x), int(210 * scale_factor_y))
        else:
            self.image = textures.SLOT_SELECTOR
            self.rect = self.image.get_rect()
            self.rect.center = (int(213 * scale_factor_x), int(264.5 * scale_factor_y))
        self.selector_visible = 1

        self.type = type

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        del self

    def get_selector(self):
        """
            Returns the selector sprite so its class attributes can be accessed.

            :return: self: the selector sprite
            :type: pygame.sprite.Sprite
        """

        return self

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

        self.selector_visible = 0

    def new_select(self, x, y):
        """
            Moves the selector over a new button based on the new x and y coordinates.

            :param x: The x-coordinate of the new button
            :type x: float

            :param y: The y-coordinate of the new button
            :type y: float

            :return: None
        """

        self.rect.center = (int(x), int(y))
