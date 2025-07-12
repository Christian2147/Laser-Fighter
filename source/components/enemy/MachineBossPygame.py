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
    File: MachineBoss.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to the boss, which is the final enemy you will
    encounter in Machine Mode.
    The boss fires massive pink lasers at the player. It dies in 10 hits and has a 1.5 second long
    death animation.
    The bosses lasers start to move faster and faster the lower that its health gets.
    When killed, the boss grants the player 50 points.
    When hit, the boss grants the player 1 point.
    The boss also moves up and down to simulate floating in outer space. It also moves left to right after
    it has been killed enough times.
"""

import pygame
import random
import time
import math
from components.ItemCoinPygame import Coin
from setup.ModeSetupMasterPygame import machine_mode_setup
from setup.TextureSetup import MACHINE_BOSS_TEXTURE
from setup.TextureSetup import MACHINE_BOSS_LASER_TEXTURE
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


class Boss(pygame.sprite.Sprite):
    """
        Represents the boss in Machine Mode. The final enemy in Machine Mode that is pink
            and fires pink lasers.

        Attributes:
            boss_laser (turtle.Turtle()): The laser sprite for the boss.
            boss_health_bar (turtle.Turtle()): The health bar sprite for the boss.

            death_count (int): Stores the death count for the enemy since the player has last died.
            health_bar (int): Stores the current health of the enemy
            hit_delay (int): Delays how often the enemy can be hit
            update (float): Value that is incremented during the death animation of the enemy.

            movement (int): Stores the direction that the enemy is supposed to move on
                the x-axis (1 = right and -1 = left)
            float (int): Stores the direction that the enemy is supposed to move on the y-axis (1 = up and -1 == down)
            start_y_float (float): Stores the y-coordinate of the enemy when the float effect is starting or when
                it is changing direction
            float_activated (int): Determines if the float effect is currently active or not (For timing purposes)

            start_time (float): Used as a timestamp for the death animation of the enemy (To make the animation run in
                a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit delay of the enemy (To make the delay tun in
                a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the enemy (To make the movement
                happen in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the enemies movement (To make the enemies movement
                happen in a consistent amount of time and not based on code execution speed)
            float_start_time (float): Used as a timestamp for the enemies floating effect movement (To make the
                movement happen in a consistent amount of time)

            laser_has_attacked (int): Determines if the enemy has been hit by the players laser since it was last fired
                (So that it does not get hit two times in a row)
            movement_activated (int): Check if the enemies side to side movement is currently happening or not. (So
                that it can create a start time for it)

            enemy_center (float): The y-axis center of the sine wave created by the machines float effect
                (when t=0, where is it?)
            float_time_offset (float): The timestamp when the float effect for the machine begins

            x_range_list (tuple): The x-axis of the hitboxes for the machine. (The range of x-coordinates the laser
                has to be in in order to hit the enemy)
            collision_y_coordinate_list: The y-axis point that the players lasers have to pass in order to
                hit the machine.
            thorns_initiated_damage (int): Checks if the enemy has damaged the player while the player has thorns on

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates a boss object and spawns it on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = pygame.image.load(MACHINE_BOSS_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (815 * scale_factor_x, 140 * scale_factor_y)
        self.boss_visible = 1

        self.boss_laser = BossLaser(scale_factor_x, scale_factor_y)

        self.boss_health_bar = BossHealthBar(scale_factor_x, scale_factor_y)

        self.death_count = 0
        self.health_bar = 10
        self.hit_delay = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.float_y = float(self.rect.centery)
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = time.time()
        self.move_start_time = time.time()
        self.float_start_time = time.time()
        self.laser_has_attacked = 0
        self.movement_activated = 0

        # For collision
        self.enemy_center = self.rect.centery
        self.float_time_offset = time.time()
        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count
        self.thorns_initiated_damage = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        if hasattr(self, 'boss_laser'):
            self.boss_laser.kill()
            del self.boss_laser
        if hasattr(self, 'boss_health_bar'):
            self.boss_health_bar.kill()
            del self.boss_health_bar
        del self

    def get_boss(self):
        """
            Returns the boss sprite so its class attributes can be accessed

            :return: boss: the boss sprite
            :type: turtle.Turtle()
        """

        return self

    def get_boss_laser(self):
        """
            Returns the boss_laser sprite so its class attributes can be accessed

            :return: boss_laser: the boss laser sprite
            :type: turtle.Turtle()
        """

        return self.boss_laser

    def get_boss_health_bar(self):
        """
            Returns the boss_health_bar sprite so its class attributes can be accessed

            :return: boss_health_bar: the boss health bar sprite
            :type: turtle.Turtle()
        """

        return self.boss_health_bar

    def get_update_value(self):
        """
            Returns the death animation update value of the boss

            :return: update: the death animation update value of the boss
            :type: float
        """

        return self.update

    def get_hit_value(self):
        """
            Returns the hit delay value of the boss

            :return: hit_delay: the hit delay value of the boss
            :type: int
        """

        return self.hit_delay

    def isvisible(self):
        return self.boss_visible

    def set_laser_has_attacked(self, new_value):
        """
            Sets the laser_has_attacked of the boss (Used for when the player fires a new laser and this value
                has to be reset to 0)

            :param new_value: The new laser_has_attacked of the boss.
            :type new_value: int

            :return: None
        """

        self.laser_has_attacked = new_value

    def remove(self):
        """
            Removes the boss sprite form the screen and resets its attributes.

            :return: None
        """

        self.boss_visible = 0
        self.boss_laser.laser_visible = 0
        self.boss_health_bar.health_bar_visible = 0
        self.death_count = 0
        self.hit_delay = 0
        self.health_bar = 10
        self.update = 0
        self.movement = 1
        self.float = 1
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0
        self.movement_activated = 0
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
            Shoots the boss laser (Spawning it right below the sprite) and move it down across the screen. The laser
                moves faster and faster the lower the bosses health goes.

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
                self.boss_laser.laser_visible = 0
            else:
                self.boss_laser.laser_visible = 1
            # If the laser is still visible in the frame of the screen
            if self.boss_laser.rect.centery < 720 * self.scale_factor_y:
                # Keep moving the laser down the screen every 0.015 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.015:
                    # Speed depends on the bosses health
                    if 10 >= self.health_bar > 8:
                        # Calculate the delta movement
                        # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                        # Done to ensure the game speed stays the same regardless of frame rate
                        delta_movement = 9.5 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.centery = self.boss_laser.centery + 9.5 * self.scale_factor_y + delta_movement
                    if 8 >= self.health_bar > 6:
                        delta_movement = 11 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.centery = self.boss_laser.centery + 11 * self.scale_factor_y + delta_movement
                    if 6 >= self.health_bar > 4:
                        delta_movement = 12.5 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.centery = self.boss_laser.centery + 12.5 * self.scale_factor_y + delta_movement
                    if 4 >= self.health_bar > 2:
                        delta_movement = 14 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.centery = self.boss_laser.centery + 14 * self.scale_factor_y + delta_movement
                    if 2 >= self.health_bar > -1:
                        delta_movement = 15.5 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.centery = self.boss_laser.centery + 15.5 * self.scale_factor_y + delta_movement
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.boss_laser.rect.centerx = self.rect.centerx
                self.boss_laser.rect.centery = self.rect.centery + 80 * self.scale_factor_y
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.boss_laser.laser_visible = 0
            self.boss_laser.rect.centerx = self.rect.centerx
            self.boss_laser.rect.centery = self.rect.centery + 80 * self.scale_factor_y
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_boss(self, death_sound, coins_on_screen):
        """
            Kills the boss and plays the enemies death animation. After that, it spawns the boss in a new location.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :return: None
        """

        # When the death animation and respawning is finished, the boss appears on the screen again
        if self.update == 6:
            self.boss_visible = 1
            self.boss_health_bar.health_bar_visible = 1
            self.movement_activated = 0
            self.update = 0
            return

        # Wait 0.05 seconds
        if 4 <= self.update < 6:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.05:
                self.update = 6
                self.start_time = 0
            return

        if self.update == 3.5:
            # Reset the health bar and the enemies health
            self.boss_health_bar.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
            old_center = self.boss_health_bar.rect.center
            self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_1010_TEXTURE)
            self.boss_health_bar.rect = self.boss_health_bar.image.get_rect(center=old_center)
            self.health_bar = 10
            self.update = 4
            self.start_time = time.time()
            return

        if self.update == 3:
            # Hide the boss and spawn a gold coin where the boss died
            self.boss_visible = 0
            platinum_coin = Coin(type="platinum", pos_x=self.rect.centerx, pos_y=self.rect.centery, scale_factor_x=self.scale_factor_x)
            # Set the hitbox for the coin
            platinum_coin.range = (platinum_coin.rect.centerx - platinum_coin.COIN_DISTANCE, platinum_coin.rect.centerx + platinum_coin.COIN_DISTANCE)
            platinum_coin.collision_coordinate = platinum_coin.rect.centery - platinum_coin.COIN_DISTANCE
            coins_on_screen.append(platinum_coin)
            # Respawn the boss in a different random location
            old_center = self.rect.center
            self.image = pygame.image.load(MACHINE_BOSS_TEXTURE)
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
            return

        # Wait 0.15 seconds
        if 1.5 <= self.update < 3:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.15:
                self.update = 3
                self.start_time = 0
            return

        # Change the texture of the boss to the second frame of the explosion
        if 1.0 <= self.update <= 1.1:
            old_center = self.rect.center
            self.image = pygame.image.load(EXPLOSION_2_TEXTURE).convert_alpha()
            self.rect = self.image.get_rect(center=old_center)
            self.update = 1.5
            self.start_time = time.time()
            self.kill_boss(death_sound, coins_on_screen)
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
            # Set health to 0 and hide the health bar
            self.health_bar = 0
            self.boss_health_bar.health_bar_visible = 0
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion.wav")
                sound.play()
            # Change the texture of the boss to the first frame of the death explosion
            old_center = self.rect.center
            self.image = pygame.image.load(EXPLOSION_1_TEXTURE).convert_alpha()
            self.rect = self.image.get_rect(center=old_center)
            self.update = 0.5
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.start_time = time.time()
            return

    def hit_boss(self, hit_sound):
        """
            Makes the enemy take "one hit" of damage and creates a hit delay before the enemy can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        # Reset the hit delay back to 0
        no_hit = 0
        if self.hit_delay == 9:
            self.hit_delay = 0
            no_hit = 1

        # Wait 0.1 seconds
        if 1 <= self.hit_delay < 9:
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.2:
                self.hit_delay = 9
                self.hit_start_time = 0

        if self.hit_delay == 0 and no_hit == 0 and self.update == 0:
            # Decrease the bosses health by the damage amount
            self.health_bar = self.health_bar - machine_mode_setup.damage
            old_center = self.boss_health_bar.rect.center
            if self.health_bar == 9:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_910_TEXTURE)
            elif self.health_bar == 8:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_810_TEXTURE)
            elif self.health_bar == 7:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_710_TEXTURE)
            elif self.health_bar == 6:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_610_TEXTURE)
            elif self.health_bar == 5:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_510_TEXTURE)
            elif self.health_bar == 4:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_410_TEXTURE)
            elif self.health_bar == 3:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_310_TEXTURE)
            elif self.health_bar == 2:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_210_TEXTURE)
            elif self.health_bar == 1:
                self.boss_health_bar.image = pygame.image.load(HEALTH_BAR_110_TEXTURE)
            self.boss_health_bar.rect = self.boss_health_bar.image.get_rect(center=old_center)
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion2.wav")
                sound.play()
            self.hit_delay = 1
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.hit_start_time = time.time()

    def float_effect(self):
        """
            Moves the boss up and down to create a float effect and make it seem as if the boss is moving
                fast through outer space.

            :return: None
        """

        # Activate the float effect
        if self.float_activated == 0:
            self.float_activated = 1
            self.start_y_float = self.rect.centery

        if self.start_y_float - 50 * self.scale_factor_y >= self.rect.centery:
            # Move down
            self.float = -1
        elif self.start_y_float + 50 * self.scale_factor_y <= self.rect.centery:
            # Move up
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
                self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
            elif self.float == -1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = machine_mode_setup.MACHINE_FLOAT * ((elapsed_time - 0.0075) / 0.0075)
                self.float_y += machine_mode_setup.MACHINE_FLOAT + delta_movement
                self.rect.centery = int(self.float_y)
                self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
            self.float_start_time = time.time()

    def move_boss(self, death):
        """
            When the boss has died enough times, this function will cause it to start moving left and
                right, which will speed up the more times that the boss dies.

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
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_4 + delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_6 + delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_8 + delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx + machine_mode_setup.MACHINE_MOVE_10 + delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_2 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_2 - delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_4 - delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_6 - delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_8 - delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.rect.centerx = self.rect.centerx - machine_mode_setup.MACHINE_MOVE_10 - delta_movement
                        self.boss_health_bar.rect.center = (self.rect.centerx, self.rect.centery - 82 * self.scale_factor_y)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0


class BossLaser(pygame.sprite.Sprite):
    def __init__(self, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(MACHINE_BOSS_LASER_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (815 * scale_factor_x, 220 * scale_factor_y)
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


class BossHealthBar(pygame.sprite.Sprite):
    def __init__(self, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.image.load(HEALTH_BAR_1010_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (815 * scale_factor_x, 58 * scale_factor_y)
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
