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
    File: UpdateText.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for the refreshing of all text on the screen.
    It also contains the logic for initiating the printing of text on the screen.
"""


class TextRefresh:
    """
        Represents the refreshing of all text on the screen.

        Pointers:
            _screen (ScreenUpdate()): Pointer to the current displayed screen and the screen changing functions
            _button (SpawnButton()): Pointer to all the button objects currently on the screen
            _panel (SpawnPanel()): Pointer to all the panel objects currently on the screen
            _textbox (SpawnTextBox()): Pointer to all the text boxes currently on the screen
            _yellow_power_up_indicator (SpawnYellowPowerUpIndicator()): Pointer to the yellow power up indicator
            _blue_power_up_indicator (SpawnBluePowerUpIndicator()): Pointer to the blue power up indicator
            _extra_power_up_indicator (SpawnExtraPowerUpIndicator()): Pointer to the extra power up indicator
            _settings (Settings()): Pointer to the current game settings
            _settings_toggle (SettingsToggle()): Pointer to the settings updater
            _statistics (Stats()): Pointer to the current game statistics
            _shop (Shop()): Pointer to the shop manager and updater
            _shop_config (ShopConfig()): Pointer to the current shop configuration
            _controls (Controls()): Pointer to the controls manager and updater
            _controls_toggle (ControlsToggle()): Pointer to the current keybinds
            _refresh (Refresh()): Pointer to the game refresh variables
    """

    def __init__(self, screen,
                 button, panel,
                 textbox, yellow_power_up_indicator,
                 blue_power_up_indicator, extra_power_up_indicator,
                 settings, settings_toggle,
                 statistics, shop,
                 shop_config, controls,
                 controls_toggle, refresh):

        """
            Passes in all the necessary pointers to update and refresh the text.

            :param screen: Pointer to the current displayed screen and the screen changing functions.
            :type screen: ScreenUpdate()

            :param button: Pointer to all the button objects currently on the screen.
            :type button: SpawnButton()

            :param panel: Pointer to all the panel objects currently on the screen.
            :type panel: SpawnPanel()

            :param textbox: Pointer to all the text boxes currently on the screen.
            :type textbox: SpawnTextBox()

            :param yellow_power_up_indicator: Pointer to the yellow power up indicator.
            :type yellow_power_up_indicator: SpawnYellowPowerUpIndicator()

            :param blue_power_up_indicator: Pointer to the blue power up indicator.
            :type blue_power_up_indicator: SpawnBluePowerUpIndicator()

            :param extra_power_up_indicator: Pointer to the extra power up indicator.
            :type extra_power_up_indicator: SpawnExtraPowerUpIndicator()

            :param settings: Pointer to the current game settings.
            :type settings: Settings()

            :param settings_toggle: Pointer to the settings updater.
            :type settings_toggle: SettingsToggle()

            :param statistics: Pointer to the current game statistics.
            :type statistics: Stats()

            :param shop: Pointer to the shop manager and updater.
            :type shop: Shop()

            :param shop_config: Pointer to the current shop configuration.
            :type shop_config: ShopConfig()

            :param controls: Pointer to the controls manager and updater.
            :type controls: Controls()

            :param controls_toggle: Pointer to the current keybinds.
            :type controls_toggle: ControlsToggle()

            :param refresh: Pointer to the game refresh variables.
            :type refresh: Refresh()
        """

        self._screen = screen
        self._button = button
        self._panel = panel
        self._textbox = textbox
        self._yellow_power_up_indicator = yellow_power_up_indicator
        self._blue_power_up_indicator = blue_power_up_indicator
        self._extra_power_up_indicator = extra_power_up_indicator
        self._settings = settings
        self._settings_toggle = settings_toggle
        self._statistics = statistics
        self._shop = shop
        self._shop_config = shop_config
        self._controls = controls
        self._controls_toggle = controls_toggle
        self._refresh = refresh

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._screen
        del self._button
        del self._panel
        del self._textbox
        del self._yellow_power_up_indicator
        del self._blue_power_up_indicator
        del self._extra_power_up_indicator
        del self._settings
        del self._settings_toggle
        del self._statistics
        del self._shop
        del self._shop_config
        del self._controls
        del self._controls_toggle
        del self._refresh

    def update_text(self):
        """
            Refreshes and updates the text on the screen.
            When VSync is on, this function is only run at the refresh rate times a second.
            Part of the "screen refresher" section in the main game loop.
            This function includes the button text, panel text, and the text boxes on the screen.

            :return: None
        """

        # Update based on the current mode
        if self._screen.mode == "Title_Mode":
            # Refreshes button text
            if self._refresh.refresh_button == 1 or self._refresh.refresh_button == 2:
                for bu in self._button.buttons_on_screen_list:
                    bu.write_lines()
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 2
            elif self._refresh.refresh_button == 2:
                self._refresh.refresh_button = 0
            # Refreshes text boxes
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Laser Fighter", 72, "bold")
                elif t.id == 2:
                    t.write("Beta 1.2.0b", 24, "normal")
                elif t.id == 3:
                    t.write("God Mode Is On!", 24, "normal")
        elif self._screen.mode == "Machine_Mode":
            if self._refresh.refresh_button == 1:
                for bu in self._button.buttons_on_screen_list:
                    bu.write_lines()
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 0
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Score: {}  High Score: {}".format(self._statistics.score, self._statistics.high_score_machine_war), 24, "normal")
                elif t.id == 2:
                    for yi in self._yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                        if yi.get_power_up_active() == 1:
                            t.write("{}".format(yi.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 3:
                    for bi in self._blue_power_up_indicator.blue_power_up_indicator_turtle:
                        if bi.get_power_up_active() == 1:
                            t.write("{}".format(bi.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 4:
                    for ei in self._extra_power_up_indicator.extra_power_up_indicator_turtle:
                        if ei.get_power_up_active() == 1:
                            t.write("{}".format(ei.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 5:
                    t.write_left("{}".format(self._shop_config.total_coins), 24, "normal")
                elif t.id == 6:
                    t.write("God Mode Is On!", 24, "normal")
        elif self._screen.mode == "Alien_Mode":
            if self._refresh.refresh_button == 1:
                for bu in self._button.buttons_on_screen_list:
                    bu.write_lines()
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 0
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Score: {}  High Score: {}".format(self._statistics.score, self._statistics.high_score_alien_mode), 24, "normal")
                elif t.id == 2:
                    for yi in self._yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                        if yi.get_power_up_active() == 1:
                            t.write("{}".format(yi.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 3:
                    for bi in self._blue_power_up_indicator.blue_power_up_indicator_turtle:
                        if bi.get_power_up_active() == 1:
                            t.write("{}".format(bi.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 4:
                    for ei in self._extra_power_up_indicator.extra_power_up_indicator_turtle:
                        if ei.get_power_up_active() == 1:
                            t.write("{}".format(ei.get_power_up_timer()), 24, "normal")
                        else:
                            t.write("0", 24, "normal")
                elif t.id == 5:
                    t.write_left("{}".format(self._shop_config.total_coins), 24, "normal")
                elif t.id == 6:
                    t.write("God Mode Is On!", 24, "normal")
        elif self._screen.mode == "Shop":
            if self._refresh.refresh_button == 1:
                for bu in self._button.buttons_on_screen_list:
                    if bu.get_type() != "Shop_Slot" and bu.get_type() != "Buy":
                        bu.write_lines()
                    # Refreshes indicators
                    if bu.get_type() == "Power_Up_Slot":
                        if bu.get_id() == 1:
                            bu.write_indicator(self._shop_config.yellow_power_up_level)
                        elif bu.get_id() == 2:
                            bu.write_indicator(self._shop_config.blue_power_up_level)
                        elif bu.get_id() == 3:
                            bu.write_indicator(self._shop_config.green_power_up_level)
                        elif bu.get_id() == 4:
                            bu.write_indicator(self._shop_config.red_power_up_level)
                    if bu.get_type() == "Buy":
                        bu.write_buy(self._shop.price_displayed)
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 0
            # Refreshes panel text
            if self._refresh.refresh_panel == 1:
                for pa in self._panel.panel_turtle:
                    pa.write_text()
                self._refresh.refresh_panel = 0
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Shop", 72, "bold")
                elif t.id == 2:
                    t.write_left("{}".format(self._shop_config.total_coins), 24, "normal")
                if self._refresh.refresh_text == 1:
                    if self._screen.page == "Machine_Mode":
                        if t.id == 3:
                            t.write_left("Machine Mode", 36, "bold")
                        elif t.id == 5:
                            t.write_left(" 5000", 22, "normal")
                        elif t.id == 6:
                            t.write_left(" 15000", 22, "normal")
                        elif t.id == 7:
                            t.write_left(" 40000", 22, "normal")
                        elif t.id == 8:
                            t.write_left(" 100000", 22, "normal")
                    elif self._screen.page == "Alien_Mode":
                        if t.id == 3:
                            t.write_left("Alien Mode", 36, "bold")
                        elif t.id == 5:
                            t.write_left(" 5000", 22, "normal")
                        elif t.id == 6:
                            t.write_left(" 15000", 22, "normal")
                        elif t.id == 7:
                            t.write_left(" 40000", 22, "normal")
                        elif t.id == 8:
                            t.write_left(" 100000", 22, "normal")
                    elif self._screen.page == "Power_Ups":
                        if t.id == 3:
                            t.write_left("Power Ups", 36, "bold")
                        elif t.id == 4:
                            if self._shop_config.yellow_power_up_level == 1:
                                t.write_left(" 1000", 22, "normal")
                            elif self._shop_config.yellow_power_up_level == 2:
                                t.write_left(" 5000", 22, "normal")
                            elif self._shop_config.yellow_power_up_level == 3:
                                t.write_left(" 15000", 22, "normal")
                            elif self._shop_config.yellow_power_up_level == 4:
                                t.write_left(" 30000", 22, "normal")
                        elif t.id == 5:
                            if self._shop_config.blue_power_up_level == 1:
                                t.write_left(" 1000", 22, "normal")
                            elif self._shop_config.blue_power_up_level == 2:
                                t.write_left(" 5000", 22, "normal")
                            elif self._shop_config.blue_power_up_level == 3:
                                t.write_left(" 15000", 22, "normal")
                            elif self._shop_config.blue_power_up_level == 4:
                                t.write_left(" 30000", 22, "normal")
                        elif t.id == 6:
                            if self._shop_config.green_power_up_level == 1:
                                t.write_left(" 1000", 22, "normal")
                            elif self._shop_config.green_power_up_level == 2:
                                t.write_left(" 5000", 22, "normal")
                            elif self._shop_config.green_power_up_level == 3:
                                t.write_left(" 15000", 22, "normal")
                            elif self._shop_config.green_power_up_level == 4:
                                t.write_left(" 30000", 22, "normal")
                        elif t.id == 7:
                            if self._shop_config.red_power_up_level == 1:
                                t.write_left(" 1000", 22, "normal")
                            elif self._shop_config.red_power_up_level == 2:
                                t.write_left(" 5000", 22, "normal")
                            elif self._shop_config.red_power_up_level == 3:
                                t.write_left(" 15000", 22, "normal")
                            elif self._shop_config.red_power_up_level == 4:
                                t.write_left(" 30000", 22, "normal")
            if self._refresh.refresh_text == 1:
                self._refresh.refresh_text = 0
        elif self._screen.mode == "Stats":
            if self._refresh.refresh_button == 1:
                for bu in self._button.buttons_on_screen_list:
                    bu.write_lines()
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 0
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Statistics", 72, "bold")
                if self._refresh.refresh_text == 1:
                    if t.id == 2:
                        t.write("Machine Mode", 48, "bold")
                    elif t.id == 3:
                        t.write("Alien Mode", 48, "bold")
                    elif t.id == 4:
                        t.write("High Score: {}".format(self._statistics.high_score_machine_war), 24, "normal")
                    elif t.id == 5:
                        t.write("Bosses Killed: {}".format(self._statistics.bosses_killed), 24, "normal")
                    elif t.id == 6:
                        t.write("Red Bots Killed: {}".format(self._statistics.red_bots_killed), 24, "normal")
                    elif t.id == 7:
                        t.write("Yellow Bots Killed: {}".format(self._statistics.yellow_bots_killed), 24, "normal")
                    elif t.id == 8:
                        t.write("Blue Bots Killed: {}".format(self._statistics.blue_bots_killed), 24, "normal")
                    elif t.id == 9:
                        t.write("Deaths: {}".format(self._statistics.classic_deaths), 24, "normal")
                    elif t.id == 10:
                        t.write("Damage Taken: {}".format(self._statistics.machine_damage_taken), 24, "normal")
                    elif t.id == 11:
                        t.write("Lasers Fired: {}".format(self._statistics.classic_lasers_fired), 24, "normal")
                    elif t.id == 12:
                        t.write("Power Ups Picked Up: {}".format(self._statistics.classic_power_ups_picked_up), 24, "normal")
                    elif t.id == 13:
                        t.write("Coins Collected: {}".format(self._statistics.machine_coins_collected), 24, "normal")
                    elif t.id == 14:
                        t.write("High Score: {}".format(self._statistics.high_score_alien_mode), 24, "normal")
                    elif t.id == 15:
                        t.write("UFOs Killed: {}".format(self._statistics.ufos_killed), 24, "normal")
                    elif t.id == 16:
                        t.write("Big Aliens Killed: {}".format(self._statistics.big_aliens_killed), 24, "normal")
                    elif t.id == 17:
                        t.write("Medium Aliens Killed: {}".format(self._statistics.medium_aliens_killed), 24, "normal")
                    elif t.id == 18:
                        t.write("Small Aliens Killed: {}".format(self._statistics.small_aliens_killed), 24, "normal")
                    elif t.id == 19:
                        t.write("Deaths: {}".format(self._statistics.alien_deaths), 24, "normal")
                    elif t.id == 20:
                        t.write("Damage Taken: {}".format(self._statistics.damage_taken), 24, "normal")
                    elif t.id == 21:
                        t.write("Lasers Fired: {}".format(self._statistics.alien_lasers_fired), 24, "normal")
                    elif t.id == 22:
                        t.write("Jumps: {}".format(self._statistics.jumps), 24, "normal")
                    elif t.id == 23:
                        t.write("Power Ups Picked Up: {}".format(self._statistics.alien_power_ups_picked_up), 24, "normal")
                    elif t.id == 24:
                        t.write("Coins Collected: {}".format(self._statistics.alien_coins_collected), 24, "normal")
                        self._refresh.refresh_text = 0
                if t.id == 25:
                    t.write("God Mode Is On!", 24, "normal")
        elif self._screen.mode == "Settings":
            for bu in self._button.buttons_on_screen_list:
                if self._refresh.refresh_button == 1:
                    bu.write_lines()
                if self._refresh.refresh_indicator == 1 or self._refresh.refresh_indicator == 2:
                    if bu.type == "Settings_Toggle":
                        if bu.id == 1:
                            bu.write_indicator(self._settings.button_sound)
                        elif bu.id == 2:
                            bu.write_indicator(self._settings.player_shooting_sound)
                        elif bu.id == 3:
                            bu.write_indicator(self._settings.enemy_shooting_sound)
                        elif bu.id == 4:
                            bu.write_indicator(self._settings.player_death_sound)
                        elif bu.id == 5:
                            bu.write_indicator(self._settings.enemy_death_sound)
                        elif bu.id == 6:
                            bu.write_indicator(self._settings.player_hit_sound)
                        elif bu.id == 7:
                            bu.write_indicator(self._settings.enemy_hit_sound)
                        elif bu.id == 8:
                            bu.write_indicator(self._settings.power_up_pickup_sound)
                        elif bu.id == 9:
                            bu.write_indicator(self._settings.power_up_spawn_sound)
                        elif bu.id == 10:
                            bu.write_indicator(self._settings.coin_pickup_sound)
                        elif bu.id == 11:
                            bu.write_fullscreen_indicator(self._settings.fullscreen, self._settings_toggle.fullscreen_toggled)
                        elif bu.id == 12:
                            bu.write_indicator(self._settings.vsync)
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 0
            if self._refresh.refresh_indicator == 2:
                self._refresh.refresh_indicator = 0
            elif self._refresh.refresh_indicator == 1:
                self._refresh.refresh_indicator = 2
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Settings", 72, "bold")
                elif t.id == 2:
                    t.write("God Mode Is On!", 24, "normal")
        elif self._screen.mode == "Controls":
            if self._refresh.refresh_button == 1 or self._refresh.refresh_button == 2:
                for bu in self._button.buttons_on_screen_list:
                    if bu.type != "Controls_Toggle":
                        bu.write_lines()
                    else:
                        bu.write_control(self._controls_toggle.go_right_key, self._controls_toggle.go_left_key, self._controls_toggle.shoot_key, self._controls_toggle.jump_key)
                        if bu.id == 1:
                            if self._controls.go_right_key_alert == 1:
                                bu.update_controls_text_color(bu.id)
                            else:
                                bu.update_controls_text_color(0)
                        elif bu.id == 2:
                            if self._controls.go_left_key_alert == 1:
                                bu.update_controls_text_color(bu.id)
                            else:
                                bu.update_controls_text_color(0)
                        elif bu.id == 3:
                            if self._controls.shoot_key_alert == 1:
                                bu.update_controls_text_color(bu.id)
                            else:
                                bu.update_controls_text_color(0)
                        elif bu.id == 4:
                            if self._controls.jump_key_alert == 1:
                                bu.update_controls_text_color(bu.id)
                            else:
                                bu.update_controls_text_color(0)
            if self._refresh.refresh_button == 1:
                self._refresh.refresh_button = 2
            elif self._refresh.refresh_button == 2:
                self._refresh.refresh_button = 0
            for t in self._textbox.text_on_screen_list:
                if t.id == 1:
                    t.write("Controls", 72, "bold")
                elif t.id == 2:
                    t.write("God Mode Is On!", 24, "normal")
