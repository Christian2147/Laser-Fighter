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
from setup.WindowSetupPygame import GameWindow
from components.spawn.SpawnCoinPygame import SpawnCoin
from components.spawn.SpawnMachinePygame import SpawnBlueMachine
from components.spawn.SpawnPlayerPygame import SpawnMachinePlayer
from components.spawn.SpawnPowerUpPygame import SpawnYellowPowerUpIndicator
from components.spawn.SpawnPowerUpPygame import SpawnBluePowerUpIndicator
from components.spawn.SpawnPowerUpPygame import SpawnExtraPowerUpIndicator
from components.spawn.SpawnCoinPygame import SpawnCoinIndicator
from physics.MachineCollisionPygame import MachineCollision
from utils.MovementManagerPygame import Movement


def main():
    window = GameWindow()
    coin = SpawnCoin()
    blue_machine = SpawnBlueMachine(window.scale_factor_X, window.scale_factor_Y)
    machine_player = SpawnMachinePlayer(window.scale_factor_X, window.scale_factor_Y)

    yellow_power_up_indicator = SpawnYellowPowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    blue_power_up_indicator = SpawnBluePowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    extra_power_up_indicator = SpawnExtraPowerUpIndicator(window.scale_factor_X, window.scale_factor_Y)
    coin_indicator = SpawnCoinIndicator(window.scale_factor_X, window.scale_factor_Y)

    machine_collision = MachineCollision(machine_player, blue_machine, window.scale_factor_X, window.scale_factor_Y)
    movement = Movement(machine_player, window.scale_factor_Y)

    MOVE_REPEAT_DELAY = 0.05
    last_move_time = 0

    # The main game loop:
    running = True
    while running:
        window.CLOCK.tick(window.TARGET_FPS)

        # EVENT HANDLER
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Shoot
                    movement.shoot(machine_collision)

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



        # Rest of regular logic
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

        if machine_player.current_player_index == 0:
            machine_player.spawn_machine_player(0)

        if blue_machine.blue_machine_index == 0:
            for i in range(3):
                blue_machine.spawn_blue_machine(i + 1)

        for p in machine_player.current_player:
            p.shoot(1, 0)

        for bm in blue_machine.blue_machines:
            bm.shoot_laser(0, 1)

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
                        # if c.get_type() == "copper":
                        #     # For each coin, check if the blue power up has a multiplier on it
                        #     if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_blue_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_blue_value
                        #     else:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.copper_coin_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.copper_coin_value
                        # elif c.get_type() == "silver":
                        #     if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_blue_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_blue_value
                        #     else:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.silver_coin_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.silver_coin_value
                        # elif c.get_type() == "gold":
                        #     if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_blue_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_blue_value
                        #     else:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.gold_coin_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.gold_coin_value
                        # elif c.get_type() == "platinum":
                        #     if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_blue_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_blue_value
                        #     else:
                        #         shop_config.total_coins = shop_config.total_coins + power_up_setup.platinum_coin_value
                        #         statistics.machine_coins_collected = statistics.machine_coins_collected + power_up_setup.platinum_coin_value
                        # shop_config.save()
                        # statistics.save()
                        coin.coins_on_screen_list.pop(hit_coin)
                        # play the coin pickup sound
                        if 1: #settings.coin_pickup_sound == 1:
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
                        #if blue_power_up_indicator.blue_power_up_indicator_turtle[0].get_power_up_active() == 1:
                            #statistics.score = statistics.score + 1 * machine_mode_setup.blue_power_up_score_multiplier
                        #else:
                            #statistics.score = statistics.score + 1 * machine_mode_setup.regular_score_multiplier

                        # Update the stats if god mode is off
                        #if settings.god_mode == 0:
                            #statistics.blue_bots_killed = statistics.blue_bots_killed + 1
                            #statistics.save()
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
                    #if settings.god_mode == 0:
                    #    statistics.classic_deaths = statistics.classic_deaths + 1
                    #    statistics.machine_damage_taken = statistics.machine_damage_taken + 1
                    #    statistics.save()
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
                                p.kill_player(1)
                                #statistics.score = 0
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
                #if p.get_hit_delay() == 2:
                #    statistics.machine_damage_taken = statistics.machine_damage_taken + 1
                #    statistics.save()
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
                                p.hit_player(1)
                                machine_player.player_hit_value = machine_player.player_hit_value + 1
                                # If the player has thorns enabled, initiate the thorns damage on the enemy
                                #if shop_config.thorns_enabled:
                                #    bm.thorns_initiated_damage = 1

        for bm in blue_machine.blue_machines:
            bm.float_effect()

        for bm in blue_machine.blue_machines:
            bm.move_enemy(0)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
