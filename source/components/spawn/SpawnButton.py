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

from components.gui.InterfaceButton import Button


class SpawnButton:
    def __init__(self, scale_factor, scale_factor_x, scale_factor_y):
        self.all_button_list = []
        self.buttons_on_screen_list = []
        self.current_button_index = 0

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_button_list
        del self.buttons_on_screen_list
        del self.current_button_index

    def spawn_button(self, type, id, page=None):
        """
            Spawns a button on the screen using the button class.

            :param type: The type of button to create
            :type type: string

            :param id: The id of the button to create
            :type id: int

            :return: None
        """

        # If a usable button sprite does not exist
        if len(self.all_button_list) <= len(self.buttons_on_screen_list):
            # Create a new button object
            if type != "Shop_Slot":
                button = Button(type, id, self.scale_factor, self.scale_factor_x, self.scale_factor_y)
            else:
                button = Button(type, id, self.scale_factor, self.scale_factor_x, self.scale_factor_y, page=page)
            self.buttons_on_screen_list.append(button)
            self.current_button_index = self.current_button_index + 1
            self.all_button_list.append(button)
        # If a usable button sprite does exist
        else:
            # If the button to create does not need a button indicator
            if type != "Settings_Toggle" and type != "Shop_Slot" and type != "Power_Up_Slot" and type != "Buy":
                # Reinstate the button like normal
                # Go through all the button sprites
                for bu in self.all_button_list:
                    # If the current sprite is already in use
                    if bu.get_button_frame().isvisible():
                        continue
                    # If the current sprite is free and ready to be used
                    else:
                        # Reinstate the button to the correct type and id
                        if type == "Title":
                            bu.reinstate_to_title(id)
                        elif type == "Title_Small":
                            bu.reinstate_to_title_small(id)
                        elif type == "Game":
                            bu.reinstate_to_game()
                        elif type == "Tab":
                            bu.reinstate_to_tab(id)
                        elif type == "Regular_Settings_And_Controls":
                            bu.reinstate_to_regular_settings_and_controls(id)
                        elif type == "Controls_Toggle":
                            bu.reinstate_to_controls_toggle(id)
                        # Add it to the screen
                        self.buttons_on_screen_list.append(bu)
                        self.current_button_index = self.current_button_index + 1
                        break
            # If the button to create does need a button indicator
            else:
                found = 0
                # Go through all the button sprites
                for bu in self.all_button_list:
                    # First check if one can be found with a button indicator
                    if bu.get_button_frame().isvisible() or bu.indicator == 0:
                        continue
                    # If found, reinstate that one
                    else:
                        if type == "Settings_Toggle":
                            bu.reinstate_to_settings_toggle(id)
                        elif type == "Shop_Slot":
                            bu.reinstate_to_shop_slot(id, page)
                        elif type == "Power_Up_Slot":
                            bu.reinstate_to_power_up_slot(id)
                        elif type == "Buy":
                            bu.reinstate_to_buy()
                        self.buttons_on_screen_list.append(bu)
                        self.current_button_index = self.current_button_index + 1
                        found = 1
                        break
                # If not found
                if found == 0:
                    # Find any available button sprite
                    for bu in self.all_button_list:
                        if bu.get_button_frame().isvisible():
                            continue
                        else:
                            # Reinstate it and add the button indicator
                            if type == "Settings_Toggle":
                                bu.reinstate_to_settings_toggle(id)
                            elif type == "Shop_Slot":
                                bu.reinstate_to_shop_slot(id, page)
                            elif type == "Power_Up_Slot":
                                bu.reinstate_to_power_up_slot(id)
                            elif type == "Buy":
                                bu.reinstate_to_buy()
                            self.buttons_on_screen_list.append(bu)
                            self.current_button_index = self.current_button_index + 1
                            break
