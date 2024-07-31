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
    File: MachinePlayer.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to the player in Machine Mode.
    The player moves left and right based on the controls and fires a green laser at fast speed.
    The player has 10 health and has a 1.5 second long death animation.
    The player is supposed to a be a cylinder laser gun that is sticking out of a ship that we cannot see in the frame.
"""

import turtle
import pygame
import time
from components.player.MachinePlayerLaser import MachineLaser
#vfrom physics.CollisionMaster import machine_collision
from setup.ModeSetupMaster import machine_mode_setup
from setup.TextureSetup import EXPLOSION_1_TEXTURE
from setup.TextureSetup import EXPLOSION_2_TEXTURE
from setup.TextureSetup import HEALTH_BAR_1010_TEXTURE
from setup.TextureSetup import HEALTH_BAR_910_TEXTURE
from setup.TextureSetup import HEALTH_BAR_810_TEXTURE
from setup.TextureSetup import HEALTH_BAR_710_TEXTURE
from setup.TextureSetup import HEALTH_BAR_610_TEXTURE
from setup.TextureSetup import HEALTH_BAR_510_TEXTURE
from setup.TextureSetup import HEALTH_BAR_410_TEXTURE
from setup.TextureSetup import HEALTH_BAR_310_TEXTURE
from setup.TextureSetup import HEALTH_BAR_210_TEXTURE
from setup.TextureSetup import HEALTH_BAR_110_TEXTURE


class Player:
    """
        Represents a player in Machine Mode. The player is controlled based on controls and fires a green laser.

        Attributes:
            player (turtle.Turtle()): The player sprite
            laser (turtle.Turtle()): The player laser sprite
            health_bar (turtle.Turtle()): The players health bar sprite
            death_animation (int): determines whether the player is currenly in the process of dying or not
            health_bar_indicator (int): Stores the current health of the player
            hit_delay (int): Delays how often the player can be hit
            update (float): Value that is incremented during the death animation of the player.
            direction (int): Stores the direction of the player (1 = right and 2 = left)
            laser_has_attacked (int): Determines whether the players laser has hit an enemy since it was fired.
            kill_start_time (float): Used as a timestamp for the death animation of the player (To make the animation
                run in a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the player (To make the movement
                happen in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit duration of the player (To make sure that the hit
                delay is constant)
    """

    def __init__(self, god_mode, scale_factor_x, scale_factor_y):
        """
            Creates a player object and spawns it on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.player = turtle.Turtle()
        self.player.shape(machine_mode_setup.player_texture)
        self.player.shapesize(5, 2)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.player.penup()
        self.player.goto(0, -300 * scale_factor_y)

        self.laser_count = machine_mode_setup.laser_count

        self.laser_list = []
        self.all_laser_list = []
        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count

        for i in range(machine_mode_setup.laser_count):
            laser = MachineLaser(0, machine_mode_setup.laser_max_distance)
            self.laser_list.append(laser)
            self.all_laser_list.append(laser)

        self.do_collision = 0

        self.health_bar = turtle.Turtle()
        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.health_bar.penup()
        self.health_bar.shapesize(1, 1)
        self.health_bar.goto(531 * scale_factor_x, 339 * scale_factor_y)
        # If god mode is on, the health bar is not visible
        if god_mode == 1:
            self.health_bar.hideturtle()

        self.death_animation = 0
        self.health_bar_indicator = 10
        self.hit_delay = 0
        self.update = 0
        self.direction = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.player.clear()
        # self.laser.clear()
        for l in self.laser_list:
            l.remove()
            del l
        self.laser_list.clear()
        self.all_laser_list.clear()
        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.health_bar.clear()
        del self.player
        # del self.laser
        del self.health_bar
        del self.laser_list
        del self.all_laser_list
        del self.laser_start_y_list
        del self.laser_has_attacked_list
        del self.lasers_fired_list

    def reinstate(self, god_mode):
        """
            Reuses the existing sprite to spawn a player on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :return: None
        """

        self.player.shape(machine_mode_setup.player_texture)
        self.player.goto(0, -300 * self.scale_factor_y)
        self.player.direction = "stop"
        self.player.showturtle()

        self.laser_count = machine_mode_setup.laser_count

        if self.laser_count >= len(self.all_laser_list):
            for l in self.all_laser_list:
                l.reinstate(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(l)

            remaining_lasers = self.laser_count - len(self.all_laser_list)
            for i in range(remaining_lasers):
                laser = MachineLaser(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(laser)
                self.all_laser_list.append(laser)
        else:
            for i in range(self.laser_count):
                self.all_laser_list[i].reinstate(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(self.all_laser_list[i])

        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count

        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        if god_mode == 0:
            self.health_bar.showturtle()

    def get_player(self):
        """
            Returns the player sprite so that its class attributes can be accessed.

            :return: player: The player sprite
            :type: Turtle.turtle()
        """

        return self.player

    def get_laser(self):
        """
            Returns the players laser sprite so that its class attributes can be accessed

            :return: laser: The player laser sprite
            :type: turtle.Turtle()
        """

        return self.laser_list

    def get_health_bar(self):
        """
            Returns the players health bar sprite so that its class attributes can be accessed

            :return: health_bar: The players health bar sprite
            :type: turtle.Turtle()
        """

        return self.health_bar

    def get_player_death_update(self):
        """
            Returns the death animation update value of the player

            :return: update: the death animation update value of the player
            :type: float
        """

        return self.update

    def get_death_animation(self):
        """
            Returns the death animation indicator variable of the player

            :return: death_animation: The death animation indicator variable
            :type: int
        """

        return self.death_animation

    def get_hit_delay(self):
        """
            Returns the hit delay value of the player

            :return: hit_delay: the hit delay value of the player
            :type: int
        """

        return self.hit_delay

    def get_health_bar_indicator(self):
        """
            Returns the health of the player

            :return: health_bar_indicator: The current health of the player
            :type: int
        """

        return self.health_bar_indicator

    def get_laser_has_attacked(self):
        """
            Returns whether the laser has hit an enemy since it was last fired

            :return: laser_last_attacked: Determines whether the player laser has hit an enemy since it was last fired
            :type: int
        """

        return self.laser_has_attacked_list

    def set_laser_has_attacked(self, new_value, index):
        """
            Sets the laser_has_attacked of the player (Used for when the player hits an enemy)

            :param new_value: The new laser_has_attacked of the yellow machine.
            :type new_value: int

            :return: None
        """

        self.laser_has_attacked_list[index] = new_value

    def remove(self):
        """
            Removes the player sprite form the screen and resets its attributes.

            :return: None
        """

        self.player.hideturtle()
        for l in self.laser_list:
            l.remove()
        self.laser_list.clear()
        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.laser_count = 0
        self.do_collision = 0
        self.health_bar.hideturtle()
        self.death_animation = 0
        self.hit_delay = 0
        self.health_bar_indicator = 10
        self.update = 0
        # self.laser_has_attacked = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

    def remove_laser_start_y(self):
        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count
        self.laser_start_time = time.time()

    def set_direction_left(self):
        """
            Sets the players direction of movement to be left

            :return: None
        """

        self.player.direction = "left"
        self.direction = 1

    def set_direction_right(self):
        """
            Sets the players direction of movement to be right

            :return: None
        """

        self.player.direction = "right"
        self.direction = 2

    def move_player(self, yellow_power_up):
        """
            Moves the player in the direction specified by the "direction" variable

            :return: None
        """

        if self.direction == 1 and self.player.xcor() > -620 * self.scale_factor_x and self.death_animation == 0:
            if yellow_power_up == 1:
                self.player.setx(self.player.xcor() - machine_mode_setup.yellow_player_movement)
            else:
                self.player.setx(self.player.xcor() - machine_mode_setup.player_movement)

        if self.direction == 2 and self.player.xcor() < 620 * self.scale_factor_x and self.death_animation == 0:
            if yellow_power_up == 1:
                self.player.setx(self.player.xcor() + machine_mode_setup.yellow_player_movement)
            else:
                self.player.setx(self.player.xcor() + machine_mode_setup.player_movement)

    def fire(self, shooting_sound, index=0):
        """
            Fires the players laser by resetting it to its original position

            :param shooting_sound: Determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :return: None
        """

        self.laser_list[index].laser.showturtle()
        if shooting_sound == 1:
            sound = pygame.mixer.Sound("Sound/Laser_Gun_Player.wav")
            sound.play()
        # Moves the laser back to the player to be fired
        self.laser_list[index].laser.setx(self.player.xcor())
        self.laser_list[index].laser.sety(self.player.ycor() + machine_mode_setup.laser_offset)
        # self.laser_start_time = time.time()
        # self.laser_has_attacked = 0
        self.laser_start_y_list[index] = self.laser_list[index].laser.ycor()
        self.laser_has_attacked_list[index] = 0
        self.lasers_fired_list[index] = 1

        self.do_collision = index + 1

    def shoot(self, shooting_sound, yellow_power_up):
        """
            Moves the player's laser across the screen after it is fired

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :return: None
        """

        # If the laser has hit an enemy, remove it from the screen
        for i in range(len(self.laser_has_attacked_list)):
            if self.laser_has_attacked_list[i] == 1:
                self.laser_list[i].laser.hideturtle()

        if len(self.laser_list) > 2 and self.lasers_fired_list[1] != 0 and self.lasers_fired_list[2] == 0 and self.laser_list[1].laser.ycor() >= self.laser_start_y_list[1] + 100 * self.scale_factor_y:
            self.fire(shooting_sound, 2)

        if len(self.laser_list) > 1 and self.lasers_fired_list[1] == 0 and self.laser_list[0].laser.ycor() >= self.laser_start_y_list[0] + 100 * self.scale_factor_y:
            self.fire(shooting_sound, 1)

        # While the laser is still in the frame of the screen
        if self.laser_list[0].laser.ycor() < machine_mode_setup.laser_max_distance:
            # Keep moving it 14.5 or 43.5 units every 0.015 seconds
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            if elapsed_time >= 0.015:
                if yellow_power_up == 0:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = machine_mode_setup.laser_speed * ((elapsed_time - 0.015) / 0.015)
                    if len(self.lasers_fired_list) == 3 and self.lasers_fired_list[2] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[2].laser.sety(self.laser_list[2].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 2 and self.lasers_fired_list[1] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 1 or self.lasers_fired_list[1] == 0:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                elif yellow_power_up == 1:
                    delta_movement = machine_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.015) / 0.015)
                    if len(self.lasers_fired_list) == 3 and self.lasers_fired_list[2] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[2].laser.sety(self.laser_list[2].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 2 and self.lasers_fired_list[1] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 1 or self.lasers_fired_list[1] == 0:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                self.laser_start_time = time.time()
        else:
            for l in self.laser_list:
                l.laser.hideturtle()
            self.laser_start_time = 0

    def kill_player(self, death_sound):
        """
            Kills the player and plays the players death animation. After that, it spawns the player back at the
                center and resets the game.

            :param death_sound: Determines if the death sound for the player is toggled on or off
            :type death_sound: int

            :return: None
        """

        no_kill = 0
        # Reveals the player sprite on the screen
        if self.update == 6:
            self.player.showturtle()
            self.update = 0
            self.death_animation = 0
            no_kill = 1

        # Wait 0.05 seconds
        if 4 <= self.update < 6:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.05:
                self.update = 6
                self.kill_start_time = 0

        # Resets the players health back to 10
        if self.update == 3.5:
            self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
            self.health_bar_indicator = 10
            self.update = 4
            self.kill_start_time = time.time()
            return

        # Respawns the player at the origin
        if self.update == 3:
            self.player.hideturtle()
            self.player.shape(machine_mode_setup.player_texture)
            self.player.goto(0, -300 * self.scale_factor_y)
            self.update = 3.5

        # Wait 0.15 seconds
        if 1.5 <= self.update < 3:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.15:
                self.update = 3
                self.kill_start_time = 0

        # Changes the players texture to the second frame of the explosion
        if 1.0 <= self.update <= 1.1:
            self.player.shape(EXPLOSION_2_TEXTURE)
            self.update = 1.5
            self.kill_start_time = time.time()

        # Wait 0.1 seconds
        if 0.5 <= self.update < 1:
            if self.update == 0.5:
                self.update = 0.6
            elif self.update == 0.6:
                self.update = 0.7
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.1:
                self.update = 1
                self.kill_start_time = 0

        if self.update == 0 and no_kill == 0:
            # Death animation is happening
            self.death_animation = 1
            self.health_bar_indicator = 0
            # Death sound plays
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion3.wav")
                sound.play()
            # Sets the players texture to the first frame of the explosion
            self.player.shape(EXPLOSION_1_TEXTURE)
            self.update = 0.5
            self.kill_start_time = time.time()

    def hit_player(self, hit_sound):
        """
            Makes the player take "one hit" of damage and creates a hit delay before the player can be hit again

            :param hit_sound: Determines if the player hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        # Reset the hit delay back to 0
        no_hit = 0
        if self.hit_delay == 39:
            self.hit_delay = 0
            no_hit = 1

        # Wait 0.5 seconds
        if 3 <= self.hit_delay < 39:
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.5:
                self.hit_delay = 39
                self.hit_start_time = 0

        if self.hit_delay == 2:
            self.hit_delay = 3

        if self.hit_delay == 1:
            self.hit_delay = 2

        if self.hit_delay == 0 and no_hit == 0 and self.update == 0:
            # Decrease the players health by 1
            if self.health_bar_indicator == 10:
                self.health_bar.shape(HEALTH_BAR_910_TEXTURE)
            elif self.health_bar_indicator == 9:
                self.health_bar.shape(HEALTH_BAR_810_TEXTURE)
            elif self.health_bar_indicator == 8:
                self.health_bar.shape(HEALTH_BAR_710_TEXTURE)
            elif self.health_bar_indicator == 7:
                self.health_bar.shape(HEALTH_BAR_610_TEXTURE)
            elif self.health_bar_indicator == 6:
                self.health_bar.shape(HEALTH_BAR_510_TEXTURE)
            elif self.health_bar_indicator == 5:
                self.health_bar.shape(HEALTH_BAR_410_TEXTURE)
            elif self.health_bar_indicator == 4:
                self.health_bar.shape(HEALTH_BAR_310_TEXTURE)
            elif self.health_bar_indicator == 3:
                self.health_bar.shape(HEALTH_BAR_210_TEXTURE)
            elif self.health_bar_indicator == 2:
                self.health_bar.shape(HEALTH_BAR_110_TEXTURE)
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion4.wav")
                sound.play()
            self.hit_delay = 1
            self.health_bar_indicator = self.health_bar_indicator - 1
            self.hit_start_time = time.time()
