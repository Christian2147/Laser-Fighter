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

from components.enemy.MachineBlueMachine import BlueMachine
from components.enemy.MachineYellowMachine import YellowMachine
from components.enemy.MachineRedMachine import RedMachine
from components.enemy.MachineBoss import Boss


class SpawnBlueMachine:
    """
        Represents the Blue Machine container in Laser Fighter.

        Attributes:
            all_blue_machines (list): Contains all of the blue machine sprites created since the game has launched, even
                ones removed from the screen
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

        self.all_blue_machines = []
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

        del self.all_blue_machines
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

        if len(self.all_blue_machines) <= len(self.blue_machines):
            blue_machine = BlueMachine(id, self.scale_factor_x, self.scale_factor_y)
            self.blue_machines.append(blue_machine)
            self.blue_machine_index = self.blue_machine_index + 1
            self.all_blue_machines.append(blue_machine)
            self.blue_machines_update_values.append(0)
        else:
            for bm in self.all_blue_machines:
                if bm.get_blue_machine().isvisible():
                    continue
                else:
                    bm.reinstate(id)
                    self.blue_machines.append(bm)
                    self.blue_machine_index = self.blue_machine_index + 1
                    self.blue_machines_update_values.append(0)
                    break


class SpawnYellowMachine:
    """
        Represents the Yellow Machine container in Laser Fighter.

        Attributes:
            all_yellow_machines (list): Contains all of the yellow machine sprites created since the game has
                launched, even ones removed from the screen
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

        self.all_yellow_machines = []
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

        del self.all_yellow_machines
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

        if len(self.all_yellow_machines) <= len(self.yellow_machines):
            yellow_machine = YellowMachine(id, self.scale_factor_x, self.scale_factor_y)
            self.yellow_machines.append(yellow_machine)
            self.yellow_machine_index = self.yellow_machine_index + 1
            self.all_yellow_machines.append(yellow_machine)
            self.yellow_machines_update_values.append(0)
        else:
            for ym in self.all_yellow_machines:
                if ym.get_yellow_machine().isvisible():
                    continue
                else:
                    ym.reinstate(id)
                    self.yellow_machines.append(ym)
                    self.yellow_machine_index = self.yellow_machine_index + 1
                    self.yellow_machines_update_values.append(0)
                    break


class SpawnRedMachine:
    """
        Represents the Red Machine container in Laser Fighter.

        Attributes:
            all_red_machines (list): Contains all of the red machine sprites created since the game has
                launched, even ones removed from the screen
            red_machines (list): Contains all of the red machine sprites currently visible/active on the screen.
            red_machines_update_values (list): Contains all of the death animation values for each red machine
                on the screen.
            red_machines_hit_values (list): Contains all of the hit delay values for each red machine on the screen.
            red_machine_index (int): Stores the number of red machines currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Red Machine.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.all_red_machines = []
        self.red_machines = []
        self.red_machines_update_values = []
        self.red_machines_hit_values = []
        self.red_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_red_machines
        del self.red_machines
        del self.red_machines_update_values
        del self.red_machines_hit_values
        del self.red_machine_index

    def spawn_red_machine(self, id):
        """
            Spawn a red machine with the given id on the screen.

            :param id: The id that the enemy should have (Determines initial location of the enemy)
            :type id: int

            :return: None
        """

        if len(self.all_red_machines) <= len(self.red_machines):
            red_machine = RedMachine(id, self.scale_factor_x, self.scale_factor_y)
            self.red_machines.append(red_machine)
            self.red_machine_index = self.red_machine_index + 1
            self.all_red_machines.append(red_machine)
            self.red_machines_update_values.append(0)
            self.red_machines_hit_values.append(0)
        else:
            for rm in self.all_red_machines:
                if rm.get_red_machine().isvisible():
                    continue
                else:
                    rm.reinstate(id)
                    self.red_machines.append(rm)
                    self.red_machine_index = self.red_machine_index + 1
                    self.red_machines_update_values.append(0)
                    self.red_machines_hit_values.append(0)
                    break


class SpawnMachineBoss:
    """
        Represents the Machine Boss container in Laser Fighter.

        Attributes:
            all_boss (list): Contains the one boss sprite that should be spawn throughout the entire game.
            boss (list): Contains the boss sprite if it is visible on the screen
            boss_update_value (list): Contains the death animation value for the boss
            boss_hit_value (list): Contains the hit delay value for the boss
            boss_index (int): Stores whether the boss sprite has been created or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Machine Boss.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.all_boss = []
        self.boss = []
        self.boss_update_value = 0
        self.boss_hit_value = 0
        self.boss_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_boss
        del self.boss
        del self.boss_update_value
        del self.boss_hit_value
        del self.boss_index

    def spawn_boss(self):
        """
            Spawn a Machine Mode boss on the screen.

            :return: None
        """

        if len(self.all_boss) <= len(self.boss):
            spawn_boss = Boss(self.scale_factor_x, self.scale_factor_y)
            self.boss.append(spawn_boss)
            self.boss_index = self.boss_index + 1
            self.all_boss.append(spawn_boss)
        else:
            for b in self.all_boss:
                if b.get_boss().isvisible():
                    continue
                else:
                    b.reinstate()
                    self.boss.append(b)
                    self.boss_index = self.boss_index + 1
                    break
