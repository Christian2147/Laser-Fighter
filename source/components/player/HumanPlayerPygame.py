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

import pygame
import math
import time
from components.player.HumanLaserPygame import HumanLaser
from setup.ModeSetupMasterPygame import alien_mode_setup
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
from setup.TextureSetup import ARMOR_BAR_10_10_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_9_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_8_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_7_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_6_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_5_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_4_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_3_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_2_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_1_TEXTURE


class Human(pygame.sprite.Sprite):
    """
        Represents a player in Alien Mode. The player is controlled based on the key controls and fires a red laser.

        Attributes:
            oxygen_tank (turtle.Turtle()): The players oxygen tank sprite
            gun (turtle.Turtle()): The player gun sprite
            health_bar (turtle.Turtle()): The players health bar sprite
            armor_bar (turtle.Turtle()): The players armor bar sprite
            armor_created (int): Determines if the armor bar has already been created or not for the player

            laser_list (list): The list of the current lasers on the screen
            laser_count (int): The amount of lasers to be fired per round
            laser_direction (int): Determines the direction that the laser is moving and facing (1 = right and 2 = left)
            laser_fire (int): Determines if the second laser has been fired or not
            laser_start_X (float): The starting x-coordinate of the laser when it is fired

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

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
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

        super().__init__()
        self.image = pygame.image.load(HUMAN_STILL_RIGHT_TEXTURE)
        self.rect = self.image.get_rect()
        self.rect.center = (640 * scale_factor_x, 501 * scale_factor_y)
        self.human_visible = 1
        self.direction = "stop"

        self.oxygen_tank = OxygenTank(self.rect.centerx, self.rect.centery, self.scale_factor_x, self.scale_factor_y)

        self.gun = Gun(self.rect.centerx, self.rect.centery, self.scale_factor_x, self.scale_factor_y)

        # Set the laser list (For multiple lasers)
        self.laser_list = []

        # Initiate the amount of lasers needed
        for i in range(alien_mode_setup.laser_count):
            laser = HumanLaser(self.gun.rect.centerx, self.gun.rect.centery, scale_factor_x, scale_factor_y)
            laser.laser_visible = 0
            self.laser_list.append(laser)

        self.health_bar = HealthBar(god_mode, scale_factor_x, scale_factor_y)

        # If the shield is enabled, an armor bar is created in the top right corner of the screen
        if alien_mode_setup.health == 20:
            self.armor_bar = ArmorBar(god_mode, scale_factor_x, scale_factor_y)
            self.armor_created = 1
        else:
            self.armor_created = 0

        self.laser_count = alien_mode_setup.laser_count

        self.initial_velocity = 23.84848 * scale_factor_y
        self.current_velocity = 23.84848 * scale_factor_y

        self.death_animation = 0
        self.death_iterator = 0
        self.health = alien_mode_setup.health
        self.hit_delay = 0
        # self.direction = 0
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

        # Clean up lasers before clearing the list
        for l in self.laser_list:
            l.remove()
            del l
        self.laser_list.clear()
        # Check if the armor bar exists or not
        # If it does, delete it here
        if hasattr(self, 'armor'):
            del self.armor
        del self.oxygen_tank
        del self.gun
        del self.health_bar
        del self.laser_list
        self.kill()
        del self

    def get_player(self):
        """
            Returns the human player sprite so that its class attributes can be accessed.

            :return: player: The human player sprite
            :type: Turtle.turtle()
        """

        return self

    def get_laser(self):
        """
            Returns the list of the players laser sprites so that their class attributes can be accessed

            :return: laser_list: The list of the players laser sprites
            :type: list
        """

        return self.laser_list

    def get_health_bar(self):
        """
            Returns the players health bar sprite so that its class attributes can be accessed

            :return: health_bar: The players health bar sprite
            :type: turtle.Turtle()
        """

        return self.health_bar

    def get_armor_bar(self):
        """
            Returns the players armor bar sprite so that its class attributes can be accessed

            :return: armor_bar: The players armor bar sprite
            :type: turtle.Turtle()
        """

        return self.armor_bar

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

        self.human_visible = 0
        self.oxygen_tank.remove()
        self.gun.remove()
        self.health_bar.remove()
        for l in self.laser_list:
            l.remove()
        # If the armor bar was created, remove it from the screen
        if self.armor_created == 1:
            self.armor_bar.remove()
        self.laser_list.clear()
        self.laser_count = 0
        self.current_velocity = 23.84848 * self.scale_factor_y
        self.death_animation = 0
        self.death_iterator = 0
        self.health = alien_mode_setup.health
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
        if self.move_update == 0 and self.jump_update == 0 and self.rect.centerx < 1280 * self.scale_factor_x and self.death_animation == 0 and self.move_right != 1:
            self.move_left = 0
            # Set the direction to right
            self.direction = "right"
            self.gun.direction = "right"
            # self.direction = 1
            self.gun_direction = 1
            self.gun.rect.center = (self.rect.centerx + alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
            self.gun.gun_visible = 1
            # Mark the starting point
            self.Start_X = self.rect.centerx
            self.move_right = 1
            self.move_start_time = time.time()

    def go_left(self):
        """
            Sets the players direction to left and initializes the players leftward movement

            :return: None
        """

        # If the player is not already moving, jumping, dying, or off the screen
        if self.move_update == 0 and self.jump_update == 0 and self.rect.centerx > 0 * self.scale_factor_x and self.death_animation == 0 and self.move_left != 1:
            self.move_right = 0
            # Set the direction to left
            self.direction = "left"
            self.gun.direction = "left"
            # self.direction = 2
            self.gun_direction = 2
            self.gun.rect.center = (self.rect.centerx - alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
            self.gun.gun_visible = 1
            # Mark the starting point
            self.Start_X = self.rect.centerx
            self.move_left = 1
            self.move_start_time = time.time()

    def jump(self):
        """
            Prepares the player to preform a jump in the given direction

            :return: None
        """

        # If the player is not already jumping and is facing a direction
        if self.jump_update == 0 and self.direction != "stop" and self.do_jump == 0:
            # If the player is not going out of bounds
            if (self.direction == "right" and self.rect.centerx < 1280 * self.scale_factor_x) or (self.direction == "left" and self.rect.centerx > 0 * self.scale_factor_x):
                # Prepare the player for a jump
                self.Start_Y = self.rect.centery
                self.Start_X = self.rect.centerx
                self.do_jump = 1
                self.jump_start_time = time.time()

    def shoot(self, shooting_sound):
        """
            Fires a laser from the players gun in the given direction that will fly across the screen.
            The amount of lasers fired depends on the laser count.

            :param shooting_sound: Variable that determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :return: None
        """

        # If the player is facing right
        if self.direction == "right":
            # Shoot to the right
            self.laser_direction = 1
            # Prepare all of the lasers in the current list to be fired
            for l in self.laser_list:
                l.laser.setx(self.gun.rect.centerx + alien_mode_setup.laser_offset)
                l.laser.sety(self.gun.rect.centery - 5 * self.scale_factor_y)
                # Set the texture to the laser facing right
                l.laser.shape(alien_mode_setup.laser_right_texture)
                l.laser_update = 0
            # If there is more than 1 laser (Can only be 2, not 3), then halt the second laser.
            if len(self.laser_list) > 1:
                self.laser_start_X = self.laser_list[0].rect.centerx
                self.laser_list[1].laser_update = 100
            if shooting_sound == 1:
                sound = pygame.mixer.Sound("sound/Laser_Gun_Player.wav")
                sound.play()
            # Ensure that the second laser is not fired right when the first one is
            self.laser_fire = 0
            self.laser_start_time = time.time()
        # If the player is facing left
        elif self.direction == "left":
            # Shoot to the left
            self.laser_direction = 2
            # Prepare all of the lasers in the current list to be fired
            for l in self.laser_list:
                l.laser.setx(self.gun.rect.centerx - alien_mode_setup.laser_offset)
                l.laser.sety(self.gun.rect.centery - 5 * self.scale_factor_y)
                # Set the texture to the laser facing left
                l.laser.shape(alien_mode_setup.laser_left_texture)
                l.laser_update = 0
            # If there is more than 1 laser (Can only be 2, not 3), then halt the second laser.
            if len(self.laser_list) > 1:
                self.laser_start_X = self.laser_list[0].rect.centerx
                self.laser_list[1].laser_update = 100
            if shooting_sound == 1:
                sound = pygame.mixer.Sound("sound/Laser_Gun_Player.wav")
                sound.play()
            # Ensure that the second laser is not fired right when the first one is
            self.laser_fire = 0
            self.laser_start_time = time.time()

    def execute_right_movement(self, yellow_power_up):
        """
            Move the player to the right 100 units in 0.012 seconds

            :return: None
        """

        # If the right movement has been initialized and the player is not dying
        if self.move_right == 1 and self.direction == "right" and self.death_animation == 0:
            # Move right in 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            # How fast the player moves depends on if the yellow power up is activated or not
            player_movement = alien_mode_setup.player_movement
            if yellow_power_up == 1:
                player_movement = alien_mode_setup.yellow_player_movement
            if elapsed_time >= 0.012:
                self.move_update = 1
                if self.rect.centerx < (self.Start_X + 100 * self.scale_factor_x):
                    # Calculate the delta movement and add it as additional movement required
                    delta_movement = player_movement * ((elapsed_time - 0.012) / 0.012)
                    self.rect.centerx = self.rect.centerx + player_movement + delta_movement
                    self.oxygen_tank.center = (self.rect.centerx - 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                    self.gun.center = (self.rect.centerx + alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                    self.moving_right = 1
                else:
                    # Once finished, reset the movement variables
                    self.moving_right = 0
                    self.move_right = 0
                self.move_update = 0
                self.move_start_time = time.time()

    def execute_left_movement(self, yellow_power_up):
        """
            Move the player to the left 100 units in 0.012 seconds

            :return: None
        """

        # If the left movement has been initialized and the player is not dying
        if self.move_left == 1 and self.direction == "left" and self.death_animation == 0:
            # Move left in 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            # How fast the player moves depends on if the yellow power up is activated or not
            player_movement = alien_mode_setup.player_movement
            if yellow_power_up == 1:
                player_movement = alien_mode_setup.yellow_player_movement
            if elapsed_time >= 0.012:
                self.move_update = 1
                if self.rect.centerx > (self.Start_X - 100 * self.scale_factor_x):
                    # Calculate the delta movement and add it as additional movement required
                    delta_movement = player_movement * ((elapsed_time - 0.012) / 0.012)
                    self.rect.centerx = self.rect.centerx - player_movement - delta_movement
                    self.oxygen_tank.center = (self.rect.centerx + 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                    self.gun.center = (self.rect.centerx - alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                    self.moving_left = 1
                else:
                    # Once finished, reset the movement variables
                    self.moving_left = 0
                    self.move_left = 0
                self.move_update = 0
                self.move_start_time = time.time()

    def execute_jump(self, yellow_power_up):
        """
            Executes the jump movement of the player in the specified direction based on the variable "direction"

            :return: None
        """

        # If the jump has been initialized
        if self.do_jump == 1 and self.death_animation == 0:
            self.jump_update = 1
            # If the direction is right
            if (self.direction == "right" and self.jump_direction == 0) or (self.jump_direction == 1):
                current_time = time.time()
                elapsed_time = current_time - self.jump_start_time
                # How fast the player jumps depends on if the yellow power up is active or not
                jump_frequency = alien_mode_setup.jump_frequency
                if yellow_power_up == 1:
                    jump_frequency = alien_mode_setup.yellow_jump_frequency
                if elapsed_time >= jump_frequency:
                    # Find the delta time (How ,much more time has passed since 0.006 seconds)
                    delta_movement = (elapsed_time - jump_frequency) / jump_frequency
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
                        self.rect.centery = self.rect.centery - self.current_velocity # Changed this to a negative
                        self.rect.centerx = self.rect.centerx + 7 * self.scale_factor_x
                        self.oxygen_tank.center = (self.rect.centerx - 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                        self.gun.center = (self.rect.centerx + alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                        self.jump_start_time = time.time()
                        # Finding the new velocity:
                        # If the highest point has not been reached yet
                        if self.current_velocity > 0:
                            # Find the new velocity using the real world physics formula vf^2 = vi^2 + 2adx where
                            #   a is the force of gravity on the moon in real life and dx is the distance between the
                            #   starting point and the current player position
                            velocity_squared = self.initial_velocity ** 2 + 2 * (-1.625 * self.scale_factor_y) * abs(self.rect.centery - self.Start_Y)
                            # Make sure there is no divide by zero error
                            if velocity_squared > 0:
                                self.current_velocity = math.sqrt(velocity_squared)
                            else:
                                self.current_velocity = 0
                        # if the highest point has already been reached
                        elif self.rect.centery < self.Start_Y and self.current_velocity <= 0: # Changed the inequality sign
                            # Use the same formula as before, but acceleration is increasing this time (because the
                            #   player is moving down)
                            self.current_velocity = math.sqrt(2 * (1.625 * self.scale_factor_y) * (self.Start_Y - 175 * self.scale_factor_y) + self.rect.centery) # Changed to -175 and + self.rect.centery
                            self.current_velocity = 0 - self.current_velocity
                        # The jump is finished
                        else:
                            # Reset the variables
                            self.jump_update = 0
                            self.jump_direction = 0
                            self.do_jump = 0
                            self.current_velocity = 23.84848 * self.scale_factor_y
                            self.rect.centery = 501 * self.scale_factor_y
                            self.oxygen_tank.center = (self.rect.centerx - 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                            self.gun.center = (self.rect.centerx + alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                            break
            # If the direction is left
            elif (self.direction == "left" and self.jump_direction == 0) or (self.jump_direction == 2):
                current_time = time.time()
                elapsed_time = current_time - self.jump_start_time
                # How fast the player jumps depends on if the yellow power up is active or not
                jump_frequency = alien_mode_setup.jump_frequency
                if yellow_power_up == 1:
                    jump_frequency = alien_mode_setup.yellow_jump_frequency
                if elapsed_time >= jump_frequency:
                    # Same process as above to find the delta time
                    delta_movement = (elapsed_time - jump_frequency) / jump_frequency
                    delta_movement = int(delta_movement)
                    iterations = 1 + delta_movement
                    for i in range(iterations):
                        # Turn all the sprites to the left
                        self.jump_direction = 2
                        self.gun.direction = "left"
                        self.gun_direction = 2
                        # Move the player
                        self.rect.centery = self.rect.centery - self.current_velocity # Changed this to a negative
                        self.rect.centerx = self.rect.centerx - 7 * self.scale_factor_x
                        self.oxygen_tank.center = (self.rect.centerx + 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                        self.gun.center = (self.rect.centerx - alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                        self.jump_start_time = time.time()
                        # Finding the new velocity:
                        # If the highest point has not been reached yet
                        if self.current_velocity > 0:
                            # Find the new velocity using the real world physics formula vf^2 = vi^2 + 2adx where
                            #   a is the force of gravity on the moon in real life and dx is the distance between the
                            #   starting point and the current player position
                            velocity_squared = self.initial_velocity ** 2 + 2 * (-1.625 * self.scale_factor_y) * abs(self.rect.centery - self.Start_Y)
                            if velocity_squared > 0:
                                self.current_velocity = math.sqrt(velocity_squared)
                            else:
                                self.current_velocity = 0
                        # if the highest point has already been reached
                        elif self.rect.centery < self.Start_Y and self.current_velocity <= 0:
                            # Use the same formula as before, but acceleration is increasing this time (because the
                            #   player is moving down)
                            self.current_velocity = math.sqrt(2 * (1.625 * self.scale_factor_y) * (self.Start_Y - 175 * self.scale_factor_y) + self.rect.centery)
                            self.current_velocity = 0 - self.current_velocity
                        # The jump is finished
                        else:
                            # Reset the variables
                            self.jump_update = 0
                            self.jump_direction = 0
                            self.do_jump = 0
                            self.current_velocity = 23.84848 * self.scale_factor_y
                            self.rect.centery = 501 * self.scale_factor_y
                            self.oxygen_tank.center = (self.rect.centerx + 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                            self.gun.center = (self.rect.centerx - alien_mode_setup.gun_offset, self.rect.centery - 12 * self.scale_factor_y)
                            break

    def execute_shoot(self, shooting_sound, yellow_power_up):
        """
            Move the lasers across the screen in the specified direction after they have been shot

            :param shooting_sound: Variable that determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :return: None
        """

        # If the direction is right
        if -440 * self.scale_factor_x < self.laser_list[0].rect.centerx < 1720 * self.scale_factor_x and self.laser_direction == 1:
            self.shoot_update = 1
            # Set all necessary lasers to face right
            for l in self.laser_list:
                if l.laser_update < alien_mode_setup.piercing:
                    l.laser_visible = 1
                l.direction = "right"
            # Fire the second laser after the first one has travelled at least 100 units (To have a gap)
            if len(self.laser_list) > 1 and self.laser_fire == 0 and self.laser_list[0].rect.centerx >= self.laser_start_X + 100 * self.scale_factor_x:
                self.laser_fire = 1
                self.laser_list[1].laser_update = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("sound/Laser_Gun_Player.wav")
                    sound.play()
            # Move the laser every 0.01 seconds
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            if elapsed_time >= 0.01:
                # Check if the yellow power up is on
                if yellow_power_up == 1:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = alien_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.01) / 0.01)
                    # Check if the second laser has already been fired or not
                    if self.laser_fire == 0:
                        self.laser_list[0].rect.centerx = self.laser_list[0].rect.centerx + alien_mode_setup.yellow_power_up_speed + delta_movement
                    else:
                        for l in self.laser_list:
                            l.rect.centerx = l.rect.centerx + alien_mode_setup.yellow_power_up_speed + delta_movement
                else:
                    delta_movement = alien_mode_setup.laser_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].rect.centerx = self.laser_list[0].rect.centerx + alien_mode_setup.laser_speed + delta_movement
                    else:
                        for l in self.laser_list:
                            l.rect.centerx = l.rect.centerx + alien_mode_setup.laser_speed + delta_movement
                self.laser_start_time = time.time()
        # If the direction is left
        elif -440 * self.scale_factor_x < self.laser_list[0].rect.centerx < 1720 * self.scale_factor_x and self.laser_direction == 2:
            self.shoot_update = 1
            # Set all necessary lasers to face left
            for l in self.laser_list:
                if l.laser_update < alien_mode_setup.piercing:
                    l.laser_visible = 1
                l.direction = "left"
            # Fire the second laser after the first one has travelled at least 100 units (To have a gap)
            if len(self.laser_list) > 1 and self.laser_fire == 0 and self.laser_list[0].rect.centerx <= self.laser_start_X - 100 * self.scale_factor_x:
                self.laser_fire = 1
                self.laser_list[1].laser_update = 0
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            # Move the laser every 0.01 seconds
            if elapsed_time >= 0.01:
                # Check if the yellow power up is on
                if yellow_power_up == 1:
                    delta_movement = alien_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.01) / 0.01)
                    # Check if the second laser has already been fired or not
                    if self.laser_fire == 0:
                        self.laser_list[0].rect.centerx = self.laser_list[0].rect.centerx - alien_mode_setup.yellow_power_up_speed - delta_movement
                    else:
                        for l in self.laser_list:
                            l.rect.centerx = l.rect.centerx - alien_mode_setup.yellow_power_up_speed - delta_movement
                else:
                    delta_movement = alien_mode_setup.laser_speed * ((elapsed_time - 0.01) / 0.01)
                    if self.laser_fire == 0:
                        self.laser_list[0].rect.centerx = self.laser_list[0].rect.centerx - alien_mode_setup.laser_speed - delta_movement
                    else:
                        for l in self.laser_list:
                            l.rect.centerx = l.rect.centerx - alien_mode_setup.laser_speed - delta_movement
                self.laser_start_time = time.time()
        # If the laser has finished moving
        else:
            # reset the variables
            self.shoot_update = 0
            for l in self.laser_list:
                l.laser_visible = 0

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
            if self.direction == "right" and self.death_animation == 0:
                # Make the player face and walk right
                if (self.moving_right == 1 and right_update % 0.5 != 0) or self.jump_update == 1:
                    self.image = pygame.image.load(HUMAN_WALKING_RIGHT_TEXTURE)
                else:
                    self.image = pygame.image.load(HUMAN_STILL_RIGHT_TEXTURE)
            # If the players direction is left
            elif self.direction == "left" and self.death_animation == 0:
                # Make the player face and walk left
                if (self.moving_left == 1 and left_update % 0.5 != 0) or self.jump_update == 1:
                    self.image = pygame.image.load(HUMAN_WALKING_LEFT_TEXTURE)
                else:
                    self.image = pygame.image.load(HUMAN_STILL_LEFT_TEXTURE)
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
                self.gun.image = pygame.image.load(alien_mode_setup.gun_right_texture)
            # If the players direction is left, make the gun face left
            elif self.gun_direction == 2:
                self.gun.image = pygame.image.load(alien_mode_setup.gun_left_texture)
            self.gun_start_time = time.time()

    def grant_player_health(self):
        """
            This function is used to grant the player 3 health when the Heart power up is picked up.

            :return: None
        """

        if self.health + 3 > alien_mode_setup.health:
            new_increase = alien_mode_setup.health - self.health
            self.health = self.health + new_increase
        else:
            self.health = self.health + 3

        if self.health >= 10:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_1010_TEXTURE)
            if self.health == 20:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_10_TEXTURE)
            elif self.health == 19:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_9_TEXTURE)
            elif self.health == 18:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_8_TEXTURE)
            elif self.health == 17:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_7_TEXTURE)
            elif self.health == 16:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_6_TEXTURE)
            elif self.health == 15:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_5_TEXTURE)
            elif self.health == 14:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_4_TEXTURE)
            elif self.health == 13:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_3_TEXTURE)
            elif self.health == 12:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_2_TEXTURE)
            elif self.health == 11:
                self.armor_bar.armor_bar_visible = 1
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_1_TEXTURE)
        elif self.health == 9:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_910_TEXTURE)
        elif self.health == 8:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_810_TEXTURE)
        elif self.health == 7:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_710_TEXTURE)
        elif self.health == 6:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_610_TEXTURE)
        elif self.health == 5:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_510_TEXTURE)
        elif self.health == 4:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_410_TEXTURE)
        elif self.health == 3:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_310_TEXTURE)
        elif self.health == 2:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_210_TEXTURE)
        elif self.health == 1:
            self.health_bar.image = pygame.image.load(HEALTH_BAR_110_TEXTURE)

    def kill_player(self, death_sound):
        """
            Kills the human player and plays the human players death animation. After that, it spawns the player back
                at the center and resets the game.

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
                self.image = pygame.image.load(PLAYER_DEATH_2_TEXTURE)
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
                # Reset the players health to 10 or 20 is armor is enabled
                self.health = alien_mode_setup.health
                self.health_bar.image = pygame.image.load(HEALTH_BAR_1010_TEXTURE)
                if self.health == 20:
                    self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_10_TEXTURE)
                    self.armor_bar.armor_bar_visible = 1
                # Move the player back to the center of the screen
                self.rect.center = (640 * self.scale_factor_x, 501 * self.scale_factor_y)
                self.oxygen_tank.center = (self.rect.centerx - 30.5 * self.scale_factor_x, self.rect.centery - 11 * self.scale_factor_y)
                self.gun.center = (self.rect.centerx, self.rect.centery - 12 * self.scale_factor_y)
                self.oxygen_tank.oxygen_tank_visible = 1
                # Reset the players texture and all related variables
                self.image = pygame.image.load(HUMAN_STILL_RIGHT_TEXTURE)
                self.direction = "stop"
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

        # The health of the player has to be 1 in order for it to die
        if self.health == 1 and self.death_animation != 1:
            # The players health goes down to 0
            self.health = 0
            for l in self.laser_list:
                l.laser_update = 20
            # Set the players texture to the first frame of the explosion
            self.image = pygame.image.load(PLAYER_DEATH_1_TEXTURE)
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Player_Death_Sound.wav")
                sound.play()
            self.oxygen_tank.oxygen_tank_visible = 0
            self.gun.gun_visible = 0
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
            # If the players health is above 10, an armor bar should be visible
            if self.health == 19:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_9_TEXTURE)
            elif self.health == 18:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_8_TEXTURE)
            elif self.health == 17:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_7_TEXTURE)
            elif self.health == 16:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_6_TEXTURE)
            elif self.health == 15:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_5_TEXTURE)
            elif self.health == 14:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_4_TEXTURE)
            elif self.health == 13:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_3_TEXTURE)
            elif self.health == 12:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_2_TEXTURE)
            elif self.health == 11:
                self.armor_bar.image = pygame.image.load(ARMOR_BAR_10_1_TEXTURE)
            # Armor bar disappears when the players health drops below 11
            elif self.health == 10:
                self.armor_bar.armor_bar_visible = 0
            elif self.health == 9:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_910_TEXTURE)
            elif self.health == 8:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_810_TEXTURE)
            elif self.health == 7:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_710_TEXTURE)
            elif self.health == 6:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_610_TEXTURE)
            elif self.health == 5:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_510_TEXTURE)
            elif self.health == 4:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_410_TEXTURE)
            elif self.health == 3:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_310_TEXTURE)
            elif self.health == 2:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_210_TEXTURE)
            elif self.health == 1:
                self.health_bar.image = pygame.image.load(HEALTH_BAR_110_TEXTURE)
            self.hit_delay = self.hit_delay + 1
            self.hit_start_time = time.time()
            return

        if self.hit_delay == 0 and self.death_animation == 0:
            # Decrease the players health by 1
            self.health = self.health - 1
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Player_Hit_Sound.wav")
                sound.play()
            self.hit_delay = 1
            return


class OxygenTank(pygame.sprite.Sprite):
    def __init__(self, x, y, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(OXYGEN_TANK_TEXTURE)
        self.rect = self.image.get_rect()
        self.rect.center = (x - 30.5 * scale_factor_x, y - 11 * scale_factor_y)
        self.oxygen_tank_visible = 1
        self.direction = "stop"

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
        del self

    def remove(self):
        self.oxygen_tank_visible = 0
        self.direction = "stop"


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(alien_mode_setup.gun_right_texture)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - 12 * scale_factor_y)
        self.gun_visible = 0
        self.direction = "stop"

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
        del self

    def remove(self):
        self.gun_visible = 0
        self.direction = "stop"


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, god_mode, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(HEALTH_BAR_1010_TEXTURE)
        self.rect = self.image.get_rect()
        self.rect.center = (1171 * scale_factor_x, 21 * scale_factor_y)
        if god_mode == 1:
            self.health_bar_visible = 0
        else:
            self.health_bar_visible = 1

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
        del self

    def remove(self):
        self.health_bar_visible = 0


class ArmorBar(pygame.sprite.Sprite):
    def __init__(self, god_mode, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(ARMOR_BAR_10_10_TEXTURE)
        self.rect = self.image.get_rect()
        self.rect.center = (1171 * scale_factor_x, 61 * scale_factor_y)
        if god_mode == 1:
            self.armor_bar_visible = 0
        else:
            self.armor_bar_visible = 1

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
        del self

    def remove(self):
        self.armor_bar_visible = 0
