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

import ctypes
import pygame
from setup.data.ShopDescriptions import MACHINE_PRICES
from setup.data.ShopDescriptions import ALIEN_PRICES
from setup.data.ShopDescriptions import POWER_UP_PRICES


class Shop:
    def __init__(self, window, screen, button, panel, textbox, price_label, settings, refresh, shop_config, scale_factor_x, scale_factor_y):
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

        self._price_displayed = 0

    def __del__(self):
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
        return self._price_displayed

    @price_displayed.setter
    def price_displayed(self, value):
        if isinstance(value, int):
            self._price_displayed = value
        else:
            raise ValueError("Mode must be a integer")

    def slot_1_select(self, x, y):
        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -503 * self._scale_factor_x) and (x < -352 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 1)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 1)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 1)

    def slot_2_select(self, x, y):
        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -333 * self._scale_factor_x) and (x < -182 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 2)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 2)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 2)

    def slot_3_select(self, x, y):
        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -163 * self._scale_factor_x) and (x < -12 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 3)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 3)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 3)

    def slot_4_select(self, x, y):
        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 7 * self._scale_factor_x) and (x < 158 * self._scale_factor_x) and (y > 11 * self._scale_factor_y) and (y < 182 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 4)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 4)
            elif self._screen.page == "Power_Ups":
                self.execute_slot_function("Power_Ups", 4)

    def slot_5_select(self, x, y):
        self._window.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -503 * self._scale_factor_x) and (x < -352 * self._scale_factor_x) and (y > -179 * self._scale_factor_y) and (y < -8 * self._scale_factor_y):
            if self._screen.page == "Machine_Mode":
                self.execute_slot_function("Machine_Mode", 5)
            elif self._screen.page == "Alien_Mode":
                self.execute_slot_function("Alien_Mode", 5)

    def execute_slot_function(self, current_page, slot_id):
        # Button sound is played
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        if current_page != "Power_Ups":
            for pa in self._panel.panel_turtle:
                pa.set_panel_text(current_page, slot_id)
            if current_page == "Machine_Mode":
                if self._shop_config.machine_slots_unlocked[slot_id - 1] == 1:
                    self._shop_config.machine_slot_selected = slot_id
                    self._shop_config.save()
                    self._refresh.move_slot_selector = 1
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                else:
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                    self._button.spawn_button("Buy", 1)
                    self._price_displayed = MACHINE_PRICES[slot_id - 1]
            elif current_page == "Alien_Mode":
                if self._shop_config.alien_slots_unlocked[slot_id - 1] == 1:
                    self._shop_config.alien_slot_selected = slot_id
                    self._shop_config.save()
                    self._refresh.move_slot_selector = 1
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                else:
                    for bu in self._button.buttons_on_screen_list:
                        if bu.get_type() == "Buy":
                            bu.remove()
                            self._button.buttons_on_screen_list.pop()
                    self._button.spawn_button("Buy", 1)
                    self._price_displayed = ALIEN_PRICES[slot_id - 1]
        else:
            if slot_id == 1:
                for pa in self._panel.panel_turtle:
                    pa.set_panel_text("Yellow_Power_Up", slot_id)
                if self._shop_config.yellow_power_up_level != 5:
                    self._price_displayed = POWER_UP_PRICES[self._shop_config.yellow_power_up_level - 1]
                else:
                    self._price_displayed = 0
            elif slot_id == 2:
                for pa in self._panel.panel_turtle:
                    pa.set_panel_text("Blue_Power_Up", slot_id)
                if self._shop_config.blue_power_up_level != 5:
                    self._price_displayed = POWER_UP_PRICES[self._shop_config.blue_power_up_level - 1]
                else:
                    self._price_displayed = 0
            elif slot_id == 3:
                for pa in self._panel.panel_turtle:
                    pa.set_panel_text("Green_Power_Up", slot_id)
                if self._shop_config.green_power_up_level != 5:
                    self._price_displayed = POWER_UP_PRICES[self._shop_config.green_power_up_level - 1]
                else:
                    self._price_displayed = 0
            elif slot_id == 4:
                for pa in self._panel.panel_turtle:
                    pa.set_panel_text("Red_Power_Up", slot_id)
                if self._shop_config.red_power_up_level != 5:
                    self._price_displayed = POWER_UP_PRICES[self._shop_config.red_power_up_level - 1]
                else:
                    self._price_displayed = 0
            if self._price_displayed != 0:
                for bu in self._button.buttons_on_screen_list:
                    if bu.get_type() == "Buy":
                        bu.remove()
                        self._button.buttons_on_screen_list.pop()
                        self._button.current_button_index = self._button.current_button_index - 1
                self._button.spawn_button("Buy", 1)
            else:
                for bu in self._button.buttons_on_screen_list:
                    if bu.get_type() == "Buy":
                        bu.remove()
                        self._button.buttons_on_screen_list.pop()
                        self._button.current_button_index = self._button.current_button_index - 1
        self._refresh.refresh_panel = 1
        self._refresh.refresh_button = 1

    def execute_buy_button(self, x, y):
        self._window.onscreenclick(None)
        if (x > 299 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -328 * self._scale_factor_y) and (y < -212 * self._scale_factor_y):
            # Button sound is played
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
                sound.play()
            if self._price_displayed > self._shop_config.total_coins:
                ctypes.windll.user32.MessageBoxW(0, "You do not have enough coins to purchase this item!", "Not Enough Coins!", 16)
            else:
                message_output = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to purchase this item for {} coins?".format(self._price_displayed), "Are you sure?", 4 + 32)
                if message_output != 7:
                    max_level = 0
                    # Coin sound is played
                    if self._settings.button_sound == 1:
                        sound = pygame.mixer.Sound("Sound/Coin_Pickup_Sound.wav")
                        sound.play()
                    self._shop_config.total_coins = self._shop_config.total_coins - self._price_displayed
                    self._shop_config.save()
                    current_slot = 0
                    for pl in self._panel.panel_turtle:
                        current_slot = pl.get_panel_id()
                    if self._screen.page == "Machine_Mode":
                        self._shop_config.machine_slots_unlocked[current_slot - 1] = 1
                        self._shop_config.machine_slot_selected = current_slot
                        self._shop_config.save()
                    elif self._screen.page == "Alien_Mode":
                        self._shop_config.alien_slots_unlocked[current_slot - 1] = 1
                        self._shop_config.alien_slot_selected = current_slot
                        self._shop_config.save()
                    elif self._screen.page == "Power_Ups":
                        if current_slot == 1:
                            self._shop_config.yellow_power_up_level = self._shop_config.yellow_power_up_level + 1
                            if self._shop_config.yellow_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.yellow_power_up_level - 1]
                                max_level = 0
                        elif current_slot == 2:
                            self._shop_config.blue_power_up_level = self._shop_config.blue_power_up_level + 1
                            if self._shop_config.blue_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.blue_power_up_level - 1]
                                max_level = 0
                        elif current_slot == 3:
                            self._shop_config.green_power_up_level = self._shop_config.green_power_up_level + 1
                            if self._shop_config.green_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.green_power_up_level - 1]
                                max_level = 0
                        elif current_slot == 4:
                            self._shop_config.red_power_up_level = self._shop_config.red_power_up_level + 1
                            if self._shop_config.red_power_up_level == 5:
                                max_level = 1
                            else:
                                self._price_displayed = POWER_UP_PRICES[self._shop_config.red_power_up_level - 1]
                                max_level = 0
                        self._shop_config.save()
                    if self._screen.page != "Power_Ups" or max_level == 1:
                        for bu in self._button.buttons_on_screen_list:
                            if bu.get_type() == "Buy":
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
                    self._refresh.refresh_panel = 1
                    self._refresh.refresh_text = 1
                    self._refresh.refresh_button = 1
                    self._refresh.refresh_indicator = 1
                    self._refresh.move_slot_selector = 1
                    self._button.buy_button_pressed = 1
