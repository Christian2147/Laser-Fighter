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
from components.EffectBackgroundEffect import Ship
from components.EffectBackgroundEffect import Ground


class SpawnSun:
    """
        Represents the Sun container in Laser Fighter.

        Attributes:
            sun_sprite (list): Contains the sun sprite once it is spawned
            sun_index (list): Determines if the sun sprite has been spawned yet or not

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Sun background object.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.sun_sprite = []
        self.sun_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.sun_sprite
        del self.sun_index

    def spawn_sun(self):
        """
            Spawn the sun in the background.

            :return: None
        """

        sun = Sun(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.sun_sprite.append(sun)
        self.sun_index = self.sun_index + 1


class SpawnEarth:
    """
        Represents the Earth container in Laser Fighter.

        Attributes:
            earth_sprite (list): Contains the earth sprite once it is spawned
            earth_index (list): Determines if the earth sprite has been spawned yet or not

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Earth in the background.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.earth_sprite = []
        self.earth_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.earth_sprite
        del self.earth_index

    def spawn_earth(self):
        """
            Spawn the Earth in the background.

            :return: None
        """

        earth = Earth(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.earth_sprite.append(earth)
        self.earth_index = self.earth_index + 1


class SpawnShip:
    """
            Represents the Background Objects container in Laser Fighter.
            This includes both the ground and the player ship in Alien Mode.

            Attributes:
                ship_sprite (list): Contains the background objects sprites once they are spawned
                ship_index (list): Determines if the background objects sprites have been spawned yet or not

                textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
                scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
                scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
        """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Player Ship in Alien Mode.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.ship_sprite = []
        self.ship_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.ship_sprite
        del self.ship_index

    def spawn_ship(self):
        """
            Spawn the Alien Mode background ship.

            :return: None
        """

        ship = Ship(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.ship_sprite.append(ship)
        self.ship_index = self.ship_index + 1


class SpawnGround:
    """
        Represents the Ground container Alien Mode in Laser Fighter.

        Attributes:
            ground_sprite (list): Contains the background objects sprites once they are spawned
            ground_index (list): Determines if the background objects sprites have been spawned yet or not

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Ground and Player Ship in Alien Mode.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.ground_sprite = []
        self.ground_index = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.ground_sprite
        del self.ground_index

    def spawn_ground(self):
        """
            Spawn the Alien Mode ground.

            :return: None
        """

        ground = Ground(self._textures, self.scale_factor_x, self.scale_factor_y)
        self.ground_sprite.append(ground)
        self.ground_index = self.ground_index + 1
