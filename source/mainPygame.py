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
# This is game version beta 1.2.1 released on 08/12/24

"""
    File: main.py
    Author: Christian Marinkovich
    Date: 2024-08-12
    Description:
    This file is the main file for Laser Fighter.
    The main file contains the main function, which contains the game loop.
    The game loop consists of three parts: The screen updater, the game quitter, and the event handler.
"""

import pygame
import time
import random
import gc
from setup.WindowSetupPygame import GameWindow
from setup.ModeSetupMasterPygame import machine_mode_setup
from setup.ModeSetupMasterPygame import power_up_setup
from setup.ConfigurationSetupPygame import refresh_variables
from setup.ConfigurationSetupPygame import settings
from setup.ConfigurationSetupPygame import statistics
from setup.ConfigurationSetupPygame import shop_config
from utils.UpdateTextPygame import TextRefresh
from components.spawn.SpawnCoinPygame import SpawnCoin
from components.spawn.SpawnMachinePygame import SpawnBlueMachine
from components.spawn.SpawnPlayerPygame import SpawnMachinePlayer
from components.spawn.SpawnPowerUpPygame import SpawnPowerUp
from components.spawn.SpawnPowerUpPygame import SpawnYellowPowerUpIndicator
from components.spawn.SpawnPowerUpPygame import SpawnBluePowerUpIndicator
from components.spawn.SpawnPowerUpPygame import SpawnExtraPowerUpIndicator
from components.spawn.SpawnCoinPygame import SpawnCoinIndicator
from components.spawn.SpawnTextboxPygame import SpawnTextbox
from components.spawn.SpawnButtonPygame import SpawnButton
from physics.MachineCollisionPygame import MachineCollision
from utils.MovementManagerPygame import Movement
from utils.ScreenManagerPygame import ScreenUpdate


def main():
    window = GameWindow()
    coin = SpawnCoin()
    blue_machine = SpawnBlueMachine(window.scale_factor_X, window.scale_factor_Y)
    power_up = SpawnPowerUp(window.scale_factor_X, window.scale_factor_Y)
    machine_player = SpawnMachinePlayer(window.scale_factor_X, window.scale_factor_Y)

    yellow_power_up_indicator = SpawnYellowPowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    blue_power_up_indicator = SpawnBluePowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    extra_power_up_indicator = SpawnExtraPowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    coin_indicator = SpawnCoinIndicator(window.scale_factor_X, window.scale_factor_Y)

    button = SpawnButton(window.scale_factor, window.scale_factor_X, window.scale_factor_Y)
    textbox = SpawnTextbox(window.scale_factor, window.scale_factor_X)

    screen = ScreenUpdate(window, button, settings, shop_config, refresh_variables,
                          power_up_setup, machine_mode_setup,
                          window.scale_factor_X, window.scale_factor_Y)

    text_refresh = TextRefresh(screen, button, textbox, yellow_power_up_indicator, blue_power_up_indicator,
                               extra_power_up_indicator, settings,
                               statistics, shop_config, refresh_variables)

    machine_collision = MachineCollision(machine_player, blue_machine, window.scale_factor_X, window.scale_factor_Y)
    movement = Movement(screen, machine_player, yellow_power_up_indicator, settings, statistics, window.scale_factor_Y)

    MOVE_REPEAT_DELAY = 0.05
    last_move_time = 0

    start_ticks = pygame.time.get_ticks()

    # The main game loop:
    running = True
    while running:
        window.CLOCK.tick(window.TARGET_FPS)

        # EVENT HANDLER
        mouse_pos = pygame.mouse.get_pos()

        for bu in button.buttons_on_screen_list:
            if bu.rect.collidepoint(mouse_pos):
                bu.toggle_highlighted()
            else:
                bu.toggle_default()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Shoot
                    movement.shoot(machine_collision)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for bu in button.buttons_on_screen_list:
                        if bu.rect.collidepoint(mouse_pos):
                            if bu.type == "Title":
                                if bu.id == 1:
                                    screen.launch_machine_mode()
                                elif bu.id == 3:
                                    running = False
                            elif bu.type == "Title_Small":
                                if bu.id == 1:
                                    screen.launch_settings_mode()
                                elif bu.id == 2:
                                    screen.launch_stats_mode()
                            elif bu.type == "Game":
                                if bu.id == 1:
                                    screen.launch_title_mode()
                            elif bu.type == "Regular_Settings_And_Controls":
                                if bu.id == 1:
                                    screen.launch_title_mode()

        current_time = time.time()

        keys = pygame.key.get_pressed()
        if current_time - last_move_time >= MOVE_REPEAT_DELAY:
            if keys[pygame.K_a]:
                movement.go_left()
                last_move_time = current_time
            elif keys[pygame.K_d]:
                movement.go_right()
                last_move_time = current_time



        # Drawer!!!! (View)
        window.screen.fill((0, 0, 0))

        window.screen.blit(window.bg_surface, (0, 0))

        for ci in coin.coins_on_screen_list:
            if ci.coin_visible == 1:
                window.screen.blit(ci.image, ci.rect)

        for bu in blue_machine.blue_machines:
            if bu.machine_visible == 1:
                window.screen.blit(bu.image, bu.rect)

                if bu.blue_machine_laser.laser_visible == 1:
                    window.screen.blit(bu.blue_machine_laser.image, bu.blue_machine_laser.rect)

        for pu in power_up.current_power_ups:
            if pu.power_up_visible == 1:
                window.screen.blit(pu.image, pu.rect)

        for mp in machine_player.current_player:
            if mp.player_visible == 1:
                window.screen.blit(mp.image, mp.rect)

                for mpl in mp.laser_list:
                    if mpl.laser_visible == 1:
                        window.screen.blit(mpl.image, mpl.rect)

                window.screen.blit(mp.health_bar.image, mp.health_bar.rect)

                if hasattr(mp, 'armor_bar') and mp.armor_bar.armor_bar_visible == 1:
                    window.screen.blit(mp.armor_bar.image, mp.armor_bar.rect)

        for ypi in yellow_power_up_indicator.yellow_power_up_indicator_sprite:
            if ypi.yellow_power_up_indicator_visible == 1:
                window.screen.blit(ypi.image, ypi.rect)

        for bpi in blue_power_up_indicator.blue_power_up_indicator_sprite:
            if bpi.blue_power_up_indicator_visible == 1:
                window.screen.blit(bpi.image, bpi.rect)

        for epi in extra_power_up_indicator.extra_power_up_indicator_sprite:
            if epi.extra_power_up_indicator_visible == 1:
                window.screen.blit(epi.image, epi.rect)

        for ci in coin_indicator.coin_indicator_sprite:
            if ci.coin_indicator_visible == 1:
                window.screen.blit(ci.image, ci.rect)

        for bu in button.buttons_on_screen_list:
            if bu.button_frame_visible == 1:
                window.screen.blit(bu.image, bu.rect)

            if bu.button_text.button_text_visible == 1:
                window.screen.blit(bu.button_text.image, bu.button_text.rect)

            if hasattr(bu, "button_indicator") and bu.button_indicator.indicator_visible == 1:
                window.screen.blit(bu.button_indicator.image, bu.button_indicator.rect)

        for t in textbox.text_on_screen_list:
            if t.text_box_visible == 1:
                window.screen.blit(t.image, t.rect)



        # Rest of regular logic

        text_refresh.update_text()

        current_ticks = pygame.time.get_ticks()
        elapsed_time = (current_ticks - start_ticks) / 1000.0
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

        # Screen update is 1 when the screen has been changed
        if screen.screen_update == 1:
            # Things that need to be updated between screens are updated here
            # Old button and text box sprites are removed
            for bu in button.buttons_on_screen_list:
                bu.remove()
            button.buttons_on_screen_list.clear()
            button.current_button_index = 0
            for t in textbox.text_on_screen_list:
                t.get_text_box().clear()
                t.remove()
            textbox.text_on_screen_list.clear()
            textbox.current_text_index = 0
            refresh_variables.refresh_button = 1
            refresh_variables.refresh_indicator = 1
            refresh_variables.refresh_text = 1
            screen.screen_update = 0
            screen.page_update = 0
            button.buy_button_pressed = 0
            gc.collect()

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
            power_up.power_up_index[4] = 0

            # Remove the coin indicator
            for ci in coin_indicator.coin_indicator_sprite:
                ci.remove()
            coin_indicator.coin_indicator_sprite.clear()
            coin_indicator.coin_indicator_index = 0

            # Remove the power up indicators
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_sprite:
                yi.remove()
            yellow_power_up_indicator.yellow_power_up_indicator_sprite.clear()
            yellow_power_up_indicator.yellow_power_up_indicator_index = 0
            for bi in blue_power_up_indicator.blue_power_up_indicator_sprite:
                bi.remove()
            blue_power_up_indicator.blue_power_up_indicator_sprite.clear()
            blue_power_up_indicator.blue_power_up_indicator_index = 0
            for ei in extra_power_up_indicator.extra_power_up_indicator_sprite:
                ei.remove()
            extra_power_up_indicator.extra_power_up_indicator_sprite.clear()
            extra_power_up_indicator.extra_power_up_indicator_index = 0

            # Remove all the coins on the screen
            for c in coin.coins_on_screen_list:
                c.remove()
            coin.coins_on_screen_list.clear()
            coin.current_coin_index = 0
            coin.coin_pickup_delay = 0

            # Spawn the title mode buttons
            if button.current_button_index == 0:
                for i in range(3):
                    button.spawn_button("Title", i + 1)
                for i in range(1):
                    button.spawn_button("Title_Locked", i + 1)
                for i in range(2):
                    button.spawn_button("Title_Small", i + 1)

            # Spawn the title mode text (Like title and version number in the bottom corner)
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 640 * window.scale_factor_X, 155 * window.scale_factor_Y, "red")
                textbox.spawn_text_box(2, 1150 * window.scale_factor_X, 693 * window.scale_factor_Y, "white")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(3, 1121 * window.scale_factor_X, 40 * window.scale_factor_Y, "white")
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)

        """
            When Machine Mode is on
        """

        if screen.mode == "Machine_Mode":
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)

            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 640 * window.scale_factor_X, 20 * window.scale_factor_Y, "white")
                textbox.spawn_text_box(2, 575 * window.scale_factor_X, 62 * window.scale_factor_Y, "#737000")
                textbox.spawn_text_box(3, 650 * window.scale_factor_X, 62 * window.scale_factor_Y, "#00001A")
                textbox.spawn_text_box(4, 720 * window.scale_factor_X, 62 * window.scale_factor_Y, "#001C00")
                textbox.spawn_text_box(5, 52 * window.scale_factor_X, 44 * window.scale_factor_Y, "yellow")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(6, 1121 * window.scale_factor_X, 20 * window.scale_factor_Y, "white")

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
                extra_power_up_indicator.spawn_extra_power_up_indicator("Machine_Mode")

            # Check if the players score is greater than the current high score
            if settings.god_mode == 0:
                if statistics.score > statistics.high_score_machine_war:
                    # Update the high score in the game and the ini file if it is
                    statistics.high_score_machine_war = statistics.score
                    statistics.save()

            if machine_player.current_player_index == 0:
                machine_player.spawn_machine_player(settings.god_mode)

            if blue_machine.blue_machine_index == 0:
                for i in range(100):
                    blue_machine.spawn_blue_machine(i + 1)

            for p in machine_player.current_player:
                p.shoot(settings.player_shooting_sound, yellow_power_up_indicator.yellow_power_up_indicator_sprite[0].get_power_up_active())

            for bm in blue_machine.blue_machines:
                bm.shoot_laser(extra_power_up_indicator.extra_power_up_indicator_sprite[0].get_power_up_active(), settings.enemy_shooting_sound)

            hit_coin = 0
            for c in coin.coins_on_screen_list:
                for p in machine_player.current_player:
                    # Check each of the players lasers
                    for l in p.get_laser():
                        # If the player picks up a coin
                        if l.isvisible() and \
                         c.rect.centerx - 50 * window.scale_factor_X < l.rect.centerx < c.rect.centerx + 50 * window.scale_factor_X and \
                         c.rect.centery - 50 * window.scale_factor_Y < l.rect.centery < c.rect.centery + 50 * window.scale_factor_Y and \
                         coin.coin_pickup_delay == 0:
                            # Remove the coin from the screen
                            c.remove()
                            # Increase the amount of coins the users has based on the type of coin picked up
                            if c.get_type() == "copper":
                                # For each coin, check if the blue power up has a multiplier on it
                                if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_value
                            elif c.get_type() == "silver":
                                if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_value
                            elif c.get_type() == "gold":
                                if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_value
                            elif c.get_type() == "platinum":
                                if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_blue_value
                                else:
                                    shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                                    statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_value
                            del c
                            shop_config.save()
                            statistics.save()
                            coin.coins_on_screen_list.pop(hit_coin)
                            # play the coin pickup sound
                            if settings.coin_pickup_sound == 1:
                                sound = pygame.mixer.Sound("sound/Coin_Pickup_Sound.wav")
                                sound.play()
                            break
                    hit_coin = hit_coin + 1

            # Collision still not working
            for p in machine_player.current_player:
                if p.do_collision == 1:
                    machine_collision.calculate_collisions(0, 0)
                    p.do_collision = 0
                elif p.do_collision == 2:
                    machine_collision.calculate_collisions(0, 1)
                    p.do_collision = 0
                elif p.do_collision == 3:
                    machine_collision.calculate_collisions(0, 2)
                    p.do_collision = 0

            # Enemy Killer
            for p in machine_player.current_player:
                current_blue_update_value_index = 0
                for bm in blue_machine.blue_machines:
                    # If the player laser hits a blue machine that is visible and not dying
                    if bm.get_blue_machine().isvisible() and blue_machine.blue_machines_update_values[current_blue_update_value_index] == 0:
                        laser_killer = 0
                        attacked = 0
                        # Check to see if the laser will attack it
                        for i in range(len(p.get_laser())):
                            if p.get_laser()[i].isvisible() and \
                             (bm.rect.centerx - 50 * window.scale_factor_X < p.get_laser()[i].rect.centerx < bm.rect.centerx + 50 * window.scale_factor_X) and \
                             (bm.rect.centery - 50 * window.scale_factor_Y < p.get_laser()[i].rect.centery < bm.rect.centery + 50 * window.scale_factor_Y):
                                # If it has, initiate the killing of the enemy
                                attacked = 1

                                # Confirm that the players laser has attacked
                                p.set_laser_has_attacked(1, i)
                                laser_killer = 1

                        # Check to see if the machine hit the player and the player has the thorns gadget enabled
                        if bm.thorns_initiated_damage == 1 and laser_killer == 0:
                            # If so, initiate the killing of the enemy
                            attacked = 1

                        # If the killing of the enemy has been initiated
                        if attacked == 1:
                            # Kill the enemy
                            bm.kill_enemy(1, coin.coins_on_screen_list, window.scale_factor_X)
                            blue_machine.blue_machines_update_values[current_blue_update_value_index] = \
                            blue_machine.blue_machines_update_values[current_blue_update_value_index] + 1

                            # Increase the players score
                            # When the blue power up is active, the score increases are doubled (This is universal)
                            if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                                statistics.score = statistics.score + 1 * machine_mode_setup.blue_power_up_score_multiplier
                            else:
                                statistics.score = statistics.score + 1 * machine_mode_setup.regular_score_multiplier

                            # Update the stats if god mode is off
                            if settings.god_mode == 0:
                                statistics.blue_bots_killed = statistics.blue_bots_killed + 1
                                statistics.save()
                    elif blue_machine.blue_machines_update_values[current_blue_update_value_index] != 0:
                        # Kill the enemy
                        bm.kill_enemy(1, coin.coins_on_screen_list, window.scale_factor_X)
                        blue_machine.blue_machines_update_values[current_blue_update_value_index] = \
                        blue_machine.blue_machines_update_values[current_blue_update_value_index] + 1

                        # Check if the death animation is finished
                        if bm.get_update_value() == 0:
                            blue_machine.blue_machines_update_values[current_blue_update_value_index] = 0
                            coin.coin_pickup_delay = 0

                        # Delay the coin pickup so it does not pick up the coin at the same time as killing the enemy
                        if bm.get_update_value() == 3:
                            coin.coin_pickup_delay = 1
                    current_blue_update_value_index = current_blue_update_value_index + 1

            # Player Killer
            for p in machine_player.current_player:
                # If the death animation has already started
                if machine_player.player_update_value != 0:
                    # Keep going with the player death animation if it has started
                    p.kill_player(1)
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
                        if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * window.scale_factor:
                            if bm.get_blue_machine_laser().isvisible() and -30 * window.scale_factor_X < (
                                    bm.get_blue_machine_laser().rect.centerx - p.rect.centerx) < 30 * window.scale_factor_X:
                                bm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() == 1 and p.get_hit_delay() == 0: #and settings.god_mode == 0:
                                    # If so kill the player and set the score down to 0 to reset the game
                                    p.kill_player(settings.player_death_sound)
                                    statistics.score = 0
                                    machine_player.player_update_value = machine_player.player_update_value + 1
                                    # If the player has thorns enabled, initiate the thorns damage on the enemy
                                    #if shop_config.thorns_enabled:
                                        #bm.thorns_initiated_damage = 1

                # If the player has more than 1 health, only deal 1 health of damage
                # If the hit delay is ongoing
                if machine_player.player_hit_value != 0:
                    p.hit_player(1)
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
                        if bm.get_blue_machine_laser().distance(p.get_player()) < 125 * window.scale_factor:
                            if bm.get_blue_machine_laser().isvisible() and -30 * window.scale_factor_X < (
                                    bm.get_blue_machine_laser().rect.centerx - p.rect.centerx) < 30 * window.scale_factor_X:
                                bm.set_laser_has_attacked(1)
                                if p.get_death_animation() == 0 and p.get_health_bar_indicator() != 1 and p.get_health_bar_indicator() != 0 and p.get_hit_delay() == 0:# and settings.god_mode == 0:
                                    # Hit the player
                                    p.hit_player(settings.player_hit_sound)
                                    machine_player.player_hit_value = machine_player.player_hit_value + 1
                                    # If the player has thorns enabled, initiate the thorns damage on the enemy
                                    #if shop_config.thorns_enabled:
                                    #    bm.thorns_initiated_damage = 1

            for bm in blue_machine.blue_machines:
                bm.float_effect()

            for p in machine_player.current_player:
                for bm in blue_machine.blue_machines:
                    bm.move_enemy(p.get_death_animation())

            # Check if the power ups are active or not
            for t in textbox.text_on_screen_list:
                # If they are, activate the power up timers
                if t.id == 2:
                    if yellow_power_up_indicator.yellow_power_up_indicator_sprite[0].get_power_up_active() == 1:
                        t.set_color("yellow")
                    else:
                        t.set_color("#737000")
                elif t.id == 3:
                    if blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 1:
                        t.set_color("#02CCFE")
                    else:
                        t.set_color("#00004A")
                elif t.id == 4:
                    if extra_power_up_indicator.extra_power_up_indicator_sprite[0].get_power_up_active() == 1:
                        t.set_color("#65FE08")
                    else:
                        t.set_color("#001C00")

            # Activate the power up indicators if the power ups become active
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_sprite:
                yi.set_texture()

            for bi in blue_power_up_indicator.blue_power_up_indicator_sprite:
                bi.set_texture()

            for ei in extra_power_up_indicator.extra_power_up_indicator_sprite:
                ei.set_texture()

            # If the RNG hits the 1/200, then spawn the power ups
            # The chances are increased when the spawn rate is 2 up to 1/100 RNG
            # 1 for yellow power up
            if (power_up.power_up_update == 1 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 2)) and \
                    yellow_power_up_indicator.yellow_power_up_indicator_sprite[0].get_power_up_active() == 0:
                if power_up.power_up_index[0] == 0:
                    power_up.spawn_power_up(1, "Machine_Mode", settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 1:
                            pu.spawn(settings.power_up_spawn_sound)

            # 50 for blue power up
            if (power_up.power_up_update == 50 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 51)) and \
                    blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 0:
                if power_up.power_up_index[1] == 0:
                    power_up.spawn_power_up(2, "Machine_Mode", settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 2:
                            pu.spawn(settings.power_up_spawn_sound)

            # 100 for the extra power up
            if (power_up.power_up_update == 100 or (machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 101)) and \
                    extra_power_up_indicator.extra_power_up_indicator_sprite[0].get_power_up_active() == 0:
                if power_up.power_up_index[2] == 0:
                    power_up.spawn_power_up(3, "Machine_Mode", settings.power_up_spawn_sound)
                else:
                    for pu in power_up.current_power_ups:
                        if pu.get_type() == 3:
                            pu.spawn(settings.power_up_spawn_sound)

            # 75 for the heart power up if the heart gadget is enabled
            # if shop_config.hearts_enabled:
            #     if power_up.power_up_update == 75 or (
            #             machine_mode_setup.power_up_spawn_rate == 2 and power_up.power_up_update == 76):
            #         if power_up.power_up_index[4] == 0:
            #             power_up.spawn_power_up(5, screen.mode, settings.power_up_spawn_sound)
            #         else:
            #             for pu in power_up.current_power_ups:
            #                 if pu.get_type() == 5:
            #                     pu.spawn(settings.power_up_spawn_sound)

            # Check if the player has picked up a power up or not
            for p in machine_player.current_player:
                for pu in power_up.current_power_ups:
                    # If a power up is visible
                    if pu.get_power_up().isvisible():
                        # Check its type (1 = yellow, 2 = blue, 3 = green, and 5 = heart)
                        # If the player runs to the power up
                        if pu.type == 1 and pu.get_power_up().distance(p.get_player()) < 50 * window.scale_factor and p.get_death_animation() == 0 and \
                                yellow_power_up_indicator.yellow_power_up_indicator_sprite[0].get_power_up_active() == 0:
                            # Pick it up
                            pu.pick_up(settings.power_up_pickup_sound)
                            # Update the stats
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            # Activate the specified power up (In this case yellow)
                            yellow_power_up_indicator.yellow_power_up_indicator_sprite[0].set_power_up_active(1)

                        if pu.type == 2 and pu.get_power_up().distance(p.get_player()) < 50 * window.scale_factor and p.get_death_animation() == 0 and \
                                blue_power_up_indicator.blue_power_up_indicator_sprite[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            blue_power_up_indicator.blue_power_up_indicator_sprite[0].set_power_up_active(1)

                        if pu.type == 3 and pu.get_power_up().distance(p.get_player()) < 50 * window.scale_factor and p.get_death_animation() == 0 and \
                                extra_power_up_indicator.extra_power_up_indicator_sprite[0].get_power_up_active() == 0:
                            pu.pick_up(settings.power_up_pickup_sound)
                            if settings.god_mode == 0:
                                statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                                statistics.save()
                            extra_power_up_indicator.extra_power_up_indicator_sprite[0].set_power_up_active(1)

                        # Allow for the heart power up if the heart gadget is enabled
                        # if shop_config.hearts_enabled:
                        #     if pu.type == 5 and pu.get_power_up().distance(
                        #             p.get_player()) < 50 * scale_factor and p.get_death_animation() == 0:
                        #         pu.pick_up(settings.power_up_pickup_sound)
                        #         if settings.god_mode == 0:
                        #             statistics.classic_power_ups_picked_up = statistics.classic_power_ups_picked_up + 1
                        #             statistics.save()
                        #         # Grant the player health
                        #         p.grant_player_health()

            # If the power ups are active, run their timers through these functions
            for yi in yellow_power_up_indicator.yellow_power_up_indicator_sprite:
                yi.set_timer()

            for bi in blue_power_up_indicator.blue_power_up_indicator_sprite:
                bi.set_timer()

            for ei in extra_power_up_indicator.extra_power_up_indicator_sprite:
                ei.set_timer()
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

        """
             Code Below is for when Statistics Mode is turned on.
        """

        if screen.mode == "Stats":
            # Create Main Menu button
            if button.current_button_index == 0:
                button.spawn_button("Game", 1)

            # Create the statistics text
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 640 * window.scale_factor_X, 120 * window.scale_factor_Y, "red")
                textbox.spawn_text_box(2, 320 * window.scale_factor_X, 220 * window.scale_factor_Y, "#ff5349")
                textbox.spawn_text_box(3, 960 * window.scale_factor_X, 220 * window.scale_factor_Y, "#ff5349")
                for i in range(10):
                    textbox.spawn_text_box(i + 4, 320 * window.scale_factor_X, (270 + (i * 40)) * window.scale_factor_Y, "white")
                for i in range(11):
                    textbox.spawn_text_box(13 + i + 1, 960 * window.scale_factor_X, (270 + (i * 40)) * window.scale_factor_Y,
                                           "white")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(25, 1121 * window.scale_factor_X, 40 * window.scale_factor_Y, "white")

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

            # Create all additional text boxes
            if textbox.current_text_index == 0:
                textbox.spawn_text_box(1, 640 * window.scale_factor_X, 70 * window.scale_factor_Y, "red")
                if settings.god_mode == 1:
                    textbox.spawn_text_box(2, 159 * window.scale_factor_X, 40 * window.scale_factor_Y, "white")

            # Move the title text left and right across the screen
            for t in textbox.text_on_screen_list:
                if t.id == 1:
                    t.move(screen.mode)
                    break

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
