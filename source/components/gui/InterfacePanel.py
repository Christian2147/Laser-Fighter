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
    File: InterfacePanel.py
    Author: Christian Marinkovich
    Date: 2024-07-14
    Description:
    This file contains the logic for the side panel. This includes updating the description on the side panel and
        loading all of the preview data of the item currently selected.
"""

import turtle
from setup.Initialization import shop_config
from setup.data.ShopDescriptions import MAIN_DESCRIPTION
from setup.data.ShopDescriptions import MACHINE_DESCRIPTIONS
from setup.data.ShopDescriptions import ALIEN_DESCRIPTIONS
from setup.data.ShopDescriptions import YELLOW_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import BLUE_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import GREEN_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import RED_POWER_UP_DESCRIPTIONS


class Panel:
    """
        Represents the panel in Laser Fighter for displaying important information.

        Attributes:
            panel (turtle.Turtle()): The sprite that represents the frame of the panel
            panel_text (turtle.Turtle()): The sprite that displays the panels text
            panel_indicator (turtle.Turtle()): The sprite that displays the visual element on the panel
            type (string): The type of panel generated (depending on the current screen)
            catigory (string): The current type of description being displayed
            id (int): The id for the specific description being displayed
    """

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
        self.panel_text.goto(self.panel.xcor() - 155 * scale_factor_x, self.panel.ycor() + 290 * scale_factor_y)
        self.panel_text.hideturtle()

        self.panel_indicator = turtle.Turtle()
        # Ensure that the turtle does not draw lines on the screen while moving
        self.panel_indicator.penup()
        if type == "Shop":
            self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 190 * scale_factor_y)
        self.panel_indicator.hideturtle()

        self.type = type
        self.catigory = "Welcome"
        self.id = 1

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

        self.panel_text.goto(self.panel.xcor() - 155 * scale_factor_x, self.panel.ycor() + 290 * scale_factor_y)

        self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 190 * scale_factor_y)

        self.type = "Shop"
        self.catigory = "Welcome"
        self.id = 1

    def get_panel_frame(self):
        return self.panel

    def get_panel_text(self):
        return self.panel_text

    def get_panel_indicator(self):
        return self.panel_indicator

    def set_panel_text(self, new_catigory, new_id, scale_factor_x, scale_factor_y):
        self.catigory = new_catigory
        self.id = new_id
        if self.catigory == "Welcome":
            self.panel_text.goto(self.panel.xcor() - 155 * scale_factor_x, self.panel.ycor() + 290 * scale_factor_y)
        elif self.catigory == "Alien_Mode":
            self.panel_text.goto(self.panel.xcor() - 155 * scale_factor_x, self.panel.ycor() + 55 * scale_factor_y)
        else:
            self.panel_text.goto(self.panel.xcor() - 155 * scale_factor_x, self.panel.ycor() + 40 * scale_factor_y)

    def remove(self):
        self.panel.hideturtle()
        self.panel_text.hideturtle()
        self.panel_text.clear()
        self.panel_indicator.hideturtle()

    def write_text(self, scale_factor, scale_factor_y, fullscreen):
        # Clears the existing text
        self.panel_text.clear()

        # Writes new text based on the panel type and id of the text
        if self.type == "Shop":
            if self.catigory == "Welcome":
                for i in range(MAIN_DESCRIPTION[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(MAIN_DESCRIPTION[self.id - 1].get_text()[i]),
                                            align=MAIN_DESCRIPTION[self.id - 1].get_align(),
                                            font=(MAIN_DESCRIPTION[self.id - 1].get_font(),
                                            int(MAIN_DESCRIPTION[self.id - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 36 * scale_factor_y)
            elif self.catigory == "Machine_Mode":
                for i in range(MACHINE_DESCRIPTIONS[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(MACHINE_DESCRIPTIONS[self.id - 1].get_text()[i]),
                                            align=MACHINE_DESCRIPTIONS[self.id - 1].get_align(),
                                            font=(MACHINE_DESCRIPTIONS[self.id - 1].get_font(),
                                            int(MACHINE_DESCRIPTIONS[self.id - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 24 * scale_factor_y)
            elif self.catigory == "Alien_Mode":
                for i in range(ALIEN_DESCRIPTIONS[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(ALIEN_DESCRIPTIONS[self.id - 1].get_text()[i]),
                                            align=ALIEN_DESCRIPTIONS[self.id - 1].get_align(),
                                            font=(ALIEN_DESCRIPTIONS[self.id - 1].get_font(),
                                            int(ALIEN_DESCRIPTIONS[self.id - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 24 * scale_factor_y)
            elif self.catigory == "Yellow_Power_Up":
                check_setting = shop_config.yellow_power_up_level

                for i in range(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * scale_factor_y)
            elif self.catigory == "Blue_Power_Up":
                check_setting = shop_config.blue_power_up_level

                for i in range(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * scale_factor_y)
            elif self.catigory == "Green_Power_Up":
                check_setting = shop_config.green_power_up_level

                for i in range(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * scale_factor_y)
            elif self.catigory == "Red_Power_Up":
                check_setting = shop_config.red_power_up_level

                for i in range(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * scale_factor_y)
        self.set_indicator(fullscreen)

    def set_indicator(self, fullscreen):
        if self.catigory == "Welcome":
            self.panel_indicator.hideturtle()
        else:
            if self.catigory == "Machine_Mode":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Player/Player_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Player/Player.gif")
            elif self.catigory == "Alien_Mode":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Gun/Player_Gun_Right_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Gun/Player_Gun_Right.gif")
            elif self.catigory == "Yellow_Power_Up":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
            elif self.catigory == "Blue_Power_Up":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Power_Ups/Blue_Lightning_Power_Up_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Power_Ups/Blue_Lightning_Power_Up.gif")
            elif self.catigory == "Green_Power_Up":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Power_Ups/Green_Lightning_Power_Up_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Power_Ups/Green_Lightning_Power_Up.gif")
            elif self.catigory == "Red_Power_Up":
                if fullscreen == 1:
                    self.panel_indicator.shape("Textures/Power_Ups/Red_Lightning_Power_Up_Scaled.gif")
                else:
                    self.panel_indicator.shape("Textures/Power_Ups/Red_Lightning_Power_Up.gif")
            self.panel_indicator.showturtle()
