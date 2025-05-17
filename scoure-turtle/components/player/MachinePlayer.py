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
from components.player.MachinePlayerLaser import MachineLaser
from setup.ModeSetupMaster import machine_mode_setup
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
from setup.TextureSetup import ARMOR_BAR_10_10_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_9_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_8_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_7_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_6_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_5_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_4_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_3_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_2_TEXTURE
from setup.TextureSetup import ARMOR_BAR_10_1_TEXTURE


class Player:
    """
        Represents a player in Machine Mode. The player is controlled based on controls and fires a green laser.

        Attributes:
            player (turtle.Turtle()): The player sprite
            health_bar (turtle.Turtle()): The players health bar sprite
            armor_bar (turtle.Turtle()): The players armor bar sprite
            armor_created (int): Determines if the armor bar has already been created or not for the player

            laser_list (list): The list of the current lasers on the screen
            all_laser_list (list): The list of all laser sprites created since the program began running (So that they
                can be reused)
            laser_start_y_list (list): The list of the lasers starting y-coordinates when they are fired
            laser_has_attacked_list (list): The the list of whether each laser has hit a machine or not
            lasers_fired_list (list): The list of whether or not each laser has been fired or not

            do_collision (int): Determines whether or not hitboxes need to be calculated and for what laser based on
                its value

            death_animation (int): determines whether the player is currently in the process of dying or not
            health_bar_indicator (int): Stores the current health of the player
            hit_delay (int): Delays how often the player can be hit
            update (float): Value that is incremented during the death animation of the player.

            direction (int): Stores the direction of the player (1 = right and 2 = left)

            kill_start_time (float): Used as a timestamp for the death animation of the player (To make the animation
                run in a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the player (To make the movement
                happen in a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit duration of the player (To make sure that the hit
                delay is constant)

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, god_mode, scale_factor_x, scale_factor_y):
        """
            Creates a player object and spawns it on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.player = turtle.Turtle()
        self.player.shape(machine_mode_setup.player_texture)
        self.player.shapesize(5, 2)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.player.penup()
        self.player.goto(0, -300 * scale_factor_y)

        self.laser_count = machine_mode_setup.laser_count

        self.laser_list = []
        self.all_laser_list = []
        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count

        for i in range(machine_mode_setup.laser_count):
            laser = MachineLaser(0, machine_mode_setup.laser_max_distance)
            self.laser_list.append(laser)
            self.all_laser_list.append(laser)

        self.do_collision = 0

        self.health_bar = turtle.Turtle()
        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.health_bar.penup()
        self.health_bar.shapesize(1, 1)
        self.health_bar.goto(531 * scale_factor_x, 339 * scale_factor_y)
        # If god mode is on, the health bar is not visible
        if god_mode == 1:
            self.health_bar.hideturtle()

        # If the shield is enabled, an armor bar is created in the top right corner of the screen
        if machine_mode_setup.health == 20:
            self.armor_bar = turtle.Turtle()
            self.armor_bar.shape(ARMOR_BAR_10_10_TEXTURE)
            self.armor_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
            # Ensure that the turtle does not draw lines on the screen while moving
            self.armor_bar.penup()
            self.armor_bar.goto(531 * scale_factor_x, 299 * scale_factor_y)
            # If god mode is on, the armor bar is not visible
            if god_mode == 1:
                self.armor_bar.hideturtle()
            self.armor_created = 1
        else:
            self.armor_created = 0

        self.death_animation = 0
        self.health_bar_indicator = machine_mode_setup.health
        self.hit_delay = 0
        self.update = 0
        self.direction = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.player.clear()
        # Remove the lasers from the list first before clearing the list
        for l in self.laser_list:
            l.remove()
            del l
        self.laser_list.clear()
        self.all_laser_list.clear()
        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.health_bar.clear()
        # Check if the armor bar exists or not
        # If it does, delete it here
        if hasattr(self, 'armor'):
            self.armor.clear()
            del self.armor
        del self.player
        del self.health_bar
        del self.laser_list
        del self.all_laser_list
        del self.laser_start_y_list
        del self.laser_has_attacked_list
        del self.lasers_fired_list

    def reinstate(self, god_mode):
        """
            Reuses the existing sprite to spawn a player on the screen

            :param god_mode: The variable that determines if god mode is toggled on or off
            :type god_mode: int

            :return: None
        """

        self.player.shape(machine_mode_setup.player_texture)
        self.player.goto(0, -300 * self.scale_factor_y)
        self.player.direction = "stop"
        self.player.showturtle()

        self.laser_count = machine_mode_setup.laser_count

        # If the laser count is greater than or equal to all available laser sprites
        if self.laser_count >= len(self.all_laser_list):
            # Reuse the existing ones
            for l in self.all_laser_list:
                l.reinstate(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(l)

            # Create the rest from scratch and add them to both lists
            remaining_lasers = self.laser_count - len(self.all_laser_list)
            for i in range(remaining_lasers):
                laser = MachineLaser(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(laser)
                self.all_laser_list.append(laser)
        # If the laser count is less than all available laser sprites
        else:
            # Reuse only the ones necessary
            for i in range(self.laser_count):
                self.all_laser_list[i].reinstate(0, machine_mode_setup.laser_max_distance)
                self.laser_list.append(self.all_laser_list[i])

        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count

        self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
        if god_mode == 0:
            self.health_bar.showturtle()

        self.health_bar_indicator = machine_mode_setup.health

        # If the shield is enabled, create the armor bar if it does not exist already
        if self.health_bar_indicator == 20:
            if self.armor_created == 0:
                self.armor_bar = turtle.Turtle()
                self.armor_bar.shapesize(1 * self.scale_factor_y, 1 * self.scale_factor_x)
                # Ensure that the turtle does not draw lines on the screen while moving
                self.armor_bar.penup()
                self.armor_bar.goto(531 * self.scale_factor_x, 299 * self.scale_factor_y)
                self.armor_created = 1

            # Set the armor bar to full
            self.armor_bar.shape(ARMOR_BAR_10_10_TEXTURE)
            # If god mode is off, show the armor bar
            if god_mode == 0:
                self.armor_bar.showturtle()

    def get_player(self):
        """
            Returns the player sprite so that its class attributes can be accessed.

            :return: player: The player sprite
            :type: Turtle.turtle()
        """

        return self.player

    def get_laser(self):
        """
            Returns the list of the players laser sprites so that their class attributes can be accessed

            :return: laser_list: The list of the players laser sprites
            :type: list
        """

        return self.laser_list

    def get_health_bar(self):
        """
            Returns the players health bar sprite so that its class attributes can be accessed

            :return: health_bar: The players health bar sprite
            :type: turtle.Turtle()
        """

        return self.health_bar

    def get_armor_bar(self):
        """
            Returns the players armor bar sprite so that its class attributes can be accessed

            :return: armor_bar: The players armor bar sprite
            :type: turtle.Turtle()
        """

        return self.armor_bar

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
            Returns the list of whether each laser has hit an enemy since it was last fired

            :return: laser_last_attacked_list: Determines whether each laser has hit an enemy since it was last fired
            :type: int
        """

        return self.laser_has_attacked_list

    def set_laser_has_attacked(self, new_value, index):
        """
            For a specific laser specified by the index, this modifies its laser_has_attacked variable

            :param new_value: The new laser_has_attacked of the yellow machine.
            :type new_value: int

            :param index: The index of the laser data to modify
            :type index: int

            :return: None
        """

        self.laser_has_attacked_list[index] = new_value

    def remove(self):
        """
            Removes the player sprite form the screen and resets its attributes.

            :return: None
        """

        self.player.hideturtle()
        # Clear laser data
        for l in self.laser_list:
            l.remove()
        self.laser_list.clear()
        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.laser_count = 0
        self.do_collision = 0
        self.health_bar.hideturtle()
        # If the armor bar was created, remove it from the screen
        if self.armor_created == 1:
            self.armor_bar.hideturtle()
        self.death_animation = 0
        self.hit_delay = 0
        self.health_bar_indicator = machine_mode_setup.health
        self.update = 0
        # self.laser_has_attacked = 0
        self.laser_start_time = 0
        self.kill_start_time = 0
        self.hit_start_time = 0

    def remove_laser_start_y(self):
        """
            Resets the data of all the lasers so that their firing can be initiated again.

            :return: None
        """

        self.laser_start_y_list.clear()
        self.laser_has_attacked_list.clear()
        self.lasers_fired_list.clear()
        self.laser_start_y_list = [0] * self.laser_count
        self.laser_has_attacked_list = [0] * self.laser_count
        self.lasers_fired_list = [0] * self.laser_count
        self.laser_start_time = time.time()

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

    def move_player(self, yellow_power_up):
        """
            Moves the player in the direction specified by the "direction" variable

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :return: None
        """

        if self.direction == 1 and self.player.xcor() > -620 * self.scale_factor_x and self.death_animation == 0:
            # How fast the player moves is determined by whether or not the yellow power up is active
            if yellow_power_up == 1:
                self.player.setx(self.player.xcor() - machine_mode_setup.yellow_player_movement)
            else:
                self.player.setx(self.player.xcor() - machine_mode_setup.player_movement)

        if self.direction == 2 and self.player.xcor() < 620 * self.scale_factor_x and self.death_animation == 0:
            if yellow_power_up == 1:
                self.player.setx(self.player.xcor() + machine_mode_setup.yellow_player_movement)
            else:
                self.player.setx(self.player.xcor() + machine_mode_setup.player_movement)

    def fire(self, shooting_sound, index=0):
        """
            Fires the players laser by resetting it to its original position

            :param shooting_sound: Determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :param index: The index of the laser to fire. (0 by default)
            :type index: int

            :return: None
        """

        self.laser_list[index].laser.showturtle()
        if shooting_sound == 1:
            sound = pygame.mixer.Sound("sound/Laser_Gun_Player.wav")
            sound.play()
        # Moves the specified laser back to the player to be fired
        self.laser_list[index].laser.setx(self.player.xcor())
        self.laser_list[index].laser.sety(self.player.ycor() + machine_mode_setup.laser_offset)
        # Set the lasers attributes correctly
        self.laser_start_y_list[index] = self.laser_list[index].laser.ycor()
        self.laser_has_attacked_list[index] = 0
        self.lasers_fired_list[index] = 1

        # Initiate the calculation of the hitboxes for the specified laser
        self.do_collision = index + 1

    def shoot(self, shooting_sound, yellow_power_up):
        """
            Moves the player's lasers across the screen after they are fired.

            :param shooting_sound: Determines if the player shooting sound is toggled on or off
            :type shooting_sound: int

            :param yellow_power_up: Determines if the yellow power up is currently active or not
            :type yellow_power_up: int

            :return: None
        """

        # If a specific laser has hit an enemy, remove it from the screen
        for i in range(len(self.laser_has_attacked_list)):
            if self.laser_has_attacked_list[i] == 1:
                self.laser_list[i].laser.hideturtle()

        # Fire the third laser when the second laser has travelled at least 100 units
        if len(self.laser_list) > 2 and self.lasers_fired_list[1] != 0 and self.lasers_fired_list[2] == 0 and self.laser_list[1].laser.ycor() >= self.laser_start_y_list[1] + 100 * self.scale_factor_y:
            self.fire(shooting_sound, 2)

        # Fire the second laser when the first laser has travelled at least 100 units
        if len(self.laser_list) > 1 and self.lasers_fired_list[1] == 0 and self.laser_list[0].laser.ycor() >= self.laser_start_y_list[0] + 100 * self.scale_factor_y:
            self.fire(shooting_sound, 1)

        # While the last laser is still in the frame of the screen
        if self.laser_list[0].laser.ycor() < machine_mode_setup.laser_max_distance:
            # Keep moving it a number of units every 0.015 seconds
            # The number of units depends on the laser speed and the yellow power up
            current_time = time.time()
            elapsed_time = current_time - self.laser_start_time
            if elapsed_time >= 0.015:
                # If the yellow power up is not activated/is activated
                if yellow_power_up == 0:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = machine_mode_setup.laser_speed * ((elapsed_time - 0.015) / 0.015)
                    # If the third laser has been fired
                    if len(self.lasers_fired_list) == 3 and self.lasers_fired_list[2] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[2].laser.sety(self.laser_list[2].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                    # If the second laser has been fired and not the third
                    elif len(self.lasers_fired_list) >= 2 and self.lasers_fired_list[1] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                    # If only the first laser has been fired
                    elif len(self.lasers_fired_list) >= 1 or self.lasers_fired_list[1] == 0:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.laser_speed + delta_movement)
                elif yellow_power_up == 1:
                    delta_movement = machine_mode_setup.yellow_power_up_speed * ((elapsed_time - 0.015) / 0.015)
                    if len(self.lasers_fired_list) == 3 and self.lasers_fired_list[2] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[2].laser.sety(self.laser_list[2].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 2 and self.lasers_fired_list[1] == 1:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                        self.laser_list[1].laser.sety(self.laser_list[1].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                    elif len(self.lasers_fired_list) >= 1 or self.lasers_fired_list[1] == 0:
                        self.laser_list[0].laser.sety(self.laser_list[0].laser.ycor() + machine_mode_setup.yellow_power_up_speed + delta_movement)
                self.laser_start_time = time.time()
        else:
            # Remove all lasers from the screen when they are done being fired
            for l in self.laser_list:
                l.laser.hideturtle()
            self.laser_start_time = 0

    def grant_player_health(self):
        """
            This function is used to grant the player 3 health when the Heart power up is picked up.

            :return: None
        """

        if self.health_bar_indicator + 3 > machine_mode_setup.health:
            new_increase = machine_mode_setup.health - self.health_bar_indicator
            self.health_bar_indicator = self.health_bar_indicator + new_increase
        else:
            self.health_bar_indicator = self.health_bar_indicator + 3

        if self.health_bar_indicator >= 10:
            self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
            if self.health_bar_indicator == 20:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_10_TEXTURE)
            elif self.health_bar_indicator == 19:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_9_TEXTURE)
            elif self.health_bar_indicator == 18:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_8_TEXTURE)
            elif self.health_bar_indicator == 17:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_7_TEXTURE)
            elif self.health_bar_indicator == 16:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_6_TEXTURE)
            elif self.health_bar_indicator == 15:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_5_TEXTURE)
            elif self.health_bar_indicator == 14:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_4_TEXTURE)
            elif self.health_bar_indicator == 13:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_3_TEXTURE)
            elif self.health_bar_indicator == 12:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_2_TEXTURE)
            elif self.health_bar_indicator == 11:
                self.armor_bar.showturtle()
                self.armor_bar.shape(ARMOR_BAR_10_1_TEXTURE)
        elif self.health_bar_indicator == 9:
            self.health_bar.shape(HEALTH_BAR_910_TEXTURE)
        elif self.health_bar_indicator == 8:
            self.health_bar.shape(HEALTH_BAR_810_TEXTURE)
        elif self.health_bar_indicator == 7:
            self.health_bar.shape(HEALTH_BAR_710_TEXTURE)
        elif self.health_bar_indicator == 6:
            self.health_bar.shape(HEALTH_BAR_610_TEXTURE)
        elif self.health_bar_indicator == 5:
            self.health_bar.shape(HEALTH_BAR_510_TEXTURE)
        elif self.health_bar_indicator == 4:
            self.health_bar.shape(HEALTH_BAR_410_TEXTURE)
        elif self.health_bar_indicator == 3:
            self.health_bar.shape(HEALTH_BAR_310_TEXTURE)
        elif self.health_bar_indicator == 2:
            self.health_bar.shape(HEALTH_BAR_210_TEXTURE)
        elif self.health_bar_indicator == 1:
            self.health_bar.shape(HEALTH_BAR_110_TEXTURE)

    def kill_player(self, death_sound):
        """
            Kills the player and plays the players death animation. After that, it spawns the player back at the
                center and resets the game.

            :param death_sound: Determines if the death sound for the player is toggled on or off
            :type death_sound: int

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

        # Resets the players health back to 10 or 20 is the shield is enabled
        if self.update == 3.5:
            self.health_bar.shape(HEALTH_BAR_1010_TEXTURE)
            self.health_bar_indicator = machine_mode_setup.health
            if self.health_bar_indicator == 20:
                self.armor_bar.shape(ARMOR_BAR_10_10_TEXTURE)
                self.armor_bar.showturtle()
            self.update = 4
            self.kill_start_time = time.time()
            return

        # Respawns the player at the origin
        if self.update == 3:
            self.player.hideturtle()
            self.player.shape(machine_mode_setup.player_texture)
            self.player.goto(0, -300 * self.scale_factor_y)
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
            self.player.shape(EXPLOSION_2_TEXTURE)
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
                sound = pygame.mixer.Sound("sound/Explosion3.wav")
                sound.play()
            # Sets the players texture to the first frame of the explosion
            self.player.shape(EXPLOSION_1_TEXTURE)
            self.update = 0.5
            self.kill_start_time = time.time()

    def hit_player(self, hit_sound):
        """
            Makes the player take "one hit" of damage and creates a hit delay before the player can be hit again

            :param hit_sound: Determines if the player hit sound is toggled on or off
            :type hit_sound: int

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
            # Update the players health bar
            # If the players health is above 10, an armor bar should be visible
            if self.health_bar_indicator == 20:
                self.armor_bar.shape(ARMOR_BAR_10_9_TEXTURE)
            elif self.health_bar_indicator == 19:
                self.armor_bar.shape(ARMOR_BAR_10_8_TEXTURE)
            elif self.health_bar_indicator == 18:
                self.armor_bar.shape(ARMOR_BAR_10_7_TEXTURE)
            elif self.health_bar_indicator == 17:
                self.armor_bar.shape(ARMOR_BAR_10_6_TEXTURE)
            elif self.health_bar_indicator == 16:
                self.armor_bar.shape(ARMOR_BAR_10_5_TEXTURE)
            elif self.health_bar_indicator == 15:
                self.armor_bar.shape(ARMOR_BAR_10_4_TEXTURE)
            elif self.health_bar_indicator == 14:
                self.armor_bar.shape(ARMOR_BAR_10_3_TEXTURE)
            elif self.health_bar_indicator == 13:
                self.armor_bar.shape(ARMOR_BAR_10_2_TEXTURE)
            elif self.health_bar_indicator == 12:
                self.armor_bar.shape(ARMOR_BAR_10_1_TEXTURE)
            # Armor bar disappears when the players health drops below 11
            elif self.health_bar_indicator == 11:
                self.armor_bar.hideturtle()
            elif self.health_bar_indicator == 10:
                self.health_bar.shape(HEALTH_BAR_910_TEXTURE)
            elif self.health_bar_indicator == 9:
                self.health_bar.shape(HEALTH_BAR_810_TEXTURE)
            elif self.health_bar_indicator == 8:
                self.health_bar.shape(HEALTH_BAR_710_TEXTURE)
            elif self.health_bar_indicator == 7:
                self.health_bar.shape(HEALTH_BAR_610_TEXTURE)
            elif self.health_bar_indicator == 6:
                self.health_bar.shape(HEALTH_BAR_510_TEXTURE)
            elif self.health_bar_indicator == 5:
                self.health_bar.shape(HEALTH_BAR_410_TEXTURE)
            elif self.health_bar_indicator == 4:
                self.health_bar.shape(HEALTH_BAR_310_TEXTURE)
            elif self.health_bar_indicator == 3:
                self.health_bar.shape(HEALTH_BAR_210_TEXTURE)
            elif self.health_bar_indicator == 2:
                self.health_bar.shape(HEALTH_BAR_110_TEXTURE)
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion4.wav")
                sound.play()
            self.hit_delay = 1
            # Decrease the players health by 1
            self.health_bar_indicator = self.health_bar_indicator - 1
            self.hit_start_time = time.time()
