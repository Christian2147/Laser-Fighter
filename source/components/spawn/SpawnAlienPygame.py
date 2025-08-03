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
from components.enemy.AlienMediumAlienPygame import MediumAlien
from components.enemy.AlienLargeAlienPygame import LargeAlien
from components.enemy.AlienUFOPygame import UFO


class SpawnSmallAlien:
    """
        Represents the Small Alien container in Laser Fighter.

        Attributes:
            small_aliens (list): Contains all of the small alien sprites currently visible/active on the screen.
            small_aliens_kill_values (list): Contains all of the death animation values for each small alien
                on the screen.
            small_alien_index (int): Stores the number of small aliens currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
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

        self._textures = textures
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

        small_alien = SmallAlien(id, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.small_aliens.append(small_alien)
        self.small_alien_index = self.small_alien_index + 1
        self.small_aliens_kill_values.append(0)


class SpawnMediumAlien:
    """
        Represents the Medium Alien container in Laser Fighter.

        Attributes:
            medium_aliens (list): Contains all of the medium alien sprites currently visible/active on the screen.
            medium_aliens_kill_values (list): Contains all of the death animation values for each medium alien
                on the screen.
            medium_aliens_hit_values (list): Contains all of the hit delay values for each medium alien on the screen.
            medium_alien_index (int): Stores the number of medium aliens currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Medium Alien.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.medium_aliens = []
        self.medium_aliens_kill_values = []
        self.medium_aliens_hit_values = []
        self.medium_alien_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.medium_aliens
        del self.medium_aliens_kill_values
        del self.medium_aliens_hit_values
        del self.medium_alien_index

    def spawn_medium_alien(self, id):
        """
            Spawn a medium alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        medium_alien = MediumAlien(id, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.medium_aliens.append(medium_alien)
        self.medium_alien_index = self.medium_alien_index + 1
        self.medium_aliens_kill_values.append(0)
        self.medium_aliens_hit_values.append(0)


class SpawnLargeAlien:
    """
        Represents the Large Alien container in Laser Fighter.

        Attributes:
            large_aliens (list): Contains all of the large alien sprites currently visible/active on the screen.
            large_aliens_kill_values (list): Contains all of the death animation values for each large alien
                on the screen.
            large_aliens_hit_values (list): Contains all of the hit delay values for each large alien on the screen.
            large_alien_index (int): Stores the number of large aliens currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Large Alien.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.large_aliens = []
        self.large_aliens_kill_values = []
        self.large_aliens_hit_values = []
        self.large_alien_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.large_aliens
        del self.large_aliens_kill_values
        del self.large_aliens_hit_values
        del self.large_alien_index

    def spawn_large_alien(self, id):
        """
            Spawn a large alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        large_alien = LargeAlien(id, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.large_aliens.append(large_alien)
        self.large_alien_index = self.large_alien_index + 1
        self.large_aliens_kill_values.append(0)
        self.large_aliens_hit_values.append(0)


class SpawnUFO:
    """
        Represents the UFO container in Laser Fighter.

        Attributes:
            ufos (list): Contains the ufo sprite if it is visible on the screen
            ufo_kill_value (list): Contains the death animation value for the ufo
            ufo_hit_value (list): Contains the hit delay value for the ufo
            ufo_index (int): Stores whether the ufo sprite has been created or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the UFO.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.ufos = []
        self.ufo_kill_value = 0
        self.ufo_hit_value = 0
        self.ufo_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.ufos
        del self.ufo_kill_value
        del self.ufo_hit_value
        del self.ufo_index

    def spawn_alien_boss(self):
        """
            Spawn an alien UFO on the screen.

            :return: None
        """

        spawn_ufo = UFO(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.ufos.append(spawn_ufo)
        self.ufo_index = self.ufo_index + 1
