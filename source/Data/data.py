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
    File: data.py
    Author: Christian Marinkovich
    Date: 2024-07-07
    Description:
    This file contains all of the global variables needed for the game to run.
    This also includes any external variables stored in the ini files.
"""

import configparser
import subprocess
import os

# Current Screen Variable - Determines what screen is currently being displayed in the window
mode = "Title_Mode"
# Determines the subscreen
page = "Machine_Mode"

# Button text highlighting - Used to ensure button text highlighting stays consistent across screens
button_update = 0

# Current Score
score = 0

# Laser piercing in alien mode (Can only pierce through 2 enemies by default)
laser_update = 0

# Variables to spawn power-ups
# power_up_update - random variable which determines if a power up spawns
# power_up_time - used to ensure that the random variable is
#   only being updated a specific number of times over an interval of time
power_up_update = 0
power_up_time = 0

"""
Sprite variables and how they work:
- "all" lists - permanently stores the turtles created throughout the entire lifetime of the application so that they
    can be referenced and used again
    - If for a type of sprite there is only one list, it is an "all" list (Like the power up indicators for example)
- "current" lists - stores the turtles as long as they are visible on the screen or being actively used
- "index" variables - used to access a specific slot in these lists
"""

# Power Up Data
all_power_ups = []
current_power_ups = []
power_up_index = [0, 0, 0, 0]

# Yellow Power Up Indicator Data
yellow_power_up_indicator_turtle = []
yellow_power_up_indicator_index = 0

# Blue Power Up Indicator Data
blue_power_up_indicator_turtle = []
blue_power_up_indicator_index = 0

# Red/Green Power Up Indicator Data
extra_power_up_indicator_turtle = []
extra_power_up_indicator_index = 0

# Refreshing when VSync is off
tick_update = 0

# Used for when certain data needs to be transferred across screens or updated only on certain screens
screen_update = 0
clickable = 0

# Button Data
all_button_list = []
buttons_on_screen_list = []
current_button_index = 0

# Panel Data
panel_turtle = []
panel_index = 0

# Which item is being displayed
displayed = 0

# Text Box Data
all_text_list = []
text_on_screen_list = []
current_text_index = 0

# Price Label data
all_price_label = []
price_label_on_screen_list = []
current_price_index = 0

# Coin Data
all_coins_list = []
all_coins_index = 0
coins_on_screen_list = []
current_coin_index = 0
coin_pickup_delay = 0

# Coin Indicator Data
coin_indicator_turtle = []
coin_indicator_index = 0

# Machine Player Data
all_player = []
current_player = []
current_player_index = 0
player_hit_value = 0
player_update_value = 0

# Blue Machine Data
all_blue_machines = []
blue_machines = []
blue_machines_update_values = []
blue_machine_index = 0

# Yellow Machine Data
all_yellow_machines = []
yellow_machines = []
yellow_machines_update_values = []
yellow_machine_index = 0

# Red Machine Data
all_red_machines = []
red_machines = []
red_machines_update_values = []
red_machines_hit_values = []
red_machine_index = 0

# Boss Data
all_boss = []
boss = []
boss_update_value = 0
boss_hit_value = 0
boss_index = 0

# Earth Object Data
earth_turtle = []
earth_index = 0

# Sun Object Data
sun_turtle = []
sun_index = 0

# Background Object Data
background_objects = []
background_objects_index = 0

# Human Data
all_human = []
current_human = []
current_human_index = 0
human_hit_value = 0
human_update_value = 0

# Small Alien Data
all_small_aliens = []
small_aliens = []
small_aliens_kill_values = []
small_alien_index = 0

# Medium Alien Data
all_medium_aliens = []
medium_aliens = []
medium_aliens_kill_values = []
medium_aliens_hit_values = []
medium_alien_index = 0

# Large Alien Data
all_large_aliens = []
large_aliens = []
large_aliens_kill_values = []
large_aliens_hit_values = []
large_alien_index = 0

# UFO Data
all_ufos = []
ufos = []
ufo_kill_value = 0
ufo_hit_value = 0
ufo_index = 0

# Walking Animation in Alien Mode
right_update = 0
left_update = 0

# Restart Variables (Having these set to 1 means the game needs to restart to update controls
updated_controls = 0
fullscreen_toggled = 0

# Key Binding Conflicts
go_right_key_alert = 0
go_left_key_alert = 0
shoot_key_alert = 0
jump_key_alert = 0

# Message Box Data
message_output = 0

# Close Window Data
quit_loop = 0

# Extract the amount of coins the user has from the playerData ini file
config = configparser.ConfigParser()
config.read('config/playerData.ini')
total_coins = config['Coins'].getint('Coins')

# Extract the users statistics from the playerData ini file
config = configparser.ConfigParser()
config.read('config/playerData.ini')
bosses_killed = config['Statistics_Machine_Mode'].getint('Bosses_Killed')
red_bots_killed = config['Statistics_Machine_Mode'].getint('Red_Bots_Killed')
yellow_bots_killed = config['Statistics_Machine_Mode'].getint('Yellow_Bots_Killed')
blue_bots_killed = config['Statistics_Machine_Mode'].getint('Blue_Bots_Killed')
classic_deaths = config['Statistics_Machine_Mode'].getint('Deaths')
machine_damage_taken = config['Statistics_Machine_Mode'].getint('Damage_Taken')
classic_lasers_fired = config['Statistics_Machine_Mode'].getint('Lasers_Fired')
classic_power_ups_picked_up = config['Statistics_Machine_Mode'].getint('Power_Ups_Picked_Up')
machine_coins_collected = config['Statistics_Machine_Mode'].getint('Coins_Collected')
ufos_killed = config['Statistics_Alien_Mode'].getint('Ufos_Killed')
big_aliens_killed = config['Statistics_Alien_Mode'].getint('Big_Aliens_Killed')
medium_aliens_killed = config['Statistics_Alien_Mode'].getint('Medium_Aliens_Killed')
small_aliens_killed = config['Statistics_Alien_Mode'].getint('Small_Aliens_Killed')
alien_deaths = config['Statistics_Alien_Mode'].getint('Deaths')
damage_taken = config['Statistics_Alien_Mode'].getint('Damage_Taken')
alien_lasers_fired = config['Statistics_Alien_Mode'].getint('Lasers_Fired')
jumps = config['Statistics_Alien_Mode'].getint('Jumps')
alien_power_ups_picked_up = config['Statistics_Alien_Mode'].getint('Power_Ups_Picked_Up')
alien_coins_collected = config['Statistics_Alien_Mode'].getint('Coins_Collected')

# Extract the users controls from the config ini file
config = configparser.ConfigParser()
config.read('Config/config.ini')
right_control = config['Controls'].get('Go_Right')
left_control = config['Controls'].get('Go_Left')
shoot_control = config['Controls'].get('Shoot')
jump_control = config['Controls'].get('Jump')
config_checker = configparser.ConfigParser()
config_checker.read('Config/keyUpdate.ini')
if config_checker['Key_Update'].get('Key_1') == 'space':
    go_right_key = "space"
else:
    go_right_key = right_control
if config_checker['Key_Update'].get('Key_2') == 'space':
    go_left_key = "space"
else:
    go_left_key = left_control
if config_checker['Key_Update'].get('Key_3') == 'space':
    shoot_key = "space"
else:
    shoot_key = shoot_control
if config_checker['Key_Update'].get('Key_4') == 'space':
    jump_key = "space"
else:
    jump_key = jump_control

# Extract the users settings from the config ini file
config = configparser.ConfigParser()
config.read('Config/config.ini')
if config['Settings'].getint('God_Mode') == 1:
    god_mode = 1
else:
    god_mode = 0
if config['Settings'].getint('Button_Sound') == 1:
    button_sound = 1
else:
    button_sound = 0
if config['Settings'].getint('Player_Shooting_Sound') == 1:
    player_shooting_sound = 1
else:
    player_shooting_sound = 0
if config['Settings'].getint('Enemy_Shooting_Sound') == 1:
    enemy_shooting_sound = 1
else:
    enemy_shooting_sound = 0
if config['Settings'].getint('Player_Death_Sound') == 1:
    player_death_sound = 1
else:
    player_death_sound = 0
if config['Settings'].getint('Enemy_Death_Sound') == 1:
    enemy_death_sound = 1
else:
    enemy_death_sound = 0
if config['Settings'].getint('Player_Hit_Sound') == 1:
    player_hit_sound = 1
else:
    player_hit_sound = 0
if config['Settings'].getint('Enemy_Hit_Sound') == 1:
    enemy_hit_sound = 1
else:
    enemy_hit_sound = 0
if config['Settings'].getint('Power_up_Pickup_Sound') == 1:
    power_up_pickup_sound = 1
else:
    power_up_pickup_sound = 0
if config['Settings'].getint('Power_up_Spawn_Sound') == 1:
    power_up_spawn_sound = 1
else:
    power_up_spawn_sound = 0
if config['Settings'].getint('Coin_Pick_Up_Sound') == 1:
    coin_pickup_sound = 1
else:
    coin_pickup_sound = 0
if config['Settings'].getint('Fullscreen') == 1:
    fullscreen = 1
else:
    fullscreen = 0
if config['Settings'].getint('VSync') == 1:
    vsync = 1
else:
    vsync = 0

# Extract the users high score from the playerData ini file
if god_mode == 0:
    config = configparser.ConfigParser()
    config.read('Config/playerData.ini')
    high_score_machine_war = config['High_Score'].getint('High_Score_Machine_War')
    high_score_alien_mode = config['High_Score'].getint('High_Score_Alien_Mode')
else:
    high_score_machine_war = "NA"
    high_score_alien_mode = "NA"

# Backup the player data and config files on launch through a batch file (Made so that the user can run the
#   script whenever they want
batch_file_path = './Config/bckp.bat'
target_directory = os.path.abspath('./Config')
absolute_batch_file_path = os.path.abspath(batch_file_path)
subprocess.run([absolute_batch_file_path], cwd=target_directory)
