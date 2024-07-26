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

from setup.TextureSetup import PLAYER_GUN_RIGHT_TEXTURE
from setup.TextureSetup import PLAYER_GUN_LEFT_TEXTURE
from setup.TextureSetup import THE_COOKER_RIGHT_TEXTURE
from setup.TextureSetup import THE_COOKER_LEFT_TEXTURE
from setup.TextureSetup import POISON_DART_GUN_RIGHT_TEXTURE
from setup.TextureSetup import POISON_DART_GUN_LEFT_TEXTURE
from setup.TextureSetup import METEOR_GUN_RIGHT_TEXTURE
from setup.TextureSetup import METEOR_GUN_LEFT_TEXTURE
from setup.TextureSetup import SUPERNOVA_RIGHT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LEFT_TEXTURE
from setup.TextureSetup import PLAYER_HEAD_LASER_TEXTURE
from setup.TextureSetup import THE_COOKER_LASER_TEXTURE
from setup.TextureSetup import POISON_DART_LASER_TEXTURE
from setup.TextureSetup import METEOR_GUN_LASER_RIGHT_TEXTURE
from setup.TextureSetup import METEOR_GUN_LASER_LEFT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LASER_RIGHT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LASER_LEFT_TEXTURE


class AlienModeSetup:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AlienModeSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config, scale_factor_x, scale_factor_y):
        self._shop_config = shop_config
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self._setup = 0

        self.regular_score_multiplier = 0
        self.blue_power_up_multiplier = 0
        self.blue_power_up_score_multiplier = 0

        self.gun_right_texture = ""
        self.gun_left_texture = ""
        self.gun_offset = 0
        self.laser_right_texture = ""
        self.laser_left_texture = ""
        self.laser_offset = 0

        self.yellow_power_up_speed_increase = 0
        self.laser_speed = 0
        self.yellow_power_up_speed = 0

        self.damage = 0
        self.piercing = 0
        self.laser_count = 0

        self.setup_alien_mode()

    def __del__(self):
        del self._shop_config
        del self._scale_factor_x
        del self._scale_factor_y
        del self._setup
        del self.regular_score_multiplier
        del self.blue_power_up_multiplier
        del self.blue_power_up_score_multiplier
        del self.gun_right_texture
        del self.gun_left_texture
        del self.gun_offset
        del self.laser_right_texture
        del self.laser_left_texture
        del self.laser_offset
        del self.yellow_power_up_speed_increase
        del self.laser_speed
        del self.yellow_power_up_speed
        del self.damage
        del self.piercing
        del self.laser_count

    @property
    def setup(self):
        return self._setup

    @setup.setter
    def setup(self, value):
        if isinstance(value, int):
            self._setup = value
        else:
            raise ValueError("Value must be an integer")

    def setup_alien_mode(self):
        if self._shop_config.yellow_power_up_level == 1:
            self.yellow_power_up_speed_increase = 2
        elif self._shop_config.yellow_power_up_level == 2 or self._shop_config.yellow_power_up_level == 3:
            self.yellow_power_up_speed_increase = 3
        elif self._shop_config.yellow_power_up_level == 4 or self._shop_config.yellow_power_up_level == 5:
            self.yellow_power_up_speed_increase = 4

        if self._shop_config.blue_power_up_level == 1:
            self.blue_power_up_multiplier = 2
        elif self._shop_config.blue_power_up_level == 2 or self._shop_config.blue_power_up_level == 3:
            self.blue_power_up_multiplier = 3
        elif self._shop_config.blue_power_up_level == 4:
            self.blue_power_up_multiplier = 4
        elif self._shop_config.blue_power_up_level == 5:
            self.blue_power_up_multiplier = 5

        if self._shop_config.alien_slot_selected == 1:
            self.gun_right_texture = PLAYER_GUN_RIGHT_TEXTURE
            self.gun_left_texture = PLAYER_GUN_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = PLAYER_HEAD_LASER_TEXTURE
            self.laser_left_texture = PLAYER_HEAD_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 13 * self._scale_factor_x

            self.damage = 1
            self.piercing = 2
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 2:
            self.gun_right_texture = THE_COOKER_RIGHT_TEXTURE
            self.gun_left_texture = THE_COOKER_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = THE_COOKER_LASER_TEXTURE
            self.laser_left_texture = THE_COOKER_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 15 * self._scale_factor_x

            self.damage = 1
            self.piercing = 3
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 3:
            self.gun_right_texture = POISON_DART_GUN_RIGHT_TEXTURE
            self.gun_left_texture = POISON_DART_GUN_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = POISON_DART_LASER_TEXTURE
            self.laser_left_texture = POISON_DART_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 25 * self._scale_factor_x

            self.damage = 2
            self.piercing = 2
            self.laser_count = 2

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 4:
            self.gun_right_texture = METEOR_GUN_RIGHT_TEXTURE
            self.gun_left_texture = METEOR_GUN_LEFT_TEXTURE
            self.gun_offset = 28 * self._scale_factor_x

            self.laser_right_texture = METEOR_GUN_LASER_RIGHT_TEXTURE
            self.laser_left_texture = METEOR_GUN_LASER_LEFT_TEXTURE
            self.laser_offset = 65 * self._scale_factor_x

            self.laser_speed = 27 * self._scale_factor_x

            self.damage = 3
            self.piercing = 3
            self.laser_count = 1

            self.regular_score_multiplier = 2
        elif self._shop_config.alien_slot_selected == 5:
            self.gun_right_texture = SUPERNOVA_RIGHT_TEXTURE
            self.gun_left_texture = SUPERNOVA_LEFT_TEXTURE
            self.gun_offset = 28 * self._scale_factor_x

            self.laser_right_texture = SUPERNOVA_LASER_RIGHT_TEXTURE
            self.laser_left_texture = SUPERNOVA_LASER_LEFT_TEXTURE
            self.laser_offset = 65 * self._scale_factor_x

            self.laser_speed = 30 * self._scale_factor_x

            self.damage = 3
            self.piercing = 4
            self.laser_count = 2

            self.regular_score_multiplier = 2

        self.yellow_power_up_speed = self.laser_speed * self.yellow_power_up_speed_increase

        self.blue_power_up_score_multiplier = self.regular_score_multiplier * self.blue_power_up_multiplier


