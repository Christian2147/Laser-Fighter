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
    File: ItemGadget.py
    Author: Christian Marinkovich
    Date: 2024-08-07
    Description:
    This file contains the logic for any gadget functions. The gadgets themselves typically do not need sprites.
    If they do need specific sprites for displaying them, they will be created here.
"""

import time
import math


class Gadget:
    """
        Represents general gadget functions in Laser Fighter.

        Pointers:
            _machine_player (MachinePlayer()): Pointer to the machine player object.
            _human_player (HumanPlayer()): Pointer to the human player object.
            _coins (Coin()): Pointer to the coin object

        Attributes:
            _scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            start_time (float): Used as a starting timestamp for the delta time for the coins movement towards the
                player
    """

    def __init__(self, machine_player, human_player, coins, scale_factor):
        """
            Initializes the gadget functions.

            :param machine_player: Pointer to the machine player object.
            :type machine_player: MachinePlayer()

            :param human_player: Pointer to the human player object.
            :type human_player: HumanPlayer()

            :param coins: Pointer to the coin object
            :type coins: Coin()

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float
        """

        # Initialize pointers
        self._machine_player = machine_player
        self._human_player = human_player
        self._coins = coins

        self._scale_factor = scale_factor

        # Start the timer
        self.start_time = time.time()

    def __del__(self):
        """
            Cleans up the variables from memory once the program has terminated

            :return: None
        """

        del self._machine_player
        del self._human_player
        del self._coins
        del self._scale_factor
        del self.start_time

    def start_timer(self):
        """
            Begin tracking the time for the coins movement delta time.

            :return: None
        """

        self.start_time = time.time()

    def attract_coins(self, mode):
        """
            Function for moving the coins towards the player while the coin magnet is enabled.

            :param mode: The current mode of the game
            :type mode: string

            :return: None
        """

        if mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                player_position = p.player.position()

                current_time = time.time()
                elapsed_time = current_time - self.start_time
                # Every 0.002 seconds, move the coin 1.75 units
                if elapsed_time >= 0.002:
                    for c in self._coins.coins_on_screen_list:
                        if c.coin.isvisible():
                            # Get the coins current position
                            coin_position = c.coin.position()

                            # Find the angle that it needs to move at in order to move towards the player and set
                            #   its heading towards that angle
                            angle = math.degrees(math.atan2(player_position[1] - coin_position[1], player_position[0] - coin_position[0]))
                            c.coin.setheading(angle)

                            # Move the coin 1.75 units with the delta movement
                            delta_movement = 1.75 * self._scale_factor * ((elapsed_time - 0.002) / 0.002)
                            c.coin.forward(1.75 * self._scale_factor + delta_movement)
                # Reset the timer
                self.start_time = time.time()
        elif mode == "Alien_Mode":
            # Same procedure here as in Machine Mode, but with the human player being the object to move towards
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
