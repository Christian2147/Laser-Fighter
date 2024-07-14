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
from Data.data import all_button_list
from Data.data import buttons_on_screen_list
from Data.data import current_button_index
from Data.data import all_text_list
from Data.data import text_on_screen_list
from Data.data import current_text_index
from Class.button import Button
from Class.textBox import Text


class Slot:
    def __init__(self, id, scale_factor_x, scale_factor_y, fullscreen):
        global current_button_index
        # If a usable button sprite does not exist
        if len(all_button_list) <= len(buttons_on_screen_list):
            # Create a new button object
            button = Button("Shop_Slot", id, scale_factor_x, scale_factor_y, fullscreen)
            buttons_on_screen_list.append(button)
            current_button_index = current_button_index + 1
            all_button_list.append(button)
        # If a usable button sprite does exist
        else:
            found = 0
            # Go through all the button sprites
            for bu in all_button_list:
                # First check if one can be found with a button indicator
                if bu.get_button_frame().isvisible() or bu.indicator == 0:
                    continue
                # If found, reinstate that one
                else:
                    bu.reinstate_to_shop_slot(id, scale_factor_x, scale_factor_y, fullscreen)
                    buttons_on_screen_list.append(bu)
                    current_button_index = current_button_index + 1
                    found = 1
                    break
            # If not found
            if found == 0:
                # Find any available button sprite
                for bu in all_button_list:
                    if bu.get_button_frame().isvisible():
                        continue
                    else:
                        # Reinstate it and add the button indicator
                        bu.reinstate_to_shop_slot(id, scale_factor_x, scale_factor_y, fullscreen)
                        buttons_on_screen_list.append(bu)
                        current_button_index = current_button_index + 1
                        break
