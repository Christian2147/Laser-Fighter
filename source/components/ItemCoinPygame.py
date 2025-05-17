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
    File: ItemCoin.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to coins, which is the main in game currency that will later on
    be used in the shop.
"""

import pygame
from setup.TextureSetup import COPPER_COIN_TEXTURE
from setup.TextureSetup import SILVER_COIN_TEXTURE
from setup.TextureSetup import GOLD_COIN_TEXTURE
from setup.TextureSetup import PLATINUM_COIN_TEXTURE
from setup.TextureSetup import COIN_INDICATOR_TEXTURE


class Coin(pygame.sprite.Sprite):
    """
        Represents a coin in Laser Fighter.

        Class Variables:
            COIN_DISTANCE (float): The size of the coins hitbox (48 * 2 = 96 * 96 hitbox without fullscreen mode)

        Attributes:
            type (string): The type of coin (copper, silver, gold, platinum)

            range (tuple): The range of the coins hitbox (Distance between one side to another on a specified axis)
            collision_coordinate (float): The point the laser has to pass in order to pick up the coin (Edge of the
                hitbox on the opposite axis of the "range" variable)
            relative_laser_position (int): Determines if the laser is in front of or behind the coin when it is fired
    """

    def __init__(self, type, pos_x, pos_y, scale_factor_x):
        """
            Creates and places a coin on the screen

            :param type: Determines the type of coin the sprite is (copper, silver, gold, platinum)
            :type type: string

            :param pos_x: The x-coordinate of the coin sprite
            :type pos_x: float

            :param pos_y: The y-coordinate of the coin sprite
            :type pos_y: float
        """

        super().__init__()
        if type == "copper":
            self.image = pygame.image.load(COPPER_COIN_TEXTURE).convert_alpha()
        if type == "silver":
            self.image = pygame.image.load(SILVER_COIN_TEXTURE).convert_alpha()
        if type == "gold":
            self.image = pygame.image.load(GOLD_COIN_TEXTURE).convert_alpha()
        if type == "platinum":
            self.image = pygame.image.load(PLATINUM_COIN_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.coin_visible = 1

        # Collision Variables
        self.range = (0, 0)
        self.collision_coordinate = 0
        self.relative_laser_position = 0
        self.just_fired = 0

        self.COIN_DISTANCE = 48 * scale_factor_x

        self.type = type

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.coin_visible = 0
        self.kill()

    def get_coin(self):
        """
            Returns the coin sprite so its class attributes can be accessed

            :return: coin: the coin sprite
            :type: turtle.Turtle()
        """

        return self

    def get_type(self):
        """
            Returns the type variable that determines the type of coin

            :return: type: the coin type as a string
            :type: string
        """

        return self.type

    def remove(self):
        """
            Removes the coin sprite form the screen

            :return: None
        """

        self.coin_visible = 0


class CoinIndicator(pygame.sprite.Sprite):
    """
        Represents the coin counter in Laser Fighter.
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates and places the coin counter sprite on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = pygame.image.load(COIN_INDICATOR_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (23 * scale_factor_x, 60 * scale_factor_y)
        self.coin_indicator_visible = 1

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_coin_indicator(self):
        """
            Returns the coin_indicator sprite so its class attributes can be accessed

            :return: coin_indicator: the coin counter sprite
            :type: turtle.Turtle()
        """

        return self

    def remove(self):
        """
            Removes the coin counter sprite form the screen

            :return: None
        """

        self.coin_indicator_visible = 0
