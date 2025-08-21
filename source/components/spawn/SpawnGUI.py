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
from components.gui.InterfacePopUp import PopUp


class SpawnPanel:
    """
        Represents the Panel container in Laser Fighter.

        Attributes:
            panel_sprite (list): Contains the panel sprite once it is spawned
            panel_index (list): Determines if the panel sprite has been spawned yet or not

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Panel object.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.panel_sprite = []
        self.panel_index = 0

        self._textures = textures
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

    def spawn_panel(self, mode, id=1):
        """
            Spawn a panel on the screen with the correct type based on what screen the player is on.

            :param mode: Determines the current mode of the game
            :type mode: string

            :return: None
        """

        panel = Panel(mode, self._textures, self.scale_factor, self.scale_factor_x, self.scale_factor_y, id)
        self.panel_sprite.append(panel)
        self.panel_index = self.panel_index + 1


class SpawnSelector:
    """
        Represents the Selector container in Laser Fighter.

        Attributes:
            selector_on_screen_list (list): Contains all of the selector sprites created since the game has launched, even
                ones removed from the screen
            current_selector_index (int): Stores the number of selectors currently active and visible on the screen.

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Selector object.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.selector_on_screen_list = []
        self.current_selector_index = 0

        self._textures = textures
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

        selector = Selector(type, self._textures, self.scale_factor_x, self.scale_factor_y)
        self.current_selector_index = self.current_selector_index + 1
        self.selector_on_screen_list.append(selector)


class SpawnPriceLabel:
    """
        Represents the Price Label container in Laser Fighter.

        Attributes:
            price_label_on_screen_list (list): Contains all of the price label sprites created since the game has launched, even
                ones removed from the screen
            current_price_index (int): Stores the number of price labels currently active and visible on the screen.

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
    """

    def __init__(self, textures):
        """
            Creates the lists necessary to store the Price Label object.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup
        """

        self.price_label_on_screen_list = []
        self.current_price_index = 0

        self._textures = textures

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

        price_label = PriceLabel(id, x, y, self._textures)
        self.current_price_index = self.current_price_index + 1
        self.price_label_on_screen_list.append(price_label)


class SpawnPopUp:
    """
        Represents the Pop Up container in Laser Fighter.

        Attributes:
            pop_up_on_screen_list (list): Contains all of the pop up sprites created since the game has launched
            current_pop_up_index (int): Stores the number of pop ups currently active and visible on the screen.

            textures (TextureSetup): Stores all of the textures that are used in Laser Fighter
    """

    def __init__(self, textures, scale_factor, scale_factor_x, scale_factor_y):
        """
            Creates the lists necessary to store the Pop Up object.

            :param textures: Stores all of the textures that are used in Laser Fighter
            :type textures: TextureSetup

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.pop_up_on_screen_list = []
        self.current_pop_up_index = 0

        self._textures = textures
        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.pop_up_on_screen_list
        del self.current_pop_up_index

    def spawn_pop_up(self, icon, text, type, on_yes=None, on_no=None, on_ok=None):
        """
            Spawns a pop up over the specified slot on the screen.

            :param icon: The type of icon to display ('error', 'warning', 'question')
            :type icon: str

            :param text: List of text lines to display in the pop-up
            :type text: list[str]

            :param type: Pop-up type (1 = Yes/No, 2 = OK)
            :type type: int

            :param on_yes: Optional callback function when Yes is clicked
            :param on_no: Optional callback function when No is clicked
            :param on_ok: Optional callback function when OK is clicked

            :return: None
        """

        pop_up = PopUp(
            icon=icon,
            text=text,
            type=type,
            textures=self._textures,
            scale_factor=self.scale_factor,
            scale_factor_x=self.scale_factor_x,
            scale_factor_y=self.scale_factor_y,
            on_yes=on_yes,
            on_no=on_no,
            on_ok=on_ok
        )
        self.current_pop_up_index = self.current_pop_up_index + 1
        self.pop_up_on_screen_list.append(pop_up)
