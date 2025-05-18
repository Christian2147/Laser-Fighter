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
    File: MachinePlayerLaser.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for the machine player's laser sprite in Machine Mode.
    For some machine players, multiple laser sprites are needed.
"""

import pygame
from setup.ModeSetupMasterPygame import machine_mode_setup


class MachineLaser(pygame.sprite.Sprite):
    """
        Represents the players laser in Machine Mode.

        Attributes:
            _laser (turtle.Turtle()): The machine players laser sprite
    """

    def __init__(self, x, y):
        """
            Creates a player laser object.

            :param x: The x-coordinate of the laser
            :type x: float

            :param y: The y-coordinate of the laser
            :type y: float
        """

        super().__init__()
        self.image = pygame.image.load(machine_mode_setup.laser_texture)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.laser_visible = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        self.kill()

    @property
    def laser(self):
        """Machine Player Laser Getter"""
        return self

    def remove(self):
        """
            Removes the players laser from the screen.

            :return: None
        """

        self.laser_visible = 0
