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
    File: shop.py
    Author: Christian Marinkovich
    Date: 2024-07-13
    Description:
    This file contains the descriptions for each of the items in the shop.
    When an item in the shop is clicked on, these descriptions are loaded in.
    A .py file is used in this case because it is the quickest to access and the data does not need modifying.
"""

from Class.descriptions import Description

# Shop Welcome Message
main_description = [
    Description("right", "Welcome to\n the Shop!\n\nHere, you can\nupgrade your\nweapons,\nabilities,\nand power-ups\nto become even\nmore powerful.", 24, "Courier")
]

# For the Machine Player upgrades
machine_descriptions = [
    Description("right", "Default\n\nLaser Speed: 14.5\nLaser Color: Green\nLaser Size: L\nLasers Per Round: 1\nDamage: 1\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "Machine Washer\n\nLaser Speed: 25\nLaser Color: Sky Blue\nLaser Size: XL\nLasers Per Round: 1\nDamage: 1\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "The Incinerater\n\nLaser Speed: 20\nLaser Color: Orange\nLaser Size: XL\nLasers Per Round: 2\nDamage: 1\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "The Black Hole\n\nLaser Speed: 28\nLaser Color: Purple\nLaser Size: XXL\nLasers Per Round: 3\nDamage: 2\nSpecial Abilities:\nDouble Score", 16, "Courier"),
    Description("right", "The Star Killer\n\nLaser Speed: 30\nLaser Color: Multicolor\nLaser Size: XXL\nLasers Per Round: 3\nDamage: 2\nSpecial Abilities:\nDouble Score\nPower Up Spawns Incr.", 16, "Courier")
]

# For the alien gun upgrades
alien_descriptions = [
    Description("right", "Default\n\nLaser Speed: 13\nLaser Color: Red\nLaser Size: L\nLasers Per Round: 1\nDamage: 1\nPiercing: 2\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "The Cooker\n\nLaser Speed: 15\nLaser Color: Orange\nLaser Size: M\nLasers Per Round: 1\nDamage: 1\nPiercing: 3\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "Poison Dart Gun\n\nLaser Speed: 25\nLaser Color: Green\nLaser Size: L\nLasers Per Round: 2\nDamage: 2\nPiercing: 2\nSpecial Abilities:\nNone", 16, "Courier"),
    Description("right", "Meteor Gun\n\nLaser Speed: 24\nLaser Color: Multicolor\nLaser Size: XL\nLasers Per Round: 1\nDamage: 3\nPiercing: 3\nSpecial Abilities:\nDouble Score", 16, "Courier"),
    Description("right", "The Supernova\n\nLaser Speed: 30\nLaser Color: Multicolor\nLaser Size: XL\nLasers Per Round: 2\nDamage: 3\nPiercing: 4\nSpecial Abilities:\nDouble Score\nFaster Movement\nPower Up Spawns Incr.", 16, "Courier")
]

# For the yellow power up upgrades
yellow_power_up_descriptions = [
    Description("right", "Level 2\n\nSpeed Increase: 3x\nDuration: 20\nSpecial:\nNone", 16, "Courier"),
    Description("right", "Level 3\n\nSpeed Increase: 3x\nDuration: 30\nSpecial:\nNone", 16, "Courier"),
    Description("right", "Level 4\n\nSpeed Increase: 4x\nDuration: 45\nSpecial:\nNone", 16, "Courier"),
    Description("right", "Level 5\n\nSpeed Increase: 4x\nDuration: 60\nSpecial:\nPlayer movement 1.5x", 16, "Courier"),
    Description("right", "Max Level Reached!", 16, "Courier")
]

# For the blue power up upgrades
blue_power_up_descriptions = [
    Description("right", "Level 2\n\nMultiplier: 3\nCoin Multiplier: 1\nDuration: 45", 16, "Courier"),
    Description("right", "Level 3\n\nMultiplier: 3\nCoin Multiplier: 2\nDuration: 60", 16, "Courier"),
    Description("right", "Level 4\n\nMultiplier: 4\nCoin Multiplier: 2\nDuration: 75", 16, "Courier"),
    Description("right", "Level 5\n\nMultiplier: 5\nCoin Multiplier: 3\nDuration: 90", 16, "Courier"),
    Description("right", "Max Level Reached!", 16, "Courier")
]

# For the green power up upgrades
green_power_up_descriptions = [
    Description("right", "Level 2\n\nDuration: 20", 16, "Courier"),
    Description("right", "Level 3\n\nDuration: 25", 16, "Courier"),
    Description("right", "Level 4\n\nDuration: 30", 16, "Courier"),
    Description("right", "Level 5\n\nDuration: 40", 16, "Courier"),
    Description("right", "Max Level Reached!", 16, "Courier")
]

# For the red power up upgrades
red_power_up_descriptions = [
    Description("right", "Level 2\n\nDuration: 20", 16, "Courier"),
    Description("right", "Level 3\n\nDuration: 25", 16, "Courier"),
    Description("right", "Level 4\n\nDuration: 30", 16, "Courier"),
    Description("right", "Level 5\n\nDuration: 40", 16, "Courier"),
    Description("right", "Max Level Reached!", 16, "Courier")
]
