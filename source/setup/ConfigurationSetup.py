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
    Date: 2024-08-01
    Description:
    This file initializes the containers for the current configuration settings and user progress in Laser Fighter.
"""

import subprocess
import os
from utils.Refresh import Refresh
from utils.UpdateSettingsData import Settings
from utils.UpdateControls import ControlsConfig
from utils.UpdateStatsData import Stats
from utils.UpdateShopData import ShopConfig

# Initialize the refresh variables
refresh_variables = Refresh()

# Create Settings Object to store the settings variables
settings = Settings()

# Create Controls Toggle Object to store the control keybinds
controls_toggle = ControlsConfig()

# Create a Stats Object to store the current statistics
statistics = Stats(settings.god_mode)

# Current Shop Configuration
shop_config = ShopConfig()

# Backup the player data and config files on launch through a batch file (Made so that the user can run the
#   script whenever they want
batch_file_path = './config/bckp.bat'
target_directory = os.path.abspath('./config')
absolute_batch_file_path = os.path.abspath(batch_file_path)
subprocess.run([absolute_batch_file_path], cwd=target_directory)
