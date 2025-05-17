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
    File: HumanLaser.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for the human player's laser sprite in Alien Mode.
    For some guns, multiple laser sprites are needed.
"""

import turtle
from setup.ModeSetupMaster import alien_mode_setup


class HumanLaser:
    """
        Represents the player's laser in Alien Mode.

        Attributes:
            _laser (turtle.Turtle()): The player laser sprite
            laser_update (int): Determines the lasers current pierce value

            scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            scale_factor_y: The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, x, y, scale_factor_x, scale_factor_y):
        """
            Creates a Human Laser sprite on the screen.

            :param x: The x-coordinate of the laser
            :type x: float

            :param y: The y-coordinate of the laser
            :type y: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self._laser = turtle.Turtle()
        self.laser.shape(alien_mode_setup.laser_right_texture)
        self.laser.shapesize(0.33 * scale_factor_y, 2 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.laser.penup()
        self.laser.goto(x, y)

        self.laser_update = 20

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        self.laser.clear()
        del self._laser
        del self.laser_update
        del self.scale_factor_x
        del self.scale_factor_y

    def reinstate(self, x, y):
        """
            Reuses the existing sprite to fire and spawn the players laser on the screen.

            :param x: The x-coordinate of the laser
            :type x: float

            :param y: The y-coordinate of the laser
            :type y: float

            :return: None
        """

        self.laser_update = 20
        self.laser.shape(alien_mode_setup.laser_right_texture)
        self.laser.goto(x, y)
        self.laser.showturtle()

    @property
    def laser(self):
        """Human Laser Getter"""
        return self._laser

    def get_laser_update(self):
        """
            Returns the pierce variable for the given laser sprite.

            :return: laser_update: The pierce variable
            :type: int
        """

        return self.laser_update

    def remove(self):
        """
            Removes the human laser form the screen.

            :return: None
        """

        self.laser.hideturtle()
        self.laser_update = 0
