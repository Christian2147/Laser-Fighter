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
    File: PowerUpSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the setup logic for the Power Ups. This setup logic is run every time the title screen is launched.
    Here, variables for the Power Ups are pre defined before the game starts to avoid in-game lag.
"""


class PowerUpSetup:
    """
        Represents the setup logic for the Power Ups.

        Pointers:
            _shop_config (ShopConfig()): A pointer to the Shop Configuration.

        Attributes:
            yellow_power_up_speed_increase (int): Stores the current speed increase when the yellow power up
                is activated
            yellow_power_up_movement_increase (int): Stores the current player movement increase when the yellow
                power up is activated

            blue_power_up_multiplier (int): Stores the score multiplier when the blue power up is activated
            blue_power_up_coin_multiplier (int): Stores the coin value multiplier when the blue power up is activated

            yellow_power_up_duration (int): Stores the current duration of the yellow power up
            blue_power_up_duration (int): Stores the current duration of the blue power up
            green_power_up_duration (int): Stores the current duration of the green power up
            red_power_up_duration (int): Stores the current duration of the red power up

            copper_coin_value (int): The default value of the copper coin
            silver_coin_value (int): The default value of the silver coin
            gold_coin_value (int): The default value of the gold coin
            platinum_coin_value (int): The default value of the platinum coin
    """

    # Set the instance to "None" at the beginning
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
            Ensures only one instance of this class exists at all times.

            :param args: NA
            :param kwargs: NA

            :return: The class instance (Which is created if it does nto already exist)
        """

        if cls._instance is None:
            cls._instance = super(PowerUpSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config):
        """
            Creates and configures the parameters for the Power Ups.

            :param shop_config: A pointer to the shop configuration
            :type shop_config: ShopConfig()
        """

        # Everything starts out initialized to 0
        self._shop_config = shop_config

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

        # Run the setup
        self.setup_power_ups()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._shop_config
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

    def setup_power_ups(self):
        # Setup the yellow power up based on its level
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

        # Setup the blue power up based on its level
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

        # Setup the green power up based on its level
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

        # Setup the red power up based on its level
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

        # Setup the coin values during gameplay
        self.copper_coin_blue_value = self.copper_coin_value * self.blue_power_up_coin_multiplier
        self.silver_coin_blue_value = self.silver_coin_value * self.blue_power_up_coin_multiplier
        self.gold_coin_blue_value = self.gold_coin_value * self.blue_power_up_coin_multiplier
        self.platinum_coin_blue_value = self.platinum_coin_value * self.blue_power_up_coin_multiplier
