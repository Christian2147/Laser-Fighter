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
    File: SpawnGUI.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the spawning logic and the containers for GUI elements in Laser Fighter.
    This includes side panels, selectors, and price labels.
"""

from components.gui.InterfaceSelectPygame import Selector
from components.gui.InterfacePanelPygame import Panel
from components.gui.InterfacePriceLabelPygame import PriceLabel


class SpawnPanel:
    """
        Represents the Panel container in Laser Fighter.

        Attributes:
            panel_sprite (list): Contains the panel sprite once it is spawned
            panel_index (list): Determines if the panel sprite has been spawned yet or not

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Panel object.

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.panel_sprite = []
        self.panel_index = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.panel_sprite
        del self.panel_index

    def spawn_panel(self, mode):
        """
            Spawn a panel on the screen with the correct type based on what screen the player is on.

            :param mode: Determines the current mode of the game
            :type mode: string

            :return: None
        """

        panel = Panel(mode, self.scale_factor, self.scale_factor_x, self.scale_factor_y)
        self.panel_sprite.append(panel)
        self.panel_index = self.panel_index + 1


class SpawnSelector:
    """
        Represents the Selector container in Laser Fighter.

        Attributes:
            selector_on_screen_list (list): Contains all of the selector sprites created since the game has launched, even
                ones removed from the screen
            current_selector_index (int): Stores the number of selectors currently active and visible on the screen.

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Selector object.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.selector_on_screen_list = []
        self.current_selector_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.selector_on_screen_list
        del self.current_selector_index

    def spawn_selector(self, type):
        """
            Spawns a selector sprite on the screen over a specific button.

            :param type: Determines if it is a tab selector or a slot selector
            :type type: string

            :return: None
        """

        selector = Selector(type, self.scale_factor_x, self.scale_factor_y)
        self.current_selector_index = self.current_selector_index + 1
        self.selector_on_screen_list.append(selector)


class SpawnPriceLabel:
    """
        Represents the Price Label container in Laser Fighter.

        Attributes:
            price_label_on_screen_list (list): Contains all of the price label sprites created since the game has launched, even
                ones removed from the screen
            current_price_index (int): Stores the number of price labels currently active and visible on the screen.
    """

    def __init__(self):
        """
            Creates the lists necessary to store the Price Label object.
        """

        self.price_label_on_screen_list = []
        self.current_price_index = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.price_label_on_screen_list
        del self.current_price_index

    def spawn_price_label(self, id, x, y):
        """
            Spawns a price label over the specified slot on the screen.
            :param id: The id of the of the price label
            :type id: int

            :param x: The x-coordinate of the button to spawn the price label over
            :type x: float

            :param y: The y-coordinate of the button to spawn the price label over
            :type y: float

            :return: None
        """

        price_label = PriceLabel(id, x, y)
        self.current_price_index = self.current_price_index + 1
        self.price_label_on_screen_list.append(price_label)
