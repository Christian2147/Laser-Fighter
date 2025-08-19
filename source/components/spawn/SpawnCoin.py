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
    File: SpawnCoin.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for coins in Laser Fighter.
    This also includes the coin indicator which appears at the top of the screen and displays the amount of coins that
        the player has.
"""

from components.ItemCoin import CoinIndicator


class SpawnCoin:
    """
        Represents the Coin container in Laser Fighter.

        Attributes:
            coins_on_screen_list (list): Contains all of the coin sprites currently visible/active on the screen.
            current_coin_index (int): Stores the number of coins currently active and visible on the screen.
            coin_pickup_delay (int): Creates a delay to pick up coins (So that they are not picked up immediately when
                the enemy is killed)
    """

    def __init__(self, textures):
        """
            Creates the lists necessary to store the Coin sprite.
        """

        self.coins_on_screen_list = []
        self.current_coin_index = 0
        self.coin_pickup_delay = 0

        self._textures = textures

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.coins_on_screen_list
        del self.current_coin_index
        del self.coin_pickup_delay
        del self._textures


class SpawnCoinIndicator:
    """
        Represents the Coin Indicator container in Laser Fighter.

        Attributes:
            coin_indicator_sprite (list): Contains the coin indicator sprite once it is spawned
            coin_indicator_index (list): Determines if the coin indicator sprite has been spawned yet or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Coin Indicator sprite.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.coin_indicator_sprite = []
        self.coin_indicator_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.coin_indicator_sprite
        del self.coin_indicator_index

    def spawn_coin_indicator(self):
        """
            Spawn a coin indicator at the top of the screen.

            :return: None
        """

        coin_ind = CoinIndicator(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.coin_indicator_sprite.append(coin_ind)
        self.coin_indicator_index = self.coin_indicator_index + 1
