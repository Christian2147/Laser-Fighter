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
from setup.TextureSetup import SLOT_SELECTOR_TEXTURE
from setup.TextureSetup import TAB_SELECTOR_TEXTURE


class Selector:
    def __init__(self, type, scale_factor_x, scale_factor_y):
        self.selector = turtle.Turtle()
        self.selector.penup()
        if type == "Tab":
            self.selector.shape(TAB_SELECTOR_TEXTURE)
            self.selector.goto(-603.5 * scale_factor_x, 150 * scale_factor_y)
        else:
            self.selector.shape(SLOT_SELECTOR_TEXTURE)
            self.selector.goto(-427 * scale_factor_x, 95.5 * scale_factor_y)

        self.type = type

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.selector.clear()
        del self.selector
        del self.type

    def reinstate_to_tab(self):
        self.selector.shape(TAB_SELECTOR_TEXTURE)
        self.selector.goto(-603.5 * self.scale_factor_x, 150 * self.scale_factor_y)
        self.selector.showturtle()

        self.type = "Tab"

    def reinstate_to_slot(self):
        self.selector.shape(SLOT_SELECTOR_TEXTURE)
        self.selector.goto(-427 * self.scale_factor_x, 95.5 * self.scale_factor_y)
        self.selector.showturtle()

        self.type = "Slot"

    def get_selector(self):
        return self.selector

    def get_type(self):
        return self.type

    def remove(self):
        self.selector.hideturtle()

    def new_select(self, x, y):
        self.selector.goto(x, y)
