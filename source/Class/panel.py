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
import configparser
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

        if fullscreen == 1:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 8 * scale_factor_y)
        else:
            self.panel_text.goto(self.panel.xcor() + 120 * scale_factor_x, self.panel.ycor() - 28 * scale_factor_y)

        self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 205 * scale_factor_y)

        self.type = "Shop"
        self.catigory = "Welcome"
        self.id = 1

    def get_panel_frame(self):
        return self.panel

    def get_panel_text(self):
        return self.panel_text

    def get_panel_indicator(self):
        return self.panel_indicator

    def set_panel_text(self, new_catigory, new_id):
        self.catigory = new_catigory
        self.id = new_id

    def remove(self):
        self.panel.hideturtle()
        self.panel_text.hideturtle()
        self.panel_text.clear()
        self.panel_indicator.hideturtle()

    def write_text(self, scale_factor):
        # Clears the existing text
        self.panel_text.clear()

        # Writes new text based on the panel type and id of the text
        if self.type == "Shop":
            if self.catigory == "Welcome":
                self.panel_text.write("{}".format(main_description[self.id - 1].get_text()),
                                        align=main_description[self.id - 1].get_align(),
                                        font=(main_description[self.id - 1].get_font(),
                                        int(main_description[self.id - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Machine_Mode":
                self.panel_text.write("{}".format(machine_descriptions[self.id - 1].get_text()),
                                        align=machine_descriptions[self.id - 1].get_align(),
                                        font=(machine_descriptions[self.id - 1].get_font(),
                                        int(machine_descriptions[self.id - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Alien_Mode":
                self.panel_text.write("{}".format(alien_descriptions[self.id - 1].get_text()),
                                        align=alien_descriptions[self.id - 1].get_align(),
                                        font=(alien_descriptions[self.id - 1].get_font(),
                                        int(alien_descriptions[self.id - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Yellow_Power_Up":
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                check_setting = config['Power_Up_Levels'].getint('yellow_power_up')

                self.panel_text.write("{}".format(yellow_power_up_descriptions[check_setting - 1].get_text()),
                                        align=yellow_power_up_descriptions[check_setting - 1].get_align(),
                                        font=(yellow_power_up_descriptions[check_setting - 1].get_font(),
                                        int(yellow_power_up_descriptions[check_setting - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Blue_Power_Up":
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                check_setting = config['Power_Up_Levels'].getint('blue_power_up')

                self.panel_text.write("{}".format(blue_power_up_descriptions[check_setting - 1].get_text()),
                                        align=blue_power_up_descriptions[check_setting - 1].get_align(),
                                        font=(blue_power_up_descriptions[check_setting - 1].get_font(),
                                        int(blue_power_up_descriptions[check_setting - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Green_Power_Up":
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                check_setting = config['Power_Up_Levels'].getint('green_power_up')

                self.panel_text.write("{}".format(green_power_up_descriptions[check_setting - 1].get_text()),
                                        align=green_power_up_descriptions[check_setting - 1].get_align(),
                                        font=(green_power_up_descriptions[check_setting - 1].get_font(),
                                        int(green_power_up_descriptions[check_setting - 1].get_size() * scale_factor), "normal"))
            elif self.catigory == "Red_Power_Up":
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                check_setting = config['Power_Up_Levels'].getint('red_power_up')

                self.panel_text.write("{}".format(red_power_up_descriptions[check_setting - 1].get_text()),
                                        align=red_power_up_descriptions[check_setting - 1].get_align(),
                                        font=(red_power_up_descriptions[check_setting - 1].get_font(),
                                        int(red_power_up_descriptions[check_setting - 1].get_size() * scale_factor), "normal"))

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
