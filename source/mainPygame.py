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
from components.spawn.SpawnCoinPygame import SpawnCoinIndicator
from physics.MachineCollisionPygame import MachineCollision
from utils.MovementManagerPygame import Movement


def main():
    window = GameWindow()
    coin = SpawnCoin()
    blue_machine = SpawnBlueMachine(window.scale_factor_X, window.scale_factor_Y)
    machine_player = SpawnMachinePlayer(window.scale_factor_X, window.scale_factor_Y)
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



        # Drawer!!!!
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

        for ci in coin_indicator.coin_indicator_sprite:
            if ci.coin_indicator_visible == 1:
                window.screen.blit(ci.image, ci.rect)



        # Rest of regular logic
        if blue_machine.blue_machine_index == 0:
            for i in range(3):
                blue_machine.spawn_blue_machine(i + 1)

        if machine_player.current_player_index == 0:
            machine_player.spawn_machine_player(0)

        if coin_indicator.coin_indicator_index == 0:
            coin_indicator.spawn_coin_indicator()

        for bm in blue_machine.blue_machines:
            bm.shoot_laser(0, 1)

        for bm in blue_machine.blue_machines:
            bm.float_effect()

        for bm in blue_machine.blue_machines:
            bm.move_enemy(0)

        for p in machine_player.current_player:
            p.shoot(1, 0)

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
                                (bm.x_range_list[i][0] < p.get_laser()[i].rect.centerx < bm.x_range_list[i][
                                    1]) and \
                                p.get_laser()[i].rect.centery > bm.collision_y_coordinate_list[i]:
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

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
