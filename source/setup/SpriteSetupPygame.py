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

from setup.WindowSetupPygame import scale_factor_X
from setup.WindowSetupPygame import scale_factor_Y
from components.spawn.SpawnMachinePygame import SpawnBlueMachine

blue_machine = SpawnBlueMachine(scale_factor_X, scale_factor_Y)
