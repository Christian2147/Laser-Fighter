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
    File: ScreenManager.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for changing screens in Laser Fighter. It also holds all of the variables used in
        refreshing specific aspects of the screen.
"""

import pygame


class ScreenUpdate:
    """
        Represents the function and logic for the different game screens/modes.
        This includes changing screens and toggling different modes.

        Pointers:
            _screen (ScreenUpdate()): Pointer to the current displayed screen and the screen changing functions
            _button (SpawnButton()): Pointer to all the button objects currently on the screen
            _settings (Settings()): Pointer to the current game settings
            _shop_config (ShopConfig()): Pointer to the current shop configuration
            _refresh (Refresh()): Pointer to the game refresh variables
            _power_up_setup (PowerUpSetup()): The current power up configuration
            _machine_mode_setup (MachineModeSetup()): The current Machine Mode configuration
            _alien_mode_setup (AlienModeSetup()): The current Alien Mode configuration

        Attributes:
            _scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode

            _mode (string): The current mode/screen of the game
            _page (string): The current page being displayed (Applies to the Shop only)
            _screen_update (int): Variable to toggle the full refresh of the screen
            _page_update (int): Variable to toggle the full refresh of the page
            _tick_update (float): Used for  refreshing text when fullscreen is not on (So it does not slow
                down the game)
            _updated_controls (int): Determines whether a restart settings was toggled so that the user can be
                prompted to restart their game when existing to the main menu
            _quit_loop (int): Determines if the program has been terminated
    """

    def __init__(self,
                 screen,
                 button,
                 pop_up,
                 settings,
                 shop_config,
                 refresh,
                 power_up_setup,
                 machine_mode_setup,
                 alien_mode_setup,
                 scale_factor,
                 scale_factor_x,
                 scale_factor_y
    ):
        """
            Initializes all the necessary pointers for the Screen Manager.

            :param screen: Pointer to the current displayed screen and the screen changing functions.
            :type screen: ScreenUpdate()

            :param button: Pointer to all the button objects currently on the screen.
            :type button: SpawnButton()

            :param settings: Pointer to the current game settings.
            :type settings: Settings()

            :param shop_config: Pointer to the current shop configuration.
            :type shop_config: ShopConfig()

            :param refresh: Pointer to the game refresh variables.
            :type refresh: Refresh()

            :param power_up_setup: The current power up configuration.
            :type power_up_setup: PowerUpSetup()

            :param machine_mode_setup: The current Machine Mode configuration.
            :type machine_mode_setup: MachineModeSetup()

            :param alien_mode_setup: The current Alien Mode configuration.
            :type alien_mode_setup: AlienModeSetup()

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode.
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode.
            :type scale_factor_y: float
        """

        self._screen = screen
        self._button = button
        self._pop_up = pop_up
        self._settings = settings
        self._shop_config = shop_config
        self._refresh = refresh
        self._power_up_setup = power_up_setup
        self._machine_mode_setup = machine_mode_setup
        self._alien_mode_setup = alien_mode_setup

        self._scale_factor = scale_factor
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self._mode = "Title_Mode"
        self._page = "Machine_Mode"
        self._screen_update = 0
        self._page_update = 0
        self._tick_update = 0
        self._updated_controls = 0
        self._quit_loop = 0

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._screen
        del self._button
        del self._pop_up
        del self._settings
        del self._shop_config
        del self._refresh
        del self._power_up_setup
        del self._machine_mode_setup
        del self._alien_mode_setup
        del self._scale_factor_x
        del self._scale_factor_y
        del self._mode
        del self._page
        del self._screen_update
        del self._page_update
        del self._updated_controls
        del self._quit_loop

    @property
    def mode(self):
        """mode getter"""
        return self._mode

    @mode.setter
    def mode(self, value):
        """mode setter"""
        if isinstance(value, str):
            self._mode = value
        else:
            raise ValueError("Mode must be a string")

    @property
    def page(self):
        """page getter"""
        return self._page

    @page.setter
    def page(self, value):
        """page setter"""
        if isinstance(value, str):
            self._page = value
        else:
            raise ValueError("Mode must be a string")

    @property
    def screen_update(self):
        """screen_update getter"""
        return self._screen_update

    @screen_update.setter
    def screen_update(self, value):
        """screen_update setter"""
        if isinstance(value, int):
            self._screen_update = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def page_update(self):
        """page_update getter"""
        return self._page_update

    @page_update.setter
    def page_update(self, value):
        """page_update setter"""
        if isinstance(value, int):
            self._page_update = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def tick_update(self):
        """tick_update getter"""
        return self._tick_update

    @tick_update.setter
    def tick_update(self, value):
        """tick_update setter"""
        if isinstance(value, int):
            self._tick_update = value
        else:
            raise ValueError("Value must be an integer.")

    @property
    def updated_controls(self):
        """updated_controls getter"""
        return self._updated_controls

    @updated_controls.setter
    def updated_controls(self, value):
        """updated_controls setter"""
        if isinstance(value, int):
            self._updated_controls = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def quit(self):
        return self._quit_loop

    def launch_title_mode(self):
        """
            Function used to go back to the title screen from a different screen.

            :return: None
        """

        if self._mode == "Machine_Mode" or self._mode == "Alien_Mode" or self._mode == "Stats" or self._mode == "Shop":
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Set the mode to "Title_Mode" to change the screen
            self._mode = "Title_Mode"
            self._screen_update = 1
            # Setup the power ups and both Machine Mode and Alien Mode
            self._power_up_setup.setup_power_ups()
            self._machine_mode_setup.setup_machine_mode()
            self._alien_mode_setup.setup_alien_mode()
        # If coming from settings or controls, there may be a special procedure needed
        if self._mode == "Settings" or self._mode == "Controls":
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # If certain settings were updated, a restart may be required.
            #  "updated_controls" checks if this is the case.
            if self._updated_controls == 1:
                confirm_text = [
                    "A restart is",
                    "required for these",
                    "changes to take",
                    "effect! Do you",
                    "want to restart",
                    "now?"
                ]

                self._pop_up.spawn_pop_up(
                    icon="warning",
                    text=confirm_text,
                    type=1,
                    on_yes=self.restart_yes_select,
                    on_no=self.restart_no_select
                )
            else:
                self._mode = "Title_Mode"
                self._screen_update = 1
                # Setup the power ups and both Machine Mode and Alien Mode
                self._power_up_setup.setup_power_ups()
                self._machine_mode_setup.setup_machine_mode()
                self._alien_mode_setup.setup_alien_mode()

    def restart_yes_select(self):
        # If the user selects "yes" to restart
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        for pu in self._pop_up.pop_up_on_screen_list:
            pu.remove()
        self._pop_up.pop_up_on_screen_list.clear()
        self._quit_loop = 1

    def restart_no_select(self):
        # If the user selects "no" to restart
        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        for pu in self._pop_up.pop_up_on_screen_list:
            pu.remove()
        self._pop_up.pop_up_on_screen_list.clear()

        # Set the mode to "Title_Mode" to change the screen
        self._mode = "Title_Mode"
        self._screen_update = 1
        # Setup the power ups and both Machine Mode and Alien Mode
        self._power_up_setup.setup_power_ups()
        self._machine_mode_setup.setup_machine_mode()
        self._alien_mode_setup.setup_alien_mode()
        self._updated_controls = 0

    def launch_machine_mode(self):
        """
            Function used to enter Machine Mode.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        self._mode = "Machine_Mode"
        self._screen_update = 1

    def launch_alien_mode(self):
        """
            Function used to enter Alien Mode.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # If Alien Mode has been unlocked
        if self._shop_config.alien_slot_selected != 0:
            # Enter Alien Mode
            self._mode = "Alien_Mode"
            self._screen_update = 1

    def launch_shop_mode(self):
        """
            Function used to enter the shop in Laser Fighter.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Enter The Shop
        self._mode = "Shop"
        # Display the Machine Mode page by default
        self._page = "Machine_Mode"
        self._screen_update = 1
        self._refresh.refresh_panel = 1
        self._refresh.refresh_text = 1
        self._refresh.move_slot_selector = 1

    def display_machine_mode_page(self):
        """
            Displays the Machine Mode Upgrades page while in the shop.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Enter the Machine Mode page
        self._page = "Machine_Mode"
        self._screen_update = 1
        self._page_update = 1
        self._refresh.refresh_text = 1
        self._refresh.move_tab_selector = 1
        self._refresh.move_slot_selector = 1

    def display_alien_mode_page(self):
        """
            Displays the Alien Mode Upgrades page while in the shop.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Enter the Alien Mode page
        self._page = "Alien_Mode"
        self._screen_update = 1
        self._page_update = 1
        self._refresh.refresh_text = 1
        self._refresh.move_tab_selector = 1
        self._refresh.move_slot_selector = 1

    def display_power_up_page(self):
        """
            Displays the Power Up Upgrades page while in the shop.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Enter the Power Ups page
        self._page = "Power_Ups"
        self._screen_update = 1
        self._page_update = 1
        self._refresh.refresh_text = 1
        self._refresh.move_tab_selector = 1

    def display_gadgets_page(self):
        """
            Displays the Gadgets page while in the shop.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Enter the Gadgets page
        self._page = "Gadgets"
        self._screen_update = 1
        self._page_update = 1
        self._refresh.refresh_text = 1
        self._refresh.move_tab_selector = 1

    def launch_stats_mode(self):
        """
            Function used to enter the statistics screen.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        self._mode = "Stats"
        self._screen_update = 1
        self._refresh.refresh_text = 1

    def launch_settings_mode(self):
        """
            Function used to enter the settings screen.

            :return: None
        """

        if self._mode == "Title_Mode":
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            self._mode = "Settings"
            self._screen_update = 1
        elif self._mode == "Controls":
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            self._mode = "Settings"
            self._screen_update = 1
            self._button.clickable = 1

    def launch_controls_mode(self):
        """
            Function used to enter the controls screen.

            :return: None
        """

        if self._settings.button_sound == 1:
            sound = pygame.mixer.Sound("sound/Button_Sound.wav")
            sound.play()
        # Go to the controls screen
        self._mode = "Controls"
        self._screen_update = 1
        # Used so that there is no delay in clicking this button from the settings screen
        self._button.clickable = 2
