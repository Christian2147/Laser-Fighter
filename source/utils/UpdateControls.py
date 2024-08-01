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
    File: ConfigManager.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:

"""

import ctypes
import configparser
from utils.ConfigManager import ConfigManager


class ControlsConfig:
    def __init__(self):
        self.check_config_file = 'config/keyUpdate.ini'
        self.config = ConfigManager()
        self.key_update = configparser.ConfigParser()

        self.go_right_key = ''
        self.go_left_key = ''
        self.shoot_key = ''
        self.jump_key = ''

        self.load()

        self.key_check = ['', '', '', '']

        self.check_load()

        if self.key_check[0] == 'space':
            self.go_right_key = 'space'
        elif self.key_check[1] == 'space':
            self.go_left_key = 'space'
        elif self.key_check[2] == 'space':
            self.shoot_key = 'space'
        elif self.key_check[3] == 'space':
            self.jump_key = 'space'

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.check_config_file
        del self.config
        del self.key_update
        del self.go_right_key
        del self.go_left_key
        del self.shoot_key
        del self.jump_key

    def load(self):
        self.go_right_key = self.config.get('Controls', 'Go_Right')
        self.go_left_key = self.config.get('Controls', 'Go_Left')
        self.shoot_key = self.config.get('Controls', 'Shoot')
        self.jump_key = self.config.get('Controls', 'Jump')

    def check_load(self):
        try:
            self.key_update.read(self.check_config_file)

            self.key_check[0] = self.key_update['Key_Update'].get('Key_1')
            self.key_check[1] = self.key_update['Key_Update'].get('Key_2')
            self.key_check[2] = self.key_update['Key_Update'].get('Key_3')
            self.key_check[3] = self.key_update['Key_Update'].get('Key_4')
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)

    def save(self):
        self.config.set('Controls', 'Go_Right', self.go_right_key)
        self.config.set('Controls', 'Go_Left', self.go_left_key)
        self.config.set('Controls', 'Shoot', self.shoot_key)
        self.config.set('Controls', 'Jump', self.jump_key)

    def save_check(self):
        try:
            self.key_update['Key_Update']['Key_1'] = self.key_check[0]
            self.key_update['Key_Update']['Key_2'] = self.key_check[1]
            self.key_update['Key_Update']['Key_3'] = self.key_check[2]
            self.key_update['Key_Update']['Key_4'] = self.key_check[3]

            with open(self.check_config_file, 'w') as checkconfigfile:
                self.key_update.write(checkconfigfile)
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error saving config file: {e}", "Error", 0x10)

    def __repr__(self):
        return (f"KeyBindings("
                f"go_right_key='{self.go_right_key}', "
                f"go_left_key='{self.go_left_key}', "
                f"shoot_key='{self.shoot_key}', "
                f"jump_key='{self.jump_key}', "
                f"go_right_check='{self.key_check[0]}', "
                f"go_left_check='{self.key_check[1]}', "
                f"shoot_check='{self.key_check[2]}', "
                f"jump_check='{self.key_check[3]}')")
