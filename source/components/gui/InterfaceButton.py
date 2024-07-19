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
    File: InterfaceButton.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to buttons in Laser Fighter.
    This includes the button texture, the button text, and any button indicators.
    Every button will have its text turn yellow (except the shop slot) when the mouse is hovering over it.
    If the player clicks with the mouse while hovering over the button, it will executes that buttons function.
    This code is messy as every single buttons attributes and location need to be individually configured since there
        is a different texture for every single type of button and every button acts differently than the others.
    This class also contains the logic for the frame of the shop slot, which is a special type of button with extra
        visuals.
"""

import turtle
import configparser


class Button:
    """
        Represents a button object in Laser Fighter. When a button is clicked, its function will be executed.

        Attributes:
            button_frame (turtle.Turtle()): Sprite that represents the frame and shape of the button
            button_text (turtle.Turtle()): Displays the buttons text
            button_indicator (turtle.Turtle()): (Only for the toggle buttons on the settings screen) Displays the
                button indicator text
            type (string): Determines the type of button
            id (int): A unique identifier for the button to further determine and locate the button.
    """

    def __init__(self, type, id, scale_factor_x, scale_factor_y, fullscreen, page="None"):
        """
            Creates a button object of the specified type and id and spawns it on the screen.

            :param type: determines the type of button that this object is
            :type type: string

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.button_frame = turtle.Turtle()
        self.button_frame.color("#3D3D3D")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.button_frame.penup()
        # Title Screen whole button
        if type == "Title":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
            self.button_frame.shapesize(3.5 * scale_factor_y, 25 * scale_factor_x)
            if id == 1:
                self.button_frame.goto(0, 85 * scale_factor_y)
            elif id == 2:
                self.button_frame.goto(0, -5 * scale_factor_y)
            elif id == 3:
                self.button_frame.goto(0, -95 * scale_factor_y)
            elif id == 4:
                self.button_frame.goto(0, -275 * scale_factor_y)
        # Title screen small button
        elif type == "Title_Small":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small.gif")
            if id == 1:
                self.button_frame.goto(-130 * scale_factor_x, -185 * scale_factor_y)
            elif id == 2:
                self.button_frame.goto(130 * scale_factor_x, -185 * scale_factor_y)
        # In game main menu button
        elif type == "Game":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
            self.button_frame.goto(-537 * scale_factor_x, 339 * scale_factor_y)
        # The tabs in the shop
        elif type == "Tab":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Tab_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Tab.gif")
            if id < 5:
                self.button_frame.goto(-602.5 * scale_factor_x, (150 - (120 * (id - 1))) * scale_factor_y)
        # The item slots in the shop
        elif type == "Shop_Slot" or type == "Power_Up_Slot":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame.gif")
            if id < 5:
                self.button_frame.goto((-427 + (170 * (id - 1))) * scale_factor_x, 96 * scale_factor_y)
            elif 4 < id < 9:
                self.button_frame.goto((-427 + (170 * (id - 1 - 4))) * scale_factor_x, -94 * scale_factor_y)
        # Standard buttons on the settings and controls screen
        elif type == "Regular_Settings_And_Controls":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            if id == 1:
                self.button_frame.goto(315.5 * scale_factor_x, -285 * scale_factor_y)
            elif id == 2 or id == 3:
                self.button_frame.goto(315.5 * scale_factor_x, -205 * scale_factor_y)
        # Toggle buttons on the settings screen
        elif type == "Settings_Toggle":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            if id < 8:
                self.button_frame.goto(-325 * scale_factor_x, (195 - (80 * (id - 1))) * scale_factor_y)
            elif id == 8:
                self.button_frame.goto(315.5 * scale_factor_x, 195 * scale_factor_y)
            elif id == 9:
                self.button_frame.goto(315.5 * scale_factor_x, 115 * scale_factor_y)
            elif id == 10:
                self.button_frame.goto(315.5 * scale_factor_x, 35 * scale_factor_y)
            elif id == 11:
                self.button_frame.goto(315.5 * scale_factor_x, -45 * scale_factor_y)
            elif id == 12:
                self.button_frame.goto(315.5 * scale_factor_x, -125 * scale_factor_y)
        # Toggle buttons on the controls screen
        elif type == "Controls_Toggle":
            if fullscreen == 1:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
            else:
                self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            self.button_frame.goto(-325 * scale_factor_x, (195 - (80 * (id - 1))) * scale_factor_y)

        self.button_text = turtle.Turtle()
        self.button_text.color("white")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.button_text.penup()
        if type == "Title":
            self.button_text.goto(0, self.button_frame.ycor() - 22 * scale_factor_y)
        elif type == "Title_Small":
            self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor() - 22 * scale_factor_y)
        elif type == "Game":
            self.button_text.goto(-537 * scale_factor_x, 320 * scale_factor_y)
        elif type == "Tab":
            if id == 1:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon.gif")
            elif id == 2:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Gun/Player_Gun_Right_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Gun/Player_Gun_Right.gif")
            elif id == 3:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
            self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor())
        elif type == "Shop_Slot" or type == "Power_Up_Slot":
            if page == "Machine_Mode":
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon.gif")
            elif page == "Alien_Mode":
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon.gif")
            elif page == "Power_Ups":
                if self.id == 1:
                    if fullscreen == 1:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon_Scaled.gif")
                    else:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon.gif")
                elif self.id == 2:
                    if fullscreen == 1:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon_Scaled.gif")
                    else:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon.gif")
                elif self.id == 3:
                    if fullscreen == 1:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon_Scaled.gif")
                    else:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon.gif")
                elif self.id == 4:
                    if fullscreen == 1:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon_Scaled.gif")
                    else:
                        self.button_text.shape("Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon.gif")
            self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor() + 20 * scale_factor_y)
        elif type == "Regular_Settings_And_Controls":
            self.button_text.goto(315.5 * scale_factor_x, self.button_frame.ycor() - 22 * scale_factor_y)
        elif type == "Settings_Toggle" or type == "Controls_Toggle":
            self.button_text.goto(self.button_frame.xcor() - 30 * scale_factor_x, self.button_frame.ycor() - 22 * scale_factor_y)
        if type != "Shop_Slot" and type != "Tab":
            self.button_text.hideturtle()

        # Create the indicators for the toggle buttons on the settings screen
        if type == "Settings_Toggle":
            self.button_indicator = turtle.Turtle()
            # Ensure that the turtle does not draw lines on the screen while moving
            self.button_indicator.penup()
            if id == 1:
                self.button_indicator.goto(-177 * scale_factor_x, 173 * scale_factor_y)
            elif id == 2:
                self.button_indicator.goto(-79 * scale_factor_x, 93 * scale_factor_y)
            elif id == 3:
                self.button_indicator.goto(-88 * scale_factor_x, 13 * scale_factor_y)
            elif id == 4:
                self.button_indicator.goto(-111 * scale_factor_x, -67 * scale_factor_y)
            elif id == 5:
                self.button_indicator.goto(-121 * scale_factor_x, -147 * scale_factor_y)
            elif id == 6:
                self.button_indicator.goto(-132 * scale_factor_x, -227 * scale_factor_y)
            elif id == 7:
                self.button_indicator.goto(-143 * scale_factor_x, -307 * scale_factor_y)
            elif id == 8:
                self.button_indicator.goto(561.5 * scale_factor_x, 173 * scale_factor_y)
            elif id == 9:
                self.button_indicator.goto(552.5 * scale_factor_x, 93 * scale_factor_y)
            elif id == 10:
                self.button_indicator.goto(530.5 * scale_factor_x, 13 * scale_factor_y)
            elif id == 11:
                self.button_indicator.goto(440.5 * scale_factor_x, -67 * scale_factor_y)
            elif id == 12:
                self.button_indicator.goto(384.5 * scale_factor_x, -147 * scale_factor_y)
            self.button_indicator.hideturtle()

            self.indicator = 1
        # Create the locks for the slots in the shop
        elif type == "Shop_Slot" or type == "Power_Up_Slot":
            self.button_indicator = turtle.Turtle()
            # Ensure that the turtle does not draw lines on the screen while moving
            self.button_indicator.penup()
            self.button_indicator.color("white")
            if fullscreen == 1:
                self.button_indicator.shape("Textures/GUI/Locked_Scaled.gif")
            else:
                self.button_indicator.shape("Textures/GUI/Locked.gif")
            self.button_indicator.goto(self.button_frame.xcor(), self.button_frame.ycor() + 20 * scale_factor_y)

            self.indicator = 1
            self.indicator_toggled = 0
        else:
            self.indicator = 0

        self.type = type
        self.id = id

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.button_frame.clear()
        self.button_text.clear()
        del self.button_frame
        del self.button_text

    def reinstate_to_title(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a title screen button based on the id.

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
        self.button_frame.shapesize(3.5 * scale_factor_y, 25 * scale_factor_x)
        if id == 1:
            self.button_frame.goto(0, 85 * scale_factor_y)
        elif id == 2:
            self.button_frame.goto(0, -5 * scale_factor_y)
        elif id == 3:
            self.button_frame.goto(0, -95 * scale_factor_y)
        elif id == 4:
            self.button_frame.goto(0, -275 * scale_factor_y)
        self.button_frame.color("white")
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(0, self.button_frame.ycor() - 22 * scale_factor_y)

        # Set the type to "Title"
        self.type = "Title"
        self.id = id

    def reinstate_to_title_small(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a small title screen button based on the id.

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small.gif")
        if id == 1:
            self.button_frame.goto(-130 * scale_factor_x, -185 * scale_factor_y)
        elif id == 2:
            self.button_frame.goto(130 * scale_factor_x, -185 * scale_factor_y)
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor() - 22 * scale_factor_y)

        # Set the type to "Title Small"
        self.type = "Title_Small"
        self.id = id

    def reinstate_to_game(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a game screen main menu button.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
        self.button_frame.goto(-537 * scale_factor_x, 339 * scale_factor_y)
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(-537 * scale_factor_x, 320 * scale_factor_y)

        # Set the type to "Game"
        self.type = "Game"
        self.id = 1

    def reinstate_to_tab(self, id, scale_factor_x, scale_factor_y, fullscreen):
        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Tab_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Tab.gif")
        if id < 5:
            self.button_frame.goto(-602.5 * scale_factor_x, (150 - (120 * (id - 1))) * scale_factor_y)
        self.button_frame.showturtle()

        if id == 1:
            if fullscreen == 1:
                self.button_text.shape("Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon_Scaled.gif")
            else:
                self.button_text.shape("Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon.gif")
        elif id == 2:
            if fullscreen == 1:
                self.button_text.shape("Textures/Gun/Player_Gun_Right_Scaled.gif")
            else:
                self.button_text.shape("Textures/Gun/Player_Gun_Right.gif")
        elif id == 3:
            if fullscreen == 1:
                self.button_text.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif")
            else:
                self.button_text.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
        self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor())
        self.button_text.showturtle()

        # Set the type to "Tab"
        self.type = "Tab"
        self.id = id

    def reinstate_to_shop_slot(self, id, scale_factor_x, scale_factor_y, fullscreen, page):
        self.reinstate_to_slot(id, scale_factor_x, scale_factor_y, fullscreen, page=page)

        # Set the type to "Shop Slot"
        self.type = "Shop_Slot"
        self.id = id

    def reinstate_to_power_up_slot(self, id, scale_factor_x, scale_factor_y, fullscreen):
        self.reinstate_to_slot(id, scale_factor_x, scale_factor_y, fullscreen, "Power_Ups")

        # Set the type to "Shop Slot"
        self.type = "Power_Up_Slot"
        self.id = id

    def reinstate_to_slot(self, id, scale_factor_x, scale_factor_y, fullscreen, page="None"):
        """
            Reuses the existing button sprite to spawn a shop slot and place it in a location based on the id.

            :param id: A unique identifier for the shop slots location
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame.gif")
        if id < 5:
            self.button_frame.goto((-427 + (170 * (id - 1))) * scale_factor_x, 96 * scale_factor_y)
        elif 4 < id < 9:
            self.button_frame.goto((-427 + (170 * (id - 1 - 4))) * scale_factor_x, -94 * scale_factor_y)
        self.button_frame.showturtle()

        if page == "Machine_Mode":
            if fullscreen == 1:
                self.button_text.shape("Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon_Scaled.gif")
            else:
                self.button_text.shape("Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon.gif")
        elif page == "Alien_Mode":
            if fullscreen == 1:
                self.button_text.shape("Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon_Scaled.gif")
            else:
                self.button_text.shape("Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon.gif")
        elif page == "Power_Ups":
            if self.id == 1:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon.gif")
            elif self.id == 2:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon.gif")
            elif self.id == 3:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon.gif")
            elif self.id == 4:
                if fullscreen == 1:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon_Scaled.gif")
                else:
                    self.button_text.shape("Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon.gif")
        self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor() + 20 * scale_factor_y)
        self.button_text.showturtle()

        # If the button indicator does not already exist, create one
        if self.indicator == 0:
            self.button_indicator = turtle.Turtle()
            # Ensure that the turtle does not draw lines on the screen while moving
            self.button_indicator.penup()
            self.indicator = 1
        if fullscreen == 1:
            self.button_indicator.shape("Textures/GUI/Locked_Scaled.gif")
        else:
            self.button_indicator.shape("Textures/GUI/Locked.gif")
        self.button_indicator.color("white")
        self.button_indicator.goto(self.button_frame.xcor(), self.button_frame.ycor() + 20 * scale_factor_y)
        self.indicator_toggled = 0

    def reinstate_to_regular_settings_and_controls(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a standard settings and controls button based on the id.

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        if id == 1:
            self.button_frame.goto(315.5 * scale_factor_x, -285 * scale_factor_y)
        elif id == 2 or id == 3:
            self.button_frame.goto(315.5 * scale_factor_x, -205 * scale_factor_y)
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(315.5 * scale_factor_x, self.button_frame.ycor() - 22 * scale_factor_y)

        # Set the type to "Regular Settings And Controls"
        self.type = "Regular_Settings_And_Controls"
        self.id = id

    def reinstate_to_settings_toggle(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a settings toggle button based on the id.

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        if id < 8:
            self.button_frame.goto(-325 * scale_factor_x, (195 - (80 * (id - 1))) * scale_factor_y)
        elif id == 8:
            self.button_frame.goto(315.5 * scale_factor_x, 195 * scale_factor_y)
        elif id == 9:
            self.button_frame.goto(315.5 * scale_factor_x, 115 * scale_factor_y)
        elif id == 10:
            self.button_frame.goto(315.5 * scale_factor_x, 35 * scale_factor_y)
        elif id == 11:
            self.button_frame.goto(315.5 * scale_factor_x, -45 * scale_factor_y)
        elif id == 12:
            self.button_frame.goto(315.5 * scale_factor_x, -125 * scale_factor_y)
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(self.button_frame.xcor() - 30 * scale_factor_x, self.button_frame.ycor() - 22 * scale_factor_y)

        # If the button indicator does not already exist, create one
        if self.indicator == 0:
            self.button_indicator = turtle.Turtle()
            self.button_indicator.penup()
            self.button_indicator.hideturtle()
            self.indicator = 1

        if id == 1:
            self.button_indicator.goto(-177 * scale_factor_x, 173 * scale_factor_y)
        elif id == 2:
            self.button_indicator.goto(-79 * scale_factor_x, 93 * scale_factor_y)
        elif id == 3:
            self.button_indicator.goto(-88 * scale_factor_x, 13 * scale_factor_y)
        elif id == 4:
            self.button_indicator.goto(-111 * scale_factor_x, -67 * scale_factor_y)
        elif id == 5:
            self.button_indicator.goto(-121 * scale_factor_x, -147 * scale_factor_y)
        elif id == 6:
            self.button_indicator.goto(-132 * scale_factor_x, -227 * scale_factor_y)
        elif id == 7:
            self.button_indicator.goto(-143 * scale_factor_x, -307 * scale_factor_y)
        elif id == 8:
            self.button_indicator.goto(561.5 * scale_factor_x, 173 * scale_factor_y)
        elif id == 9:
            self.button_indicator.goto(552.5 * scale_factor_x, 93 * scale_factor_y)
        elif id == 10:
            self.button_indicator.goto(530.5 * scale_factor_x, 13 * scale_factor_y)
        elif id == 11:
            self.button_indicator.goto(440.5 * scale_factor_x, -67 * scale_factor_y)
        elif id == 12:
            self.button_indicator.goto(384.5 * scale_factor_x, -147 * scale_factor_y)

        # Set the type to "Settings_Toggle"
        self.type = "Settings_Toggle"
        self.id = id

    def reinstate_to_controls_toggle(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing button sprite to spawn a controls toggle button based on the id.

            :param id: A unique identifier for the button
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
        else:
            self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        self.button_frame.goto(-325 * scale_factor_x, (195 - (80 * (id - 1))) * scale_factor_y)
        self.button_frame.showturtle()

        self.button_text.color("white")
        self.button_text.goto(self.button_frame.xcor(), self.button_frame.ycor() - 22 * scale_factor_y)

        # Set the type to "Controls_Toggle"
        self.type = "Controls_Toggle"
        self.id = id

    def get_button_frame(self):
        """
            Returns the button frame sprite so its class attributes can be accessed

            :return: button_frame: the button frame sprite
            :type: turtle.Turtle()
        """

        return self.button_frame

    def get_button_text(self):
        """
            Returns the button text sprite so its class attributes can be accessed

            :return: button_text: the button text sprite
            :type: turtle.Turtle()
        """

        return self.button_text

    def get_button_indicator(self):
        """
            Returns the button indicator sprite so its class attributes can be accessed

            :return: button_indicator: the button indicator sprite
            :type: turtle.Turtle()
        """

        # If the button indicator exists
        if self.indicator == 1:
            return self.button_indicator

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def get_indicator_toggled(self):
        if self.type == "Shop_Slot":
            return self.indicator_toggled

    def remove(self):
        """
            Removes the button sprites from the screen and resets its attributes.

            :return: None
        """

        self.button_frame.hideturtle()
        self.button_text.hideturtle()
        self.button_text.clear()
        # If the button indicator exists, also remove it from the screen.
        if self.indicator == 1:
            self.button_indicator.hideturtle()
            self.button_indicator.clear()

    def write_lines(self, scale_factor):
        """
            Writes the text for all the regular buttons on the screen and then updates the screen with that text.

            :param scale_factor: The scale factor for fullscreen mode
            :type scale_factor: float

            :return: None
        """

        # Clears the existing text
        if self.type != "Shop_Slot":
            self.button_text.clear()
        # Writes new text based on the button type and id
        if self.type == "Title":
            if self.id == 1:
                self.button_text.write("Machine Mode", align="center", font=("Courier", int(30 * scale_factor), "normal"))
            elif self.id == 2:
                self.button_text.write("Alien Mode", align="center", font=("Courier", int(30 * scale_factor), "normal"))
            elif self.id == 3:
                self.button_text.write("Coin Shop", align="center", font=("Courier", int(30 * scale_factor), "normal"))
            elif self.id == 4:
                self.button_text.write("Exit", align="center", font=("Courier", int(30 * scale_factor), "normal"))
        elif self.type == "Title_Small":
            if self.id == 1:
                self.button_text.write("Settings", align="center",  font=("Courier", int(30 * scale_factor), "normal"))
            elif self.id == 2:
                self.button_text.write("Stats", align="center",  font=("Courier", int(30 * scale_factor), "normal"))
        elif self.type == "Game":
            self.button_text.write("Main Menu", align="center", font=("Courier", int(24 * scale_factor), "normal"))
        elif self.type == "Regular_Settings_And_Controls":
            if self.id == 1:
                self.button_text.write("Main Menu", align="center", font=("Courier", int(28 * scale_factor), "bold"))
            elif self.id == 2:
                self.button_text.write("Controls", align="center", font=("Courier", int(28 * scale_factor), "bold"))
            elif self.id == 3:
                self.button_text.write("Settings", align="center", font=("Courier", int(28 * scale_factor), "bold"))
        elif self.type == "Settings_Toggle":
            if self.id == 1:
                self.button_text.write("Button Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 2:
                self.button_text.write("Player Shooting Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 3:
                self.button_text.write("Enemy Shooting Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 4:
                self.button_text.write("Player Death Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 5:
                self.button_text.write("Enemy Death Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 6:
                self.button_text.write("Player Hit Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 7:
                self.button_text.write("Enemy Hit Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 8:
                self.button_text.write("Power Up Pickup Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 9:
                self.button_text.write("Power Up Spawn Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 10:
                self.button_text.write("Coin Pick Up Sound:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 11:
                self.button_text.write("Fullscreen:", align="center", font=("Courier", int(28 * scale_factor), "normal"))
            elif self.id == 12:
                self.button_text.write("VSync:", align="center", font=("Courier", int(28 * scale_factor), "normal"))

    def write_control(self, go_right_key, go_left_key, shoot_key, jump_key, scale_factor):
        """
            Writes the text and indicators for the control toggle buttons and then updates the screen with that text.

            :param go_right_key: Stores the current keybind for moving right
            :type go_right_key: string

            :param go_left_key: Stores the current keybind for moving left
            :type go_left_key: string

            :param shoot_key: Stores the current keybind for shooting the laser in both modes
            :type shoot_key: string

            :param jump_key: Stores the current keybind for jumping
            :type jump_key: string

            :param scale_factor: The scale factor for fullscreen mode
            :type scale_factor: float

            :return: None
        """

        # Clears the existing text
        self.button_text.clear()
        # Writes new text based on the button id
        if self.id == 1:
            self.button_text.write("Go Right: " + go_right_key, align="center", font=("Courier", int(28 * scale_factor), "normal"))
        elif self.id == 2:
            self.button_text.write("Go Left: " + go_left_key, align="center", font=("Courier", int(28 * scale_factor), "normal"))
        elif self.id == 3:
            self.button_text.write("Shoot: " + shoot_key, align="center", font=("Courier", int(28 * scale_factor), "normal"))
        elif self.id == 4:
            self.button_text.write("Jump: " + jump_key, align="center", font=("Courier", int(28 * scale_factor), "normal"))

    def write_indicator(self, setting, scale_factor):
        """
            Writes the text for the button indicators tied to the settings toggle buttons.

            :param setting: Stores the current configuration for the given setting.
            :type setting: int

            :param scale_factor: The scale factor for fullscreen mode
            :type scale_factor: float

            :return: None
        """

        if self.type == "Settings_Toggle":
            if setting == 1:
                self.button_indicator.color("green")
                self.button_indicator.clear()
                self.button_indicator.write("On", align="center", font=("Courier", int(28 * scale_factor), "bold"))
            else:
                self.button_indicator.color("red")
                self.button_indicator.clear()
                self.button_indicator.write("Off", align="center", font=("Courier", int(28 * scale_factor), "bold"))
        elif self.type == "Power_Up_Slot":
            if setting != 0:
                self.button_indicator.clear()
                self.button_indicator.write("Level {}".format(setting), align="center", font=("Courier", int(18 * scale_factor), "normal"))

    def write_fullscreen_indicator(self, setting, fullscreen_toggled, scale_factor):
        """
            Writes the text for the fullscreen toggle button indicator specifically since it requires extra steps.

            :param setting: Stores the current configuration for the given setting.
            :type setting: int

            :param fullscreen_toggled: Determines if a switch to the toggle has been made or not.
            :type fullscreen_toggled: int

            :param scale_factor: The scale factor for fullscreen mode
            :type scale_factor: float

            :return: None
        """

        if fullscreen_toggled == 1:
            # Display "RST" in yellow for the indicator if an in-game switch has been made
            self.button_indicator.color("yellow")
            self.button_indicator.clear()
            self.button_indicator.write("RST", align="center", font=("Courier", int(28 * scale_factor), "bold"))
        else:
            # No in game switch has been made, display the indicator like normal
            if setting == 1:
                self.button_indicator.color("green")
                self.button_indicator.clear()
                self.button_indicator.write("On", align="center", font=("Courier", int(28 * scale_factor), "bold"))
            else:
                self.button_indicator.color("red")
                self.button_indicator.clear()
                self.button_indicator.write("Off", align="center", font=("Courier", int(28 * scale_factor), "bold"))

    def toggle_indicator(self, check_value):
        if check_value == 0:
            self.button_indicator.showturtle()
            self.indicator_toggled = 1
        else:
            self.button_indicator.hideturtle()
            self.indicator_toggled = 0

    def set_indicator_location(self, scale_factor_y):
        if self.indicator_toggled == 1:
            self.button_indicator.goto(self.button_frame.xcor(), self.button_frame.ycor() + 20 * scale_factor_y)
        else:
            self.button_indicator.goto(self.button_frame.xcor(), self.button_frame.ycor() - 45 * scale_factor_y)

    def update_highlight(self, x, y, scale_factor_x, scale_factor_y, fullscreen):
        """
            Used to change the color of the buttons text when the user decides to hover their mouse over the area
                that the  button takes up.

            :param x: The current x-coordinate of the cursor
            :type x: int

            :param y: The current y-coordinate of the cursor
            :type y: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if self.type == "Title":
            if self.id == 1:
                if 388 * scale_factor_x < x < 890 * scale_factor_x and 239 * scale_factor_y < y < 311 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
            elif self.id == 2:
                if 388 * scale_factor_x < x < 890 * scale_factor_x and 329 * scale_factor_y < y < 401 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
            elif self.id == 3:
                if 388 * scale_factor_x < x < 890 * scale_factor_x and 419 * scale_factor_y < y < 491 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
            elif self.id == 4:
                if 388 * scale_factor_x < x < 890 * scale_factor_x and 599 * scale_factor_y < y < 671 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button.gif")
        elif self.type == "Title_Small":
            if self.id == 1:
                if 388 * scale_factor_x < x < 630 * scale_factor_x and 509 * scale_factor_y < y < 581 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small.gif")
            elif self.id == 2:
                if 648 * scale_factor_x < x < 890 * scale_factor_x and 509 * scale_factor_y < y < 581 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Title_Screen_Button_Small.gif")
        elif self.type == "Game":
            if 6 * scale_factor_x < x < 197 * scale_factor_x and 5 * scale_factor_y < y < 37 * scale_factor_y:
                self.button_frame.color("yellow")
                if fullscreen == 1:
                    self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main_Highlighted_Scaled.gif")
                else:
                    self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main_Highlighted.gif")
                return 1
            else:
                self.button_frame.color("white")
                if fullscreen == 1:
                    self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main_Scaled.gif")
                else:
                    self.button_frame.shape("Textures/Buttons/Main_Menu_Button_Main.gif")
                return 0
        elif self.type == "Tab":
            if 0 * scale_factor_x < x < 75 * scale_factor_x and (159 + (120 * (self.id - 1))) * scale_factor_y < y < (259 + (120 * (self.id - 1))) * scale_factor_y:
                self.button_frame.color("yellow")
                if fullscreen == 1:
                    self.button_frame.shape("Textures/Buttons/Tab_Highlighted_Scaled.gif")
                else:
                    self.button_frame.shape("Textures/Buttons/Tab_Highlighted.gif")
            else:
                self.button_frame.color("white")
                if fullscreen == 1:
                    self.button_frame.shape("Textures/Buttons/Tab_Scaled.gif")
                else:
                    self.button_frame.shape("Textures/Buttons/Tab.gif")
        elif self.type == "Shop_Slot" or self.type == "Power_Up_Slot":
            if self.id < 5:
                if (137 + (170 * (self.id - 1))) * scale_factor_x < x < (288 + (170 * (self.id - 1))) * scale_factor_x and 178 * scale_factor_y < y < 349 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame.gif")
            elif 4 < self.id < 9:
                if (137 + (170 * (self.id - 1 - 4))) * scale_factor_x < x < (288 + (170 * (self.id - 1 - 4))) * scale_factor_x and 368 * scale_factor_y < y < 539 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Highlighted.gif")
                else:
                    self.button_frame.color("White")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Inventory_Slot_Frame.gif")
        elif self.type == "Regular_Settings_And_Controls":
            if self.id == 1:
                if 669 * scale_factor_x < x < 1240 * scale_factor_x and 614 * scale_factor_y < y < 675 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                    return 1
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
                    return 0
            elif self.id == 2 or self.id == 3:
                if 669 * scale_factor_x < x < 1240 * scale_factor_x and 534 * scale_factor_y < y < 595 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        elif self.type == "Settings_Toggle":
            if self.id < 8:
                if 28 * scale_factor_x < x < 599 * scale_factor_x and (134 + (80 * (self.id - 1))) * scale_factor_y < y < (195 + (80 * (self.id - 1))) * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 8:
                if 671 * scale_factor_x < x < 1243 * scale_factor_x and 134 * scale_factor_y < y < 195 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 9:
                if 671 * scale_factor_x < x < 1243 * scale_factor_x and 214 * scale_factor_y < y < 275 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 10:
                if 671 * scale_factor_x < x < 1243 * scale_factor_x and 294 * scale_factor_y < y < 355 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 11:
                if 671 * scale_factor_x < x < 1243 * scale_factor_x and 374 * scale_factor_y < y < 435 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 12:
                if 671 * scale_factor_x < x < 1243 * scale_factor_x and 454 * scale_factor_y < y < 515 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
        elif self.type == "Controls_Toggle":
            if self.id == 1:
                if 28 * scale_factor_x < x < 599 * scale_factor_x and 134 * scale_factor_y < y < 195 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 2:
                if 28 * scale_factor_x < x < 599 * scale_factor_x and 214 * scale_factor_y < y < 275 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 3:
                if 28 * scale_factor_x < x < 599 * scale_factor_x and 294 * scale_factor_y < y < 355 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")
            elif self.id == 4:
                if 28 * scale_factor_x < x < 599 * scale_factor_x and 374 * scale_factor_y < y < 435 * scale_factor_y:
                    self.button_frame.color("yellow")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif")
                else:
                    self.button_frame.color("white")
                    if fullscreen == 1:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button_Scaled.gif")
                    else:
                        self.button_frame.shape("Textures/Buttons/Settings_And_Controls_Button.gif")

    def update_controls_text_color(self, alert):
        """
            Used to change the color of the control toggle buttons text when the user decides to hover their mouse over
                the area that the  button takes up.

            :param alert: Used to determine if there is a keybind conflict with the control setting
                for this buttons control
            :type alert: int

            :return: None
        """

        if self.id == 1:
            # If the there is a keybind conflict, use red and orange as the colors rather than yellow and white
            if alert == 1:
                self.button_text.color("red")
            else:
                self.button_text.color("white")
        elif self.id == 2:
            # If the there is a keybind conflict, use red and orange as the colors rather than yellow and white
            if alert == 2:
                self.button_text.color("red")
            else:
                self.button_text.color("white")
        elif self.id == 3:
            # If the there is a keybind conflict, use red and orange as the colors rather than yellow and white
            if alert == 3:
                self.button_text.color("red")
            else:
                self.button_text.color("white")
        elif self.id == 4:
            # If the there is a keybind conflict, use red and orange as the colors rather than yellow and white
            if alert == 4:
                self.button_text.color("red")
            else:
                self.button_text.color("white")

    def click_button(self):
        """
            Returns the required attributes of the shop slot to determine if it has been clicked or not.
            This works differently than the button because the text is not highlighted yellow, rather, the entire
                button is.

            :return: button_color: the current color of the buttons frame
            :type: string

            :return: type: The type of button that the current button is
            :type: string

            :return: id: The unique identifier for the current button
            :type: int
        """

        button_color = self.button_frame.fillcolor()
        return button_color, self.type, self.id
