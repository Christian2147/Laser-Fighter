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
    Description: This file contains the logic related to coins, which is the main in game currency that will later on
    be used in the shop.
"""

import turtle


class Coin:
    """
        Represents a coin in Laser Fighter.

        Attributes:
            type (str): The type of coin (copper, silver, gold, platinum)
            coin (turtle): The coin sprite
    """

    def __init__(self, type, pos_x, pos_y, fullscreen):
        """
            Creates and places a coin on the screen

            :param type: Determines the type of coin the sprite is (copper, silver, gold, platinum)
            :type type: string

            :param pos_x: The x-coordinate of the coin sprite
            :type pos_x: float

            :param pos_y: The y-coordinate of the coin sprite
            :type pos_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.coin = turtle.Turtle()
        if type == "copper":
            if fullscreen == 1:
                self.coin.shape("Textures/Coins/Copper_Coin_Scaled.gif")
            else:
                self.coin.shape("Textures/Coins/Copper_Coin.gif")
        if type == "silver":
            if fullscreen == 1:
                self.coin.shape("Textures/Coins/Silver_Coin_Scaled.gif")
            else:
                self.coin.shape("Textures/Coins/Silver_Coin.gif")
        if type == "gold":
            if fullscreen == 1:
                self.coin.shape("Textures/Coins/Gold_Coin_Scaled.gif")
            else:
                self.coin.shape("Textures/Coins/Gold_Coin.gif")
        if type == "platinum":
            if fullscreen == 1:
                self.coin.shape("Textures/Coins/Platinum_Coin_Scaled.gif")
            else:
                self.coin.shape("Textures/Coins/Platinum_Coin.gif")
        # Ensure that the turtle does not draw lines
        self.coin.penup()
        self.coin.shapesize(2, 2)
        self.coin.goto(pos_x, pos_y)

        self.type = type

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.coin.hideturtle()
        self.coin.reset()

    def reinstate_to_copper(self, pos_x, pos_y, fullscreen):
        """
            Reuses the existing coin sprite to generate a copper coin on the screen

            :param: pos_x: the x-coordinate of the new coin
            :type: float

            :param: pos-y: the y-coordinate of the new coin
            :type: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.coin.shape("Textures/Coins/Copper_Coin_Scaled.gif")
        else:
            self.coin.shape("Textures/Coins/Copper_Coin.gif")
        self.coin.goto(pos_x, pos_y)
        self.coin.showturtle()

        self.type = "copper"

    def reinstate_to_silver(self, pos_x, pos_y, fullscreen):
        """
            Reuses the existing coin sprite to generate a silver coin on the screen

            :param: pos_x: the x-coordinate of the new coin
            :type: float

            :param: pos-y: the y-coordinate of the new coin
            :type: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.coin.shape("Textures/Coins/Silver_Coin_Scaled.gif")
        else:
            self.coin.shape("Textures/Coins/Silver_Coin.gif")
        self.coin.goto(pos_x, pos_y)
        self.coin.showturtle()

        self.type = "silver"

    def reinstate_to_gold(self, pos_x, pos_y, fullscreen):
        """
            Reuses the existing coin sprite to generate a gold coin on the screen

            :param: pos_x: the x-coordinate of the new coin
            :type: float

            :param: pos-y: the y-coordinate of the new coin
            :type: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.coin.shape("Textures/Coins/Gold_Coin_Scaled.gif")
        else:
            self.coin.shape("Textures/Coins/Gold_Coin.gif")
        self.coin.goto(pos_x, pos_y)
        self.coin.showturtle()

        self.type = "gold"

    def reinstate_to_platinum(self, pos_x, pos_y, fullscreen):
        """
            Reuses the existing coin sprite to generate a platinum coin on the screen

            :param: pos_x: the x-coordinate of the new coin
            :type: float

            :param: pos-y: the y-coordinate of the new coin
            :type: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.coin.shape("Textures/Coins/Platinum_Coin_Scaled.gif")
        else:
            self.coin.shape("Textures/Coins/Platinum_Coin.gif")
        self.coin.goto(pos_x, pos_y)
        self.coin.showturtle()

        self.type = "platinum"

    def get_coin(self):
        """
            Returns the coin sprite so its class attributes can be accessed

            :return: coin: the coin sprite
            :type: turtle.Turtle()
        """

        return self.coin

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

        self.coin.hideturtle()


class CoinIndicator:
    """
        Represents the coin counter in Laser Fighter.

        Attributes:
            coin_indicator(turtle.Turtle()): The coin_indicator sprite
    """

    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates and places the coin counter sprite on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.coin_indicator = turtle.Turtle()
        if fullscreen == 1:
            self.coin_indicator.shape("Textures/Coins/Coin_Indicator_Scaled.gif")
        else:
            self.coin_indicator.shape("Textures/Coins/Coin_Indicator.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.coin_indicator.penup()
        self.coin_indicator.goto(-617 * scale_factor_x, 300 * scale_factor_y)

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.coin_indicator.clear()
        del self.coin_indicator

    def reinstate(self):
        """
            Reuses the existing sprite to generate a coin counter on the screen

            :return: None
        """

        self.coin_indicator.showturtle()

    def get_coin_indicator(self):
        """
            Returns the coin_indicator sprite so its class attributes can be accessed

            :return: coin_indicator: the coin counter sprite
            :type: turtle.Turtle()
        """

        return self.coin_indicator

    def remove(self):
        """
            Removes the coin counter sprite form the screen

            :return: None
        """

        self.coin_indicator.hideturtle()