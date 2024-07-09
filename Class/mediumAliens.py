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
    File: mediumAliens.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to the Medium Aliens in Alien Mode.
    The medium alien is the second enemy the player encounters in Alien Mode.
    The medium aliens will always move towards the player and moves faster the more times they are killed.
    When they come into contact with the player, they reduce the players health.
    The medium alien dies in two hits from the players laser and grants the player two points.
    The medium alien also grants the player 1 point when it is hit for the first time.
"""

import turtle
import pygame
import random
import time
from Class.coin import Coin


class MediumAlien:
    """
        Represents a medium alien in Alien Mode. The medium alien is slightly taller than the player and moves towards
            the player at all times.

        Attributes:
            medium_alien (turtle.Turtle()): The medium alien sprite
            medium_alien_health_bar (turtle.Turtle()): The medium alien health bar sprite
            death_animation (float): Iterated during the medium aliens death animation
            death_count (int): Stores the amount of times the medium alien has died since the player has last died
            direction (int): Stores the direction that the medium alien is facing (1 = right and 2 = left)
            hit_delay (float):  Delays how often the medium alien can be hit
            health (int): Stores the medium aliens current health
            kill_start_time (float): Used as a timestamp for the death animation of the medium alien (To make the
                animation run in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit delay of the medium alien (To make sure that the
                hit delay lasts a consistent amount of time)
            walk_start_time (float): Used as a timestamp for the medium aliens walking texture update (To make sure the
                walking animation happens in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the medium aliens movement (To make the medium aliens
                movement happen in a consistent amount of time and not based on code execution speed)
    """

    def __init__(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates a medium alien object with the given id and spawns it in the game.

            :param id: A unique identifier for the medium alien
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.medium_alien = turtle.Turtle()
        if fullscreen == 1:
            self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10)_Scaled.gif")
        else:
            self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        self.medium_alien.shapesize(5.5 * scale_factor_y, 3 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.medium_alien.penup()
        # Set the medium aliens initial location based on its id
        if id == 1:
            self.medium_alien.goto(850 * scale_factor_x, -124 * scale_factor_y)
        elif id == 2:
            self.medium_alien.goto(-850 * scale_factor_x, -124 * scale_factor_y)
        elif id == 3:
            self.medium_alien.goto(900 * scale_factor_x, -124 * scale_factor_y)
        elif id == 4:
            self.medium_alien.goto(-900 * scale_factor_x, -124 * scale_factor_y)
        elif id == 5:
            self.medium_alien.goto(725 * scale_factor_x, -124 * scale_factor_y)
        self.medium_alien.direction = "stop"

        self.medium_alien_health_bar = turtle.Turtle()
        if fullscreen == 1:
            self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2_Scaled.gif")
        else:
            self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        self.medium_alien_health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.medium_alien_health_bar.penup()
        self.medium_alien_health_bar.goto(self.medium_alien.xcor(), -39 * scale_factor_y)

        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 2
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.medium_alien.clear()
        self.medium_alien_health_bar.clear()
        del self.medium_alien
        del self.medium_alien_health_bar

    def reinstate(self, id, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing sprite to spawn a medium alien on the screen

            :param id: A new unique identifier for the medium alien
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        if fullscreen == 1:
            self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10)_Scaled.gif")
        else:
            self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
        # Initial location based on the medium aliens new id
        if id == 1:
            self.medium_alien.goto(850 * scale_factor_x, -124 * scale_factor_y)
        elif id == 2:
            self.medium_alien.goto(-850 * scale_factor_x, -124 * scale_factor_y)
        elif id == 3:
            self.medium_alien.goto(900 * scale_factor_x, -124 * scale_factor_y)
        elif id == 4:
            self.medium_alien.goto(-900 * scale_factor_x, -124 * scale_factor_y)
        elif id == 5:
            self.medium_alien.goto(725 * scale_factor_x, -124 * scale_factor_y)
        self.medium_alien.direction = "stop"
        self.medium_alien.showturtle()

        if fullscreen == 1:
            self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2_Scaled.gif")
        else:
            self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
        self.medium_alien_health_bar.goto(self.medium_alien.xcor(), -39 * scale_factor_y)
        self.medium_alien_health_bar.showturtle()

    def get_medium_alien(self):
        """
            Returns the medium alien sprite so that its class attributes can be accessed.

            :return: medium_alien: The medium alien sprite
            :type: Turtle.turtle()
        """

        return self.medium_alien

    def get_medium_alien_health_bar(self):
        """
            Returns the medium aliens health bar sprite so that its class attributes can be accessed.

            :return: medium_alien_health_bar: The medium aliens health bar sprite
            :type: Turtle.turtle()
        """

        return self.medium_alien_health_bar

    def get_medium_alien_health(self):
        """
            Returns the medium aliens current health.

            :return: health: The medium aliens current health
            :type: int
        """

        return self.health

    def get_death_animation(self):
        """
            Returns the current state of the medium aliens death animation (0 if it is not happening)

            :return: death_animation: The current state of the medium aliens death animation
            :type: float
        """

        return self.death_animation

    def get_hit_delay(self):
        """
            Returns the current state of the medium aliens hit delay (0 if it is not happening)

            :return: hit_delay: The current state of the medium aliens hit delay
            :type: float
        """

        return self.hit_delay

    def remove(self):
        """
            Removes the medium alien sprite form the screen and resets its attributes.

            :return: None
        """

        self.medium_alien.hideturtle()
        self.medium_alien_health_bar.hideturtle()
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 2
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0

    def set_alien_direction(self, player_x):
        """
            Sets the direction of the medium alien so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.medium_alien.isvisible():
            # If the players x-coordinate is smaller than the medium aliens, then make the medium alien face left
            if self.medium_alien.xcor() > player_x:
                self.medium_alien.direction = "left"
                self.direction = 2
            # If the players x-coordinate is larger than the medium aliens, then make the medium alien face right
            else:
                self.medium_alien.direction = "right"
                self.direction = 1

    def set_alien_texture(self, right_update, left_update, fullscreen):
        """
            Sets the medium aliens texture based on the medium aliens direction and creates a walking animation when the
                medium alien is walking.

            :param right_update: Used to update the walking right animation correctly
            :type right_update: float

            :param left_update: Used to update the walking left animation correctly
            :type left_update: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        # Updates the walking animation every 0.005 seconds
        current_time = time.time()
        elapsed_time = current_time - self.walk_start_time
        if elapsed_time >= 0.005:
            # If the medium aliens direction is right
            if self.direction == 1 and self.death_animation == 0:
                # Make the medium alien face and walk right
                if right_update % 0.5 != 0:
                    if fullscreen == 1:
                        self.medium_alien.shape("Textures/Aliens/Alien_Walking_Right(6-10)_Scaled.gif")
                    else:
                        self.medium_alien.shape("Textures/Aliens/Alien_Walking_Right(6-10).gif")
                else:
                    if fullscreen == 1:
                        self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10)_Scaled.gif")
                    else:
                        self.medium_alien.shape("Textures/Aliens/Alien_Still_Right(6-10).gif")
            # If the medium aliens direction is left
            elif self.direction == 2 and self.death_animation == 0:
                # Make the medium alien face and walk left
                if left_update % 0.5 != 0:
                    if fullscreen == 1:
                        self.medium_alien.shape("Textures/Aliens/Alien_Walking_Left(6-10)_Scaled.gif")
                    else:
                        self.medium_alien.shape("Textures/Aliens/Alien_Walking_Left(6-10).gif")
                else:
                    if fullscreen == 1:
                        self.medium_alien.shape("Textures/Aliens/Alien_Still_Left(6-10)_Scaled.gif")
                    else:
                        self.medium_alien.shape("Textures/Aliens/Alien_Still_Left(6-10).gif")
            self.walk_start_time = time.time()

    def kill_alien(self, death_sound, coins_on_screen, all_coins, scale_factor_x, scale_factor_y, fullscreen):
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

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if 4 <= self.death_animation < 5:
            # Spawn a coin where the alien has died
            self.medium_alien.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                silver_coin = Coin(type="silver", pos_x=self.medium_alien.xcor(), pos_y=self.medium_alien.ycor(), fullscreen=fullscreen)
                coins_on_screen.append(silver_coin)
                all_coins.append(silver_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_silver(pos_x=self.medium_alien.xcor(), pos_y=self.medium_alien.ycor(), fullscreen=fullscreen)
                        coins_on_screen.append(coin)
                        break
            # Respawn the medium alien in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.medium_alien.goto(random.randint(-900 * scale_factor_x, -690 * scale_factor_x), -124 * scale_factor_y)
                self.medium_alien_health_bar.goto(self.medium_alien.xcor(), -39 * scale_factor_y)
            if alien_random == 2:
                self.medium_alien.goto(random.randint(690 * scale_factor_x, 900 * scale_factor_x), -124 * scale_factor_y)
                self.medium_alien_health_bar.goto(self.medium_alien.xcor(), -39 * scale_factor_y)
            # Reset the medium aliens health
            if fullscreen == 1:
                self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2_Scaled.gif")
            else:
                self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.2.gif")
            self.health = 2
            self.medium_alien.showturtle()
            self.medium_alien_health_bar.showturtle()
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
            # Change the medium aliens texture to the second frame in the death scene
            if fullscreen == 1:
                self.medium_alien.shape("Textures/Explosions/Alien_Death_2_Scaled.gif")
            else:
                self.medium_alien.shape("Textures/Explosions/Alien_Death_2.gif")
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
            self.medium_alien_health_bar.hideturtle()
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Alien_Death_Sound.wav")
                sound.play()
            # Set the texture of the medium alien to the first frame in the death scene
            if fullscreen == 1:
                self.medium_alien.shape("Textures/Explosions/Alien_Death_1_Scaled.gif")
            else:
                self.medium_alien.shape("Textures/Explosions/Alien_Death_1.gif")
            self.death_animation = 1
            self.kill_start_time = time.time()
            return

    def hit_alien(self, hit_sound, fullscreen):
        """
            Makes the medium alien take "one hit" of damage and creates a hit delay before the medium alien can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

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

        if self.death_animation == 0 and self.health == 2:
            # Decrease the aliens health by 1
            if fullscreen == 1:
                self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.1_Scaled.gif")
            else:
                self.medium_alien_health_bar.shape("Textures/Health_Bars/HealthBar_2.1.gif")
            # Play the hit sound
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Alien_Hit_Sound.wav")
                sound.play()
            self.health = 1
            self.hit_delay = 1
            self.hit_start_time = time.time()
            return

    def set_movement_speed(self, scale_factor_x):
        """
            Function for the medium aliens movement.
            When the medium alien has died enough times, this function will cause it to start moving faster and faster.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :return: None
        """

        if self.medium_alien.isvisible() and self.death_animation == 0:
            # Move the medium alien every 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                # If the aliens direction is right
                if self.direction == 1:
                    # Move the alien right
                    if 0 <= self.death_count < 6:
                        self.medium_alien.setx(self.medium_alien.xcor() + 0.3 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 0.3 * scale_factor_x)
                    if 6 <= self.death_count < 12:
                        self.medium_alien.setx(self.medium_alien.xcor() + 0.6 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 0.6 * scale_factor_x)
                    if 12 <= self.death_count < 18:
                        self.medium_alien.setx(self.medium_alien.xcor() + 0.9 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 0.9 * scale_factor_x)
                    if 18 <= self.death_count < 24:
                        self.medium_alien.setx(self.medium_alien.xcor() + 1.2 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 1.2 * scale_factor_x)
                    if 24 <= self.death_count < 30:
                        self.medium_alien.setx(self.medium_alien.xcor() + 1.5 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 1.5 * scale_factor_x)
                    if 30 <= self.death_count:
                        self.medium_alien.setx(self.medium_alien.xcor() + 1.8 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() + 1.8 * scale_factor_x)
                # If the aliens direction is left
                else:
                    # Move the alien left
                    if 0 <= self.death_count < 6:
                        self.medium_alien.setx(self.medium_alien.xcor() - 0.3 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 0.3 * scale_factor_x)
                    if 6 <= self.death_count < 12:
                        self.medium_alien.setx(self.medium_alien.xcor() - 0.6 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 0.6 * scale_factor_x)
                    if 12 <= self.death_count < 18:
                        self.medium_alien.setx(self.medium_alien.xcor() - 0.9 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 0.9 * scale_factor_x)
                    if 18 <= self.death_count < 24:
                        self.medium_alien.setx(self.medium_alien.xcor() - 1.2 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 1.2 * scale_factor_x)
                    if 24 <= self.death_count < 30:
                        self.medium_alien.setx(self.medium_alien.xcor() - 1.5 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 1.5 * scale_factor_x)
                    if 30 <= self.death_count:
                        self.medium_alien.setx(self.medium_alien.xcor() - 1.8 * scale_factor_x)
                        self.medium_alien_health_bar.setx(self.medium_alien_health_bar.xcor() - 1.8 * scale_factor_x)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0