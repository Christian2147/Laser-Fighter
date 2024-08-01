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
    File: Refresh.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    Controls the refreshing of text in Laser Fighter. These variables exist to ensure that the text is not
        constantly being updated and causing performance issues.
"""


class Refresh:
    """
        Holds the refresh variables for Laser Fighter.

        Attributes:
            refresh_button (int): Determines when the button text needs to be refreshed.
            refresh_indicator (int): Determines when the button indicators text needs to be refreshed.
            refresh_text (int): Determines when standalone text needs to be refreshed.
            refresh_panel (int): Determines when the panels text needs to be refreshed.
            move_tab_selector (int): Determines when the tab selector needs to be moved.
            move_slot_selector (int): Determines when the slot selector needs to be moved.
    """

    def __init__(self):
        """
            Creates an instance for the refresh variables to be held in.
        """

        self.refresh_button = 1
        self.refresh_indicator = 0
        self.refresh_text = 0
        self.refresh_panel = 0
        self.move_tab_selector = 0
        self.move_slot_selector = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.refresh_button
        del self.refresh_indicator
        del self.refresh_text
        del self.refresh_panel
        del self.move_tab_selector
        del self.move_slot_selector

    def __repr__(self):
        """
            Creates a print statement for the refresh variables where they are all listed out in order.

            :return: Prints all of the refresh variables in a list.
            :type: string
        """

        return (f"MyClass(refresh_button={self.refresh_button}, "
                f"refresh_indicator={self.refresh_indicator}, "
                f"refresh_text={self.refresh_text}, "
                f"refresh_panel={self.refresh_panel}, "
                f"move_tab_selector={self.move_tab_selector}, "
                f"move_slot_selector={self.move_slot_selector})")
