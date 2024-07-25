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


class Stats:
    def __init__(self, god_mode):
        self.config_file = 'Config/playerData.ini'
        self.config = configparser.ConfigParser()

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
        del self.config_file

    def load(self):
        self.config.read(self.config_file)

        try:
            # Machine Mode Statistics
            if self.god_mode == 1:
                self.high_score_machine_war = "NA"
            else:
                self.high_score_machine_war = self.config['High_Score'].getint('High_Score_Machine_War')
            self.bosses_killed = self.config['Statistics_Machine_Mode'].getint('Bosses_Killed')
            self.red_bots_killed = self.config['Statistics_Machine_Mode'].getint('Red_Bots_Killed')
            self.yellow_bots_killed = self.config['Statistics_Machine_Mode'].getint('Yellow_Bots_Killed')
            self.blue_bots_killed = self.config['Statistics_Machine_Mode'].getint('Blue_Bots_Killed')
            self.classic_deaths = self.config['Statistics_Machine_Mode'].getint('Deaths')
            self.machine_damage_taken = self.config['Statistics_Machine_Mode'].getint('Damage_Taken')
            self.classic_lasers_fired = self.config['Statistics_Machine_Mode'].getint('Lasers_Fired')
            self.classic_power_ups_picked_up = self.config['Statistics_Machine_Mode'].getint('Power_Ups_Picked_Up')
            self.machine_coins_collected = self.config['Statistics_Machine_Mode'].getint('Coins_Collected')

            # Alien Mode Statistics
            if self.god_mode == 1:
                self.high_score_alien_mode = "NA"
            else:
                self.high_score_alien_mode = self.config['High_Score'].getint('High_Score_Alien_Mode')
            self.ufos_killed = self.config['Statistics_Alien_Mode'].getint('Ufos_Killed')
            self.big_aliens_killed = self.config['Statistics_Alien_Mode'].getint('Big_Aliens_Killed')
            self.medium_aliens_killed = self.config['Statistics_Alien_Mode'].getint('Medium_Aliens_Killed')
            self.small_aliens_killed = self.config['Statistics_Alien_Mode'].getint('Small_Aliens_Killed')
            self.alien_deaths = self.config['Statistics_Alien_Mode'].getint('Deaths')
            self.damage_taken = self.config['Statistics_Alien_Mode'].getint('Damage_Taken')
            self.alien_lasers_fired = self.config['Statistics_Alien_Mode'].getint('Lasers_Fired')
            self.jumps = self.config['Statistics_Alien_Mode'].getint('Jumps')
            self.alien_power_ups_picked_up = self.config['Statistics_Alien_Mode'].getint('Power_Ups_Picked_Up')
            self.alien_coins_collected = self.config['Statistics_Alien_Mode'].getint('Coins_Collected')
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)

    def save(self):
        try:
            if self.god_mode != 1:
                self.config['High_Score']['High_Score_Machine_War'] = str(self.high_score_machine_war)
                self.config['High_Score']['High_Score_Alien_Mode'] = str(self.high_score_alien_mode)

            self.config['Statistics_Machine_Mode'] = {
                'Bosses_Killed': str(self.bosses_killed),
                'Red_Bots_Killed': str(self.red_bots_killed),
                'Yellow_Bots_Killed': str(self.yellow_bots_killed),
                'Blue_Bots_Killed': str(self.blue_bots_killed),
                'Deaths': str(self.classic_deaths),
                'Damage_Taken': str(self.machine_damage_taken),
                'Lasers_Fired': str(self.classic_lasers_fired),
                'Power_Ups_Picked_Up': str(self.classic_power_ups_picked_up),
                'Coins_Collected': str(self.machine_coins_collected)
            }

            self.config['Statistics_Alien_Mode'] = {
                'Ufos_Killed': str(self.ufos_killed),
                'Big_Aliens_Killed': str(self.big_aliens_killed),
                'Medium_Aliens_Killed': str(self.medium_aliens_killed),
                'Small_Aliens_Killed': str(self.small_aliens_killed),
                'Deaths': str(self.alien_deaths),
                'Damage_Taken': str(self.damage_taken),
                'Lasers_Fired': str(self.alien_lasers_fired),
                'Jumps': str(self.jumps),
                'Power_Ups_Picked_Up': str(self.alien_power_ups_picked_up),
                'Coins_Collected': str(self.alien_coins_collected)
            }

            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error saving config file: {e}", "Error", 0x10)

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
