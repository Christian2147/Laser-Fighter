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
    File: SpawnMachine.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for Machines in Laser Fighter.
    These classes are used to access all 4 types of Machines.
"""

from components.enemy.MachineBlueMachinePygame import BlueMachine
from components.enemy.MachineYellowMachinePygame import YellowMachine


class SpawnBlueMachine:
    """
        Represents the Blue Machine container in Laser Fighter.

        Attributes:
            blue_machines (list): Contains all of the blue machine sprites currently visible/active on the screen.
            blue_machines_update_values (list): Contains all of the death animation values for each blue machine
                on the screen.
            blue_machine_index (int): Stores the number of blue machines currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Blue Machine.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.blue_machines = []
        self.blue_machines_update_values = []
        self.blue_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.blue_machines
        del self.blue_machines_update_values
        del self.blue_machine_index

    def spawn_blue_machine(self, id):
        """
            Spawn a blue machine with the given id on the screen.

            :param id: The id that the enemy should have (Determines initial location of the enemy)
            :type id: int

            :return: None
        """

        blue_machine = BlueMachine(id, self.scale_factor_x, self.scale_factor_y)
        self.blue_machines.append(blue_machine)
        self.blue_machine_index = self.blue_machine_index + 1
        self.blue_machines_update_values.append(0)


class SpawnYellowMachine:
    """
        Represents the Yellow Machine container in Laser Fighter.

        Attributes:
            yellow_machines (list): Contains all of the yellow machine sprites currently visible/active on the screen.
            yellow_machines_update_values (list): Contains all of the death animation values for each yellow machine
                on the screen.
            yellow_machine_index (int): Stores the number of yellow machines currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Yellow Machine.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.yellow_machines = []
        self.yellow_machines_update_values = []
        self.yellow_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.yellow_machines
        del self.yellow_machines_update_values
        del self.yellow_machine_index

    def spawn_yellow_machine(self, id):
        """
            Spawn a yellow machine with the given id on the screen.

            :param id: The id that the enemy should have (Determines initial location of the enemy)
            :type id: int

            :return: None
        """

        yellow_machine = YellowMachine(id, self.scale_factor_x, self.scale_factor_y)
        self.yellow_machines.append(yellow_machine)
        self.yellow_machine_index = self.yellow_machine_index + 1
        self.yellow_machines_update_values.append(0)
