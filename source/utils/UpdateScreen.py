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


class ScreenUpdate:
    def __init__(self):
        self._mode = "Title_Mode"
        self.page = "Machine_Mode"

        self.tick_update = 0
        self.screen_update = 0
        self.page_update = 0

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        self._mode = new_mode

    #def __del__(self):
        #del self.mode
        #del self.page
        #del self.tick_update
        #el self.screen_update
        #del self.page_update
