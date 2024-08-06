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
# This is game version beta 1.1.0 released on 08/03/24

"""
    File: main.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file is the main file for Laser Fighter.
    The main file contains the main function, which contains the game loop.
    The game loop consists of three parts: The screen updater, the game quitter, and the event handler.
"""

import time
import random
from setup.ConfigurationSetup import *
from setup.WindowSetup import *
from setup.SpriteSetup import button
from setup.SpriteSetup import textbox
from setup.SpriteSetup import panel
from setup.SpriteSetup import selector
from setup.SpriteSetup import price_label
from setup.SpriteSetup import earth
from setup.SpriteSetup import sun
from setup.SpriteSetup import background_objects
from setup.SpriteSetup import power_up
from setup.SpriteSetup import yellow_power_up_indicator
from setup.SpriteSetup import blue_power_up_indicator
from setup.SpriteSetup import extra_power_up_indicator
from setup.SpriteSetup import coin
from setup.SpriteSetup import coin_indicator
from setup.SpriteSetup import machine_player
from setup.SpriteSetup import human_player
from setup.SpriteSetup import blue_machine
from setup.SpriteSetup import yellow_machine
from setup.SpriteSetup import red_machine
from setup.SpriteSetup import machine_boss
from setup.SpriteSetup import small_alien
from setup.SpriteSetup import medium_alien
from setup.SpriteSetup import large_alien
from setup.SpriteSetup import ufo
from setup.SpriteSetup import gadget
from setup.ModeSetupMaster import power_up_setup
from setup.ModeSetupMaster import machine_mode_setup
from setup.ModeSetupMaster import alien_mode_setup
from physics.CollisionMaster import machine_collision
from physics.CollisionMaster import alien_collision
from setup.UtilitySetup import screen
from setup.UtilitySetup import shop
from setup.UtilitySetup import settings_toggle
from setup.UtilitySetup import controls
from setup.UtilitySetup import text_refresh
from utils.PreventSleep import MonitorSleepController


def main():
    # Start the game tick counting
    start_ticks = pygame.time.get_ticks()
    # The main game loop:
    while True:
        """
            Screen Updater - Updates the screen with the events that occurred in the event handler
        """

        # If VSync is on
        if settings.vsync == 1:
            # Update the screen based on the refresh rate
            # For example, if the refresh rate is 60, update the screen 60 times a second
            current_ticks = pygame.time.get_ticks()
            elapsed_time = (current_ticks - start_ticks) / 1000.0

            if elapsed_time >= MONITOR_DELAY:
                text_refresh.update_text()
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
            if screen.mode == "Title_Mode":
                text_refresh.update_text()
            elif screen.mode == "Machine_Mode" or screen.mode == "Alien_Mode":
                if screen.tick_update % 15 == 0:
                    text_refresh.update_text()
            elif screen.mode == "Stats":
                if screen.tick_update % 4 == 0:
                    text_refresh.update_text()
            elif screen.mode == "Settings" or screen.mode == "Shop":
                if screen.tick_update % 3 == 0:
                    text_refresh.update_text()
            elif screen.mode == "Controls":
                if screen.tick_update % 5 == 0:
                    text_refresh.update_text()
            wn.update()

        """
            Loop Terminator - Terminates the game loop
        """

        # If requested, terminates the game loop
        if screen.quit_loop == 1:
            break

        """
            Event Handler - Updates all the game parameters and variables as needed
        """

        # Every 0.4 seconds, there is a 1/67 chance of a power up spawning (1/200 per a power up type)
        current_power_up_time = time.time()
        elapsed_power_up_time = current_power_up_time - power_up.power_up_time
        if elapsed_power_up_time >= 0.4:
            # See if more than 1 whole 0.4 seconds has passed (Just in case there is EXTREME lag)
            # If it has, run the random chance the number of 0.4 that have passed
            delta_movement = (elapsed_time - 1.0) / 1.0
            delta_movement = int(delta_movement)
            iterations = 1 + delta_movement
            for i in range(iterations):
                # Random number between 1 and 200 to create the 1/200 random chance for each power up
                power_up.power_up_update = random.randint(-50, 150)
                power_up.power_up_time = time.time()

        # Used when VSync is off
        screen.tick_update = screen.tick_update + 1

        """
            Screen Object Re-Setter
        """

        # Screen update is 1 when the screen has been changed
        if screen.screen_update == 1:
            # Things that need to be updated between screens are updated here
            # Old button and text box sprites are removed
            for bu in button.buttons_on_screen_list:
                bu.remove()
            button.buttons_on_screen_list.clear()
            button.current_button_index = 0
            if screen.page_update != 1:
                for pa in panel.panel_turtle:
                    pa.remove()
                panel.panel_index = 0
            for t in textbox.text_on_screen_list:
                t.get_text_box().clear()
                t.remove()
            textbox.text_on_screen_list.clear()
            textbox.current_text_index = 0
            for pl in price_label.price_label_on_screen_list:
                pl.remove()
            price_label.price_label_on_screen_list.clear()
            price_label.current_price_index = 0
            for s in selector.selectors_on_screen_list:
                s.remove()
            selector.selectors_on_screen_list.clear()
            selector.current_selector_index = 0
            statistics.score = 0
            refresh_variables.refresh_button = 1
            refresh_variables.refresh_indicator = 1
            refresh_variables.refresh_text = 1
            screen.screen_update = 0
            screen.page_update = 0
            button.buy_button_pressed = 0
            if screen.mode == "Machine_Mode" or screen.mode == "Alien_Mode":
                gadget.start_timer()
            print(len(wn.turtles()))

        # The game background objects and the panel is created right when the game is launched.
        # This is done to make sure that they are truly in the background and that nothing lies behind these sprites.
        # Since turtle does not allow a way to push a turtle in front of another turtle,
        #   this is the only way to do this.
        if len(panel.panel_turtle) == 0:
            panel.spawn_panel("Shop")
            for pa in panel.panel_turtle:
                pa.remove()
            panel.panel_index = 0

        if len(background_objects.background_objects_turtle) == 0:
            background_objects.spawn_background_objects()
            for bo in background_objects.background_objects_turtle:
                bo.remove()
            background_objects.background_objects_index = 0

        if len(sun.sun_turtle) == 0:
            sun.spawn_sun()
            for s in sun.sun_turtle:
                s.remove()
            sun.sun_index = 0

        """
            When Title Mode is on
        """

        if screen.mode == "Title_Mode":
            # Remove and reset all power ups
            for pu in power_up.current_power_ups:
                pu.remove()
            power_up.current_power_ups.clear()
            power_up.power_up_index[0] = 0
            power_up.power_up_index[1] = 0
            power_up.power_up_index[2] = 0
            power_up.power_up_index[3] = 0

            # Remove the coin indicator
            for ci in coin_indicator.coin_indicator_turtle:
                ci.remove()
            coin_indicator.coin_indicator_index = 0

            # Remove the power up indicators
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                yi.remove()
            yellow_power_up_indicator.yellow_power_up_indicator_index = 0
            for bi in blue_power_up_indicator.blue_power_up_indicator_turtle:
                bi.remove()
            blue_power_up_indicator.blue_power_up_indicator_index = 0
            for ei in extra_power_up_indicator.extra_power_up_indicator_turtle:
                ei.remove()
            extra_power_up_indicator.extra_power_up_indicator_index = 0

            # Remove all the coins on the screen
            for c in coin.coins_on_screen_list:
                c.remove()
            coin.coins_on_screen_list.clear()
            coin.current_coin_index = 0
            coin.coin_pickup_delay = 0

            # Spawn the title mode buttons
            if button.current_button_index == 0:
                for i in range(4):
                    button.spawn_button("Title", i + 1)
                for i in range(2):
                    button.spawn_button("Title_Small", i + 1)

            # Spawn the title mode text (Like title and version number in the bottom corner)
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 155 * scale_factor_Y, "red")
                textbox.spawn_text_box(2, 510 * scale_factor_X, -347 * scale_factor_Y, "white")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(3, 481 * scale_factor_X, 320 * scale_factor_Y, "white")
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)

            # detect if the buttons have been clicked
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Title":
                    # If the mouse is hovering over the valid button
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        # Run the button function if clicked
                        wn.onscreenclick(screen.launch_machine_mode)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_alien_mode)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_shop_mode)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.exit_game)
                elif button_type == "Title_Small":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_settings_mode)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_stats_mode)

        """
            When Machine Mode is on
        """

        if screen.mode == "Machine_Mode":
            # Create the in game main menu button
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)

            # Check if the main menu button has been clicked or not
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(screen.launch_title_mode)

            # Spawn the rest of the game interface
            # This includes the power up timers
            # The power up timers are created as just ordinary text boxes with the correct colors
            # This is done to ensure turtle are being reused
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 320 * scale_factor_Y, "white")
                textbox.spawn_text_box(2, -65 * scale_factor_X, 278 * scale_factor_Y, "#737000")
                textbox.spawn_text_box(3, 10 * scale_factor_X, 278 * scale_factor_Y, "#00001A")
                textbox.spawn_text_box(4, 80 * scale_factor_X, 278 * scale_factor_Y, "#001C00")
                textbox.spawn_text_box(5, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(6, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

            # Spawn the coin indicator
            if coin_indicator.coin_indicator_index == 0:
                coin_indicator.spawn_coin_indicator()

            # Spawn the yellow power up indicator
            if yellow_power_up_indicator.yellow_power_up_indicator_index == 0:
                yellow_power_up_indicator.spawn_yellow_power_up_indicator()

            # Spawn the blue power up indicator
            if blue_power_up_indicator.blue_power_up_indicator_index == 0:
                blue_power_up_indicator.spawn_blue_power_up_indicator()

            # Spawn the green power up indicator
            if extra_power_up_indicator.extra_power_up_indicator_index == 0:
                extra_power_up_indicator.spawn_extra_power_up_indiciator(screen.mode)

            # Check if the players score is greater than the current high score
            if settings.god_mode == 0:
                if statistics.score > statistics.high_score_machine_war:
                    # Update the high score in the game and the ini file if it is
                    statistics.high_score_machine_war = statistics.score
                    statistics.save()

            # Spawn the player
            if machine_player.current_player_index == 0:
                machine_player.spawn_machine_player(settings.god_mode)
            # Spawn 3 blue machines to start the game
            if blue_machine.blue_machine_index == 0:
                for i in range(3):
                    blue_machine.spawn_blue_machine(i + 1)

            # Used to shoot the players laser
            for p in machine_player.current_player:
                p.shoot(settings.player_shooting_sound, yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active())

            # Spawn Machine enemies based on the players score
            # At its peak, there will be 5 blue machines, 5 yellow machines, 5 red machines,
            #   and 1 machine boss attacking
            #   the player
            if statistics.score >= 10 and blue_machine.blue_machine_index == 3:
                blue_machine.spawn_blue_machine(4)
            elif statistics.score >= 20 and blue_machine.blue_machine_index == 4:
                blue_machine.spawn_blue_machine(5)
            elif statistics.score >= 30 and yellow_machine.yellow_machine_index == 0:
                yellow_machine.spawn_yellow_machine(1)
            elif statistics.score >= 40 and yellow_machine.yellow_machine_index == 1:
                yellow_machine.spawn_yellow_machine(2)
            elif statistics.score >= 50 and yellow_machine.yellow_machine_index == 2:
                yellow_machine.spawn_yellow_machine(3)
            elif statistics.score >= 60 and yellow_machine.yellow_machine_index == 3:
                yellow_machine.spawn_yellow_machine(4)
            elif statistics.score >= 70 and yellow_machine.yellow_machine_index == 4:
                yellow_machine.spawn_yellow_machine(5)
            elif statistics.score >= 80 and red_machine.red_machine_index == 0:
                red_machine.spawn_red_machine(1)
            elif statistics.score >= 100 and red_machine.red_machine_index == 1:
                red_machine.spawn_red_machine(2)
            elif statistics.score >= 120 and red_machine.red_machine_index == 2:
                red_machine.spawn_red_machine(3)
            elif statistics.score >= 140 and red_machine.red_machine_index == 3:
                red_machine.spawn_red_machine(4)
            elif statistics.score >= 160 and red_machine.red_machine_index == 4:
                red_machine.spawn_red_machine(5)
            elif statistics.score >= 200 and machine_boss.boss_index == 0:
                machine_boss.spawn_boss()
            # If score is 0, reset the number of enemies back down to 3
            elif statistics.score == 0:
                for bm in blue_machine.blue_machines:
                    if bm.get_id() == 4 or bm.get_id() == 5:
                        bm.remove()
                        blue_machine.blue_machine_index = blue_machine.blue_machine_index - 1
                if len(blue_machine.blue_machines_update_values) == 4:
                    blue_machine.blue_machines_update_values.pop(3)
                    blue_machine.blue_machines.pop(3)
                elif len(blue_machine.blue_machines_update_values) == 5:
                    blue_machine.blue_machines_update_values.pop(4)
                    blue_machine.blue_machines_update_values.pop(3)
                    blue_machine.blue_machines.pop(4)
                    blue_machine.blue_machines.pop(3)

                for ym in yellow_machine.yellow_machines:
                    ym.remove()
                yellow_machine.yellow_machines.clear()
                yellow_machine.yellow_machine_index = 0
                yellow_machine.yellow_machines_update_values.clear()
                for rm in red_machine.red_machines:
                    rm.remove()
                red_machine.red_machines.clear()
                red_machine.red_machine_index = 0
                red_machine.red_machines_update_values.clear()
                red_machine.red_machines_hit_values.clear()
                for b in machine_boss.boss:
                    b.remove()
                machine_boss.boss.clear()
                machine_boss.boss_index = 0
                machine_boss.boss_update_value = 0
                machine_boss.boss_hit_value = 0
                coin.coin_pickup_delay = 0

            # Run the functions to shoot the lasers for each of the enemies
            for bm in blue_machine.blue_machines:
                bm.shoot_laser(extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active(), settings.enemy_shooting_sound)

            for ym in yellow_machine.yellow_machines:
                ym.shoot_laser(extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active(), settings.enemy_shooting_sound)

            for rm in red_machine.red_machines:
                rm.shoot_laser(extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active(), settings.enemy_shooting_sound)

            for b in machine_boss.boss:
                b.shoot_laser(extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active(), settings.enemy_shooting_sound)

            # Detects if the players has picked up a coin
            if not shop_config.coin_magnet_enabled:
                hit_coin = 0
                for c in coin.coins_on_screen_list:
                    for p in machine_player.current_player:
                        # Check each of the players lasers
                        for l in p.get_laser():
                            # If the player picks up a coin
                            if l.laser.isvisible() and \
                                    (c.range[0] < l.laser.xcor() < c.range[1]) and \
                                    l.laser.ycor() > c.collision_coordinate and \
                                    coin.coin_pickup_delay == 0:
                                # Remove the coin from the screen
                                c.remove()
                                # Increase the amount of coins the users has based on the type of coin picked up
                                if c.get_type() == "copper":
                                    # For each coin, check if the blue power up has a multiplier on it
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_blue_value
                                    else:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_value
                                elif c.get_type() == "silver":
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_blue_value
                                    else:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_value
                                elif c.get_type() == "gold":
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_blue_value
                                    else:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_value
                                elif c.get_type() == "platinum":
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_blue_value
                                    else:
                                        shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                                        statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_value
                                shop_config.save()
                                statistics.save()
                                coin.coins_on_screen_list.pop(hit_coin)
                                # play the coin pickup sound
                                if settings.coin_pickup_sound == 1:
                                    sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                                    sound.play()
                                break
                        hit_coin = hit_coin + 1
            else:
                gadget.attract_coins("Machine_Mode")
                hit_coin = 0
                for c in coin.coins_on_screen_list:
                    for p in machine_player.current_player:
                        if p.player.isvisible() and p.death_animation == 0 and p.player.distance(c.coin) < c.COIN_DISTANCE:
                            # Remove the coin from the screen
                            c.remove()
                            # Increase the amount of coins the users has based on the type of coin picked up
                            if c.get_type() == "copper":
                                # For each coin, check if the blue power up has a multiplier on it
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_value
                            elif c.get_type() == "silver":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_value
                            elif c.get_type() == "gold":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_value
                            elif c.get_type() == "platinum":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_value
                            shop_config.save()
                            statistics.save()
                            coin.coins_on_screen_list.pop(hit_coin)
                            # play the coin pickup sound
                            if settings.coin_pickup_sound == 1:
                                sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                                sound.play()
                        hit_coin = hit_coin + 1

            # Create the machine hitboxes when requested (Value of do_collision is determined by the index of the laser)
            for p in machine_player.current_player:
                if p.do_collision == 1:
                    machine_collision.calculate_collisions(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active(), 0)
                    p.do_collision = 0
                elif p.do_collision == 2:
                    machine_collision.calculate_collisions(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active(), 1)
                    p.do_collision = 0
                elif p.do_collision == 3:
                    machine_collision.calculate_collisions(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active(), 2)
                    p.do_collision = 0

            # Enemy Killer
            for p in machine_player.current_player:
                current_blue_update_value_index = 0
                for bm in blue_machine.blue_machines:
                    # If the player laser hits a blue machine that is visible and not dying
                    if bm.get_blue_machine().isvisible() and blue_machine.blue_machines_update_values[current_blue_update_value_index] == 0:
                        for i in range(len(p.get_laser())):
                            if p.get_laser()[i].laser.isvisible() and \
                                    (bm.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < bm.x_range_list[i][1]) and \
                                    p.get_laser()[i].laser.ycor() > bm.collision_y_coordinate_list[i]:
                                # Kill the enemy
                                bm.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                                blue_machine.blue_machines_update_values[current_blue_update_value_index] = blue_machine.blue_machines_update_values[current_blue_update_value_index] + 1

                                # Increase the players score
                                # When the blue power up is active, the score increases are doubled (This is universal)
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 1 * machine_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 1 * machine_mode_setup.regular_score_multiplier

                                # Update the stats if god mode is off
                                if settings.god_mode == 0:
                                    statistics.blue_bots_killed = statistics.blue_bots_killed + 1
                                    statistics.save()

                                # Confirm that the players laser has attacked
                                p.set_laser_has_attacked(1, i)
                    elif blue_machine.blue_machines_update_values[current_blue_update_value_index] != 0:
                        # Kill the enemy
                        bm.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        blue_machine.blue_machines_update_values[current_blue_update_value_index] = blue_machine.blue_machines_update_values[current_blue_update_value_index] + 1

                        # Check if the death animation is finished
                        if bm.get_update_value() == 0:
                            blue_machine.blue_machines_update_values[current_blue_update_value_index] = 0
                            coin.coin_pickup_delay = 0

                        # Delay the coin pickup so it does not pick up the coin at the same time as killing the enemy
                        if bm.get_update_value() == 3:
                            coin.coin_pickup_delay = 1
                    current_blue_update_value_index = current_blue_update_value_index + 1

                current_yellow_update_value_index = 0
                for ym in yellow_machine.yellow_machines:
                    # If the player laser hits a yellow machine that is visible and not dying
                    if ym.get_yellow_machine().isvisible() and yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] == 0:
                        for i in range(len(p.get_laser())):
                            if p.get_laser()[i].laser.isvisible() and \
                                    (ym.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < ym.x_range_list[i][1]) and \
                                    p.get_laser()[i].laser.ycor() > ym.collision_y_coordinate_list[i]:
                                # Same procedure as before
                                ym.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                                yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] = yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] + 1

                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 2 * machine_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 2 * machine_mode_setup.regular_score_multiplier

                                if settings.god_mode == 0:
                                    statistics.yellow_bots_killed = statistics.yellow_bots_killed + 1
                                    statistics.save()

                                p.set_laser_has_attacked(1, i)
                    elif yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] != 0:
                        # Same procedure as before
                        ym.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] = yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] + 1

                        if ym.get_update_value() == 0:
                            yellow_machine.yellow_machines_update_values[current_yellow_update_value_index] = 0
                            coin.coin_pickup_delay = 0

                        if ym.get_update_value() == 3:
                            coin.coin_pickup_delay = 1
                    current_yellow_update_value_index = current_yellow_update_value_index + 1

                current_red_update_value_index = 0
                current_red_hit_value_index = 0
                for rm in red_machine.red_machines:
                    # If the player laser hits a red machine that is visible and not dying with health less
                    #   than or equal to damage
                    if rm.get_red_machine().isvisible() and red_machine.red_machines_update_values[current_red_update_value_index] == 0:
                        if rm.health_bar <= machine_mode_setup.damage and rm.hit_delay == 0:
                            for i in range(len(p.get_laser())):
                                if p.get_laser()[i].laser.isvisible() and \
                                        (rm.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < rm.x_range_list[i][1]) and \
                                        p.get_laser()[i].laser.ycor() > rm.collision_y_coordinate_list[i]:
                                    rm.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                                    red_machine.red_machines_update_values[current_red_update_value_index] = red_machine.red_machines_update_values[current_red_update_value_index] + 1

                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 5 * machine_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 5 * machine_mode_setup.regular_score_multiplier

                                    if settings.god_mode == 0:
                                        statistics.red_bots_killed = statistics.red_bots_killed + 1
                                        statistics.save()

                                    p.set_laser_has_attacked(1, i)
                    elif red_machine.red_machines_update_values[current_red_update_value_index] != 0:
                        rm.kill_enemy(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        red_machine.red_machines_update_values[current_red_update_value_index] = red_machine.red_machines_update_values[current_red_update_value_index] + 1

                        if rm.get_update_value() == 0:
                            red_machine.red_machines_update_values[current_red_update_value_index] = 0
                            coin.coin_pickup_delay = 0

                        if rm.get_update_value() == 3:
                            coin.coin_pickup_delay = 1
                    current_red_update_value_index = current_red_update_value_index + 1

                    # If the player laser hits a red machine that is visible and not dying with health > damage
                    if rm.get_red_machine().isvisible() and red_machine.red_machines_hit_values[current_red_hit_value_index] == 0:
                        if rm.health_bar > machine_mode_setup.damage:
                            for i in range(len(p.get_laser())):
                                if p.get_laser()[i].laser.isvisible() and \
                                        (rm.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < rm.x_range_list[i][1]) and \
                                        p.get_laser()[i].laser.ycor() > rm.collision_y_coordinate_list[i]:
                                    # Deal 1 health of damage to the red machine, but do not kill it yet
                                    rm.hit_enemy(settings.enemy_hit_sound)
                                    red_machine.red_machines_hit_values[current_red_hit_value_index] = red_machine.red_machines_hit_values[current_red_hit_value_index] + 1

                                    # Increase the players score for hitting the red machine
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 1 * machine_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 1 * machine_mode_setup.regular_score_multiplier

                                    # Confirm that the players laser has attacked and make it disappear
                                    p.set_laser_has_attacked(1, i)
                    elif red_machine.red_machines_hit_values[current_red_hit_value_index] != 0:
                        # Deal 1 health of damage to the red machine, but do not kill it yet
                        rm.hit_enemy(settings.enemy_hit_sound)
                        red_machine.red_machines_hit_values[current_red_hit_value_index] = red_machine.red_machines_hit_values[current_red_hit_value_index] + 1

                        # Check if hit delay is finished
                        if rm.get_hit_value() == 0:
                            red_machine.red_machines_hit_values[current_red_hit_value_index] = 0
                    current_red_hit_value_index = current_red_hit_value_index + 1

                for b in machine_boss.boss:
                    # If the player laser hits the boss that is visible and not dying with health <= damage
                    if b.get_boss().isvisible() and machine_boss.boss_update_value == 0:
                        if b.health_bar <= machine_mode_setup.damage and b.hit_delay == 0:
                            for i in range(len(p.get_laser())):
                                if p.get_laser()[i].laser.isvisible() and \
                                        (b.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < b.x_range_list[i][1]) and \
                                        p.get_laser()[i].laser.ycor() > b.collision_y_coordinate_list[i]:
                                    b.kill_boss(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                                    machine_boss.boss_update_value = machine_boss.boss_update_value + 1

                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 50 * machine_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 50 * machine_mode_setup.regular_score_multiplier

                                    if settings.god_mode == 0:
                                        statistics.bosses_killed = statistics.bosses_killed + 1
                                        statistics.save()

                                    p.set_laser_has_attacked(1, i)
                    elif machine_boss.boss_update_value != 0:
                        b.kill_boss(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        machine_boss.boss_update_value = machine_boss.boss_update_value + 1

                        if b.get_update_value() == 0:
                            machine_boss.boss_update_value = 0
                            coin.coin_pickup_delay = 0

                        if b.get_update_value() == 3:
                            coin.coin_pickup_delay = 1

                    # If the player laser hits the boss that is visible and not dying with health > damage
                    if b.get_boss().isvisible() and machine_boss.boss_hit_value == 0:
                        # Same procedure as before
                        if b.health_bar > machine_mode_setup.damage:
                            for i in range(len(p.get_laser())):
                                if p.get_laser()[i].laser.isvisible() and \
                                        (b.x_range_list[i][0] < p.get_laser()[i].laser.xcor() < b.x_range_list[i][1]) and \
                                        p.get_laser()[i].laser.ycor() > b.collision_y_coordinate_list[i]:
                                    b.hit_boss(settings.enemy_hit_sound)
                                    machine_boss.boss_hit_value = machine_boss.boss_hit_value + 1

                                    if b.health_bar == 9:
                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 2 * machine_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 2 * machine_mode_setup.regular_score_multiplier
                                    else:
                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 1 * machine_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 1 * machine_mode_setup.regular_score_multiplier

                                    p.set_laser_has_attacked(1, i)
                    elif machine_boss.boss_hit_value != 0:
                        b.hit_boss(settings.enemy_hit_sound)
                        machine_boss.boss_hit_value = machine_boss.boss_hit_value + 1

                        if b.get_hit_value() == 0:
                            machine_boss.boss_hit_value = 0

            # Player Killer
            for p in machine_player.current_player:
                # If the death animation has already started
                if machine_player.player_update_value != 0:
                    # Keep going with the player death animation if it has started
                    p.kill_player(settings.player_death_sound)
                    machine_player.player_update_value = machine_player.player_update_value + 1
                    if p.get_player_death_update() == 0.6:
                        # Reset the initial and staying blue machines death count
                        for bm in blue_machine.blue_machines:
                            bm.set_death_count(0)
                        # Update the stats if god mode is off
                        if settings.god_mode == 0:
                            statistics.classic_deaths = statistics.classic_deaths + 1
                            statistics.machine_damage_taken = statistics.machine_damage_taken + 1
                            statistics.save()
                    # Check if the death animation is finished
                    if p.get_player_death_update() == 0:
                        machine_player.player_update_value = 0
                # If the death animation is not ongoing
                else:
                    # For every enemy, check if the enemies laser has hit the player
                    for bm in blue_machine.blue_machines:
                        if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if bm.get_blue_machine_laser().isvisible() and -30 * scale_factor_X < (bm.get_blue_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                bm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    # If so kill the player and set the score down to 0 to reset the game
                                    p.kill_player(settings.player_death_sound)
                                    statistics.score = 0
                                    machine_player.player_update_value = machine_player.player_update_value + 1

                    for ym in yellow_machine.yellow_machines:
                        if ym.get_yellow_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if ym.get_yellow_machine_laser().isvisible() and -30 * scale_factor_X < (ym.get_yellow_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                ym.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.kill_player(settings.player_death_sound)
                                    statistics.score = 0
                                    machine_player.player_update_value = machine_player.player_update_value + 1

                    for rm in red_machine.red_machines:
                        if rm.get_red_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if rm.get_red_machine_laser().isvisible() and -30 * scale_factor_X < (rm.get_red_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                rm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.kill_player(settings.player_death_sound)
                                    statistics.score = 0
                                    machine_player.player_update_value = machine_player.player_update_value + 1

                    for b in machine_boss.boss:
                        if b.get_boss_laser().distance(p.get_player()) < 125 * scale_factor:
                            if b.get_boss_laser().isvisible() and -30 * scale_factor_X < (b.get_boss_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                b.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.kill_player(settings.player_death_sound)
                                    statistics.score = 0
                                    machine_player.player_update_value = machine_player.player_update_value + 1

                # If the player has more than 1 health, only deal 1 health of damage
                # If the hit delay is ongoing
                if machine_player.player_hit_value != 0:
                    p.hit_player(settings.player_hit_sound)
                    machine_player.player_hit_value = machine_player.player_hit_value + 1
                    # Update the stats
                    if p.get_hit_delay() == 2:
                        statistics.machine_damage_taken = statistics.machine_damage_taken + 1
                        statistics.save()
                    if p.get_hit_delay() == 0:
                        machine_player.player_hit_value = 0
                # If there is no hit delay
                else:
                    # Check if the lasers of any enemies have hit the player
                    for bm in blue_machine.blue_machines:
                        if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if bm.get_blue_machine_laser().isvisible() and -30 * scale_factor_X < (bm.get_blue_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                bm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    # Hit the player
                                    p.hit_player(settings.player_hit_sound)
                                    machine_player.player_hit_value = machine_player.player_hit_value + 1

                    for ym in yellow_machine.yellow_machines:
                        if ym.get_yellow_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if ym.get_yellow_machine_laser().isvisible() and -30 * scale_factor_X < (ym.get_yellow_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                ym.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.hit_player(settings.player_hit_sound)
                                    machine_player.player_hit_value = machine_player.player_hit_value + 1

                    for rm in red_machine.red_machines:
                        if rm.get_red_machine_laser().distance(p.get_player()) < 125 * scale_factor:
                            if rm.get_red_machine_laser().isvisible() and -30 * scale_factor_X < (rm.get_red_machine_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                rm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.hit_player(settings.player_hit_sound)
                                    machine_player.player_hit_value = machine_player.player_hit_value + 1

                    for b in machine_boss.boss:
                        if b.get_boss_laser().distance(p.get_player()) < 125 * scale_factor:
                            if b.get_boss_laser().isvisible() and -30 * scale_factor_X < (b.get_boss_laser().xcor() - p.get_player().xcor()) < 30 * scale_factor_X:
                                b.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0 and settings.god_mode == 0:
                                    p.hit_player(settings.player_hit_sound)
                                    machine_player.player_hit_value = machine_player.player_hit_value + 1

            # Function for the float effect of the machine enemies
            # This float effect was added to create the illusion that the enemies are flying through outer space at
            #   fast speeds
            for bm in blue_machine.blue_machines:
                bm.float_effect()

            for ym in yellow_machine.yellow_machines:
                ym.float_effect()

            for rm in red_machine.red_machines:
                rm.float_effect()

            for b in machine_boss.boss:
                b.float_effect()

            # For the enemy movement
            # If the machine enemy has been killed enough times, it will start moving along the x-axis
            for p in machine_player.current_player:
                for bm in blue_machine.blue_machines:
                    bm.move_enemy(p.get_death_animation())

                for ym in yellow_machine.yellow_machines:
                    ym.move_enemy(p.get_death_animation())

                for rm in red_machine.red_machines:
                    rm.move_enemy(p.get_death_animation())

                for b in machine_boss.boss:
                    b.move_boss(p.get_death_animation())

            # Check if the power ups are active or not
            for t in textbox.text_on_screen_list:
                # If they are, activate the power up timers
                if t.id == 2:
                    if yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("yellow")
                    else:
                        t.set_color("#737000")
                elif t.id == 3:
                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("#02CCFE")
                    else:
                        t.set_color("#00004A")
                elif t.id == 4:
                    if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("#65FE08")
                    else:
                        t.set_color("#001C00")

            # Activate the power up indicators if the power ups become active
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                yi.set_texture()

            for bi in blue_power_up_indicator.blue_power_up_indicator_turtle:
                bi.set_texture()

            for ei in extra_power_up_indicator.extra_power_up_indicator_turtle:
                ei.set_texture()

            # If the RNG hits the 1/200, then spawn the power ups
            # The chances are increased when the spawn rate is 2 up to 1/100 RNG
            # 1 for yellow power up
            if (power_up.power_up_update == 1 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 2)) and yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[0] == 0:
                    power_up.spawn_power_up(1, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 1:
                            pu.spawn(settings.power_up_spawn_sound)

            # 50 for blue power up
            if (power_up.power_up_update == 50 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 51)) and blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[1] == 0:
                    power_up.spawn_power_up(2, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 2:
                            pu.spawn(settings.power_up_spawn_sound)

            # 100 for the extra power up
            if (power_up.power_up_update == 100 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 101)) and extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[2] == 0:
                    power_up.spawn_power_up(3, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 3:
                            pu.spawn(settings.power_up_spawn_sound)

            # Check if the player has picked up a power up or not
            for p in machine_player.current_player:
                for pu in power_up.current_power_ups:
                    # If a power up is visible
                    if pu.get_power_up().isvisible():
                        # Check its type (1 = yellow, 2 = blue, and 3 = green)
                        # If the player runs to the power up
                        if pu.type == 1 and pu.get_power_up().distance(p.get_player()) < 50 * scale_factor and p.get_death_animation() == 0 and yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            # Pick it up
                            pu.pick_up(settings.power_up_pickup_sound)
                            # Update the stats
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            # Activate the specified power up (In this case yellow)
                            yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].set_power_up_active(1)

                        if pu.type == 2 and pu.get_power_up().distance(p.get_player()) < 50 * scale_factor and p.get_death_animation() == 0 and blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            blue_power_up_indicator.blue_power_up_indicator_turtle[0].set_power_up_active(1)

                        if pu.type == 3 and pu.get_power_up().distance(p.get_player()) < 50 * scale_factor and p.get_death_animation() == 0 and extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            extra_power_up_indicator.extra_power_up_indicator_turtle[0].set_power_up_active(1)

            # If the power ups are active, run their timers through these functions
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                yi.set_timer()

            for bi in blue_power_up_indicator.blue_power_up_indicator_turtle:
                bi.set_timer()

            for ei in extra_power_up_indicator.extra_power_up_indicator_turtle:
                ei.set_timer()

        # If Machine Mode is toggled off
        else:
            # Remove all the Machine Mode sprites from the screen
            for p in machine_player.current_player:
                p.remove()
            machine_player.current_player.clear()
            machine_player.current_player_index = 0
            machine_player.player_update_value = 0
            for bm in blue_machine.blue_machines:
                bm.remove()
            blue_machine.blue_machines.clear()
            blue_machine.blue_machine_index = 0
            blue_machine.blue_machines_update_values.clear()
            for ym in yellow_machine.yellow_machines:
                ym.remove()
            yellow_machine.yellow_machines.clear()
            yellow_machine.yellow_machine_index = 0
            yellow_machine.yellow_machines_update_values.clear()
            for rm in red_machine.red_machines:
                rm.remove()
            red_machine.red_machines.clear()
            red_machine.red_machine_index = 0
            red_machine.red_machines_update_values.clear()
            red_machine.red_machines_hit_values.clear()
            for b in machine_boss.boss:
                b.remove()
            machine_boss.boss.clear()
            machine_boss.boss_index = 0
            machine_boss.boss_update_value = 0
            machine_boss.boss_hit_value = 0

        """
            Code Below is for when Alien Mode is turned on.
        """

        if screen.mode == "Alien_Mode":
            # Create the in game main menu button
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)

            # Check if the main menu button has been clicked or not
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(screen.launch_title_mode)

            # Spawn the rest of the game interface
            # This includes the power up timers
            # The power up timers are created as just ordinary text boxes with the correct colors
            # This is done to ensure turtle are being reused
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 320 * scale_factor_Y, "white")
                textbox.spawn_text_box(2, -65 * scale_factor_X, 278 * scale_factor_Y, "#737000")
                textbox.spawn_text_box(3, 10 * scale_factor_X, 278 * scale_factor_Y, "#00001A")
                textbox.spawn_text_box(4, 80 * scale_factor_X, 278 * scale_factor_Y, "#300000")
                textbox.spawn_text_box(5, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(6, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

            # Spawn all of the Alien Mode background objects
            if sun.sun_index == 0:
                sun.spawn_sun()
            if earth.earth_index == 0:
                earth.spawn_earth()
            if background_objects.background_objects_index == 0:
                background_objects.spawn_background_objects()
            # Spawn the human player
            if human_player.current_human_index == 0:
                human_player.spawn_human_player(settings.god_mode)
            # Spawn three small aliens to start out
            if small_alien.small_alien_index == 0:
                for i in range(3):
                    small_alien.spawn_small_alien(i + 1)

            # Spawn the coin indicator
            if coin_indicator.coin_indicator_index == 0:
                coin_indicator.spawn_coin_indicator()

            # Spawn the yellow power up indicator
            if yellow_power_up_indicator.yellow_power_up_indicator_index == 0:
                yellow_power_up_indicator.spawn_yellow_power_up_indicator()

            # Spawn the blue power up indicator
            if blue_power_up_indicator.blue_power_up_indicator_index == 0:
                blue_power_up_indicator.spawn_blue_power_up_indicator()

            # Spawn the red power up indicator
            if extra_power_up_indicator.extra_power_up_indicator_index == 0:
                extra_power_up_indicator.spawn_extra_power_up_indiciator(screen.mode)

            # Check if the players score is greater than the current high score
            if settings.god_mode == 0:
                if statistics.score > statistics.high_score_alien_mode:
                    # Update the high score in the game and the ini file if it is
                    statistics.high_score_alien_mode = statistics.score
                    statistics.save()

            # Check if the power ups are active or not
            for t in textbox.text_on_screen_list:
                # If they are, activate the power up timers
                if t.id == 2:
                    if yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("yellow")
                    else:
                        t.set_color("#737000")
                elif t.id == 3:
                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("#02CCFE")
                    else:
                        t.set_color("#00004A")
                elif t.id == 4:
                    if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        t.set_color("#FF0000")
                    else:
                        t.set_color("#300000")

            # Activate the power up indicators if the power ups become active
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                yi.set_texture()

            for bi in blue_power_up_indicator.blue_power_up_indicator_turtle:
                bi.set_texture()

            for ei in extra_power_up_indicator.extra_power_up_indicator_turtle:
                ei.set_texture()

            # If the RNG hits the 1/200, then spawn the power ups
            # 1 for yellow power up
            if (power_up.power_up_update == 1 or (alien_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 2)) and yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[0] == 0:
                    power_up.spawn_power_up(1, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 1:
                            pu.spawn(settings.power_up_spawn_sound)

            # 50 for blue power up
            if (power_up.power_up_update == 50 or (alien_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 51)) and blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[1] == 0:
                    power_up.spawn_power_up(2, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 2:
                            pu.spawn(settings.power_up_spawn_sound)

            # 100 for the extra power up
            if (power_up.power_up_update == 100 or (alien_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 101)) and extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                if power_up.power_up_index[3] == 0:
                    power_up.spawn_power_up(4, screen.mode, settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 4:
                            pu.spawn(settings.power_up_spawn_sound)

            # Check if the player has picked up a power up or not
            for h in human_player.current_human:
                for pu in power_up.current_power_ups:
                    # If a power up is visible
                    if pu.get_power_up().isvisible():
                        # Check its type (1 = yellow, 2 = blue, and 3 = green)
                        # If the player runs to the power up
                        if pu.type == 1 and pu.get_power_up().distance(h.get_player()) < 50 * scale_factor and h.get_death_animation() == 0 and yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            # Pick it up
                            pu.pick_up(settings.power_up_pickup_sound)
                            # Update the stats
                            if settings.god_mode == 0:
                                statistics.alien_power_ups_picked_up = statistics.alien_power_ups_picked_up + 1
                                statistics.save()
                            # Activate the specified power up (In this case yellow)
                            yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].set_power_up_active(1)

                        if pu.type == 2 and pu.get_power_up().distance(h.get_player()) < 50 * scale_factor and h.get_death_animation() == 0 and blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.alien_power_ups_picked_up = statistics.alien_power_ups_picked_up + 1
                                statistics.save()
                            blue_power_up_indicator.blue_power_up_indicator_turtle[0].set_power_up_active(1)

                        if pu.type == 4 and pu.get_power_up().distance(h.get_player()) < 50 * scale_factor and h.get_death_animation() == 0 and extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.alien_power_ups_picked_up = statistics.alien_power_ups_picked_up + 1
                                statistics.save()
                            extra_power_up_indicator.extra_power_up_indicator_turtle[0].set_power_up_active(1)

            # If the power ups are active, run their timers through these functions
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                yi.set_timer()

            for bi in blue_power_up_indicator.blue_power_up_indicator_turtle:
                bi.set_timer()

            for ei in extra_power_up_indicator.extra_power_up_indicator_turtle:
                ei.set_timer()

            # Spawn aliens based on the players score
            # At its peak, there will be 5 small aliens, 5 medium aliens, 5 large aliens, and 1 UFO attacking the player
            if statistics.score > 20 and small_alien.small_alien_index == 3:
                small_alien.spawn_small_alien(4)
            elif statistics.score > 40 and small_alien.small_alien_index == 4:
                small_alien.spawn_small_alien(5)
            elif statistics.score > 60 and medium_alien.medium_alien_index == 0:
                medium_alien.spawn_medium_alien(1)
            elif statistics.score > 80 and medium_alien.medium_alien_index == 1:
                medium_alien.spawn_medium_alien(2)
            elif statistics.score > 100 and medium_alien.medium_alien_index == 2:
                medium_alien.spawn_medium_alien(3)
            elif statistics.score > 120 and medium_alien.medium_alien_index == 3:
                medium_alien.spawn_medium_alien(4)
            elif statistics.score > 140 and medium_alien.medium_alien_index == 4:
                medium_alien.spawn_medium_alien(5)
            elif statistics.score > 160 and large_alien.large_alien_index == 0:
                large_alien.spawn_large_alien(1)
            elif statistics.score > 180 and large_alien.large_alien_index == 1:
                large_alien.spawn_large_alien(2)
            elif statistics.score > 200 and large_alien.large_alien_index == 2:
                large_alien.spawn_large_alien(3)
            elif statistics.score > 220 and large_alien.large_alien_index == 3:
                large_alien.spawn_large_alien(4)
            elif statistics.score > 240 and large_alien.large_alien_index == 4:
                large_alien.spawn_large_alien(5)
            elif statistics.score >= 300 and ufo.ufo_index == 0:
                ufo.spawn_alien_boss()
            # If score is less than 7, reset the number of aliens back down to 3
            elif statistics.score < 7:
                if small_alien.small_alien_index == 4 or small_alien.small_alien_index == 5:
                    for sa in small_alien.small_aliens:
                        sa.remove()
                    small_alien.small_aliens.clear()
                    small_alien.small_alien_index = 0
                    small_alien.small_aliens_kill_values.clear()
                for ma in medium_alien.medium_aliens:
                    ma.remove()
                medium_alien.medium_aliens.clear()
                medium_alien.medium_alien_index = 0
                medium_alien.medium_aliens_kill_values.clear()
                medium_alien.medium_aliens_hit_values.clear()
                for la in large_alien.large_aliens:
                    la.remove()
                large_alien.large_aliens.clear()
                large_alien.large_alien_index = 0
                large_alien.large_aliens_kill_values.clear()
                large_alien.large_aliens_hit_values.clear()
                for u in ufo.ufos:
                    u.remove()
                ufo.ufos.clear()
                ufo.ufo_index = 0
                ufo.ufo_update_value = 0
                ufo.ufo_hit_value = 0

            # Move the sun along the ellipse
            for s in sun.sun_turtle:
                s.update_position()

            # Check if a right movement of the player needs to be executed
            for h in human_player.current_human:
                h.execute_right_movement(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active())

            # Update the time variable used to create the walking right animation
            human_player.right_update = time.perf_counter()
            human_player.right_update = round(human_player.right_update, 1)

            # Check if a left movement of the player needs to be executed
            for h in human_player.current_human:
                h.execute_left_movement(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active())

            # Update the time variable used to create the walking left animation
            human_player.left_update = time.perf_counter()
            human_player.left_update = round(human_player.left_update, 1)

            # Check if a player jump needs to be executed
            for h in human_player.current_human:
                h.execute_jump(yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active())

            # Check if the players laser needs to be shot
            for h in human_player.current_human:
                h.execute_shoot(settings.player_shooting_sound, yellow_power_up_indicator.yellow_power_up_indicator_turtle[0].get_power_up_active())

            # Execute the walking animation for the player
            for h in human_player.current_human:
                h.set_player_texture(human_player.right_update, human_player.left_update)
                h.set_gun_texture()

            # Update the directions that each of the aliens are facing
            for h in human_player.current_human:
                for sa in small_alien.small_aliens:
                    sa.set_alien_direction(h.get_player().xcor())

                for ma in medium_alien.medium_aliens:
                    ma.set_alien_direction(h.get_player().xcor())

                for la in large_alien.large_aliens:
                    la.set_alien_direction(h.get_player().xcor())

                for u in ufo.ufos:
                    u.set_ufo_direction(h.get_player().xcor())

            # Update the aliens position, the aliens move faster the more times they are killed until the player dies
            for sa in small_alien.small_aliens:
                sa.set_movement_speed()

            for ma in medium_alien.medium_aliens:
                ma.set_movement_speed()

            for la in large_alien.large_aliens:
                la.set_movement_speed()

            for u in ufo.ufos:
                u.set_movement_speed()

            # Shoot the UFOs laser
            for u in ufo.ufos:
                u.shoot_laser(settings.enemy_shooting_sound)

            # Update the aliens texture based on their direction and the walking animation
            for sa in small_alien.small_aliens:
                if sa.get_small_alien().isvisible():
                    sa.set_alien_texture(human_player.right_update, human_player.left_update)

            for ma in medium_alien.medium_aliens:
                if ma.get_medium_alien().isvisible():
                    ma.set_alien_texture(human_player.right_update, human_player.left_update)

            for la in large_alien.large_aliens:
                if la.get_large_alien().isvisible():
                    la.set_alien_texture(human_player.right_update, human_player.left_update)

            # Detects if the players has picked up a coin
            if not shop_config.coin_magnet_enabled:
                hit_coin = 0
                for c in coin.coins_on_screen_list:
                    for h in human_player.current_human:
                        # If the player picks up a coin
                        # This can be done with any one of the players lasers
                        if (any(l.laser.isvisible() and (
                            h.direction == 1 and c.relative_laser_position == -1 and l.laser.xcor() > c.collision_coordinate or
                            h.direction == 2 and c.relative_laser_position == 1 and l.laser.xcor() < c.collision_coordinate
                        ) for l in h.get_laser())) or h.get_player().distance(c.get_coin()) < 55 * scale_factor:
                            # Remove the coin
                            c.remove()
                            # Increase the amount of coins based on the type of coin picked up
                            if c.get_type() == "copper":
                                # Check if the blue power up has a multiplier activated for the coins value and use it
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.copper_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.copper_coin_value
                            elif c.get_type() == "silver":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.silver_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.silver_coin_value
                            elif c.get_type() == "gold":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.gold_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.gold_coin_value
                            elif c.get_type() == "platinum":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.platinum_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.platinum_coin_value
                            shop_config.save()
                            statistics.save()
                            coin.coins_on_screen_list.pop(hit_coin)
                            # play the coin pickup sound
                            if settings.coin_pickup_sound == 1:
                                sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                                sound.play()
                        hit_coin = hit_coin + 1
            else:
                gadget.attract_coins("Alien_Mode")

                hit_coin = 0
                for c in coin.coins_on_screen_list:
                    for h in human_player.current_human:
                        if h.player.isvisible() and h.death_animation == 0 and h.player.distance(c.coin) < c.COIN_DISTANCE:
                            # Remove the coin from the screen
                            c.remove()
                            # Increase the amount of coins the users has based on the type of coin picked up
                            if c.get_type() == "copper":
                                # For each coin, check if the blue power up has a multiplier on it
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.copper_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.copper_coin_value
                            elif c.get_type() == "silver":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.silver_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.silver_coin_value
                            elif c.get_type() == "gold":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.gold_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.gold_coin_value
                            elif c.get_type() == "platinum":
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.platinum_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                                    statistics.alien_coins_collected = statistics.alien_coins_collected + power_up_setup.platinum_coin_value
                            shop_config.save()
                            statistics.save()
                            coin.coins_on_screen_list.pop(hit_coin)
                            # play the coin pickup sound
                            if settings.coin_pickup_sound == 1:
                                sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                                sound.play()
                        hit_coin = hit_coin + 1

            # Alien Killer
            for h in human_player.current_human:
                current_small_alien_update_value_index = 0
                for sa in small_alien.small_aliens:
                    # If the player laser hits a small alien that is visible and not dying
                    if small_alien.small_aliens_kill_values[current_small_alien_update_value_index] == 0:
                        if sa.get_small_alien().isvisible():
                            # Check for all player lasers
                            laser_killed = 0
                            if sa.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.SMALL_ALIEN_Y_RANGE[0] < l.laser.ycor() < alien_collision.SMALL_ALIEN_Y_RANGE[1] and (
                                        (l.laser.xcor() > sa.get_small_alien().xcor() + alien_collision.SMALL_ALIEN_X_DISTANCE * sa.collision_point and h.laser_direction == 1 and sa.already_ahead == 0) or
                                        (l.laser.xcor() < sa.get_small_alien().xcor() + alien_collision.SMALL_ALIEN_X_DISTANCE * sa.collision_point and h.laser_direction == 2 and sa.already_behind == 0)
                                    ):
                                        small_alien.small_aliens_kill_values[current_small_alien_update_value_index] = small_alien.small_aliens_kill_values[current_small_alien_update_value_index] + 1

                                        # Increase the players score
                                        # When the blue power up is active, the score increases are doubled
                                        #   (This is universal)
                                        # The player gun type may also have a score multiplier applied
                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier

                                        # Update the stats if god mode is off
                                        if settings.god_mode == 0:
                                            statistics.small_aliens_killed = statistics.small_aliens_killed + 1
                                            statistics.save()

                                        # Increase the lasers pierce by 1 and try hiding the laser
                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_killed = 1
                                        break

                            if sa.thorns_initiated_damage == 1 and laser_killed == 0:
                                small_alien.small_aliens_kill_values[current_small_alien_update_value_index] =  small_alien.small_aliens_kill_values[current_small_alien_update_value_index] + 1

                                # Increase the players score
                                # When the blue power up is active, the score increases are doubled
                                #   (This is universal)
                                # The player gun type may also have a score multiplier applied
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier

                                # Update the stats if god mode is off
                                if settings.god_mode == 0:
                                    statistics.small_aliens_killed = statistics.small_aliens_killed + 1
                                    statistics.save()
                    elif small_alien.small_aliens_kill_values[current_small_alien_update_value_index] != 0:
                        # Kill the alien
                        sa.kill_alien(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        small_alien.small_aliens_kill_values[current_small_alien_update_value_index] = small_alien.small_aliens_kill_values[current_small_alien_update_value_index] + 1

                        # If the death animation has finished, reset the update value back to 0 to signal it
                        #   being finished
                        if sa.get_death_animation() == 0:
                            small_alien.small_aliens_kill_values[current_small_alien_update_value_index] = 0
                    current_small_alien_update_value_index = current_small_alien_update_value_index + 1

                current_medium_alien_update_value_index = 0
                current_medium_alien_hit_value_index = 0
                for ma in medium_alien.medium_aliens:
                    # If the player laser hits a medium alien that is visible and not dying and has health less
                    #   than or equal to damage
                    # Same procedure as before
                    if medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] == 0:
                        if ma.health <= alien_mode_setup.damage and ma.get_medium_alien().isvisible() and ma.hit_delay == 0:
                            laser_killed = 0
                            if ma.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.MEDIUM_ALIEN_Y_RANGE[0] < l.laser.ycor() < alien_collision.MEDIUM_ALIEN_Y_RANGE[1] and (
                                        (l.laser.xcor() > ma.get_medium_alien().xcor() + alien_collision.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point and h.laser_direction == 1 and ma.already_ahead == 0) or
                                        (l.laser.xcor() < ma.get_medium_alien().xcor() + alien_collision.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point and h.laser_direction == 2 and ma.already_behind == 0)
                                    ):
                                        medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] = medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] + 1

                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 2 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 2 * alien_mode_setup.regular_score_multiplier

                                        if settings.god_mode == 0:
                                            statistics.medium_aliens_killed = statistics.medium_aliens_killed + 1
                                            statistics.save()

                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_killed = 1
                                        break

                            if ma.thorns_initiated_damage == 1 and laser_killed == 0:
                                medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] = medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] + 1

                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 2 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 2 * alien_mode_setup.regular_score_multiplier

                                if settings.god_mode == 0:
                                    statistics.medium_aliens_killed = statistics.medium_aliens_killed + 1
                                    statistics.save()
                    elif medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] != 0:
                        ma.kill_alien(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] = medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] + 1

                        if ma.get_death_animation() == 0:
                            medium_alien.medium_aliens_kill_values[current_medium_alien_update_value_index] = 0
                    current_medium_alien_update_value_index = current_medium_alien_update_value_index + 1

                    # If the player laser hits a medium alien that is visible and not dying and has health
                    #   greater than damage
                    if medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] == 0:
                        if ma.get_medium_alien_health() > alien_mode_setup.damage and ma.get_medium_alien().isvisible():
                            laser_hit = 0
                            if ma.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.MEDIUM_ALIEN_Y_RANGE[0] < l.laser.ycor() < alien_collision.MEDIUM_ALIEN_Y_RANGE[1] and (
                                        (l.laser.xcor() > ma.get_medium_alien().xcor() + alien_collision.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point and h.laser_direction == 1 and ma.already_ahead == 0) or
                                        (l.laser.xcor() < ma.get_medium_alien().xcor() + alien_collision.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point and h.laser_direction == 2 and ma.already_behind == 0)
                                    ):
                                        medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] = medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] + 1

                                        # Increase the players score by the hit amount
                                        # When the blue power up is active, the score increases are doubled
                                        #   (This is universal)
                                        # The player gun type may also have a score multiplier applied
                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier

                                        # Increase the lasers pierce by 1 and try hiding the laser
                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                            laser_hit = 1
                                        break

                            if ma.thorns_initiated_damage == 1 and laser_hit == 0:
                                medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] = medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] + 1

                                # Increase the players score by the hit amount
                                # When the blue power up is active, the score increases are doubled
                                #   (This is universal)
                                # The player gun type may also have a score multiplier applied
                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier
                    elif medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] != 0:
                        # Hit the alien
                        ma.hit_alien(settings.enemy_hit_sound)
                        medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] = medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] + 1

                        # If the hit delay is finished, reset the hit value back to 0 to signal the hit delay ending
                        if ma.get_hit_delay() == 0:
                            medium_alien.medium_aliens_hit_values[current_medium_alien_hit_value_index] = 0
                    current_medium_alien_hit_value_index = current_medium_alien_hit_value_index + 1

                current_large_alien_update_value_index = 0
                current_large_alien_hit_value_index = 0
                for la in large_alien.large_aliens:
                    # If the player laser hits a large alien that is visible and not dying and has health less
                    #   than or equal to damage
                    if large_alien.large_aliens_kill_values[current_large_alien_update_value_index] == 0:
                        if la.health <= alien_mode_setup.damage and la.get_large_alien().isvisible() and la.hit_delay == 0:
                            laser_killed = 0
                            if la.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.LARGE_ALIEN_Y_RANGE[0] < l.laser.ycor() < alien_collision.LARGE_ALIEN_Y_RANGE[1] and (
                                        (l.laser.xcor() > la.get_large_alien().xcor() + alien_collision.LARGE_ALIEN_X_DISTANCE * la.collision_point and h.laser_direction == 1 and la.already_ahead == 0) or
                                        (l.laser.xcor() < la.get_large_alien().xcor() + alien_collision.LARGE_ALIEN_X_DISTANCE * la.collision_point and h.laser_direction == 2 and la.already_behind == 0)
                                    ):
                                        large_alien.large_aliens_kill_values[current_large_alien_update_value_index] = large_alien.large_aliens_kill_values[current_large_alien_update_value_index] + 1

                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 4 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 4 * alien_mode_setup.regular_score_multiplier

                                        if settings.god_mode == 0:
                                            statistics.big_aliens_killed = statistics.big_aliens_killed + 1
                                            statistics.save()

                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_killed = 1
                                        break

                            if la.thorns_initiated_damage == 1 and laser_killed == 0:
                                large_alien.large_aliens_kill_values[current_large_alien_update_value_index] = large_alien.large_aliens_kill_values[current_large_alien_update_value_index] + 1

                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 4 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 4 * alien_mode_setup.regular_score_multiplier

                                if settings.god_mode == 0:
                                    statistics.big_aliens_killed = statistics.big_aliens_killed + 1
                                    statistics.save()
                    elif large_alien.large_aliens_kill_values[current_large_alien_update_value_index] != 0:
                        la.kill_alien(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        large_alien.large_aliens_kill_values[current_large_alien_update_value_index] = large_alien.large_aliens_kill_values[current_large_alien_update_value_index] + 1

                        if la.get_death_animation() == 0:
                            large_alien.large_aliens_kill_values[current_large_alien_update_value_index] = 0
                    current_large_alien_update_value_index = current_large_alien_update_value_index + 1

                    # If the player laser hits a large alien that is visible and not dying and has health
                    #   greater than damage
                    # Same procedure as before
                    if large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] == 0:
                        if la.get_large_alien_health() > alien_mode_setup.damage and la.get_large_alien().isvisible():
                            laser_hit = 0
                            if la.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.LARGE_ALIEN_Y_RANGE[0] < l.laser.ycor() < alien_collision.LARGE_ALIEN_Y_RANGE[1] and (
                                        (l.laser.xcor() > la.get_large_alien().xcor() + alien_collision.LARGE_ALIEN_X_DISTANCE * la.collision_point and h.laser_direction == 1 and la.already_ahead == 0) or
                                        (l.laser.xcor() < la.get_large_alien().xcor() + alien_collision.LARGE_ALIEN_X_DISTANCE * la.collision_point and h.laser_direction == 2 and la.already_behind == 0)
                                    ):
                                        large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] = large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] + 1

                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier

                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_hit = 1
                                        break

                            if la.thorns_initiated_damage == 1 and laser_hit == 0:
                                large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] = large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] + 1

                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier
                    elif large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] != 0:
                        la.hit_alien(settings.enemy_hit_sound)
                        large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] = large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] + 1

                        if la.get_hit_delay() == 0:
                            large_alien.large_aliens_hit_values[current_large_alien_hit_value_index] = 0
                    current_large_alien_hit_value_index = current_large_alien_hit_value_index + 1

                for u in ufo.ufos:
                    # If the player laser hits the ufo that is visible and not dying and has health less than
                    #   or equal to damage
                    if ufo.ufo_kill_value == 0:
                        if u.get_ufo_health() <= alien_mode_setup.damage and u.get_ufo().isvisible() and u.hit_delay == 0:
                            laser_killed = 0
                            if u.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.UFO_Y_RANGE[0] < l.laser.ycor() < alien_collision.UFO_Y_RANGE[1] and (
                                        (l.laser.xcor() > u.get_ufo().xcor() + alien_collision.UFO_X_DISTANCE * u.collision_point and h.laser_direction == 1 and u.already_ahead == 0) or
                                        (l.laser.xcor() < u.get_ufo().xcor() + alien_collision.UFO_X_DISTANCE * u.collision_point and h.laser_direction == 2 and u.already_behind == 0)
                                    ):
                                        ufo.ufo_kill_value = ufo.ufo_kill_value + 1

                                        if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                            statistics.score = statistics.score + 50 * alien_mode_setup.blue_power_up_score_multiplier
                                        else:
                                            statistics.score = statistics.score + 50 * alien_mode_setup.regular_score_multiplier

                                        if settings.god_mode == 0:
                                            statistics.ufos_killed = statistics.ufos_killed + 1
                                            statistics.save()

                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_killed = 1
                                        break

                            if u.thorns_initiated_damage == 1 and laser_killed == 0:
                                ufo.ufo_kill_value = ufo.ufo_kill_value + 1

                                if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                    statistics.score = statistics.score + 50 * alien_mode_setup.blue_power_up_score_multiplier
                                else:
                                    statistics.score = statistics.score + 50 * alien_mode_setup.regular_score_multiplier

                                if settings.god_mode == 0:
                                    statistics.ufos_killed = statistics.ufos_killed + 1
                                    statistics.save()
                    elif ufo.ufo_kill_value != 0:
                        u.kill_ufo(settings.enemy_death_sound, coin.coins_on_screen_list, coin.all_coins_list)
                        ufo.ufo_kill_value = ufo.ufo_kill_value + 1

                        if u.get_death_animation() == 0:
                            ufo.ufo_kill_value = 0

                    # If the player laser hits a ufo that is visible and not dying and has health
                    #   greater than damage
                    if ufo.ufo_hit_value == 0:
                        if u.got_hit == 0 and u.get_ufo_health() > alien_mode_setup.damage and u.get_ufo().isvisible():
                            laser_hit = 0
                            if u.got_hit == 0:
                                for l in h.get_laser():
                                    if l.laser_update < alien_mode_setup.piercing and \
                                        alien_collision.UFO_Y_RANGE[0] < l.laser.ycor() < alien_collision.UFO_Y_RANGE[1] and (
                                        (l.laser.xcor() > u.get_ufo().xcor() + alien_collision.UFO_X_DISTANCE * u.collision_point and h.laser_direction == 1 and u.already_ahead == 0) or
                                        (l.laser.xcor() < u.get_ufo().xcor() + alien_collision.UFO_X_DISTANCE * u.collision_point and h.laser_direction == 2 and u.already_behind == 0)
                                    ):
                                        ufo.ufo_hit_value = ufo.ufo_hit_value + 1

                                        if u.get_ufo_health() == 2 or u.get_ufo_health() == 1:
                                            if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                                statistics.score = statistics.score + 3 * alien_mode_setup.blue_power_up_score_multiplier
                                            else:
                                                statistics.score = statistics.score + 3 * alien_mode_setup.regular_score_multiplier
                                        elif u.get_ufo_health() == 5 or u.get_ufo_health() == 4 or u.get_ufo_health() == 3:
                                            if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                                statistics.score = statistics.score + 2 * alien_mode_setup.blue_power_up_score_multiplier
                                            else:
                                                statistics.score = statistics.score + 2 * alien_mode_setup.regular_score_multiplier
                                        else:
                                            if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                                statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                            else:
                                                statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier

                                        l.laser.hideturtle()
                                        if extra_power_up_indicator.extra_power_up_indicator_turtle[0].get_power_up_active() == 0:
                                            l.laser_update = l.laser_update + 1
                                        laser_hit = 1
                                        break

                            if u.thorns_initiated_damage == 1 and laser_hit == 0:
                                ufo.ufo_hit_value = ufo.ufo_hit_value + 1

                                if u.get_ufo_health() == 2 or u.get_ufo_health() == 1:
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 3 * alien_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 3 * alien_mode_setup.regular_score_multiplier
                                elif u.get_ufo_health() == 5 or u.get_ufo_health() == 4 or u.get_ufo_health() == 3:
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 2 * alien_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 2 * alien_mode_setup.regular_score_multiplier
                                else:
                                    if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                                        statistics.score = statistics.score + 1 * alien_mode_setup.blue_power_up_score_multiplier
                                    else:
                                        statistics.score = statistics.score + 1 * alien_mode_setup.regular_score_multiplier
                    elif ufo.ufo_hit_value != 0:
                        u.hit_ufo(settings.enemy_hit_sound)
                        ufo.ufo_hit_value = ufo.ufo_hit_value + 1

                        if u.get_hit_delay() == 0:
                            ufo.ufo_hit_value = 0

            # Player Killer
            for h in human_player.current_human:
                # If the death animation has already started
                if human_player.human_update_value != 0:
                    # Keep going with the players death animation
                    h.kill_player(settings.player_death_sound)
                    human_player.human_update_value = human_player.human_update_value + 1
                    if h.get_death_iterator() == 2:
                        # Update the stats if god mode is off
                        if settings.god_mode == 0:
                            statistics.alien_deaths = statistics.alien_deaths + 1
                            statistics.damage_taken = statistics.damage_taken + 1
                            statistics.save()
                        # Set the store to 0 and reset the game
                        statistics.score = 0
                    # Check if the death animation has finished
                    if h.get_death_iterator() == 0:
                        human_player.human_update_value = 0
                # If the death animation is not ongoing
                else:
                    # For every alien, check if the alien got close enough to hit the player
                    for sa in small_alien.small_aliens:
                        if sa.get_small_alien().distance(h.get_player()) < 70 * scale_factor:
                            # The players health also has to be 1
                            if h.health == 1 and h.hit_delay == 0 and sa.get_small_alien().xcor() - 12.5 * scale_factor_X < h.get_player().xcor() < sa.get_small_alien().xcor() + 12.5 * scale_factor_X and human_player.human_update_value == 0 and sa.get_death_animation() == 0 and settings.god_mode == 0:
                                # Then, kill the player
                                h.kill_player(settings.player_death_sound)
                                human_player.human_update_value = human_player.human_update_value + 1
                                if shop_config.thorns_enabled:
                                    sa.thorns_initiated_damage = 1

                    for ma in medium_alien.medium_aliens:
                        if ma.get_medium_alien().distance(h.get_player()) < 100 * scale_factor:
                            if h.health == 1 and h.hit_delay == 0 and ma.get_medium_alien().xcor() - 15 * scale_factor_X < h.get_player().xcor() < ma.get_medium_alien().xcor() + 15 * scale_factor_X and human_player.human_update_value == 0 and ma.get_death_animation() == 0 and settings.god_mode == 0:
                                h.kill_player(settings.player_death_sound)
                                human_player.human_update_value = human_player.human_update_value + 1
                                if shop_config.thorns_enabled:
                                    ma.thorns_initiated_damage = 1

                    for la in large_alien.large_aliens:
                        if la.get_large_alien().distance(h.get_player()) < 160 * scale_factor:
                            if h.health == 1 and h.hit_delay == 0 and la.get_large_alien().xcor() - 18 * scale_factor_X < h.get_player().xcor() < la.get_large_alien().xcor() + 18 * scale_factor_X and human_player.human_update_value == 0 and la.get_death_animation() == 0 and settings.god_mode == 0:
                                h.kill_player(settings.player_death_sound)
                                human_player.human_update_value = human_player.human_update_value + 1
                                if shop_config.thorns_enabled:
                                    la.thorns_initiated_damage = 1

                    for u in ufo.ufos:
                        if u.get_ufo().distance(h.get_player()) < 53 * scale_factor:
                            if h.health == 1 and h.hit_delay == 0 and u.get_ufo().xcor() - 18 * scale_factor_X < h.get_player().xcor() < u.get_ufo().xcor() + 18 * scale_factor_X and human_player.human_update_value == 0 and u.get_ufo().isvisible() and u.get_death_animation() == 0 and settings.god_mode == 0:
                                h.kill_player(settings.player_death_sound)
                                human_player.human_update_value = human_player.human_update_value + 1
                                if shop_config.thorns_enabled:
                                    u.thorns_initiated_damage = 1

                        if u.get_ufo_laser().distance(h.get_player()) < 25 * scale_factor:
                            if h.health == 1 and h.hit_delay == 0 and u.get_ufo_laser().isvisible() and settings.god_mode == 0 and human_player.human_update_value == 0:
                                h.kill_player(settings.player_death_sound)
                                human_player.human_update_value = human_player.human_update_value + 1

                # If the player has more than 1 health, only deal 1 health owrth of damage
                # If the hit delay is ongoing
                if human_player.human_hit_value != 0:
                    # keep it going
                    h.hit_player(settings.player_hit_sound)
                    human_player.human_hit_value = human_player.human_hit_value + 1
                    # Update the stats
                    if h.get_hit_delay() == 2:
                        statistics.damage_taken = statistics.damage_taken + 1
                        statistics.save()
                    if h.get_hit_delay() == 0:
                        human_player.human_hit_value = 0
                # If there is no hit delay
                else:
                    # For every alien, check if the alien got close enough to hit the player
                    for sa in small_alien.small_aliens:
                        if sa.get_small_alien().distance(h.get_player()) < 70 * scale_factor:
                            # If the players health is greater than 1
                            if h.get_health() > 1 and sa.get_small_alien().xcor() - 12.5 * scale_factor_X < h.get_player().xcor() < sa.get_small_alien().xcor() + 12.5 * scale_factor_X and sa.get_death_animation() == 0 and h.get_hit_delay() == 0 and settings.god_mode == 0:
                                # Hit the player
                                h.hit_player(settings.player_hit_sound)
                                human_player.human_hit_value = human_player.human_hit_value + 1
                                if shop_config.thorns_enabled:
                                    sa.thorns_initiated_damage = 1

                    for ma in medium_alien.medium_aliens:
                        if ma.get_medium_alien().distance(h.get_player()) < 100 * scale_factor:
                            if h.get_health() > 1 and ma.get_medium_alien().xcor() - 15 * scale_factor_X < h.get_player().xcor() < ma.get_medium_alien().xcor() + 15 * scale_factor_X and ma.get_death_animation() == 0 and h.get_hit_delay() == 0 and settings.god_mode == 0:
                                h.hit_player(settings.player_hit_sound)
                                human_player.human_hit_value = human_player.human_hit_value + 1
                                if shop_config.thorns_enabled:
                                    ma.thorns_initiated_damage = 1

                    for la in large_alien.large_aliens:
                        if la.get_large_alien().distance(h.get_player()) < 160 * scale_factor:
                            if h.get_health() > 1 and la.get_large_alien().xcor() - 18 * scale_factor_X < h.get_player().xcor() < la.get_large_alien().xcor() + 18 * scale_factor_X and la.get_death_animation() == 0 and h.get_hit_delay() == 0 and settings.god_mode == 0:
                                h.hit_player(settings.player_hit_sound)
                                human_player.human_hit_value = human_player.human_hit_value + 1
                                if shop_config.thorns_enabled:
                                    la.thorns_initiated_damage = 1

                    for u in ufo.ufos:
                        # For the UFO, the player can get hurt by both touching the UFO and getting hit
                        #   by the UFOs laser
                        if u.get_ufo().distance(h.get_player()) < 53 * scale_factor:
                            if h.get_health() > 1 and u.get_ufo().xcor() - 18 * scale_factor_X < h.get_player().xcor() < u.get_ufo().xcor() + 18 * scale_factor_X and u.get_ufo().isvisible() and u.get_death_animation() == 0 and h.get_hit_delay() == 0 and settings.god_mode == 0:
                                h.hit_player(settings.player_hit_sound)
                                human_player.human_hit_value = human_player.human_hit_value + 1
                                if shop_config.thorns_enabled:
                                    u.thorns_initiated_damage = 1

                        if u.get_ufo_laser().distance(h.get_player()) < 25 * scale_factor:
                            if h.get_health() > 1 and u.get_ufo_laser().isvisible() and settings.god_mode == 0:
                                h.hit_player(settings.player_hit_sound)
                                human_player.human_hit_value = human_player.human_hit_value + 1
        # If Alien Mode is toggled off
        else:
            # Remove all the Alien Mode exclusive sprites from the screen
            for s in sun.sun_turtle:
                s.remove()
            sun.sun_index = 0
            for e in earth.earth_turtle:
                e.remove()
            earth.earth_index = 0
            for bo in background_objects.background_objects_turtle:
                bo.remove()
            background_objects.background_objects_index = 0
            for h in human_player.current_human:
                h.remove()
            human_player.current_human.clear()
            human_player.current_human_index = 0
            human_player.human_update_value = 0
            human_player.human_hit_value = 0
            human_player.laser_update = 0
            for sa in small_alien.small_aliens:
                sa.remove()
            small_alien.small_aliens.clear()
            small_alien.small_alien_index = 0
            small_alien.small_aliens_kill_values.clear()
            for ma in medium_alien.medium_aliens:
                ma.remove()
            medium_alien.medium_aliens.clear()
            medium_alien.medium_alien_index = 0
            medium_alien.medium_aliens_kill_values.clear()
            medium_alien.medium_aliens_hit_values.clear()
            for la in large_alien.large_aliens:
                la.remove()
            large_alien.large_aliens.clear()
            large_alien.large_alien_index = 0
            large_alien.large_aliens_kill_values.clear()
            large_alien.large_aliens_hit_values.clear()
            for u in ufo.ufos:
                u.remove()
            ufo.ufos.clear()
            ufo.ufo_index = 0
            ufo.ufo_kill_value = 0
            ufo.ufo_hit_value = 0

        """
            Code below is for when the Shop is entered
        """

        if screen.mode == "Shop":
            # Create the side panel
            if panel.panel_index == 0:
                panel.spawn_panel(screen.mode)

            # Create Main Menu button and the different Tabs
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)
                for i in range(4):
                    button.spawn_button("Tab", i + 1)

            # Check if the main menu button has been clicked or not
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(screen.launch_title_mode)

            # Check to see if the tabs have been click or not
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Tab":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.display_machine_mode_page)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.display_alien_mode_page)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.display_power_up_page)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.display_gadgets_page)

            # Spawn all the necessary standalone text
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, -75 * scale_factor_X, 240 * scale_factor_Y, "red")
                textbox.spawn_text_box(2, -588 * scale_factor_X, 281 * scale_factor_Y, "yellow")
                textbox.spawn_text_box(3, -500 * scale_factor_X, 190 * scale_factor_Y, "#ff5349")

            # Spawn the tab selector if it does not exist
            if selector.current_selector_index == 0:
                selector.spawn_selector("Tab")

            # If the current page is "Machine_Mode"
            if screen.page == "Machine_Mode":
                # Create 5 shop slots
                if button.current_button_index == 5:
                    for i in range(5):
                        button.spawn_button("Shop_Slot", i + 1, screen.page)

                # Create 0-4 price labels if needed (They are only needed if items are locked)
                if textbox.current_text_index == 3 and button.buy_button_pressed == 0:
                    counter = 4
                    for bu in button.buttons_on_screen_list:
                        if bu.get_type() == "Shop_Slot":
                            if bu.get_indicator_toggled() == 1:
                                textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                refresh_variables.refresh_text = 1
                            counter = counter + 1

                # Spawn the slot selector if it does not exist
                if selector.current_selector_index == 1:
                    selector.spawn_selector("Slot")

                # Check if the tab selector must be moved
                if refresh_variables.move_tab_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Tab":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Tab" and bu.get_id() == 1:
                                    s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                    refresh_variables.move_tab_selector = 0

                # Check if the slot selector must be moved
                if refresh_variables.move_slot_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Slot":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Shop_Slot" and bu.get_id() == shop_config.machine_slot_selected:
                                    s.new_select(bu.get_button_frame().xcor(), bu.get_button_frame().ycor())
                                    refresh_variables.move_slot_selector = 0

                # Check if the slots are locked or not
                for bu in button.buttons_on_screen_list:
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

                # Check if the slots have been clicked or not
                for bu in button.buttons_on_screen_list:
                    button_color, button_type, id = bu.click_button()
                    if bu.get_type() == "Shop_Slot":
                        if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_1_select)
                        elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_2_select)
                        elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_3_select)
                        elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_4_select)
                        elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_5_select)
                    elif bu.get_type() == "Buy":
                        if button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.execute_buy_button)
            # If the page is "Alien_Mode"
            elif screen.page == "Alien_Mode":
                # Create 5 shop slots
                if button.current_button_index == 5:
                    for i in range(5):
                        button.spawn_button("Shop_Slot", i + 1, screen.page)

                # Create 0-4 price labels if needed (They are only needed if items are locked)
                if textbox.current_text_index == 3 and button.buy_button_pressed == 0:
                    counter = 4
                    for bu in button.buttons_on_screen_list:
                        if bu.get_type() == "Shop_Slot":
                            if bu.get_indicator_toggled() == 1:
                                textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                refresh_variables.refresh_text = 1
                            counter = counter + 1

                # Spawn a slot selector if one does not exist already
                if selector.current_selector_index == 1:
                    selector.spawn_selector("Slot")

                # Check to see if the tab selector needs to be moved
                if refresh_variables.move_tab_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Tab":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Tab" and bu.get_id() == 2:
                                    s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                    refresh_variables.move_tab_selector = 0

                # Check to see if the slot selector needs to be moved
                if refresh_variables.move_slot_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Slot":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Shop_Slot" and bu.get_id() == shop_config.alien_slot_selected:
                                    s.new_select(bu.get_button_frame().xcor(), bu.get_button_frame().ycor())
                                    refresh_variables.move_slot_selector = 0

                # Check to see if each slot is locked or not
                for bu in button.buttons_on_screen_list:
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

                # Check to see if each slot has been clicked or not
                for bu in button.buttons_on_screen_list:
                    button_color, button_type, id = bu.click_button()
                    if bu.get_type() == "Shop_Slot":
                        if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_1_select)
                        elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_2_select)
                        elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_3_select)
                        elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_4_select)
                        elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_5_select)
                    elif bu.get_type() == "Buy":
                        if button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.execute_buy_button)
            # If the page is "Power_Ups"
            elif screen.page == "Power_Ups":
                # Spawn 4 power up slots
                if button.current_button_index == 5:
                    for i in range(4):
                        button.spawn_button("Power_Up_Slot", i + 1)

                # Check to see if a price label is still needed and if the power ups are on their max level or not
                if textbox.current_text_index == 3 and button.buy_button_pressed == 0:
                    counter = 4
                    for bu in button.buttons_on_screen_list:
                        if bu.get_type() == "Power_Up_Slot":
                            if bu.get_id() == 1:
                                if shop_config.yellow_power_up_level != 5 and shop_config.yellow_power_up_level != 0:
                                    textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                    price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                    refresh_variables.refresh_text = 1
                            elif bu.get_id() == 2:
                                if shop_config.blue_power_up_level != 5 and shop_config.blue_power_up_level != 0:
                                    textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                    price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                    refresh_variables.refresh_text = 1
                            elif bu.get_id() == 3:
                                if shop_config.green_power_up_level != 5 and shop_config.green_power_up_level != 0:
                                    textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                    price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                    refresh_variables.refresh_text = 1
                            elif bu.get_id() == 4:
                                if shop_config.red_power_up_level != 5 and shop_config.red_power_up_level != 0:
                                    textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                    price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                    refresh_variables.refresh_text = 1
                            counter = counter + 1

                # Check to see if the tab selector needs to be moved
                if refresh_variables.move_tab_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Tab":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Tab" and bu.get_id() == 3:
                                    s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                    refresh_variables.move_tab_selector = 0

                # Check what level each power up is at
                for bu in button.buttons_on_screen_list:
                    if bu.get_type() == "Power_Up_Slot":
                        if bu.get_id() == 1:
                            bu.toggle_indicator(shop_config.yellow_power_up_level)
                        elif bu.get_id() == 2:
                            bu.toggle_indicator(shop_config.blue_power_up_level)
                        elif bu.get_id() == 3:
                            bu.toggle_indicator(shop_config.green_power_up_level)
                        elif bu.get_id() == 4:
                            bu.toggle_indicator(shop_config.red_power_up_level)
                        bu.set_indicator_location()

                # Check if the slots have been clicked on or not
                for bu in button.buttons_on_screen_list:
                    button_color, button_type, id = bu.click_button()
                    if bu.get_type() == "Power_Up_Slot":
                        if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_1_select)
                        elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_2_select)
                        elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_3_select)
                        elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_4_select)
                    elif bu.get_type() == "Buy":
                        if button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.execute_buy_button)
            elif screen.page == "Gadgets":
                # Spawn 4 gadget slots
                if button.current_button_index == 5:
                    for i in range(4):
                        button.spawn_button("Gadget_Slot", i + 1)

                # Check to see if a price label is still needed and if the power ups are on their max level or not
                if textbox.current_text_index == 3 and button.buy_button_pressed == 0:
                    counter = 4
                    for bu in button.buttons_on_screen_list:
                        if bu.get_type() == "Gadget_Slot":
                            if bu.get_indicator_toggled() == 1:
                                textbox.spawn_text_box(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 78 * scale_factor_Y, "yellow")
                                price_label.spawn_price_label(counter, bu.get_button_frame().xcor() - 50 * scale_factor_X, bu.get_button_frame().ycor() - 60 * scale_factor_Y)
                                refresh_variables.refresh_text = 1
                            counter = counter + 1

                # Check to see if each gadget is enabled or not
                for bu in button.buttons_on_screen_list:
                    if bu.get_type() == "Gadget_Slot":
                        if bu.get_id() == 1:
                            bu.toggle_indicator(shop_config.coin_magnet_unlocked)
                        elif bu.get_id() == 2:
                            bu.toggle_indicator(shop_config.shield_unlocked)
                        elif bu.get_id() == 3:
                            bu.toggle_indicator(shop_config.thorns_unlocked)
                        elif bu.get_id() == 4:
                            bu.toggle_indicator(shop_config.hearts_unlocked)
                        bu.set_indicator_location()

                # Check to see if the tab selector needs to be moved
                if refresh_variables.move_tab_selector == 1:
                    for s in selector.selectors_on_screen_list:
                        if s.get_type() == "Tab":
                            for bu in button.buttons_on_screen_list:
                                if bu.get_type() == "Tab" and bu.get_id() == 4:
                                    s.new_select(bu.get_button_frame().xcor() - 1 * scale_factor_X, bu.get_button_frame().ycor())
                                    refresh_variables.move_tab_selector = 0

                # Check if the slots have been clicked on or not
                for bu in button.buttons_on_screen_list:
                    button_color, button_type, id = bu.click_button()
                    if bu.get_type() == "Gadget_Slot":
                        if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_1_select)
                        elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_2_select)
                        elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_3_select)
                        elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.slot_4_select)
                    elif bu.get_type() == "Buy":
                        if button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.execute_buy_button)
                    elif bu.get_type() == "Enable":
                        if button_color == "yellow" and bu.get_button_frame().isvisible():
                            wn.onscreenclick(shop.execute_enable_button)

            # Spawn the coin indicator
            if coin_indicator.coin_indicator_index == 0:
                coin_indicator.spawn_coin_indicator()

            # Move the title text back and fourth across the screen as needed
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)
                    break

        """
             Code Below is for when Statistics Mode is turned on.
        """

        if screen.mode == "Stats":
            # Create Main Menu button
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)

            # Check if the button has been clicked
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Game" and button_color == "yellow" and bu.get_button_frame().isvisible():
                    wn.onscreenclick(screen.launch_title_mode)

            # Create the statistics text
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
                textbox.spawn_text_box(2, -320 * scale_factor_X, 140 * scale_factor_Y, "#ff5349")
                textbox.spawn_text_box(3, 320 * scale_factor_X, 140 * scale_factor_Y, "#ff5349")
                for i in range(10):
                    textbox.spawn_text_box(i + 4, -320 * scale_factor_X, (90 - (i * 40)) * scale_factor_Y, "white")
                for i in range(11):
                    textbox.spawn_text_box(13 + i + 1, 320 * scale_factor_X, (90 - (i * 40)) * scale_factor_Y, "white")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(25, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

            # Move the title text back and fourth across the screen as needed
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)
                    break

        """
            Code Below is for when Settings Mode is turned on.
        """

        if screen.mode == "Settings":
            # Create all the screen buttons, including the toggle buttons
            if button.current_button_index == 0:
                for i in range(2):
                    button.spawn_button("Regular_Settings_And_Controls", i + 1)
                for i in range(12):
                    button.spawn_button("Settings_Toggle", i + 1)

            # Check if each of the buttons has been clicked
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Regular_Settings_And_Controls":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_title_mode)
                    elif id == 2 and (button_color == "yellow" or button.clickable == 1) and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_controls_mode)
                        button.clickable = 0
                elif button_type == "Settings_Toggle":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_button_sound)
                    elif id == 2 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_player_shooting_sound)
                    elif id == 3 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_enemy_shooting_sound)
                    elif id == 4 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_player_death_sound)
                    elif id == 5 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_enemy_death_sound)
                    elif id == 6 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_player_hit_sound)
                    elif id == 7 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_enemy_hit_sound)
                    elif id == 8 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_power_up_pickup_sound)
                    elif id == 9 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_power_up_spawn_sound)
                    elif id == 10 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_coin_pick_up_sound)
                    elif id == 11 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_fullscreen)
                    elif id == 12 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(settings_toggle.toggle_vsync)

            # Create all additional text boxes
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(2, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

            # Move the title text left and right across the screen
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)
                    break

        """
            Code Below is for when Controls Mode is turned on.
        """

        if screen.mode == "Controls":
            # Create all the buttons for the screen, including the toggle buttons.
            if button.current_button_index == 0:
                button.spawn_button("Regular_Settings_And_Controls", 1)
                button.spawn_button("Regular_Settings_And_Controls", 3)
                for i in range(4):
                    button.spawn_button("Controls_Toggle", i + 1)

            # Check if any of the buttons have been clicked
            for bu in button.buttons_on_screen_list:
                button_color, button_type, id = bu.click_button()
                if button_type == "Regular_Settings_And_Controls":
                    if id == 1 and button_color == "yellow" and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_title_mode)
                    elif id == 3 and (button_color == "yellow" or button.clickable == 2) and bu.get_button_frame().isvisible():
                        wn.onscreenclick(screen.launch_settings_mode)
                        button.clickable = 0
                elif button_type == "Controls_Toggle":
                    if id == 1 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                        wn.onscreenclick(controls.change_go_right_key)
                    elif id == 2 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                        wn.onscreenclick(controls.change_go_left_key)
                    elif id == 3 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                        wn.onscreenclick(controls.change_shoot_key)
                    elif id == 4 and (button_color == "yellow" or button_color == "orange") and bu.get_button_frame().isvisible():
                        wn.onscreenclick(controls.change_jump_key)

            # Create any additional text boxes
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 0, 240 * scale_factor_Y, "red")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(2, 481 * scale_factor_X, 320 * scale_factor_Y, "white")

            # Move the title text left and right across the screen
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)
                    break

            # Control Setting Conflict Updates
            # This checks if there are any conflicts with the current controls.
            # This is done here in case any new updates to the controls cause conflicts.
            if controls_toggle.go_right_key != controls_toggle.go_left_key and controls_toggle.go_right_key != controls_toggle.shoot_key and controls_toggle.go_right_key != controls_toggle.jump_key:
                controls.go_right_key_alert = 0
            else:
                controls.go_right_key_alert = 1

            if controls_toggle.go_left_key != controls_toggle.go_right_key and controls_toggle.go_left_key != controls_toggle.shoot_key and controls_toggle.go_left_key != controls_toggle.jump_key:
                controls.go_left_key_alert = 0
            else:
                controls.go_left_key_alert = 1

            if controls_toggle.shoot_key != controls_toggle.go_left_key and controls_toggle.shoot_key != controls_toggle.go_right_key and controls_toggle.shoot_key != controls_toggle.jump_key:
                controls.shoot_key_alert = 0
            else:
                controls.shoot_key_alert = 1

            if controls_toggle.jump_key != controls_toggle.go_left_key and controls_toggle.jump_key != controls_toggle.shoot_key and controls_toggle.jump_key != controls_toggle.go_right_key:
                controls.jump_key_alert = 0
            else:
                controls.jump_key_alert = 1


if __name__ == "__main__":
    # Make sure the computer does not enter sleep mode while the game is running
    with MonitorSleepController():
        main()
