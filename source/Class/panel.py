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
from Data.shop import *


class Panel:
    def __init__(self, type, scale_factor_x, scale_factor_y, fullscreen):
        self.panel = turtle.Turtle()
        self.panel.color("#3D3D3D")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.panel.penup()
        if type == "Shop":
            if fullscreen == 1:
                self.panel.shape("Textures/GUI/Side_Panel_Shop_Scaled.gif")
            else:
                self.panel.shape("Textures/GUI/Side_Panel_Shop.gif")
            self.panel.goto(450 * scale_factor_x, 0)

        self.panel_text = turtle.Turtle()
        self.panel_text.color("white")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.panel_text.penup()
        if fullscreen == 1:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 8 * scale_factor_y)
        else:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 28 * scale_factor_y)
        self.panel_text.hideturtle()

        self.panel_indicator = turtle.Turtle()
        # Ensure that the turtle does not draw lines on the screen while moving
        self.panel_indicator.penup()
        if type == "Shop":
            self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 205 * scale_factor_y)
        self.panel_indicator.hideturtle()

        self.type = type

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.panel.clear()
        self.panel_text.clear()
        self.panel_indicator.clear()
        del self.panel
        del self.panel_text
        del self.panel_indicator

    def reinstate_to_shop(self, scale_factor_x, scale_factor_y, fullscreen):
        if fullscreen == 1:
            self.panel.shape("Textures/GUI/Side_Panel_Shop_Scaled.gif")
        else:
            self.panel.shape("Textures/GUI/Side_Panel_Shop.gif")
        self.panel.goto(450 * scale_factor_x, 0)
        self.panel.showturtle()

        if fullscreen == 1:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 8 * scale_factor_y)
        else:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 28 * scale_factor_y)

        self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 205 * scale_factor_y)

        self.type = "Shop"

    def get_panel_frame(self):
        return self.panel

    def get_panel_text(self):
        return self.panel_text

    def get_panel_indicator(self):
        return self.panel_indicator

    def remove(self):
        self.panel.hideturtle()
        self.panel_text.hideturtle()
        self.panel_text.clear()
        self.panel_indicator.hideturtle()

    def write_text(self, id, scale_factor):
        # Clears the existing text
        self.panel_text.clear()

        # Writes new text based on the panel type and id of the text
        if self.type == "Shop":
            if id == 0:
                self.panel_text.write("Welcome to\n the Shop!\n\nHere, you can\nupgrade your\nweapons,\nabilities,\nand power-ups\nto become even\nmore powerful.", align="right", font=("Courier", int(24 * scale_factor), "normal"))

    def set_indicator(self, id, fullscreen):
        if id != 0:
            if id == 1:
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Player/Player_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Player/Player.gif")

        if id == 0:
            self.panel_indicator.hideturtle()
        else:
            self.panel_indicator.showturtle()
