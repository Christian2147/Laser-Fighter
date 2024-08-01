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

from utils.PlayerDataManager import PlayerDataManager


class ShopConfig:
    def __init__(self):
        self.player_data_manager = PlayerDataManager()

        self.total_coins = 0
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
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.player_data_manager

    def load(self):
        self.total_coins = self.player_data_manager.getint('Coins', 'coins')

        self.machine_slot_selected = self.player_data_manager.getint('Machine_Player_Enabled', 'type_enabled')
        self.alien_slot_selected = self.player_data_manager.getint('Alien_Mode_Gun_Enabled', 'type_enabled')

        self.machine_slots_unlocked = [self.player_data_manager.getint('Machine_Unlocked', f'slot_{i + 1}') for i in range(5)]
        self.alien_slots_unlocked = [self.player_data_manager.getint('Alien_Unlocked', f'slot_{i + 1}') for i in range(5)]
        self.yellow_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Yellow_Power_Up')
        self.blue_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Blue_Power_Up')
        self.green_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Green_Power_Up')
        self.red_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Red_Power_Up')

    def save(self):
        self.player_data_manager.set('Coins', 'coins', str(self.total_coins))

        self.player_data_manager.set('Machine_Player_Enabled', 'type_enabled', str(self.machine_slot_selected))
        self.player_data_manager.set('Alien_Mode_Gun_Enabled', 'type_enabled', str(self.alien_slot_selected))

        for i in range(5):
            self.player_data_manager.set('Machine_Unlocked', f'slot_{i + 1}', str(self.machine_slots_unlocked[i]))
            self.player_data_manager.set('Alien_Unlocked', f'slot_{i + 1}', str(self.alien_slots_unlocked[i]))

        self.player_data_manager.set('Power_Up_Levels', 'Yellow_Power_Up', str(self.yellow_power_up_level))
        self.player_data_manager.set('Power_Up_Levels', 'Blue_Power_Up', str(self.blue_power_up_level))
        self.player_data_manager.set('Power_Up_Levels', 'Green_Power_Up', str(self.green_power_up_level))
        self.player_data_manager.set('Power_Up_Levels', 'Red_Power_Up', str(self.red_power_up_level))

    def __repr__(self):
        return (f"PlayerConfig(total_coins={self.total_coins}, "
                f"machine_slot_selected={self.machine_slot_selected}, "
                f"alien_slot_selected={self.alien_slot_selected}, "
                f"machine_slots_unlocked={self.machine_slots_unlocked}, "
                f"alien_slots_unlocked={self.alien_slots_unlocked}, "
                f"yellow_power_up_level={self.yellow_power_up_level}, "
                f"blue_power_up_level={self.blue_power_up_level}, "
                f"green_power_up_level={self.green_power_up_level}, "
                f"red_power_up_level={self.red_power_up_level})")
