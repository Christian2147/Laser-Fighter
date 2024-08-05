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
from setup.ConfigurationSetup import shop_config
from setup.data.MilestoneMessages import MILESTONE_1_MESSAGE
from setup.data.MilestoneMessages import MILESTONE_2_MESSAGE
from setup.data.MilestoneMessages import MILESTONE_3_MESSAGE
from setup.data.ShopDescriptions import MAIN_DESCRIPTION
from setup.data.ShopDescriptions import MACHINE_DESCRIPTIONS
from setup.data.ShopDescriptions import ALIEN_DESCRIPTIONS
from setup.data.ShopDescriptions import YELLOW_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import BLUE_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import GREEN_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptions import RED_POWER_UP_DESCRIPTIONS
from setup.TextureSetup import SIDE_PANEL_SHOP_TEXTURE
from setup.TextureSetup import MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import MACHINE_WASHER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_INCINERATOR_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_BLACK_HOLE_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_STAR_KILLER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_COOKER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import POISON_DART_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import METEOR_GUN_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import SUPERNOVA_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import BLUE_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import GREEN_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import RED_POWER_UP_DISPLAY_ICON_TEXTURE


class Panel:
    """
        Represents the panel in Laser Fighter for displaying important information.

        Attributes:
            panel (turtle.Turtle()): The sprite that represents the frame of the panel
            panel_text (turtle.Turtle()): The sprite that displays the panels text
            panel_indicator (turtle.Turtle()): The sprite that displays the visual element on the panel

            type (string): The type of panel generated (depending on the current screen)
            category (string): The current type of description being displayed
            id (int): The id for the specific description being displayed

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, scale_factor, scale_factor_x, scale_factor_y):
        """
            Creates a panel object to be displayed on the screen.

            :param type: The type of panel to create
            :type type: string

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.panel = turtle.Turtle()
        self.panel.color("#3D3D3D")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.panel.penup()
        if type == "Shop":
            self.panel.shape(SIDE_PANEL_SHOP_TEXTURE)
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
        self.category = "Welcome"
        self.id = 1

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

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

    def reinstate_to_shop(self):
        """
            Reuses the existing sprite to create a side panel in the shop.

            :return: None
        """

        self.panel.shape(SIDE_PANEL_SHOP_TEXTURE)
        self.panel.goto(450 * self.scale_factor_x, 0)
        self.panel.showturtle()

        self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 290 * self.scale_factor_y)

        self.panel_indicator.goto(self.panel.xcor(), self.panel.ycor() + 190 * self.scale_factor_y)

        # Set it to the welcome message
        self.type = "Shop"
        self.category = "Welcome"
        self.id = 1

    def get_panel_frame(self):
        """
            Returns the panel frame so that its class attributes can be accessed.

            :return: panel_frame: the panel frame
            :type: turtle.Turtle()
        """

        return self.panel

    def get_panel_text(self):
        """
            Returns the panel text so that its class attributes can be accessed.

            :return: panel_text: the panel text
            :type: turtle.Turtle()
        """

        return self.panel_text

    def get_panel_indicator(self):
        """
            Returns the panel indicator so that its class attributes can be accessed.

            :return: panel_indicator: the panel indicator
            :type: turtle.Turtle()
        """

        return self.panel_indicator

    def get_panel_id(self):
        """
            Returns the panel id so that its class attributes can be accessed.

            :return: id: the panel id
            :type: int
        """

        return self.id

    def set_panel_text(self, new_category, new_id):
        """
            Sets the panel text to show the information of the shop slot specified by the new category and the new id.

            :param new_category: The new category to be displayed (Machine Mode, Alien Mode, Power Ups)
            :type new_category: string

            :param new_id: The new id of the slot to display
            :type new_id: int

            :return: None
        """

        self.category = new_category
        self.id = new_id
        if self.category == "Welcome":
            self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 290 * self.scale_factor_y)
        elif self.category == "Alien_Mode":
            self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 55 * self.scale_factor_y)
        else:
            self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 40 * self.scale_factor_y)

    def remove(self):
        """
            Removes the panel from the screen and resets its attributes.

            :return: None
        """

        self.panel.hideturtle()
        self.panel_text.hideturtle()
        self.panel_text.clear()
        self.panel_indicator.hideturtle()

    def write_text(self):
        """
            Writes the panels text based on the category of the slot to display and the id of the slot to display.
            These descriptions are extracted from ShopDescriptions.py

            :return: None
        """

        # Clears the existing text
        self.panel_text.clear()

        # Writes new text based on the panel type and id of the text
        if self.type == "Shop":
            if self.category == "Welcome":
                self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 290 * self.scale_factor_y)
            elif self.category == "Alien_Mode":
                self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 55 * self.scale_factor_y)
            else:
                self.panel_text.goto(self.panel.xcor() - 155 * self.scale_factor_x, self.panel.ycor() + 40 * self.scale_factor_y)
            if self.category == "Welcome":
                for i in range(MAIN_DESCRIPTION[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(MAIN_DESCRIPTION[self.id - 1].get_text()[i]),
                                            align=MAIN_DESCRIPTION[self.id - 1].get_align(),
                                            font=(MAIN_DESCRIPTION[self.id - 1].get_font(),
                                            int(MAIN_DESCRIPTION[self.id - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 36 * self.scale_factor_y)
            elif self.category == "Machine_Mode":
                for i in range(MACHINE_DESCRIPTIONS[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(MACHINE_DESCRIPTIONS[self.id - 1].get_text()[i]),
                                            align=MACHINE_DESCRIPTIONS[self.id - 1].get_align(),
                                            font=(MACHINE_DESCRIPTIONS[self.id - 1].get_font(),
                                            int(MACHINE_DESCRIPTIONS[self.id - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 24 * self.scale_factor_y)
            elif self.category == "Alien_Mode":
                for i in range(ALIEN_DESCRIPTIONS[self.id - 1].get_length()):
                    self.panel_text.write("{}".format(ALIEN_DESCRIPTIONS[self.id - 1].get_text()[i]),
                                            align=ALIEN_DESCRIPTIONS[self.id - 1].get_align(),
                                            font=(ALIEN_DESCRIPTIONS[self.id - 1].get_font(),
                                            int(ALIEN_DESCRIPTIONS[self.id - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 24 * self.scale_factor_y)
            # Display the description of the next level up of the given power up
            elif self.category == "Yellow_Power_Up":
                check_setting = shop_config.yellow_power_up_level

                for i in range(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * self.scale_factor_y)
            elif self.category == "Blue_Power_Up":
                check_setting = shop_config.blue_power_up_level

                for i in range(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * self.scale_factor_y)
            elif self.category == "Green_Power_Up":
                check_setting = shop_config.green_power_up_level

                for i in range(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * self.scale_factor_y)
            elif self.category == "Red_Power_Up":
                check_setting = shop_config.red_power_up_level

                for i in range(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_length()):
                    self.panel_text.write("{}".format(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_text()[i]),
                                            align=RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_align(),
                                            font=(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_font(),
                                            int(RED_POWER_UP_DESCRIPTIONS[check_setting - 1].get_size() * self.scale_factor), "normal"))
                    self.panel_text.goto(self.panel_text.xcor(), self.panel_text.ycor() - 30 * self.scale_factor_y)
        # Set the panel indicator after the text is updated
        self.set_indicator()

    def set_indicator(self):
        """
            Sets the panel indicator (Icon) based on the category (Page of the slot) and the id (Id of the slot).

            :return: None
        """

        if self.category == "Welcome":
            # Do not need the panel indicator if the welcome message is being displayed.
            self.panel_indicator.hideturtle()
        else:
            if self.category == "Machine_Mode":
                if self.id == 1:
                    self.panel_indicator.shape(MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE)
                elif self.id == 2:
                    self.panel_indicator.shape(MACHINE_WASHER_DISPLAY_ICON_TEXTURE)
                elif self.id == 3:
                    self.panel_indicator.shape(THE_INCINERATOR_DISPLAY_ICON_TEXTURE)
                elif self.id == 4:
                    self.panel_indicator.shape(THE_BLACK_HOLE_DISPLAY_ICON_TEXTURE)
                elif self.id == 5:
                    self.panel_indicator.shape(THE_STAR_KILLER_DISPLAY_ICON_TEXTURE)
            elif self.category == "Alien_Mode":
                if self.id == 1:
                    self.panel_indicator.shape(ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE)
                elif self.id == 2:
                    self.panel_indicator.shape(THE_COOKER_DISPLAY_ICON_TEXTURE)
                elif self.id == 3:
                    self.panel_indicator.shape(POISON_DART_DISPLAY_ICON_TEXTURE)
                elif self.id == 4:
                    self.panel_indicator.shape(METEOR_GUN_DISPLAY_ICON_TEXTURE)
                elif self.id == 5:
                    self.panel_indicator.shape(SUPERNOVA_DISPLAY_ICON_TEXTURE)
            elif self.category == "Yellow_Power_Up":
                self.panel_indicator.shape(YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Blue_Power_Up":
                self.panel_indicator.shape(BLUE_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Green_Power_Up":
                self.panel_indicator.shape(GREEN_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Red_Power_Up":
                self.panel_indicator.shape(RED_POWER_UP_DISPLAY_ICON_TEXTURE)
            self.panel_indicator.showturtle()
