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
from scipy.optimize import fsolve
from setup.ScreenSetup import scale_factor_X
from setup.ScreenSetup import scale_factor_Y
from setup.ModeSetupMaster import machine_mode_setup


class MachineCollision:
    BLUE_MACHINE_DISTANCE = 55 * scale_factor_X
    YELLOW_MACHINE_DISTANCE = 59 * scale_factor_X
    RED_MACHINE_DISTANCE = 64 * scale_factor_X
    BOSS_DISTANCE = 75 * scale_factor_X

    FLOAT_AMPLITUDE = 50 * scale_factor_Y
    PERIOD = 10

    MACHINE_0_2_MOVEMENT_SPEED = (2 * scale_factor_X) / 0.02
    MACHINE_2_4_MOVEMENT_SPEED = (4 * scale_factor_X) / 0.02
    MACHINE_4_6_MOVEMENT_SPEED = (6 * scale_factor_X) / 0.02
    MACHINE_6_8_MOVEMENT_SPEED = (8 * scale_factor_X) / 0.02
    MACHINE_8_10_MOVEMENT_SPEED = (10 * scale_factor_X) / 0.02

    def __init__(self, machine_player, blue_machine, yellow_machine, red_machine, machine_boss, coin):
        self._machine_player = machine_player
        self._blue_machine = blue_machine
        self._yellow_machine = yellow_machine
        self._red_machine = red_machine
        self._machine_boss = machine_boss
        self._coin = coin

        self.laser_speed = 0
        self.initial_distance = 0
        self.enemy_center = 0
        self.float_time_offset = 0

    def __del__(self):
        del self._machine_player
        del self._blue_machine
        del self._yellow_machine
        del self._red_machine
        del self._machine_boss
        del self._coin
        del self.laser_speed
        del self.initial_distance
        del self.float_time_offset

    def calculate_collisions(self, yellow_power_up):
        if yellow_power_up == 1:
            self.laser_speed = machine_mode_setup.yellow_power_up_speed
        else:
            self.laser_speed = machine_mode_setup.laser_speed
        self.laser_speed = self.laser_speed/0.015

        for bm in self._blue_machine.blue_machines:
            self.enemy_center = bm.enemy_center
            current_time = time.time()
            self.float_time_offset = current_time - bm.float_time_offset
            self.initial_distance = self.enemy_center - self.BLUE_MACHINE_DISTANCE - self._machine_player.current_player[0].laser.ycor()
            intersection_time = self.calculate_time()

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

            if x_offset != 0:
                if bm.movement == -1:
                    x_offset = x_offset * -1
                    edge = -640 * scale_factor_X
                    distance_from_edge = edge - (bm.blue_machine.xcor() + x_offset)
                    if distance_from_edge > 0:
                        x_offset = x_offset + (2 * distance_from_edge)
                else:
                    edge = 640 * scale_factor_X
                    distance_from_edge = edge - (bm.blue_machine.xcor() + x_offset)
                    if distance_from_edge < 0:
                        x_offset = x_offset + (2 * distance_from_edge)

            bm.x_range = (bm.blue_machine.xcor() + x_offset - self.BLUE_MACHINE_DISTANCE, bm.blue_machine.xcor() + x_offset + self.BLUE_MACHINE_DISTANCE)

            collision_y_coordinate = self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (intersection_time[0] * -1 + self.float_time_offset)) / self.PERIOD) + \
                self.initial_distance + \
                self._machine_player.current_player[0].laser.ycor()

            bm.collision_y_coordinate = collision_y_coordinate

        for ym in self._yellow_machine.yellow_machines:
            self.enemy_center = ym.enemy_center
            current_time = time.time()
            self.float_time_offset = current_time - ym.float_time_offset
            self.initial_distance = self.enemy_center - self.YELLOW_MACHINE_DISTANCE - self._machine_player.current_player[0].laser.ycor()
            intersection_time = self.calculate_time()

            x_offset = 0
            if 4 <= ym.death_count < 7:
                x_offset = intersection_time[0] * self.MACHINE_0_2_MOVEMENT_SPEED * -1
            elif 7 <= ym.death_count < 10:
                x_offset = intersection_time[0] * self.MACHINE_2_4_MOVEMENT_SPEED * -1
            elif 10 <= ym.death_count < 13:
                x_offset = intersection_time[0] * self.MACHINE_4_6_MOVEMENT_SPEED * -1
            elif 13 <= ym.death_count < 16:
                x_offset = intersection_time[0] * self.MACHINE_6_8_MOVEMENT_SPEED * -1
            elif 16 <= ym.death_count:
                x_offset = intersection_time[0] * self.MACHINE_8_10_MOVEMENT_SPEED * -1

            if x_offset != 0:
                if ym.movement == -1:
                    x_offset = x_offset * -1
                    edge = -640 * scale_factor_X
                    distance_from_edge = edge - (ym.yellow_machine.xcor() + x_offset)
                    if distance_from_edge > 0:
                        x_offset = x_offset + (2 * distance_from_edge)
                else:
                    edge = 640 * scale_factor_X
                    distance_from_edge = edge - (ym.yellow_machine.xcor() + x_offset)
                    if distance_from_edge < 0:
                        x_offset = x_offset + (2 * distance_from_edge)

            ym.x_range = (ym.yellow_machine.xcor() + x_offset - self.YELLOW_MACHINE_DISTANCE, ym.yellow_machine.xcor() + x_offset + self.YELLOW_MACHINE_DISTANCE)

            collision_y_coordinate = self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (intersection_time[0] * -1 + self.float_time_offset)) / self.PERIOD) + \
                self.initial_distance + \
                self._machine_player.current_player[0].laser.ycor()

            ym.collision_y_coordinate = collision_y_coordinate

        for rm in self._red_machine.red_machines:
            self.enemy_center = rm.enemy_center
            current_time = time.time()
            self.float_time_offset = current_time - rm.float_time_offset
            self.initial_distance = self.enemy_center - self.RED_MACHINE_DISTANCE - self._machine_player.current_player[0].laser.ycor()
            intersection_time = self.calculate_time()

            x_offset = 0
            if 4 <= rm.death_count < 7:
                x_offset = intersection_time[0] * self.MACHINE_0_2_MOVEMENT_SPEED * -1
            elif 7 <= rm.death_count < 10:
                x_offset = intersection_time[0] * self.MACHINE_2_4_MOVEMENT_SPEED * -1
            elif 10 <= rm.death_count < 13:
                x_offset = intersection_time[0] * self.MACHINE_4_6_MOVEMENT_SPEED * -1
            elif 13 <= rm.death_count < 16:
                x_offset = intersection_time[0] * self.MACHINE_6_8_MOVEMENT_SPEED * -1
            elif 16 <= rm.death_count:
                x_offset = intersection_time[0] * self.MACHINE_8_10_MOVEMENT_SPEED * -1

            if x_offset != 0:
                if rm.movement == -1:
                    x_offset = x_offset * -1
                    edge = -640 * scale_factor_X
                    distance_from_edge = edge - (rm.red_machine.xcor() + x_offset)
                    if distance_from_edge > 0:
                        x_offset = x_offset + (2 * distance_from_edge)
                else:
                    edge = 640 * scale_factor_X
                    distance_from_edge = edge - (rm.red_machine.xcor() + x_offset)
                    if distance_from_edge < 0:
                        x_offset = x_offset + (2 * distance_from_edge)

            rm.x_range = (rm.red_machine.xcor() + x_offset - self.RED_MACHINE_DISTANCE, rm.red_machine.xcor() + x_offset + self.RED_MACHINE_DISTANCE)

            collision_y_coordinate = self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (intersection_time[0] * -1 + self.float_time_offset)) / self.PERIOD) + \
                self.initial_distance + \
                self._machine_player.current_player[0].laser.ycor()

            rm.collision_y_coordinate = collision_y_coordinate

        for b in self._machine_boss.boss:
            self.enemy_center = b.enemy_center
            current_time = time.time()
            self.float_time_offset = current_time - b.float_time_offset
            self.initial_distance = self.enemy_center - self.BOSS_DISTANCE - self._machine_player.current_player[0].laser.ycor()
            intersection_time = self.calculate_time()

            x_offset = 0
            if 4 <= b.death_count < 7:
                x_offset = intersection_time[0] * self.MACHINE_0_2_MOVEMENT_SPEED * -1
            elif 7 <= b.death_count < 10:
                x_offset = intersection_time[0] * self.MACHINE_2_4_MOVEMENT_SPEED * -1
            elif 10 <= b.death_count < 13:
                x_offset = intersection_time[0] * self.MACHINE_4_6_MOVEMENT_SPEED * -1
            elif 13 <= b.death_count < 16:
                x_offset = intersection_time[0] * self.MACHINE_6_8_MOVEMENT_SPEED * -1
            elif 16 <= b.death_count:
                x_offset = intersection_time[0] * self.MACHINE_8_10_MOVEMENT_SPEED * -1

            if x_offset != 0:
                if b.movement == -1:
                    x_offset = x_offset * -1
                    edge = -640 * scale_factor_X
                    distance_from_edge = edge - (b.boss.xcor() + x_offset)
                    if distance_from_edge > 0:
                        x_offset = x_offset + (2 * distance_from_edge)
                else:
                    edge = 640 * scale_factor_X
                    distance_from_edge = edge - (b.boss.xcor() + x_offset)
                    if distance_from_edge < 0:
                        x_offset = x_offset + (2 * distance_from_edge)

            b.x_range = (b.boss.xcor() + x_offset - self.BOSS_DISTANCE, b.boss.xcor() + x_offset + self.BOSS_DISTANCE)

            collision_y_coordinate = self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (intersection_time[0] * -1 + self.float_time_offset)) / self.PERIOD) + \
                self.initial_distance + \
                self._machine_player.current_player[0].laser.ycor()

            b.collision_y_coordinate = collision_y_coordinate

    def time_equation(self, t):
        return (self.FLOAT_AMPLITUDE * math.sin((2 * math.pi * (t + self.float_time_offset)) / self.PERIOD)) - (self.laser_speed * t + self.initial_distance)

    def calculate_time(self):
        initial_guess = 1
        return fsolve(self.time_equation, initial_guess)
