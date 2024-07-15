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
    File: description.py
    Author: Christian Marinkovich
    Date: 2024-07-14
    Description:
    This file contains the class for the description object, which is used to store all of the side panel
        descriptions for all of the items and upgrades in the shop.
    These variables are used to create turtle text on the screen.
"""


class Description:
    """
        Represents the description object for storing the side panel descriptions.

        Attributes:
            align (string): The vertical alignment of the text (left, center, right)
            text (string): The text itself as a string
            size (int): The font size
            font (string): The font type (Courier always)
    """

    def __init__(self, align, text, size, font):
        """
            Creates a description object

            :param align: The vertical alignment of the text
            :type align: string

            :param text: The description text
            :type text: string

            :param size: The font size
            :type size: int

            :param font: The font type
            :type font: string
        """

        self.align = align
        self.text = text
        self.size = size
        self.font = font

    def __del__(self):
        """
            Cleans up the variables from memory once the program has terminated

            :return: None
        """

        del self.align
        del self.text
        del self.size
        del self.font

    def get_align(self):
        """
            Returns the vertical alignment of the text

            :return: align: The vertical alignment of the text
            :type: string
        """

        return self.align

    def get_text(self):
        """
            Returns the description text

            :return: text: The description text
            :type: string
        """

        return self.text

    def get_size(self):
        """
            Returns the font size of the description text

            :return: size: The font size
            :type: int
        """

        return self.size

    def get_font(self):
        """
            Returns the font type of the description text

            :return: font: The font type
            :type: string
        """

        return self.font
