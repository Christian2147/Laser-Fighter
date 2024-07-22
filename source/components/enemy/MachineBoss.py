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

import turtle
import pygame
import random
import time
from components.ItemCoin import Coin
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
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Creates a boss object and spawns it on the screen

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.boss = turtle.Turtle()
        self.boss.shape(MACHINE_BOSS_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.boss.penup()
        self.boss.shapesize(2 * scale_factor_y, 2 * scale_factor_x)
        self.boss.goto(175 * scale_factor_x, 220 * scale_factor_y)
        self.boss.direction = "down"

        self.boss_laser = turtle.Turtle()
        self.boss_laser.shape(MACHINE_BOSS_LASER_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.boss_laser.penup()
        self.boss_laser.shapesize(2.25 * scale_factor_y, 0.5 * scale_factor_x)
        self.boss_laser.goto(175 * scale_factor_x, 140 * scale_factor_y)
        self.boss_laser.direction = "down"

        self.boss_health_bar = turtle.Turtle()
        self.boss_health_bar.shape(HEALTH_BAR_1010_TEXTURE)
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
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = time.time()
        self.float_start_time = time.time()
        self.laser_has_attacked = 0
        self.movement_activated = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

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

    def reinstate(self):
        """
            Reuses the existing sprite to spawn a boss on the screen

            :return: None
        """

        self.boss.shape(MACHINE_BOSS_TEXTURE)
        self.boss_health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        self.boss.goto(175 * self.scale_factor_x, 220 * self.scale_factor_y)
        self.boss_laser.goto(175 * self.scale_factor_x, 140 * self.scale_factor_y)
        self.boss_health_bar.goto(175 * self.scale_factor_x, 302 * self.scale_factor_y)
        self.boss.direction = "down"
        self.boss_laser.direction = "down"
        self.boss.showturtle()
        self.boss_laser.showturtle()
        self.boss_health_bar.showturtle()
        self.move_start_time = time.time()
        self.float_start_time = time.time()

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
                self.boss_laser.hideturtle()
            else:
                self.boss_laser.showturtle()
            # If the laser is still visible in the frame of the screen
            if self.boss_laser.ycor() > -360 * self.scale_factor_y:
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
                        self.boss_laser.sety(self.boss_laser.ycor() - 9.5 * self.scale_factor_y - delta_movement)
                    if 8 >= self.health_bar > 6:
                        delta_movement = 11 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.sety(self.boss_laser.ycor() - 11 * self.scale_factor_y - delta_movement)
                    if 6 >= self.health_bar > 4:
                        delta_movement = 12.5 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.sety(self.boss_laser.ycor() - 12.5 * self.scale_factor_y - delta_movement)
                    if 4 >= self.health_bar > 2:
                        delta_movement = 14 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.sety(self.boss_laser.ycor() - 14 * self.scale_factor_y - delta_movement)
                    if 2 >= self.health_bar > -1:
                        delta_movement = 15.5 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                        self.boss_laser.sety(self.boss_laser.ycor() - 15.5 * self.scale_factor_y - delta_movement)
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.boss_laser.setx(self.boss.xcor())
                self.boss_laser.sety(self.boss.ycor() - 80 * self.scale_factor_y)
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("Sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.boss_laser.hideturtle()
            self.boss_laser.setx(self.boss.xcor())
            self.boss_laser.sety(self.boss.ycor() - 80 * self.scale_factor_y)
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_boss(self, death_sound, coins_on_screen, all_coins):
        """
            Kills the boss and plays the enemies death animation. After that, it spawns the boss in a new location.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :param all_coins: Array that lists all of the coin sprites generated since the
                programs execution (for reusing purposes)
            :type all_coins: list

            :return: None
        """

        # When the death animation and respawning is finished, the boss appears on the screen again
        if self.update == 6:
            self.boss.showturtle()
            self.boss_health_bar.showturtle()
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
            self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
            self.boss_health_bar.shape(HEALTH_BAR_1010_TEXTURE)
            self.health_bar = 10
            self.update = 4
            self.start_time = time.time()
            return

        if self.update == 3:
            # Hide the boss and spawn a gold coin where the boss died
            self.boss.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                platinum_coin = Coin(type="platinum", pos_x=self.boss.xcor(), pos_y=self.boss.ycor())
                coins_on_screen.append(platinum_coin)
                all_coins.append(platinum_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_platinum(pos_x=self.boss.xcor(), pos_y=self.boss.ycor())
                        coins_on_screen.append(coin)
                        break
            # Respawn the boss in a different random location
            self.boss.shape(MACHINE_BOSS_TEXTURE)
            # Want to cast these ranges to integers to avoid a crash at certain resolutions
            self.boss.goto(random.randint(int(-640 * self.scale_factor_x), int(640 * self.scale_factor_x)), random.randint(int(120 * self.scale_factor_y), int(220 * self.scale_factor_y)))
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
            self.boss.shape(EXPLOSION_2_TEXTURE)
            self.update = 1.5
            self.start_time = time.time()
            self.kill_boss(death_sound, coins_on_screen, all_coins)
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
            self.boss.shape(EXPLOSION_1_TEXTURE)
            self.update = 0.5
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
            # Decrease the bosses health by 1
            if self.health_bar == 10:
                self.boss_health_bar.shape(HEALTH_BAR_910_TEXTURE)
            elif self.health_bar == 9:
                self.boss_health_bar.shape(HEALTH_BAR_810_TEXTURE)
            elif self.health_bar == 8:
                self.boss_health_bar.shape(HEALTH_BAR_710_TEXTURE)
            elif self.health_bar == 7:
                self.boss_health_bar.shape(HEALTH_BAR_610_TEXTURE)
            elif self.health_bar == 6:
                self.boss_health_bar.shape(HEALTH_BAR_510_TEXTURE)
            elif self.health_bar == 5:
                self.boss_health_bar.shape(HEALTH_BAR_410_TEXTURE)
            elif self.health_bar == 4:
                self.boss_health_bar.shape(HEALTH_BAR_310_TEXTURE)
            elif self.health_bar == 3:
                self.boss_health_bar.shape(HEALTH_BAR_210_TEXTURE)
            elif self.health_bar == 2:
                self.boss_health_bar.shape(HEALTH_BAR_110_TEXTURE)
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion2.wav")
                sound.play()
            self.hit_delay = 1
            self.health_bar = self.health_bar - 1
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
            self.start_y_float = self.boss.ycor()

        if self.start_y_float + 50 < self.boss.ycor():
            # Move down
            self.float = -1
        elif self.start_y_float - 50 > self.boss.ycor():
            # Move up
            self.float = 1
        current_time = time.time()
        elapsed_time = current_time - self.float_start_time
        # Make a movement every 0.0075 seconds to reduce the effects of lag
        if elapsed_time >= 0.0075:
            if self.float == 1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = 0.15 * self.scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                self.boss.goto(self.boss.xcor(), self.boss.ycor() + 0.15 * self.scale_factor_y + delta_movement)
                self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
            elif self.float == -1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = 0.15 * self.scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                self.boss.goto(self.boss.xcor(), self.boss.ycor() - 0.15 * self.scale_factor_y - delta_movement)
                self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
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
            # Move the boss every 0.02 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.02:
                # Boss reaches the right end of the screen
                if 600 * self.scale_factor_x < self.boss.xcor() < 650 * self.scale_factor_x:
                    # Move left
                    self.movement = -1
                # Boss reaches the left end of the screen
                if -600 * self.scale_factor_x > self.boss.xcor() > -650 * self.scale_factor_x:
                    # Move right
                    self.movement = 1
                if self.movement == 1:
                    # Speeds up based on the death_count variable
                    if 4 <= self.death_count < 7:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = 2 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() + 2 * self.scale_factor_x + delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() + 4 * self.scale_factor_x + delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = 6 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() + 6 * self.scale_factor_x + delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = 8 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() + 8 * self.scale_factor_x + delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = 10 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() + 10 * self.scale_factor_x + delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        delta_movement = 2 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() - 2 * self.scale_factor_x - delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() - 4 * self.scale_factor_x - delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = 6 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() - 6 * self.scale_factor_x - delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = 8 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() - 8 * self.scale_factor_x - delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = 10 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.boss.setx(self.boss.xcor() - 10 * self.scale_factor_x - delta_movement)
                        self.boss_health_bar.goto(self.boss.xcor(), self.boss.ycor() + 82 * self.scale_factor_y)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
