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

import turtle
import random
import pygame
import time
from components.ItemCoin import Coin
from setup.TextureSetup import BLUE_MACHINE_TEXTURE
from setup.TextureSetup import BLUE_MACHINE_LASER_TEXTURE
from setup.TextureSetup import EXPLOSION_1_TEXTURE
from setup.TextureSetup import EXPLOSION_2_TEXTURE


class BlueMachine:
    """
        Represents a blue machine in Laser Fighter. The first enemy in Machine Mode that is blue and fires blue lasers.

        Attributes:
            blue_machine (turtle.Turtle()): The blue machine enemy sprite.
            blue_machine_laser (turtle.Turtle()): The laser sprite for each blue machine enemy.
            death_count (int): Stores the death count for the enemy since the player has last died.
            update (float): Value that is incremented during the death animation of the enemy.
            movement (int): Stores the direction that the enemy is supposed to move on
                the x-axis (1 = right and -1 = left)
            float (int): Stores the direction that the enemy is supposed to move on the y-axis (1 = up and -1 == down)
            start_y_float (float): Stores the y-coordinate of the enemy when the float effect is starting or when
                it is changing direction
            float_activated (int): Determines if the float effect is currently active or not (For timing purposes)
            start_time (float): Used as a timestamp for the death animation of the enemy (To make the animation run in
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
            id (int): The id of the current blue machine (Used for counting how many are on the screen)
    """

    def __init__(self, id, scale_factor_x, scale_factor_y):
        """
            Creates a blue machine object and spawns it on the screen

            :param id: Ths id of the blue machine (Determines where it spawns and it keeps track of how many are on
                the screen)
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.blue_machine = turtle.Turtle()
        self.blue_machine.shape(BLUE_MACHINE_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.blue_machine.penup()
        self.blue_machine.shapesize(2 * scale_factor_y, 2 * scale_factor_x)
        # Correct location based on id
        if id == 1:
            self.blue_machine.goto(-200 * scale_factor_x, 220 * scale_factor_y)
        elif id == 2:
            self.blue_machine.goto(200 * scale_factor_x, 220 * scale_factor_y)
        elif id == 3:
            self.blue_machine.goto(500 * scale_factor_x, 220 * scale_factor_y)
        elif id == 4:
            self.blue_machine.goto(-500 * scale_factor_x, 220 * scale_factor_y)
        elif id == 5:
            self.blue_machine.goto(-400 * scale_factor_x, 220 * scale_factor_y)
        self.blue_machine.direction = "down"

        self.blue_machine_laser = turtle.Turtle()
        self.blue_machine_laser.shape(BLUE_MACHINE_LASER_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.blue_machine_laser.penup()
        self.blue_machine_laser.shapesize(2.25 * scale_factor_y, 0.5 * scale_factor_x)
        self.blue_machine_laser.direction = "down"
        # Correct location based on id
        if id == 1:
            self.blue_machine_laser.goto(-200 * scale_factor_x, 170 * scale_factor_y)
        elif id == 2:
            self.blue_machine_laser.goto(200 * scale_factor_x, 170 * scale_factor_y)
        elif id == 3:
            self.blue_machine_laser.goto(500 * scale_factor_x, 170 * scale_factor_y)
        elif id == 4:
            self.blue_machine_laser.goto(-500 * scale_factor_x, 170 * scale_factor_y)
        elif id == 5:
            self.blue_machine_laser.goto(-400 * scale_factor_x, 170 * scale_factor_y)

        self.death_count = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.laser_start_time = 0
        self.move_start_time = time.time()
        self.float_start_time = time.time()
        self.laser_has_attacked = 0
        self.movement_activated = 0
        self.id = id

        self.enemy_center = self.blue_machine.ycor()
        self.float_time_offset = time.time()
        self.x_range = (0, 0)
        self.collision_y_coordinate = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.blue_machine.clear()
        self.blue_machine_laser.clear()
        del self.blue_machine
        del self.blue_machine_laser

    def reinstate(self, id):
        """
            Reuses the existing sprite to spawn a blue machine on the screen with the correct id

            :param id: Ths id of the new blue machine (Determines where it spawns and its keeps track of how many are
                on the screen)
            :type id: int

            :return: None
        """

        self.blue_machine.shape(BLUE_MACHINE_TEXTURE)
        # Correct location based on id
        if id == 1:
            self.blue_machine.goto(-200 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.blue_machine_laser.goto(-200 * self.scale_factor_x, 170 * self.scale_factor_y)
        elif id == 2:
            self.blue_machine.goto(200 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.blue_machine_laser.goto(200 * self.scale_factor_x, 170 * self.scale_factor_y)
        elif id == 3:
            self.blue_machine.goto(500 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.blue_machine_laser.goto(500 * self.scale_factor_x, 170 * self.scale_factor_y)
        elif id == 4:
            self.blue_machine.goto(-500 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.blue_machine_laser.goto(-500 * self.scale_factor_x, 170 * self.scale_factor_y)
        elif id == 5:
            self.blue_machine.goto(-400 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.blue_machine_laser.goto(-400 * self.scale_factor_x, 170 * self.scale_factor_y)

        self.enemy_center = self.blue_machine.ycor()
        self.float_time_offset = time.time()

        self.blue_machine.direction = "down"
        self.blue_machine_laser.direction = "down"

        # Set the id to the new id
        self.id = id
        self.blue_machine.showturtle()
        self.blue_machine_laser.showturtle()

        self.move_start_time = time.time()
        self.float_start_time = time.time()

    def get_blue_machine(self):
        """
            Returns the blue_machine sprite so its class attributes can be accessed

            :return: blue_machine: the blue machine sprite
            :type: turtle.Turtle()
        """

        return self.blue_machine

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
            Removes the blue machine sprite form the screen and resets its attributes.

            :return: None
        """

        self.blue_machine.hideturtle()
        self.blue_machine_laser.hideturtle()
        self.death_count = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0
        self.movement_activated = 0
        self.x_range = (0, 0)
        self.collision_y_coordinate = 0

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
                self.blue_machine_laser.hideturtle()
            else:
                self.blue_machine_laser.showturtle()
            # If the laser is still visible in the frame of the screen
            if self.blue_machine_laser.ycor() > -360 * self.scale_factor_y:
                # Keep moving the laser down the screen 4.8 units every 0.015 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.015:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 4.8 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                    self.blue_machine_laser.sety(self.blue_machine_laser.ycor() - 4.8 * self.scale_factor_y - delta_movement)
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.blue_machine_laser.setx(self.blue_machine.xcor())
                self.blue_machine_laser.sety(self.blue_machine.ycor() - 50 * self.scale_factor_y)
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("Sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.blue_machine_laser.hideturtle()
            self.blue_machine_laser.setx(self.blue_machine.xcor())
            self.blue_machine_laser.sety(self.blue_machine.ycor() - 50 * self.scale_factor_y)
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_enemy(self, death_sound, coins_on_screen, all_coins):
        """
            Kills the enemy and plays the enemies death animation. After that, it spawns the enemy in a new location.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :param all_coins: Array that lists all of the coin sprites generated since the
                programs execution (for reusing purposes)
            :type all_coins: list

            :return: None
        """

        # When the death animation and respawning is finished, the blue machine appears on the screen again
        if self.update == 6:
            self.blue_machine.showturtle()
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
            self.blue_machine.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                copper_coin = Coin(type="copper", pos_x=self.blue_machine.xcor(), pos_y=self.blue_machine.ycor())
                coins_on_screen.append(copper_coin)
                all_coins.append(copper_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_copper(pos_x=self.blue_machine.xcor(), pos_y=self.blue_machine.ycor())
                        coins_on_screen.append(coin)
                        break
            # Respawn the blue machine in a different random location
            self.blue_machine.shape(BLUE_MACHINE_TEXTURE)
            # Want to cast these ranges to integers to avoid a crash at certain resolutions
            self.blue_machine.goto(random.randint(int(-640 * self.scale_factor_x), int(640 * self.scale_factor_x)), random.randint(int(120 * self.scale_factor_y), int(220 * self.scale_factor_y)))
            self.float_activated = 0
            self.float_time_offset = time.time()
            self.enemy_center = self.blue_machine.ycor()
            self.x_range = (0, 0)
            self.collision_y_coordinate = 0
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
            self.blue_machine.shape(EXPLOSION_2_TEXTURE)
            self.update = 1.5
            self.start_time = time.time()
            self.kill_enemy(death_sound, coins_on_screen, all_coins)
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
                sound = pygame.mixer.Sound("Sound/Explosion.wav")
                sound.play()
            # Change the texture of the blue machine to the first frame of the death explosion
            self.blue_machine.shape(EXPLOSION_1_TEXTURE)
            self.update = 0.5
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
            self.start_y_float = self.blue_machine.ycor()

        if self.start_y_float + 50 < self.blue_machine.ycor():
            # Move down
            self.float = -1
        elif self.start_y_float - 50 > self.blue_machine.ycor():
            # Move up
            self.float = 1
        current_time = time.time()
        elapsed_time = current_time - self.float_start_time
        # Make a movement every 0.0075 seconds to reduce the effects of lag
        if elapsed_time >= 0.0075:
            if self.float == 1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = 0.15 * self.scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                self.blue_machine.goto(self.blue_machine.xcor(), self.blue_machine.ycor() + 0.15 * self.scale_factor_y + delta_movement)
            elif self.float == -1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = 0.15 * self.scale_factor_y * ((elapsed_time - 0.0075) / 0.0075)
                self.blue_machine.goto(self.blue_machine.xcor(), self.blue_machine.ycor() - 0.15 * self.scale_factor_y - delta_movement)
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
                if 640 * self.scale_factor_x < self.blue_machine.xcor():
                    # Move left
                    self.movement = -1
                # Blue machine reaches the left end of the screen
                if -640 * self.scale_factor_x > self.blue_machine.xcor():
                    # Move right
                    self.movement = 1
                if self.movement == 1:
                    # Speeds up based on the death_count variable
                    if 4 <= self.death_count < 7:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = 2 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() + 2 * self.scale_factor_x + delta_movement)
                    elif 7 <= self.death_count < 10:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() + 4 * self.scale_factor_x + delta_movement)
                    elif 10 <= self.death_count < 13:
                        delta_movement = 6 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() + 6 * self.scale_factor_x + delta_movement)
                    elif 13 <= self.death_count < 16:
                        delta_movement = 8 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() + 8 * self.scale_factor_x + delta_movement)
                    elif 16 <= self.death_count:
                        delta_movement = 10 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() + 10 * self.scale_factor_x + delta_movement)
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        delta_movement = 2 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() - 2 * self.scale_factor_x - delta_movement)
                    elif 7 <= self.death_count < 10:
                        delta_movement = 4 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() - 4 * self.scale_factor_x - delta_movement)
                    elif 10 <= self.death_count < 13:
                        delta_movement = 6 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() - 6 * self.scale_factor_x - delta_movement)
                    elif 13 <= self.death_count < 16:
                        delta_movement = 8 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() - 8 * self.scale_factor_x - delta_movement)
                    elif 16 <= self.death_count:
                        delta_movement = 10 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                        self.blue_machine.setx(self.blue_machine.xcor() - 10 * self.scale_factor_x - delta_movement)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
