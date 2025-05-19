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
    File: MachineCollision.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for calculating collisions in Machine Mode.
"""

import time
import math
from scipy.optimize import fsolve
from setup.ModeSetupMasterPygame import machine_mode_setup


class MachineCollision:
    """
        Represents the hitboxes for all objects in Machine Mode.

        Class Variables:
            BLUE_MACHINE_DISTANCE (float): Stores the x axis distance away from the center of the blue machine that
                the players laser can be in order to still hit it. (Size of the hitbox)
            YELLOW_MACHINE_DISTANCE (float): Stores the x axis distance away from the center of the yellow machine that
                the players laser can be in order to still hit it. (Size of the hitbox)
            RED_MACHINE_DISTANCE (float): Stores the x axis distance away from the center of the red machine that
                the players laser can be in order to still hit it. (Size of the hitbox)
            BOSS_DISTANCE (float): Stores the x axis distance away from the center of the boss that
                the players laser can be in order to still hit it. (Size of the hitbox)

            FLOAT_AMPLITUDE (float): Stores the amplitude of the sin wave created by the machine float effect.
            PERIOD (int): Stores the period of the sin wave created by the machine float effect.

            MACHINE_(Num)_MOVEMENT_SPEED (float): The speed of the machines movement from side to side depending on
                how many times it has been killed.

        Pointers:
            _machine_player (SpawnMachinePlayer()): A pointer to the machine player object
            _blue_machine (SpawnBlueMachine()): A pointer to the blue machine object
            _yellow_machine (SpawnYellowMachine()): A pointer to the yellow machine object
            _red_machine (SpawnRedMachine()): A pointer to the red machine object
            _machine_boss (SpawnMachineBoss()): A pointer to the machine boss object

        Attributes:
            laser_speed (float): The current laser speed based on the shop configuration
            initial_distance (float): The initial distance between the players laser and the center of the machines
                float sin wave.
            enemy_center (float): The center point of the machines float sin wave
            float_time_offset (float): The time passed since the float effect for the machine began.
    """

    def __init__(self, machine_player, blue_machine, scale_factor_x, scale_factor_y):#, yellow_machine, red_machine, machine_boss):
        """
            Creates the hitboxes for all objects in Machine Mode.

            :param machine_player: A pointer to the machine player object
            :type machine_player: SpawnMachinePlayer()

            :param blue_machine: A pointer to the blue machine object
            :type blue_machine: SpawnBlueMachine()

            :param yellow_machine: A pointer to the yellow machine object
            :type yellow_machine: SpawnYellowMachine()

            :param red_machine: A pointer to the red machine object
            :type red_machine: SpawnRedMachine()

            :param machine_boss: A pointer to the machine boss object
            :type machine_boss: SpawnMachineBoss()
        """

        self.BLUE_MACHINE_DISTANCE = 55 * scale_factor_x
        self.YELLOW_MACHINE_DISTANCE = 59 * scale_factor_x
        self.RED_MACHINE_DISTANCE = 64 * scale_factor_x
        self.BOSS_DISTANCE = 75 * scale_factor_x

        self.FLOAT_AMPLITUDE = 50 * scale_factor_y
        self.PERIOD = 10

        self.MACHINE_0_2_MOVEMENT_SPEED = (2 * scale_factor_x) / 0.02
        self.MACHINE_2_4_MOVEMENT_SPEED = (4 * scale_factor_x) / 0.02
        self.MACHINE_4_6_MOVEMENT_SPEED = (6 * scale_factor_x) / 0.02
        self.MACHINE_6_8_MOVEMENT_SPEED = (8 * scale_factor_x) / 0.02
        self.MACHINE_8_10_MOVEMENT_SPEED = (10 * scale_factor_x) / 0.02

        self._machine_player = machine_player
        self._blue_machine = blue_machine
        #self._yellow_machine = yellow_machine
        #self._red_machine = red_machine
        #self._machine_boss = machine_boss

        self.laser_speed = 0
        self.initial_distance = 0
        self.enemy_center = 0
        self.float_time_offset = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._machine_player
        del self._blue_machine
        #del self._yellow_machine
        #del self._red_machine
        #del self._machine_boss
        del self.laser_speed
        del self.initial_distance
        del self.float_time_offset

    def calculate_collisions(self, yellow_power_up, index):
        """
            Calculates the hitboxes for Machine Mode based off of the laser that was just fired.

            :param yellow_power_up: Determines whether the yellow power up is currently on or off
            :type yellow_power_up: int

            :param index: The index of the current laser being analyzed
            :type index: int

            :return: None
        """

        # Find the current speed of the laser.
        if yellow_power_up == 1:
            self.laser_speed = machine_mode_setup.yellow_power_up_speed
        else:
            self.laser_speed = machine_mode_setup.laser_speed
        self.laser_speed = self.laser_speed/0.015

        # Calculate the hit boxes for the Blue Machine
        for bm in self._blue_machine.blue_machines:
            # Find the time it will take for the laser and the machine to intersect through a physics wave equation
            # This wave equation is inseparable and requires a powerful library to solve.
            self.enemy_center = bm.enemy_center
            current_time = time.time()
            self.float_time_offset = current_time - bm.float_time_offset
            self.initial_distance = self.enemy_center - self.BLUE_MACHINE_DISTANCE - self._machine_player.current_player[0].laser_list[index].rect.centery
            intersection_time = self.calculate_time()

            # Based off the intersection time, calculate the amount that the machine will move along the x-axis during
            #   that time.
            x_offset = 0
            if 4 <= bm.death_count < 7:
                x_offset = intersection_time[0] * self.MACHINE_0_2_MOVEMENT_SPEED * -1
            elif 7 <= bm.death_count < 10:
                x_offset = intersection_time[0] * self.MACHINE_2_4_MOVEMENT_SPEED * -1
            elif 10 <= bm.death_count < 13:
                x_offset = intersection_time[0] * self.MACHINE_4_6_MOVEMENT_SPEED * -1
            elif 13 <= bm.death_count < 16:
                x_offset = intersection_time[0] * self.MACHINE_6_8_MOVEMENT_SPEED * -1
            elif 16 <= bm.death_count:
                x_offset = intersection_time[0] * self.MACHINE_8_10_MOVEMENT_SPEED * -1

            # Check for cases where the machine hits the edge of the screen and turns around.
            if x_offset != 0:
                if bm.movement == -1:
                    x_offset = x_offset * -1
                    edge = 0 * self.scale_factor_x
                    distance_from_edge = edge - (bm.rect.centerx + x_offset)
                    if distance_from_edge > 0:
                        x_offset = x_offset + (2 * distance_from_edge)
                else:
                    edge = 1280 * self.scale_factor_x
                    distance_from_edge = edge - (bm.rect.centerx + x_offset)
                    if distance_from_edge < 0:
                        x_offset = x_offset + (2 * distance_from_edge)

            # Find the width of the hit box
            bm.x_range_list[index] = (bm.rect.centerx + x_offset - self.BLUE_MACHINE_DISTANCE, bm.rect.centerx + x_offset + self.BLUE_MACHINE_DISTANCE)

            # Find the y-coordinate the laser must reach in order to hit the enemy based on the sine wave
            collision_y_coordinate = self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (intersection_time[0] * -1 + self.float_time_offset)) / self.PERIOD) + \
                self.initial_distance + \
                self._machine_player.current_player[0].laser_list[index].rect.centery

            bm.collision_y_coordinate_list[index] = collision_y_coordinate

    def remove_collisions(self):
        """
            Resets the current collision variables for all machines.

            :return: None
        """

        for bm in self._blue_machine.blue_machines:
            bm.remove_collisions()

    def time_equation(self, t):
        """
            Used to create the equation to calculate the intersection time

            :param t: The parameter we are trying to solve for
            :type t: float

            :return: The equation to solve
        """

        return (self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (t + self.float_time_offset)) / self.PERIOD)) - (self.laser_speed * t + self.initial_distance)

    def calculate_time(self):
        """
            Calculates the laser and machine intersection time with an initial guess of 1.

            :return: The intersection time
            :type: list
        """

        initial_guess = 1
        return fsolve(self.time_equation, initial_guess)