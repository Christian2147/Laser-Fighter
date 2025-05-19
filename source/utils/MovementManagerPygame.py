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
    File: MovementManager.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for triggering in game movements and functions based on the keybinds.
    This includes shooting the laser and moving around in both Machine Mode and Alien Mode.
"""

from setup.ModeSetupMasterPygame import machine_mode_setup
# from physics.CollisionMaster import machine_collision
# from physics.CollisionMaster import alien_collision


class Movement:
    """
        Represents the logic for triggering in game movements and functions from the keybinds.

        Pointers:
            _screen (ScreenUpdate()): Pointer to the current displayed screen and the screen changing functions.
            _machine_player (MachinePlayer()): Pointer to the machine player object.
            _human_player (HumanPlayer()): Pointer to the human player object.
            _yellow_power_up_indicator (YellowPowerUpIndicator()): Pointer to the yellow power up indicator.
            _settings (Settings()): Pointer to the current game settings.
            _statistics (Statistics()): Pointer to the current game statistics.

        Attributes:
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode.
    """

    def __init__(self, machine_player, scale_factor_y):
        """
            Initializes all the necessary pointers for the Movement Manager.

            :param screen: Pointer to the current displayed screen and the screen changing functions.
            :type screen: ScreenUpdate()

            :param machine_player: Pointer to the machine player object.
            :type machine_player: MachinePlayer()

            :param human_player: Pointer to the human player object.
            :type human_player: HumanPlayer()

            :param yellow_power_up_indicator: Pointer to the yellow power up indicator.
            :type yellow_power_up_indicator: YellowPowerUpIndicator()

            :param settings: Pointer to the current game settings.
            :type settings: Settings()

            :param statistics: Pointer to the current game statistics.
            :type statistics: Statistics()

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode.
            :type scale_factor_y: float
        """

        # Initialize all the pointers
        self._machine_player = machine_player

        self._scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._machine_player
        del self._scale_factor_y

    def go_right(self):
        """
            Function for moving right in Laser Fighter. Activates when the keybind to move right is triggered.

            :return: None
        """

        for p in self._machine_player.current_player:
            # The machine player is prepared to move right and faces right
            p.set_direction_right()
        self.move()

    def go_left(self):
        """
            Function for moving left in Laser Fighter. Activates when the keybind to move left is triggered.

            :return: None
        """

        for p in self._machine_player.current_player:
            # The machine player is prepared to move left and faces left
            p.set_direction_left()
        self.move()

    def move(self):
        """
            Function used to trigger the players movement in Machine Mode.

            :return: None
        """

        # Player is moved in its current facing direction when this function is activated.
        for p in self._machine_player.current_player:
            p.move_player(0)

    def shoot(self, machine_collision):
        """
            Function used to fire the players laser.

            :return: None
        """

        for p in self._machine_player.current_player:
            # If the laser is not currently moving across the screen and if the player is not dying
            if p.get_laser()[0].rect.centery < machine_mode_setup.laser_max_distance + 1 and p.get_death_animation() == 0:
                # Reset the collision variables
                machine_collision.remove_collisions()
                p.remove_laser_start_y()
                # The laser is fired
                print("dude")
                p.fire(1)
                # Update the game statistics
