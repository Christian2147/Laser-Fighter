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

from setup.ModeSetupMaster import machine_mode_setup
from physics.CollisionMaster import machine_collision
from physics.CollisionMaster import alien_collision


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

    def __init__(self, screen, machine_player, human_player, yellow_power_up_indicator, settings, statistics, scale_factor_y):
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
        self._screen = screen
        self._machine_player = machine_player
        self._human_player = human_player
        self._yellow_power_up_indicator = yellow_power_up_indicator
        self._settings = settings
        self._statistics = statistics

        self._scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._screen
        del self._machine_player
        del self._human_player
        del self._yellow_power_up_indicator
        del self._settings
        del self._statistics
        del self._scale_factor_y

    def go_right(self):
        """
            Function for moving right in Laser Fighter. Activates when the keybind to move right is triggered.

            :return: None
        """

        if self._screen.mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                # The machine player is prepared to move right and faces right
                p.set_direction_right()
            self.move()
        if self._screen.mode == "Alien_Mode":
            for h in self._human_player.current_human:
                # Prepares the human player to move right
                h.go_right()

    def go_left(self):
        """
            Function for moving left in Laser Fighter. Activates when the keybind to move left is triggered.

            :return: None
        """

        if self._screen.mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                # The machine player is prepared to move left and faces left
                p.set_direction_left()
            self.move()
        if self._screen.mode == "Alien_Mode":
            for h in self._human_player.current_human:
                # Prepares the human player to move left
                h.go_left()

    def move(self):
        """
            Function used to trigger the players movement in Machine Mode.

            :return: None
        """

        # Player is moved in its current facing direction when this function is activated.
        if self._screen.mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                for yi in self._yellow_power_up_indicator.yellow_power_up_indicator_turtle:
                    p.move_player(yi.yellow_power_up_active)

    def jump(self):
        """
            Function used to activate the players jump in Alien Mode.

            :return: None
        """

        if self._screen.mode == "Alien_Mode":
            for h in self._human_player.current_human:
                # Prepare the player for a jump
                h.jump()
                # If the jump can successfully be preformed given the circumstances required to preform it
                if self._settings.god_mode == 0 and h.do_jump == 1:
                    # Update the game statistics to show that the player has jumped
                    self._statistics.jumps = self._statistics.jumps + 1
                    self._statistics.save()

    def shoot(self):
        """
            Function used to fire the players laser.

            :return: None
        """

        if self._screen.mode == "Machine_Mode":
            for p in self._machine_player.current_player:
                # If the laser is not currently moving across the screen and if the player is not dying
                if p.get_laser()[0].laser.ycor() > machine_mode_setup.laser_max_distance - 1 and p.get_death_animation() == 0:
                    # Reset the collision variables
                    machine_collision.remove_collisions()
                    p.remove_laser_start_y()
                    # The laser is fired
                    p.fire(self._settings.player_shooting_sound)
                    # Update the game statistics
                    if self._settings.god_mode == 0:
                        self._statistics.classic_lasers_fired = self._statistics.classic_lasers_fired + 1
                        self._statistics.save()
        elif self._screen.mode == "Alien_Mode":
            for h in self._human_player.current_human:
                # If the laser is not currently flying across the screen and if the player is not in the
                #   process of dying
                if h.shoot_update == 0 and h.death_animation == 0 and h.direction != 0:
                    # Fire the laser
                    h.shoot(self._settings.player_shooting_sound)
                    # Recalculate collision parameters based on the new laser fired
                    alien_collision.calculate_collision()
                    # Update the game statistics
                    if self._settings.god_mode == 0:
                        self._statistics.alien_lasers_fired = self._statistics.alien_lasers_fired + 1
                        self._statistics.save()
