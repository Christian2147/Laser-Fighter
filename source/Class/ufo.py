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
    File: ufo.py
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

import turtle
import pygame
import random
import time
from Class.coin import Coin


class UFO:
    """
        Represents a UFO in Alien Mode. The UFO hovers in the air and moves towards the player at all times.

        Attributes:
            ufo (turtle.Turtle()): The UFO sprite
            ufo_laser (turtle.Turtle()): The UFO laser sprite
            ufo_health_bar (turtle.Turtle()): The UFO health bar sprite
            death_animation (float): Iterated during the UFOs death animation
            death_count (int): Stores the amount of times the UFO has died since the player has last died
            direction (int): Stores the direction that the UFO is facing (1 = right and 2 = left)
            hit_delay (float):  Delays how often the UFO can be hit
            health (int): Stores the UFOs current health
            got_hit (int): Determines if the UFO has already been hit by the players laser since it was last fired
                (To prevent double hitting).
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
    """

    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates a UFO object and spawns it in the game.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.ufo = turtle.Turtle()
        if fullscreen == 1:
            self.ufo.shape("Textures/Aliens/Alien_Boss_Scaled.gif")
        else:
            self.ufo.shape("Textures/Aliens/Alien_Boss.gif")
        self.ufo.shapesize(1.75 * scale_factor_y, 6 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.ufo.penup()
        self.ufo.goto(875 * scale_factor_x, -20 * scale_factor_y)
        self.ufo.direction = "stop"

        self.ufo_laser = turtle.Turtle()
        if fullscreen == 1:
            self.ufo_laser.shape("Textures/Lasers/Enemy(6-10)_Laser_Scaled.gif")
        else:
            self.ufo_laser.shape("Textures/Lasers/Enemy(6-10)_Laser.gif")
        self.ufo_laser.shapesize(2.25 * scale_factor_y, 0.5 * scale_factor_x)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.ufo_laser.penup()
        self.ufo_laser.goto(877 * scale_factor_x, -90 * scale_factor_y)
        self.ufo_laser.direction = "stop"

        self.ufo_health_bar = turtle.Turtle()
        if fullscreen == 1:
            self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.ufo_health_bar.penup()
        self.ufo_health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        self.ufo_health_bar.goto(875 * scale_factor_x, 50 * scale_factor_y)

        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 10
        self.got_hit = 0
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = time.time()
        self.movement_activated = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.ufo.clear()
        self.ufo_laser.clear()
        self.ufo_health_bar.clear()
        del self.ufo
        del self.ufo_laser
        del self.ufo_health_bar

    def reinstate(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing sprite to spawn a UFO on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        if fullscreen == 1:
            self.ufo.shape("Textures/Aliens/Alien_Boss_Scaled.gif")
        else:
            self.ufo.shape("Textures/Aliens/Alien_Boss.gif")
        self.ufo.goto(875 * scale_factor_x, -20 * scale_factor_y)
        self.ufo.direction = "stop"
        self.ufo.showturtle()

        self.ufo_laser.goto(877 * scale_factor_x, -90 * scale_factor_y)
        self.ufo_laser.direction = "stop"
        self.ufo_laser.showturtle()

        if fullscreen == 1:
            self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        self.ufo_health_bar.goto(875 * scale_factor_x, 50 * scale_factor_y)
        self.ufo_health_bar.showturtle()
        self.move_start_time = time.time()

    def get_ufo(self):
        """
            Returns the UFO sprite so that its class attributes can be accessed.

            :return: ufo: The UFO sprite
            :type: Turtle.turtle()
        """

        return self.ufo

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

        self.ufo.hideturtle()
        self.ufo_laser.hideturtle()
        self.ufo_health_bar.hideturtle()
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.hit_delay = 0
        self.health = 10
        self.got_hit = 0
        self.kill_start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.movement_activated = 0

    def shoot_laser(self, shooting_sound, scale_factor_x, scale_factor_y):
        """
            Shoots the UFOs laser and moves it down to the ground after it is fired.

            :param shooting_sound: Determines whether the toggle for the enemy lasers shooting sound is on. If it is,
                the shooting sound will play when the enemy laser is fired.
            :type shooting_sound: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        self.ufo_laser.showturtle()
        if self.ufo.isvisible() or self.death_animation != 0:
            if self.ufo_laser.ycor() > -600 * scale_factor_y:
                # Move the laser down 3.2 units every 0.0075 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.0075:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 3.2 * scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                    self.ufo_laser.sety(self.ufo_laser.ycor() - 3.2 * scale_factor_y - delta_movement)
                    self.laser_start_time = time.time()
            # If the UFO is not dying
            elif self.death_animation == 0:
                # Fire the laser
                self.ufo_laser.setx(self.ufo.xcor() + 2 * scale_factor_x)
                self.ufo_laser.sety(-90 * scale_factor_y)
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("Sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the ufo is not visible, then stop firing the laser
        else:
            self.ufo_laser.setx(self.ufo.xcor() + 2 * scale_factor_x)
            self.ufo_laser.sety(-90 * scale_factor_y)
            self.laser_start_time = time.time()

        # Make the laser disappear once it hits the ground
        if self.ufo_laser.ycor() < -170 * scale_factor_y:
            self.ufo_laser.hideturtle()

    def set_ufo_direction(self, player_x):
        """
            Sets the direction of the UFO so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.ufo.isvisible():
            # If the players x-coordinate is smaller than the UFOs, then make the UFO face left
            if self.ufo.xcor() > player_x:
                self.ufo.direction = "left"
                self.direction = 2
            # If the players x-coordinate is smaller than the UFOs, then make the UFO face right
            else:
                self.ufo.direction = "right"
                self.direction = 1

    def kill_ufo(self, death_sound, coins_on_screen, all_coins, scale_factor_x, scale_factor_y, fullscreen):
        """
            Kills the UFO and plays the aliens death animation. After that, it respawns the UFO on a random
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
            # Spawn a coin where the UFO has died
            self.ufo.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                platinum_coin = Coin(type="platinum", pos_x=self.ufo.xcor(), pos_y=self.ufo.ycor(), fullscreen=fullscreen)
                coins_on_screen.append(platinum_coin)
                all_coins.append(platinum_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_platinum(pos_x=self.ufo.xcor(), pos_y=self.ufo.ycor(), fullscreen=fullscreen)
                        coins_on_screen.append(coin)
                        break
            # Respawn the UFO in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.ufo.goto(random.randint(-900 * scale_factor_x, -690 * scale_factor_x), -20 * scale_factor_y)
                self.ufo_health_bar.goto(self.ufo.xcor(), 50 * scale_factor_y)
            if alien_random == 2:
                self.ufo.goto(random.randint(690 * scale_factor_x, 900 * scale_factor_x), -20 * scale_factor_y)
                self.ufo_health_bar.goto(self.ufo.xcor(), 50 * scale_factor_y)
            # Reset the UFOs health
            if fullscreen == 1:
                self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
            else:
                self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            if fullscreen == 1:
                self.ufo.shape("Textures/Aliens/Alien_Boss_Scaled.gif")
            else:
                self.ufo.shape("Textures/Aliens/Alien_Boss.gif")
            self.health = 10
            self.ufo.showturtle()
            self.ufo_health_bar.showturtle()
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
            if fullscreen == 1:
                self.ufo.shape("Textures/Explosions/Explosion2_Scaled.gif")
            else:
                self.ufo.shape("Textures/Explosions/Explosion2.gif")
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

        if self.death_animation == 0 and self.got_hit == 0:
            # UFO was hit by the players laser
            self.got_hit = 1
            # Increase the death count
            self.death_count = self.death_count + 1
            self.health = 0
            self.ufo_health_bar.hideturtle()
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion.wav")
                sound.play()
            # Set the texture of the large alien to the first frame in the death scene
            if fullscreen == 1:
                self.ufo.shape("Textures/Explosions/Explosion1_Scaled.gif")
            else:
                self.ufo.shape("Textures/Explosions/Explosion1.gif")
            self.death_animation = 1
            self.kill_start_time = time.time()
            return

    def hit_ufo(self, hit_sound, fullscreen):
        """
            Makes the UFO take "one hit" of damage and creates a hit delay before the UFO can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

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

        if self.death_animation == 0 and self.got_hit == 0:
            # detect that the UFO just got hit by the players laser
            self.got_hit = 1
            # Decrease the aliens health by 1
            if self.health == 10:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.9_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            elif self.health == 9:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.8_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            elif self.health == 8:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.7_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            elif self.health == 7:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.6_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            elif self.health == 6:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.5_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            elif self.health == 5:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.4_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            elif self.health == 4:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.3_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            elif self.health == 3:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.2_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            elif self.health == 2:
                if fullscreen == 1:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.1_Scaled.gif")
                else:
                    self.ufo_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            # Play the hit sound
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion2.wav")
                sound.play()
            self.health = self.health - 1
            self.hit_delay = 1
            self.hit_start_time = time.time()
            return

    def set_movement_speed(self, scale_factor_x):
        """
            Function for the UFOs movement.
            When the UFO has died enough times, this function will cause it to start moving faster and faster.
            Notice how the speed increase is greater than that of regular aliens.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :return: None
        """

        if self.ufo.isvisible() and self.death_animation == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the UFO every 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                # If the UFOs direction is right
                if self.direction == 1:
                    # Move the UFO right
                    if 0 <= self.death_count < 3:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = 0.25 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 0.25 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 0.25 * scale_factor_x + delta_movement)
                    if 3 <= self.death_count < 6:
                        delta_movement = 0.5 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 0.5 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 0.5 * scale_factor_x + delta_movement)
                    if 6 <= self.death_count < 9:
                        delta_movement = 1 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 1 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 1 * scale_factor_x + delta_movement)
                    if 9 <= self.death_count < 12:
                        delta_movement = 1.75 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 1.75 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 1.75 * scale_factor_x + delta_movement)
                    if 12 <= self.death_count < 15:
                        delta_movement = 2.75 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 2.75 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 2.75 * scale_factor_x + delta_movement)
                    if 15 <= self.death_count:
                        delta_movement = 4 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() + 4 * scale_factor_x + delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() + 4 * scale_factor_x + delta_movement)
                # If the UFOs direction is left
                else:
                    # Move the UFO left
                    if 0 <= self.death_count < 3:
                        delta_movement = 0.25 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 0.25 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 0.25 * scale_factor_x - delta_movement)
                    if 3 <= self.death_count < 6:
                        delta_movement = 0.5 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 0.5 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 0.5 * scale_factor_x - delta_movement)
                    if 6 <= self.death_count < 9:
                        delta_movement = 1 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 1 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 1 * scale_factor_x - delta_movement)
                    if 9 <= self.death_count < 12:
                        delta_movement = 1.75 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 1.75 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 1.75 * scale_factor_x - delta_movement)
                    if 12 <= self.death_count < 15:
                        delta_movement = 2.75 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 2.75 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 2.75 * scale_factor_x - delta_movement)
                    if 15 <= self.death_count:
                        delta_movement = 4 * scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.ufo.setx(self.ufo.xcor() - 4 * scale_factor_x - delta_movement)
                        self.ufo_health_bar.setx(self.ufo_health_bar.xcor() - 4 * scale_factor_x - delta_movement)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
