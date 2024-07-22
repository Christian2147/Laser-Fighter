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


class Settings:
    def __init__(self):
        self.config_file = 'Config/config.ini'
        self.config = configparser.ConfigParser()

        self.god_mode = 0
        self.button_sound = 0
        self.player_shooting_sound = 0
        self.enemy_shooting_sound = 0
        self.player_death_sound = 0
        self.enemy_death_sound = 0
        self.player_hit_sound = 0
        self.enemy_hit_sound = 0
        self.power_up_pickup_sound = 0
        self.power_up_spawn_sound = 0
        self.coin_pickup_sound = 0
        self.fullscreen = 0
        self.vsync = 0

        self.load()

    def load(self):
        self.config.read(self.config_file)

        try:
            self.god_mode = self.config['Settings'].getint('God_Mode')
            self.button_sound = self.config['Settings'].getint('Button_Sound')
            self.player_shooting_sound = self.config['Settings'].getint('Player_Shooting_Sound')
            self.enemy_shooting_sound = self.config['Settings'].getint('Enemy_Shooting_Sound')
            self.player_death_sound = self.config['Settings'].getint('Player_Death_Sound')
            self.enemy_death_sound = self.config['Settings'].getint('Enemy_Death_Sound')
            self.player_hit_sound = self.config['Settings'].getint('Player_Hit_Sound')
            self.enemy_hit_sound = self.config['Settings'].getint('Enemy_Hit_Sound')
            self.power_up_pickup_sound = self.config['Settings'].getint('Power_up_Pickup_Sound')
            self.power_up_spawn_sound = self.config['Settings'].getint('Power_up_Spawn_Sound')
            self.coin_pickup_sound = self.config['Settings'].getint('Coin_Pick_Up_Sound')
            self.fullscreen = self.config['Settings'].getint('Fullscreen')
            self.vsync = self.config['Settings'].getint('VSync')
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)

    def save(self):
        self.config['Settings']['God_Mode'] = str(self.god_mode)
        self.config['Settings']['Button_Sound'] = str(self.button_sound)
        self.config['Settings']['Player_Shooting_Sound'] = str(self.player_shooting_sound)
        self.config['Settings']['Enemy_Shooting_Sound'] = str(self.enemy_shooting_sound)
        self.config['Settings']['Player_Death_Sound'] = str(self.player_death_sound)
        self.config['Settings']['Enemy_Death_Sound'] = str(self.enemy_death_sound)
        self.config['Settings']['Player_Hit_Sound'] = str(self.player_hit_sound)
        self.config['Settings']['Enemy_Hit_Sound'] = str(self.enemy_hit_sound)
        self.config['Settings']['Power_up_Pickup_Sound'] = str(self.power_up_pickup_sound)
        self.config['Settings']['Power_up_Spawn_Sound'] = str(self.power_up_spawn_sound)
        self.config['Settings']['Coin_Pick_Up_Sound'] = str(self.coin_pickup_sound)
        self.config['Settings']['VSync'] = str(self.vsync)

        try:
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        except IOError as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error saving config file: {e}", "Error", 0x10)

    def toggle_fullscreen(self):
        current_fullscreen = self.config['Settings'].getint('Fullscreen')

        if current_fullscreen == 1:
            self.config['Settings']['Fullscreen'] = str(0)
        else:
            self.config['Settings']['Fullscreen'] = str(1)

        try:
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        except IOError as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error saving config file: {e}", "Error", 0x10)

    def __repr__(self):
        return (f"GameSettings(god_mode={self.god_mode}, button_sound={self.button_sound}, "
                f"player_shooting_sound={self.player_shooting_sound}, enemy_shooting_sound={self.enemy_shooting_sound}, "
                f"player_death_sound={self.player_death_sound}, enemy_death_sound={self.enemy_death_sound}, "
                f"player_hit_sound={self.player_hit_sound}, enemy_hit_sound={self.enemy_hit_sound}, "
                f"power_up_pickup_sound={self.power_up_pickup_sound}, power_up_spawn_sound={self.power_up_spawn_sound}, "
                f"coin_pickup_sound={self.coin_pickup_sound}, fullscreen={self.fullscreen}, vsync={self.vsync})")
