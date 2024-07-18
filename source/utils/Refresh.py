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


class Refresh:
    def __init__(self):
        self.update_variables = 0
        self.refresh_indicator = 0
        self.refresh_text = 0
        self.refresh_panel = 0
        self.move_tab_selector = 0
        self.move_slot_selector = 0

    def __del__(self):
        del self.update_variables
        del self.refresh_indicator
        del self.refresh_text
        del self.refresh_panel
        del self.move_tab_selector
        del self.move_slot_selector

    def __repr__(self):
        return (f"MyClass(update_variables={self.update_variables}, "
                f"refresh_indicator={self.refresh_indicator}, "
                f"refresh_text={self.refresh_text}, "
                f"refresh_panel={self.refresh_panel}, "
                f"move_tab_selector={self.move_tab_selector}, "
                f"move_slot_selector={self.move_slot_selector})")
