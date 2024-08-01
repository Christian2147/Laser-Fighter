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


class PowerUpSetup:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PowerUpSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config):
        self._shop_config = shop_config

        self._setup = 0

        self.yellow_power_up_speed_increase = 1
        self.yellow_power_up_movement_increase = 1
        self.blue_power_up_multiplier = 1
        self.blue_power_up_coin_multiplier = 1

        self.yellow_power_up_duration = 15
        self.blue_power_up_duration = 30
        self.green_power_up_duration = 10
        self.red_power_up_duration = 10

        self.copper_coin_value = 1
        self.silver_coin_value = 5
        self.gold_coin_value = 10
        self.platinum_coin_value = 25

        self.copper_coin_blue_value = 1
        self.silver_coin_blue_value = 5
        self.gold_coin_blue_value = 10
        self.platinum_coin_blue_value = 25

        self.setup_power_ups()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._shop_config
        del self._setup
        del self.yellow_power_up_speed_increase
        del self.yellow_power_up_movement_increase
        del self.blue_power_up_multiplier
        del self.blue_power_up_coin_multiplier
        del self.yellow_power_up_duration
        del self.blue_power_up_duration
        del self.green_power_up_duration
        del self.red_power_up_duration
        del self.copper_coin_value
        del self.silver_coin_value
        del self.gold_coin_value
        del self.platinum_coin_value
        del self.copper_coin_blue_value
        del self.silver_coin_blue_value
        del self.gold_coin_blue_value
        del self.platinum_coin_blue_value

    @property
    def setup(self):
        return self._setup

    @setup.setter
    def setup(self, value):
        if isinstance(value, int):
            self._setup = value
        else:
            raise ValueError("Value must be an integer")

    def setup_power_ups(self):
        if self._shop_config.yellow_power_up_level == 1:
            self.yellow_power_up_speed_increase = 2
            self.yellow_power_up_movement_increase = 1
            self.yellow_power_up_duration = 15
        elif self._shop_config.yellow_power_up_level == 2:
            self.yellow_power_up_speed_increase = 2.5
            self.yellow_power_up_movement_increase = 1
            self.yellow_power_up_duration = 20
        elif self._shop_config.yellow_power_up_level == 3:
            self.yellow_power_up_speed_increase = 2.5
            self.yellow_power_up_movement_increase = 1.5
            self.yellow_power_up_duration = 30
        elif self._shop_config.yellow_power_up_level == 4:
            self.yellow_power_up_speed_increase = 2.75
            self.yellow_power_up_movement_increase = 1.5
            self.yellow_power_up_duration = 45
        elif self._shop_config.yellow_power_up_level == 5:
            self.yellow_power_up_speed_increase = 3
            self.yellow_power_up_movement_increase = 2
            self.yellow_power_up_duration = 60

        if self._shop_config.blue_power_up_level == 1:
            self.blue_power_up_multiplier = 2
            self.blue_power_up_coin_multiplier = 1
            self.blue_power_up_duration = 30
        elif self._shop_config.blue_power_up_level == 2:
            self.blue_power_up_multiplier = 3
            self.blue_power_up_coin_multiplier = 1
            self.blue_power_up_duration = 45
        elif self._shop_config.blue_power_up_level == 3:
            self.blue_power_up_multiplier = 3
            self.blue_power_up_coin_multiplier = 2
            self.blue_power_up_duration = 60
        elif self._shop_config.blue_power_up_level == 4:
            self.blue_power_up_multiplier = 4
            self.blue_power_up_coin_multiplier = 2
            self.blue_power_up_duration = 75
        elif self._shop_config.blue_power_up_level == 5:
            self.blue_power_up_multiplier = 5
            self.blue_power_up_coin_multiplier = 3
            self.blue_power_up_duration = 90

        if self._shop_config.green_power_up_level == 1:
            self.green_power_up_duration = 10
        elif self._shop_config.green_power_up_level == 2:
            self.green_power_up_duration = 20
        elif self._shop_config.green_power_up_level == 3:
            self.green_power_up_duration = 25
        elif self._shop_config.green_power_up_level == 4:
            self.green_power_up_duration = 30
        elif self._shop_config.green_power_up_level == 5:
            self.green_power_up_duration = 40

        if self._shop_config.red_power_up_level == 1:
            self.red_power_up_duration = 10
        elif self._shop_config.red_power_up_level == 2:
            self.red_power_up_duration = 20
        elif self._shop_config.red_power_up_level == 3:
            self.red_power_up_duration = 25
        elif self._shop_config.red_power_up_level == 4:
            self.red_power_up_duration = 30
        elif self._shop_config.red_power_up_level == 5:
            self.red_power_up_duration = 40

        self.copper_coin_blue_value = self.copper_coin_value * self.blue_power_up_coin_multiplier
        self.silver_coin_blue_value = self.silver_coin_value * self.blue_power_up_coin_multiplier
        self.gold_coin_blue_value = self.gold_coin_value * self.blue_power_up_coin_multiplier
        self.platinum_coin_blue_value = self.platinum_coin_value * self.blue_power_up_coin_multiplier
