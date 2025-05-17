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
    File: SpawnButton.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for buttons in Laser Fighter.
    This includes any type of clickable button that may appear on the screen.
"""

from components.EffectBackgroundEffect import Earth
from components.EffectBackgroundEffect import Sun
from components.EffectBackgroundEffect import BackgroundObjects


class SpawnSun:
    """
        Represents the Sun container in Laser Fighter.

        Attributes:
            sun_turtle (list): Contains the sun sprite once it is spawned
            sun_index (list): Determines if the sun sprite has been spawned yet or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Sun background object.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.sun_turtle = []
        self.sun_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.sun_turtle
        del self.sun_index

    def spawn_sun(self):
        """
            Spawn the sun in the background.

            :return: None
        """

        if len(self.sun_turtle) == 0:
            sun = Sun(self.scale_factor_x, self.scale_factor_y)
            self.sun_turtle.append(sun)
            self.sun_index = self.sun_index + 1
        else:
            for s in self.sun_turtle:
                if s.get_sun().isvisible():
                    continue
                else:
                    s.reinstate()
                    self.sun_index = self.sun_index + 1


class SpawnEarth:
    """
        Represents the Earth container in Laser Fighter.

        Attributes:
            earth_turtle (list): Contains the earth sprite once it is spawned
            earth_index (list): Determines if the earth sprite has been spawned yet or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Earth in the background.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.earth_turtle = []
        self.earth_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.earth_turtle
        del self.earth_index

    def spawn_earth(self):
        """
            Spawn the Earth in the background.

            :return: None
        """

        if len(self.earth_turtle) == 0:
            earth = Earth(self.scale_factor_x, self.scale_factor_y)
            self.earth_turtle.append(earth)
            self.earth_index = self.earth_index + 1
        else:
            for e in self.earth_turtle:
                if e.get_earth().isvisible():
                    continue
                else:
                    e.reinstate()
                    self.earth_turtle.append(e)
                    self.earth_index = self.earth_index + 1


class SpawnBackgroundObjects:
    """
        Represents the Background Objects container in Laser Fighter.
        This includes both the ground and the player ship in Alien Mode.

        Attributes:
            background_objects_turtle (list): Contains the background objects sprites once they are spawned
            background_objects_index (list): Determines if the background objects sprites have been spawned yet or not

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Ground and Player Ship in Alien Mode.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.background_objects_turtle = []
        self.background_objects_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.background_objects_turtle
        del self.background_objects_index

    def spawn_background_objects(self):
        """
            Spawn the Alien Mode background objects.

            :return: None
        """

        if len(self.background_objects_turtle) == 0:
            background_object = BackgroundObjects(self.scale_factor_x, self.scale_factor_y)
            self.background_objects_turtle.append(background_object)
            self.background_objects_index = self.background_objects_index + 1
        else:
            for bo in self.background_objects_turtle:
                if bo.get_ground().isvisible():
                    continue
                else:
                    bo.reinstate()
                    self.background_objects_turtle.append(bo)
                    self.background_objects_index = self.background_objects_index + 1
