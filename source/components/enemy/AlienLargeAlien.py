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

import turtle
import pygame
import random
import time
from components.ItemCoin import Coin
from setup.TextureSetup import ALIEN_STILL_RIGHT_11_15_TEXTURE
from setup.TextureSetup import ALIEN_STILL_LEFT_11_15_TEXTURE
from setup.TextureSetup import ALIEN_WALKING_RIGHT_11_15_TEXTURE
from setup.TextureSetup import ALIEN_WALKING_LEFT_11_15_TEXTURE
from setup.TextureSetup import ALIEN_DEATH_1_TEXTURE
from setup.TextureSetup import ALIEN_DEATH_2_TEXTURE
from setup.TextureSetup import HEALTH_BAR_13_TEXTURE
from setup.TextureSetup import HEALTH_BAR_23_TEXTURE
from setup.TextureSetup import HEALTH_BAR_33_TEXTURE


class LargeAlien:
    """
        Represents a large alien in Alien Mode. The large alien is significantly taller than the player and moves
            towards the player at all times.

        Attributes:
            large_alien (turtle.Turtle()): The large alien sprite
            large_alien_health_bar (turtle.Turtle()): The large alien health bar sprite
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
    """

    def __init__(self, id, scale_factor_x, scale_factor_y):
        """
            Creates a large alien object with the given id and spawns it in the game.

            :param id: A unique identifier for the large alien
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.large_alien = turtle.Turtle()
        self.large_alien.shape(ALIEN_STILL_RIGHT_11_15_TEXTURE)
        self.large_alien.shapesize(8.5 * scale_factor_y, 3.5 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.large_alien.penup()
        # Set the large aliens initial location based on its id
        if id == 1:
            self.large_alien.goto(-725 * scale_factor_x, -85 * scale_factor_y)
        elif id == 2:
            self.large_alien.goto(775 * scale_factor_x, -85 * scale_factor_y)
        elif id == 3:
            self.large_alien.goto(-775 * scale_factor_x, -85 * scale_factor_y)
        elif id == 4:
            self.large_alien.goto(825 * scale_factor_x, -85 * scale_factor_y)
        elif id == 5:
            self.large_alien.goto(-825 * scale_factor_x, -85 * scale_factor_y)
        self.large_alien.direction = "stop"

        self.large_alien_health_bar = turtle.Turtle()
        self.large_alien_health_bar.shape(HEALTH_BAR_33_TEXTURE)
        self.large_alien_health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.large_alien_health_bar.penup()
        self.large_alien_health_bar.goto(self.large_alien.xcor(), 38 * scale_factor_y)

        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 3
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0
        self.movement_activated = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.large_alien.clear()
        self.large_alien_health_bar.clear()
        del self.large_alien
        del self.large_alien_health_bar

    def reinstate(self, id):
        """
            Reuses the existing sprite to spawn a large alien on the screen

            :param id: A new unique identifier for the medium alien
            :type id: int
        """

        self.large_alien.shape(ALIEN_STILL_RIGHT_11_15_TEXTURE)
        # Initial location based on the large aliens new id
        if id == 1:
            self.large_alien.goto(-725 * self.scale_factor_x, -85 * self.scale_factor_y)
        elif id == 2:
            self.large_alien.goto(775 * self.scale_factor_x, -85 * self.scale_factor_y)
        elif id == 3:
            self.large_alien.goto(-775 * self.scale_factor_x, -85 * self.scale_factor_y)
        elif id == 4:
            self.large_alien.goto(825 * self.scale_factor_x, -85 * self.scale_factor_y)
        elif id == 5:
            self.large_alien.goto(-825 * self.scale_factor_x, -85 * self.scale_factor_y)
        self.large_alien.direction = "stop"
        self.large_alien.showturtle()

        self.large_alien_health_bar.shape(HEALTH_BAR_33_TEXTURE)
        self.large_alien_health_bar.goto(self.large_alien.xcor(), 38 * self.scale_factor_y)
        self.large_alien_health_bar.showturtle()
        self.move_start_time = time.time()

    def get_large_alien(self):
        """
            Returns the large alien sprite so that its class attributes can be accessed.

            :return: large_alien: The large alien sprite
            :type: Turtle.turtle()
        """

        return self.large_alien

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

    def remove(self):
        """
            Removes the large alien sprite form the screen and resets its attributes.

            :return: None
        """

        self.large_alien.hideturtle()
        self.large_alien_health_bar.hideturtle()
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 3
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0

    def set_alien_direction(self, player_x):
        """
            Sets the direction of the large alien so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.large_alien.isvisible():
            # If the players x-coordinate is smaller than the large aliens, then make the large alien face left
            if self.large_alien.xcor() > player_x:
                self.large_alien.direction = "left"
                self.direction = 2
            # If the players x-coordinate is smaller than the large aliens, then make the large alien face right
            else:
                self.large_alien.direction = "right"
                self.direction = 1

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
            if self.direction == 1 and self.death_animation == 0:
                # Make the large alien face and walk right
                if right_update % 0.5 != 0:
                    self.large_alien.shape(ALIEN_WALKING_RIGHT_11_15_TEXTURE)
                else:
                    self.large_alien.shape(ALIEN_STILL_RIGHT_11_15_TEXTURE)
            # If the large aliens direction is left
            elif self.direction == 2 and self.death_animation == 0:
                # Make the large alien face and walk left
                if left_update % 0.5 != 0:
                    self.large_alien.shape(ALIEN_WALKING_LEFT_11_15_TEXTURE)
                else:
                    self.large_alien.shape(ALIEN_STILL_LEFT_11_15_TEXTURE)
            self.walk_start_time = time.time()

    def kill_alien(self, death_sound, coins_on_screen, all_coins):
        """
            Kills the alien and plays the aliens death animation. After that, it respawns the alien on a random
                side of the screen.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :param all_coins: Array that lists all of the coin sprites generated since the
                programs execution (for reusing purposes)
            :type all_coins: list

            :return: None
        """

        if 4 <= self.death_animation < 5:
            # Spawn a coin where the alien has died
            self.large_alien.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                gold_coin = Coin(type="gold", pos_x=self.large_alien.xcor(), pos_y=self.large_alien.ycor())
                coins_on_screen.append(gold_coin)
                all_coins.append(gold_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_gold(pos_x=self.large_alien.xcor(), pos_y=self.large_alien.ycor())
                        coins_on_screen.append(coin)
                        break
            # Respawn the large alien in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.large_alien.goto(random.randint(-900 * self.scale_factor_x, -690 * self.scale_factor_x), -85 * self.scale_factor_y)
                self.large_alien_health_bar.goto(self.large_alien.xcor(), 38 * self.scale_factor_y)
            if alien_random == 2:
                self.large_alien.goto(random.randint(690 * self.scale_factor_x, 900 * self.scale_factor_x), -85 * self.scale_factor_y)
                self.large_alien_health_bar.goto(self.large_alien.xcor(), 38 * self.scale_factor_y)
            # Reset the large aliens health
            self.large_alien_health_bar.shape(HEALTH_BAR_33_TEXTURE)
            self.health = 3
            self.large_alien.showturtle()
            self.large_alien_health_bar.showturtle()
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
            self.large_alien.shape(ALIEN_DEATH_2_TEXTURE)
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
            self.large_alien_health_bar.hideturtle()
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Alien_Death_Sound.wav")
                sound.play()
            # Set the texture of the large alien to the first frame in the death scene
            self.large_alien.shape(ALIEN_DEATH_1_TEXTURE)
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
            if self.health == 3:
                self.large_alien_health_bar.shape(HEALTH_BAR_23_TEXTURE)
            elif self.health == 2:
                self.large_alien_health_bar.shape(HEALTH_BAR_13_TEXTURE)
            # Play the hit sound
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Alien_Hit_Sound.wav")
                sound.play()
            self.health = self.health - 1
            self.hit_delay = 1
            self.hit_start_time = time.time()
            return

    def set_movement_speed(self):
        """
            Function for the large aliens movement.
            When the large alien has died enough times, this function will cause it to start moving faster and faster.

            :return: None
        """

        if self.large_alien.isvisible() and self.death_animation == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the large alien every 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                # If the aliens direction is right
                if self.direction == 1:
                    # Move the alien right
                    if 0 <= self.death_count < 6:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 0.3 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 0.3 * self.scale_factor_x + delta_movement)
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 0.6 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 0.6 * self.scale_factor_x + delta_movement)
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 0.9 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 0.9 * self.scale_factor_x + delta_movement)
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 1.2 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 1.2 * self.scale_factor_x + delta_movement)
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 1.5 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 1.5 * self.scale_factor_x + delta_movement)
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() + 1.8 * self.scale_factor_x + delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() + 1.8 * self.scale_factor_x + delta_movement)
                # If the aliens direction is left
                else:
                    # Move the alien left
                    if 0 <= self.death_count < 6:
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 0.3 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 0.3 * self.scale_factor_x - delta_movement)
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 0.6 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 0.6 * self.scale_factor_x - delta_movement)
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 0.9 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 0.9 * self.scale_factor_x - delta_movement)
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 1.2 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 1.2 * self.scale_factor_x - delta_movement)
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 1.5 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 1.5 * self.scale_factor_x - delta_movement)
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.large_alien.setx(self.large_alien.xcor() - 1.8 * self.scale_factor_x - delta_movement)
                        self.large_alien_health_bar.setx(self.large_alien_health_bar.xcor() - 1.8 * self.scale_factor_x - delta_movement)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
