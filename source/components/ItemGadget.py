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

import time
import math


class Gadget:
    def __init__(self, machine_player, human_player, coins, scale_factor):
        self._machine_player = machine_player
        self._human_player = human_player
        self._coins = coins

        self._scale_factor = scale_factor

        self.start_time = time.time()

    def __del__(self):
        del self._machine_player
        del self._human_player
        del self._coins
        del self._scale_factor
        del self.start_time

    def start_timer(self):
        self.start_time = time.time()

    def attract_coins(self, mode):
        if mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                player_position = p.player.position()

                current_time = time.time()
                elapsed_time = current_time - self.start_time
                if elapsed_time >= 0.002:
                    for c in self._coins.coins_on_screen_list:
                        if c.coin.isvisible():
                            coin_position = c.coin.position()

                            angle = math.degrees(math.atan2(player_position[1] - coin_position[1], player_position[0] - coin_position[0]))
                            c.coin.setheading(angle)

                            delta_movement = 1.75 * self._scale_factor * ((elapsed_time - 0.002) / 0.002)
                            c.coin.forward(1.75 * self._scale_factor + delta_movement)
                self.start_time = time.time()
        elif mode == "Alien_Mode":
            for h in self._human_player.current_human:
                player_position = h.player.position()

                current_time = time.time()
                elapsed_time = current_time - self.start_time
                if elapsed_time >= 0.002:
                    for c in self._coins.coins_on_screen_list:
                        if c.coin.isvisible():
                            coin_position = c.coin.position()

                            angle = math.degrees(math.atan2(player_position[1] - coin_position[1], player_position[0] - coin_position[0]))
                            c.coin.setheading(angle)

                            delta_movement = 1.75 * self._scale_factor * ((elapsed_time - 0.002) / 0.002)
                            c.coin.forward(1.75 * self._scale_factor + delta_movement)
                self.start_time = time.time()
