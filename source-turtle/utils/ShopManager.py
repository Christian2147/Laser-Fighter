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
    File: ShopManager.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for updating the current shop configuration and navigating through the in game shop.
    This includes all the execution functions for all the buttons in the shop.
"""

import pygame
from tkinter import messagebox
from setup.data.ShopDescriptions import MACHINE_PRICES
from setup.data.ShopDescriptions import ALIEN_PRICES
from setup.data.ShopDescriptions import POWER_UP_PRICES
from setup.data.ShopDescriptions import GADGET_PRICE


class Shop:
    """
        Represents the function and logic for the in game Shop.
        This includes navigating the shop and buying items in the shop.

        Pointers:
            _window (turtle.Screen()): Pointer to the application window.
            _screen (ScreenUpdate()): Pointer to the current displayed screen and the screen changing functions
            _button (SpawnButton()): Pointer to all the button objects currently on the screen
            _panel (SpawnPanel()): Pointer to all the panel objects currently on the screen
            _textbox (SpawnTextBox()): Pointer to all the text boxes currently on the screen
            _price_label (SpawnPriceLabel()): Pointer to all the price label objects currently on the screen
            _settings (Settings()): Pointer to the current game settings
            _refresh (Refresh()): Pointer to the game refresh variables
            _shop_config (ShopConfig()): Pointer to the current shop configuration

        Attributes:
            _scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode

            _price_displayed (int): The current price displayed on the buy button in the shop
    """

    def __init__(self, window, screen, button, panel, textbox, price_label, settings, refresh, shop_config, scale_factor_x, scale_factor_y):
        """
            Initializes all the necessary pointers for the Shop Manager.

            :param window: Pointer to the application window.
            :type window: turtle.Screen()

            :param screen: Pointer to the current displayed screen and the screen changing functions.
            :type screen: ScreenUpdate()

            :param button: Pointer to all the button objects currently on the screen.
            :type button: SpawnButton()

            :param panel: Pointer to all the panel objects currently on the screen.
            :type panel: SpawnPanel()

            :param textbox: Pointer to all the text boxes currently on the screen.
            :type textbox: SpawnTextBox()

            :param price_label: Pointer to all the price label objects currently on the screen.
            :type price_label: SpawnPriceLabel()

            :param settings: Pointer to the current game settings.
            :type settings: Settings()

            :param refresh: Pointer to the game refresh variables.
            :type refresh: Refresh()

            :param shop_config: Pointer to the current shop configuration.
            :type shop_config: ShopConfig()

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode.
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode.
            :type scale_factor_y: float
        """

        # Initialize all the pointers
        self._window = window
        self._screen = screen
        self._button = button
        self._panel = panel
        self._textbox = textbox
        self._price_label = price_label
        self._settings = settings
        self._refresh = refresh
        self._shop_config = shop_config

        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        # Price displayed on the buy button
        self._price_displayed = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._window
        del self._screen
        del self._button
        del self._panel
        del self._textbox
        del self._price_label
        del self._settings
        del self._refresh
        del self._shop_config
        del self._scale_factor_x
        del self._scale_factor_y
        del self._price_displayed

    @property
    def price_displayed(self):
        """price_displayed getter"""
        return self._price_displayed

    @price_displayed.setter
    def price_displayed(self, value):
        """price_displayed setter"""
        if isinstance(value, int):
            self._price_displayed = value
        else:
            raise ValueError("price_displayed must be a integer")

    def slot_1_select(self, x, y):
        """
            Used to display the first slot on the page on the side panel and select it if the item is available.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -503 * self._scale_factor_x) and (x < -352 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            # Which item is displayed depends on the current page that is being displayed in the shop
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 1)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 1)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 1)
            elif self._screen.page == "Gadgets":
                self.execute_slot_function("Gadgets", 1)

    def slot_2_select(self, x, y):
        """
            Used to display the second slot on the page on the side panel and select it if the item is available.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -333 * self._scale_factor_x) and (x < -182 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 2)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 2)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 2)
            elif self._screen.page == "Gadgets":
                self.execute_slot_function("Gadgets", 2)

    def slot_3_select(self, x, y):
        """
            Used to display the third slot on the page on the side panel and select it if the item is available.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -163 * self._scale_factor_x) and (x < -12 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 3)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 3)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 3)
            elif self._screen.page == "Gadgets":
                self.execute_slot_function("Gadgets", 3)

    def slot_4_select(self, x, y):
        """
            Used to display the fourth slot on the page on the side panel and select it if the item is available.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 7 * self._scale_factor_x) and (x < 158 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 4)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 4)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 4)
            elif self._screen.page == "Gadgets":
                self.execute_slot_function("Gadgets", 4)

    def slot_5_select(self, x, y):
        """
            Used to display the fifth slot on the page on the side panel and select it if the item is available.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -503 * self._scale_factor_x) and (x < -352 * self._scale_factor_x) and (y > -179 * self._scale_factor_y) and (y < -8 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 5)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 5)

    def execute_slot_function(self, current_page, slot_id):
        """
            Executes the displaying of the slot that was clicked on and also selects that slot if the item is available.

            :param current_page: The current page displayed in the shop
            :type current_page: string

            :param slot_id: The id of the slot that was selected (1-5)
            :type slot_id: int

            :return: None
        """

        # Button sound is played
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # If the page is not "Power_Ups" and "Gadgets", the item has to be bought in order for it to be selected
        if current_page != "Power_Ups" and current_page != "Gadgets":
            # Display the slot item on the side panel in the shop
            for pa in self._panel.panel_turtle:
                pa.set_panel_text(current_page, slot_id)
            if current_page == "Machine_Mode":
                # if the item displayed in the slot is unlocked
                if self._shop_config.machine_slots_unlocked[slot_id - 1] == 1:
                    # Select the slot
                    self._shop_config.machine_slot_selected = slot_id
                    self._shop_config.save()
                    self._refresh.move_slot_selector = 1
                    # Remove the buy button
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                # If the item is not bought
                else:
                    # Recreate the buy button to show the price for the selected item
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                    self._button.spawn_button("Buy", 1)
                    self._price_displayed = MACHINE_PRICES[slot_id - 1]
            elif current_page == "Alien_Mode":
                # if the item displayed in the slot is unlocked
                if self._shop_config.alien_slots_unlocked[slot_id - 1] == 1:
                    # Select the slot
                    self._shop_config.alien_slot_selected = slot_id
                    self._shop_config.save()
                    self._refresh.move_slot_selector = 1
                    # Remove the buy button
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy" or bu.get_type() == "Enable":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                            self._button.current_button_index = self._button.current_button_index - 1
                # If the item is not bought
                else:
                    # Remove the current buy button being displayed
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy" or bu.get_type() == "Enable":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                            self._button.current_button_index = self._button.current_button_index - 1
                    # If Alien Mode is unlocked, recreate the buy button
                    #   and display the price and allow the user to buy the item
                    if self._shop_config.alien_slots_unlocked[slot_id -1] != -1:
                        self._button.spawn_button("Buy", 1)
                        self._price_displayed = ALIEN_PRICES[slot_id - 1]
                    # If it is locked, do not allow the user to buy the item
                    else:
                        self._price_displayed = 0
        else:
            if slot_id == 1:
                # If the current page is power ups, display the information for the next level up from the current
                #   level of the power up selected
                if current_page == "Power_Ups":
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Yellow_Power_Up", slot_id)
                    # Display a price if there is still a level higher
                    if self._shop_config.yellow_power_up_level != 5:
                        self._price_displayed = POWER_UP_PRICES[self._shop_config.yellow_power_up_level]
                    else:
                        self._price_displayed = 0
                # If the current page is gadgets, display the price of the gadget if it is
                #   not bought, or display a button to enable/disable it
                else:
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Gadget", slot_id)
                    # Check if the item has already been unlocked or not
                    if not self._shop_config.coin_magnet_unlocked:
                        self._price_displayed = GADGET_PRICE
                    else:
                        self._price_displayed = 0
            elif slot_id == 2:
                if current_page == "Power_Ups":
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Blue_Power_Up", slot_id)
                    if self._shop_config.blue_power_up_level != 5:
                        self._price_displayed = POWER_UP_PRICES[self._shop_config.blue_power_up_level]
                    else:
                        self._price_displayed = 0
                else:
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Gadget", slot_id)
                    if not self._shop_config.shield_unlocked:
                        self._price_displayed = GADGET_PRICE
                    else:
                        self._price_displayed = 0
            elif slot_id == 3:
                if current_page == "Power_Ups":
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Green_Power_Up", slot_id)
                    if self._shop_config.green_power_up_level != 5:
                        self._price_displayed = POWER_UP_PRICES[self._shop_config.green_power_up_level]
                    else:
                        self._price_displayed = 0
                else:
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Gadget", slot_id)
                    if not self._shop_config.thorns_unlocked:
                        self._price_displayed = GADGET_PRICE
                    else:
                        self._price_displayed = 0
            elif slot_id == 4:
                if current_page == "Power_Ups":
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Red_Power_Up", slot_id)
                    if self._shop_config.red_power_up_level != 5:
                        self._price_displayed = POWER_UP_PRICES[self._shop_config.red_power_up_level]
                    else:
                        self._price_displayed = 0
                else:
                    for pa in self._panel.panel_turtle:
                        pa.set_panel_text("Gadget", slot_id)
                    if not self._shop_config.hearts_unlocked:
                        self._price_displayed = GADGET_PRICE
                    else:
                        self._price_displayed = 0
            # If there is a price, create a buy button, if not, do not create a button at all
            #   and remove any existing one
            if self._price_displayed != 0:
                for bu in self._button.buttons_on_screen_list:
                    if bu.get_type() == "Buy" or bu.get_type() == "Enable":
                        bu.remove()
                        self._button.buttons_on_screen_list.pop()
                        self._button.current_button_index = self._button.current_button_index - 1
                self._button.spawn_button("Buy", 1)
            else:
                for bu in self._button.buttons_on_screen_list:
                    if bu.get_type() == "Buy" or bu.get_type() == "Enable":
                        bu.remove()
                        self._button.buttons_on_screen_list.pop()
                        self._button.current_button_index = self._button.current_button_index - 1
            # If the item is a gadget, an "enable" button should replace the "buy" button when the item is bought
            if current_page == "Gadgets" and self._price_displayed == 0:
                self._button.spawn_button("Enable", 1)
        # Refresh the side panel and all buttons
        self._refresh.refresh_panel = 1
        self._refresh.refresh_button = 1

    def execute_buy_button(self, x, y):
        """
            Buys the item that is selected in the shop and selects the item to be used.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 299 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -328 * self._scale_factor_y) and (y < -212 * self._scale_factor_y):
            # Button sound is played
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # If the player does not have enough coins, display an error message
            if self._price_displayed > self._shop_config.total_coins:
                messagebox.showerror("Not Enough Coins!", "You do not have enough coins to purchase this item!")
            # If the player does have enough coins
            else:
                # Clarify if the user wants to purchase the item
                message_output = messagebox.askquestion("Are you sure?", "Are you sure you want to purchase this item for {} coins?".format(self._price_displayed), icon='question')
                # If the user says yes
                if message_output == 'yes':
                    max_level = 0
                    # Coin sound is played
                    if self._settings.button_sound == 1:
                        sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                        sound.play()
                    # Subtract from the total coins
                    self._shop_config.total_coins = self._shop_config.total_coins - self._price_displayed
                    self._shop_config.save()
                    current_slot = 0
                    for pl in self._panel.panel_turtle:
                        current_slot = pl.get_panel_id()
                    # Unlock the slot and select it
                    if self._screen.page == "Machine_Mode":
                        self._shop_config.machine_slots_unlocked[current_slot - 1] = 1
                        self._shop_config.machine_slot_selected = current_slot
                        self._shop_config.save()
                    elif self._screen.page == "Alien_Mode":
                        self._shop_config.alien_slots_unlocked[current_slot - 1] = 1
                        self._shop_config.alien_slot_selected = current_slot
                        self._shop_config.save()
                    # If the page is power ups
                    elif self._screen.page == "Power_Ups":
                        # Increase the power up level by 1
                        if current_slot == 1:
                            self._shop_config.yellow_power_up_level = self._shop_config.yellow_power_up_level + 1
                            if self._shop_config.yellow_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.yellow_power_up_level]
                                max_level = 0
                        elif current_slot == 2:
                            self._shop_config.blue_power_up_level = self._shop_config.blue_power_up_level + 1
                            if self._shop_config.blue_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.blue_power_up_level]
                                max_level = 0
                        elif current_slot == 3:
                            self._shop_config.green_power_up_level = self._shop_config.green_power_up_level + 1
                            if self._shop_config.green_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.green_power_up_level]
                                max_level = 0
                        elif current_slot == 4:
                            self._shop_config.red_power_up_level = self._shop_config.red_power_up_level + 1
                            if self._shop_config.red_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.red_power_up_level]
                                max_level = 0
                        self._shop_config.save()
                    # If the page is gadgets
                    elif self._screen.page == "Gadgets":
                        # Unlock and enable the gadget if it is successfully bought
                        if current_slot == 1:
                            self._shop_config.coin_magnet_unlocked = True
                            self._shop_config.coin_magnet_enabled = True
                        elif current_slot == 2:
                            self._shop_config.shield_unlocked = True
                            self._shop_config.shield_enabled = True
                        elif current_slot == 3:
                            self._shop_config.thorns_unlocked = True
                            self._shop_config.thorns_enabled = True
                        elif current_slot == 4:
                            self._shop_config.hearts_unlocked = True
                            self._shop_config.hearts_enabled = True
                        self._shop_config.save()
                    # Remove the buy button is the page is not the power ups page or the max level as been reached
                    if self._screen.page != "Power_Ups" or max_level == 1:
                        for bu in self._button.buttons_on_screen_list:
                            if bu.get_type() == "Buy" or bu.get_type() == "Enable":
                                bu.remove()
                                self._button.buttons_on_screen_list.pop()
                                self._button.current_button_index = self._button.current_button_index - 1
                        for t in self._textbox.text_on_screen_list:
                            if t.get_id() == current_slot + 3:
                                t.remove()
                                self._textbox.text_on_screen_list.remove(t)
                                self._textbox.current_text_index = self._textbox.current_text_index - 1
                        for pr in self._price_label.price_label_on_screen_list:
                            if pr.get_id() == current_slot + 3:
                                pr.remove()
                        # If the current page is the gadgets page, display an enable/disable button after
                        #   removing the buy button
                        if self._screen.page == "Gadgets":
                            self._button.spawn_button("Enable", 1)
                    # Refresh the panel, text, buttons, indicators, selectors, and set buy_button_pressed to 1
                    self._refresh.refresh_panel = 1
                    self._refresh.refresh_text = 1
                    self._refresh.refresh_button = 1
                    self._refresh.refresh_indicator = 1
                    self._refresh.move_slot_selector = 1
                    self._button.buy_button_pressed = 1

    def execute_enable_button(self, x, y):
        """
            Toggles the currently selected gadget on or off.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 299 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -328 * self._scale_factor_y) and (y < -212 * self._scale_factor_y):
            # Button sound is played
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            for pa in self._panel.panel_turtle:
                # Check to see what gadgets is currently being displayed
                if pa.category == "Gadget":
                    if pa.id == 1:
                        # Toggle the gadget on if it is off and off if it is on
                        if self._shop_config.coin_magnet_enabled:
                            self._shop_config.coin_magnet_enabled = False
                        else:
                            self._shop_config.coin_magnet_enabled = True
                    elif pa.id == 2:
                        if self._shop_config.shield_enabled:
                            self._shop_config.shield_enabled = False
                        else:
                            self._shop_config.shield_enabled = True
                    elif pa.id == 3:
                        if self._shop_config.thorns_enabled:
                            self._shop_config.thorns_enabled = False
                        else:
                            self._shop_config.thorns_enabled = True
                    elif pa.id == 4:
                        if self._shop_config.hearts_enabled:
                            self._shop_config.hearts_enabled = False
                        else:
                            self._shop_config.hearts_enabled = True
            # Save the settings and update the screen
            self._shop_config.save()
            self._refresh.refresh_panel = 1
            self._refresh.refresh_text = 1
            self._refresh.refresh_button = 1
