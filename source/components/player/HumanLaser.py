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

import turtle
from setup.ModeSetupMaster import alien_mode_setup


class HumanLaser:
    def __init__(self, x, y, scale_factor_x, scale_factor_y):
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
        self.laser_update = 20
        self.laser.shape(alien_mode_setup.laser_right_texture)
        self.laser.goto(x, y)
        self.laser.showturtle()

    @property
    def laser(self):
        return self._laser

    def get_laser_update(self):
        return self.laser_update

    def remove(self):
        self.laser.hideturtle()
        self.laser_update = 0
