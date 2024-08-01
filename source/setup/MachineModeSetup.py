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
    MACHINE_MOVE_2 = 2 * scale_factor_X
    MACHINE_MOVE_4 = 4 * scale_factor_X
    MACHINE_MOVE_6 = 6 * scale_factor_X
    MACHINE_MOVE_8 = 8 * scale_factor_X
    MACHINE_MOVE_10 = 10 * scale_factor_X

    MACHINE_FLOAT = 0.15 * scale_factor_Y

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MachineModeSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config, power_up_setup, scale_factor_x, scale_factor_y):
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
        self.player_movement = 30
        self.yellow_player_movement = 30
        self.power_up_spawn_rate = 1

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

        self.yellow_power_up_speed = self.laser_speed * self._power_up_setup.yellow_power_up_speed_increase

        self.blue_power_up_score_multiplier = self.regular_score_multiplier * self._power_up_setup.blue_power_up_multiplier

        self.player_movement = self.player_movement * self._scale_factor_x
        self.yellow_player_movement = self.player_movement * self._power_up_setup.yellow_power_up_movement_increase
