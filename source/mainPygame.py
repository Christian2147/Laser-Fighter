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
from setup.WindowSetupPygame import GameWindow
from components.spawn.SpawnMachinePygame import SpawnBlueMachine
from components.spawn.SpawnPlayerPygame import SpawnMachinePlayer
from components.spawn.SpawnCoinPygame import SpawnCoinIndicator


def main():
    window = GameWindow()
    blue_machine = SpawnBlueMachine(window.scale_factor_X, window.scale_factor_Y)
    machine_player = SpawnMachinePlayer(window.scale_factor_X, window.scale_factor_Y)
    coin_indicator = SpawnCoinIndicator(window.scale_factor_X, window.scale_factor_Y)

    # The main game loop:
    running = True
    while running:
        window.CLOCK.tick(window.TARGET_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False



        # Drawer!!!!
        window.screen.fill((0, 0, 0))

        window.screen.blit(window.bg_surface, (0, 0))

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

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
