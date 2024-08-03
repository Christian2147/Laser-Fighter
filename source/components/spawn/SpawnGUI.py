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

from components.gui.InterfaceSelect import Selector
from components.gui.InterfacePanel import Panel
from components.gui.InterfacePriceLabel import PriceLabel


class SpawnPanel:
    """
        Represents the Panel container in Laser Fighter.

        Attributes:
            panel_turtle (list): Contains the panel sprite once it is spawned
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

        self.panel_turtle = []
        self.panel_index = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.panel_turtle
        del self.panel_index

    def spawn_panel(self, mode):
        """
            Spawn a panel on the screen with the correct type based on what screen the player is on.

            :param mode: Determines the current mode of the game
            :type mode: string

            :return: None
        """

        # If the panel sprite does not exist
        if len(self.panel_turtle) == 0:
            panel = Panel(mode, self.scale_factor, self.scale_factor_x, self.scale_factor_y)
            self.panel_turtle.append(panel)
            self.panel_index = self.panel_index + 1
        # If it does exist, just reinstate the existing one
        else:
            for pa in self.panel_turtle:
                if pa.get_panel_frame().isvisible():
                    continue
                else:
                    if mode == "Shop":
                        pa.reinstate_to_shop()
                    self.panel_index = self.panel_index + 1


class SpawnSelector:
    """
        Represents the Selector container in Laser Fighter.

        Attributes:
            all_selector (list): Contains all of the selector sprites created since the game has launched, even
                ones removed from the screen
            selectors_on_screen_list (list): Contains all of the selector sprites currently visible/active on
                the screen.
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

        self.all_selector = []
        self.selectors_on_screen_list = []
        self.current_selector_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_selector
        del self.selectors_on_screen_list
        del self.current_selector_index

    def spawn_selector(self, type):
        """
            Spawns a selector sprite on the screen over a specific button.

            :param type: Determines if it is a tab selector or a slot selector
            :type type: string

            :return: None
        """

        if len(self.all_selector) <= len(self.selectors_on_screen_list):
            selector = Selector(type, self.scale_factor_x, self.scale_factor_y)
            self.selectors_on_screen_list.append(selector)
            self.current_selector_index = self.current_selector_index + 1
            self.all_selector.append(selector)
        else:
            for s in self.all_selector:
                if s.get_selector().isvisible():
                    continue
                else:
                    if type == "Tab":
                        s.reinstate_to_tab()
                    elif type == "Slot":
                        s.reinstate_to_slot()
                    self.selectors_on_screen_list.append(s)
                    self.current_selector_index = self.current_selector_index + 1
                    break


class SpawnPriceLabel:
    """
        Represents the Price Label container in Laser Fighter.

        Attributes:
            all_price_label (list): Contains all of the price label sprites created since the game has launched, even
                ones removed from the screen
            price_label_on_screen_list (list): Contains all of the price label sprites currently visible/active on
                the screen.
            current_price_index (int): Stores the number of price labels currently active and visible on the screen.
    """

    def __init__(self):
        """
            Creates the lists necessary to store the Price Label object.
        """

        self.all_price_label = []
        self.price_label_on_screen_list = []
        self.current_price_index = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.all_price_label
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

        if len(self.all_price_label) <= len(self.price_label_on_screen_list):
            price_label = PriceLabel(id, x, y)
            self.price_label_on_screen_list.append(price_label)
            self.current_price_index = self.current_price_index + 1
            self.all_price_label.append(price_label)
        else:
            for pl in self.all_price_label:
                if pl.get_price_label().isvisible():
                    continue
                else:
                    pl.reinstate(id, x, y)
                    self.price_label_on_screen_list.append(pl)
                    self.current_price_index = self.current_price_index + 1
                    break
