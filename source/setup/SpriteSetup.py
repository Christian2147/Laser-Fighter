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
    File: SpriteSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    Loads in all of the different sprites and their containers.
"""

from setup.WindowSetup import scale_factor
from setup.WindowSetup import scale_factor_X
from setup.WindowSetup import scale_factor_Y
from components.spawn.SpawnButton import SpawnButton
from components.spawn.SpawnTextBox import SpawnTextbox
from components.spawn.SpawnGUI import SpawnPanel
from components.spawn.SpawnGUI import SpawnSelector
from components.spawn.SpawnGUI import SpawnPriceLabel
from components.spawn.SpawnBackgroundObjects import SpawnSun
from components.spawn.SpawnBackgroundObjects import SpawnEarth
from components.spawn.SpawnBackgroundObjects import SpawnBackgroundObjects
from components.spawn.SpawnPowerUp import SpawnPowerUp
from components.spawn.SpawnPowerUp import SpawnYellowPowerUpIndicator
from components.spawn.SpawnPowerUp import SpawnBluePowerUpIndicator
from components.spawn.SpawnPowerUp import SpawnExtraPowerUpIndicator
from components.spawn.SpawnCoin import SpawnCoin
from components.spawn.SpawnCoin import SpawnCoinIndicator
from components.spawn.SpawnPlayer import SpawnMachinePlayer
from components.spawn.SpawnPlayer import SpawnHumanPlayer
from components.spawn.SpawnMachine import SpawnBlueMachine
from components.spawn.SpawnMachine import SpawnYellowMachine
from components.spawn.SpawnMachine import SpawnRedMachine
from components.spawn.SpawnMachine import SpawnMachineBoss
from components.spawn.SpawnAlien import SpawnSmallAlien
from components.spawn.SpawnAlien import SpawnMediumAlien
from components.spawn.SpawnAlien import SpawnLargeAlien
from components.spawn.SpawnAlien import SpawnUFO


# Stores Button Objects
button = SpawnButton(scale_factor, scale_factor_X, scale_factor_Y)

# Stores Textboxes
textbox = SpawnTextbox(scale_factor, scale_factor_X)

# Stores the Side Panel
panel = SpawnPanel(scale_factor, scale_factor_X, scale_factor_Y)

# Stores Selectors
selector = SpawnSelector(scale_factor_X, scale_factor_Y)

# Stores the Price label
price_label = SpawnPriceLabel()

# Stores the Sun
sun = SpawnSun(scale_factor_X, scale_factor_Y)

# Stores the Earth
earth = SpawnEarth(scale_factor_X, scale_factor_Y)

# Stores the Background Objects
background_objects = SpawnBackgroundObjects(scale_factor_X, scale_factor_Y)

# Stores the Power Ups
power_up = SpawnPowerUp(scale_factor_X, scale_factor_Y)

# Stores the Yellow Power Up Indicator
yellow_power_up_indicator = SpawnYellowPowerUpIndicator(scale_factor_X, scale_factor_Y)

# Stores the Blue Power Up Indicator
blue_power_up_indicator = SpawnBluePowerUpIndicator(scale_factor_X, scale_factor_Y)

# Stores the Third Power Up Indicator
extra_power_up_indicator = SpawnExtraPowerUpIndicator(scale_factor_X, scale_factor_Y)

# Stores the Coins
coin = SpawnCoin()

# Stores the Coin Indicator
coin_indicator = SpawnCoinIndicator(scale_factor_X, scale_factor_Y)

# Stores the Machine Player
machine_player = SpawnMachinePlayer(scale_factor_X, scale_factor_Y)

# Stores the Human Player
human_player = SpawnHumanPlayer(scale_factor_X, scale_factor_Y)

# Stores the Blue Machines
blue_machine = SpawnBlueMachine(scale_factor_X, scale_factor_Y)

# Stores the Yellow Machines
yellow_machine = SpawnYellowMachine(scale_factor_X, scale_factor_Y)

# Stores the Red Machines
red_machine = SpawnRedMachine(scale_factor_X, scale_factor_Y)

# Stores the Machine Boss
machine_boss = SpawnMachineBoss(scale_factor_X, scale_factor_Y)

# Stores the Small Aliens
small_alien = SpawnSmallAlien(scale_factor_X, scale_factor_Y)

# Stores the Medium Aliens
medium_alien = SpawnMediumAlien(scale_factor_X, scale_factor_Y)

# Stores the Large Aliens
large_alien = SpawnLargeAlien(scale_factor_X, scale_factor_Y)

# Stores the UFO
ufo = SpawnUFO(scale_factor_X, scale_factor_Y)
