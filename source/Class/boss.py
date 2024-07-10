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
    File: boss.py
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

import turtle
import pygame
import random
import time
from Class.coin import Coin


class Boss:
    """
        Represents the boss in Machine Mode. The final enemy in Machine Mode that is pink
            and fires pink lasers.

        Attributes:
            boss (turtle.Turtle()): The boss enemy sprite.
            boss_laser (turtle.Turtle()): The laser sprite for the boss.
            boss_health_bar (turtle.Turtle()): The health bar sprite for the boss.
            death_count (int): Stores the death count for the enemy since the player has last died.
            health_bar (int): Stores the current health of the enemy
            hit_delay (int): Delays how often the enemy can be hit
            update (float): Value that is incremented during the death animation of the enemy.
            movement (int): Stores the direction that the enemy is supposed to move on
                the x-axis (1 = right and -1 = left)
            float (int): Stores the direction that the enemy is supposed to move on the y-axis (1 = up and -1 == down)
            float_movement (int): Stores the distance that the enemy has moved on the y-axis during the float from the
                initial starting point (When this goes over 110, the direction of movement switches)
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
    """

    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates a boss object and spawns it on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.boss = turtle.Turtle()
        if fullscreen == 1:
            self.boss.shape("Textures/Enemies/Boss_Scaled.gif")
        else:
            self.boss.shape("Textures/Enemies/Boss.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.boss.penup()
        self.boss.shapesize(2 * scale_factor_y, 2 * scale_factor_x)
        self.boss.goto(175 * scale_factor_x, 220 * scale_factor_y)
        self.boss.direction = "down"

        self.boss_laser = turtle.Turtle()
        if fullscreen == 1:
            self.boss_laser.shape("Textures/Lasers/Boss_Laser_Scaled.gif")
        else:
            self.boss_laser.shape("Textures/Lasers/Boss_Laser.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.boss_laser.penup()
        self.boss_laser.shapesize(2.25 * scale_factor_y, 0.5 * scale_factor_x)
        self.boss_laser.goto(175 * scale_factor_x, 140 * scale_factor_y)
        self.boss_laser.direction = "down"

        self.boss_health_bar = turtle.Turtle()
        if fullscreen == 1:
            self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.boss_health_bar.penup()
        self.boss_health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        self.boss_health_bar.goto(175 * scale_factor_x, 302 * scale_factor_y)

        self.death_count = 0
        self.health_bar = 10
        self.hit_delay = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.float_movement = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.boss.hideturtle()
        self.boss_laser.hideturtle()
        self.boss_health_bar.hideturtle()
        self.boss.clear()
        self.boss_laser.clear()
        self.boss_health_bar.clear()
        del self.boss
        del self.boss_laser
        del self.boss_health_bar

    def reinstate(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing sprite to spawn a boss on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if fullscreen == 1:
            self.boss.shape("Textures/Enemies/Boss_Scaled.gif")
        else:
            self.boss.shape("Textures/Enemies/Boss.gif")
        if fullscreen == 1:
            self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        self.boss.goto(175 * scale_factor_x, 220 * scale_factor_y)
        self.boss_laser.goto(175 * scale_factor_x, 140 * scale_factor_y)
        self.boss_health_bar.goto(175 * scale_factor_x, 302 * scale_factor_y)
        self.boss.direction = "down"
        self.boss_laser.direction = "down"
        self.boss.showturtle()
        self.boss_laser.showturtle()
        self.boss_health_bar.showturtle()

    def get_boss(self):
        """
            Returns the boss sprite so its class attributes can be accessed

            :return: boss: the boss sprite
            :type: turtle.Turtle()
        """

        return self.boss

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

        self.boss.hideturtle()
        self.boss_laser.hideturtle()
        self.boss_health_bar.hideturtle()
        self.death_count = 0
        self.hit_delay = 0
        self.health_bar = 10
        self.update = 0
        self.movement = 1
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0

    def shoot_laser(self, green_power_up, shooting_sound, scale_factor_y):
        """
            Shoots the boss laser (Spawning it right below the sprite) and move it down across the screen. The laser
                moves faster and faster the lower the bosses health goes.

            :param green_power_up: Variable used to determine if the green power up is active or not. If it is active,
                the enemy laser will not fire.
            :type green_power_up: int

            :param shooting_sound: Determines whether the toggle for the enemy lasers shooting sound is on. If it is,
                the shooting sound will play when the enemy laser is fired.
            :type shooting_sound: int

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        if green_power_up == 0:
            # Remove the laser from the screen once it has hit the player
            if self.laser_has_attacked == 1:
                self.boss_laser.hideturtle()
            else:
                self.boss_laser.showturtle()
            # If the laser is still visible in the frame of the screen
            if self.boss_laser.ycor() > -360 * scale_factor_y:
                # Keep moving the laser down the screen every 0.01 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.01:
                    # Speed depends on the bosses health
                    if 10 >= self.health_bar > 8:
                        self.boss_laser.sety(self.boss_laser.ycor() - 9.5 * scale_factor_y)
                    if 8 >= self.health_bar > 6:
                        self.boss_laser.sety(self.boss_laser.ycor() - 11 * scale_factor_y)
                    if 6 >= self.health_bar > 4:
                        self.boss_laser.sety(self.boss_laser.ycor() - 12.5 * scale_factor_y)
                    if 4 >= self.health_bar > 2:
                        self.boss_laser.sety(self.boss_laser.ycor() - 14 * scale_factor_y)
                    if 2 >= self.health_bar > -1:
                        self.boss_laser.sety(self.boss_laser.ycor() - 15.5 * scale_factor_y)
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.boss_laser.setx(self.boss.xcor())
                self.boss_laser.sety(self.boss.ycor() - 80 * scale_factor_y)
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("Sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.boss_laser.hideturtle()
            self.boss_laser.setx(self.boss.xcor())
            self.boss_laser.sety(self.boss.ycor() - 80 * scale_factor_y)
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_boss(self, death_sound, coins_on_screen, all_coins, scale_factor_x, scale_factor_y, fullscreen):
        """
            Kills the boss and plays the enemies death animation. After that, it spawns the boss in a new location.

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

        # When the death animation and respawning is finished, the boss appears on the screen again
        if self.update == 6:
            self.boss.showturtle()
            self.boss_health_bar.showturtle()
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
            self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
            if fullscreen == 1:
                self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
            else:
                self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            self.health_bar = 10
            self.update = 4
            self.start_time = time.time()
            return

        if self.update == 3:
            # Hide the boss and spawn a gold coin where the boss died
            self.boss.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                platinum_coin = Coin(type="platinum", pos_x=self.boss.xcor(), pos_y=self.boss.ycor(), fullscreen=fullscreen)
                coins_on_screen.append(platinum_coin)
                all_coins.append(platinum_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_platinum(pos_x=self.boss.xcor(), pos_y=self.boss.ycor(), fullscreen=fullscreen)
                        coins_on_screen.append(coin)
                        break
            # Respawn the boss in a different random location
            if fullscreen == 1:
                self.boss.shape("Textures/Enemies/Boss_Scaled.gif")
            else:
                self.boss.shape("Textures/Enemies/Boss.gif")
            # Want to cast these ranges to integers to avoid a crash at certain resolutions
            self.boss.goto(random.randint(int(-640 * scale_factor_x), int(640 * scale_factor_x)), random.randint(int(120 * scale_factor_y), int(220 * scale_factor_y)))
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
            if fullscreen == 1:
                self.boss.shape("Textures/Explosions/Explosion2_Scaled.gif")
            else:
                self.boss.shape("Textures/Explosions/Explosion2.gif")
            self.update = 1.5
            self.start_time = time.time()
            self.kill_boss(death_sound, coins_on_screen, all_coins, scale_factor_x, scale_factor_y, fullscreen)
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
            self.boss_health_bar.hideturtle()
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion.wav")
                sound.play()
            # Change the texture of the boss to the first frame of the death explosion
            if fullscreen == 1:
                self.boss.shape("Textures/Explosions/Explosion1_Scaled.gif")
            else:
                self.boss.shape("Textures/Explosions/Explosion1.gif")
            self.update = 0.5
            self.start_time = time.time()
            return

    def hit_boss(self, hit_sound, fullscreen):
        """
            Makes the enemy take "one hit" of damage and creates a hit delay before the enemy can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

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
            # Decrease the bosses health by 1
            if self.health_bar == 10:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.9_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            elif self.health_bar == 9:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.8_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            elif self.health_bar == 8:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.7_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            elif self.health_bar == 7:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.6_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            elif self.health_bar == 6:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.5_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            elif self.health_bar == 5:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.4_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            elif self.health_bar == 4:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.3_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            elif self.health_bar == 3:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.2_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            elif self.health_bar == 2:
                if fullscreen == 1:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.1_Scaled.gif")
                else:
                    self.boss_health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion2.wav")
                sound.play()
            self.hit_delay = 1
            self.health_bar = self.health_bar - 1
            self.hit_start_time = time.time()

    def float_effect(self, scale_factor_y):
        """
            Moves the boss up and down to create a float effect and make it seem as if the boss is moving
                fast through outer space.

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        if self.float_movement == 110 and self.float == 1:
            # Move down
            self.float = -1
            self.float_movement = 0
        elif self.float_movement == 110 and self.float == -1:
            # Move up
            self.float = 1
            self.float_movement = 0
        current_time = time.time()
        elapsed_time = current_time - self.float_start_time
        # Make a movement every 0.0075 seconds to reduce the effects of lag
        if elapsed_time >= 0.0075:
            if self.float == 1:
                self.boss.goto(self.boss.xcor(), self.boss.ycor() + 0.3 * scale_factor_y)
                self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                self.float_movement = self.float_movement + 1
            elif self.float == -1:
                self.boss.goto(self.boss.xcor(), self.boss.ycor() - 0.3 * scale_factor_y)
                self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                self.float_movement = self.float_movement + 1
            self.float_start_time = time.time()

    def move_boss(self, death, scale_factor_x, scale_factor_y):
        """
            When the boss has died enough times, this function will cause it to start moving left and
                right, which will speed up the more times that the boss dies.

            :param death: Determines whether the death animation for the player is active or not.
            :type death: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :return: None
        """

        if self.death_count >= 4 and death == 0 and self.update == 0:
            # Move the boss every 0.02 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.02:
                # Boss reaches the right end of the screen
                if 600 * scale_factor_x < self.boss.xcor() < 650 * scale_factor_x:
                    # Move left
                    self.movement = -1
                # Boss reaches the left end of the screen
                if -600 * scale_factor_x > self.boss.xcor() > -650 * scale_factor_x:
                    # Move right
                    self.movement = 1
                if self.movement == 1:
                    # Speeds up based on the death_count variable
                    if 4 <= self.death_count < 7:
                        self.boss.setx(self.boss.xcor() + 2 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        self.boss.setx(self.boss.xcor() + 4 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        self.boss.setx(self.boss.xcor() + 6 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        self.boss.setx(self.boss.xcor() + 8 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 16 <= self.death_count:
                        self.boss.setx(self.boss.xcor() + 10 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        self.boss.setx(self.boss.xcor() - 2 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        self.boss.setx(self.boss.xcor() - 4 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        self.boss.setx(self.boss.xcor() - 6 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        self.boss.setx(self.boss.xcor() - 8 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                    elif 16 <= self.death_count:
                        self.boss.setx(self.boss.xcor() - 10 * scale_factor_x)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * scale_factor_y)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
