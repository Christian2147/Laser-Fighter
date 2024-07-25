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
    File: ConfigurationSetup.py
    Author: Christian Marinkovich
    Date: 2024-07-23
    Description:
    This file contains all of the global variables needed for the game to run.
    This also includes any external variables stored in the ini files.
"""

import subprocess
import os
from utils.Refresh import Refresh
from utils.UpdateSettingsData import Settings
from utils.UpdateControls import ControlsConfig
from utils.UpdateStatsData import Stats
from utils.UpdateShopData import ShopConfig

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

# Initialize the update variables
refresh_variables = Refresh()

# Walking Animation in Alien Mode
right_update = 0
left_update = 0

# Create Settings Object to store the settings variables
settings = Settings()

# Create Controls Object to store the control keybinds
controls_toggle = ControlsConfig()

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
