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

from components.ItemPowerUp import PowerUp
from components.ItemPowerUp import YellowIndicator
from components.ItemPowerUp import BlueIndicator
from components.ItemPowerUp import ExtraIndicator


class SpawnPowerUp:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_power_ups = []
        self.current_power_ups = []
        self.power_up_index = [0, 0, 0, 0]
        self.power_up_update = 0
        self.power_up_time = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_power_ups
        del self.current_power_ups
        del self.power_up_index
        del self.power_up_update
        del self.power_up_time

    def spawn_power_up(self, type, mode, power_up_spawn_sound):
        """
            Spawn a power up on the screen.
            The type of power up depends on the parameter "type".
            What height it spawns at depends on the current mode the user is in.

            :param type: Determines which type of power up spawns
            :type type: int

            :return: None
        """

        if len(self.all_power_ups) <= len(self.current_power_ups):
            if type == 1:
                if mode == "Machine_Mode":
                    power_up = PowerUp(1, 1, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                elif mode == "Alien_Mode":
                    power_up = PowerUp(1, 2, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                self.power_up_index[0] = 1
                self.current_power_ups.append(power_up)
                self.all_power_ups.append(power_up)
            elif type == 2:
                if mode == "Machine_Mode":
                    power_up = PowerUp(2, 1, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                elif mode == "Alien_Mode":
                    power_up = PowerUp(2, 2, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                self.power_up_index[1] = 1
                self.current_power_ups.append(power_up)
                self.all_power_ups.append(power_up)
            elif type == 3:
                if mode == "Machine_Mode":
                    power_up = PowerUp(3, 1, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                elif mode == "Alien_Mode":
                    power_up = PowerUp(3, 2, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                self.power_up_index[2] = 1
                self.current_power_ups.append(power_up)
                self.all_power_ups.append(power_up)
            else:
                if mode == "Machine_Mode":
                    power_up = PowerUp(4, 1, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                elif mode == "Alien_Mode":
                    power_up = PowerUp(4, 2, power_up_spawn_sound, self.scale_factor_x, self.scale_factor_y)
                self.power_up_index[3] = 1
                self.current_power_ups.append(power_up)
                self.all_power_ups.append(power_up)
        else:
            for pu in self.all_power_ups:
                if pu.get_power_up().isvisible():
                    continue
                else:
                    if type == 1:
                        if mode == "Machine_Mode":
                            pu.reinstate(1, 1, power_up_spawn_sound)
                        elif mode == "Alien_Mode":
                            pu.reinstate(1, 2, power_up_spawn_sound)
                        self.power_up_index[0] = 1
                        self.current_power_ups.append(pu)
                    elif type == 2:
                        if mode == "Machine_Mode":
                            pu.reinstate(2, 1, power_up_spawn_sound)
                        elif mode == "Alien_Mode":
                            pu.reinstate(2, 2, power_up_spawn_sound)
                        self.power_up_index[1] = 1
                        self.current_power_ups.append(pu)
                    elif type == 3:
                        if mode == "Machine_Mode":
                            pu.reinstate(3, 1, power_up_spawn_sound)
                        elif mode == "Alien_Mode":
                            pu.reinstate(3, 2, power_up_spawn_sound)
                        self.power_up_index[2] = 1
                        self.current_power_ups.append(pu)
                    else:
                        if mode == "Machine_Mode":
                            pu.reinstate(4, 1, power_up_spawn_sound)
                        elif mode == "Alien_Mode":
                            pu.reinstate(4, 2, power_up_spawn_sound)
                        self.power_up_index[3] = 1
                        self.current_power_ups.append(pu)
                    break


class SpawnYellowPowerUpIndicator:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.yellow_power_up_indicator_turtle = []
        self.yellow_power_up_indicator_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.yellow_power_up_indicator_turtle
        del self.yellow_power_up_indicator_index

    def spawn_yellow_power_up_indicator(self):
        """
            Spawn a yellow power up indicator at the top of the screen.

            :return: None
        """

        if len(self.yellow_power_up_indicator_turtle) == 0:
            yellow_power_up_indicator = YellowIndicator(self.scale_factor_x, self.scale_factor_y)
            self.yellow_power_up_indicator_turtle.append(yellow_power_up_indicator)
            self.yellow_power_up_indicator_index = self.yellow_power_up_indicator_index + 1
        else:
            for yi in self.yellow_power_up_indicator_turtle:
                if yi.get_yellow_power_up_indicator().isvisible():
                    continue
                else:
                    yi.reinstate()
                    self.yellow_power_up_indicator_index = self.yellow_power_up_indicator_index + 1
                    break


class SpawnBluePowerUpIndicator:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.blue_power_up_indicator_turtle = []
        self.blue_power_up_indicator_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.blue_power_up_indicator_turtle
        del self.blue_power_up_indicator_index

    def spawn_blue_power_up_indicator(self):
        """
            Spawn a blue power up indicator at the top of the screen.

            :return: None
        """

        if len(self.blue_power_up_indicator_turtle) == 0:
            blue_power_up_indicator = BlueIndicator(self.scale_factor_x, self.scale_factor_y)
            self.blue_power_up_indicator_turtle.append(blue_power_up_indicator)
            self.blue_power_up_indicator_index = self.blue_power_up_indicator_index + 1
        else:
            for bi in self.blue_power_up_indicator_turtle:
                if bi.get_blue_power_up_indicator().isvisible():
                    continue
                else:
                    bi.reinstate()
                    self.blue_power_up_indicator_index = self.blue_power_up_indicator_index + 1
                    break


class SpawnExtraPowerUpIndicator:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.extra_power_up_indicator_turtle = []
        self.extra_power_up_indicator_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.extra_power_up_indicator_turtle
        del self.extra_power_up_indicator_index

    def spawn_extra_power_up_indiciator(self, mode):
        """
            Spawn an extra power up indicator at the top of the screen.

            :return: None
        """

        if len(self.extra_power_up_indicator_turtle) == 0:
            # The id depends on the current mode the user is in (Whether it will be green or blue)
            if mode == "Machine_Mode":
                extra_power_up_indicator = ExtraIndicator(1, self.scale_factor_x, self.scale_factor_y)
            elif mode == "Alien_Mode":
                extra_power_up_indicator = ExtraIndicator(2, self.scale_factor_x, self.scale_factor_y)
            self.extra_power_up_indicator_turtle.append(extra_power_up_indicator)
            self.extra_power_up_indicator_index = self.extra_power_up_indicator_index + 1
        else:
            for ei in self.extra_power_up_indicator_turtle:
                if ei.get_extra_power_up_indicator().isvisible():
                    continue
                else:
                    if mode == "Machine_Mode":
                        ei.reinstate(1)
                    elif mode == "Alien_Mode":
                        ei.reinstate(2)
                    self.extra_power_up_indicator_index = self.extra_power_up_indicator_index + 1
                    break
