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
    File: AlienLargeAlien.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to the Large Aliens in Alien Mode.
    The large alien is the third enemy the player encounters in Alien Mode.
    The large alien will always move towards the player and moves faster the more times they are killed.
    When they come into contact with the player, they reduce the players health.
    The large alien dies in three hits from the players laser and grants the player 5 points.
    The large alien also grants the player 1 point each time it is hit.
"""

import pygame
import random
import time
import math
from components.ItemCoinPygame import Coin
from setup.ModeSetupMasterPygame import alien_mode_setup


class LargeAlien(pygame.sprite.Sprite):
    """
        Represents a large alien in Alien Mode. The large alien is significantly taller than the player and moves
            towards the player at all times.

        Attributes:
            large_alien_health_bar (pygame.sprite.Sprite): The large alien health bar sprite

            death_animation (float): Iterated during the large aliens death animation
            death_count (int): Stores the amount of times the large alien has died since the player has last died
            direction (int): Stores the direction that the large alien is facing (1 = right and 2 = left)
            hit_delay (float):  Delays how often the large alien can be hit
            health (int): Stores the large aliens current health

            kill_start_time (float): Used as a timestamp for the death animation of the large alien (To make the
                animation run in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit delay of the large alien (To make sure that the
                hit delay lasts a consistent amount of time)
            walk_start_time (float): Used as a timestamp for the large aliens walking texture update (To make sure the
                walking animation happens in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the large aliens movement (To make the large aliens
                movement happen in a consistent amount of time and not based on code execution speed)

            movement_activated (int): Check if the aliens movement is currently happening or not. (So that
                it can create a start time for it)

            got_hit (int): Determines if the alien has already gotten hit or not
            collision_point (int): Determines the x-axis collision line for the alien
            already_ahead (int): Determines if the player is already ahead of the alien (larger x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the alien)
            already_behind (int): Determines of the player is already behind the alien (smaller x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the alien)
            thorns_initiated_damage (int): Checks if the enemy has damaged the player while the player has thorns on

            id (int): The id of the alien

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, id, textures, scale_factor_x, scale_factor_y):
        """
            Creates a large alien object with the given id and spawns it in the game.

            :param id: A unique identifier for the large alien
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = textures.ALIEN_STILL_RIGHT_11_15
        self.rect = self.image.get_rect()
        if id == 1:
            self.rect.center = (int(-85 * scale_factor_x), round(445 * scale_factor_y))
        elif id == 2:
            self.rect.center = (int(1415 * scale_factor_x), round(445 * scale_factor_y))
        elif id == 3:
            self.rect.center = (int(-135 * scale_factor_x), round(445 * scale_factor_y))
        elif id == 4:
            self.rect.center = (int(1465 * scale_factor_x), round(445 * scale_factor_y))
        elif id == 5:
            self.rect.center = (int(-185 * scale_factor_x), round(445 * scale_factor_y))
        self.large_alien_visible = 1
        self.direction = "stop"

        self.large_alien_health_bar = LargeAlienHealthBar(self.rect.centerx, textures, scale_factor_x, scale_factor_y)

        self.death_animation = 0
        self.death_count = 0
        self.hit_delay = 0
        self.health = 3
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0
        self.movement_activated = 0
        self.precise_x = float(self.rect.centerx)

        # For collision
        self.got_hit = 1
        self.collision_point = 0
        self.already_ahead = 1
        self.already_behind = 1
        self.thorns_initiated_damage = 0

        self._textures = textures
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        if hasattr(self, 'large_alien_health_bar'):
            self.large_alien_health_bar.kill()
            del self.large_alien_health_bar
        del self

    def get_large_alien(self):
        """
            Returns the large alien sprite so that its class attributes can be accessed.

            :return: large_alien: The large alien sprite
            :type: Turtle.turtle()
        """

        return self

    def get_large_alien_health_bar(self):
        """
            Returns the large alien health bar sprite so that its class attributes can be accessed.

            :return: large_alien_health_bar: The large alien health bar sprite
            :type: Turtle.turtle()
        """

        return self.large_alien_health_bar

    def get_large_alien_health(self):
        """
            Returns the current health of the large alien.

            :return: health: The current health of the large alien
            :type: int
        """

        return self.health

    def get_death_animation(self):
        """
            Returns the current state of the large aliens death animation (0 if it is not happening)

            :return: death_animation: The current state of the large aliens death animation
            :type: float
        """

        return self.death_animation

    def get_hit_delay(self):
        """
            Returns the current state of the large aliens hit delay (0 if it is not happening)

            :return: hit_delay: The current state of the large aliens hit delay
            :type: float
        """

        return self.hit_delay

    def isvisible(self):
        return self.large_alien_visible

    def distance(self, other_sprite):
        """
            Calculates the Euclidean distance to another sprite.

            :param other_sprite: Another sprite with a rect attribute

            :return: float
        """

        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)

    def remove(self):
        """
            Removes the large alien sprite form the screen and resets its attributes.

            :return: None
        """

        self.large_alien_visible = 0
        self.large_alien_health_bar.health_bar_visible = 0
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 3
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0
        self.got_hit = 1
        self.collision_point = 0
        self.already_ahead = 1
        self.already_behind = 1
        self.thorns_initiated_damage = 0

    def set_alien_direction(self, player_x):
        """
            Sets the direction of the large alien so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.large_alien_visible == 1:
            # If the players x-coordinate is smaller than the large aliens, then make the large alien face left
            if self.rect.centerx > player_x:
                self.direction = "left"
            # If the players x-coordinate is smaller than the large aliens, then make the large alien face right
            else:
                self.direction = "right"

    def set_alien_texture(self, right_update, left_update):
        """
            Sets the large aliens texture based on the large aliens direction and creates a walking animation when the
                large alien is walking.

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
            # If the large aliens direction is right
            if self.direction == "right" and self.death_animation == 0:
                # Make the large alien face and walk right
                if right_update % 0.5 != 0:
                    self.image = self._textures.ALIEN_WALKING_RIGHT_11_15
                else:
                    self.image = self._textures.ALIEN_STILL_RIGHT_11_15
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
            # If the large aliens direction is left
            elif self.direction == "left" and self.death_animation == 0:
                # Make the large alien face and walk left
                if left_update % 0.5 != 0:
                    self.image = self._textures.ALIEN_WALKING_LEFT_11_15
                else:
                    self.image = self._textures.ALIEN_STILL_LEFT_11_15
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
            self.walk_start_time = time.time()

    def kill_alien(self, death_sound, coins_on_screen):
        """
            Kills the alien and plays the aliens death animation. After that, it respawns the alien on a random
                side of the screen.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :return: None
        """

        if 4 <= self.death_animation < 5:
            # Spawn a coin where the alien has died
            self.large_alien_visible = 0
            gold_coin = Coin(type="gold", pos_x=self.rect.centerx, pos_y=self.rect.centery, textures=self._textures, scale_factor_x=self.scale_factor_x)
            # Set the hitbox for the coin
            gold_coin.range = (gold_coin.rect.centery - gold_coin.COIN_DISTANCE, gold_coin.rect.centery + gold_coin.COIN_DISTANCE)
            gold_coin.collision_coordinate = gold_coin.rect.centerx
            gold_coin.just_fired = 0
            coins_on_screen.append(gold_coin)
            # Respawn the large alien in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.rect.center = (random.randint(int(-260 * self.scale_factor_x), int(-50 * self.scale_factor_x)), round(445 * self.scale_factor_y))
                self.large_alien_health_bar.rect.center = (self.rect.centerx, 322 * self.scale_factor_y)
            if alien_random == 2:
                self.rect.center = (random.randint(int(1330 * self.scale_factor_x), int(1540 * self.scale_factor_x)), round(445 * self.scale_factor_y))
                self.large_alien_health_bar.rect.center = (self.rect.centerx, 322 * self.scale_factor_y)
            # Reset the large aliens health
            old_center = self.large_alien_health_bar.rect.center
            self.large_alien_health_bar.image = self._textures.HEALTH_BAR_33
            self.large_alien_health_bar.rect = self.large_alien_health_bar.image.get_rect(center=old_center)
            self.health = 3
            self.precise_x = float(self.rect.centerx)
            self.large_alien_visible = 1
            self.large_alien_health_bar.health_bar_visible = 1
            self.movement_activated = 0
            self.death_animation = 0
            return

        # Wait 0.15 seconds
        if 3 <= self.death_animation < 4.5:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.15:
                self.death_animation = 4.5
                self.kill_start_time = 0
            return

        if 2 <= self.death_animation < 3:
            # Change the large aliens texture to the second frame in the death scene
            old_center = self.rect.center
            self.image = self._textures.ALIEN_DEATH_2
            self.rect = self.image.get_rect(center=old_center)
            self.death_animation = 3
            self.kill_start_time = time.time()
            return

        # Wait 0.1 seconds
        if 1 <= self.death_animation < 2:
            if self.death_animation == 1:
                self.death_animation = 1.5
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.1:
                self.death_animation = 2
                self.kill_start_time = 0
            return

        if self.death_animation == 0:
            # Increase the death count
            self.death_count = self.death_count + 1
            self.health = 0
            self.large_alien_health_bar.health_bar_visible = 0
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Alien_Death_Sound.wav")
                sound.play()
            # Set the texture of the large alien to the first frame in the death scene
            old_center = self.rect.center
            self.image = self._textures.ALIEN_DEATH_1
            self.rect = self.image.get_rect(center=old_center)
            # Reset collision variables
            self.got_hit = 1
            self.already_ahead = 0
            self.already_behind = 0
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.death_animation = 1
            self.kill_start_time = time.time()
            return

    def hit_alien(self, hit_sound):
        """
            Makes the large alien take "one hit" of damage and creates a hit delay before the large alien can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        # Reset the hit delay variable
        if self.hit_delay == 9:
            self.hit_delay = 0
            return

        # Wait 0.1 seconds
        if 1 <= self.hit_delay < 9:
            if self.hit_delay == 1:
                self.hit_delay = 1.5
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.1:
                self.hit_delay = 9
                self.hit_start_time = 0
            return

        if self.death_animation == 0:
            # Decrease the aliens health by 1
            self.health = self.health - alien_mode_setup.damage
            old_center = self.large_alien_health_bar.rect.center
            if self.health == 2:
                self.large_alien_health_bar.image = self._textures.HEALTH_BAR_23
            elif self.health == 1:
                self.large_alien_health_bar.image = self._textures.HEALTH_BAR_13
            self.large_alien_health_bar.rect = self.large_alien_health_bar.image.get_rect(center=old_center)
            # Play the hit sound
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Alien_Hit_Sound.wav")
                sound.play()
            # Reset collision variables
            self.got_hit = 1
            self.already_ahead = 0
            self.already_behind = 0
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.hit_delay = 1
            self.hit_start_time = time.time()
            return

    def set_movement_speed(self):
        """
            Function for the large aliens movement.
            When the large alien has died enough times, this function will cause it to start moving faster and faster.

            :return: None
        """

        if self.large_alien_visible == 1 and self.death_animation == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the large alien every 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                if self.direction == "right":
                    # Move the alien right
                    if 0 <= self.death_count < 6:
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 0.3 * self.scale_factor_x + delta_movement
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 0.6 * self.scale_factor_x + delta_movement
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 0.9 * self.scale_factor_x + delta_movement
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 1.2 * self.scale_factor_x + delta_movement
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 1.5 * self.scale_factor_x + delta_movement
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 1.8 * self.scale_factor_x + delta_movement
                else:
                    # Move the alien left
                    if 0 <= self.death_count < 6:
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 0.3 * self.scale_factor_x - delta_movement
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 0.6 * self.scale_factor_x - delta_movement
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 0.9 * self.scale_factor_x - delta_movement
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 1.2 * self.scale_factor_x - delta_movement
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 1.5 * self.scale_factor_x - delta_movement
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 1.8 * self.scale_factor_x - delta_movement

                # Sync the float position to the rect
                self.rect.centerx = int(round(self.precise_x))
                self.large_alien_health_bar.rect.centerx = int(round(self.precise_x))

                # Reset movement timer
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0


class LargeAlienHealthBar(pygame.sprite.Sprite):
    def __init__(self, x, textures, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.HEALTH_BAR_33
        self.rect = self.image.get_rect()
        self.rect.center = (x, 322 * scale_factor_y)
        self.health_bar_visible = 1

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()

    def isvisible(self):
        return self.health_bar_visible

    def distance(self, other_sprite):
        """Return the Euclidean distance to another sprite based on center positions."""
        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)
