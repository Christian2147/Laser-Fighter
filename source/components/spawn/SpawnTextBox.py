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

from components.gui.InterfaceTextBox import Text


class SpawnTextbox:
    def __init__(self, scale_factor, scale_factor_x):
        self.all_text_list = []
        self.text_on_screen_list = []
        self.current_text_index = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x

    def __del__(self):
        del self.all_text_list
        del self.text_on_screen_list
        del self.current_text_index

    def spawn_text_box(self, id, x, y, color):
        """
            Spawn a textbox on the screen with the given coordinates.

            :param id: The unique identifier for the textbox
            :type id: int

            :param x: The x-coordinate of the text box
            :type x: float

            :param y: The y-coordinate of the text box
            :type y: float

            :param color: The color of the text in the text box.
            :type color: string

            :return: None
        """

        # All spawn functions have this same procedure to check for existing sprites to use
        # This is done because the turtle module makes it impossible to actually fully get rid of a turtle while the
        #   program is running.
        # In order to maintain performance, all turtle sprites are reused as often as possible.
        # This is why a global list exists for every type of sprite in the game.
        if len(self.all_text_list) <= len(self.text_on_screen_list):
            text_box = Text(id, x, y, color, self.scale_factor, self.scale_factor_x)
            self.text_on_screen_list.append(text_box)
            self.current_text_index = self.current_text_index + 1
            self.all_text_list.append(text_box)
        else:
            for t in self.all_text_list:
                if t.in_use == 1:
                    continue
                else:
                    t.reinstate(id, x, y, color)
                    self.text_on_screen_list.append(t)
                    self.current_text_index = self.current_text_index + 1
                    break
