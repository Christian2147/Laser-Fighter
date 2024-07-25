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

import ctypes
import configparser


class ControlsConfig:
    def __init__(self):
        self.config_file = 'Config/config.ini'
        self.check_config_file = 'Config/keyUpdate.ini'
        self.config = configparser.ConfigParser()

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
        del self.config_file
        del self.check_config_file

    def load(self):
        self.config.read(self.config_file)

        self.go_right_key = self.config['Controls'].get('Go_Right')
        self.go_left_key = self.config['Controls'].get('Go_Left')
        self.shoot_key = self.config['Controls'].get('Shoot')
        self.jump_key = self.config['Controls'].get('Jump')

    def check_load(self):
        self.config.read(self.check_config_file)

        self.key_check[0] = self.config['Key_Update'].get('Key_1')
        self.key_check[1] = self.config['Key_Update'].get('Key_2')
        self.key_check[2] = self.config['Key_Update'].get('Key_3')
        self.key_check[3] = self.config['Key_Update'].get('Key_4')

    def save(self):
        try:
            self.config['Controls']['Go_Right'] = self.go_right_key
            self.config['Controls']['Go_Left'] = self.go_left_key
            self.config['Controls']['Shoot'] = self.shoot_key
            self.config['Controls']['Jump'] = self.jump_key

            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error saving config file: {e}", "Error", 0x10)

    def save_check(self):
        try:
            self.config['Key_Update']['Key_1'] = self.key_check[0]
            self.config['Key_Update']['Key_2'] = self.key_check[1]
            self.config['Key_Update']['Key_3'] = self.key_check[2]
            self.config['Key_Update']['Key_4'] = self.key_check[3]

            with open(self.check_config_file, 'w') as checkconfigfile:
                self.config.write(checkconfigfile)
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
