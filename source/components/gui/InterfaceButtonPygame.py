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

import pygame
from setup.TextureSetup import TITLE_SCREEN_BUTTON_TEXTURE
from setup.TextureSetup import TITLE_SCREEN_BUTTON_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import TITLE_SCREEN_BUTTON_SMALL_TEXTURE
from setup.TextureSetup import TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import SETTINGS_AND_CONTROLS_BUTTON_TEXTURE
from setup.TextureSetup import SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import MAIN_MENU_BUTTON_MAIN_TEXTURE
from setup.TextureSetup import MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import TAB_TEXTURE
from setup.TextureSetup import TAB_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import INVENTORY_SLOT_FRAME_TEXTURE
from setup.TextureSetup import INVENTORY_SLOT_FRAME_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import BUY_BUTTON_TEXTURE
from setup.TextureSetup import BUY_BUTTON_HIGHLIGHTED_TEXTURE
from setup.TextureSetup import MACHINE_MODE_TAB_ICON_TEXTURE
from setup.TextureSetup import GADGETS_TAB_ICON_TEXTURE
from setup.TextureSetup import PLAYER_GUN_RIGHT_TEXTURE
from setup.TextureSetup import YELLOW_LIGHTNING_POWER_UP_TEXTURE
from setup.TextureSetup import LOCKED_TEXTURE
from setup.TextureSetup import COIN_INDICATOR_TEXTURE
from setup.TextureSetup import MACHINE_DEFAULT_SLOT_ICON_TEXTURE
from setup.TextureSetup import MACHINE_WASHER_SLOT_ICON_TEXTURE
from setup.TextureSetup import THE_INCINERATOR_SLOT_ICON_TEXTURE
from setup.TextureSetup import THE_BLACK_HOLE_SLOT_ICON_TEXTURE
from setup.TextureSetup import THE_STAR_KILLER_SLOT_ICON_TEXTURE
from setup.TextureSetup import ALIEN_DEFAULT_SLOT_ICON_TEXTURE
from setup.TextureSetup import THE_COOKER_SLOT_ICON_TEXTURE
from setup.TextureSetup import POISON_DART_SLOT_ICON_TEXTURE
from setup.TextureSetup import METEOR_GUN_SLOT_ICON_TEXTURE
from setup.TextureSetup import SUPERNOVA_SLOT_ICON_TEXTURE
from setup.TextureSetup import YELLOW_POWER_UP_SLOT_ICON_TEXTURE
from setup.TextureSetup import BLUE_POWER_UP_SLOT_ICON_TEXTURE
from setup.TextureSetup import GREEN_POWER_UP_SLOT_ICON_TEXTURE
from setup.TextureSetup import RED_POWER_UP_SLOT_ICON_TEXTURE
from setup.TextureSetup import COIN_MAGNET_SLOT_ICON_TEXTURE
from setup.TextureSetup import ARMOR_SLOT_ICON_TEXTURE
from setup.TextureSetup import THORNS_SLOT_ICON_TEXTURE
from setup.TextureSetup import HEART_POWER_UP_SLOT_ICON_TEXTURE


class Button(pygame.sprite.Sprite):
    """
        Represents a button object in Laser Fighter. When a button is clicked, its function will be executed.

        Attributes:
            button_text (turtle.Turtle()): Displays the buttons text
            button_indicator (turtle.Turtle()): (Only for the toggle buttons on the settings screen) Displays the
                button indicator text

            type (string): Determines the type of button
            id (int): A unique identifier for the button to further determine and locate the button.

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, id, scale_factor, scale_factor_x, scale_factor_y, page="None"):
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

            :param page: The current page being displayed (Only applies to the Shop Slot and Power Up Slot)
            :type page: string
        """

        super().__init__()
        if type == "Title":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            if id == 1:
                self.rect.center = (640 * scale_factor_x, 275 * scale_factor_y)
            elif id == 2:
                self.rect.center = (640 * scale_factor_x, 455 * scale_factor_y)
            elif id == 3:
                self.rect.center = (640 * scale_factor_x, 635 * scale_factor_y)
        elif type == "Title_Locked":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            if id == 1:
                self.rect.center = (640 * scale_factor_x, 365 * scale_factor_y)
        elif type == "Title_Small":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_SMALL_TEXTURE)
            self.rect = self.image.get_rect()
            if id == 1:
                self.rect.center = (510 * scale_factor_x, 545 * scale_factor_y)
            elif id == 2:
                self.rect.center = (770 * scale_factor_x, 545 * scale_factor_y)
        elif type == "Game":
            self.image = pygame.image.load(MAIN_MENU_BUTTON_MAIN_TEXTURE)
            self.rect = self.image.get_rect()
            if id == 1:
                self.rect.center = (103 * scale_factor_x, 21 * scale_factor_y)
        elif type == "Shop_Slot" or type == "Power_Up_Slot" or type == "Gadgets_Slot":
            self.image = pygame.image.load(INVENTORY_SLOT_FRAME_TEXTURE)
            self.rect = self.image.get_rect()
            if id < 5:
                self.rect.center = ((213 + (170 * (id - 1))) * scale_factor_x, 264 * scale_factor_y)
            elif 4 < id < 9:
                self.rect.center = ((213 + (170 * (id - 1 - 4))) * scale_factor_x, 454 * scale_factor_y)
        elif type == "Buy" or type == "Enable":
            self.image = pygame.image.load(BUY_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (1090 * scale_factor_x, 630 * scale_factor_y)
        elif type == "Regular_Settings_And_Controls":
            self.image = pygame.image.load(SETTINGS_AND_CONTROLS_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            if id == 1:
                self.rect.center = (int(955.5 * scale_factor_x), 645 * scale_factor_y)
            elif id == 2 or id == 3:
                self.rect.center = (int(955.5 * scale_factor_x), 565 * scale_factor_y)
        elif type == "Settings_Toggle":
            self.image = pygame.image.load(SETTINGS_AND_CONTROLS_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            if id < 8:
                self.rect.center = (int(315 * scale_factor_x), (165 + (80 * (id - 1))) * scale_factor_y)
            elif id == 8:
                self.rect.center = (int(955.5 * scale_factor_x), 165 * scale_factor_y)
            elif id == 9:
                self.rect.center = (int(955.5 * scale_factor_x), 245 * scale_factor_y)
            elif id == 10:
                self.rect.center = (int(955.5 * scale_factor_x), 325 * scale_factor_y)
            elif id == 11:
                self.rect.center = (int(955.5 * scale_factor_x), 405 * scale_factor_y)
            elif id == 12:
                self.rect.center = (int(955.5 * scale_factor_x), 485 * scale_factor_y)
        elif type == "Controls_Toggle":
            self.image = pygame.image.load(SETTINGS_AND_CONTROLS_BUTTON_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (int(315 * scale_factor_x), (165 + (80 * (id - 1))) * scale_factor_y)
        self.button_frame_visible = 1

        self.button_text = ButtonText(type, id, self.rect.centerx, self.rect.centery,
                                      scale_factor, scale_factor_x, scale_factor_y, page)

        if type == "Settings_Toggle" or type == "Shop_Slot" or \
                type == "Power_Up_Slot" or type == "Gadgets_Slot" or type == "Buy":
            self.button_indicator = ButtonIndicator(type, id, self.rect.centerx, self.rect.centery,
                                                    scale_factor, scale_factor_x, scale_factor_y)
            self.indicator = 1
        else:
            self.indicator = 0

        self.type = type
        self.id = id

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        del self

    def get_button_frame(self):
        """
            Returns the button frame sprite so its class attributes can be accessed

            :return: button_frame: the button frame sprite
            :type: turtle.Turtle()
        """

        return self

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
        """
             Returns the type of button associated with the given button sprite.

             :return: type: the button type
             :type: string
        """

        return self.type

    def get_id(self):
        """
             Returns the id of the button sprite.

             :return: id: the button id
             :type: int
        """

        return self.id

    def get_indicator_toggled(self):
        """
             Returns whether or not the item associated with the slot is locked or not (For Shop_Slot only).

             :return: indicator_toggled: whether or not the lock is visible or not
             :type: int
        """

        if self.type == "Shop_Slot" or self.type == "Gadget_Slot":
            return self.button_indicator.indicator_toggled

    def remove(self):
        """
            Removes the button sprites from the screen and resets its attributes.

            :return: None
        """

        self.button_frame_visible = 0
        self.button_text.button_text_visible = 0

        if hasattr(self, "button_indicator"):
            self.button_indicator.indicator_visible = 0

        self.button_text.color = "White"

    def write_lines(self):
        """
            Writes the text for all the regular buttons on the screen and then updates the screen with that text.

            :return: None
        """

        if self.type != "Shop_Slot":
            if self.type == "Title":
                if self.id == 1:
                    self.button_text.write_text("Machine Mode", "semi-large", "normal")
                elif self.id == 2:
                    self.button_text.write_text("Coin Shop", "semi-large", "normal")
                elif self.id == 3:
                    self.button_text.write_text("Exit", "semi-large", "normal")
            elif self.type == "Title_Small":
                if self.id == 1:
                    self.button_text.write_text("Settings", "semi-large", "normal")
                elif self.id == 2:
                    self.button_text.write_text("Stats", "semi-large", "normal")
            elif self.type == "Game":
                self.button_text.write_text("Main Menu", "normal", "normal")
            elif self.type == "Regular_Settings_And_Controls":
                if self.id == 1:
                    self.button_text.write_text("Main Menu", "semi-medium", "bold")
                elif self.id == 2:
                    self.button_text.write_text("Controls", "semi-medium", "bold")
                elif self.id == 3:
                    self.button_text.write_text("Settings", "semi-medium", "bold")
            elif self.type == "Settings_Toggle":
                if self.id == 1:
                    self.button_text.write_text("Button Sound:", "semi-medium", "normal")
                elif self.id == 2:
                    self.button_text.write_text("Player Shooting Sound:", "semi-medium", "normal")
                elif self.id == 3:
                    self.button_text.write_text("Enemy Shooting Sound:", "semi-medium", "normal")
                elif self.id == 4:
                    self.button_text.write_text("Player Death Sound:", "semi-medium", "normal")
                elif self.id == 5:
                    self.button_text.write_text("Enemy Death Sound:", "semi-medium", "normal")
                elif self.id == 6:
                    self.button_text.write_text("Player Hit Sound:", "semi-medium", "normal")
                elif self.id == 7:
                    self.button_text.write_text("Enemy Hit Sound:", "semi-medium", "normal")
                elif self.id == 8:
                    self.button_text.write_text("Power Up Pickup Sound:", "semi-medium", "normal")
                elif self.id == 9:
                    self.button_text.write_text("Power Up Spawn Sound:", "semi-medium", "normal")
                elif self.id == 10:
                    self.button_text.write_text("Coin Pick Up Sound:", "semi-medium", "normal")
                elif self.id == 11:
                    self.button_text.write_text("Fullscreen:", "semi-medium", "normal")
                elif self.id == 12:
                    self.button_text.write_text("VSync:", "semi-medium", "normal")

    def toggle_title_lock(self, setting):
        """
            Toggles the lock buttons lock on or off.

            :param setting: Determines whether the button needs to be locked or not
            :type setting: int

            :return:
        """

        # For Alien Mode specifically:
        # If the user does currently have an Alien Mode gun selected (Means it is unlocked)
        if setting != 0:
            # display the regular button text
            if self.id == 1:
                self.button_text.image = pygame.Surface((0, 0), pygame.SRCALPHA)
                self.button_text.image.fill((0, 0, 0, 0))
                self.button_text.rect = self.button_text.image.get_rect()
                self.button_text.rect.center = (640 * self.scale_factor_x, self.rect.centery)
                self.button_text.write_text("Alien Mode", "semi-large", "normal")
        else:
            self.button_text.image = pygame.image.load(LOCKED_TEXTURE)
            self.button_text.rect = self.button_text.image.get_rect()
            self.button_text.rect.center = (640 * self.scale_factor_x, self.rect.centery)

    # def write_buy(self, price):
    #     """
    #         Writes the price text on the buy button based on the item that is currently selected.
    #
    #         :param price: The price of the current item selected
    #         :type price: int
    #
    #         :return: None
    #     """
    #
    #     self.button_text.clear()
    #     self.button_text.goto(self.button_frame.xcor() - 80 * self.scale_factor_x, self.button_frame.ycor() + 10 * self.scale_factor_y)
    #     self.button_text.write("Buy: ", align="center", font=("Courier", int(28 * self.scale_factor), "normal"))
    #     self.button_text.goto(self.button_frame.xcor() - 105 * self.scale_factor_x, self.button_frame.ycor() - 50 * self.scale_factor_y)
    #     self.button_text.write("{}".format(price), align="left", font=("Courier", int(28 * self.scale_factor), "normal"))

    def write_enable(self, check_gadget):
        """
            Used to write the enable buttons text based on whether the gadget is currently disabled or enabled.

            :param check_gadget: Check the current gadget to see if it is enabled or not.
            :type check_gadget: bool

            :return: None
        """

        if check_gadget:
            # If it is enabled, give the option to disable
            self.button_text.color = "red"
            self.button_text.write_text("Disable", "semi-medium", "bold")
        else:
            # If it is disabled, give the option to enable
            self.button_text.color = (0, 128, 0)
            self.button_text.write_text("Enable", "semi-medium", "bold")

    def write_control(self, go_right_key, go_left_key, shoot_key, jump_key):
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

            :return: None
        """

        # Writes new text based on the button id
        if self.id == 1:
            self.button_text.write_text(f"Go Right: {go_right_key}", "semi-medium", "normal")
        elif self.id == 2:
            self.button_text.write_text(f"Go Left: {go_left_key}", "semi-medium", "normal")
        elif self.id == 3:
            self.button_text.write_text(f"Shoot: {shoot_key}", "semi-medium", "normal")
        elif self.id == 4:
            self.button_text.write_text(f"Jump: {jump_key}", "semi-medium", "normal")

    def write_indicator(self, setting):
        """
            Writes the text for the button indicators tied to the settings toggle buttons and the power up slots.

            :param setting: Stores the current configuration for the given setting.
            :type setting: int

            :return: None
        """

        if self.type == "Settings_Toggle":
            # For the settings toggle buttons, make them show on/off in green/red
            if setting == 1:
                self.button_indicator.color = (0, 128, 0)
                self.button_indicator.write_text("On", "semi-medium", "bold")
            else:
                self.button_indicator.color = "red"
                self.button_indicator.write_text("Off", "semi-medium", "bold")
        elif self.type == "Power_Up_Slot":
            # For the power up slots, write the current power up level.
            if setting != 0:
                self.button_indicator.write_text(f"Level {setting}", "tiny", "normal")
        elif self.type == "Gadget_Slot":
            # For the gadget slots, write if they are enabled or disabled
            if setting:
                self.button_indicator.color = (0, 128, 0)
                self.button_indicator.write_text("Enabled", "tiny", "bold")
            else:
                self.button_indicator.color = "red"
                self.button_indicator.write_text("Disabled", "tiny", "bold")

    def write_fullscreen_indicator(self, setting, fullscreen_toggled):
        """
            Writes the text for the fullscreen toggle button indicator specifically since it requires extra steps.

            :param setting: Stores the current configuration for the given setting.
            :type setting: int

            :param fullscreen_toggled: Determines if a switch to the toggle has been made or not.
            :type fullscreen_toggled: int

            :return: None
        """

        if fullscreen_toggled == 1:
            # Display "RST" in yellow for the indicator if an in-game switch has been made
            self.button_indicator.color = "yellow"
            self.button_indicator.write_text("RST", "semi-medium", "bold")
        else:
            # No in game switch has been made, display the indicator like normal
            if setting == 1:
                self.button_indicator.color = (0, 128, 0)
                self.button_indicator.write_text("On", "semi-medium", "bold")
            else:
                self.button_indicator.color = "red"
                self.button_indicator.write_text("Off", "semi-medium", "bold")

    def toggle_indicator(self, check_value):
        """
            Toggled the indicator on and off based on the value passed in. (Whether the item has been bought or not)

            :param check_value: Value that determines whether then indicator is shown or not.
            :type check_value: int

            :return: None
        """

        if self.type != "Gadget_Slot":
            if check_value == 0 or check_value == -1:
                self.button_indicator.indicator_visible = 1
                self.button_text.rect.center = (self.rect.centerx, self.rect.centery + 20 * self.scale_factor_y)
                self.indicator_toggled = 1
            else:
                self.button_indicator.indicator_visible = 0
                if self.type != "Power_Up_Slot":
                    self.button_text.center = (self.rect.centerx, self.rect.centery)
                self.indicator_toggled = 0
        else:
            if not check_value:
                self.button_indicator.indicator_visible = 1
                self.button_text.center = (self.rect.centerx, self.rect.centery + 20 * self.scale_factor_y)
                self.indicator_toggled = 1
            else:
                self.button_indicator.indicator_visible = 0
                self.indicator_toggled = 0

    def set_indicator_location(self):
        """
            Set the location of the indicator based on whether it is toggled or not.

            :return: None
        """

        if self.indicator_toggled == 1:
            self.button_indicator.center = (self.rect.centerx, self.rect.centery + 20 * self.scale_factor_y)
        else:
            if self.type == "Power_Up_Slot":
                self.button_indicator.center = (self.rect.centerx, self.rect.centery - 45 * self.scale_factor_y)
            else:
                self.button_indicator.center = (self.rect.centerx, self.rect.centery - 75 * self.scale_factor_y)

    def toggle_default(self):
        if self.type == "Title" or self.type == "Title_Locked":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_TEXTURE)
        elif self.type == "Title_Small":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_SMALL_TEXTURE)
        elif self.type == "Game":
            self.image = pygame.image.load(MAIN_MENU_BUTTON_MAIN_TEXTURE)
        elif self.type == "Tab":
            self.image = pygame.image.load(TAB_TEXTURE)
        elif self.type == "Shop_Slot" or self.type == "Power_Up_Slot" or self.type == "Gadget_Slot":
            self.image = pygame.image.load(INVENTORY_SLOT_FRAME_TEXTURE)
        elif self.type == "Buy" or self.type == "Enable":
            self.image = pygame.image.load(BUY_BUTTON_TEXTURE)
        elif self.type == "Regular_Settings_And_Controls" or self.type == "Settings_Toggle" or \
                self.type == "Controls_Toggle":
            self.image = pygame.image.load(SETTINGS_AND_CONTROLS_BUTTON_TEXTURE)

    def toggle_highlighted(self):
        if self.type == "Title" or self.type == "Title_Locked":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_HIGHLIGHTED_TEXTURE)
        elif self.type == "Title_Small":
            self.image = pygame.image.load(TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED_TEXTURE)
        elif self.type == "Game":
            self.image = pygame.image.load(MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED_TEXTURE)
        elif self.type == "Tab":
            self.image = pygame.image.load(TAB_HIGHLIGHTED_TEXTURE)
        elif self.type == "Shop_Slot" or self.type == "Power_Up_Slot" or self.type == "Gadget_Slot":
            self.image = pygame.image.load(INVENTORY_SLOT_FRAME_HIGHLIGHTED_TEXTURE)
        elif self.type == "Buy" or self.type == "Enable":
            self.image = pygame.image.load(BUY_BUTTON_HIGHLIGHTED_TEXTURE)
        elif self.type == "Regular_Settings_And_Controls" or self.type == "Settings_Toggle" or \
                self.type == "Controls_Toggle":
            self.image = pygame.image.load(SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED_TEXTURE)

    def update_controls_text_color(self, alert):
        """
            Used to change the color of the control toggle buttons text to red when there is a keybind conflict.

            :param alert: Used to determine if there is a keybind conflict with the control setting
                for this buttons control
            :type alert: int

            :return: None
        """

        if self.id == 1:
            # If the there is a keybind conflict, use red as the color rather than yellow
            if alert == 1:
                self.button_text.color = "red"
            else:
                self.button_text.color = "white"
        elif self.id == 2:
            # If the there is a keybind conflict, use red as the color rather than yellow
            if alert == 2:
                self.button_text.color = "red"
            else:
                self.button_text.color = "white"
        elif self.id == 3:
            # If the there is a keybind conflict, use red as the color rather than yellow
            if alert == 3:
                self.button_text.color = "red"
            else:
                self.button_text.color = "white"
        elif self.id == 4:
            # If the there is a keybind conflict, use red as the color rather than yellow
            if alert == 4:
                self.button_text.color = "red"
            else:
                self.button_text.color = "white"


class ButtonText(pygame.sprite.Sprite):
    def __init__(self, type, id, x, y, scale_factor, scale_factor_x, scale_factor_y, page="None"):
        super().__init__()
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.color = "white"
        if type == "Title":
            self.rect.center = (640 * scale_factor_x, y)
        elif type == "Title_Locked":
            self.image = pygame.image.load(LOCKED_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (640 * scale_factor_x, y)
        elif type == "Title_Small" or type == "Game":
            self.rect.center = (x, y)
        elif type == "Tab":
            if id == 1:
                self.image = pygame.image.load(MACHINE_MODE_TAB_ICON_TEXTURE)
            elif id == 2:
                self.image = pygame.image.load(PLAYER_GUN_RIGHT_TEXTURE)
            elif id == 3:
                self.image = pygame.image.load(YELLOW_LIGHTNING_POWER_UP_TEXTURE)
            elif id == 4:
                self.image = pygame.image.load(GADGETS_TAB_ICON_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        elif type == "Shop_Slot" or type == "Power_Up_Slot" or type == "Gadgets_Slot":
            if page == "Machine_Mode":
                if id == 1:
                    self.button_image = pygame.image.load(MACHINE_DEFAULT_SLOT_ICON_TEXTURE)
                elif id == 2:
                    self.button_image = pygame.image.load(MACHINE_WASHER_SLOT_ICON_TEXTURE)
                elif id == 3:
                    self.button_image = pygame.image.load(THE_INCINERATOR_SLOT_ICON_TEXTURE)
                elif id == 4:
                    self.button_image = pygame.image.load(THE_BLACK_HOLE_SLOT_ICON_TEXTURE)
                elif id == 5:
                    self.button_image = pygame.image.load(THE_STAR_KILLER_SLOT_ICON_TEXTURE)
            elif page == "Alien_Mode":
                if id == 1:
                    self.button_image = pygame.image.load(ALIEN_DEFAULT_SLOT_ICON_TEXTURE)
                elif id == 2:
                    self.button_image = pygame.image.load(THE_COOKER_SLOT_ICON_TEXTURE)
                elif id == 3:
                    self.button_image = pygame.image.load(POISON_DART_SLOT_ICON_TEXTURE)
                elif id == 4:
                    self.button_image = pygame.image.load(METEOR_GUN_SLOT_ICON_TEXTURE)
                elif id == 5:
                    self.button_image = pygame.image.load(SUPERNOVA_SLOT_ICON_TEXTURE)
            elif page == "Power_Ups":
                if id == 1:
                    self.button_image = pygame.image.load(YELLOW_POWER_UP_SLOT_ICON_TEXTURE)
                elif id == 2:
                    self.button_image = pygame.image.load(BLUE_POWER_UP_SLOT_ICON_TEXTURE)
                elif id == 3:
                    self.button_image = pygame.image.load(GREEN_POWER_UP_SLOT_ICON_TEXTURE)
                elif id == 4:
                    self.button_image = pygame.image.load(RED_POWER_UP_SLOT_ICON_TEXTURE)
            elif page == "Gadgets":
                if id == 1:
                    self.button_image = pygame.image.load(COIN_MAGNET_SLOT_ICON_TEXTURE)
                elif id == 2:
                    self.button_image = pygame.image.load(ARMOR_SLOT_ICON_TEXTURE)
                elif id == 3:
                    self.button_image = pygame.image.load(THORNS_SLOT_ICON_TEXTURE)
                elif id == 4:
                    self.button_image = pygame.image.load(HEART_POWER_UP_SLOT_ICON_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y + 20 * scale_factor_y)
        elif type == "Buy":
            self.rect.center = (x - 80 * scale_factor_x, y + 10 * scale_factor_y)
            self.color = "Yellow"
        elif type == "Enable":
            self.rect.center = (x, y)
            self.color = "Red"
        elif type == "Regular_Settings_And_Controls":
            self.rect.center = (x, y)
        elif type == "Settings_Toggle":
            self.rect.center = (x - 30 * scale_factor_x, y)
        elif type == "Controls_Toggle":
            self.rect.center = (x, y)
        self.button_text_visible = 1

        self.small_font = pygame.font.SysFont("Courier", int(29.5 * scale_factor))
        self.normal_font = pygame.font.SysFont("Courier", int(32.5 * scale_factor))
        self.semi_medium_font = pygame.font.SysFont("Courier", int(37.8 * scale_factor))
        self.semi_large_font = pygame.font.SysFont("Courier", int(40.5 * scale_factor))
        self.large_font = pygame.font.SysFont("Courier", int(48.5 * scale_factor))
        self.subtitle_font = pygame.font.SysFont("Courier", int(65 * scale_factor))
        self.title_font = pygame.font.SysFont("Courier", int(97 * scale_factor))

        self.small_font_bold = pygame.font.SysFont("Courier", int(29.5 * scale_factor), bold=True)
        self.normal_font_bold = pygame.font.SysFont("Courier", int(32.5 * scale_factor), bold=True)
        self.semi_medium_font_bold = pygame.font.SysFont("Courier", int(37.8 * scale_factor), bold=True)
        self.semi_large_font_bold = pygame.font.SysFont("Courier", int(40.5 * scale_factor), bold=True)
        self.large_font_bold = pygame.font.SysFont("Courier", int(48.5 * scale_factor), bold=True)
        self.subtitle_font_bold = pygame.font.SysFont("Courier", int(65 * scale_factor), bold=True)
        self.title_font_bold = pygame.font.SysFont("Courier", int(97 * scale_factor), bold=True)

        self.type = type
        self.id = id

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y
        self.scale_factor = scale_factor

    def __del__(self):
        self.kill()

    def write_text(self, text, size, type):
        if self.type != "Shop_Slot":
            old_center = self.rect.center
            if size == "small":
                if type == "bold":
                    self.image = self.small_font_bold.render(text, True, self.color)
                else:
                    self.image = self.small_font.render(text, True, self.color)

            elif size == "normal":
                if type == "bold":
                    self.image = self.normal_font_bold.render(text, True, self.color)
                else:
                    self.image = self.normal_font.render(text, True, self.color)

            elif size == "semi-medium":
                if type == "bold":
                    self.image = self.semi_medium_font_bold.render(text, True, self.color)
                else:
                    self.image = self.semi_medium_font.render(text, True, self.color)

            elif size == "semi-large":
                if type == "bold":
                    self.image = self.semi_large_font_bold.render(text, True, self.color)
                else:
                    self.image = self.semi_large_font.render(text, True, self.color)

            elif size == "large":
                if type == "bold":
                    self.image = self.large_font_bold.render(text, True, self.color)
                else:
                    self.image = self.large_font.render(text, True, self.color)

            elif size == "subtitle":
                if type == "bold":
                    self.image = self.subtitle_font_bold.render(text, True, self.color)
                else:
                    self.image = self.subtitle_font.render(text, True, self.color)

            elif size == "title":
                if type == "bold":
                    self.image = self.title_font_bold.render(text, True, self.color)
                else:
                    self.image = self.title_font.render(text, True, self.color)

            else:
                # fallback if size not recognized, default to normal
                if type == "bold":
                    self.image = self.normal_font_bold.render(text, True, self.color)
                else:
                    self.image = self.normal_font.render(text, True, self.color)
            self.rect = self.image.get_rect(center=old_center)


class ButtonIndicator(pygame.sprite.Sprite):
    def __init__(self, type, id, x, y, scale_factor, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.color = "red"
        if type == "Settings_Toggle":
            if id == 1:
                self.rect.center = (463 * scale_factor_x, 165 * scale_factor_y)
            elif id == 2:
                self.rect.center = (561 * scale_factor_x, 245 * scale_factor_y)
            elif id == 3:
                self.rect.center = (552 * scale_factor_x, 325 * scale_factor_y)
            elif id == 4:
                self.rect.center = (529 * scale_factor_x, 405 * scale_factor_y)
            elif id == 5:
                self.rect.center = (519 * scale_factor_x, 485 * scale_factor_y)
            elif id == 6:
                self.rect.center = (508 * scale_factor_x, 565 * scale_factor_y)
            elif id == 7:
                self.rect.center = (497 * scale_factor_x, 645 * scale_factor_y)
            elif id == 8:
                self.rect.center = (int(1201.5 * scale_factor_x), 165 * scale_factor_y)
            elif id == 9:
                self.rect.center = (int(1192.5 * scale_factor_x), 245 * scale_factor_y)
            elif id == 10:
                self.rect.center = (int(1170.5 * scale_factor_x), 325 * scale_factor_y)
            elif id == 11:
                self.rect.center = (int(1080.5 * scale_factor_x), 405 * scale_factor_y)
            elif id == 12:
                self.rect.center = (int(1024.5 * scale_factor_x), 485 * scale_factor_y)
        elif type == "Shop_Slot" or type == "Power_Up_Slot" or type == "Gadgets_Slot":
            self.color = "white"
            self.image = pygame.image.load(LOCKED_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y + 20 * scale_factor_y)
            self.indicator_toggled = 0
        elif type == "Buy":
            self.image = pygame.image.load(COIN_INDICATOR_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (x - 125 * scale_factor_x,y - 28 * scale_factor_y)
        self.indicator_visible = 1

        self.tiny_font = pygame.font.SysFont("Courier", int(24.3 * scale_factor))
        self.small_font = pygame.font.SysFont("Courier", int(29.5 * scale_factor))
        self.normal_font = pygame.font.SysFont("Courier", int(32.5 * scale_factor))
        self.semi_medium_font = pygame.font.SysFont("Courier", int(37.8 * scale_factor))
        self.semi_large_font = pygame.font.SysFont("Courier", int(40.5 * scale_factor))
        self.large_font = pygame.font.SysFont("Courier", int(48.5 * scale_factor))
        self.subtitle_font = pygame.font.SysFont("Courier", int(65 * scale_factor))
        self.title_font = pygame.font.SysFont("Courier", int(97 * scale_factor))

        self.tiny_font_bold = pygame.font.SysFont("Courier", int(24.3 * scale_factor), bold=True)
        self.small_font_bold = pygame.font.SysFont("Courier", int(29.5 * scale_factor), bold=True)
        self.normal_font_bold = pygame.font.SysFont("Courier", int(32.5 * scale_factor), bold=True)
        self.semi_medium_font_bold = pygame.font.SysFont("Courier", int(37.8 * scale_factor), bold=True)
        self.semi_large_font_bold = pygame.font.SysFont("Courier", int(40.5 * scale_factor), bold=True)
        self.large_font_bold = pygame.font.SysFont("Courier", int(48.5 * scale_factor), bold=True)
        self.subtitle_font_bold = pygame.font.SysFont("Courier", int(65 * scale_factor), bold=True)
        self.title_font_bold = pygame.font.SysFont("Courier", int(97 * scale_factor), bold=True)

        self.type = type
        self.id = id

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y
        self.scale_factor = scale_factor

    def __del__(self):
        self.kill()

    def write_text(self, text, size, type):
        old_center = self.rect.center
        if size == "tiny":
            if type == "bold":
                self.image = self.tiny_font_bold.render(text, True, self.color)
            else:
                self.image = self.tiny_font.render(text, True, self.color)

        elif size == "small":
            if type == "bold":
                self.image = self.small_font_bold.render(text, True, self.color)
            else:
                self.image = self.small_font.render(text, True, self.color)

        elif size == "normal":
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)

        elif size == "semi-medium":
            if type == "bold":
                self.image = self.semi_medium_font_bold.render(text, True, self.color)
            else:
                self.image = self.semi_medium_font.render(text, True, self.color)

        elif size == "semi-large":
            if type == "bold":
                self.image = self.semi_large_font_bold.render(text, True, self.color)
            else:
                self.image = self.semi_large_font.render(text, True, self.color)

        elif size == "large":
            if type == "bold":
                self.image = self.large_font_bold.render(text, True, self.color)
            else:
                self.image = self.large_font.render(text, True, self.color)

        elif size == "subtitle":
            if type == "bold":
                self.image = self.subtitle_font_bold.render(text, True, self.color)
            else:
                self.image = self.subtitle_font.render(text, True, self.color)

        elif size == "title":
            if type == "bold":
                self.image = self.title_font_bold.render(text, True, self.color)
            else:
                self.image = self.title_font.render(text, True, self.color)

        else:
            # fallback if size not recognized, default to normal
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)
        self.rect = self.image.get_rect(center=old_center)