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

import configparser


class ShopConfig:
    def __init__(self):
        self.shop_config_file = 'Config/playerData.ini'
        self.config = configparser.ConfigParser()

        self.machine_slot_selected = 0
        self.alien_slot_selected = 0
        self.machine_slots_unlocked = []
        self.alien_slots_unlocked = []
        self.yellow_power_up_level = 0
        self.blue_power_up_level = 0
        self.green_power_up_level = 0
        self.red_power_up_level = 0

        self.load()

    def __del__(self):
        del self.shop_config_file

    def load(self):
        self.config.read(self.shop_config_file)
        self.machine_slot_selected = self.config['Machine_Player_Enabled'].getint('type_enabled')
        self.alien_slot_selected = self.config['Alien_Mode_Gun_Enabled'].getint('type_enabled')

        self.machine_slots_unlocked = [self.config['Machine_Unlocked'].getint(f'slot_{i + 1}') for i in range(5)]
        self.alien_slots_unlocked = [self.config['Alien_Unlocked'].getint(f'slot_{i + 1}') for i in range(5)]
        self.yellow_power_up_level = self.config['Power_Up_Levels'].getint('Yellow_Power_Up')
        self.blue_power_up_level = self.config['Power_Up_Levels'].getint('Blue_Power_Up')
        self.green_power_up_level = self.config['Power_Up_Levels'].getint('Green_Power_Up')
        self.red_power_up_level = self.config['Power_Up_Levels'].getint('Red_Power_Up')

    def save(self):
        self.config['Machine_Player_Enabled']['type_enabled'] = str(self.machine_slot_selected)
        self.config['Alien_Mode_Gun_Enabled']['type_enabled'] = str(self.alien_slot_selected)

        for i in range(5):
            self.config['Machine_Unlocked'][f'slot_{i + 1}'] = str(self.machine_slots_unlocked[i])
            self.config['Alien_Unlocked'][f'slot_{i + 1}'] = str(self.alien_slots_unlocked[i])

        self.config['Power_Up_Levels']['Yellow_Power_Up'] = str(self.yellow_power_up_level)
        self.config['Power_Up_Levels']['Blue_Power_Up'] = str(self.blue_power_up_level)
        self.config['Power_Up_Levels']['Green_Power_Up'] = str(self.green_power_up_level)
        self.config['Power_Up_Levels']['Red_Power_Up'] = str(self.red_power_up_level)

        with open(self.shop_config_file, 'w') as configfile:
            self.config.write(configfile)

    def __repr__(self):
        return (f"PlayerConfig(machine_slot_selected={self.machine_slot_selected}, "
                f"alien_slot_selected={self.alien_slot_selected}, "
                f"machine_slots_unlocked={self.machine_slots_unlocked}, "
                f"alien_slots_unlocked={self.alien_slots_unlocked}, "
                f"yellow_power_up_level={self.yellow_power_up_level}, "
                f"blue_power_up_level={self.blue_power_up_level}, "
                f"green_power_up_level={self.green_power_up_level}, "
                f"red_power_up_level={self.red_power_up_level})")
