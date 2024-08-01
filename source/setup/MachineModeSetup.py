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
    File: MachineModeSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the setup logic for Machine Mode. This setup logic is run every time the title screen is launched.
    Here, variables for Machine Mode are pre defined before the game starts to avoid in-game lag.
"""

from setup.WindowSetup import scale_factor_X
from setup.WindowSetup import scale_factor_Y
from setup.TextureSetup import MACHINE_PLAYER_TEXTURE
from setup.TextureSetup import MACHINE_PLAYER_LASER_TEXTURE
from setup.TextureSetup import MACHINE_WASHER_TEXTURE
from setup.TextureSetup import MACHINE_WASHER_LASER_TEXTURE
from setup.TextureSetup import THE_INCINERATOR_TEXTURE
from setup.TextureSetup import INCINERATOR_LASER_TEXTURE
from setup.TextureSetup import THE_BLACK_HOLE_TEXTURE
from setup.TextureSetup import BLACK_HOLE_LASER_TEXTURE
from setup.TextureSetup import THE_STAR_KILLER_TEXTURE
from setup.TextureSetup import STAR_KILLER_LASER_TEXTURE


class MachineModeSetup:
    """
        Represents the setup logic for Machine Mode.

        Class Variables:
            MACHINE_MOVE_(Num) (float): Stores the speed at which the machine will move side to side depending on how
                many times it has been killed.
            MACHINE_FLOAT (float): Stores the speed at which the machine will float up and down.

        Pointers:
            _shop_config (ShopConfig()): A pointer to the Shop Configuration.
            _power_up_setup (PowerUpSetup()): A pointer to the current power up configuration.
            _scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode

        Attributes:
            regular_score_multiplier (int): Stores the default score multiplier for Alien Mode (How much does a point
                increase your score)
            blue_power_up_score_multiplier (int): Store the score multiplier when the blue power up is activated

            player_texture (string): Stores the current player texture (depending on the shop selection)

            laser_texture (string): Stores the current laser texture (depending on shop selection)
            laser_offset (int): Stores the current offset of the lasers coordinate vs the players (bigger for
                bigger lasers)
            laser_max_distance (int): Stores the maximum distance the laser will travel before it disappears and is
                able to be fired agian.

            laser_speed (float): Stores the player lasers speed
            yellow_power_up_speed (float): Stores the lasers speed when the yellow power up is activated

            damage (int): Stores the current damage infliction of the player
            laser_count (int): Stores the number of lasers fired each round

            player_movement (float): Stores the players movement speed
            yellow_player_movement (float): Stores the players movement speed when the yellow power up is active

            power_up_spawn_rate (int): Stores the spawn rate of all power ups
        """

    MACHINE_MOVE_2 = 2 * scale_factor_X
    MACHINE_MOVE_4 = 4 * scale_factor_X
    MACHINE_MOVE_6 = 6 * scale_factor_X
    MACHINE_MOVE_8 = 8 * scale_factor_X
    MACHINE_MOVE_10 = 10 * scale_factor_X

    MACHINE_FLOAT = 0.15 * scale_factor_Y

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
            cls._instance = super(MachineModeSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config, power_up_setup, scale_factor_x, scale_factor_y):
        """
            Creates and configures the parameters for Machine Mode.

            :param shop_config: A pointer to the shop configuration
            :type shop_config: ShopConfig()

            :param power_up_setup: A pointer to the current power up setup
            :type power_up_setup: PowerUpSetup()

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        # Everything starts out initialized to 0
        self._shop_config = shop_config
        self._power_up_setup = power_up_setup
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self.regular_score_multiplier = 0
        self.blue_power_up_score_multiplier = 0

        self.player_texture = ""
        self.laser_texture = ""
        self.laser_offset = 0
        self.laser_max_distance = 0

        self.laser_speed = 0
        self.yellow_power_up_speed = 0

        self.damage = 0
        self.laser_count = 0

        self.player_movement = 30
        self.yellow_player_movement = 30
        self.power_up_spawn_rate = 1

        # Run the setup
        self.setup_machine_mode()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._shop_config
        del self._power_up_setup
        del self._scale_factor_x
        del self._scale_factor_y
        del self.regular_score_multiplier
        del self.blue_power_up_score_multiplier
        del self.player_texture
        del self.laser_texture
        del self.laser_offset
        del self.laser_max_distance
        del self.laser_speed
        del self.yellow_power_up_speed
        del self.damage
        del self.laser_count
        del self.player_movement
        del self.yellow_player_movement
        del self.power_up_spawn_rate

    def setup_machine_mode(self):
        """
            Sets up the Machine Mode variables.

            :return: None
        """

        # Initializes some variables to their default state (In case they do not need to change)
        self.player_movement = 30
        self.yellow_player_movement = 30
        self.power_up_spawn_rate = 1

        # Sets the variables based on which items in the shop are selected
        if self._shop_config.machine_slot_selected == 1:
            self.player_texture = MACHINE_PLAYER_TEXTURE

            self.laser_texture = MACHINE_PLAYER_LASER_TEXTURE
            self.laser_offset = 130 * self._scale_factor_y
            self.laser_speed = 14.5 * self._scale_factor_y #14.5
            self.laser_max_distance = 360 * self._scale_factor_y

            self.damage = 1
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.machine_slot_selected == 2:
            self.player_texture = MACHINE_WASHER_TEXTURE

            self.laser_texture = MACHINE_WASHER_LASER_TEXTURE
            self.laser_offset = 135 * self._scale_factor_y
            self.laser_speed = 25 * self._scale_factor_y
            self.laser_max_distance = 370 * self._scale_factor_y

            self.damage = 1
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.machine_slot_selected == 3:
            self.player_texture = THE_INCINERATOR_TEXTURE

            self.laser_texture = INCINERATOR_LASER_TEXTURE
            self.laser_offset = 135 * self._scale_factor_y
            self.laser_speed = 20 * self._scale_factor_y
            self.laser_max_distance = 470 * self._scale_factor_y

            self.damage = 1
            self.laser_count = 2

            self.regular_score_multiplier = 1
        elif self._shop_config.machine_slot_selected == 4:
            self.player_texture = THE_BLACK_HOLE_TEXTURE

            self.laser_texture = BLACK_HOLE_LASER_TEXTURE
            self.laser_offset = 145 * self._scale_factor_y
            self.laser_speed = 27 * self._scale_factor_y
            self.laser_max_distance = 580 * self._scale_factor_y

            self.damage = 2
            self.laser_count = 3

            self.regular_score_multiplier = 2
        elif self._shop_config.machine_slot_selected == 5:
            self.player_texture = THE_STAR_KILLER_TEXTURE

            self.laser_texture = STAR_KILLER_LASER_TEXTURE
            self.laser_offset = 145 * self._scale_factor_y
            self.laser_speed = 30 * self._scale_factor_y
            self.laser_max_distance = 580 * self._scale_factor_y

            self.damage = 2
            self.laser_count = 3

            self.regular_score_multiplier = 2
            self.power_up_spawn_rate = 2

        # After the player selection is detected, the variables are modified again based on the current level of the
        #   power ups
        self.yellow_power_up_speed = self.laser_speed * self._power_up_setup.yellow_power_up_speed_increase

        self.blue_power_up_score_multiplier = self.regular_score_multiplier * self._power_up_setup.blue_power_up_multiplier

        self.player_movement = self.player_movement * self._scale_factor_x
        self.yellow_player_movement = self.player_movement * self._power_up_setup.yellow_power_up_movement_increase
