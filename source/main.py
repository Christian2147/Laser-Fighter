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

# Created By: Christian Marinkovich (@Christian2147 On GitHub) This is the main source file for Laser Fighter.
# This is game version beta 1.1.0 released on 07/27/24

"""
    File: main.py
    Author: Christian Marinkovich
    Date: 2024-07-11
    Description:
    This file is the main file for Laser Fighter.
    The main file contains the main game functions, like the controls and spawning sprites, and also includes of the
        main game loop.
"""

import ctypes
import time
import random
from setup.Initialization import *
from setup.ScreenSetup import *
from components.gui.InterfaceButton import Button
from components.gui.InterfacePanel import Panel
from components.gui.InterfaceTextBox import Text
from components.gui.InterfaceSelect import Selector
from components.gui.InterfacePriceLabel import PriceLabel
from components.ItemCoin import CoinIndicator
from components.ItemPowerUp import PowerUp
from components.ItemPowerUp import YellowIndicator
from components.ItemPowerUp import BlueIndicator
from components.ItemPowerUp import ExtraIndicator
from components.player.MachinePlayer import Player
from components.player.HumanPlayer import Human
from components.enemy.MachineBlueMachine import BlueMachine
from components.enemy.MachineYellowMachine import YellowMachine
from components.enemy.MachineRedMachine import RedMachine
from components.enemy.MachineBoss import Boss
from components.enemy.AlienSmallAlien import SmallAlien
from components.enemy.AlienMediumAlien import MediumAlien
from components.enemy.AlienLargeAlien import LargeAlien
from components.enemy.AlienUFO import UFO
from components.EffectBackgroundEffect import Earth
from components.EffectBackgroundEffect import Sun
from components.EffectBackgroundEffect import BackgroundObjects

"""
    The functions below are for the player controls.
"""


def go_right():
    """
        Function for moving right in Laser Fighter. Activates when the keybind to move right is triggered.

        :return: None
    """

    if mode == "Machine_Mode":
        for p in current_player:
            # The machine player is prepared to move right and faces right
            p.set_direction_right()
        move()
    if mode == "Alien_Mode":
        for h in current_human:
            # Prepares the human player to move right
            h.go_right(scale_factor_X, scale_factor_Y)


def go_left():
    """
        Function for moving left in Laser Fighter. Activates when the keybind to move left is triggered.

        :return: None
    """

    if mode == "Machine_Mode":
        for p in current_player:
            # The machine player is prepared to move left and faces left
            p.set_direction_left()
        move()
    if mode == "Alien_Mode":
        for h in current_human:
            # Prepares the human player to move left
            h.go_left(scale_factor_X, scale_factor_Y)


def move():
    """
        Function used to trigger the players movement in Machine Mode.

        :return: None
    """

    # Player is moved in its current facing direction when this function is activated.
    if mode == "Machine_Mode":
        for p in current_player:
            p.move_player(scale_factor_X)


def jump():
    """
        Function used to activate the players jump in Alien Mode.

        :return: None
    """

    if mode == "Alien_Mode":
        # The global keyword is used for parameters that are to simply be accessed globally.
        global jumps
        for h in current_human:
            # Prepare the player for a jump
            h.jump(scale_factor_X)
            # If the jump can successfully be preformed given the circumstances required to preform it
            if god_mode == 0 and h.do_jump == 1:
                # Update the game statistics to show that the player has jumped
                jumps = jumps + 1
                # New config parser object is created
                config = configparser.ConfigParser()
                # Data from config file is extracted
                config.read('Config/playerData.ini')
                # The statistic to edit is extracted
                statistic_to_update = list(config['Statistics_Alien_Mode'])[7]
                # The statistic to edit is updated
                config['Statistics_Alien_Mode'][statistic_to_update] = str(jumps)
                # The new data is written back to the ini file
                with open('Config/playerData.ini', 'w') as configfile:
                    config.write(configfile)


def shoot():
    """
        Function used to fire the players laser.

        :return: None
    """

    global shoot_update
    global laser_direction
    global head_death_animation
    global classic_lasers_fired
    global alien_lasers_fired
    if mode == "Machine_Mode":
        for p in current_player:
            # If the laser is not currently moving across the screen and if the player is not dying
            if p.get_laser().ycor() > 359 * scale_factor_Y and p.get_death_animation() == 0:
                # The laser is fired
                p.fire(player_shooting_sound, scale_factor_Y)
                # Update the game statistics
                if god_mode == 0:
                    classic_lasers_fired = classic_lasers_fired + 1
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    statistic_to_update = list(config['Statistics_Machine_Mode'])[6]
                    config['Statistics_Machine_Mode'][statistic_to_update] = str(classic_lasers_fired)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
    if mode == "Alien_Mode":
        for h in current_human:
            # If the laser is not currently flying across the screen and if the player is not in the process of dying
            if h.shoot_update == 0 and h.death_animation == 0 and h.direction != 0:
                # Fire the laser
                h.shoot(player_shooting_sound, scale_factor_X, scale_factor_Y)
                # Change "got_hit" for the UFO back to 0 since this is a new laser being fired
                for u in ufos:
                    u.set_got_hit(0)
                # Update the game statistics
                if god_mode == 0:
                    alien_lasers_fired = alien_lasers_fired + 1
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    statistic_to_update = list(config['Statistics_Alien_Mode'])[6]
                    config['Statistics_Alien_Mode'][statistic_to_update] = str(alien_lasers_fired)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)


"""
    The functions below are for switching screens.
"""


def launch_title_mode(x, y):
    """
        Function used to go back to the title screen from a different screen.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global updated_controls
    global message_output
    global screen_update
    wn.onscreenclick(None)
    if mode == "Machine_Mode" or mode == "Alien_Mode" or mode == "Stats" or mode == "Shop":
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -634 * scale_factor_X) and (x < -442 * scale_factor_X) and (y > 323 * scale_factor_Y) and (y < 355 * scale_factor_Y):
            if button_sound == 1:
                sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
                sound.play()
            # Set the mode to "Title_Mode" to change the screen
            mode = "Title_Mode"
            screen_update = 1
            wn.onscreenclick(None)
    # If coming from settings or controls, there may be a special procedure needed
    if mode == "Settings" or mode == "Controls":
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 26 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > -315 * scale_factor_Y) and (y < -254 * scale_factor_Y):
            if button_sound == 1:
                sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
                sound.play()
            # If certain settings were updated, a restart may be required.
            # "updated_controls" checks if this is the case.
            if updated_controls == 1:
                # Warn the user that a restart is required
                message_output = ctypes.windll.user32.MessageBoxW(0, "A restart is required for these changes to take effect!\nDo you want to restart now?", "Restart Required!", 4+48)
                # If the user selects "yes"
                if message_output == 6:
                    on_quit()
                # If the user selects "no"
                elif message_output == 7:
                    # Set the mode to "Title_Mode" to change the screen
                    mode = "Title_Mode"
                    screen_update = 1
                    wn.onscreenclick(None)
                    updated_controls = 0
                    message_output = 0
            else:
                mode = "Title_Mode"
                screen_update = 1
                wn.onscreenclick(None)


def launch_machine_mode(x, y):
    """
        Function used to enter Machine Mode.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global screen_update
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -252 * scale_factor_X) and (x < 250 * scale_factor_X) and (y > 49 * scale_factor_Y) and (y < 121 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter Machine Mode
        mode = "Machine_Mode"
        screen_update = 1


def launch_alien_mode(x, y):
    """
        Function used to enter Alien Mode.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global screen_update
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -252 * scale_factor_X) and (x < 250 * scale_factor_X) and (y > -42 * scale_factor_Y) and (y < 30 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter Alien Mode
        mode = "Alien_Mode"
        screen_update = 1


def launch_shop_mode(x, y):
    """
        Function used to enter the shop in Laser Fighter.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global page
    global screen_update
    global refresh_variables
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -252 * scale_factor_X) and (x < 250 * scale_factor_X) and (y > -133 * scale_factor_Y) and (y < -61 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter The Shop
        mode = "Shop"
        page = "Machine_Mode"
        screen_update = 1
        refresh_variables.refresh_panel = 1
        refresh_variables.refresh_text = 1
        refresh_variables.move_slot_selector = 1


def display_machine_mode_page(x, y):
    global page
    global screen_update
    global page_update
    global refresh_variables
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -641 * scale_factor_X) and (x < -566 * scale_factor_X) and (y > 99 * scale_factor_Y) and (y < 201 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter the Machine Mode page
        page = "Machine_Mode"
        screen_update = 1
        page_update = 1
        refresh_variables.refresh_text = 1
        refresh_variables.move_tab_selector = 1
        refresh_variables.move_slot_selector = 1


def display_alien_mode_page(x, y):
    global page
    global screen_update
    global page_update
    global refresh_variables
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -641 * scale_factor_X) and (x < -566 * scale_factor_X) and (y > -21 * scale_factor_Y) and (y < 81 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter the Alien Mode page
        page = "Alien_Mode"
        screen_update = 1
        page_update = 1
        refresh_variables.refresh_text = 1
        refresh_variables.move_tab_selector = 1
        refresh_variables.move_slot_selector = 1


def display_power_up_page(x, y):
    global page
    global screen_update
    global page_update
    global refresh_variables
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -641 * scale_factor_X) and (x < -566 * scale_factor_X) and (y > -141 * scale_factor_Y) and (y < -39 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Enter the Power Ups page
        page = "Power_Ups"
        screen_update = 1
        page_update = 1
        refresh_variables.refresh_text = 1
        refresh_variables.move_tab_selector = 1


def launch_stats_mode(x, y):
    """
        Function used to enter the statistics screen.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global screen_update
    global refresh_variables
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 9 * scale_factor_X) and (x < 250 * scale_factor_X) and (y > -224 * scale_factor_Y) and (y < -150 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Go to the statistics screen
        mode = "Stats"
        screen_update = 1
        refresh_variables.refresh_text = 1


def launch_settings_mode(x, y):
    """
        Function used to enter the settings screen.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global screen_update
    global clickable
    wn.onscreenclick(None)
    # If entering from the title screen
    if mode == "Title_Mode":
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > -252 * scale_factor_X) and (x < -10 * scale_factor_X) and (y > -224 * scale_factor_Y) and (y < -150 * scale_factor_Y):
            if button_sound == 1:
                sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
                sound.play()
            # Change to settings
            mode = "Settings"
            screen_update = 1
    # If entering from the controls screen
    if mode == "Controls":
        # Check to see if the cursor is in the bound of the button to be clicked
        if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > -235 * scale_factor_Y) and (y < -173 * scale_factor_Y):
            if button_sound == 1:
                sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
                sound.play()
            # Change to settings
            mode = "Settings"
            screen_update = 1
            # Used so that there is no delay in clicking this button from the controls screen
            clickable = 1


def launch_controls_mode(x, y):
    """
        Function used to enter the controls screen.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global mode
    global screen_update
    global clickable
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > -235 * scale_factor_Y) and (y < -173 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Go to the controls screen
        mode = "Controls"
        screen_update = 1
        # Used so that there is no delay in clicking this button from the settings screen
        clickable = 2


def exit_game(x, y):
    """
        Function used to force exit the game.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -252 * scale_factor_X) and (x < 250 * scale_factor_X) and (y > -315 * scale_factor_Y) and (y < -241 * scale_factor_Y):
        if button_sound == 1:
            sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
            sound.play()
        # Quit the game and exit the application
        on_quit()


def slot_1_select(x, y):
    global page
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -503 * scale_factor_X) and (x < -352 * scale_factor_X) and (y > 11 * scale_factor_Y) and (y < 182 * scale_factor_Y):
        if page == "Machine_Mode":
            execute_slot_function("Machine_Mode", 1)
        elif page == "Alien_Mode":
            execute_slot_function("Alien_Mode", 1)
        elif page == "Power_Ups":
            execute_slot_function("Power_Ups", 1)


def slot_2_select(x, y):
    global page
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -333 * scale_factor_X) and (x < -182 * scale_factor_X) and (y > 11 * scale_factor_Y) and (y < 182 * scale_factor_Y):
        if page == "Machine_Mode":
            execute_slot_function("Machine_Mode", 2)
        elif page == "Alien_Mode":
            execute_slot_function("Alien_Mode", 2)
        elif page == "Power_Ups":
            execute_slot_function("Power_Ups", 2)


def slot_3_select(x, y):
    global page
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -163 * scale_factor_X) and (x < -12 * scale_factor_X) and (y > 11 * scale_factor_Y) and (y < 182 * scale_factor_Y):
        if page == "Machine_Mode":
            execute_slot_function("Machine_Mode", 3)
        elif page == "Alien_Mode":
            execute_slot_function("Alien_Mode", 3)
        elif page == "Power_Ups":
            execute_slot_function("Power_Ups", 3)


def slot_4_select(x, y):
    global page
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 7 * scale_factor_X) and (x < 158 * scale_factor_X) and (y > 11 * scale_factor_Y) and (y < 182 * scale_factor_Y):
        if page == "Machine_Mode":
            execute_slot_function("Machine_Mode", 4)
        elif page == "Alien_Mode":
            execute_slot_function("Alien_Mode", 4)
        elif page == "Power_Ups":
            execute_slot_function("Power_Ups", 4)


def slot_5_select(x, y):
    global page
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -503 * scale_factor_X) and (x < -352 * scale_factor_X) and (y > -179 * scale_factor_Y) and (y < -8 * scale_factor_Y):
        if page == "Machine_Mode":
            execute_slot_function("Machine_Mode", 5)
        elif page == "Alien_Mode":
            execute_slot_function("Alien_Mode", 5)


def execute_slot_function(current_page, slot_id):
    global refresh_variables
    # Button sound is played
    if button_sound == 1:
        sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
        sound.play()
    if current_page != "Power_Ups":
        for pa in panel_turtle:
            pa.set_panel_text(current_page, slot_id, scale_factor_X, scale_factor_Y)
        if current_page == "Machine_Mode":
            if shop_config.machine_slots_unlocked[slot_id - 1] == 1:
                shop_config.machine_slot_selected = slot_id
                shop_config.save()
                refresh_variables.move_slot_selector = 1
        elif current_page == "Alien_Mode":
            if shop_config.alien_slots_unlocked[slot_id - 1] == 1:
                shop_config.alien_slot_selected = slot_id
                shop_config.save()
                refresh_variables.move_slot_selector = 1
    else:
        if slot_id == 1:
            for pa in panel_turtle:
                pa.set_panel_text("Yellow_Power_Up", slot_id, scale_factor_X, scale_factor_Y)
        elif slot_id == 2:
            for pa in panel_turtle:
                pa.set_panel_text("Blue_Power_Up", slot_id, scale_factor_X, scale_factor_Y)
        elif slot_id == 3:
            for pa in panel_turtle:
                pa.set_panel_text("Green_Power_Up", slot_id, scale_factor_X, scale_factor_Y)
        elif slot_id == 4:
            for pa in panel_turtle:
                pa.set_panel_text("Red_Power_Up", slot_id, scale_factor_X, scale_factor_Y)
    refresh_variables.refresh_panel = 1


"""
    The next functions are for changing the game settings.
"""


def toggle_button_sound(x, y):
    """
        Used to toggle the button sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 165 * scale_factor_Y) and (y < 226 * scale_factor_Y):
        execute_setting_function(1)


def toggle_player_shooting_sound(x, y):
    """
        Used to toggle the button sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 85 * scale_factor_Y) and (y < 146 * scale_factor_Y):
        execute_setting_function(2)


def toggle_enemy_shooting_sound(x, y):
    """
        Used to toggle the button sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 5 * scale_factor_Y) and (y < 66 * scale_factor_Y):
        execute_setting_function(3)


def toggle_player_death_sound(x, y):
    """
        Used to toggle the player death sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > -75 * scale_factor_Y) and (y < -14 * scale_factor_Y):
        execute_setting_function(4)


def toggle_enemy_death_sound(x, y):
    """
        Used to toggle the enemy death sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > -155 * scale_factor_Y) and (y < -94 * scale_factor_Y):
        execute_setting_function(5)


def toggle_player_hit_sound(x, y):
    """
        Used to toggle the player hit sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > -235 * scale_factor_Y) and (y < -174 * scale_factor_Y):
        execute_setting_function(6)


def toggle_enemy_hit_sound(x, y):
    """
        Used to toggle the enemy hit sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > -315 * scale_factor_Y) and (y < -254 * scale_factor_Y):
        execute_setting_function(7)


def toggle_power_up_pickup_sound(x, y):
    """
        Used to toggle the power up pickup sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > 165 * scale_factor_Y) and (y < 226 * scale_factor_Y):
        execute_setting_function(8)


def toggle_power_up_spawn_sound(x, y):
    """
        Used to toggle the power up spawn sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > 85 * scale_factor_Y) and (y < 146 * scale_factor_Y):
        execute_setting_function(9)


def toggle_coin_pick_up_sound(x, y):
    """
        Used to toggle the coin pick up sound on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > 5 * scale_factor_Y) and (y < 66 * scale_factor_Y):
        execute_setting_function(10)


def toggle_fullscreen(x, y):
    """
        Used to toggle fullscreen on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    global updated_controls
    global fullscreen_toggled
    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > -75 * scale_factor_Y) and (y < -14 * scale_factor_Y):
        # If fullscreen was originally off
        if fullscreen == 0 and fullscreen_toggled == 0:
            # Warn the player about the effects of performance
            message_output = ctypes.windll.user32.MessageBoxW(0,"Enabling fullscreen may cause a performance drop and expose your game to bugs. Are you sure you want to enable fullscreen?", "Warning!", 4 + 48)
            # If the player says yes
            if message_output != 7:
                # Toggle fullscreen
                execute_setting_function(11)
                # Alert the game of a needed restart
                if fullscreen_toggled == 0:
                    fullscreen_toggled = 1
                    updated_controls = 1
                else:
                    fullscreen_toggled = 0
                    updated_controls = 0
        # If fullscreen was originally on
        else:
            # Turn it off like normal, but a restart is still required
            execute_setting_function(11)
            if fullscreen_toggled == 0:
                fullscreen_toggled = 1
                updated_controls = 1
            else:
                fullscreen_toggled = 0
                updated_controls = 0


def toggle_vsync(x, y):
    """
        Used to toggle VSync on and off.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > 29 * scale_factor_X) and (x < 600 * scale_factor_X) and (y > -155 * scale_factor_Y) and (y < -94 * scale_factor_Y):
        # If VSync was originally off
        if vsync == 0:
            # Warn the user about effects on performance
            message_output = ctypes.windll.user32.MessageBoxW(0, "Turning on VSync may lower performance. Are you sure you want to enable VSync?", "Warning!", 4 + 48)
            # If the user selects yes
            if message_output != 7:
                # Toggle VSync
                execute_setting_function(12)
        # If VSync was originally on
        else:
            # Toggle like normal
            execute_setting_function(12)


def execute_setting_function(type):
    """
        Used to actually execute the toggle based on the parameter "type".

        :param type: The type of toggle to be executed based on the button clicked.
        :type type: int

        :return: None
    """
    global refresh_variables
    # Button sound is played
    if button_sound == 1:
        sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
        sound.play()
    # The configuration file is updated
    config = configparser.ConfigParser()
    config.read('Config/config.ini')
    setting = list(config['Settings'])[type]
    # The specific toggle is edited
    if config['Settings'].getint(setting) == 1:
        config['Settings'][setting] = '0'
    else:
        config['Settings'][setting] = '1'
    # Write back to file
    with open('Config/config.ini', 'w') as configfile:
        config.write(configfile)
    refresh_variables.refresh_indicator = 1


def change_go_right_key(x, y):
    """
        Used to change the keybind for going right.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 165 * scale_factor_Y) and (y < 226 * scale_factor_Y):
        execute_control_setting(0)


def change_go_left_key(x, y):
    """
        Used to change the keybind for going left.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 85 * scale_factor_Y) and (y < 146 * scale_factor_Y):
        execute_control_setting(1)


def change_shoot_key(x, y):
    """
        Used to change the keybind for shooting the player laser.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > 5 * scale_factor_Y) and (y < 66 * scale_factor_Y):
        execute_control_setting(2)


def change_jump_key(x, y):
    """
        Used to change the keybind for jumping.

        :param x: The current x-coordinate of the cursor
        :type x: float

        :param y: The current y-coordinate of the cursor
        :type y: float

        :return: None
    """

    wn.onscreenclick(None)
    # Check to see if the cursor is in the bound of the button to be clicked
    if (x > -612 * scale_factor_X) and (x < -40 * scale_factor_X) and (y > -75 * scale_factor_Y) and (y < -14 * scale_factor_Y):
        execute_control_setting(3)


def execute_control_setting(type):
    """
        Actaully executes the keybind change given by the "type" parameter.

        :param type: The type of keybind change to be executed.
        :type type: int

        :return: None
    """

    global message_output
    global updated_controls
    # Actual keybind
    key_1 = 0
    # String inputted into the textbox
    key_2 = 0
    # Keybind conflict
    key_alert = 0
    # Backup of actual keybind (In case something goes wrong)
    key_backup = 0
    # "type" parameter as a string
    type_string = ""
    # Go right key
    if type == 0:
        global go_right_key, go_right_key_alert
        key_1 = go_right_key
        key_alert = go_right_key_alert
        type_string = "Go Right"
    # Go left key
    elif type == 1:
        global go_left_key, go_left_key_alert
        key_1 = go_left_key
        key_alert = go_left_key_alert
        type_string = "Go Left"
    # Shoot key
    elif type == 2:
        global shoot_key, shoot_key_alert
        key_1 = shoot_key
        key_alert = shoot_key_alert
        type_string = "Shoot"
    # Jump key
    elif type == 3:
        global jump_key, jump_key_alert
        key_1 = jump_key
        key_alert = jump_key_alert
        type_string = "Jump"
    # Play the button click sound
    if button_sound == 1:
        sound = pygame.mixer.Sound("Sound/Button_Sound.wav")
        sound.play()
    # Backup the original keybind
    key_backup = key_1
    # Set "key_2" to whatever the user inputted into the textbox
    key_2 = wn.textinput("{}".format(type_string), "Insert new key here:")
    # If the user inputted a space, display "space"
    if key_2 == " ":
        key_2 = "space"
    # Listen for new keybinds
    wn.listen()
    # If the new keybind exists and is different from the one before, the keybind setting need to be updated
    if key_2 != None and key_2 != key_backup:
        # If the new keybind input is invalid (enter key or multiple charecters)
        if (len(key_2) > 1 and key_2 != "space") or key_2 == "":
            # Let the user know through an error
            ctypes.windll.user32.MessageBoxW(0, "That is an invalid input!", "Invalid Input!", 16)
            # Go back to the old keybind
            key_2 = key_backup
        # if it is valid
        else:
            # Update the keybind in the backup ini file.
            config = configparser.ConfigParser()
            config.read('Config/keyUpdate.ini')
            key_to_change = list(config['Key_Update'])[type]
            config['Key_Update'][key_to_change] = key_2
            with open('Config/keyUpdate.ini', 'w') as configfile:
                config.write(configfile)
            key_1 = key_2
            # Check for keybind conflicts for each keybind individually
            if type == 0:
                go_right_key = key_1
                if go_right_key != go_left_key and go_right_key != shoot_key and go_right_key != jump_key:
                    go_right_key_alert = 0
                else:
                    go_right_key_alert = 1
                key_alert = go_right_key_alert
            elif type == 1:
                go_left_key = key_1
                if go_left_key != go_right_key and go_left_key != shoot_key and go_left_key != jump_key:
                    go_left_key_alert = 0
                else:
                    go_left_key_alert = 1
                key_alert = go_left_key_alert
            elif type == 2:
                shoot_key = key_1
                if shoot_key != go_right_key and shoot_key != go_left_key and shoot_key != jump_key:
                    shoot_key_alert = 0
                else:
                    shoot_key_alert = 1
                key_alert = shoot_key_alert
            else:
                jump_key = key_1
                if jump_key != go_right_key and jump_key != go_left_key and jump_key != shoot_key:
                    jump_key_alert = 0
                else:
                    jump_key_alert = 1
                key_alert = jump_key_alert
            # If there is a conflict
            if key_alert == 1:
                # Alert the user about the conflict
                message_output = ctypes.windll.user32.MessageBoxW(0, "Your current configuration may cause conflicts with other controls!\nAre you sure you want to keep it?", "Conflict!", 4 + 48)
                # If the user wants to go back
                if message_output == 7:
                    # Reinstate the old keybinds and update the backup keybind file
                    key_1 = key_backup
                    key_2 = key_backup
                    config = configparser.ConfigParser()
                    config.read('Config/keyUpdate.ini')
                    key_to_change = list(config['Key_Update'])[type]
                    config['Key_Update'][key_to_change] = key_2
                    with open('Config/keyUpdate.ini', 'w') as configfile:
                        config.write(configfile)
                    if type == 0:
                        go_right_key = key_1
                    elif type == 1:
                        go_left_key = key_1
                    elif type == 2:
                        shoot_key = key_1
                    else:
                        jump_key = key_1
                # If the user wants to keep the controls
                else:
                    # Update the main config file to confirm the changes
                    config = configparser.ConfigParser()
                    config.read('Config/config.ini')
                    key_to_change = list(config['Controls'])[type]
                    if type == 0:
                        config['Controls'][key_to_change] = go_right_key
                    elif type == 1:
                        config['Controls'][key_to_change] = go_left_key
                    elif type == 2:
                        config['Controls'][key_to_change] = shoot_key
                    elif type == 3:
                        config['Controls'][key_to_change] = jump_key
                    with open('Config/config.ini', 'w') as configfile:
                        config.write(configfile)

                    key_backup = key_1
                    # Alert that a restart is needed for changes to take effect
                    updated_controls = 1
            else:
                # If there are no conflicts, update the main config file like normal.
                config = configparser.ConfigParser()
                config.read('Config/config.ini')
                key_to_change = list(config['Controls'])[type]
                if type == 0:
                    config['Controls'][key_to_change] = go_right_key
                elif type == 1:
                    config['Controls'][key_to_change] = go_left_key
                elif type == 2:
                    config['Controls'][key_to_change] = shoot_key
                elif type == 3:
                    config['Controls'][key_to_change] = jump_key
                with open('Config/config.ini', 'w') as configfile:
                    config.write(configfile)

                key_backup = key_1
                # Alert that a restart is needed for changes to take effect
                updated_controls = 1
    # If the keybind settings to do not need to updated
    else:
        key_2 = key_backup


"""
    The functions below are for updating the text on the screen.
"""


def position(event):
    """
        Change the color of the button text to yellow when the mouse is hovering over it.
        It also changes the colors to red/orange for the control buttons based on if there is a keybind conflict or not.

        :param event: Holds the current position of the cursor on the screen
        :type event: tkinter.Event()

        :return: None
    """

    global button_update
    # Extract x and y coordinate of the cursor
    a, b = event.x, event.y
    # Update button text as needed
    if mode == "Title_Mode":
        for bu in buttons_on_screen_list:
            bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
    if mode == "Machine_Mode" or mode == "Alien_Mode" or mode == "Stats" or mode == "Shop":
        for bu in buttons_on_screen_list:
            button_update = bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
    if mode == "Settings":
        for bu in buttons_on_screen_list:
            if bu.type == "Regular_Settings_And_Controls":
                if id == 1:
                    button_update = bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
                else:
                    bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
            else:
                bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
    if mode == "Controls":
        for bu in buttons_on_screen_list:
            if bu.type == "Regular_Settings_And_Controls":
                if id == 1:
                    button_update = bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
                else:
                    bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)
            elif bu.type == "Controls_Toggle":
                if bu.id == 1:
                    # If there is a keybind conflict
                    if go_right_key_alert == 1:
                        bu.update_controls_text_color(1, a, b, scale_factor_X, scale_factor_Y)
                    else:
                        bu.update_controls_text_color(0, a, b, scale_factor_X, scale_factor_Y)
                elif bu.id == 2:
                    # If there is a keybind conflict
                    if go_left_key_alert == 1:
                        bu.update_controls_text_color(2, a, b, scale_factor_X, scale_factor_Y)
                    else:
                        bu.update_controls_text_color(0, a, b, scale_factor_X, scale_factor_Y)
                elif bu.id == 3:
                    # If there is a keybind conflict
                    if shoot_key_alert == 1:
                        bu.update_controls_text_color(3, a, b, scale_factor_X, scale_factor_Y)
                    else:
                        bu.update_controls_text_color(0, a, b, scale_factor_X, scale_factor_Y)
                elif bu.id == 4:
                    # If there is a keybind conflict
                    if jump_key_alert == 1:
                        bu.update_controls_text_color(4, a, b, scale_factor_X, scale_factor_Y)
                    else:
                        bu.update_controls_text_color(0, a, b, scale_factor_X, scale_factor_Y)
            else:
                bu.update_text_color(a, b, scale_factor_X, scale_factor_Y, fullscreen)


def update_text():
    """
        Refreshes and updates the text on the screen.
        When VSync is on, this function is only run at the refresh rate times a second.
        Part of the "screen refresher" section in the main game loop.
        This function includes both the button text and the text boxes on the screen.

        :return: None
    """

    global mode
    global refresh_variables
    # Update based on the current mode
    if mode == "Title_Mode":
        for bu in buttons_on_screen_list:
            bu.write_lines(scale_factor)
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Laser Fighter", 72, "bold", scale_factor)
            elif t.id == 2:
                t.write("Beta 1.1.0b", 24, "normal", scale_factor)
            elif t.id == 3:
                t.write("God Mode Is On!", 24, "normal", scale_factor)
    elif mode == "Machine_Mode":
        for bu in buttons_on_screen_list:
            bu.write_lines(scale_factor)
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Score: {}  High Score: {}".format(score, high_score_machine_war), 24, "normal", scale_factor)
            elif t.id == 2:
                for yi in yellow_power_up_indicator_turtle:
                    if yi.get_power_up_active() == 1:
                        t.write("{}".format(yi.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 3:
                for bi in blue_power_up_indicator_turtle:
                    if bi.get_power_up_active() == 1:
                        t.write("{}".format(bi.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 4:
                for ei in extra_power_up_indicator_turtle:
                    if ei.get_power_up_active() == 1:
                        t.write("{}".format(ei.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 5:
                t.write_left("{}".format(total_coins), 24, "normal", scale_factor)
            elif t.id == 6:
                t.write("God Mode Is On!", 24, "normal", scale_factor)
    elif mode == "Alien_Mode":
        for bu in buttons_on_screen_list:
            bu.write_lines(scale_factor)
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Score: {}  High Score: {}".format(score, high_score_alien_mode), 24, "normal",
                        scale_factor)
            elif t.id == 2:
                for yi in yellow_power_up_indicator_turtle:
                    if yi.get_power_up_active() == 1:
                        t.write("{}".format(yi.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 3:
                for bi in blue_power_up_indicator_turtle:
                    if bi.get_power_up_active() == 1:
                        t.write("{}".format(bi.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 4:
                for ei in extra_power_up_indicator_turtle:
                    if ei.get_power_up_active() == 1:
                        t.write("{}".format(ei.get_power_up_timer()), 24, "normal", scale_factor)
                    else:
                        t.write("0", 24, "normal", scale_factor)
            elif t.id == 5:
                t.write_left("{}".format(total_coins), 24, "normal", scale_factor)
            elif t.id == 6:
                t.write("God Mode Is On!", 24, "normal", scale_factor)
    elif mode == "Shop":
        for bu in buttons_on_screen_list:
            if bu.get_type() != "Shop_Slot":
                bu.write_lines(scale_factor)
            if bu.get_type() == "Power_Up_Slot":
                if bu.get_id() == 1:
                    bu.write_indicator(shop_config.yellow_power_up_level, scale_factor)
                elif bu.get_id() == 2:
                    bu.write_indicator(shop_config.blue_power_up_level, scale_factor)
                elif bu.get_id() == 3:
                    bu.write_indicator(shop_config.green_power_up_level, scale_factor)
                elif bu.get_id() == 4:
                    bu.write_indicator(shop_config.red_power_up_level, scale_factor)
        if refresh_variables.refresh_panel == 1:
            for pa in panel_turtle:
                pa.write_text(scale_factor, scale_factor_Y, fullscreen)
            refresh_variables.refresh_panel = 0
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Shop", 72, "bold", scale_factor)
            elif t.id == 2:
                t.write_left("{}".format(total_coins), 24, "normal", scale_factor)
            if refresh_variables.refresh_text == 1:
                if page == "Machine_Mode":
                    if t.id == 3:
                        t.write_left("Machine Mode", 36, "bold", scale_factor)
                    elif t.id == 5:
                        t.write_left(" 5000", 22, "normal", scale_factor)
                    elif t.id == 6:
                        t.write_left(" 15000", 22, "normal", scale_factor)
                    elif t.id == 7:
                        t.write_left(" 40000", 22, "normal", scale_factor)
                    elif t.id == 8:
                        t.write_left(" 100000", 22, "normal", scale_factor)
                elif page == "Alien_Mode":
                    if t.id == 3:
                        t.write_left("Alien Mode", 36, "bold", scale_factor)
                    elif t.id == 5:
                        t.write_left(" 5000", 22, "normal", scale_factor)
                    elif t.id == 6:
                        t.write_left(" 15000", 22, "normal", scale_factor)
                    elif t.id == 7:
                        t.write_left(" 40000", 22, "normal", scale_factor)
                    elif t.id == 8:
                        t.write_left(" 100000", 22, "normal", scale_factor)
                elif page == "Power_Ups":
                    if t.id == 3:
                        t.write_left("Power Ups", 36, "bold", scale_factor)
                    elif t.id == 4:
                        if shop_config.yellow_power_up_level == 1:
                            t.write_left(" 1000", 22, "normal", scale_factor)
                        elif shop_config.yellow_power_up_level == 2:
                            t.write_left(" 5000", 22, "normal", scale_factor)
                        elif shop_config.yellow_power_up_level == 3:
                            t.write_left(" 15000", 22, "normal", scale_factor)
                        elif shop_config.yellow_power_up_level == 4:
                            t.write_left(" 30000", 22, "normal", scale_factor)
                    elif t.id == 5:
                        if shop_config.blue_power_up_level == 1:
                            t.write_left(" 1000", 22, "normal", scale_factor)
                        elif shop_config.blue_power_up_level == 2:
                            t.write_left(" 5000", 22, "normal", scale_factor)
                        elif shop_config.blue_power_up_level == 3:
                            t.write_left(" 15000", 22, "normal", scale_factor)
                        elif shop_config.blue_power_up_level == 4:
                            t.write_left(" 30000", 22, "normal", scale_factor)
                    elif t.id == 6:
                        if shop_config.green_power_up_level == 1:
                            t.write_left(" 1000", 22, "normal", scale_factor)
                        elif shop_config.green_power_up_level == 2:
                            t.write_left(" 5000", 22, "normal", scale_factor)
                        elif shop_config.green_power_up_level == 3:
                            t.write_left(" 15000", 22, "normal", scale_factor)
                        elif shop_config.green_power_up_level == 4:
                            t.write_left(" 30000", 22, "normal", scale_factor)
                    elif t.id == 7:
                        if shop_config.red_power_up_level == 1:
                            t.write_left(" 1000", 22, "normal", scale_factor)
                        elif shop_config.red_power_up_level == 2:
                            t.write_left(" 5000", 22, "normal", scale_factor)
                        elif shop_config.red_power_up_level == 3:
                            t.write_left(" 15000", 22, "normal", scale_factor)
                        elif shop_config.red_power_up_level == 4:
                            t.write_left(" 30000", 22, "normal", scale_factor)
        if refresh_variables.refresh_text == 1:
            refresh_variables.refresh_text = 0
    elif mode == "Stats":
        for bu in buttons_on_screen_list:
            bu.write_lines(scale_factor)
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Statistics", 72, "bold", scale_factor)
            if refresh_variables.refresh_text == 1:
                if t.id == 2:
                    t.write("Machine Mode", 48, "bold", scale_factor)
                elif t.id == 3:
                    t.write("Alien Mode", 48, "bold", scale_factor)
                elif t.id == 4:
                    t.write("High Score: {}".format(high_score_machine_war), 24, "normal", scale_factor)
                elif t.id == 5:
                    t.write("Bosses Killed: {}".format(bosses_killed), 24, "normal", scale_factor)
                elif t.id == 6:
                    t.write("Red Bots Killed: {}".format(red_bots_killed), 24, "normal", scale_factor)
                elif t.id == 7:
                    t.write("Yellow Bots Killed: {}".format(yellow_bots_killed), 24, "normal", scale_factor)
                elif t.id == 8:
                    t.write("Blue Bots Killed: {}".format(blue_bots_killed), 24, "normal", scale_factor)
                elif t.id == 9:
                    t.write("Deaths: {}".format(classic_deaths), 24, "normal", scale_factor)
                elif t.id == 10:
                    t.write("Damage Taken: {}".format(machine_damage_taken), 24, "normal", scale_factor)
                elif t.id == 11:
                    t.write("Lasers Fired: {}".format(classic_lasers_fired), 24, "normal", scale_factor)
                elif t.id == 12:
                    t.write("Power Ups Picked Up: {}".format(classic_power_ups_picked_up), 24, "normal", scale_factor)
                elif t.id == 13:
                    t.write("Coins Collected: {}".format(machine_coins_collected), 24, "normal", scale_factor)
                elif t.id == 14:
                    t.write("High Score: {}".format(high_score_alien_mode), 24, "normal", scale_factor)
                elif t.id == 15:
                    t.write("UFOs Killed: {}".format(ufos_killed), 24, "normal", scale_factor)
                elif t.id == 16:
                    t.write("Big Aliens Killed: {}".format(big_aliens_killed), 24, "normal", scale_factor)
                elif t.id == 17:
                    t.write("Medium Aliens Killed: {}".format(medium_aliens_killed), 24, "normal", scale_factor)
                elif t.id == 18:
                    t.write("Small Aliens Killed: {}".format(small_aliens_killed), 24, "normal", scale_factor)
                elif t.id == 19:
                    t.write("Deaths: {}".format(alien_deaths), 24, "normal", scale_factor)
                elif t.id == 20:
                    t.write("Damage Taken: {}".format(damage_taken), 24, "normal", scale_factor)
                elif t.id == 21:
                    t.write("Lasers Fired: {}".format(alien_lasers_fired), 24, "normal", scale_factor)
                elif t.id == 22:
                    t.write("Jumps: {}".format(jumps), 24, "normal", scale_factor)
                elif t.id == 23:
                    t.write("Power Ups Picked Up: {}".format(alien_power_ups_picked_up), 24, "normal", scale_factor)
                elif t.id == 24:
                    t.write("Coins Collected: {}".format(alien_coins_collected), 24, "normal", scale_factor)
                    refresh_variables.refresh_text = 0
            if t.id == 25:
                t.write("God Mode Is On!", 24, "normal", scale_factor)
    elif mode == "Settings":
        for bu in buttons_on_screen_list:
            bu.write_lines(scale_factor)
            if refresh_variables.refresh_indicator == 1 or refresh_variables.refresh_indicator == 2:
                if bu.type == "Settings_Toggle":
                    if bu.id == 1:
                        bu.write_indicator(button_sound, scale_factor)
                    elif bu.id == 2:
                        bu.write_indicator(player_shooting_sound, scale_factor)
                    elif bu.id == 3:
                        bu.write_indicator(enemy_shooting_sound, scale_factor)
                    elif bu.id == 4:
                        bu.write_indicator(player_death_sound, scale_factor)
                    elif bu.id == 5:
                        bu.write_indicator(enemy_death_sound, scale_factor)
                    elif bu.id == 6:
                        bu.write_indicator(player_hit_sound, scale_factor)
                    elif bu.id == 7:
                        bu.write_indicator(enemy_hit_sound, scale_factor)
                    elif bu.id == 8:
                        bu.write_indicator(power_up_pickup_sound, scale_factor)
                    elif bu.id == 9:
                        bu.write_indicator(power_up_spawn_sound, scale_factor)
                    elif bu.id == 10:
                        bu.write_indicator(coin_pickup_sound, scale_factor)
                    elif bu.id == 11:
                        bu.write_fullscreen_indicator(fullscreen, fullscreen_toggled, scale_factor)
                    elif bu.id == 12:
                        bu.write_indicator(vsync, scale_factor)
        if refresh_variables.refresh_indicator == 2:
            refresh_variables.refresh_indicator = 0
        elif refresh_variables.refresh_indicator == 1:
            refresh_variables.refresh_indicator = 2
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Settings", 72, "bold", scale_factor)
            elif t.id == 2:
                t.write("God Mode Is On!", 24, "normal", scale_factor)
    elif mode == "Controls":
        for bu in buttons_on_screen_list:
            if bu.type != "Controls_Toggle":
                bu.write_lines(scale_factor)
            else:
                bu.write_control(go_right_key, go_left_key, shoot_key, jump_key, scale_factor)
        for t in text_on_screen_list:
            if t.id == 1:
                t.write("Controls", 72, "bold", scale_factor)
            elif t.id == 2:
                t.write("God Mode Is On!", 24, "normal", scale_factor)


"""
    The next functions are for spawning sprites on the screen
"""


def spawn_buttons(type, id):
    """
        Spawns a button on the screen using the button class.

        :param type: The type of button to create
        :type type: string

        :param id: The id of the button to create
        :type id: int

        :return: None
    """

    global current_button_index
    # If a usable button sprite does not exist
    if len(all_button_list) <= len(buttons_on_screen_list):
        # Create a new button object
        button = Button(type, id, scale_factor_X, scale_factor_Y, fullscreen)
        buttons_on_screen_list.append(button)
        current_button_index = current_button_index + 1
        all_button_list.append(button)
    # If a usable button sprite does exist
    else:
        # If the button to create does not need a button indicator
        if type != "Settings_Toggle" and type != "Shop_Slot" and type != "Power_Up_Slot":
            # Reinstate the button like normal
            # Go throguh all the button sprites
            for bu in all_button_list:
                # If the current sprite is already in use
                if bu.get_button_frame().isvisible():
                    continue
                # If the current sprite is free and ready to be used
                else:
                    # Reinstate the button to the correct type and id
                    if type == "Title":
                        bu.reinstate_to_title(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Title_Small":
                        bu.reinstate_to_title_small(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Game":
                        bu.reinstate_to_game(scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Tab":
                        bu.reinstate_to_tab(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Regular_Settings_And_Controls":
                        bu.reinstate_to_regular_settings_and_controls(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Controls_Toggle":
                        bu.reinstate_to_controls_toggle(id, scale_factor_X, scale_factor_Y, fullscreen)
                    # Add it to the screen
                    buttons_on_screen_list.append(bu)
                    current_button_index = current_button_index + 1
                    break
        # If the button to create does need a button indicator
        else:
            found = 0
            # Go through all the button sprites
            for bu in all_button_list:
                # First check if one can be found with a button indicator
                if bu.get_button_frame().isvisible() or bu.indicator == 0:
                    continue
                # If found, reinstate that one
                else:
                    if type == "Settings_Toggle":
                        bu.reinstate_to_settings_toggle(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Shop_Slot":
                        bu.reinstate_to_shop_slot(id, scale_factor_X, scale_factor_Y, fullscreen)
                    elif type == "Power_Up_Slot":
                        bu.reinstate_to_power_up_slot(id, scale_factor_X, scale_factor_Y, fullscreen)
                    buttons_on_screen_list.append(bu)
                    current_button_index = current_button_index + 1
                    found = 1
                    break
            # If not found
            if found == 0:
                # Find any available button sprite
                for bu in all_button_list:
                    if bu.get_button_frame().isvisible():
                        continue
                    else:
                        # Reinstate it and add the button indicator
                        if type == "Settings_Toggle":
                            bu.reinstate_to_settings_toggle(id, scale_factor_X, scale_factor_Y, fullscreen)
                        elif type == "Shop_Slot":
                            bu.reinstate_to_shop_slot(id, scale_factor_X, scale_factor_Y, fullscreen)
                        elif type == "Power_Up_Slot":
                            bu.reinstate_to_power_up_slot(id, scale_factor_X, scale_factor_Y, fullscreen)
                        buttons_on_screen_list.append(bu)
                        current_button_index = current_button_index + 1
                        break


def spawn_panel():
    """
        Spawn a panel on the screen with the correct type based on what screen the player is on.

        :return: None
    """

    global mode
    global panel_index
    # If the panel sprite does not exist
    if len(panel_turtle) == 0:
        panel = Panel(mode, scale_factor_X, scale_factor_Y, fullscreen)
        panel_turtle.append(panel)
        panel_index = panel_index + 1
    # If it does exist, just reinstate the existing one
    else:
        for pa in panel_turtle:
            if pa.get_panel_frame().isvisible():
                continue
            else:
                if mode == "Shop":
                    pa.reinstate_to_shop(scale_factor_X, scale_factor_Y, fullscreen)
                panel_index = panel_index + 1


def spawn_text_box(id, x, y, color):
    """
        Spawn a textbox on the screen with the given coordinates.

        :param id: The unique identifier for the textbox
        :type id: int

        :param x: The x-coordinate of the text box
        :type x: float

        :param y: The y-coordinate of the text box
        :type y: float

        :param color: The color of the text in the text box.
        :type color: string

        :return: None
    """

    # All spawn functions have this same procedure to check for existing sprites to use
    # This is done because the turtle module makes it impossible to actually fully get rid of a turtle while the
    #   program is running.
    # In order to maintain performance, all turtle sprites are reused as often as possible.
    # This is why a global list exists for every type of sprite in the game.
    global current_text_index
    if len(all_text_list) <= len(text_on_screen_list):
        text_box = Text(id, x, y, color)
        text_on_screen_list.append(text_box)
        current_text_index = current_text_index + 1
        all_text_list.append(text_box)
    else:
        for t in all_text_list:
            if t.in_use == 1:
                continue
            else:
                t.reinstate(id, x, y, color)
                text_on_screen_list.append(t)
                current_text_index = current_text_index + 1
                break


def spawn_price_label(x, y):
    global current_price_index
    if len(all_price_label) <= len(price_label_on_screen_list):
        price_label = PriceLabel(x, y, fullscreen)
        price_label_on_screen_list.append(price_label)
        current_price_index = current_price_index + 1
        all_price_label.append(price_label)
    else:
        for pl in all_price_label:
            if pl.get_price_label().isvisible():
                continue
            else:
                pl.reinstate(x, y)
                price_label_on_screen_list.append(pl)
                current_price_index = current_price_index + 1
                break


def spawn_selector(type):
    global current_selector_index
    if len(all_selector) <= len(selectors_on_screen_list):
        selector = Selector(type, scale_factor_X, scale_factor_Y, fullscreen)
        selectors_on_screen_list.append(selector)
        current_selector_index = current_selector_index + 1
        all_selector.append(selector)
    else:
        for s in all_selector:
            if s.get_selector().isvisible():
                continue
            else:
                if type == "Tab":
                    s.reinstate_to_tab(scale_factor_X, scale_factor_Y, fullscreen)
                elif type == "Slot":
                    s.reinstate_to_slot(scale_factor_X, scale_factor_Y, fullscreen)
                selectors_on_screen_list.append(s)
                current_selector_index = current_selector_index + 1
                break


def spawn_coin_indicator():
    """
        Spawn a coin indicator at the top of the screen.

        :return: None
    """

    global coin_indicator_index
    if len(coin_indicator_turtle) == 0:
        coin_ind = CoinIndicator(scale_factor_X, scale_factor_Y, fullscreen)
        coin_indicator_turtle.append(coin_ind)
        coin_indicator_index = coin_indicator_index + 1
    else:
        for ci in coin_indicator_turtle:
            if ci.get_coin_indicator().isvisible():
                continue
            else:
                ci.reinstate()
                coin_indicator_index = coin_indicator_index + 1


def spawn_yellow_power_up_indicator():
    """
        Spawn a yellow power up indicator at the top of the screen.

        :return: None
    """

    global yellow_power_up_indicator_index
    if len(yellow_power_up_indicator_turtle) == 0:
        yellow_power_up_indicator = YellowIndicator(scale_factor_X, scale_factor_Y, fullscreen)
        yellow_power_up_indicator_turtle.append(yellow_power_up_indicator)
        yellow_power_up_indicator_index = yellow_power_up_indicator_index + 1
    else:
        for yi in yellow_power_up_indicator_turtle:
            if yi.get_yellow_power_up_indicator().isvisible():
                continue
            else:
                yi.reinstate(fullscreen)
                yellow_power_up_indicator_index = yellow_power_up_indicator_index + 1
                break


def spawn_blue_power_up_indicator():
    """
        Spawn a blue power up indicator at the top of the screen.

        :return: None
    """

    global blue_power_up_indicator_index
    if len(blue_power_up_indicator_turtle) == 0:
        blue_power_up_indicator = BlueIndicator(scale_factor_X, scale_factor_Y, fullscreen)
        blue_power_up_indicator_turtle.append(blue_power_up_indicator)
        blue_power_up_indicator_index = blue_power_up_indicator_index + 1
    else:
        for bi in blue_power_up_indicator_turtle:
            if bi.get_blue_power_up_indicator().isvisible():
                continue
            else:
                bi.reinstate(fullscreen)
                blue_power_up_indicator_index = blue_power_up_indicator_index + 1
                break


def spawn_extra_power_up_indiciator():
    """
        Spawn an extra power up indicator at the top of the screen.

        :return: None
    """

    global mode
    global extra_power_up_indicator_index
    if len(extra_power_up_indicator_turtle) == 0:
        # The id depends on the current mode the user is in (Whether it will be green or blue)
        if mode == "Machine_Mode":
            extra_power_up_indicator = ExtraIndicator(1, scale_factor_X, scale_factor_Y, fullscreen)
        elif mode == "Alien_Mode":
            extra_power_up_indicator = ExtraIndicator(2, scale_factor_X, scale_factor_Y, fullscreen)
        extra_power_up_indicator_turtle.append(extra_power_up_indicator)
        extra_power_up_indicator_index = extra_power_up_indicator_index + 1
    else:
        for ei in extra_power_up_indicator_turtle:
            if ei.get_extra_power_up_indicator().isvisible():
                continue
            else:
                if mode == "Machine_Mode":
                    ei.reinstate(1, fullscreen)
                elif mode == "Alien_Mode":
                    ei.reinstate(2, fullscreen)
                extra_power_up_indicator_index = extra_power_up_indicator_index + 1
                break


def spawn_power_up(type):
    """
        Spawn a power up on the screen.
        The type of power up depends on the parameter "type".
        What height it spawns at depends on the current mode the user is in.

        :param type: Determines which type of power up spawns
        :type type: int

        :return: None
    """

    global mode
    global power_up_index
    if len(all_power_ups) <= len(current_power_ups):
        if type == 1:
            if mode == "Machine_Mode":
                power_up = PowerUp(1, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            elif mode == "Alien_Mode":
                power_up = PowerUp(1, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            power_up_index[0] = 1
            current_power_ups.append(power_up)
            all_power_ups.append(power_up)
        elif type == 2:
            if mode == "Machine_Mode":
                power_up = PowerUp(2, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            elif mode == "Alien_Mode":
                power_up = PowerUp(2, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            power_up_index[1] = 1
            current_power_ups.append(power_up)
            all_power_ups.append(power_up)
        elif type == 3:
            if mode == "Machine_Mode":
                power_up = PowerUp(3, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            elif mode == "Alien_Mode":
                power_up = PowerUp(3, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            power_up_index[2] = 1
            current_power_ups.append(power_up)
            all_power_ups.append(power_up)
        else:
            if mode == "Machine_Mode":
                power_up = PowerUp(4, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            elif mode == "Alien_Mode":
                power_up = PowerUp(4, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
            power_up_index[3] = 1
            current_power_ups.append(power_up)
            all_power_ups.append(power_up)
    else:
        for pu in all_power_ups:
            if pu.get_power_up().isvisible():
                continue
            else:
                if type == 1:
                    if mode == "Machine_Mode":
                        pu.reinstate(1, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    elif mode == "Alien_Mode":
                        pu.reinstate(1, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    power_up_index[0] = 1
                    current_power_ups.append(pu)
                elif type == 2:
                    if mode == "Machine_Mode":
                        pu.reinstate(2, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    elif mode == "Alien_Mode":
                        pu.reinstate(2, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    power_up_index[1] = 1
                    current_power_ups.append(pu)
                elif type == 3:
                    if mode == "Machine_Mode":
                        pu.reinstate(3, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    elif mode == "Alien_Mode":
                        pu.reinstate(3, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    power_up_index[2] = 1
                    current_power_ups.append(pu)
                else:
                    if mode == "Machine_Mode":
                        pu.reinstate(4, 1, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    elif mode == "Alien_Mode":
                        pu.reinstate(4, 2, power_up_spawn_sound, scale_factor_X, scale_factor_Y, fullscreen)
                    power_up_index[3] = 1
                    current_power_ups.append(pu)
                break


def spawn_machine_player():
    """
        Spawn the Machine Mode player on the screen.

        :return: None
    """

    global current_player_index
    if len(all_player) <= len(current_player):
        player = Player(god_mode, scale_factor_X, scale_factor_Y, fullscreen)
        current_player.append(player)
        current_player_index = current_player_index + 1
        all_player.append(player)
    else:
        for p in all_player:
            if p.get_player().isvisible():
                continue
            else:
                p.reinstate(god_mode, scale_factor_Y, fullscreen)
                current_player.append(p)
                current_player_index = current_player_index + 1
                break


def spawn_blue_machine(id):
    """
        Spawn a blue machine with the given id on the screen.

        :param id: The id that the enemy should have (Determines initial location of the enemy)
        :type id: int

        :return: None
    """

    global blue_machine_index
    if len(all_blue_machines) <= len(blue_machines):
        blue_machine = BlueMachine(id, scale_factor_X, scale_factor_Y, fullscreen)
        blue_machines.append(blue_machine)
        blue_machine_index = blue_machine_index + 1
        all_blue_machines.append(blue_machine)
        blue_machines_update_values.append(0)
    else:
        for bm in all_blue_machines:
            if bm.get_blue_machine().isvisible():
                continue
            else:
                bm.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                blue_machines.append(bm)
                blue_machine_index = blue_machine_index + 1
                blue_machines_update_values.append(0)
                break


def spawn_yellow_machine(id):
    """
        Spawn a yellow machine with the given id on the screen.

        :param id: The id that the enemy should have (Determines initial location of the enemy)
        :type id: int

        :return: None
    """

    global yellow_machine_index
    if len(all_yellow_machines) <= len(yellow_machines):
        yellow_machine = YellowMachine(id, scale_factor_X, scale_factor_Y, fullscreen)
        yellow_machines.append(yellow_machine)
        yellow_machine_index = yellow_machine_index + 1
        all_yellow_machines.append(yellow_machine)
        yellow_machines_update_values.append(0)
    else:
        for ym in all_yellow_machines:
            if ym.get_yellow_machine().isvisible():
                continue
            else:
                ym.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                yellow_machines.append(ym)
                yellow_machine_index = yellow_machine_index + 1
                yellow_machines_update_values.append(0)
                break


def spawn_red_machine(id):
    """
        Spawn a red machine with the given id on the screen.

        :param id: The id that the enemy should have (Determines initial location of the enemy)
        :type id: int

        :return: None
    """

    global red_machine_index
    if len(all_red_machines) <= len(red_machines):
        red_machine = RedMachine(id, scale_factor_X, scale_factor_Y, fullscreen)
        red_machines.append(red_machine)
        red_machine_index = red_machine_index + 1
        all_red_machines.append(red_machine)
        red_machines_update_values.append(0)
        red_machines_hit_values.append(0)
    else:
        for rm in all_red_machines:
            if rm.get_red_machine().isvisible():
                continue
            else:
                rm.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                red_machines.append(rm)
                red_machine_index = red_machine_index + 1
                red_machines_update_values.append(0)
                red_machines_hit_values.append(0)
                break


def spawn_boss():
    """
        Spawn a Machine Mode boss on the screen.

        :return: None
    """

    global boss_index
    if len(all_boss) <= len(boss):
        spawn_boss = Boss(scale_factor_X, scale_factor_Y, fullscreen)
        boss.append(spawn_boss)
        boss_index = boss_index + 1
        all_boss.append(spawn_boss)
    else:
        for b in all_boss:
            if b.get_boss().isvisible():
                continue
            else:
                b.reinstate(scale_factor_X, scale_factor_Y, fullscreen)
                boss.append(b)
                boss_index = boss_index + 1
                break


def spawn_sun():
    """
        Spawn the sun in the background.

        :return: None
    """

    global sun_index
    if len(sun_turtle) == 0:
        sun = Sun(scale_factor_X, scale_factor_Y, fullscreen)
        sun_turtle.append(sun)
        sun_index = sun_index + 1
    else:
        for s in sun_turtle:
            if s.get_sun().isvisible():
                continue
            else:
                s.reinstate()
                sun_index = sun_index + 1


def spawn_earth():
    """
        Spawn the Earth in the background.

        :return: None
    """

    global earth_index
    if len(earth_turtle) == 0:
        earth = Earth(scale_factor_X, scale_factor_Y, fullscreen)
        earth_turtle.append(earth)
        earth_index = earth_index + 1
    else:
        for e in earth_turtle:
            if e.get_earth().isvisible():
                continue
            else:
                e.reinstate()
                earth_turtle.append(e)
                earth_index = earth_index + 1


def spawn_background_objects():
    """
        Spawn the Alien Mode background objects.

        :return: None
    """

    global background_objects_index
    if len(background_objects) == 0:
        background_object = BackgroundObjects(scale_factor_X, scale_factor_Y, fullscreen)
        background_objects.append(background_object)
        background_objects_index = background_objects_index + 1
    else:
        for bo in background_objects:
            if bo.get_ground().isvisible():
                continue
            else:
                bo.reinstate()
                background_objects.append(bo)
                background_objects_index = background_objects_index + 1


def spawn_human_player():
    """
        Spawn the human player on the screen.

        :return: None
    """

    global current_human_index
    if len(all_human) <= len(current_human):
        human = Human(god_mode, scale_factor_X, scale_factor_Y, fullscreen)
        current_human.append(human)
        current_human_index = current_human_index + 1
        all_human.append(human)
    else:
        for h in all_human:
            if h.get_player().isvisible():
                continue
            else:
                h.reinstate(god_mode, scale_factor_X, scale_factor_Y, fullscreen)
                current_human.append(h)
                current_human_index = current_human_index + 1
                break


def spawn_small_alien(id):
    """
        Spawn a small alien with the given id on the screen.

        :param id: The id that the alien should have (Determines initial location of the alien)
        :type id: int

        :return: None
    """

    global small_alien_index
    if len(all_small_aliens) <= len(small_aliens):
        small_alien = SmallAlien(id, scale_factor_X, scale_factor_Y, fullscreen)
        small_aliens.append(small_alien)
        small_alien_index = small_alien_index + 1
        all_small_aliens.append(small_alien)
        small_aliens_kill_values.append(0)
    else:
        for sa in all_small_aliens:
            if sa.get_small_alien().isvisible():
                continue
            else:
                sa.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                small_aliens.append(sa)
                small_alien_index = small_alien_index + 1
                small_aliens_kill_values.append(0)
                break


def spawn_medium_alien(id):
    """
        Spawn a medium alien with the given id on the screen.

        :param id: The id that the alien should have (Determines initial location of the alien)
        :type id: int

        :return: None
    """

    global medium_alien_index
    if len(all_medium_aliens) <= len(medium_aliens):
        medium_alien = MediumAlien(id, scale_factor_X, scale_factor_Y, fullscreen)
        medium_aliens.append(medium_alien)
        medium_alien_index = medium_alien_index + 1
        all_medium_aliens.append(medium_alien)
        medium_aliens_kill_values.append(0)
        medium_aliens_hit_values.append(0)
    else:
        for ma in all_medium_aliens:
            if ma.get_medium_alien().isvisible():
                continue
            else:
                ma.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                medium_aliens.append(ma)
                medium_alien_index = medium_alien_index + 1
                medium_aliens_kill_values.append(0)
                medium_aliens_hit_values.append(0)
                break


def spawn_large_alien(id):
    """
        Spawn a large alien with the given id on the screen.

        :param id: The id that the alien should have (Determines initial location of the alien)
        :type id: int

        :return: None
    """

    global large_alien_index
    if len(all_large_aliens) <= len(large_aliens):
        large_alien = LargeAlien(id, scale_factor_X, scale_factor_Y, fullscreen)
        large_aliens.append(large_alien)
        large_alien_index = large_alien_index + 1
        all_large_aliens.append(large_alien)
        large_aliens_kill_values.append(0)
        large_aliens_hit_values.append(0)
    else:
        for la in all_large_aliens:
            if la.get_large_alien().isvisible():
                continue
            else:
                la.reinstate(id, scale_factor_X, scale_factor_Y, fullscreen)
                large_aliens.append(la)
                large_alien_index = large_alien_index + 1
                large_aliens_kill_values.append(0)
                large_aliens_hit_values.append(0)
                break


def spawn_alien_boss():
    """
        Spawn an alien UFO on the screen.

        :return: None
    """

    global ufo_index
    if len(all_ufos) <= len(ufos):
        spawn_ufo = UFO(scale_factor_X, scale_factor_Y, fullscreen)
        ufos.append(spawn_ufo)
        ufo_index = ufo_index + 1
        all_ufos.append(spawn_ufo)
    else:
        for u in all_ufos:
            if u.get_ufo().isvisible():
                continue
            else:
                u.reinstate(scale_factor_X, scale_factor_Y, fullscreen)
                ufos.append(u)
                ufo_index = ufo_index + 1
                break


def on_quit():
    """
        Closes the game and terminates the turtle graphics window properly

        :return: None
    """

    global quit_loop
    # Quit loop means the game loop must be closed
    quit_loop = 1
    # After 300 milliseconds, destroy the window and terminate the program
    wn._root.after(300, wn._root.destroy)

# Set the keybinds for the turtle graphics window:
# Bind the current keybinds to their appropriate functions
wn.listen()
wn.onkeypress(go_left, go_left_key)
wn.onkeypress(go_right, go_right_key)
wn.onkeypress(shoot, shoot_key)
wn.onkeypress(jump, jump_key)

# Detect when the user wants to close the window and terminate the game loop.
# "WM_DELETE_WINDOW" is the parameter used to determine if the user has clicked the red x in the corner of the window
# If so, run the "on_quit" function which terminates the window
wn._root.protocol("WM_DELETE_WINDOW", on_quit)

# The two lines of code below are used to collect the position of the users mouse on the canvas
mouse_position = wn.getcanvas()
mouse_position.bind('<Motion>', position)

# The main game loop:
while True:
    """
        Screen Updater - Updates the screen with the events that occurred in the event handler
    """

    # If VSync is on
    if vsync == 1:
        # Update the screen based on the refresh rate
        # For example, if the refresh rate is 60, update the screen 60 times a second
        current_ticks = pygame.time.get_ticks()
        elapsed_time = (current_ticks - start_ticks) / 1000.0

        if elapsed_time >= MONITOR_DELAY:
            update_text()
            wn.update()
            start_ticks = pygame.time.get_ticks()
    # If VSync is off
    else:
        # Get the elapsed time
        current_ticks = pygame.time.get_ticks()
        elapsed_time = (current_ticks - start_ticks) / 1000.0

        # Update the screen as many times as the hardware allows (Not ideal)
        # "tick_update" is used for updating text because the game lags when the text is updated too often
        # The frequency of updating depends on the screen
        if mode == "Title_Mode":
            update_text()
        elif mode == "Machine_Mode" or mode == "Alien_Mode":
            if tick_update % 15 == 0:
                update_text()
        elif mode == "Stats":
            if tick_update % 4 == 0:
                update_text()
        elif mode == "Settings" or mode == "Shop":
            if tick_update % 3 == 0:
                update_text()
        elif mode == "Controls":
            if tick_update % 5 == 0:
                update_text()
        wn.update()

    """
        Loop Terminator - Terminates the game loop
    """

    # If requested, terminates the game loop
    if quit_loop == 1:
        break

    """
        Event Handler - Updates all the game parameters and variables as needed
    """

    # Every 0.4 seconds, there is a 1/67 chance of a power up spawning (1/200 per a power up type)
    current_power_up_time = time.time()
    elapsed_power_up_time = current_power_up_time - power_up_time
    if elapsed_power_up_time >= 0.4:
        # See if more than 1 whole 0.4 seconds has passed (Just in case there is EXTREME lag)
        # If it has, run the random chance the number of 0.4 that have passed
        delta_movement = (elapsed_time - 1.0) / 1.0
        delta_movement = int(delta_movement)
        iterations = 1 + delta_movement
        for i in range(iterations):
            # Random number between 1 and 200 to create the 1/200 random chance for each power up
            power_up_update = random.randint(-50, 150)
            power_up_time = time.time()

    # Used when VSync is off
    tick_update = tick_update + 1

    # Screen update is 1 when the screen has been changed
    if screen_update == 1:
        # Things that need to be updated between screens are updated here
        # Old button and text box sprites are removed
        for bu in buttons_on_screen_list:
            bu.remove()
        buttons_on_screen_list.clear()
        current_button_index = 0
        if page_update != 1:
            for pa in panel_turtle:
                pa.remove()
            panel_index = 0
        for t in text_on_screen_list:
            t.get_text_box().clear()
            t.remove()
        text_on_screen_list.clear()
        current_text_index = 0
        for pl in price_label_on_screen_list:
            pl.remove()
        price_label_on_screen_list.clear()
        current_price_index = 0
        for s in selectors_on_screen_list:
            s.remove()
        selectors_on_screen_list.clear()
        current_selector_index = 0
        score = 0
        refresh_variables.refresh_indicator = 1
        refresh_variables.refresh_text = 1
        screen_update = 0
        page_update = 0
        print(len(wn.turtles()))

    # The Alien Mode background objects are created right when the game is launched.
    # This is done to make sure that they are truely in the background and that nothing lies behind these sprites.
    # Since turtle does not allow a way to push a turtle in front of another turtle, this is the only way to do this.
    if len(background_objects) == 0:
        spawn_background_objects()
        for bo in background_objects:
            bo.remove()
        background_objects_index = 0

    if len(sun_turtle) == 0:
        spawn_sun()
        for s in sun_turtle:
            s.remove()
        sun_index = 0

    """
        When Title Mode is on
    """

    if mode == "Title_Mode":
        # Remove and reset all power ups
        for pu in current_power_ups:
            pu.remove()
        current_power_ups.clear()
        power_up_index[0] = 0
        power_up_index[1] = 0
        power_up_index[2] = 0
        power_up_index[3] = 0

        # Remove the coin indicator
        for ci in coin_indicator_turtle:
            ci.remove()
        coin_indicator_index = 0

        # Remove the power up indicators
        for yi in yellow_power_up_indicator_turtle:
            yi.remove()
        yellow_power_up_indicator_index = 0
        for bi in blue_power_up_indicator_turtle:
            bi.remove()
        blue_power_up_indicator_index = 0
        for ei in extra_power_up_indicator_turtle:
            ei.remove()
        extra_power_up_indicator_index = 0

        # Remove all the coins on the screen
        for coin in coins_on_screen_list:
            coin.remove()
        coins_on_screen_list.clear()
        current_coin_index = 0
        coin_pickup_delay = 0

        # Spawn the title mode buttons
        if current_button_index == 0:
            for i in range(4):
                spawn_buttons("Title", i + 1)
            for i in range(2):
                spawn_buttons("Title_Small", i + 1)

        # Spawn the title mode text (Like title and bversion number in the bottom corner)
        if current_text_index == 0:
            spawn_text_box(1, 0, 155 * scale_factor_Y, "red")
            spawn_text_box(2, 510 * scale_factor_X, -347 * scale_factor_Y, "white")
            if god_mode == 1:
                spawn_text_box(3, 481 * scale_factor_X, 320 * scale_factor_Y, "white")
        for t in text_on_screen_list:
            if t.id == 1:
                t.move(mode, scale_factor_X)

        # detect if the buttons have been clicked
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Title":
                # If the mouse is hovering over the valid button
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    # Run the button function if clicked
                    wn.onscreenclick(launch_machine_mode)
                elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_alien_mode)
                elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_shop_mode)
                elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(exit_game)
            elif button_type == "Title_Small":
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_settings_mode)
                elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_stats_mode)

    """
        When Machine Mode is on
    """

    if mode == "Machine_Mode":
        # Create the in game main menu button
        if current_button_index == 0:
            spawn_buttons("Game", 1)

        # Check if the main menu button has been clicked or not
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                wn.onscreenclick(launch_title_mode)

        # Spawn the rest of the game interface
        # This includes the power up timers
        # The power up timers are created as just ordinary text boxes with the correct colors
        # This is done to ensure turtle are being reused
        if current_text_index == 0:
            spawn_text_box(1, 0, 320 * scale_factor_Y, "white")
            spawn_text_box(2, -65 * scale_factor_X, 278 * scale_factor_Y, "#737000")
            spawn_text_box(3, 10 * scale_factor_X, 278 * scale_factor_Y, "#00001A")
            spawn_text_box(4, 80 * scale_factor_X, 278 * scale_factor_Y, "#001C00")
            spawn_text_box(5, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
            if god_mode == 1:
                spawn_text_box(6, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

        # Spawn the coin indicator
        if coin_indicator_index == 0:
            spawn_coin_indicator()

        # Spawn the yellow power up indicator
        if yellow_power_up_indicator_index == 0:
            spawn_yellow_power_up_indicator()

        # Spawn the blue power up indicator
        if blue_power_up_indicator_index == 0:
            spawn_blue_power_up_indicator()

        # Spawn the green power up indicator
        if extra_power_up_indicator_index == 0:
            spawn_extra_power_up_indiciator()

        # Check if the players score is greater than the current high score
        if god_mode == 0:
            if score > high_score_machine_war:
                # Update the high score in the game and the ini file if it is
                high_score_machine_war = score
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                high_score = list(config['High_Score'])[0]
                config['High_Score'][high_score] = str(high_score_machine_war)
                with open('Config/playerData.ini', 'w') as configfile:
                    config.write(configfile)

        # Spawn the player
        if current_player_index == 0:
            spawn_machine_player()
        # Spawn 3 blue machines to start the game
        if blue_machine_index == 0:
            for i in range(3):
                spawn_blue_machine(i + 1)

        # Used to shoot the players laser
        for p in current_player:
            p.shoot(yellow_power_up_indicator_turtle[0].get_power_up_active(), scale_factor_Y)

        # Spawn Machine enemies based on the players score
        # At its peak, there will be 5 blue machines, 5 yellow machines, 5 red machines, and 1 machine boss attacking
        #   the player
        if score >= 10 and blue_machine_index == 3:
            spawn_blue_machine(4)
        elif score >= 20 and blue_machine_index == 4:
            spawn_blue_machine(5)
        elif score >= 30 and yellow_machine_index == 0:
            spawn_yellow_machine(1)
        elif score >= 40 and yellow_machine_index == 1:
            spawn_yellow_machine(2)
        elif score >= 50 and yellow_machine_index == 2:
            spawn_yellow_machine(3)
        elif score >= 60 and yellow_machine_index == 3:
            spawn_yellow_machine(4)
        elif score >= 70 and yellow_machine_index == 4:
            spawn_yellow_machine(5)
        elif score >= 80 and red_machine_index == 0:
            spawn_red_machine(1)
        elif score >= 100 and red_machine_index == 1:
            spawn_red_machine(2)
        elif score >= 120 and red_machine_index == 2:
            spawn_red_machine(3)
        elif score >= 140 and red_machine_index == 3:
            spawn_red_machine(4)
        elif score >= 160 and red_machine_index == 4:
            spawn_red_machine(5)
        elif score >= 200 and boss_index == 0:
            spawn_boss()
        # If score is 0, reset the number of enemies back down to 3
        elif score == 0:
            for blue_machine in blue_machines:
                if blue_machine.get_id() == 4 or blue_machine.get_id() == 5:
                    blue_machine.remove()
                    blue_machine_index = blue_machine_index - 1
            if len(blue_machines_update_values) == 4:
                blue_machines_update_values.pop(3)
                blue_machines.pop(3)
            elif len(blue_machines_update_values) == 5:
                blue_machines_update_values.pop(4)
                blue_machines_update_values.pop(3)
                blue_machines.pop(4)
                blue_machines.pop(3)

            for yellow_machine in yellow_machines:
                yellow_machine.remove()
            yellow_machines.clear()
            yellow_machine_index = 0
            yellow_machines_update_values.clear()
            for red_machine in red_machines:
                red_machine.remove()
            red_machines.clear()
            red_machine_index = 0
            red_machines_update_values.clear()
            red_machines_hit_values.clear()
            for b in boss:
                b.remove()
            boss.clear()
            boss_index = 0
            boss_update_value = 0
            boss_hit_value = 0
            coin_pickup_delay = 0

        # Run the functions to shoot the lasers for each of the enemies
        for blue_machine in blue_machines:
            blue_machine.shoot_laser(extra_power_up_indicator_turtle[0].get_power_up_active(), enemy_shooting_sound, scale_factor_Y)

        for yellow_machine in yellow_machines:
            yellow_machine.shoot_laser(extra_power_up_indicator_turtle[0].get_power_up_active(), enemy_shooting_sound, scale_factor_Y)

        for red_machine in red_machines:
            red_machine.shoot_laser(extra_power_up_indicator_turtle[0].get_power_up_active(), enemy_shooting_sound, scale_factor_Y)

        for b in boss:
            b.shoot_laser(extra_power_up_indicator_turtle[0].get_power_up_active(), enemy_shooting_sound, scale_factor_Y)

        # Detects if the players has picked up a coin
        hit_coin = 0
        for coin in coins_on_screen_list:
            for p in current_player:
                # If the player picks up a coin
                if p.get_laser().isvisible() and p.get_laser().distance(coin.get_coin()) < 55 * scale_factor and coin_pickup_delay == 0:
                    coin.remove()
                    # Increase the amount of coins based on the type of coin picked up
                    if coin.get_type() == "copper":
                        total_coins = total_coins + 1
                        machine_coins_collected = machine_coins_collected + 1
                    elif coin.get_type() == "silver":
                        total_coins = total_coins + 5
                        machine_coins_collected = machine_coins_collected + 5
                    elif coin.get_type() == "gold":
                        total_coins = total_coins + 10
                        machine_coins_collected = machine_coins_collected + 10
                    elif coin.get_type() == "platinum":
                        total_coins = total_coins + 25
                        machine_coins_collected = machine_coins_collected + 25
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    coins = list(config['Coins'])[0]
                    config['Coins'][coins] = str(total_coins)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                    coins = list(config['Statistics_Machine_Mode'])[8]
                    config['Statistics_Machine_Mode'][coins] = str(machine_coins_collected)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                    coins_on_screen_list.pop(hit_coin)
                    # play the coin pickup sound
                    if coin_pickup_sound == 1:
                        sound = pygame.mixer.Sound("Sound/Coin_Pickup_Sound.wav")
                        sound.play()
                hit_coin = hit_coin + 1

        # Enemy Killer
        for p in current_player:
            current_blue_update_value_index = 0
            for bm in blue_machines:
                # If the player laser hits a blue machine that is visible and not dying
                if (bm.get_blue_machine().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(bm.get_blue_machine()) < 55 * scale_factor and blue_machines_update_values[current_blue_update_value_index] == 0) or blue_machines_update_values[current_blue_update_value_index] != 0:
                    # Kill the enemy
                    bm.kill_enemy(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    blue_machines_update_values[current_blue_update_value_index] = blue_machines_update_values[current_blue_update_value_index] + 1
                    # Check if the death animation is finished
                    if bm.get_update_value() == 0:
                        blue_machines_update_values[current_blue_update_value_index] = 0
                        coin_pickup_delay = 0
                    # Delay the coin pickup so it does not pick up the coin at the same time as killing the enemy
                    if bm.get_update_value() == 3:
                        coin_pickup_delay = 1
                    if blue_machines_update_values[current_blue_update_value_index] == 1:
                        # Increase the players score
                        # When the blue power up is active, the score increases are doubled (This is universal)
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 2
                        else:
                            score = score + 1
                        # Update the stats if god mode is off
                        if god_mode == 0:
                            blue_bots_killed = blue_bots_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[3]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(blue_bots_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        # Confirm that the players laser has attacked
                        p.set_laser_has_attacked(1)
                current_blue_update_value_index = current_blue_update_value_index + 1

            current_yellow_update_value_index = 0
            for ym in yellow_machines:
                # If the player laser hits a yellow machine that is visible and not dying
                if (ym.get_yellow_machine().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(ym.get_yellow_machine()) < 59 * scale_factor and yellow_machines_update_values[current_yellow_update_value_index] == 0) or yellow_machines_update_values[current_yellow_update_value_index] != 0:
                    # Same procedure as before
                    ym.kill_enemy(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    yellow_machines_update_values[current_yellow_update_value_index] = yellow_machines_update_values[current_yellow_update_value_index] + 1
                    if ym.get_update_value() == 0:
                        yellow_machines_update_values[current_yellow_update_value_index] = 0
                        coin_pickup_delay = 0
                    if ym.get_update_value() == 3:
                        coin_pickup_delay = 1
                    if yellow_machines_update_values[current_yellow_update_value_index] == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 4
                        else:
                            score = score + 2
                        if god_mode == 0:
                            yellow_bots_killed = yellow_bots_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[2]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(yellow_bots_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        p.set_laser_has_attacked(1)
                current_yellow_update_value_index = current_yellow_update_value_index + 1

            current_red_update_value_index = 0
            current_red_hit_value_index = 0
            for rm in red_machines:
                # If the player laser hits a red machine that is visible and not dying with 1 health
                if red_machines_update_values[current_red_update_value_index] != 0 or (rm.get_red_machine().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(rm.get_red_machine()) < 64 * scale_factor and rm.health_bar == 1 and rm.hit_delay == 0 and red_machines_update_values[current_red_update_value_index] == 0):
                    rm.kill_enemy(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    red_machines_update_values[current_red_update_value_index] = red_machines_update_values[current_red_update_value_index] + 1
                    if rm.get_update_value() == 0:
                        red_machines_update_values[current_red_update_value_index] = 0
                        coin_pickup_delay = 0
                    if rm.get_update_value() == 3:
                        coin_pickup_delay = 1
                    if red_machines_update_values[current_red_update_value_index] == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 10
                        else:
                            score = score + 5
                        if god_mode == 0:
                            red_bots_killed = red_bots_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[1]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(red_bots_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        p.set_laser_has_attacked(1)
                current_red_update_value_index = current_red_update_value_index + 1

                # If the player laser hits a red machine that is visible and not dying with health > 1
                if red_machines_hit_values[current_red_hit_value_index] != 0 or (rm.get_red_machine().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(rm.get_red_machine()) < 64 * scale_factor and rm.health_bar != 1 and rm.health_bar != 0 and red_machines_hit_values[current_red_hit_value_index] == 0):
                    # Deal 1 health of damage to the red machine, but do not kill it yet
                    rm.hit_enemy(enemy_hit_sound, fullscreen)
                    red_machines_hit_values[current_red_hit_value_index] = red_machines_hit_values[current_red_hit_value_index] + 1
                    # Check if hit delay is finished
                    if rm.get_hit_value() == 0:
                        red_machines_hit_values[current_red_hit_value_index] = 0
                    if red_machines_hit_values[current_red_hit_value_index] == 1:
                        # Increase the players score for hitting the red machine
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 2
                        else:
                            score = score + 1
                        # Confirm that the players laser has attacked and make it disappear
                        p.set_laser_has_attacked(1)
                current_red_hit_value_index = current_red_hit_value_index + 1

            for b in boss:
                # If the player laser hits the boss that is visible and not dying with 1 health
                if boss_update_value != 0 or (b.get_boss().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(b.get_boss()) < 75 * scale_factor and b.health_bar == 1 and b.hit_delay == 0 and boss_update_value == 0):
                    b.kill_boss(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    boss_update_value = boss_update_value + 1
                    if b.get_update_value() == 0:
                        boss_update_value = 0
                        coin_pickup_delay = 0
                    if b.get_update_value() == 3:
                        coin_pickup_delay = 1
                    if boss_update_value == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 100
                        else:
                            score = score + 50
                        if god_mode == 0:
                            bosses_killed = bosses_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[0]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(bosses_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        p.set_laser_has_attacked(1)

                # If the player laser hits the boss that is visible and not dying with health > 1
                if boss_hit_value != 0 or (b.get_boss().isvisible() and p.get_laser().isvisible() and p.get_laser().distance(b.get_boss()) < 75 * scale_factor and b.health_bar != 1 and b.health_bar != 0 and boss_hit_value == 0):
                    b.hit_boss(enemy_hit_sound, fullscreen)
                    boss_hit_value = boss_hit_value + 1
                    if b.get_hit_value() == 0:
                        boss_hit_value = 0
                    if boss_hit_value == 1:
                        # First hit gets double the points, the rest are only 1 point
                        # This means that the total points you can get from killing
                        #   one boss is 60 (120 with blue power up)
                        if b.health_bar == 9:
                            if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                score = score + 4
                            else:
                                score = score + 2
                        else:
                            if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                score = score + 2
                            else:
                                score = score + 1
                        p.set_laser_has_attacked(1)

        # Player Killer
        for p in current_player:
            # If the death animation has already started
            if player_update_value != 0:
                # Keep going with the player death animation if it has started
                p.kill_player(player_death_sound, scale_factor_Y, fullscreen)
                player_update_value = player_update_value + 1
                if p.get_player_death_update() == 0.6:
                    # Reset the initial and staying blue machines death count
                    for bm in blue_machines:
                        bm.set_death_count(0)
                    # Update the stats if god mode is off
                    if god_mode == 0:
                        classic_deaths = classic_deaths + 1
                        machine_damage_taken = machine_damage_taken + 1
                        config = configparser.ConfigParser()
                        config.read('Config/playerData.ini')
                        statistic_to_update = list(config['Statistics_Machine_Mode'])[4]
                        config['Statistics_Machine_Mode'][statistic_to_update] = str(classic_deaths)
                        with open('Config/playerData.ini', 'w') as configfile:
                            config.write(configfile)
                        statistic_to_update = list(config['Statistics_Machine_Mode'])[5]
                        config['Statistics_Machine_Mode'][statistic_to_update] = str(machine_damage_taken)
                        with open('Config/playerData.ini', 'w') as configfile:
                            config.write(configfile)
                # Check if the death animation is finished
                if p.get_player_death_update() == 0:
                    player_update_value = 0
            # If the death animation is not ongoing
            else:
                # For every enemy, check if the enemies laser has hit the player
                for bm in blue_machines:
                    if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if bm.get_blue_machine_laser().isvisible() and -30 * scale_factor_X < (bm.get_blue_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            bm.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and god_mode == 0:
                                # If so kill the player and set the score down to 0 to reset the game
                                p.kill_player(player_death_sound, scale_factor_Y, fullscreen)
                                score = 0
                                player_update_value = player_update_value + 1

                for ym in yellow_machines:
                    if ym.get_yellow_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if ym.get_yellow_machine_laser().isvisible() and -30 * scale_factor_X < (ym.get_yellow_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            ym.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.kill_player(player_death_sound, scale_factor_Y, fullscreen)
                                score = 0
                                player_update_value = player_update_value + 1

                for rm in red_machines:
                    if rm.get_red_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if rm.get_red_machine_laser().isvisible() and -30 * scale_factor_X < (rm.get_red_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            rm.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.kill_player(player_death_sound, scale_factor_Y, fullscreen)
                                score = 0
                                player_update_value = player_update_value + 1

                for b in boss:
                    if b.get_boss_laser().distance(p.get_player()) < 125 * scale_factor:
                        if b.get_boss_laser().isvisible() and -30 * scale_factor_X < (b.get_boss_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            b.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.kill_player(player_death_sound, scale_factor_Y, fullscreen)
                                score = 0
                                player_update_value = player_update_value + 1

            # If the player has more than 1 health, only deal 1 health of damage
            # If the hit delay is ongoing
            if player_hit_value != 0:
                p.hit_player(player_hit_sound, fullscreen)
                player_hit_value = player_hit_value + 1
                # Update the stats
                if p.get_hit_delay() == 2:
                    machine_damage_taken = machine_damage_taken + 1
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    statistic_to_update = list(config['Statistics_Machine_Mode'])[5]
                    config['Statistics_Machine_Mode'][statistic_to_update] = str(machine_damage_taken)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                if p.get_hit_delay() == 0:
                    player_hit_value = 0
            # If there is no hit delay
            else:
                # Check if the lasers of any enemies have hit the player
                for bm in blue_machines:
                    if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if bm.get_blue_machine_laser().isvisible() and -30 * scale_factor_X < (bm.get_blue_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            bm.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and god_mode == 0:
                                # Hit the player
                                p.hit_player(player_hit_sound, fullscreen)
                                player_hit_value = player_hit_value + 1

                for ym in yellow_machines:
                    if ym.get_yellow_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if ym.get_yellow_machine_laser().isvisible() and -30 * scale_factor_X < (ym.get_yellow_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            ym.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.hit_player(player_hit_sound, fullscreen)
                                player_hit_value = player_hit_value + 1

                for rm in red_machines:
                    if rm.get_red_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                        if rm.get_red_machine_laser().isvisible() and -30 * scale_factor_X < (rm.get_red_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            rm.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.hit_player(player_hit_sound, fullscreen)
                                player_hit_value = player_hit_value + 1

                for b in boss:
                    if b.get_boss_laser().distance(p.get_player()) < 125 * scale_factor:
                        if b.get_boss_laser().isvisible() and -30 * scale_factor_X < (b.get_boss_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                            b.set_laser_has_attacked(1)
                            if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and god_mode == 0:
                                p.hit_player(player_hit_sound, fullscreen)
                                player_hit_value = player_hit_value + 1

        # Function for the float effect of the machine enemies
        # This float effect was added to create the illusion that the enemies are flying through outer space at
        #   fast speeds
        for bm in blue_machines:
            bm.float_effect(scale_factor_Y)

        for ym in yellow_machines:
            ym.float_effect(scale_factor_Y)

        for rm in red_machines:
            rm.float_effect(scale_factor_Y)

        for b in boss:
            b.float_effect(scale_factor_Y)

        # For the enemy movement
        # If the machine enemy has been killed enough times, it will start moving along the x-axis
        for p in current_player:
            for bm in blue_machines:
                bm.move_enemy(p.get_death_animation(), scale_factor_X)

            for ym in yellow_machines:
                ym.move_enemy(p.get_death_animation(), scale_factor_X)

            for rm in red_machines:
                rm.move_enemy(p.get_death_animation(), scale_factor_X, scale_factor_Y)

            for b in boss:
                b.move_boss(p.get_death_animation(), scale_factor_X, scale_factor_Y)

        # Check if the power ups are active or not
        for t in text_on_screen_list:
            # If they are, activate the power up timers
            if t.id == 2:
                if yellow_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("yellow")
                else:
                    t.set_color("#737000")
            elif t.id == 3:
                if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("#02CCFE")
                else:
                    t.set_color("#00004A")
            elif t.id == 4:
                if extra_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("#65FE08")
                else:
                    t.set_color("#001C00")

        # Activate the power up indicators if the power ups become active
        for yi in yellow_power_up_indicator_turtle:
            yi.set_texture(fullscreen)

        for bi in blue_power_up_indicator_turtle:
            bi.set_texture(fullscreen)

        for ei in extra_power_up_indicator_turtle:
            ei.set_texture(fullscreen)

        # If the RNG hits the 1/200, then spawn the power ups
        # 1 for yellow power up
        if power_up_update == 1 and yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[0] == 0:
                spawn_power_up(1)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 1:
                        pu.spawn(power_up_spawn_sound)

        # 50 for blue power up
        if power_up_update == 50 and blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[1] == 0:
                spawn_power_up(2)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 2:
                        pu.spawn(power_up_spawn_sound)

        # 100 for the extra power up
        if power_up_update == 100 and extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[2] == 0:
                spawn_power_up(3)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 3:
                        pu.spawn(power_up_spawn_sound)

        # Check if the player has picked up a power up or not
        for p in current_player:
            for pu in current_power_ups:
                # If a power up is visible
                if pu.get_power_up().isvisible():
                    # Check its type (1 = yellow, 2 = blue, and 3 = green)
                    # If the player runs to the power up
                    if pu.type == 1 and pu.get_power_up().distance(p.get_player()) < 27 * scale_factor and p.get_death_animation() == 0 and yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        # Pick it up
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        # Update the stats
                        if god_mode == 0:
                            classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[7]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(classic_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        # Activate the specified power up (In this case yellow)
                        yellow_power_up_indicator_turtle[0].set_power_up_active(1)

                    if pu.type == 2 and pu.get_power_up().distance(p.get_player()) < 27 * scale_factor and p.get_death_animation() == 0 and blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        if god_mode == 0:
                            classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[7]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(classic_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        blue_power_up_indicator_turtle[0].set_power_up_active(1)

                    if pu.type == 3 and pu.get_power_up().distance(p.get_player()) < 27 * scale_factor and p.get_death_animation() == 0 and extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        if god_mode == 0:
                            classic_power_ups_picked_up = classic_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Machine_Mode'])[7]
                            config['Statistics_Machine_Mode'][statistic_to_update] = str(classic_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        extra_power_up_indicator_turtle[0].set_power_up_active(1)

        # If the power ups are active, run their timers through these functions
        for yi in yellow_power_up_indicator_turtle:
            yi.set_timer()

        for bi in blue_power_up_indicator_turtle:
            bi.set_timer()

        for ei in extra_power_up_indicator_turtle:
            ei.set_timer()

    # If Machine Mode is toggled off
    else:
        # Remove all the Machine Mode sprites from the screen
        for p in current_player:
            p.remove()
        current_player.clear()
        current_player_index = 0
        player_update_value = 0
        for bm in blue_machines:
            bm.remove()
        blue_machines.clear()
        blue_machine_index = 0
        blue_machines_update_values.clear()
        for ym in yellow_machines:
            ym.remove()
        yellow_machines.clear()
        yellow_machine_index = 0
        yellow_machines_update_values.clear()
        for rm in red_machines:
            rm.remove()
        red_machines.clear()
        red_machine_index = 0
        red_machines_update_values.clear()
        red_machines_hit_values.clear()
        for b in boss:
            b.remove()
        boss.clear()
        boss_index = 0
        boss_update_value = 0
        boss_hit_value = 0

    """
        Code Below is for when Alien Mode is turned on.
    """

    if mode == "Alien_Mode":
        # Create the in game main menu button
        if current_button_index == 0:
            spawn_buttons("Game", 1)

        # Check if the main menu button has been clicked or not
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                wn.onscreenclick(launch_title_mode)

        # Spawn the rest of the game interface
        # This includes the power up timers
        # The power up timers are created as just ordinary text boxes with the correct colors
        # This is done to ensure turtle are being reused
        if current_text_index == 0:
            spawn_text_box(1, 0, 320 * scale_factor_Y, "white")
            spawn_text_box(2, -65 * scale_factor_X, 278 * scale_factor_Y, "#737000")
            spawn_text_box(3, 10 * scale_factor_X, 278 * scale_factor_Y, "#00001A")
            spawn_text_box(4, 80 * scale_factor_X, 278 * scale_factor_Y, "#300000")
            spawn_text_box(5, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
            if god_mode == 1:
                spawn_text_box(6, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

        # Spawn all of the Alien Mode background objects
        if sun_index == 0:
            spawn_sun()
        if earth_index == 0:
            spawn_earth()
        if background_objects_index == 0:
            spawn_background_objects()
        # Spawn the human player
        if current_human_index == 0:
            spawn_human_player()
        # Spawn three small aliens to start out
        if small_alien_index == 0:
            for i in range(3):
                spawn_small_alien(i + 1)

        # Spawn the coin indicator
        if coin_indicator_index == 0:
            spawn_coin_indicator()

        # Spawn the yellow power up indicator
        if yellow_power_up_indicator_index == 0:
            spawn_yellow_power_up_indicator()

        # Spawn the blue power up indicator
        if blue_power_up_indicator_index == 0:
            spawn_blue_power_up_indicator()

        # Spawn the red power up indicator
        if extra_power_up_indicator_index == 0:
            spawn_extra_power_up_indiciator()

        # Check if the players score is greater than the current high score
        if god_mode == 0:
            if score > high_score_alien_mode:
                # Update the high score in the game and the ini file if it is
                high_score_alien_mode = score
                config = configparser.ConfigParser()
                config.read('Config/playerData.ini')
                high_score = list(config['High_Score'])[1]
                config['High_Score'][high_score] = str(high_score_alien_mode)
                with open('Config/playerData.ini', 'w') as configfile:
                    config.write(configfile)

        # Check if the power ups are active or not
        for t in text_on_screen_list:
            # If they are, activate the power up timers
            if t.id == 2:
                if yellow_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("yellow")
                else:
                    t.set_color("#737000")
            elif t.id == 3:
                if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("#02CCFE")
                else:
                    t.set_color("#00004A")
            elif t.id == 4:
                if extra_power_up_indicator_turtle[0].get_power_up_active() == 1:
                    t.set_color("#FF0000")
                else:
                    t.set_color("#300000")

        # Activate the power up indicators if the power ups become active
        for yi in yellow_power_up_indicator_turtle:
            yi.set_texture(fullscreen)

        for bi in blue_power_up_indicator_turtle:
            bi.set_texture(fullscreen)

        for ei in extra_power_up_indicator_turtle:
            ei.set_texture(fullscreen)

        # If the RNG hits the 1/200, then spawn the power ups
        # 1 for yellow power up
        if power_up_update == 1 and yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[0] == 0:
                spawn_power_up(1)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 1:
                        pu.spawn(power_up_spawn_sound)

        # 50 for blue power up
        if power_up_update == 50 and blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[1] == 0:
                spawn_power_up(2)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 2:
                        pu.spawn(power_up_spawn_sound)

        # 100 for the extra power up
        if power_up_update == 100 and extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
            if power_up_index[3] == 0:
                spawn_power_up(4)
            else:
                for pu in current_power_ups:
                    if pu.get_type() == 4:
                        pu.spawn(power_up_spawn_sound)

        # Check if the player has picked up a power up or not
        for h in current_human:
            for pu in current_power_ups:
                # If a power up is visible
                if pu.get_power_up().isvisible():
                    # Check its type (1 = yellow, 2 = blue, and 3 = green)
                    # If the player runs to the power up
                    if pu.type == 1 and pu.get_power_up().distance(h.get_player()) < 27 * scale_factor and h.get_death_animation() == 0 and yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        # Pick it up
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        # Update the stats
                        if god_mode == 0:
                            alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[8]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(alien_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        # Activate the specified power up (In this case yellow)
                        yellow_power_up_indicator_turtle[0].set_power_up_active(1)

                    if pu.type == 2 and pu.get_power_up().distance(h.get_player()) < 27 * scale_factor and h.get_death_animation() == 0 and blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        if god_mode == 0:
                            alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[8]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(alien_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        blue_power_up_indicator_turtle[0].set_power_up_active(1)

                    if pu.type == 4 and pu.get_power_up().distance(h.get_player()) < 27 * scale_factor and h.get_death_animation() == 0 and extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                        pu.pick_up(power_up_pickup_sound, scale_factor_X, scale_factor_Y)
                        if god_mode == 0:
                            alien_power_ups_picked_up = alien_power_ups_picked_up + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[8]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(alien_power_ups_picked_up)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        extra_power_up_indicator_turtle[0].set_power_up_active(1)

        # If the power ups are active, run their timers through these functions
        for yi in yellow_power_up_indicator_turtle:
            yi.set_timer()

        for bi in blue_power_up_indicator_turtle:
            bi.set_timer()

        for ei in extra_power_up_indicator_turtle:
            ei.set_timer()

        # Spawn aliens based on the players score
        # At its peak, there will be 5 small aliens, 5 medium aliens, 5 large aliens, and 1 UFO attacking the player
        if score > 20 and small_alien_index == 3:
            spawn_small_alien(4)
        elif score > 40 and small_alien_index == 4:
            spawn_small_alien(5)
        elif score > 60 and medium_alien_index == 0:
            spawn_medium_alien(1)
        elif score > 80 and medium_alien_index == 1:
            spawn_medium_alien(2)
        elif score > 100 and medium_alien_index == 2:
            spawn_medium_alien(3)
        elif score > 120 and medium_alien_index == 3:
            spawn_medium_alien(4)
        elif score > 140 and medium_alien_index == 4:
            spawn_medium_alien(5)
        elif score > 160 and large_alien_index == 0:
            spawn_large_alien(1)
        elif score > 180 and large_alien_index == 1:
            spawn_large_alien(2)
        elif score > 200 and large_alien_index == 2:
            spawn_large_alien(3)
        elif score > 220 and large_alien_index == 3:
            spawn_large_alien(4)
        elif score > 240 and large_alien_index == 4:
            spawn_large_alien(5)
        elif score >= 300 and ufo_index == 0:
            spawn_alien_boss()
        # If score is less than 7, reset the number of aliens back down to 3
        elif score < 7:
            if small_alien_index == 4 or small_alien_index == 5:
                for small_alien in small_aliens:
                    small_alien.remove()
                small_aliens.clear()
                small_alien_index = 0
                small_aliens_kill_values.clear()
            for medium_alien in medium_aliens:
                medium_alien.remove()
            medium_aliens.clear()
            medium_alien_index = 0
            medium_aliens_kill_values.clear()
            medium_aliens_hit_values.clear()
            for large_alien in large_aliens:
                large_alien.remove()
            large_aliens.clear()
            large_alien_index = 0
            large_aliens_kill_values.clear()
            large_aliens_hit_values.clear()
            for u in ufos:
                u.remove()
            ufos.clear()
            ufo_index = 0
            ufo_update_value = 0
            ufo_hit_value = 0

        # Move the sun along the ellipse
        for s in sun_turtle:
            s.update_position(scale_factor_X, scale_factor_Y)

        # Check if a right movement of the player needs to be executed
        for h in current_human:
            h.execute_right_movement(scale_factor_X, scale_factor_Y)

        # Update the time variable used to create the walking right animation
        right_update = time.perf_counter()
        right_update = round(right_update, 1)

        # Cherck if a left movement of the player needs to be executed
        for h in current_human:
            h.execute_left_movement(scale_factor_X, scale_factor_Y)

        # Update the time variable used to create the walking left animation
        left_update = time.perf_counter()
        left_update = round(left_update, 1)

        # Check if a player jump needs to be executed
        for h in current_human:
            h.execute_jump(scale_factor_X, scale_factor_Y)

        # Check if the players laser needs to be shot
        for h in current_human:
            laser_update = h.execute_shoot(yellow_power_up_indicator_turtle[0].get_power_up_active(), laser_update, scale_factor_X)

        # Execute the walking animation for the player
        for h in current_human:
            h.set_player_texture(right_update, left_update, fullscreen)
            h.set_gun_texture(fullscreen)

        # Update the directions that each of the aliens are facing
        for h in current_human:
            for sa in small_aliens:
                sa.set_alien_direction(h.get_player().xcor())

            for ma in medium_aliens:
                ma.set_alien_direction(h.get_player().xcor())

            for la in large_aliens:
                la.set_alien_direction(h.get_player().xcor())

            for u in ufos:
                u.set_ufo_direction(h.get_player().xcor())

        # Update the aliens position, the aliens move faster the more times they are killed until the player dies
        for sa in small_aliens:
            sa.set_movement_speed(scale_factor_X)

        for ma in medium_aliens:
            ma.set_movement_speed(scale_factor_X)

        for la in large_aliens:
            la.set_movement_speed(scale_factor_X)

        for u in ufos:
            u.set_movement_speed(scale_factor_X)

        # Shoot the UFOs laser
        for u in ufos:
            u.shoot_laser(enemy_shooting_sound, scale_factor_X, scale_factor_Y)

        # Update the aliens texture based on their direction and the walking animation
        for sa in small_aliens:
            if sa.get_small_alien().isvisible():
                sa.set_alien_texture(right_update, left_update, fullscreen)

        for ma in medium_aliens:
            if ma.get_medium_alien().isvisible():
                ma.set_alien_texture(right_update, left_update, fullscreen)

        for la in large_aliens:
            if la.get_large_alien().isvisible():
                la.set_alien_texture(right_update, left_update, fullscreen)

        # Detects if the players has picked up a coin
        hit_coin = 0
        for coin in coins_on_screen_list:
            for h in current_human:
                # If the player picks up a coin
                if (h.get_laser().isvisible() and h.get_laser().distance(coin.get_coin()) < 55 * scale_factor) or h.get_player().distance(coin.get_coin()) < 55 * scale_factor:
                    coin.remove()
                    # Increase the amount of coins based on the type of coin picked up
                    if coin.get_type() == "copper":
                        total_coins = total_coins + 1
                        alien_coins_collected = alien_coins_collected + 1
                    elif coin.get_type() == "silver":
                        total_coins = total_coins + 5
                        alien_coins_collected = alien_coins_collected + 5
                    elif coin.get_type() == "gold":
                        total_coins = total_coins + 10
                        alien_coins_collected = alien_coins_collected + 10
                    elif coin.get_type() == "platinum":
                        total_coins = total_coins + 25
                        alien_coins_collected = alien_coins_collected + 25
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    coins = list(config['Coins'])[0]
                    config['Coins'][coins] = str(total_coins)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                    coins = list(config['Statistics_Alien_Mode'])[9]
                    config['Statistics_Alien_Mode'][coins] = str(alien_coins_collected)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                    coins_on_screen_list.pop(hit_coin)
                    # play the coin pickup sound
                    if coin_pickup_sound == 1:
                        sound = pygame.mixer.Sound("Sound/Coin_Pickup_Sound.wav")
                        sound.play()
                hit_coin = hit_coin + 1

        # Alien Killer
        for h in current_human:
            current_small_alien_update_value_index = 0
            for sa in small_aliens:
                # If the player laser hits a small alien that is visible and not dying
                if (sa.get_small_alien().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(sa.get_small_alien()) < 53 * scale_factor and (
                        (sa.get_small_alien().xcor() - 26 * scale_factor_X < h.get_laser().xcor() < sa.get_small_alien().xcor() + 26 * scale_factor_X) or yellow_power_up_indicator_turtle[0].get_power_up_active() == 1) and
                        small_aliens_kill_values[current_small_alien_update_value_index] == 0) or small_aliens_kill_values[current_small_alien_update_value_index] != 0:
                    # Kill the alien
                    sa.kill_alien(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    small_aliens_kill_values[current_small_alien_update_value_index] = small_aliens_kill_values[current_small_alien_update_value_index] + 1
                    # Check if the death animation is finished
                    if sa.get_death_animation() == 0:
                        small_aliens_kill_values[current_small_alien_update_value_index] = 0
                    if sa.get_death_animation() == 1:
                        # Increase the players score
                        # When the blue power up is active, the score increases are doubled (This is universal)
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 2
                        else:
                            score = score + 1
                        # Update the stats if god mode is off
                        if god_mode == 0:
                            small_aliens_killed = small_aliens_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[3]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(small_aliens_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        # Confirm that the players laser has attacked and count it as an enemy pierced
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1
                current_small_alien_update_value_index = current_small_alien_update_value_index + 1

            current_medium_alien_update_value_index = 0
            current_medium_alien_hit_value_index = 0
            for ma in medium_aliens:
                # If the player laser hits a medium alien that is visible and not dying and has 1 health
                if (ma.get_medium_alien().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(ma.get_medium_alien()) < 72 * scale_factor and (
                        (ma.get_medium_alien().xcor() - 36 * scale_factor_X < h.get_laser().xcor() < ma.get_medium_alien().xcor() + 36 * scale_factor_X) or yellow_power_up_indicator_turtle[0].get_power_up_active() == 1) and ma.health == 1 and ma.hit_delay == 0 and
                        medium_aliens_kill_values[current_medium_alien_update_value_index] == 0) or medium_aliens_kill_values[current_medium_alien_update_value_index] != 0:
                    # Same procedure as before
                    ma.kill_alien(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    medium_aliens_kill_values[current_medium_alien_update_value_index] = medium_aliens_kill_values[current_medium_alien_update_value_index] + 1
                    if ma.get_death_animation() == 0:
                        medium_aliens_kill_values[current_medium_alien_update_value_index] = 0
                    if ma.get_death_animation() == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 4
                        else:
                            score = score + 2
                        if god_mode == 0:
                            medium_aliens_killed = medium_aliens_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[2]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(medium_aliens_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1
                current_medium_alien_update_value_index = current_medium_alien_update_value_index + 1

                # If the player laser hits a medium alien that is visible and not dying and has health > 1
                if (ma.get_medium_alien().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(ma.get_medium_alien()) < 72 * scale_factor and (
                        (ma.get_medium_alien().xcor() - 36 * scale_factor_X < h.get_laser().xcor() < ma.get_medium_alien().xcor() + 36 * scale_factor_X) or yellow_power_up_indicator_turtle[0].get_power_up_active() == 1) and ma.get_medium_alien_health() == 2 and
                        medium_aliens_hit_values[current_medium_alien_hit_value_index] == 0) or medium_aliens_hit_values[current_medium_alien_hit_value_index] != 0:
                    # Deal one damage to the medium alien
                    ma.hit_alien(enemy_hit_sound, fullscreen)
                    medium_aliens_hit_values[current_medium_alien_hit_value_index] = medium_aliens_hit_values[current_medium_alien_hit_value_index] + 1
                    # Check if the hit delay is finished
                    if ma.get_hit_delay() == 0:
                        medium_aliens_hit_values[current_medium_alien_hit_value_index] = 0
                    if ma.get_hit_delay() == 1:
                        # Increase the players score for hitting the medium alien
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 2
                        else:
                            score = score + 1
                        # Confirm that the players laser has attacked and count it as an enemy pierced
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1
                current_medium_alien_hit_value_index = current_medium_alien_hit_value_index + 1

            current_large_alien_update_value_index = 0
            current_large_alien_hit_value_index = 0
            for la in large_aliens:
                # If the player laser hits a large alien that is visible and not dying and has 1 health
                if (la.get_large_alien().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(la.get_large_alien()) < 112 * scale_factor and (
                        (la.get_large_alien().xcor() - 50 * scale_factor_X < h.get_laser().xcor() < la.get_large_alien().xcor() + 50 * scale_factor_X) or yellow_power_up_indicator_turtle[0].get_power_up_active() == 1) and la.health == 1 and la.hit_delay == 0 and
                        large_aliens_kill_values[current_large_alien_update_value_index] == 0) or large_aliens_kill_values[current_large_alien_update_value_index] != 0:
                    la.kill_alien(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    large_aliens_kill_values[current_large_alien_update_value_index] = large_aliens_kill_values[current_large_alien_update_value_index] + 1
                    if la.get_death_animation() == 0:
                        large_aliens_kill_values[current_large_alien_update_value_index] = 0
                    if la.get_death_animation() == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 8
                        else:
                            score = score + 4
                        if god_mode == 0:
                            big_aliens_killed = big_aliens_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[1]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(big_aliens_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1
                current_large_alien_update_value_index = current_large_alien_update_value_index + 1

                # If the player laser hits a medium alien that is visible and not dying and has health > 1
                if (la.get_large_alien().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(la.get_large_alien()) < 112 * scale_factor and (
                        (la.get_large_alien().xcor() - 50 * scale_factor_X < h.get_laser().xcor() < la.get_large_alien().xcor() + 50 * scale_factor_X) or yellow_power_up_indicator_turtle[0].get_power_up_active() == 1) and (la.get_large_alien_health() == 2 or la.get_large_alien_health() == 3) and
                        large_aliens_hit_values[current_large_alien_hit_value_index] == 0) or large_aliens_hit_values[current_large_alien_hit_value_index] != 0:
                    # Same procedure as before
                    la.hit_alien(enemy_hit_sound, fullscreen)
                    large_aliens_hit_values[current_large_alien_hit_value_index] = large_aliens_hit_values[current_large_alien_hit_value_index] + 1
                    if la.get_hit_delay() == 0:
                        large_aliens_hit_values[current_large_alien_hit_value_index] = 0
                    if la.get_hit_delay() == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 2
                        else:
                            score = score + 1
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1
                current_large_alien_hit_value_index = current_large_alien_hit_value_index + 1

            for u in ufos:
                # If the player laser hits the UFO that is visible and not dying and has 1 health
                if ufo_kill_value != 0 or (u.get_ufo().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(u.get_ufo()) < 72 * scale_factor and
                        (u.get_ufo().xcor() - 53 * scale_factor_X < h.get_laser().xcor() < u.get_ufo().xcor() + 53 * scale_factor_X) and
                        u.get_ufo_health() == 1 and u.hit_delay == 0 and ufo_kill_value == 0):
                    u.kill_ufo(enemy_death_sound, coins_on_screen_list, all_coins_list, scale_factor_X, scale_factor_Y, fullscreen)
                    ufo_kill_value = ufo_kill_value + 1
                    if u.get_death_animation() == 0:
                        ufo_kill_value = 0
                    if u.get_death_animation() == 1:
                        if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            score = score + 100
                        else:
                            score = score + 50
                        if god_mode == 0:
                            ufos_killed = ufos_killed + 1
                            config = configparser.ConfigParser()
                            config.read('Config/playerData.ini')
                            statistic_to_update = list(config['Statistics_Alien_Mode'])[0]
                            config['Statistics_Alien_Mode'][statistic_to_update] = str(ufos_killed)
                            with open('Config/playerData.ini', 'w') as configfile:
                                config.write(configfile)
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1

                # If the player laser hits the UFO that is visible and not dying and has health > 1
                if ufo_hit_value != 0 or (u.get_ufo().isvisible() and h.get_laser().isvisible() and h.get_laser().distance(u.get_ufo()) < 72 * scale_factor and
                        (u.get_ufo().xcor() - 53 * scale_factor_X < h.get_laser().xcor() < u.get_ufo().xcor() + 53 * scale_factor_X) and
                        u.get_ufo_health() != 1 and u.get_ufo_health() != 0 and ufo_hit_value == 0):
                    u.hit_ufo(enemy_hit_sound, fullscreen)
                    ufo_hit_value = ufo_hit_value + 1
                    if u.get_hit_delay() == 0:
                        ufo_hit_value = 0
                    if u.get_hit_delay() == 1:
                        if u.get_ufo_health() == 2 or u.get_ufo_health() == 1:
                            if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                score = score + 6
                            else:
                                score = score + 3
                        elif u.get_ufo_health() == 5 or u.get_ufo_health() == 4 or u.get_ufo_health() == 3:
                            if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                score = score + 4
                            else:
                                score = score + 2
                        else:
                            if blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                score = score + 2
                            else:
                                score = score + 1
                        h.get_laser().hideturtle()
                        if extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            laser_update = laser_update + 1

        # Player Killer
        for h in current_human:
            # If the death animation has already started
            if human_update_value != 0:
                # Keep going with the players death animation
                h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                human_update_value = human_update_value + 1
                if h.get_death_iterator() == 2:
                    # Update the stats if god mode is off
                    if god_mode == 0:
                        alien_deaths = alien_deaths + 1
                        damage_taken = damage_taken + 1
                        config = configparser.ConfigParser()
                        config.read('Config/playerData.ini')
                        statistic_to_update = list(config['Statistics_Alien_Mode'])[4]
                        config['Statistics_Alien_Mode'][statistic_to_update] = str(alien_deaths)
                        with open('Config/playerData.ini', 'w') as configfile:
                            config.write(configfile)
                        statistic_to_update = list(config['Statistics_Alien_Mode'])[5]
                        config['Statistics_Alien_Mode'][statistic_to_update] = str(damage_taken)
                        with open('Config/playerData.ini', 'w') as configfile:
                            config.write(configfile)
                    # Set the store to 0 and reset the game
                    score = 0
                # Check if the death animation has finished
                if h.get_death_iterator() == 0:
                    human_update_value = 0
            # If the death animation is not ongoing
            else:
                # For every alien, check if the alien got close enough to hit the player
                for sa in small_aliens:
                    if sa.get_small_alien().distance(h.get_player()) < 70 * scale_factor:
                        # The players health also has to be 1
                        if h.health == 1 and h.hit_delay == 0 and sa.get_small_alien().xcor() - 12.5 * scale_factor_X < h.get_player().xcor() < sa.get_small_alien().xcor() + 12.5 * scale_factor_X and human_update_value == 0 and sa.get_death_animation() == 0 and god_mode == 0:
                            # Then, kill the player
                            h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                            human_update_value = human_update_value + 1

                for ma in medium_aliens:
                    if ma.get_medium_alien().distance(h.get_player()) < 100 * scale_factor:
                        if h.health == 1 and h.hit_delay == 0 and ma.get_medium_alien().xcor() - 15 * scale_factor_X < h.get_player().xcor() < ma.get_medium_alien().xcor() + 15 * scale_factor_X and human_update_value == 0 and ma.get_death_animation() == 0 and god_mode == 0:
                            h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                            human_update_value = human_update_value + 1

                for la in large_aliens:
                    if la.get_large_alien().distance(h.get_player()) < 160 * scale_factor:
                        if h.health == 1 and h.hit_delay == 0 and la.get_large_alien().xcor() - 18 * scale_factor_X < h.get_player().xcor() < la.get_large_alien().xcor() + 18 * scale_factor_X and human_update_value == 0 and la.get_death_animation() == 0 and god_mode == 0:
                            h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                            human_update_value = human_update_value + 1

                for u in ufos:
                    if u.get_ufo().distance(h.get_player()) < 53 * scale_factor:
                        if h.health == 1 and h.hit_delay == 0 and u.get_ufo().xcor() - 18 * scale_factor_X < h.get_player().xcor() < u.get_ufo().xcor() + 18 * scale_factor_X and human_update_value == 0 and u.get_ufo().isvisible() and u.get_death_animation() == 0 and god_mode == 0:
                            h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                            human_update_value = human_update_value + 1

                    if u.get_ufo_laser().distance(h.get_player()) < 25 * scale_factor:
                        if h.health == 1 and h.hit_delay == 0 and u.get_ufo_laser().isvisible() and god_mode == 0 and human_update_value == 0:
                            h.kill_player(player_death_sound, scale_factor_X, scale_factor_Y, fullscreen)
                            human_update_value = human_update_value + 1

            # If the player has more than 1 health, only deal 1 health owrth of damage
            # If the hit delay is ongoing
            if human_hit_value != 0:
                # keep it going
                h.hit_player(player_hit_sound, fullscreen)
                human_hit_value = human_hit_value + 1
                # Update the stats
                if h.get_hit_delay() == 2:
                    damage_taken = damage_taken + 1
                    config = configparser.ConfigParser()
                    config.read('Config/playerData.ini')
                    statistic_to_update = list(config['Statistics_Alien_Mode'])[5]
                    config['Statistics_Alien_Mode'][statistic_to_update] = str(damage_taken)
                    with open('Config/playerData.ini', 'w') as configfile:
                        config.write(configfile)
                if h.get_hit_delay() == 0:
                    human_hit_value = 0
            # If there is no hit delay
            else:
                # For every alien, check if the alien got close enough to hit the player
                for sa in small_aliens:
                    if sa.get_small_alien().distance(h.get_player()) < 70 * scale_factor:
                        # If the players health is greater than 1
                        if h.get_health() > 1 and sa.get_small_alien().xcor() - 12.5 * scale_factor_X < h.get_player().xcor() < sa.get_small_alien().xcor() + 12.5 * scale_factor_X and sa.get_death_animation() == 0 and h.get_hit_delay() == 0 and god_mode == 0:
                            # Hit the player
                            h.hit_player(player_hit_sound, fullscreen)
                            human_hit_value = human_hit_value + 1

                for ma in medium_aliens:
                    if ma.get_medium_alien().distance(h.get_player()) < 100 * scale_factor:
                        if h.get_health() > 1 and ma.get_medium_alien().xcor() - 15 * scale_factor_X < h.get_player().xcor() < ma.get_medium_alien().xcor() + 15 * scale_factor_X and ma.get_death_animation() == 0 and h.get_hit_delay() == 0 and god_mode == 0:
                            h.hit_player(player_hit_sound, fullscreen)
                            human_hit_value = human_hit_value + 1

                for la in large_aliens:
                    if la.get_large_alien().distance(h.get_player()) < 160 * scale_factor:
                        if h.get_health() > 1 and la.get_large_alien().xcor() - 18 * scale_factor_X < h.get_player().xcor() < la.get_large_alien().xcor() + 18 * scale_factor_X and la.get_death_animation() == 0 and h.get_hit_delay() == 0 and god_mode == 0:
                            h.hit_player(player_hit_sound, fullscreen)
                            human_hit_value = human_hit_value + 1

                for u in ufos:
                    # For the UFo, the player can get hurt by both touching the UFO and getting hit by the UFOs laser
                    if u.get_ufo().distance(h.get_player()) < 53 * scale_factor:
                        if h.get_health() > 1 and u.get_ufo().xcor() - 18 * scale_factor_X < h.get_player().xcor() < u.get_ufo().xcor() + 18 * scale_factor_X and u.get_ufo().isvisible() and u.get_death_animation() == 0 and h.get_hit_delay() == 0 and god_mode == 0:
                            h.hit_player(player_hit_sound, fullscreen)
                            human_hit_value = human_hit_value + 1

                    if u.get_ufo_laser().distance(h.get_player()) < 25 * scale_factor:
                        if h.get_health() > 1 and u.get_ufo_laser().isvisible() and god_mode == 0:
                            h.hit_player(player_hit_sound, fullscreen)
                            human_hit_value = human_hit_value + 1
    # If Alien Mode is toggled off
    else:
        # Remove all the Alien Mode exclusive sprites from the screen
        for s in sun_turtle:
            s.remove()
        sun_index = 0
        for e in earth_turtle:
            e.remove()
        earth_index = 0
        for bo in background_objects:
            bo.remove()
        background_objects_index = 0
        for h in current_human:
            h.remove(scale_factor_Y)
        current_human.clear()
        current_human_index = 0
        human_update_value = 0
        human_hit_value = 0
        laser_update = 0
        for small_alien in small_aliens:
            small_alien.remove()
        small_aliens.clear()
        small_alien_index = 0
        small_aliens_kill_values.clear()
        for medium_alien in medium_aliens:
            medium_alien.remove()
        medium_aliens.clear()
        medium_alien_index = 0
        medium_aliens_kill_values.clear()
        medium_aliens_hit_values.clear()
        for large_alien in large_aliens:
            large_alien.remove()
        large_aliens.clear()
        large_alien_index = 0
        large_aliens_kill_values.clear()
        large_aliens_hit_values.clear()
        for ufo in ufos:
            ufo.remove()
        ufos.clear()
        ufo_index = 0
        ufo_kill_value = 0
        ufo_hit_value = 0

    """
        Code below is for when the Shop is entered
    """

    if mode == "Shop":
        # Create the side panel
        if panel_index == 0:
            spawn_panel()

        # Create Main Menu button
        if current_button_index == 0:
            spawn_buttons("Game", 1)
            for i in range(3):
                spawn_buttons("Tab", i + 1)

        # Check if the main menu button has been clicked or not
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                wn.onscreenclick(launch_title_mode)

        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_slot()
            if button_type == "Tab":
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(display_machine_mode_page)
                elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(display_alien_mode_page)
                elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(display_power_up_page)

        # Spawn all the necessary standalone text
        if current_text_index == 0:
            spawn_text_box(1, -75 * scale_factor_X, 240 * scale_factor_Y, "red")
            spawn_text_box(2, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
            spawn_text_box(3, -500 * scale_factor_X, 190 * scale_factor_Y, "#ff5349")

        if current_selector_index == 0:
            spawn_selector("Tab")

        if page == "Machine_Mode":
            if current_button_index == 4:
                for i in range(5):
                    spawn_buttons("Shop_Slot", i + 1)

            if current_text_index == 3:
                counter = 4
                for bu in buttons_on_screen_list:
                    if bu.get_type() == "Shop_Slot":
                        if bu.get_indicator_toggled() == 1:
                            spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                            spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        counter = counter + 1

            if current_selector_index == 1:
                spawn_selector("Slot")

            if refresh_variables.move_tab_selector == 1:
                for s in selectors_on_screen_list:
                    if s.get_type() == "Tab":
                        for bu in buttons_on_screen_list:
                            if bu.get_type() == "Tab" and bu.get_id() == 1:
                                s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                refresh_variables.move_tab_selector = 0

            if refresh_variables.move_slot_selector == 1:
                for s in selectors_on_screen_list:
                    if s.get_type() == "Slot":
                        for bu in buttons_on_screen_list:
                            if bu.get_type() == "Shop_Slot" and bu.get_id() == shop_config.machine_slot_selected:
                                s.new_select(bu.get_button_frame().xcor(), bu.get_button_frame().ycor())
                                refresh_variables.move_slot_selector = 0

            for bu in buttons_on_screen_list:
                if bu.get_type() == "Shop_Slot":
                    if bu.get_id() == 1:
                        bu.toggle_indicator(shop_config.machine_slots_unlocked[0])
                    elif bu.get_id() == 2:
                        bu.toggle_indicator(shop_config.machine_slots_unlocked[1])
                    elif bu.get_id() == 3:
                        bu.toggle_indicator(shop_config.machine_slots_unlocked[2])
                    elif bu.get_id() == 4:
                        bu.toggle_indicator(shop_config.machine_slots_unlocked[3])
                    elif bu.get_id() == 5:
                        bu.toggle_indicator(shop_config.machine_slots_unlocked[4])

            for bu in buttons_on_screen_list:
                button_color, button_type, id = bu.click_slot()
                if bu.get_type() == "Shop_Slot":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_1_select)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_2_select)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_3_select)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_4_select)
                    elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_5_select)
        elif page == "Alien_Mode":
            if current_button_index == 4:
                for i in range(5):
                    spawn_buttons("Shop_Slot", i + 1)

            if current_text_index == 3:
                counter = 4
                for bu in buttons_on_screen_list:
                    if bu.get_type() == "Shop_Slot":
                        if bu.get_indicator_toggled() == 1:
                            spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                            spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        counter = counter + 1

            if current_selector_index == 1:
                spawn_selector("Slot")

            if refresh_variables.move_tab_selector == 1:
                for s in selectors_on_screen_list:
                    if s.get_type() == "Tab":
                        for bu in buttons_on_screen_list:
                            if bu.get_type() == "Tab" and bu.get_id() == 2:
                                s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                refresh_variables.move_tab_selector = 0

            if refresh_variables.move_slot_selector == 1:
                for s in selectors_on_screen_list:
                    if s.get_type() == "Slot":
                        for bu in buttons_on_screen_list:
                            if bu.get_type() == "Shop_Slot" and bu.get_id() == shop_config.alien_slot_selected:
                                s.new_select(bu.get_button_frame().xcor(), bu.get_button_frame().ycor())
                                refresh_variables.move_slot_selector = 0

            for bu in buttons_on_screen_list:
                if bu.get_type() == "Shop_Slot":
                    if bu.get_id() == 1:
                        bu.toggle_indicator(shop_config.alien_slots_unlocked[0])
                    elif bu.get_id() == 2:
                        bu.toggle_indicator(shop_config.alien_slots_unlocked[1])
                    elif bu.get_id() == 3:
                        bu.toggle_indicator(shop_config.alien_slots_unlocked[2])
                    elif bu.get_id() == 4:
                        bu.toggle_indicator(shop_config.alien_slots_unlocked[3])
                    elif bu.get_id() == 5:
                        bu.toggle_indicator(shop_config.alien_slots_unlocked[4])

            for bu in buttons_on_screen_list:
                button_color, button_type, id = bu.click_slot()
                if bu.get_type() == "Shop_Slot":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_1_select)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_2_select)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_3_select)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_4_select)
                    elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_5_select)
        elif page == "Power_Ups":
            if current_button_index == 4:
                for i in range(4):
                    spawn_buttons("Power_Up_Slot", i + 1)

            if current_text_index == 3:
                counter = 4
                for bu in buttons_on_screen_list:
                    if bu.get_type() == "Power_Up_Slot":
                        if bu.get_id() == 1:
                            if shop_config.yellow_power_up_level != 5 and shop_config.yellow_power_up_level != 0:
                                spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        elif bu.get_id() == 2:
                            if shop_config.blue_power_up_level != 5 and shop_config.blue_power_up_level != 0:
                                spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        elif bu.get_id() == 3:
                            if shop_config.green_power_up_level != 5 and shop_config.green_power_up_level != 0:
                                spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        elif bu.get_id() == 4:
                            if shop_config.red_power_up_level != 5 and shop_config.red_power_up_level != 0:
                                spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                spawn_price_label(bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                        counter = counter + 1

            if refresh_variables.move_tab_selector == 1:
                for s in selectors_on_screen_list:
                    if s.get_type() == "Tab":
                        for bu in buttons_on_screen_list:
                            if bu.get_type() == "Tab" and bu.get_id() == 3:
                                s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                refresh_variables.move_tab_selector = 0

            for bu in buttons_on_screen_list:
                if bu.get_type() == "Power_Up_Slot":
                    if bu.get_id() == 1:
                        bu.toggle_indicator(shop_config.yellow_power_up_level)
                    elif bu.get_id() == 2:
                        bu.toggle_indicator(shop_config.blue_power_up_level)
                    elif bu.get_id() == 3:
                        bu.toggle_indicator(shop_config.green_power_up_level)
                    elif bu.get_id() == 4:
                        bu.toggle_indicator(shop_config.red_power_up_level)
                    bu.set_indicator_location(scale_factor_Y)

            for bu in buttons_on_screen_list:
                button_color, button_type, id = bu.click_slot()
                if bu.get_type() == "Power_Up_Slot":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_1_select)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_2_select)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_3_select)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(slot_4_select)

        # Spawn the coin indicator
        if coin_indicator_index == 0:
            spawn_coin_indicator()

        # Move the title text back and fourth across the screen as needed
        for t in text_on_screen_list:
            if t.id == 1:
                t.move(mode, scale_factor_X)
                break

        if refresh_variables.update_variables == 1:
            shop_config.load()
            refresh_variables.update_variables = 0

    """
         Code Below is for when Statistics Mode is turned on.
    """

    if mode == "Stats":
        # Create Main Menu button
        if current_button_index == 0:
            spawn_buttons("Game", 1)

        # Check if the button has been clicked
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                wn.onscreenclick(launch_title_mode)

        # Create the statistics text
        if current_text_index == 0:
            spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
            spawn_text_box(2, -320 * scale_factor_X, 140 * scale_factor_Y, "#ff5349")
            spawn_text_box(3, 320 * scale_factor_X, 140 * scale_factor_Y, "#ff5349")
            for i in range(10):
                spawn_text_box(i + 4, -320 * scale_factor_X, (90 - (i * 40)) * scale_factor_Y, "white")
            for i in range(11):
                spawn_text_box(13 + i + 1, 320 * scale_factor_X, (90 - (i * 40)) * scale_factor_Y, "white")
            if god_mode == 1:
                spawn_text_box(25, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

        # Move the title text back and fourth across the screen as needed
        for t in text_on_screen_list:
            if t.id == 1:
                t.move(mode, scale_factor_X)
                break

    """
        Code Below is for when Settings Mode is turned on.
    """

    if mode == "Settings":
        # Create all the screen buttons, including the toggle buttons
        if current_button_index == 0:
            for i in range(2):
                spawn_buttons("Regular_Settings_And_Controls", i + 1)
            for i in range(12):
                spawn_buttons("Settings_Toggle", i + 1)

        # Check if each of the buttons has been clicked
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Regular_Settings_And_Controls":
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_title_mode)
                elif id == 2 and (button_color == "yellow" or clickable == 1) and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_controls_mode)
                    clickable = 0
            elif button_type == "Settings_Toggle":
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_button_sound)
                elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_player_shooting_sound)
                elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_enemy_shooting_sound)
                elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_player_death_sound)
                elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_enemy_death_sound)
                elif id == 6 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_player_hit_sound)
                elif id == 7 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_enemy_hit_sound)
                elif id == 8 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_power_up_pickup_sound)
                elif id == 9 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_power_up_spawn_sound)
                elif id == 10 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_coin_pick_up_sound)
                elif id == 11 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_fullscreen)
                elif id == 12 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(toggle_vsync)

        # Create all additional text boxes
        if current_text_index == 0:
            spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
            if god_mode == 1:
                spawn_text_box(2, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

        # Move the title text left and right across the screen
        for t in text_on_screen_list:
            if t.id == 1:
                t.move(mode, scale_factor_X)
                break

        # Settings Data Updates
        # This is used to check if any of the configuration settings have been updated through the toggle buttons
        # If they have been, they are then updated in the current game
        # The only one not on here is the fullscreen one. That is because that one needs a restart.
        config = configparser.ConfigParser()
        config.read('Config/config.ini')
        if config['Settings'].getint('God_Mode') == 1:
            god_mode = 1
        else:
            god_mode = 0
        if config['Settings'].getint('Button_Sound') == 1:
            button_sound = 1
        else:
            button_sound = 0
        if config['Settings'].getint('Player_Shooting_Sound') == 1:
            player_shooting_sound = 1
        else:
            player_shooting_sound = 0
        if config['Settings'].getint('Enemy_Shooting_Sound') == 1:
            enemy_shooting_sound = 1
        else:
            enemy_shooting_sound = 0
        if config['Settings'].getint('Player_Death_Sound') == 1:
            player_death_sound = 1
        else:
            player_death_sound = 0
        if config['Settings'].getint('Enemy_Death_Sound') == 1:
            enemy_death_sound = 1
        else:
            enemy_death_sound = 0
        if config['Settings'].getint('Player_Hit_Sound') == 1:
            player_hit_sound = 1
        else:
            player_hit_sound = 0
        if config['Settings'].getint('Enemy_Hit_Sound') == 1:
            enemy_hit_sound = 1
        else:
            enemy_hit_sound = 0
        if config['Settings'].getint('Power_up_Pickup_Sound') == 1:
            power_up_pickup_sound = 1
        else:
            power_up_pickup_sound = 0
        if config['Settings'].getint('Power_up_Spawn_Sound') == 1:
            power_up_spawn_sound = 1
        else:
            power_up_spawn_sound = 0
        if config['Settings'].getint('Coin_Pick_Up_Sound') == 1:
            coin_pickup_sound = 1
        else:
            coin_pickup_sound = 0
        if config['Settings'].getint('VSync') == 1:
            vsync = 1
        else:
            vsync = 0

    """
        Code Below is for when Controls Mode is turned on.
    """

    if mode == "Controls":
        # Create all the buttons for the screen, including the toggle buttons.
        if current_button_index == 0:
            spawn_buttons("Regular_Settings_And_Controls", 1)
            spawn_buttons("Regular_Settings_And_Controls", 3)
            for i in range(4):
                spawn_buttons("Controls_Toggle", i + 1)

        # Check if any of the buttons have been clicked
        for bu in buttons_on_screen_list:
            button_color, button_type, id = bu.click_button()
            if button_type == "Regular_Settings_And_Controls":
                if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_title_mode)
                elif id == 3 and (button_color == "yellow" or clickable == 2) and bu.get_button_frame().isvisible():
                    wn.onscreenclick(launch_settings_mode)
                    clickable = 0
            elif button_type == "Controls_Toggle":
                if id == 1 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                    wn.onscreenclick(change_go_right_key)
                elif id == 2 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                    wn.onscreenclick(change_go_left_key)
                elif id == 3 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                    wn.onscreenclick(change_shoot_key)
                elif id == 4 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                    wn.onscreenclick(change_jump_key)

        # Create any additional text boxes
        if current_text_index == 0:
            spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
            if god_mode == 1:
                spawn_text_box(2, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

        # Move the title text left and right across the screen
        for t in text_on_screen_list:
            if t.id == 1:
                t.move(mode, scale_factor_X)
                break

        # Control Setting Conflict Updates
        # This checks if there are any conflicts with the current controls.
        # This is done here in case any new updates to the controls cause conflicts.
        if go_right_key != go_left_key and go_right_key != shoot_key and go_right_key != jump_key:
            go_right_key_alert = 0
        else:
            go_right_key_alert = 1

        if go_left_key != go_right_key and go_left_key != shoot_key and go_left_key != jump_key:
            go_left_key_alert = 0
        else:
            go_left_key_alert = 1

        if shoot_key != go_left_key and shoot_key != go_right_key and shoot_key != jump_key:
            shoot_key_alert = 0
        else:
            shoot_key_alert = 1

        if jump_key != go_left_key and jump_key != shoot_key and jump_key != go_right_key:
            jump_key_alert = 0
        else:
            jump_key_alert = 1
