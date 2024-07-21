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
    File: EffectBackgroundEffect.py
    Author: Christian Marinkovich
    Date: 2024-07-07
    Description:
    This file contains the logic related to all of the background effects and sprites in Alien Mode.
    This includes the ground, player ship, the Sun, and the Earth.
"""

import turtle
import math
import time
from setup.TextureSetup import EARTH_TEXTURE
from setup.TextureSetup import SUN_TEXTURE
from setup.TextureSetup import SPACE_SHIP_TEXTURE
from setup.TextureSetup import GROUND_TEXTURE


class Earth:
    """
        Represents the Earth sprite in Alien Mode's background. This is a stationary sprite and never moves.

        Attributes:
            earth (turtle.Turtle()): The Earth sprite
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates an Earth sprite and spawns it on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.earth = turtle.Turtle()
        self.earth.shape(EARTH_TEXTURE)
        self.earth.shapesize(3 * scale_factor_y, 3 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.earth.penup()
        self.earth.goto(0, 150)

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.earth.clear()
        del self.earth

    def reinstate(self):
        """
            Reuses the existing sprite to spawn the Earth on the screen

            :return: None
        """

        self.earth.showturtle()

    def get_earth(self):
        """
            Returns the Earth sprite so that its class attributes can be accessed.

            :return: earth: The Earth sprite
            :type: Turtle.turtle()
        """

        return self.earth

    def remove(self):
        """
            Removes the Earth sprite form the screen and resets its attributes.

            :return: None
        """

        self.earth.hideturtle()


class Sun:
    """
        Represents the Sun sprite in Alien Mode's background. This sprite moves slowly in an ellipse to represent
            the day/night cycle.

        Attributes:
            sun (turtle.Turtle()): The Sun sprite
            angle (int): The angle that the sun is currently moving at in the ellipse
            x-coordinate (float): Represents the current x-coordinate of the sun
            y-coordinate (float): Represents the current y-coordinate of the sun
            start_time (float): Used as a timestamp for the suns movement (So that the movement is consistent
                regardless of frame rate)
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates a Sun sprite and spawns it on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.sun = turtle.Turtle()
        self.sun.shape(SUN_TEXTURE)
        self.sun.shapesize(4 * scale_factor_y, 4 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.sun.penup()

        self.angle = 90
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.start_time = 0
        self.movement_activated = 0

        self.x_coordinate = 715 * math.cos(math.radians(self.angle))
        self.y_coordinate = 350 * math.sin(math.radians(self.angle)) - 150

        self.sun.goto(self.x_coordinate * scale_factor_x, self.y_coordinate * scale_factor_y)

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.sun.clear()
        del self.sun

    def reinstate(self):
        """
            Reuses the existing sprite to spawn the Sun on the screen

            :return: None
        """

        self.sun.showturtle()

    def get_sun(self):
        """
            Returns the Sun sprite so that its class attributes can be accessed.

            :return: sun: The Sun sprite
            :type: Turtle.turtle()
        """

        return self.sun

    def remove(self):
        """
            Removes the Sun sprite from the screen and resets its attributes.

            :return: None
        """

        self.sun.hideturtle()
        self.movement_activated = 0

    def update_position(self):
        """
            Updates the suns position over a given interval of time on its elliptical path across the screen.

            :return: None
        """

        # If the movement has just started, a start time is created for it
        if self.movement_activated == 0:
            self.start_time = time.time()
            self.movement_activated = 1

        # Update the suns position every 0.2 seconds
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= 0.2:
            # Create a delta angle so that movement stays consistent regardless of lag
            delta_angle = 0.1 * ((elapsed_time - 0.2) / 0.2)
            # Move the angle 0.1 every iteration (Very slow movement)
            if self.angle > 0:
                self.angle = self.angle - 0.1 - delta_angle
            else:
                self.angle = 180
            # Find the new x and y coordinate of the sun given the new angle
            self.x_coordinate = 715 * math.cos(math.radians(self.angle))
            self.y_coordinate = 350 * math.sin(math.radians(self.angle)) - 150

            # Move the sun to this new location
            self.sun.goto(self.x_coordinate * self.scale_factor_x, self.y_coordinate * self.scale_factor_y)
            self.start_time = time.time()


class BackgroundObjects:
    """
        Represents the ground level background sprites in Alien Mode's background. These are stationary and
            never move.

        Attributes:
            ground (turtle.Turtle()): The ground sprite
            ship (turtle.Turtle()): The player's ship sprite
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the ground level background sprites and spawns them on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        # Ground is created
        self.ground = turtle.Turtle()
        self.ground.shape(GROUND_TEXTURE)
        self.ground.shapesize(22.5 * scale_factor_y, 80 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.ground.penup()
        self.ground.goto(0, -731 * scale_factor_y)

        # The players ship is created
        self.ship = turtle.Turtle()
        self.ship.shape(SPACE_SHIP_TEXTURE)
        self.ship.shapesize(3 * scale_factor_y, 6 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.ship.penup()
        self.ship.goto(0, -116 * scale_factor_y)

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.ground.clear()
        self.ship.clear()
        del self.ground
        del self.ship

    def reinstate(self):
        """
            Reuses the existing sprites to spawn the background objects on the screen

            :return: None
        """

        self.ground.showturtle()
        self.ship.showturtle()

    def get_ground(self):
        """
            Returns the ground sprite so that its class attributes can be accessed.

            :return: ground: The ground sprite
            :type: Turtle.turtle()
        """

        return self.ground

    def get_ship(self):
        """
            Returns the players ship sprite so that its class attributes can be accessed.

            :return: ship: The players ship sprite
            :type: Turtle.turtle()
        """

        return self.ship

    def remove(self):
        """
            Removes the sprites from the screen and resets their attributes.

            :return: None
        """

        self.ground.hideturtle()
        self.ship.hideturtle()
