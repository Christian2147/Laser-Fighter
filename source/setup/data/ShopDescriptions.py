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
    File: ShopDescriptions.py
    Author: Christian Marinkovich
    Date: 2024-07-13
    Description:
    This file contains the descriptions for each of the items in the shop.
    When an item in the shop is clicked on, these descriptions are loaded in.
    A .py file is used in this case because it is the quickest to access and the data does not need modifying.
"""

from components.gui.GUIDataDescription import Description

# Prices for each item in the shop
MACHINE_PRICES = [0, 5000, 15000, 40000, 100000]
ALIEN_PRICES = [0, 5000, 15000, 40000, 100000]
POWER_UP_PRICES = [1000, 5000, 15000, 30000]

# Shop Welcome Message
MAIN_DESCRIPTION = [
    Description("left", [
        "Welcome to",
        "the Shop!",
        "",
        "Here, you can",
        "upgrade your",
        "weapons,",
        "abilities",
        "and power ups",
        "to become even",
        "more powerful."
    ], 24, "Courier")
]

# For the Machine Player upgrades
MACHINE_DESCRIPTIONS = [
    Description("left", [
        "Default",
        "",
        "Laser Speed: 14.5",
        "Laser Color: Green",
        "Laser Size: L",
        "Lasers Per Round: 1",
        "Damage: 1",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "Machine Washer",
        "",
        "Laser Speed: 25",
        "Laser Color: Sky Blue",
        "Laser Size: XL",
        "Lasers Per Round: 1",
        "Damage: 1",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "The Incinerator",
        "",
        "Laser Speed: 20",
        "Laser Color: Orange",
        "Laser Size: XL",
        "Lasers Per Round: 2",
        "Damage: 1",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "The Black Hole",
        "",
        "Laser Speed: 28",
        "Laser Color: Purple",
        "Laser Size: XXL",
        "Lasers Per Round: 3",
        "Damage: 2",
        "Special Abilities:",
        "Double Score"
    ], 16, "Courier"),
    Description("left", [
        "The Star Killer",
        "",
        "Laser Speed: 30",
        "Laser Color: Multicolor",
        "Laser Size: XXL",
        "Lasers Per Round: 3",
        "Damage: 2",
        "Special Abilities:",
        "Double Score",
        "Power Up Spawns Incr."
    ], 16, "Courier")
]

# For the alien gun upgrades
ALIEN_DESCRIPTIONS = [
    Description("left", [
        "Default",
        "",
        "Laser Speed: 13",
        "Laser Color: Red",
        "Laser Size: L",
        "Lasers Per Round: 1",
        "Damage: 1",
        "Piercing: 2",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "The Cooker",
        "",
        "Laser Speed: 15",
        "Laser Color: Orange",
        "Laser Size: M",
        "Lasers Per Round: 1",
        "Damage: 1",
        "Piercing: 3",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "Poison Dart Gun",
        "",
        "Laser Speed: 25",
        "Laser Color: Green",
        "Laser Size: L",
        "Lasers Per Round: 2",
        "Damage: 2",
        "Piercing: 2",
        "Special Abilities:",
        "None"
    ], 16, "Courier"),
    Description("left", [
        "Meteor Gun",
        "",
        "Laser Speed: 24",
        "Laser Color: Multicolor",
        "Laser Size: XL",
        "Lasers Per Round: 1",
        "Damage: 3",
        "Piercing: 3",
        "Special Abilities:",
        "Double Score"
    ], 16, "Courier"),
    Description("left", [
        "The Supernova",
        "",
        "Laser Speed: 30",
        "Laser Color: Multicolor",
        "Laser Size: XL",
        "Lasers Per Round: 2",
        "Damage: 3",
        "Piercing: 4",
        "Special Abilities:",
        "Double Score",
        "Faster Movement",
        "Power Up Spawns Incr."
    ], 16, "Courier")
]

# For the yellow power up upgrades
YELLOW_POWER_UP_DESCRIPTIONS = [
    Description("left", [
        "Level 2",
        "",
        "Speed Increase: 3x",
        "Duration: 20",
        "Special:",
        "None"
    ], 20, "Courier"),
    Description("left", [
        "Level 3",
        "",
        "Speed Increase: 3x",
        "Duration: 30",
        "Special:",
        "None"
    ], 20, "Courier"),
    Description("left", [
        "Level 4",
        "",
        "Speed Increase: 4x",
        "Duration: 45",
        "Special:",
        "None"
    ], 20, "Courier"),
    Description("left", [
        "Level 5",
        "",
        "Speed Increase: 4x",
        "Duration: 60",
        "Special:",
        "Player movement 1.5x"
    ], 20, "Courier"),
    Description("left", [
        "Max Level Reached!"
    ], 20, "Courier")
]

# For the blue power up upgrades
BLUE_POWER_UP_DESCRIPTIONS = [
    Description("left", [
        "Level 2",
        "",
        "Multiplier: 3",
        "Coin Multiplier: 1",
        "Duration: 45"
    ], 20, "Courier"),
    Description("left", [
        "Level 3",
        "",
        "Multiplier: 3",
        "Coin Multiplier: 2",
        "Duration: 60"
    ], 20, "Courier"),
    Description("left", [
        "Level 4",
        "",
        "Multiplier: 4",
        "Coin Multiplier: 2",
        "Duration: 75"
    ], 20, "Courier"),
    Description("left", [
        "Level 5",
        "",
        "Multiplier: 5",
        "Coin Multiplier: 3",
        "Duration: 90"
    ], 20, "Courier"),
    Description("left", [
        "Max Level Reached!"
    ], 20, "Courier")
]

# For the green power up upgrades
GREEN_POWER_UP_DESCRIPTIONS = [
    Description("left", [
        "Level 2",
        "",
        "Duration: 20"
    ], 20, "Courier"),
    Description("left", [
        "Level 3",
        "",
        "Duration: 25"
    ], 20, "Courier"),
    Description("left", [
        "Level 4",
        "",
        "Duration: 30"
    ], 20, "Courier"),
    Description("left", [
        "Level 5",
        "",
        "Duration: 40"
    ], 20, "Courier"),
    Description("left", [
        "Max Level Reached!"
    ], 20, "Courier")
]

# For the red power up upgrades
RED_POWER_UP_DESCRIPTIONS = [
    Description("left", [
        "Level 2",
        "",
        "Duration: 20"
    ], 20, "Courier"),
    Description("left", [
        "Level 3",
        "",
        "Duration: 25"
    ], 20, "Courier"),
    Description("left", [
        "Level 4",
        "",
        "Duration: 30"
    ], 20, "Courier"),
    Description("left", [
        "Level 5",
        "",
        "Duration: 40"
    ], 20, "Courier"),
    Description("left", [
        "Max Level Reached!"
    ], 20, "Courier")
]
