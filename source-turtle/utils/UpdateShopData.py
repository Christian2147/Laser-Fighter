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
    File: UpdateShopData.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for saving the shop configuration to the player data file and for loading the
        current shop configuration from the player data file.
    Data like the users coins, what items the user has bought, and what weapons the user has selected are
        updated and saved here.
"""

from utils.PlayerDataManager import PlayerDataManager


class ShopConfig:
    """
        Represents the parser for the current game shop configuration.

        Attributes:
            player_data_manager (PlayerDataManager()): The parser for the playerData.ini file

            total_coins (int): The total number of coins that the user currently owns
            machine_slot_selected (int): The current machine player selected in the shop
            alien_slot_selected (int): The current gun selected in the shop

            machine_slots_unlocked (list): A list that determines if each machine player slot in the
                shop is unlocked or not (1 = unlocked and 0 = locked)
            alien_slots_unlocked (list): A list that determines if each alien gun slot in the
                shop is unlocked or not (1 = unlocked and 0 = locked)

            yellow_power_up_level (int): The current level of the yellow power up
            blue_power_up_level (int): The current level of the blue power up
            green_power_up_level (int): The current level of the green power up
            red_power_up_level (int): The current level of the red power up

            coin_magnet_unlocked (boolean): Determines if the coin magnet gadget is unlocked.
            shield_unlocked (boolean): Determines if the shield gadget is unlocked.
            thorns_unlocked (boolean): Determines if the thorns gadget is unlocked.
            hearts_unlocked (boolean): Determines if the hearts gadget is unlocked.

            coin_magnet_enabled (boolean): Determines if the coin magnet gadget is currently enabled.
            shield_enabled (boolean): Determines if the shield gadget is currently enabled.
            thorns_enabled (boolean): Determines if the thorns gadget is currently enabled.
            hearts_enabled (boolean): Determines if the hearts gadget is currently enabled.
    """

    def __init__(self):
        """
            Initializes and loads the current shop configuration.
        """

        # Initialize the playerData.ini parser
        self.player_data_manager = PlayerDataManager()

        # Initialize the shop configuration variables
        self.total_coins = 0

        self.machine_slot_selected = 0
        self.alien_slot_selected = 0

        self.machine_slots_unlocked = []
        self.alien_slots_unlocked = []

        self.yellow_power_up_level = 0
        self.blue_power_up_level = 0
        self.green_power_up_level = 0
        self.red_power_up_level = 0

        self.coin_magnet_unlocked = False
        self.shield_unlocked = False
        self.thorns_unlocked = False
        self.hearts_unlocked = False

        self.coin_magnet_enabled = False
        self.shield_enabled = False
        self.thorns_enabled = False
        self.hearts_enabled = False

        # Load the current shop configuration
        self.load()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.player_data_manager

    def load(self):
        """
            Loads the current shop configuration from the player data file.

            :return: None
        """

        self.total_coins = self.player_data_manager.getint('Coins', 'coins')

        self.machine_slot_selected = self.player_data_manager.getint('Machine_Player_Enabled', 'type_enabled')
        self.alien_slot_selected = self.player_data_manager.getint('Alien_Mode_Gun_Enabled', 'type_enabled')

        self.machine_slots_unlocked = [self.player_data_manager.getint('Machine_Unlocked', f'slot_{i + 1}') for i in range(5)]
        self.alien_slots_unlocked = [self.player_data_manager.getint('Alien_Unlocked', f'slot_{i + 1}') for i in range(5)]

        self.yellow_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Yellow_Power_Up')
        self.blue_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Blue_Power_Up')
        self.green_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Green_Power_Up')
        self.red_power_up_level = self.player_data_manager.getint('Power_Up_Levels', 'Red_Power_Up')

        self.coin_magnet_unlocked = self.player_data_manager.getboolean('Gadgets_Unlocked', 'Coin_Magnet_Unlocked')
        self.shield_unlocked = self.player_data_manager.getboolean('Gadgets_Unlocked', 'Armor_Unlocked')
        self.thorns_unlocked = self.player_data_manager.getboolean('Gadgets_Unlocked', 'Thorns_Unlocked')
        self.hearts_unlocked = self.player_data_manager.getboolean('Gadgets_Unlocked', 'Hearts_Unlocked')

        self.coin_magnet_enabled = self.player_data_manager.getboolean('Gadgets_Enabled', 'Coin_Magnet_Enabled')
        self.shield_enabled = self.player_data_manager.getboolean('Gadgets_Enabled', 'Armor_Enabled')
        self.thorns_enabled = self.player_data_manager.getboolean('Gadgets_Enabled', 'Thorns_Enabled')
        self.hearts_enabled = self.player_data_manager.getboolean('Gadgets_Enabled', 'Hearts_Enabled')

    def save(self):
        """
            Saves the current shop configuration to the player data file.

            :return: None
        """

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

        self.player_data_manager.set('Gadgets_Unlocked', 'Coin_Magnet_Unlocked', str(self.coin_magnet_unlocked))
        self.player_data_manager.set('Gadgets_Unlocked', 'Armor_Unlocked', str(self.shield_unlocked))
        self.player_data_manager.set('Gadgets_Unlocked', 'Thorns_Unlocked', str(self.thorns_unlocked))
        self.player_data_manager.set('Gadgets_Unlocked', 'Hearts_Unlocked', str(self.hearts_unlocked))

        self.player_data_manager.set('Gadgets_Enabled', 'Coin_Magnet_Enabled', str(self.coin_magnet_enabled))
        self.player_data_manager.set('Gadgets_Enabled', 'Armor_Enabled', str(self.shield_enabled))
        self.player_data_manager.set('Gadgets_Enabled', 'Thorns_Enabled', str(self.thorns_enabled))
        self.player_data_manager.set('Gadgets_Enabled', 'Hearts_Enabled', str(self.hearts_enabled))

    def __repr__(self):
        """
            Creates a print statement for the current shop configuration where they are all listed out in order.

            :return: Prints the current shop configuration in a list.
            :type: string
        """

        return (f"PlayerConfig(total_coins={self.total_coins}, "
                f"machine_slot_selected={self.machine_slot_selected}, "
                f"alien_slot_selected={self.alien_slot_selected}, "
                f"machine_slots_unlocked={self.machine_slots_unlocked}, "
                f"alien_slots_unlocked={self.alien_slots_unlocked}, "
                f"yellow_power_up_level={self.yellow_power_up_level}, "
                f"blue_power_up_level={self.blue_power_up_level}, "
                f"green_power_up_level={self.green_power_up_level}, "
                f"red_power_up_level={self.red_power_up_level}, "
                f"coin_magnet_unlocked={self.coin_magnet_unlocked}, "
                f"shield_unlocked={self.shield_unlocked}, "
                f"thorns_unlocked={self.thorns_unlocked}, "
                f"hearts_unlocked={self.hearts_unlocked}, "
                f"coin_magnet_enabled={self.coin_magnet_enabled}, "
                f"shield_enabled={self.shield_enabled}, "
                f"thorns_enabled={self.thorns_enabled}, "
                f"hearts_enabled={self.hearts_enabled})")
