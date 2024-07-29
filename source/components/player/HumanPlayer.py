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
    File: HumanPlayer.py
    Author: Christian Marinkovich
    Date: 2024-07-07
    Description:
    This file contains the logic related to the player in Alien Mode.
    The player moves left and right based on the controls and fires a red laser at fast speed. The player
        can also jump in both directions.
    The player has 10 health and has a 1.5 second long death animation.
    The player is supposed to be a human figure with an oxygen tank attached to him.
"""

import turtle
import pygame
import math
import time
from components.player.HumanLaser import HumanLaser
from setup.ModeSetupMaster import alien_mode_setup
from setup.TextureSetup import HUMAN_STILL_RIGHT_TEXTURE
from setup.TextureSetup import HUMAN_STILL_LEFT_TEXTURE
from setup.TextureSetup import HUMAN_WALKING_RIGHT_TEXTURE
from setup.TextureSetup import HUMAN_WALKING_LEFT_TEXTURE
from setup.TextureSetup import OXYGEN_TANK_TEXTURE
from setup.TextureSetup import PLAYER_DEATH_1_TEXTURE
from setup.TextureSetup import PLAYER_DEATH_2_TEXTURE
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


class Human:
    """
        Represents a player in Alien Mode. The player is controlled based on the key controls and fires a red laser.

        Attributes:
            player (turtle.Turtle()): The player sprite
            oxygen_tank (turtle.Turtle()): The players oxygen tank sprite
            gun (turtle.Turtle()): The player gun sprite
            laser (turtle.Turtle()): The player laser sprite
            health_bar (turtle.Turtle()): The players health bar sprite
            initial_velocity (float): The players initial velocity when starting a jump.
            current_velocity (float): The players current velocity during a jump (Set to initial when jump is not\
                being preformed)
            death_animation (int): Determines whether the player is currently in the process of dying or not
            death_iterator (float): Iterates during the players death animation
            health (int): Stores the players current health
            hit_delay (int): Iterates during the players hit delay and creates a delay between hits
            direction (int): Determines the current direction of the player (1 = right and 2 = left)
            gun_direction (int): Determines the current direction of the players gun (1 = right and 2 = left)
            jump_direction (int): Determines the direction that the player is jumping (1 = right and 2 = left)
            move_update (int): Determines if the player is currently moving
            jump_update (int): Determines if the player is currently jumping
            shoot_update (int): Determines if the players laser has been fired and is on the screen
            laser_direction (int): Determines the direction that the laser is moving (1 = right and 2 = left)
            Start_X (float): The x-coordinate starting point when the player begins to move right or left
            Start_Y (float): The y-coordinate starting point when the player jumps
            move_right (int): Set to 1 when the player is to preform a rightward movement
            move_left (int): Set to 1 when the player is to preform a leftward movement
            moving_right (int): Set to 1 when the player is in the process of moving right
            moving_left (int): Set to 1 when the player is in the process of moving left
            do_jump (int): Set to 1 when the play is to jump
            kill_start_time (float): Used as a timestamp for the death animation of the player (To make the animation
                run in a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the player (To make the movement
                happen in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit duration of the player (To make sure that the hit
                delay is constant)
            jump_start_time (float): Used as a timestamp for the jump duration of the player (To make sure that the
                time it takes to jump stays consistent)
            move_start_time (float): Used as a timestamp for the players movement (To make the players movement
                happen in a consistent amount of time and not based on code execution speed)
            walk_start_time (float): Used as a timestamp for the players walking texture update (To make sure the
                walking animation happens in a consistent amount of time)
            gun_start_time (float): Used as a timestamp for updating the guns texture when the player changes
                direction (To make sure it stays consistent with frame rate)
    """

    def __init__(self, god_mode, scale_factor_x, scale_factor_y):
        """
            Creates a human object and spawns it on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.player = turtle.Turtle()
        self.player.shape(HUMAN_STILL_RIGHT_TEXTURE)
        self.player.shapesize(4 * scale_factor_y, 2 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.player.penup()
        self.player.goto(0, -141 * scale_factor_y)
        self.player.direction = "stop"

        self.oxygen_tank = turtle.Turtle()
        self.oxygen_tank.shape(OXYGEN_TANK_TEXTURE)
        self.oxygen_tank.shapesize(1.5 * scale_factor_y, 0.75 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.oxygen_tank.penup()
        self.oxygen_tank.goto(self.player.xcor() - 30.5 * scale_factor_x, self.player.ycor() + 11 * scale_factor_y)
        self.oxygen_tank.direction = "stop"

        self.gun = turtle.Turtle()
        self.gun.shape(alien_mode_setup.gun_right_texture)
        self.gun.shapesize(0.67 * scale_factor_y, 2 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.gun.penup()
        self.gun.goto(self.player.xcor(), self.player.ycor() + 12 * scale_factor_y)
        self.gun.direction = "stop"
        self.gun.hideturtle()

        self.laser_list = []
        self.all_laser_list = []

        for i in range(alien_mode_setup.laser_count):
            laser = HumanLaser(self.gun.xcor(), self.gun.ycor(), scale_factor_x, scale_factor_y)
            laser.laser.hideturtle()
            self.laser_list.append(laser)
            self.all_laser_list.append(laser)

        self.health_bar = turtle.Turtle()
        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        self.health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.health_bar.penup()
        self.health_bar.goto(531 * scale_factor_x, 339 * scale_factor_y)
        # If god mode is on, the health bar is not visible
        if god_mode == 1:
            self.health_bar.hideturtle()

        self.laser_count = alien_mode_setup.laser_count

        self.initial_velocity = 23.84848 * scale_factor_y
        self.current_velocity = 23.84848 * scale_factor_y

        self.death_animation = 0
        self.death_iterator = 0
        self.health = 10
        self.hit_delay = 0
        self.direction = 0
        self.gun_direction = 0
        self.jump_direction = 0
        self.move_update = 0
        self.jump_update = 0
        self.shoot_update = 0
        self.laser_direction = 0
        self.laser_fire = 0
        self.laser_start_X = 0
        self.Start_X = 0
        self.Start_Y = 0
        self.move_right = 0
        self.move_left = 0
        self.moving_right = 0
        self.moving_left = 0
        self.do_jump = 0
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.jump_start_time = 0
        self.move_start_time = 0
        self.walk_start_time = 0
        self.gun_start_time = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.player.clear()
        self.oxygen_tank.clear()
        self.gun.clear()
        for l in self.laser_list:
            l.remove()
            del l
        self.laser_list.clear()
        self.all_laser_list.clear()
        self.health_bar.clear()
        del self.player
        del self.oxygen_tank
        del self.gun
        del self.laser_list
        del self.health_bar
        del self.laser_list
        del self.all_laser_list

    def reinstate(self, god_mode):
        """
            Reuses the existing sprite to spawn a human player on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :return: None
        """

        self.player.shape(HUMAN_STILL_RIGHT_TEXTURE)
        self.player.goto(0, -141 * self.scale_factor_y)
        self.player.direction = "stop"
        self.player.showturtle()

        self.oxygen_tank.shape(OXYGEN_TANK_TEXTURE)
        self.oxygen_tank.goto(self.player.xcor() - 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
        self.oxygen_tank.direction = "stop"
        self.oxygen_tank.showturtle()

        self.gun.shape(alien_mode_setup.gun_right_texture)
        self.gun.goto(self.player.xcor(), self.player.ycor() + 12 * self.scale_factor_y)
        self.gun.direction = "stop"

        self.laser_count = alien_mode_setup.laser_count

        if self.laser_count >= len(self.all_laser_list):
            for l in self.all_laser_list:
                l.reinstate(self.gun.xcor(), self.gun.ycor())
                self.laser_list.append(l)

            remaining_lasers = self.laser_count - len(self.all_laser_list)
            for i in range(remaining_lasers):
                laser = HumanLaser(self.gun.xcor(), self.gun.ycor(), self.scale_factor_x, self.scale_factor_y)
                self.laser_list.append(laser)
                self.all_laser_list.append(laser)
        else:
            for i in range(self.laser_count):
                self.all_laser_list[i].reinstate(self.gun.xcor(), self.gun.ycor())
                self.laser_list.append(self.all_laser_list[i])

        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        # If god mode is off, show the health bar
        if god_mode == 0:
            self.health_bar.showturtle()

    def get_player(self):
        """
            Returns the human player sprite so that its class attributes can be accessed.

            :return: player: The human player sprite
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

    def get_death_animation(self):
        """
            Returns the death animation indicator variable of the human player

            :return: death_animation: The death animation indicator variable
            :type: int
        """

        return self.death_animation

    def get_death_iterator(self):
        """
            Returns the death animation update value of the human player

            :return: update: the death animation update value of the human player
            :type: float
        """

        return self.death_iterator

    def get_hit_delay(self):
        """
            Returns the hit delay value of the human player

            :return: hit_delay: the hit delay value of the player
            :type: int
        """

        return self.hit_delay

    def get_health(self):
        """
            Returns the current health of the human player

            :return: health: The current health of the human player
            :type: int
        """

        return self.health

    def remove(self):
        """
            Removes the human player sprite form the screen and resets its attributes.

            :return: None
        """

        self.player.hideturtle()
        self.oxygen_tank.hideturtle()
        self.gun.hideturtle()
        self.health_bar.hideturtle()
        for l in self.laser_list:
            l.remove()
        self.laser_list.clear()
        self.laser_count = 0
        self.current_velocity = 23.84848 * self.scale_factor_y
        self.death_animation = 0
        self.death_iterator = 0
        self.health = 10
        self.hit_delay = 0
        self.direction = 0
        self.gun_direction = 0
        self.jump_direction = 0
        self.move_update = 0
        self.jump_update = 0
        self.shoot_update = 0
        self.laser_direction = 0
        self.laser_fire = 0
        self.laser_start_X = 0
        self.Start_X = 0
        self.Start_Y = 0
        self.move_right = 0
        self.move_left = 0
        self.moving_right = 0
        self.moving_left = 0
        self.do_jump = 0
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.jump_start_time = 0
        self.move_start_time = 0
        self.walk_start_time = 0
        self.gun_start_time = 0

    def go_right(self):
        """
            Sets the players direction to right and initializes the players rightward movement

            :return: None
        """

        # If the player is not already moving, jumping, dying, or off the screen
        if self.move_update == 0 and self.jump_update == 0 and self.player.xcor() < 640 * self.scale_factor_x and self.death_animation == 0 and self.move_right != 1:
            self.move_left = 0
            # Set the direction to right
            self.player.direction = "right"
            self.gun.direction = "right"
            self.direction = 1
            self.gun_direction = 1
            self.gun.goto(self.player.xcor() + alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
            self.gun.showturtle()
            # Mark the starting point
            self.Start_X = self.player.xcor()
            self.move_right = 1
            self.move_start_time = time.time()

    def go_left(self):
        """
            Sets the players direction to left and initializes the players leftward movement

            :return: None
        """

        # If the player is not already moving, jumping, dying, or off the screen
        if self.move_update == 0 and self.jump_update == 0 and self.player.xcor() > -640 * self.scale_factor_x and self.death_animation == 0 and self.move_left != 1:
            self.move_right = 0
            # Set the direction to left
            self.player.direction = "left"
            self.gun.direction = "left"
            self.direction = 2
            self.gun_direction = 2
            self.gun.goto(self.player.xcor() - alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
            self.gun.showturtle()
            # Mark the starting point
            self.Start_X = self.player.xcor()
            self.move_left = 1
            self.move_start_time = time.time()

    def jump(self):
        """
            Prepares the player to preform a jump in the given direction

            :return: None
        """

        # If the player is not already jumping and is facing a direction
        if self.jump_update == 0 and self.direction != 0 and self.do_jump == 0:
            # If the player is not going out of bounds
            if (self.direction == 1 and self.player.xcor() < 640 * self.scale_factor_x) or (self.direction == 2 and self.player.xcor() > -640 * self.scale_factor_x):
                # Prepare the player for a jump
                self.Start_Y = self.player.ycor()
                self.Start_X = self.player.xcor()
                self.do_jump = 1
                self.jump_start_time = time.time()

    def shoot(self, shooting_sound):
        """
            Fires a laser from the players gun in the given direction that will fly across the screen

            :param shooting_sound: Variable that determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :return: None
        """

        # If the player is facing right
        if self.direction == 1:
            # Shoot to the right
            self.laser_direction = 1
            for l in self.laser_list:
                l.laser.setx(self.gun.xcor() + alien_mode_setup.laser_offset)
                l.laser.sety(self.gun.ycor() + 5 * self.scale_factor_y)
                l.laser.shape(alien_mode_setup.laser_right_texture)
                l.laser_update = 0
            if len(self.laser_list) > 1:
                self.laser_start_X = self.laser_list[0].laser.xcor()
                self.laser_list[1].laser_update = 100
            if shooting_sound == 1:
                sound = pygame.mixer.Sound("Sound/Laser_Gun_Player.wav")
                sound.play()
            self.laser_fire = 0
            self.laser_start_time = time.time()
        # If the player is facing left
        elif self.direction == 2:
            # Shoot to the left
            self.laser_direction = 2
            for l in self.laser_list:
                l.laser.setx(self.gun.xcor() - alien_mode_setup.laser_offset)
                l.laser.sety(self.gun.ycor() + 5 * self.scale_factor_y)
                l.laser.shape(alien_mode_setup.laser_left_texture)
                l.laser_update = 0
            if len(self.laser_list) > 1:
                self.laser_start_X = self.laser_list[0].laser.xcor()
                self.laser_list[1].laser_update = 100
            if shooting_sound == 1:
                sound = pygame.mixer.Sound("Sound/Laser_Gun_Player.wav")
                sound.play()
            self.laser_fire = 0
            self.laser_start_time = time.time()

    def execute_right_movement(self):
        """
            Move the player to the right 100 units in 0.012 seconds

            :return: None
        """

        # If the right movement has been initialized and the player is not dying
        if self.move_right == 1 and self.direction == 1 and self.death_animation == 0:
            # Move right in 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                self.move_update = 1
                if self.player.xcor() < (self.Start_X + 100 * self.scale_factor_x):
                    # Calculate the delta movement and add it as additional movement required
                    delta_movement = alien_mode_setup.player_movement * ((elapsed_time - 0.012) / 0.012)
                    self.player.setx(self.player.xcor() + alien_mode_setup.player_movement + delta_movement)
                    self.oxygen_tank.goto(self.player.xcor() - 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                    self.gun.goto(self.player.xcor() + alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                    self.moving_right = 1
                else:
                    # Once finished, reset the movement variables
                    self.moving_right = 0
                    self.move_right = 0
                self.move_update = 0
                self.move_start_time = time.time()

    def execute_left_movement(self):
        """
            Move the player to the left 100 units in 0.012 seconds

            :return: None
        """

        # If the left movement has been initialized and the player is not dying
        if self.move_left == 1 and self.direction == 2 and self.death_animation == 0:
            # Move left in 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                self.move_update = 1
                if self.player.xcor() > (self.Start_X - 100 * self.scale_factor_x):
                    # Calculate the delta movement and add it as additional movement required
                    delta_movement = alien_mode_setup.player_movement * ((elapsed_time - 0.012) / 0.012)
                    self.player.setx(self.player.xcor() - alien_mode_setup.player_movement - delta_movement)
                    self.oxygen_tank.goto(self.player.xcor() + 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                    self.gun.goto(self.player.xcor() - alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                    self.moving_left = 1
                else:
                    # Once finished, reset the movement variables
                    self.moving_left = 0
                    self.move_left = 0
                self.move_update = 0
                self.move_start_time = time.time()

    def execute_jump(self):
        """
            Executes the jump movement of the player in the specified direction based on the variable "direction"

            :return: None
        """

        # If the jump has been initialized
        if self.do_jump == 1 and self.death_animation == 0:
            self.jump_update = 1
            # If the direction is right
            if (self.direction == 1 and self.jump_direction == 0) or (self.jump_direction == 1):
                current_time = time.time()
                elapsed_time = current_time - self.jump_start_time
                if elapsed_time >= alien_mode_setup.jump_frequency:
                    # Find the delta time (How ,much more time has passed since 0.006 seconds)
                    delta_movement = (elapsed_time - alien_mode_setup.jump_frequency) / alien_mode_setup.jump_frequency
                    # Convert this value to an integer to get the whole number amounts of
                    #   "0.006 seconds" that have passed
                    delta_movement = int(delta_movement)
                    # Account for delta time in the jump by doing the right number of iterations in a row to ensure
                    #   that the jumps speed stays consistent
                    iterations = 1 + delta_movement
                    for i in range(iterations):
                        # Turn all the sprites to the right
                        self.jump_direction = 1
                        self.gun.direction = "right"
                        self.gun_direction = 1
                        # Move the player
                        self.player.sety(self.player.ycor() + self.current_velocity)
                        self.player.setx(self.player.xcor() + 7 * self.scale_factor_x)
                        self.oxygen_tank.goto(self.player.xcor() - 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                        self.gun.goto(self.player.xcor() + alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                        self.jump_start_time = time.time()
                        # Finding the new velocity:
                        # If the highest point has not been reached yet
                        if self.current_velocity > 0:
                            # Find the new velocity using the real world physics formula vf^2 = vi^2 + 2adx where
                            #   a is the force of gravity on the moon in real life and dx is the distance between the
                            #   starting point and the current player position
                            velocity_squared = self.initial_velocity ** 2 + 2 * (-1.625 * self.scale_factor_y) * abs(self.player.ycor() - self.Start_Y)
                            # Make sure there is no divide by zero error
                            if velocity_squared > 0:
                                self.current_velocity = math.sqrt(velocity_squared)
                            else:
                                self.current_velocity = 0
                        # if the highest point has already been reached
                        elif self.player.ycor() > self.Start_Y and self.current_velocity <= 0:
                            # Use the same formula as before, but acceleration is increasing this time (because the
                            #   player is moving down)
                            self.current_velocity = math.sqrt(2 * (1.625 * self.scale_factor_y) * (self.Start_Y + 175 * self.scale_factor_y) - self.player.ycor())
                            self.current_velocity = 0 - self.current_velocity
                        # The jump is finished
                        else:
                            # Reset the variables
                            self.jump_update = 0
                            self.jump_direction = 0
                            self.do_jump = 0
                            self.current_velocity = 23.84848 * self.scale_factor_y
                            self.player.sety(-141 * self.scale_factor_y)
                            self.oxygen_tank.goto(self.player.xcor() - 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                            self.gun.goto(self.player.xcor() + alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                            break
            # If the direction is left
            elif (self.direction == 2 and self.jump_direction == 0) or (self.jump_direction == 2):
                current_time = time.time()
                elapsed_time = current_time - self.jump_start_time
                if elapsed_time >= alien_mode_setup.jump_frequency:
                    # Same process as above to find the delta time
                    delta_movement = (elapsed_time - alien_mode_setup.jump_frequency) / alien_mode_setup.jump_frequency
                    delta_movement = int(delta_movement)
                    iterations = 1 + delta_movement
                    for i in range(iterations):
                        # Turn all the sprites to the left
                        self.jump_direction = 2
                        self.gun.direction = "left"
                        self.gun_direction = 2
                        # Move the player
                        self.player.sety(self.player.ycor() + self.current_velocity)
                        self.player.setx(self.player.xcor() - 7 * self.scale_factor_x)
                        self.oxygen_tank.goto(self.player.xcor() + 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                        self.gun.goto(self.player.xcor() - alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                        self.jump_start_time = time.time()
                        # Finding the new velocity:
                        # If the highest point has not been reached yet
                        if self.current_velocity > 0:
                            # Find the new velocity using the real world physics formula vf^2 = vi^2 + 2adx where
                            #   a is the force of gravity on the moon in real life and dx is the distance between the
                            #   starting point and the current player position
                            velocity_squared = self.initial_velocity ** 2 + 2 * (-1.625 * self.scale_factor_y) * abs(self.player.ycor() - self.Start_Y)
                            if velocity_squared > 0:
                                self.current_velocity = math.sqrt(velocity_squared)
                            else:
                                self.current_velocity = 0
                        # if the highest point has already been reached
                        elif self.player.ycor() > self.Start_Y and self.current_velocity <= 0:
                            # Use the same formula as before, but acceleration is increasing this time (because the
                            #   player is moving down)
                            self.current_velocity = math.sqrt(2 * (1.625 * self.scale_factor_y) * (self.Start_Y + 175 * self.scale_factor_y) - self.player.ycor())
                            self.current_velocity = 0 - self.current_velocity
                        # The jump is finished
                        else:
                            # Reset the variables
                            self.jump_update = 0
                            self.jump_direction = 0
                            self.do_jump = 0
                            self.current_velocity = 23.84848 * self.scale_factor_y
                            self.player.sety(-141 * self.scale_factor_y)
                            self.oxygen_tank.goto(self.player.xcor() + 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                            self.gun.goto(self.player.xcor() - alien_mode_setup.gun_offset, self.player.ycor() + 12 * self.scale_factor_y)
                            break

    def execute_shoot(self, yellow_power_up):
        """
            Move thr laser across the screen in the specified direction after it has been shot

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :return: None
        """
        # If the direction is right
        if -1080 * self.scale_factor_x < self.laser_list[0].laser.xcor() < 1080 * self.scale_factor_x and self.laser_direction == 1:
            self.shoot_update = 1
            for l in self.laser_list:
                if l.laser_update < alien_mode_setup.piercing:
                    l.laser.showturtle()
                l.laser.direction = "right"
            if len(self.laser_list) > 1 and self.laser_fire == 0 and self.laser_list[0].laser.xcor() >= self.laser_start_X + 100 * self.scale_factor_x:
                self.laser_fire = 1
                self.laser_list[1].laser_update = 0
            # Move the laser every 0.01 seconds
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            if elapsed_time >= 0.01:
                if yellow_power_up == 1:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = alien_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].laser.setx(self.laser_list[0].laser.xcor() + alien_mode_setup.yellow_power_up_speed + delta_movement)
                    else:
                        for l in self.laser_list:
                            l.laser.setx(l.laser.xcor() + alien_mode_setup.yellow_power_up_speed + delta_movement)
                else:
                    delta_movement = alien_mode_setup.laser_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].laser.setx(self.laser_list[0].laser.xcor() + alien_mode_setup.laser_speed + delta_movement)
                    else:
                        for l in self.laser_list:
                            l.laser.setx(l.laser.xcor() + alien_mode_setup.laser_speed + delta_movement)
                self.laser_start_time = time.time()
        # If the direction is left
        elif -1080 * self.scale_factor_x < self.laser_list[0].laser.xcor() < 1080 * self.scale_factor_x and self.laser_direction == 2:
            self.shoot_update = 1
            for l in self.laser_list:
                if l.laser_update < alien_mode_setup.piercing:
                    print(l.laser_update)
                    l.laser.showturtle()
                l.laser.direction = "left"
            if len(self.laser_list) > 1 and self.laser_fire == 0 and self.laser_list[0].laser.xcor() <= self.laser_start_X - 100 * self.scale_factor_x:
                self.laser_fire = 1
                self.laser_list[1].laser_update = 0
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            # Move the laser every 0.01 seconds
            if elapsed_time >= 0.01:
                if yellow_power_up == 1:
                    delta_movement = alien_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].laser.setx(self.laser_list[0].laser.xcor() - alien_mode_setup.yellow_power_up_speed - delta_movement)
                    else:
                        for l in self.laser_list:
                            l.laser.setx(l.laser.xcor() - alien_mode_setup.yellow_power_up_speed - delta_movement)
                else:
                    delta_movement = alien_mode_setup.laser_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].laser.setx(self.laser_list[0].laser.xcor() - alien_mode_setup.laser_speed - delta_movement)
                    else:
                        for l in self.laser_list:
                            l.laser.setx(l.laser.xcor() - alien_mode_setup.laser_speed - delta_movement)
                self.laser_start_time = time.time()
        # If the laser has finished moving
        else:
            # reset the variables
            self.shoot_update = 0
            for l in self.laser_list:
                l.laser.hideturtle()
                #l.laser_update = 0

    def set_player_texture(self, right_update, left_update):
        """
            Sets the players texture based on the players direction and creates a walking animation when the
                player is walking.

            :param right_update: Used to update the walking right animation correctly
            :type right_update: float

            :param left_update: Used to update the walking left animation correctly
            :type left_update: float

            :return: None
        """

        # Updates the walking animation every 0.005 seconds
        current_time = time.time()
        elapsed_time = current_time - self.walk_start_time
        if elapsed_time >= 0.005:
            # If the players direction is right
            if self.direction == 1 and self.death_animation == 0:
                # Make the player face and walk right
                if (self.moving_right == 1 and right_update % 0.5 != 0) or self.jump_update == 1:
                    self.player.shape(HUMAN_WALKING_RIGHT_TEXTURE)
                else:
                    self.player.shape(HUMAN_STILL_RIGHT_TEXTURE)
            # If the players direction is left
            elif self.direction == 2 and self.death_animation == 0:
                # Make the player face and walk left
                if (self.moving_left == 1 and left_update % 0.5 != 0) or self.jump_update == 1:
                    self.player.shape(HUMAN_WALKING_LEFT_TEXTURE)
                else:
                    self.player.shape(HUMAN_STILL_LEFT_TEXTURE)
            self.walk_start_time = time.time()

    def set_gun_texture(self):
        """
            Sets the player guns texture based on the direction that the player is facing

            :return: None
        """

        # Change the guns texture every 0.005 seconds
        current_time = time.time()
        elapsed_time = current_time - self.gun_start_time
        if elapsed_time >= 0.005:
            # If the players direction is right, make the gun face right
            if self.gun_direction == 1:
                self.gun.shape(alien_mode_setup.gun_right_texture)
            # If the players direction is left, make the gun face left
            elif self.gun_direction == 2:
                self.gun.shape(alien_mode_setup.gun_left_texture)
            self.gun_start_time = time.time()

    def kill_player(self, death_sound):
        """
            Kills the human player and plays the human players death animation. After that, it spawns the player back
                at thecenter and resets the game.

            :param death_sound: Determines if the death sound for the player is toggled on or off
            :type death_sound: int

            :return: None
        """

        if self.death_animation == 1:
            if 0 < self.death_iterator < 2:
                # Wait 0.1 seconds
                current_time = time.time()
                elapsed_time = current_time - self.kill_start_time
                if elapsed_time >= 0.1:
                    self.death_iterator = 2
                    self.kill_start_time = 0
            elif 2 <= self.death_iterator < 3:
                self.death_iterator = 3
            elif self.death_iterator == 3:
                # Change the players texture to the second frame of the explosion
                self.player.shape(PLAYER_DEATH_2_TEXTURE)
                self.death_iterator = self.death_iterator + 0.125
                self.kill_start_time = time.time()
            elif 3 < self.death_iterator < 5:
                # wait 0.15 seconds
                current_time = time.time()
                elapsed_time = current_time - self.kill_start_time
                if elapsed_time >= 0.15:
                    self.death_iterator = 5
                    self.kill_start_time = 0
            elif 5 <= self.death_iterator < 6:
                self.death_iterator = 6
            elif self.death_iterator == 6:
                # Reset the players health to 10
                self.health = 10
                self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
                # Move the player back to the center of the screen
                self.player.goto(0, -141 * self.scale_factor_y)
                self.oxygen_tank.goto(self.player.xcor() - 30.5 * self.scale_factor_x, self.player.ycor() + 11 * self.scale_factor_y)
                self.gun.goto(self.player.xcor(), self.player.ycor() + 12 * self.scale_factor_y)
                self.oxygen_tank.showturtle()
                # Reset the players texture and all related variables
                self.player.shape(HUMAN_STILL_RIGHT_TEXTURE)
                self.player.direction = "stop"
                self.direction = 0
                self.death_iterator = 0
                self.death_animation = 0
                self.do_jump = 0
                self.jump_update = 0
                self.jump_direction = 0
                self.current_velocity = 23.84848 * self.scale_factor_y
                self.moving_left = 0
                self.moving_right = 0
                self.move_left = 0
                self.move_right = 0
                return

        if self.health == 1 and self.death_animation != 1:
            # The players health goes down to 0
            self.health = 0
            for l in self.laser_list:
                l.laser_update = 20
            # Set the players texture to the first frame of the explosion
            self.player.shape(PLAYER_DEATH_1_TEXTURE)
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Player_Death_Sound.wav")
                sound.play()
            self.oxygen_tank.hideturtle()
            self.gun.hideturtle()
            self.death_iterator = 0.125
            self.death_animation = 1
            self.kill_start_time = time.time()
            return

    def hit_player(self, hit_sound):
        """
            Makes the human player take "one hit" of damage and creates a hit delay before the player can be hit again

            :param hit_sound: Determines if the player hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        if self.hit_delay == 10:
            # Reset the hit delay variable
            self.hit_delay = 0
            return

        if self.hit_delay == 3:
            # Wait 0.5 seconds
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.5:
                self.hit_delay = 10
                self.hit_start_time = 0
            return

        if self.hit_delay == 2:
            self.hit_delay = 3

        if self.hit_delay == 1:
            # Update the players health bar
            if self.health == 9:
                self.health_bar.shape(HEALTH_BAR_910_TEXTURE)
            elif self.health == 8:
                self.health_bar.shape(HEALTH_BAR_810_TEXTURE)
            elif self.health == 7:
                self.health_bar.shape(HEALTH_BAR_710_TEXTURE)
            elif self.health == 6:
                self.health_bar.shape(HEALTH_BAR_610_TEXTURE)
            elif self.health == 5:
                self.health_bar.shape(HEALTH_BAR_510_TEXTURE)
            elif self.health == 4:
                self.health_bar.shape(HEALTH_BAR_410_TEXTURE)
            elif self.health == 3:
                self.health_bar.shape(HEALTH_BAR_310_TEXTURE)
            elif self.health == 2:
                self.health_bar.shape(HEALTH_BAR_210_TEXTURE)
            elif self.health == 1:
                self.health_bar.shape(HEALTH_BAR_110_TEXTURE)
            self.hit_delay = self.hit_delay + 1
            self.hit_start_time = time.time()
            return

        if self.hit_delay == 0 and self.death_animation == 0:
            # Decrease the players health by 1
            self.health = self.health - 1
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Player_Hit_Sound.wav")
                sound.play()
            self.hit_delay = 1
            return
