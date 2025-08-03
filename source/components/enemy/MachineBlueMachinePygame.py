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
    File: MachineBlueMachine.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to the blue machine, which is the first enemy you will encounter
    in Machine Mode.
    The blue machine fires small blue lasers at the player. It dies in one hit and has a 1.5 second long
    death animation.
    When killed, the blue machine grants the player 1 point.
    The blue machine also moves up and down to simulate floating in outer space. It also moves left to right after
    it has been killed enough times.
"""

import random
import pygame
import time
import math

from setup.ModeSetupMasterPygame import machine_mode_setup
from components.ItemCoinPygame import Coin


class BlueMachine(pygame.sprite.Sprite):
    def __init__(self, id, textures, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.BLUE_MACHINE
        self.rect = self.image.get_rect()

        if id == 1:
            self.rect.center = (440 * scale_factor_x, 140 * scale_factor_y)
        elif id == 2:
            self.rect.center = (840 * scale_factor_x, 140 * scale_factor_y)
        elif id == 3:
            self.rect.center = (1140 * scale_factor_x, 140 * scale_factor_y)
        elif id == 4:
            self.rect.center = (140 * scale_factor_x, 140 * scale_factor_y)
        elif id == 5:
            self.rect.center = (240 * scale_factor_x, 140 * scale_factor_y)
        else:
            self.rect.center = (0, 0)
        self.machine_visible = 1

        self.blue_machine_laser = BlueMachineLaser(id, textures, scale_factor_x, scale_factor_y)

        self.death_count = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.float_y = float(self.rect.centery)
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.laser_start_time = time.time()
        self.move_start_time = time.time()
        self.float_start_time = time.time()
        self.laser_has_attacked = 0
        self.movement_activated = 0
        self.id = id

        # For collision
        self.enemy_center = self.rect.centery
        self.float_time_offset = time.time()
        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count
        self.thorns_initiated_damage = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
        Cleans up the sprite from memory once the program has terminated.

        :return: None
        """

        self.kill()

        if hasattr(self, 'blue_machine_laser'):
            self.blue_machine_laser.kill()
            del self.blue_machine_laser

    def get_blue_machine(self):
        """
            Returns the blue_machine sprite so its class attributes can be accessed

            :return: blue_machine: the blue machine sprite
            :type: turtle.Turtle()
        """

        return self

    def get_blue_machine_laser(self):
        """
            Returns the blue_machine_laser sprite so its class attributes can be accessed

            :return: blue_machine_laser: the blue machine laser sprite
            :type: turtle.Turtle()
        """

        return self.blue_machine_laser

    def get_id(self):
        """
            Returns the id of the blue machine

            :return: id: the id of the blue machine
            :type: int
        """

        return self.id

    def get_update_value(self):
        """
            Returns the death animation update value of the blue machine

            :return: update: the death animation update value of the blue machine
            :type: float
        """

        return self.update

    def isvisible(self):
        return self.machine_visible

    def set_death_count(self, new_death_count):
        """
            Sets the death count for the blue machine. (Used for when the player dies and the death count has to
                be set to 0). The movement activated is also set to 0 because the enemies side to side movement stops
                happening.

            :param new_death_count: The new death count of the blue machine.
            :type new_death_count: int

            :return: None
        """

        self.death_count = new_death_count
        self.movement_activated = 0

    def set_laser_has_attacked(self, new_value):
        """
            Sets the laser_has_attacked of the blue machine (Used for when the player fires a new laser and this value
                has to be reset to 0)

            :param new_value: The new laser_has_attacked of the blue machine.
            :type new_value: int

            :return: None
        """

        self.laser_has_attacked = new_value

    def remove(self):
        """
            Removes the blue machine sprite from the screen and resets its attributes.

            :return: None
        """
        # Remove sprites from all groups and delete
        if hasattr(self, 'blue_machine'):
            self.blue_machine.kill()
            del self.blue_machine

        if hasattr(self, 'blue_machine_laser'):
            self.blue_machine_laser.kill()
            del self.blue_machine_laser

        # Reset game-related state
        self.death_count = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.float_y = float(self.rect.centery)
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0
        self.movement_activated = 0

        # Clear collision and positional lists
        self.x_range_list.clear()
        self.collision_y_coordinate_list.clear()
        self.thorns_initiated_damage = 0

    def remove_collisions(self):
        """
            Clears and resets the machines hitboxes so they can be recreated.

            :return: None
        """

        # Clear the lists
        self.x_range_list.clear()
        self.collision_y_coordinate_list.clear()

        # Initialize lists with the required number of elements
        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count

    def shoot_laser(self, green_power_up, shooting_sound):
        """
            Shoots the blue machine laser (Spawning it right below the sprite) and move it down across the screen)

            :param green_power_up: Variable used to determine if the green power up is active or not. If it is active,
                the enemy laser will not fire.
            :type green_power_up: int

            :param shooting_sound: Determines whether the toggle for the enemy lasers shooting sound is on. If it is,
                the shooting sound will play when the enemy laser is fired.
            :type shooting_sound: int

            :return: None
        """

        if green_power_up == 0:
            # Remove the laser from the screen once it has hit the player
            if self.laser_has_attacked == 1:
                self.blue_machine_laser.laser_visible = 0
            else:
                self.blue_machine_laser.laser_visible = 1
            # If the laser is still visible in the frame of the screen
            if self.blue_machine_laser.rect.centery < 720 * self.scale_factor_y:
                # Keep moving the laser down the screen 4.8 units every 0.015 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.015:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 4.8 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                    self.blue_machine_laser.rect.centery = int(self.blue_machine_laser.rect.centery + 4.8 * self.scale_factor_y + delta_movement)
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.blue_machine_laser.rect.centerx = self.rect.centerx
                self.blue_machine_laser.rect.centery = self.rect.centery + 50 * self.scale_factor_y
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.blue_machine_laser.laser_visible = 0
            self.blue_machine_laser.rect.centerx = self.rect.centerx
            self.blue_machine_laser.rect.centery = self.rect.centery + 50 * self.scale_factor_y
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_enemy(self, death_sound, coins_on_screen, scale_factor_x):
        """
            Kills the enemy and plays the enemies death animation. After that, it spawns the enemy in a new location.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :return: None
        """

        # When the death animation and respawning is finished, the blue machine appears on the screen again
        if self.update == 6:
            self.machine_visible = 1
            self.movement_activated = 0
            self.update = 0
            return

        # Wait 0.05 seconds
        if 3.5 <= self.update < 6:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.05:
                self.update = 6
                self.start_time = 0
            return

        if self.update == 3:
            # Hide the blue machine and spawn a copper coin where the blue machine died
            self.machine_visible = 0
            copper_coin = Coin(type="copper", pos_x=self.rect.centerx, pos_y=self.rect.centery, scale_factor_x=scale_factor_x)
            # Set the hitbox for the coin
            copper_coin.range = (copper_coin.rect.centerx - copper_coin.COIN_DISTANCE, copper_coin.rect.centerx + copper_coin.COIN_DISTANCE)
            copper_coin.collision_coordinate = copper_coin.rect.centery - copper_coin.COIN_DISTANCE
            coins_on_screen.append(copper_coin)
            # Respawn the blue machine in a different random location
            old_center = self.rect.center
            self.image = self._textures.BLUE_MACHINE
            self.rect = self.image.get_rect(center=old_center)
            # Want to cast these ranges to integers to avoid a crash at certain resolutions
            self.rect.center = (random.randint(int(0 * self.scale_factor_x), int(1280 * self.scale_factor_x)), random.randint(int(140 * self.scale_factor_y), int(240 * self.scale_factor_y)))
            # Restart the float effect
            self.float_activated = 0
            self.float = 1
            self.float_time_offset = time.time()
            self.enemy_center = self.rect.centery
            # Reset the hitboxes
            self.x_range_list.clear()
            self.collision_y_coordinate_list.clear()
            self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
            self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count
            self.update = 3.5
            self.start_time = time.time()
            return

        # Wait 0.15 seconds
        if 1.5 <= self.update < 3:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.15:
                self.update = 3
                self.start_time = 0
            return

        # Change the texture of the blue machine to the second frame of the explosion
        if 1.0 <= self.update <= 1.1:
            old_center = self.rect.center
            self.image = self._textures.EXPLOSION_2
            self.rect = self.image.get_rect(center=old_center)
            self.update = 1.5
            self.start_time = time.time()
            self.kill_enemy(death_sound, coins_on_screen, scale_factor_x)
            return

        # Wait 0.1 seconds
        if 0.5 <= self.update < 1:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.1:
                self.update = 1
                self.start_time = 0
            return

        if self.update == 0:
            # Increase the death count
            self.death_count = self.death_count + 1
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion.wav")
                sound.play()
            # Change the texture of the blue machine to the first frame of the death explosion
            old_center = self.rect.center
            self.image = self._textures.EXPLOSION_1
            self.rect = self.image.get_rect(center=old_center)
            self.update = 0.5
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.start_time = time.time()
            return

    def float_effect(self):
        """
            Moves the blue machine up and down to create a float effect and make it seem as if the enemy is moving fast
                through outer space.

            :return: None
        """

        # Activate the float effect
        if self.float_activated == 0:
            self.float_activated = 1
            self.start_y_float = self.rect.centery

        if self.start_y_float - 50 * self.scale_factor_y >= self.rect.centery:
            self.float = -1
        elif self.start_y_float + 50 * self.scale_factor_y <= self.rect.centery:
            self.float = 1
        current_time = time.time()
        elapsed_time = current_time - self.float_start_time
        # Make a movement every 0.0075 seconds to reduce the effects of lag
        if elapsed_time >= 0.0075:
            if self.float == 1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = machine_mode_setup.MACHINE_FLOAT * ((elapsed_time - 0.0075) / 0.0075)
                self.float_y -= machine_mode_setup.MACHINE_FLOAT + delta_movement
                self.rect.centery = int(self.float_y)
            elif self.float == -1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = machine_mode_setup.MACHINE_FLOAT * ((elapsed_time - 0.0075) / 0.0075)
                self.float_y += machine_mode_setup.MACHINE_FLOAT + delta_movement
                self.rect.centery = int(self.float_y)
            self.float_start_time = time.time()

    def move_enemy(self, death):
        """
            When the blue machine has died enough times, this function will cause it to start moving left and
                right, which will speed up the more times that the blue machine dies.

            :param death: Determines whether the death animation for the player is active or not.
            :type death: int

            :return: None
        """

        if self.death_count >= 4 and death == 0 and self.update == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the blue machine every 0.02 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.02:
                # Blue machine reaches the right end of the screen
                if 1280 * self.scale_factor_x < self.rect.centerx:
                    # Move left
                    self.movement = -1
                # Blue machine reaches the left end of the screen
                if self.rect.centerx < 0:
                    # Move right
                    self.movement = 1
                if self.movement == 1:
                    # Speeds up based on the death_count variable
                    if 4 <= self.death_count < 7:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = machine_mode_setup.MACHINE_MOVE_2 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_2 + delta_movement
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_4 + delta_movement
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_6 + delta_movement
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_8 + delta_movement
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_10 + delta_movement
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_2 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_2 - delta_movement
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_4 - delta_movement
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_6 - delta_movement
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_8 - delta_movement
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_10 - delta_movement
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0


class BlueMachineLaser(pygame.sprite.Sprite):
    def __init__(self, id, textures, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.BLUE_MACHINE_LASER
        self.rect = self.image.get_rect()
        if id == 1:
            self.rect.center = (440 * scale_factor_x, 190 * scale_factor_y)
        elif id == 2:
            self.rect.center = (840 * scale_factor_x, 190 * scale_factor_y)
        elif id == 3:
            self.rect.center = (1140 * scale_factor_x, 190 * scale_factor_y)
        elif id == 4:
            self.rect.center = (140 * scale_factor_x, 190 * scale_factor_y)
        elif id == 5:
            self.rect.center = (240 * scale_factor_x, 190 * scale_factor_y)
        else:
            self.rect.center = (0, 0)
        self.laser_visible = 1

    def __del__(self):
        self.kill()

    def isvisible(self):
        return self.laser_visible

    def distance(self, other_sprite):
        """Return the Euclidean distance to another sprite based on center positions."""
        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)
