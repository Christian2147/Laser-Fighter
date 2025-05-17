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
            all_player (list): Contains the one machine player sprite that should be spawned throughout the entire game.
            current_player (list): Contains the machine player sprite if it is visible on the screen
            current_player_index (int): Stores whether the machine player sprite has been created or not
            player_hit_value (list): Contains the hit delay value for the machine player
            player_update_value (list): Contains the death animation value for the machine player

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Machine Player.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.all_player = []
        self.current_player = []
        self.current_player_index = 0
        self.player_hit_value = 0
        self.player_update_value = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_player
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

        if len(self.all_player) <= len(self.current_player):
            player = Player(god_mode, self.scale_factor_x, self.scale_factor_y)
            self.current_player.append(player)
            self.current_player_index = self.current_player_index + 1
            self.all_player.append(player)
        else:
            for p in self.all_player:
                if p.get_player().isvisible():
                    continue
                else:
                    p.reinstate(god_mode)
                    self.current_player.append(p)
                    self.current_player_index = self.current_player_index + 1
                    break


class SpawnHumanPlayer:
    """
        Represents the Human Player container in Laser Fighter.

        Attributes:
            all_human (list): Contains the one human player sprite that should be spawned throughout the entire game.
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

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Human Player.
            Also creates any miscellaneous variables necessary for Alien Mode.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.all_human = []
        self.current_human = []
        self.current_human_index = 0
        self.human_hit_value = 0
        self.human_update_value = 0
        self.right_update = 0
        self.left_update = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_human
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

        if len(self.all_human) <= len(self.current_human):
            human = Human(god_mode, self.scale_factor_x, self.scale_factor_y)
            self.current_human.append(human)
            self.current_human_index = self.current_human_index + 1
            self.all_human.append(human)
        else:
            for h in self.all_human:
                if h.get_player().isvisible():
                    continue
                else:
                    h.reinstate(god_mode)
                    self.current_human.append(h)
                    self.current_human_index = self.current_human_index + 1
                    break
