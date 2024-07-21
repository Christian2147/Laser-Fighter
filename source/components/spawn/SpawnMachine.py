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

from components.enemy.MachineBlueMachine import BlueMachine
from components.enemy.MachineYellowMachine import YellowMachine
from components.enemy.MachineRedMachine import RedMachine
from components.enemy.MachineBoss import Boss


class SpawnBlueMachine:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_blue_machines = []
        self.blue_machines = []
        self.blue_machines_update_values = []
        self.blue_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
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
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_yellow_machines = []
        self.yellow_machines = []
        self.yellow_machines_update_values = []
        self.yellow_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
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
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_red_machines = []
        self.red_machines = []
        self.red_machines_update_values = []
        self.red_machines_hit_values = []
        self.red_machine_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
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
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_boss = []
        self.boss = []
        self.boss_update_value = 0
        self.boss_hit_value = 0
        self.boss_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
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
