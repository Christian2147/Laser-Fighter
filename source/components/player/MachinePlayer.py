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
    File: MachinePlayer.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to the player in Machine Mode.
    The player moves left and right based on the controls and fires a green laser at fast speed.
    The player has 10 health and has a 1.5 second long death animation.
    The player is supposed to a be a cylinder laser gun that is sticking out of a ship that we cannot see in the frame.
"""

import turtle
import pygame
import time


class Player:
    """
        Represents a player in Machine Mode. The player is controlled based on controls and fires a green laser.

        Attributes:
            player (turtle.Turtle()): The player sprite
            laser (turtle.Turtle()): The player laser sprite
            health_bar (turtle.Turtle()): The players health bar sprite
            death_animation (int): determines whether the player is currenly in the process of dying or not
            health_bar_indicator (int): Stores the current health of the player
            hit_delay (int): Delays how often the player can be hit
            update (float): Value that is incremented during the death animation of the player.
            direction (int): Stores the direction of the player (1 = right and 2 = left)
            laser_has_attacked (int): Determines whether the players laser has hit an enemy since it was fired.
            kill_start_time (float): Used as a timestamp for the death animation of the player (To make the animation
                run in a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the player (To make the movement
                happen in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit duration of the player (To make sure that the hit
                delay is constant)
    """

    def __init__(self, god_mode, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates a player object and spawns it on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.player = turtle.Turtle()
        if fullscreen == 1:
            self.player.shape("Textures/Player/Player_Scaled.gif")
        else:
            self.player.shape("Textures/Player/Player.gif")
        self.player.shapesize(5, 2)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.player.penup()
        self.player.goto(0, -300 * scale_factor_y)

        self.laser = turtle.Turtle()
        if fullscreen == 1:
            self.laser.shape("Textures/Lasers/Player_Laser_Scaled.gif")
        else:
            self.laser.shape("Textures/Lasers/Player_Laser.gif")
        self.laser.direction = "down"
        # Ensure that the turtle does not draw lines on the screen while moving
        self.laser.penup()
        self.laser.shapesize(1, 1)
        self.laser.goto(0, 360 * scale_factor_y)
        self.laser.hideturtle()

        self.health_bar = turtle.Turtle()
        if fullscreen == 1:
            self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.health_bar.penup()
        self.health_bar.shapesize(1, 1)
        self.health_bar.goto(531 * scale_factor_x, 339 * scale_factor_y)
        # If god mode is on, the health bar is not visible
        if god_mode == 1:
            self.health_bar.hideturtle()

        self.death_animation = 0
        self.health_bar_indicator = 10
        self.hit_delay = 0
        self.update = 0
        self.direction = 0
        self.laser_has_attacked = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.player.clear()
        self.laser.clear()
        self.health_bar.clear()
        del self.player
        del self.laser
        del self.health_bar

    def reinstate(self, god_mode, scale_factor_y, fullscreen):
        """
            Reuses the existing sprite to spawn a player on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        self.player.goto(0, -300 * scale_factor_y)
        self.player.direction = "stop"
        self.player.showturtle()
        self.laser.goto(0, 360 * scale_factor_y)
        self.laser.direction = "down"
        if fullscreen == 1:
            self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
        else:
            self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
        if god_mode == 0:
            self.health_bar.showturtle()

    def get_player(self):
        """
            Returns the player sprite so that its class attributes can be accessed.

            :return: player: The player sprite
            :type: Turtle.turtle()
        """

        return self.player

    def get_laser(self):
        """
            Returns the players laser sprite so that its class attributes can be accessed

            :return: laser: The player laser sprite
            :type: turtle.Turtle()
        """

        return self.laser

    def get_health_bar(self):
        """
            Returns the players health bar sprite so that its class attributes can be accessed

            :return: health_bar: The players health bar sprite
            :type: turtle.Turtle()
        """

        return self.health_bar

    def get_player_death_update(self):
        """
            Returns the death animation update value of the player

            :return: update: the death animation update value of the player
            :type: float
        """

        return self.update

    def get_death_animation(self):
        """
            Returns the death animation indicator variable of the player

            :return: death_animation: The death animation indicator variable
            :type: int
        """

        return self.death_animation

    def get_hit_delay(self):
        """
            Returns the hit delay value of the player

            :return: hit_delay: the hit delay value of the player
            :type: int
        """

        return self.hit_delay

    def get_health_bar_indicator(self):
        """
            Returns the health of the player

            :return: health_bar_indicator: The current health of the player
            :type: int
        """

        return self.health_bar_indicator

    def get_laser_has_attacked(self):
        """
            Returns whether the laser has hit an enemy since it was last fired

            :return: laser_last_attacked: Determines whether the player laser has hit an enemy since it was last fired
            :type: int
        """

        return self.laser_has_attacked

    def set_laser_has_attacked(self, new_value):
        """
            Sets the laser_has_attacked of the player (Used for when the player hits an enemy)

            :param new_value: The new laser_has_attacked of the yellow machine.
            :type new_value: int

            :return: None
        """

        self.laser_has_attacked = new_value

    def remove(self):
        """
            Removes the player sprite form the screen and resets its attributes.

            :return: None
        """

        self.player.hideturtle()
        self.laser.hideturtle()
        self.health_bar.hideturtle()
        self.death_animation = 0
        self.hit_delay = 0
        self.health_bar_indicator = 10
        self.update = 0
        self.laser_has_attacked = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

    def set_direction_left(self):
        """
            Sets the players direction of movement to be left

            :return: None
        """

        self.player.direction = "left"
        self.direction = 1

    def set_direction_right(self):
        """
            Sets the players direction of movement to be right

            :return: None
        """

        self.player.direction = "right"
        self.direction = 2

    def move_player(self, scale_factor_x):
        """
            Moves the player in the direction specified by the "direction" variable

            :return: None
        """

        if self.direction == 1 and self.player.xcor() > -620 * scale_factor_x and self.death_animation == 0:
            self.player.setx(self.player.xcor() - 30 * scale_factor_x)

        if self.direction == 2 and self.player.xcor() < 620 * scale_factor_x and self.death_animation == 0:
            self.player.setx(self.player.xcor() + 30 * scale_factor_x)

    def fire(self, shooting_sound, scale_factor_y):
        """
            Fires the players laser by resetting it to its original position

            :param shooting_sound: Determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        self.laser.showturtle()
        if shooting_sound == 1:
            sound = pygame.mixer.Sound("Sound/Laser_Gun_Player.wav")
            sound.play()
        # Moves the laser back to the player to be fired
        self.laser.setx(self.player.xcor())
        self.laser.sety(self.player.ycor() + 120 * scale_factor_y)
        self.laser_start_time = time.time()
        self.laser_has_attacked = 0

    def shoot(self, yellow_power_up, scale_factor_y):
        """
            Moves the player's laser across the screen after it is fired

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        # If the laser has hit an enemy, remove it from the screen
        if self.laser_has_attacked == 1:
            self.laser.hideturtle()

        # While the laser is still in the frame of the screen
        if self.laser.ycor() < 360 * scale_factor_y:
            # Keep moving it 14.5 or 43.5 units every 0.015 seconds
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            if elapsed_time >= 0.015:
                if yellow_power_up == 0:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 14.5 * scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                    self.laser.sety(self.laser.ycor() + 14.5 * scale_factor_y + delta_movement)
                elif yellow_power_up == 1:
                    delta_movement = 43.5 * scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                    self.laser.sety(self.laser.ycor() + 43.5 * scale_factor_y + delta_movement)
                self.laser_start_time = time.time()
        else:
            self.laser.hideturtle()
            self.laser_start_time = 0

    def kill_player(self, death_sound, scale_factor_y, fullscreen):
        """
            Kills the player and plays the players death animation. After that, it spawns the player back at the
                center and resets the game.

            :param death_sound: Determines if the death sound for the player is toggled on or off
            :type death_sound: int

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        no_kill = 0
        # Reveals the player sprite on the screen
        if self.update == 6:
            self.player.showturtle()
            self.update = 0
            self.death_animation = 0
            no_kill = 1

        # Wait 0.05 seconds
        if 4 <= self.update < 6:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.05:
                self.update = 6
                self.kill_start_time = 0

        # Resets the players health back to 10
        if self.update == 3.5:
            if fullscreen == 1:
                self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10_Scaled.gif")
            else:
                self.health_bar.shape("Textures/Health_Bars/HealthBar_10.10.gif")
            self.health_bar_indicator = 10
            self.update = 4
            self.kill_start_time = time.time()
            return

        # Respawns the player at the origin
        if self.update == 3:
            self.player.hideturtle()
            if fullscreen == 1:
                self.player.shape("Textures/Player/Player_Scaled.gif")
            else:
                self.player.shape("Textures/Player/Player.gif")
            self.player.goto(0, -300 * scale_factor_y)
            self.update = 3.5

        # Wait 0.15 seconds
        if 1.5 <= self.update < 3:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.15:
                self.update = 3
                self.kill_start_time = 0

        # Changes the players texture to the second frame of the explosion
        if 1.0 <= self.update <= 1.1:
            if fullscreen == 1:
                self.player.shape("Textures/Explosions/Explosion2_Scaled.gif")
            else:
                self.player.shape("Textures/Explosions/Explosion2.gif")
            self.update = 1.5
            self.kill_start_time = time.time()

        # Wait 0.1 seconds
        if 0.5 <= self.update < 1:
            if self.update == 0.5:
                self.update = 0.6
            elif self.update == 0.6:
                self.update = 0.7
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.1:
                self.update = 1
                self.kill_start_time = 0

        if self.update == 0 and no_kill == 0:
            # Death animation is happening
            self.death_animation = 1
            self.health_bar_indicator = 0
            # Death sound plays
            if death_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion3.wav")
                sound.play()
            # Sets the players texture to the first frame of the explosion
            if fullscreen == 1:
                self.player.shape("Textures/Explosions/Explosion1_Scaled.gif")
            else:
                self.player.shape("Textures/Explosions/Explosion1.gif")
            self.update = 0.5
            self.kill_start_time = time.time()

    def hit_player(self, hit_sound, fullscreen):
        """
            Makes the player take "one hit" of damage and creates a hit delay before the player can be hit again

            :param hit_sound: Determines if the player hit sound is toggled on or off
            :type hit_sound: int

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        # Reset the hit delay back to 0
        no_hit = 0
        if self.hit_delay == 39:
            self.hit_delay = 0
            no_hit = 1

        # Wait 0.5 seconds
        if 3 <= self.hit_delay < 39:
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.5:
                self.hit_delay = 39
                self.hit_start_time = 0

        if self.hit_delay == 2:
            self.hit_delay = 3

        if self.hit_delay == 1:
            self.hit_delay = 2

        if self.hit_delay == 0 and no_hit == 0 and self.update == 0:
            # Decrease the players health by 1
            if self.health_bar_indicator == 10:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.9_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.9.gif")
            elif self.health_bar_indicator == 9:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.8_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.8.gif")
            elif self.health_bar_indicator == 8:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.7_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.7.gif")
            elif self.health_bar_indicator == 7:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.6_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.6.gif")
            elif self.health_bar_indicator == 6:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.5_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.5.gif")
            elif self.health_bar_indicator == 5:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.4_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.4.gif")
            elif self.health_bar_indicator == 4:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.3_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.3.gif")
            elif self.health_bar_indicator == 3:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.2_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.2.gif")
            elif self.health_bar_indicator == 2:
                if fullscreen == 1:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.1_Scaled.gif")
                else:
                    self.health_bar.shape("Textures/Health_Bars/HealthBar_10.1.gif")
            if hit_sound == 1:
                sound = pygame.mixer.Sound("Sound/Explosion4.wav")
                sound.play()
            self.hit_delay = 1
            self.health_bar_indicator = self.health_bar_indicator - 1
            self.hit_start_time = time.time()
