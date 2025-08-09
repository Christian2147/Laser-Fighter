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
    File: AlienUFO.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to the UFO boss in Alien Mode.
    The UFO is the final enemy the player encounters in Alien Mode.
    The UFO will always move towards the player and moves faster the more times it is killed.
    When it comes into contact with the player, it reduces the players health.
    The UFO also has a laser that it shoots down at the player which will hurt the player if hit by it.
    The UFO dies in 10 hits from the players laser and grants the player 50 points.
    The UFO also grants the player 1 - 3 points each time it is hit.
"""

import pygame
import random
import time
import math
from components.ItemCoinPygame import Coin
from setup.ModeSetupMasterPygame import alien_mode_setup


class UFO(pygame.sprite.Sprite):
    """
        Represents a UFO in Alien Mode. The UFO hovers in the air and moves towards the player at all times.

        Attributes:
            ufo_laser (pygame.sprite.Sprite): The UFO laser sprite
            ufo_health_bar (pygame.sprite.Sprite): The UFO health bar sprite

            death_animation (float): Iterated during the UFOs death animation
            death_count (int): Stores the amount of times the UFO has died since the player has last died
            direction (int): Stores the direction that the UFO is facing (1 = right and 2 = left)
            hit_delay (float):  Delays how often the UFO can be hit
            health (int): Stores the UFOs current health

            kill_start_time (float): Used as a timestamp for the death animation of the UFO (To make the
                animation run in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit delay of the UFO (To make sure that the
                hit delay lasts a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the UFO's laser movement (To make sure the movement
                happens in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the UFOs movement (To make the UFOs
                movement happen in a consistent amount of time and not based on code execution speed)

            movement_activated (int): Check if the aliens movement is currently happening or not. (So that
                it can create a start time for it)

            got_hit (int): Determines if the UFO has already been hit by the players laser since it was last fired
            collision_point (int): Determines the x-axis collision line for the UFO
            already_ahead (int): Determines if the player is already ahead of the UFO (larger x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the UFO)
            already_behind (int): Determines of the player is already behind the UFO (smaller x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the UFO)
            thorns_initiated_damage (int): Checks if the enemy has damaged the player while the player has thorns on

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, textures, scale_factor_x, scale_factor_y):
        """
            Creates a UFO object and spawns it in the game.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = textures.ALIEN_BOSS
        self.rect = self.image.get_rect()
        self.rect.center = (int(1515 * scale_factor_x), round(380 * scale_factor_y))
        self.ufo_visible = 1
        self.direction = "stop"

        self.ufo_laser = UFOLaser(textures, scale_factor_x, scale_factor_y)

        self.ufo_health_bar = UFOHealthBar(textures, scale_factor_x, scale_factor_y)

        self.death_animation = 0
        self.death_count = 0
        self.hit_delay = 0
        self.health = 10
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = time.time()
        self.move_start_time = time.time()
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
        if hasattr(self, 'ufo_laser'):
            self.ufo_laser.kill()
            del self.ufo_laser
        if hasattr(self, 'ufo_health_bar'):
            self.ufo_health_bar.kill()
            del self.ufo_health_bar
        del self

    def get_ufo(self):
        """
            Returns the UFO sprite so that its class attributes can be accessed.

            :return: ufo: The UFO sprite
            :type: Turtle.turtle()
        """

        return self

    def get_ufo_laser(self):
        """
            Returns UFOs laser sprite so that its class attributes can be accessed.

            :return: ufo_laser: The UFOs laser sprite
            :type: Turtle.turtle()
        """

        return self.ufo_laser

    def get_ufo_health_bar(self):
        """
            Returns the UFOs health bar sprite so that its class attributes can be accessed.

            :return: ufo_health_bar: The UFOs health bar sprite
            :type: Turtle.turtle()
        """

        return self.ufo_health_bar

    def get_ufo_health(self):
        """
            Returns the current health of the UFO.

            :return: health: The current health of the UFO
            :type: int
        """

        return self.health

    def get_death_animation(self):
        """
            Returns the current state of the UFOs death animation (0 if it is not happening)

            :return: death_animation: The current state of the UFOs death animation
            :type: float
        """

        return self.death_animation

    def get_hit_delay(self):
        """
            Returns the current state of the UFOs hit delay (0 if it is not happening)

            :return: hit_delay: The current state of the UFOs hit delay
            :type: float
        """

        return self.hit_delay

    def isvisible(self):
        return self.ufo_visible

    def distance(self, other_sprite):
        """
            Calculates the Euclidean distance to another sprite.

            :param other_sprite: Another sprite with a rect attribute

            :return: float
        """

        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)

    def set_got_hit(self, new_value):
        """
            Sets the got hit variable of the UFO when the UFO gets hit by a players laser.

            :param new_value: The new value that the "got_hit" variable will be set to
            :type new_value: 1

            :return: None
        """

        self.got_hit = new_value

    def remove(self):
        """
            Removes the UFO sprite form the screen and resets its attributes.

            :return: None
        """

        self.ufo_visible = 0
        self.ufo_laser.laser_visible = 0
        self.ufo_health_bar.health_bar_visible = 0
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 10
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.movement_activated = 0
        self.got_hit = 1
        self.collision_point = 0
        self.already_ahead = 1
        self.already_behind = 1
        self.thorns_initiated_damage = 0

    def shoot_laser(self, shooting_sound):
        """
            Shoots the UFOs laser and moves it down to the ground after it is fired.

            :param shooting_sound: Determines whether the toggle for the enemy lasers shooting sound is on. If it is,
                the shooting sound will play when the enemy laser is fired.
            :type shooting_sound: int

            :return: None
        """

        self.ufo_laser.laser_visible = 1
        if self.isvisible() or self.death_animation != 0:
            if self.ufo_laser.rect.centery < 960 * self.scale_factor_y:
                # Move the laser down 3.2 units every 0.0075 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.0075:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 3.2 * self.scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                    self.ufo_laser.rect.centery = self.ufo_laser.rect.centery + 3.2 * self.scale_factor_y + delta_movement
                    self.laser_start_time = time.time()
            # If the UFO is not dying
            elif self.death_animation == 0:
                # Fire the laser
                self.ufo_laser.rect.centerx = self.rect.centerx + 2 * self.scale_factor_x
                self.ufo_laser.rect.centery = 450 * self.scale_factor_y
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the ufo is not visible, then stop firing the laser
        else:
            self.ufo_laser.rect.centerx = self.rect.centerx + 2 * self.scale_factor_x
            self.ufo_laser.rect.centery = 450 * self.scale_factor_y
            self.laser_start_time = time.time()

        # Make the laser disappear once it hits the ground
        if self.ufo_laser.rect.centery > 530 * self.scale_factor_y:
            self.ufo_laser.laser_visible = 0

    def set_ufo_direction(self, player_x):
        """
            Sets the direction of the UFO so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.ufo_visible == 1:
            # If the players x-coordinate is smaller than the UFOs, then make the UFO face left
            if self.rect.centerx > player_x:
                self.direction = "left"
            # If the players x-coordinate is smaller than the UFOs, then make the UFO face right
            else:
                self.direction = "right"

    def kill_ufo(self, death_sound, coins_on_screen):
        """
            Kills the UFO and plays the aliens death animation. After that, it respawns the UFO on a random
                side of the screen.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :return: None
        """

        if 4 <= self.death_animation < 5:
            # Spawn a coin where the UFO has died
            self.ufo_visible = 0
            platinum_coin = Coin(type="platinum", pos_x=self.rect.centerx, pos_y=self.rect.centery, textures=self._textures, scale_factor_x=self.scale_factor_x)
            # Set the hitbox for the coin
            platinum_coin.range = (platinum_coin.rect.centery - platinum_coin.COIN_DISTANCE, platinum_coin.rect.centery + platinum_coin.COIN_DISTANCE)
            platinum_coin.collision_coordinate = platinum_coin.rect.centerx
            platinum_coin.just_fired = 0
            coins_on_screen.append(platinum_coin)
            # Respawn the UFO in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.rect.center = (random.randint(int(-260 * self.scale_factor_x), int(-50 * self.scale_factor_x)), round(380 * self.scale_factor_y))
                self.ufo_health_bar.rect.center = (self.rect.centerx, 310 * self.scale_factor_y)
            if alien_random == 2:
                self.rect.center = (random.randint(int(1330 * self.scale_factor_x), int(1540 * self.scale_factor_x)), round(380 * self.scale_factor_y))
                self.ufo_health_bar.rect.center = (self.rect.centerx, 310 * self.scale_factor_y)
            # Reset the UFOs health
            old_center = self.ufo_health_bar.rect.center
            self.ufo_health_bar.image = self._textures.HEALTH_BAR_1010
            self.ufo_health_bar.rect = self.ufo_health_bar.image.get_rect(center=old_center)
            old_center = self.rect.center
            self.image = self._textures.ALIEN_BOSS
            self.rect = self.image.get_rect(center=old_center)
            self.health = 10
            self.precise_x = float(self.rect.centerx)
            self.ufo_visible = 1
            self.ufo_health_bar.health_bar_visible = 1
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
            # Change the UFOs texture to the second frame in the death scene
            old_center = self.rect.center
            self.image = self._textures.EXPLOSION_2
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
            # UFO was hit by the players laser
            # Increase the death count
            self.death_count = self.death_count + 1
            self.health = 0
            self.ufo_health_bar.health_bar_visible = 0
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion.wav")
                sound.play()
            # Set the texture of the large alien to the first frame in the death scene
            old_center = self.rect.center
            self.image = self._textures.EXPLOSION_1
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

    def hit_ufo(self, hit_sound):
        """
            Makes the UFO take "one hit" of damage and creates a hit delay before the UFO can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        # Reset the hit delay variable
        if 99.9 < self.hit_delay < 100.1:
            self.hit_delay = 0
            return

        # Wait 0.1 seconds
        if 1 <= self.hit_delay < 100:
            if self.hit_delay == 1:
                self.hit_delay = 1.5
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.1:
                self.hit_delay = 100
                self.hit_start_time = 0
            return

        if self.death_animation == 0:
            # Decrease the ufos health by the damage amount
            self.health = self.health - alien_mode_setup.damage
            old_center = self.ufo_health_bar.rect.center
            if self.health == 9:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_910
            elif self.health == 8:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_810
            elif self.health == 7:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_710
            elif self.health == 6:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_610
            elif self.health == 5:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_510
            elif self.health == 4:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_410
            elif self.health == 3:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_310
            elif self.health == 2:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_210
            elif self.health == 1:
                self.ufo_health_bar.image = self._textures.HEALTH_BAR_110
            self.ufo_health_bar.rect = self.ufo_health_bar.image.get_rect(center=old_center)
            # Play the hit sound
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion2.wav")
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
            Function for the UFOs movement.
            When the UFO has died enough times, this function will cause it to start moving faster and faster.

            :return: None
        """

        if self.ufo_visible == 1 and self.death_animation == 0:
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
                    if 0 <= self.death_count < 3:
                        delta_movement = 0.25 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 0.25 * self.scale_factor_x + delta_movement
                    if 3 <= self.death_count < 6:
                        delta_movement = 0.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 0.5 * self.scale_factor_x + delta_movement
                    if 6 <= self.death_count < 9:
                        delta_movement = 1 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 1 * self.scale_factor_x + delta_movement
                    if 9 <= self.death_count < 12:
                        delta_movement = 1.75 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 1.75 * self.scale_factor_x + delta_movement
                    if 12 <= self.death_count < 15:
                        delta_movement = 2.75 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 2.75 * self.scale_factor_x + delta_movement
                    if 15 <= self.death_count:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x + 4 * self.scale_factor_x + delta_movement
                else:
                    # Move the alien left
                    if 0 <= self.death_count < 3:
                        delta_movement = 0.25 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 0.25 * self.scale_factor_x - delta_movement
                    if 3 <= self.death_count < 6:
                        delta_movement = 0.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 0.5 * self.scale_factor_x - delta_movement
                    if 6 <= self.death_count < 9:
                        delta_movement = 1 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 1 * self.scale_factor_x - delta_movement
                    if 9 <= self.death_count < 12:
                        delta_movement = 1.75 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 1.75 * self.scale_factor_x - delta_movement
                    if 12 <= self.death_count < 15:
                        delta_movement = 2.75 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 2.75 * self.scale_factor_x - delta_movement
                    if 15 <= self.death_count:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.precise_x = self.precise_x - 4 * self.scale_factor_x - delta_movement

                # Sync the float position to the rect
                self.rect.centerx = int(round(self.precise_x))
                self.ufo_health_bar.rect.centerx = int(round(self.precise_x))

                # Reset movement timer
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0


class UFOLaser(pygame.sprite.Sprite):
    def __init__(self, textures, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.YELLOW_MACHINE_LASER
        self.rect = self.image.get_rect()
        self.rect.center = (int(1517 * scale_factor_x), round(450 * scale_factor_y))
        self.laser_visible = 1

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()

    def isvisible(self):
        return self.laser_visible

    def distance(self, other_sprite):
        """Return the Euclidean distance to another sprite based on center positions."""
        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)


class UFOHealthBar(pygame.sprite.Sprite):
    def __init__(self, textures, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.HEALTH_BAR_1010
        self.rect = self.image.get_rect()
        self.rect.center = (int(1515 * scale_factor_x), round(310 * scale_factor_y))
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
