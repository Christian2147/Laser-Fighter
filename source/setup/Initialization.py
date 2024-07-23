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
    File: Initialization.py
    Author: Christian Marinkovich
    Date: 2024-07-23
    Description:
    This file contains all of the global variables needed for the game to run.
    This also includes any external variables stored in the ini files.
"""

import configparser
import subprocess
import os
from utils.Refresh import Refresh
from utils.UpdateSettingsData import Settings
from utils.UpdateStatsData import Stats
from utils.UpdateShopData import ShopConfig

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

# Refreshing when VSync is off
tick_update = 0

# Used for when certain data needs to be transferred across screens or updated only on certain screens
screen_update = 0
page_update = 0
clickable = 0
buy_button_pressed = 0

# Initialize the update variables
refresh_variables = Refresh()

# Which item is being displayed
price_displayed = 0

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

# Message Box setup
message_output = 0

# Close Window setup
quit_loop = 0

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

# Create Settings Object to store the settings variables
settings = Settings()

# Create a Stats PObject to store the statistics variables
statistics = Stats(settings.god_mode)

# Current Shop Configuration
shop_config = ShopConfig()

# Backup the player data and config files on launch through a batch file (Made so that the user can run the
#   script whenever they want
batch_file_path = './Config/bckp.bat'
target_directory = os.path.abspath('./Config')
absolute_batch_file_path = os.path.abspath(batch_file_path)
subprocess.run([absolute_batch_file_path], cwd=target_directory)
