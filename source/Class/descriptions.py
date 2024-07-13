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


class Description:
    def __init__(self, align, text, size, font):
        self.align = align
        self.text = text
        self.size = size
        self.font = font

    def __del__(self):
        del self.align
        del self.text
        del self.size
        del self.font

    def get_align(self):
        return self.align

    def get_text(self):
        return self.text

    def get_size(self):
        return self.size

    def get_font(self):
        return self.font