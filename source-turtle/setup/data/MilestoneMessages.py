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

from components.gui.GUIDataDescription import Description

# When the player enters Machine Mode for the first time
MILESTONE_1_MESSAGE = [
    Description("center", [
        "Welcome To Laser Fighter",
        "",
        "You have just left Earth",
        "after the region got taken",
        "over by mysterious aliens. You",
        "know that the aliens central",
        "base is located on the",
        "moon. Your goal is to",
        "make it there, destroy their",
        "base, and make it back",
        "all in one piece!"
    ], 16, "Courier"),
]

# When the player beats the machine boss for the first time
MILESTONE_2_MESSAGE = [
    Description("center", [
        "Congratulations!",
        "",
        "You have successfully entered",
        "the moons orbit! Now, you",
        "must find a safe place",
        "to land so that you",
        "can begin your operation.",
        "Careful! There seems to be",
        "a lot of aliens on",
        "the moon.",
    ], 16, "Courier"),
]

# When the player enters Alien Mode for the first time
MILESTONE_3_MESSAGE = [
    Description("center", [
        "Congratulations!",
        "",
        "You have successfully made it",
        "to the moon! Now, you",
        "must find a way to",
        "the aliens central base. It",
        "is said that the saucers",
        "the aliens use not only",
        "carry a map to the base,",
        "but also carry a key",
        "to get inside."
    ], 16, "Courier"),
]

# When the player beats the boss in Alien Mode for the first time
MILESTONE_4_MESSAGE = [
    Description("center", [
        "Congratulations!",
        "",
        "You have successfully killed an",
        "alien saucer and therefore found",
        "a map and a key",
        "to the base. Your next",
        "goal is to get inside",
        "and destroy their operation!"
    ], 16, "Courier"),
]
