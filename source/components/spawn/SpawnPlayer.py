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
    File: SpawnPlayer.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for the player in Laser Fighter.
    This includes the player in both Machine Mode and Alien Mode.
"""

from components.player.MachinePlayer import Player
from components.player.HumanPlayer import Human


class SpawnMachinePlayer:
    """
        Represents the Machine Player container in Laser Fighter.

        Attributes:
            current_player (list): Contains the machine player sprite if it is visible on the screen
            current_player_index (int): Stores whether the machine player sprite has been created or not
            player_hit_value (list): Contains the hit delay value for the machine player
            player_update_value (list): Contains the death animation value for the machine player

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Machine Player.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.current_player = []
        self.current_player_index = 0
        self.player_hit_value = 0
        self.player_update_value = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.current_player
        del self.current_player_index
        del self.player_hit_value
        del self.player_update_value

    def spawn_machine_player(self, god_mode):
        """
            Spawn the Machine Mode player on the screen.

            :param god_mode: determines whether god_mode is toggled on/off
            :type god_mode: int

            :return: None
        """

        player = Player(god_mode, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.current_player.append(player)
        self.current_player_index = self.current_player_index + 1


class SpawnHumanPlayer:
    """
        Represents the Human Player container in Laser Fighter.

        Attributes:
            current_human (list): Contains the human player sprite if it is visible on the screen
            current_human_index (int): Stores whether the human player sprite has been created or not
            human_hit_value (list): Contains the hit delay value for the human player
            human_update_value (list): Contains the death animation value for the human player

            right_update (float): Used for updating the facing right walking animation for both the human player and
                the aliens in Alien Mode
            left_update (float): Used for updating the facing left walking animation for both the human player and
                the aliens in Alien Mode

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Human Player.
            Also creates any miscellaneous variables necessary for Alien Mode.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.current_human = []
        self.current_human_index = 0
        self.human_hit_value = 0
        self.human_update_value = 0
        self.right_update = 0
        self.left_update = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.current_human
        del self.current_human_index
        del self.human_hit_value
        del self.human_update_value
        del self.right_update
        del self.left_update

    def spawn_human_player(self, god_mode):
        """
            Spawn the human player on the screen.

            :param god_mode: determines whether god_mode is toggled on/off
            :type god_mode: int

            :return: None
        """

        human = Human(god_mode, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.current_human.append(human)
        self.current_human_index = self.current_human_index + 1
