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


class PriceLabel:
    def __init__(self, id, x, y, fullscreen):
        self.price_label = turtle.Turtle()
        self.price_label.penup()
        if fullscreen == 1:
            self.price_label.shape("Textures/Coins/Coin_Indicator_Scaled.gif")
        else:
            self.price_label.shape("Textures/Coins/Coin_Indicator.gif")
        self.price_label.goto(x, y)

        self.id = id

    def __del__(self):
        self.price_label.clear()
        del self.price_label

    def reinstate(self, id, x, y):
        self.price_label.goto(x, y)
        self.price_label.showturtle()

        self.id = id

    def get_price_label(self):
        return self.price_label

    def get_id(self):
        return self.id

    def remove(self):
        self.price_label.hideturtle()
