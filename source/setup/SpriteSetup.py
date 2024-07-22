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

from setup.ScreenSetup import scale_factor
from setup.ScreenSetup import scale_factor_X
from setup.ScreenSetup import scale_factor_Y
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


button = SpawnButton(scale_factor, scale_factor_X, scale_factor_Y)

textbox = SpawnTextbox(scale_factor, scale_factor_X)

panel = SpawnPanel(scale_factor, scale_factor_X, scale_factor_Y)

selector = SpawnSelector(scale_factor_X, scale_factor_Y)

price_label = SpawnPriceLabel()

sun = SpawnSun(scale_factor_X, scale_factor_Y)

earth = SpawnEarth(scale_factor_X, scale_factor_Y)

background_objects = SpawnBackgroundObjects(scale_factor_X, scale_factor_Y)

power_up = SpawnPowerUp(scale_factor_X, scale_factor_Y)

yellow_power_up_indicator = SpawnYellowPowerUpIndicator(scale_factor_X, scale_factor_Y)

blue_power_up_indicator = SpawnBluePowerUpIndicator(scale_factor_X, scale_factor_Y)

extra_power_up_indicator = SpawnExtraPowerUpIndicator(scale_factor_X, scale_factor_Y)

coin_indicator = SpawnCoinIndicator(scale_factor_X, scale_factor_Y)

machine_player = SpawnMachinePlayer(scale_factor_X, scale_factor_Y)

human_player = SpawnHumanPlayer(scale_factor_X, scale_factor_Y)

blue_machine = SpawnBlueMachine(scale_factor_X, scale_factor_Y)

yellow_machine = SpawnYellowMachine(scale_factor_X, scale_factor_Y)

red_machine = SpawnRedMachine(scale_factor_X, scale_factor_Y)

machine_boss = SpawnMachineBoss(scale_factor_X, scale_factor_Y)

small_alien = SpawnSmallAlien(scale_factor_X, scale_factor_Y)

medium_alien = SpawnMediumAlien(scale_factor_X, scale_factor_Y)

large_alien = SpawnLargeAlien(scale_factor_X, scale_factor_Y)

ufo = SpawnUFO(scale_factor_X, scale_factor_Y)

