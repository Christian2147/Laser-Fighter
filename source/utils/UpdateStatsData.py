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


class Stats:
    def __init__(self, god_mode):
        self.player_data_manager = PlayerDataManager()

        self.score = 0

        self.high_score_machine_war = 0
        self.bosses_killed = 0
        self.red_bots_killed = 0
        self.yellow_bots_killed = 0
        self.blue_bots_killed = 0
        self.classic_deaths = 0
        self.machine_damage_taken = 0
        self.classic_lasers_fired = 0
        self.classic_power_ups_picked_up = 0
        self.machine_coins_collected = 0

        self.high_score_alien_mode = 0
        self.ufos_killed = 0
        self.big_aliens_killed = 0
        self.medium_aliens_killed = 0
        self.small_aliens_killed = 0
        self.alien_deaths = 0
        self.damage_taken = 0
        self.alien_lasers_fired = 0
        self.jumps = 0
        self.alien_power_ups_picked_up = 0
        self.alien_coins_collected = 0

        self.god_mode = god_mode

        self.load()

    def __del__(self):
        del self.player_data_manager

    def load(self):
        # Machine Mode Statistics
        if self.god_mode == 1:
            self.high_score_machine_war = "NA"
        else:
            self.high_score_machine_war = self.player_data_manager.getint('High_Score', 'High_Score_Machine_War')
        self.bosses_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Bosses_Killed')
        self.red_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Red_Bots_Killed')
        self.yellow_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Yellow_Bots_Killed')
        self.blue_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Blue_Bots_Killed')
        self.classic_deaths = self.player_data_manager.getint('Statistics_Machine_Mode', 'Deaths')
        self.machine_damage_taken = self.player_data_manager.getint('Statistics_Machine_Mode', 'Damage_Taken')
        self.classic_lasers_fired = self.player_data_manager.getint('Statistics_Machine_Mode', 'Lasers_Fired')
        self.classic_power_ups_picked_up = self.player_data_manager.getint('Statistics_Machine_Mode', 'Power_Ups_Picked_Up')
        self.machine_coins_collected = self.player_data_manager.getint('Statistics_Machine_Mode', 'Coins_Collected')

        # Alien Mode Statistics
        if self.god_mode == 1:
            self.high_score_alien_mode = "NA"
        else:
            self.high_score_alien_mode = self.player_data_manager.getint('High_Score', 'High_Score_Alien_Mode')
        self.ufos_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Ufos_Killed')
        self.big_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Big_Aliens_Killed')
        self.medium_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Medium_Aliens_Killed')
        self.small_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Small_Aliens_Killed')
        self.alien_deaths = self.player_data_manager.getint('Statistics_Alien_Mode', 'Deaths')
        self.damage_taken = self.player_data_manager.getint('Statistics_Alien_Mode', 'Damage_Taken')
        self.alien_lasers_fired = self.player_data_manager.getint('Statistics_Alien_Mode', 'Lasers_Fired')
        self.jumps = self.player_data_manager.getint('Statistics_Alien_Mode', 'Jumps')
        self.alien_power_ups_picked_up = self.player_data_manager.getint('Statistics_Alien_Mode', 'Power_Ups_Picked_Up')
        self.alien_coins_collected = self.player_data_manager.getint('Statistics_Alien_Mode', 'Coins_Collected')

    def save(self):
        if self.god_mode != 1:
            self.player_data_manager.set('High_Score', 'High_Score_Machine_War', str(self.high_score_machine_war))
            self.player_data_manager.set('High_Score', 'High_Score_Alien_Mode', str(self.high_score_alien_mode))

        self.player_data_manager.set('Statistics_Machine_Mode', 'Bosses_Killed', str(self.bosses_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Red_Bots_Killed', str(self.red_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Yellow_Bots_Killed', str(self.yellow_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Blue_Bots_Killed', str(self.blue_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Deaths', str(self.classic_deaths))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Damage_Taken', str(self.machine_damage_taken))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Lasers_Fired', str(self.classic_lasers_fired))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Power_Ups_Picked_Up', str(self.classic_power_ups_picked_up))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Coins_Collected', str(self.machine_coins_collected))

        self.player_data_manager.set('Statistics_Alien_Mode', 'Ufos_Killed', str(self.ufos_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Big_Aliens_Killed', str(self.big_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Medium_Aliens_Killed', str(self.medium_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Small_Aliens_Killed', str(self.small_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Deaths', str(self.alien_deaths))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Damage_Taken', str(self.damage_taken))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Lasers_Fired', str(self.alien_lasers_fired))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Jumps', str(self.jumps))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Power_Ups_Picked_Up', str(self.alien_power_ups_picked_up))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Coins_Collected', str(self.alien_coins_collected))

    def __repr__(self):
        return (f"Statistics("
                f"high_score_machine_war={self.high_score_machine_war}, "
                f"bosses_killed={self.bosses_killed}, "
                f"red_bots_killed={self.red_bots_killed}, "
                f"yellow_bots_killed={self.yellow_bots_killed}, "
                f"blue_bots_killed={self.blue_bots_killed}, "
                f"classic_deaths={self.classic_deaths}, "
                f"machine_damage_taken={self.machine_damage_taken}, "
                f"classic_lasers_fired={self.classic_lasers_fired}, "
                f"classic_power_ups_picked_up={self.classic_power_ups_picked_up}, "
                f"machine_coins_collected={self.machine_coins_collected}, "
                f"high_score_alien_mode={self.high_score_alien_mode}, "
                f"ufos_killed={self.ufos_killed}, "
                f"big_aliens_killed={self.big_aliens_killed}, "
                f"medium_aliens_killed={self.medium_aliens_killed}, "
                f"small_aliens_killed={self.small_aliens_killed}, "
                f"alien_deaths={self.alien_deaths}, "
                f"damage_taken={self.damage_taken}, "
                f"alien_lasers_fired={self.alien_lasers_fired}, "
                f"jumps={self.jumps}, "
                f"alien_power_ups_picked_up={self.alien_power_ups_picked_up}, "
                f"alien_coins_collected={self.alien_coins_collected})")
