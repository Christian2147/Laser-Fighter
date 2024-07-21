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

from components.gui.InterfaceSelect import Selector
from components.gui.InterfacePanel import Panel
from components.gui.InterfacePriceLabel import PriceLabel


class SpawnPanel:
    def __init__(self, scale_factor, scale_factor_x, scale_factor_y):
        self.panel_turtle = []
        self.panel_index = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.panel_turtle
        del self.panel_index

    def spawn_panel(self, mode):
        """
            Spawn a panel on the screen with the correct type based on what screen the player is on.

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
    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        self.all_selector = []
        self.selectors_on_screen_list = []
        self.current_selector_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y
        self.fullscreen = fullscreen

    def __del__(self):
        del self.all_selector
        del self.selectors_on_screen_list
        del self.current_selector_index

    def spawn_selector(self, type):
        if len(self.all_selector) <= len(self.selectors_on_screen_list):
            selector = Selector(type, self.scale_factor_x, self.scale_factor_y, self.fullscreen)
            self.selectors_on_screen_list.append(selector)
            self.current_selector_index = self.current_selector_index + 1
            self.all_selector.append(selector)
        else:
            for s in self.all_selector:
                if s.get_selector().isvisible():
                    continue
                else:
                    if type == "Tab":
                        s.reinstate_to_tab(self.scale_factor_x, self.scale_factor_y, self.fullscreen)
                    elif type == "Slot":
                        s.reinstate_to_slot(self.scale_factor_x, self.scale_factor_y, self.fullscreen)
                    self.selectors_on_screen_list.append(s)
                    self.current_selector_index = self.current_selector_index + 1
                    break


class SpawnPriceLabel:
    def __init__(self, fullscreen):
        self.all_price_label = []
        self.price_label_on_screen_list = []
        self.current_price_index = 0

        self.fullscreen = fullscreen

    def __del__(self):
        del self.all_price_label
        del self.price_label_on_screen_list
        del self.current_price_index

    def spawn_price_label(self, id, x, y):
        if len(self.all_price_label) <= len(self.price_label_on_screen_list):
            price_label = PriceLabel(id, x, y, self.fullscreen)
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
