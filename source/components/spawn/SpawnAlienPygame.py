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

from components.enemy.AlienSmallAlienPygame import SmallAlien


class SpawnSmallAlien:
    """
        Represents the Small Alien container in Laser Fighter.

        Attributes:
            all_small_aliens (list): Contains all of the small alien sprites created since the game has launched, even
                ones removed from the screen
            small_aliens (list): Contains all of the small alien sprites currently visible/active on the screen.
            small_aliens_kill_values (list): Contains all of the death animation values for each small alien
                on the screen.
            small_alien_index (int): Stores the number of small aliens currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Small Alien.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.small_aliens = []
        self.small_aliens_kill_values = []
        self.small_alien_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.small_aliens
        del self.small_aliens_kill_values
        del self.small_alien_index

    def spawn_small_alien(self, id):
        """
            Spawn a small alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        small_alien = SmallAlien(id, self.scale_factor_x, self.scale_factor_y)
        self.small_aliens.append(small_alien)
        self.small_alien_index = self.small_alien_index + 1
        self.small_aliens_kill_values.append(0)
