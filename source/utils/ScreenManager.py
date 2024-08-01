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


class ScreenUpdate:
    def __init__(self, screen, button, settings, refresh, machine_mode_setup, alien_mode_setup, scale_factor_x, scale_factor_y):
        self._screen = screen
        self._button = button
        self._settings = settings
        self._refresh = refresh
        self._machine_mode_setup = machine_mode_setup
        self._alien_mode_setup = alien_mode_setup
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
        del self._screen
        del self._button
        del self._settings
        del self._refresh
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
        return self._mode

    @mode.setter
    def mode(self, value):
        if isinstance(value, str):
            self._mode = value
        else:
            raise ValueError("Mode must be a string")

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, str):
            self._page = value
        else:
            raise ValueError("Mode must be a string")

    @property
    def screen_update(self):
        return self._screen_update

    @screen_update.setter
    def screen_update(self, value):
        if isinstance(value, int):
            self._screen_update = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def page_update(self):
        return self._page_update

    @page_update.setter
    def page_update(self, value):
        if isinstance(value, int):
            self._page_update = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def tick_update(self):
        return self._tick_update

    @tick_update.setter
    def tick_update(self, value):
        if isinstance(value, int):
            self._tick_update = value
        else:
            raise ValueError("Value must be an integer.")

    @property
    def updated_controls(self):
        return self._updated_controls

    @updated_controls.setter
    def updated_controls(self, value):
        if isinstance(value, int):
            self._updated_controls = value
        else:
            raise ValueError("Mode must be a integer")

    @property
    def quit_loop(self):
        return self._quit_loop

    def launch_title_mode(self, x, y):
        """
            Function used to go back to the title screen from a different screen.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        if self._mode == "Machine_Mode" or self._mode == "Alien_Mode" or self._mode == "Stats" or self._mode == "Shop":
            # Check to see if the cursor is in the bound of the button to be clicked
            if (x > -634 * self._scale_factor_x) and (x < -442 * self._scale_factor_x) and (y > 323 * self._scale_factor_y) and (y < 355 * self._scale_factor_y):
                if self._settings.button_sound == 1:
                    sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                    sound.play()
                # Set the mode to "Title_Mode" to change the screen
                self._mode = "Title_Mode"
                self._screen_update = 1
                self._machine_mode_setup.setup_machine_mode()
                self._alien_mode_setup.setup_alien_mode()
                self._screen.onscreenclick(None)
        # If coming from settings or controls, there may be a special procedure needed
        if self._mode == "Settings" or self._mode == "Controls":
            # Check to see if the cursor is in the bound of the button to be clicked
            if (x > 26 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -315 * self._scale_factor_y) and (y < -254 * self._scale_factor_y):
                if self._settings.button_sound == 1:
                    sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                    sound.play()
                # If certain settings were updated, a restart may be required.
                # "updated_controls" checks if this is the case.
                if self._updated_controls == 1:
                    # Warn the user that a restart is required
                    message_output = ctypes.windll.user32.MessageBoxW(0, "A restart is required for these changes to take effect!\nDo you want to restart now?", "Restart Required!", 4 + 48)
                    # If the user selects "yes"
                    if message_output == 6:
                        self.on_quit()
                    # If the user selects "no"
                    elif message_output == 7:
                        # Set the mode to "Title_Mode" to change the screen
                        self._mode = "Title_Mode"
                        self._screen_update = 1
                        self._machine_mode_setup.setup_machine_mode()
                        self._alien_mode_setup.setup_alien_mode()
                        self._screen.onscreenclick(None)
                        self._updated_controls = 0
                else:
                    self._mode = "Title_Mode"
                    self._screen_update = 1
                    self._machine_mode_setup.setup_machine_mode()
                    self._alien_mode_setup.setup_alien_mode()
                    self._screen.onscreenclick(None)

    def launch_machine_mode(self, x, y):
        """
            Function used to enter Machine Mode.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -252 * self._scale_factor_x) and (x < 250 * self._scale_factor_x) and (y > 49 * self._scale_factor_y) and (y < 121 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Enter Machine Mode
            self._mode = "Machine_Mode"
            self._screen_update = 1

    def launch_alien_mode(self, x, y):
        """
            Function used to enter Alien Mode.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -252 * self._scale_factor_x) and (x < 250 * self._scale_factor_x) and (y > -42 * self._scale_factor_y) and (y < 30 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Enter Alien Mode
            self._mode = "Alien_Mode"
            self._screen_update = 1

    def launch_shop_mode(self, x, y):
        """
            Function used to enter the shop in Laser Fighter.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -252 * self._scale_factor_x) and (x < 250 * self._scale_factor_x) and (y > -133 * self._scale_factor_y) and (y < -61 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Enter The Shop
            self._mode = "Shop"
            self._page = "Machine_Mode"
            self._screen_update = 1
            self._refresh.refresh_panel = 1
            self._refresh.refresh_text = 1
            self._refresh.move_slot_selector = 1

    def display_machine_mode_page(self, x, y):
        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -641 * self._scale_factor_x) and (x < -566 * self._scale_factor_x) and (y > 99 * self._scale_factor_y) and (y < 201 * self._scale_factor_y):
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

    def display_alien_mode_page(self, x, y):
        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -641 * self._scale_factor_x) and (x < -566 * self._scale_factor_x) and (y > -21 * self._scale_factor_y) and (y < 81 * self._scale_factor_y):
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

    def display_power_up_page(self, x, y):
        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -641 * self._scale_factor_x) and (x < -566 * self._scale_factor_x) and (y > -141 * self._scale_factor_y) and (y < -39 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Enter the Power Ups page
            self._page = "Power_Ups"
            self._screen_update = 1
            self._page_update = 1
            self._refresh.refresh_text = 1
            self._refresh.move_tab_selector = 1

    def launch_stats_mode(self, x, y):
        """
            Function used to enter the statistics screen.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 9 * self._scale_factor_x) and (x < 250 * self._scale_factor_x) and (y > -224 * self._scale_factor_y) and (y < -150 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Go to the statistics screen
            self._mode = "Stats"
            self._screen_update = 1
            self._refresh.refresh_text = 1

    def launch_settings_mode(self, x, y):
        """
            Function used to enter the settings screen.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # If entering from the title screen
        if self._mode == "Title_Mode":
            # Check to see if the cursor is in the bound of the button to be clicked
            if (x > -252 * self._scale_factor_x) and (x < -10 * self._scale_factor_x) and (y > -224 * self._scale_factor_y) and (y < -150 * self._scale_factor_y):
                if self._settings.button_sound == 1:
                    sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                    sound.play()
                # Change to settings
                self._mode = "Settings"
                self._screen_update = 1
        # If entering from the controls screen
        if self._mode == "Controls":
            # Check to see if the cursor is in the bound of the button to be clicked
            if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -235 * self._scale_factor_y) and (y < -173 * self._scale_factor_y):
                if self._settings.button_sound == 1:
                    sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                    sound.play()
                # Change to settings
                self._mode = "Settings"
                self._screen_update = 1
                # Used so that there is no delay in clicking this button from the controls screen
                self._button.clickable = 1

    def launch_controls_mode(self, x, y):
        """
            Function used to enter the controls screen.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * self._scale_factor_x) and (x < 600 * self._scale_factor_x) and (y > -235 * self._scale_factor_y) and (y < -173 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Go to the controls screen
            self._mode = "Controls"
            self._screen_update = 1
            # Used so that there is no delay in clicking this button from the settings screen
            self._button.clickable = 2

    def exit_game(self, x, y):
        """
            Function used to force exit the game.

            :param x: The current x-coordinate of the cursor
            :type x: float

            :param y: The current y-coordinate of the cursor
            :type y: float

            :return: None
        """

        self._screen.onscreenclick(None)
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -252 * self._scale_factor_x) and (x < 250 * self._scale_factor_x) and (y > -315 * self._scale_factor_y) and (y < -241 * self._scale_factor_y):
            if self._settings.button_sound == 1:
                sound = pygame.mixer.Sound("sound/Button_Sound.wav")
                sound.play()
            # Quit the game and exit the application
            self.on_quit()

    def on_quit(self):
        """
            Closes the game and terminates the turtle graphics window properly

            :return: None
        """

        # Quit loop means the game loop must be closed
        self._quit_loop = 1
        # After 300 milliseconds, destroy the window and terminate the program
        self._screen._root.after(300, self._screen._root.destroy)
