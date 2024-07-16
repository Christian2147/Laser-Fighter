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
    File: ItemPowerUp.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to power ups in both Machine Mode and Alien Mode.
    Power Ups have a random chance of spawning while the user is playing either of these modes.
    The red power up is exclusive to Alien Mode and the green power up is exclusive the Machine Mode.
    When picked up, the power ups activate a special ability depending on the type picked up.
"""

import turtle
import random
import time
import pygame


class PowerUp:
    """
        Represents a power up in Laser Fighter. Power ups have a random chance of spawning in both Machine Mode
            and Alien Mode.

        Attributes:
            power_up (turtle.Turtle()): The power up sprite
            type (int): Determines the type of power up that this object is
            mode (int): Determines the current mode of the game (Machine mode or Alien mode)
    """

    def __init__(self, type, mode, spawn_sound, scale_factor_x, scale_factor_y, fullscreen):
        """
            Creates a power up object of the given type and spawn it at a random place on the screen.

            :param type: Determines the type of power up to create
            :type type: int

            :param mode: Determines the current mode of the game
            :type mode: int

            :param spawn_sound: Determines if the power up spawn sound is toggled on or off.
            :type spawn_sound: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.power_up = turtle.Turtle()
        # Type 1 = yellow power up
        if type == 1:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
        # Type 2 = blue power up
        elif type == 2:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Blue_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Blue_Lightning_Power_Up.gif")
        # Type 3 = green power up
        elif type == 3:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Green_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Green_Lightning_Power_Up.gif")
        # Type 4 = red power up
        elif type == 4:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Red_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Red_Lightning_Power_Up.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.power_up.penup()
        self.power_up.shapesize(2 * scale_factor_y, 2 * scale_factor_x)
        # Spawn in a random location on the x-axis (y axis depends on the mode of the game)
        if mode == 1:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -300 * scale_factor_y)
        elif mode == 2:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -150 * scale_factor_y)
        if spawn_sound == 1:
            sound = pygame.mixer.Sound("Sound/Power_Up_Spawn_Sound.wav")
            sound.play()

        self.type = type
        self.mode = mode

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.power_up.clear()
        del self.power_up

    def reinstate(self, type, mode, spawn_sound, scale_factor_x, scale_factor_y, fullscreen):
        """
            Reuses the existing sprite to spawn a power up on the screen with the correct type

            :param type: Determines the type of power up to create
            :type type: int

            :param mode: Determines the current mode of the game
            :type mode: int

            :param spawn_sound: Determines if the power up spawn sound is toggled on or off.
            :type spawn_sound: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        # Type 1 = yellow power up
        if type == 1:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Yellow_Lightning_Power_Up.gif")
        # Type 2 = blue power up
        elif type == 2:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Blue_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Blue_Lightning_Power_Up.gif")
        # Type 3 = green power up
        elif type == 3:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Green_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Green_Lightning_Power_Up.gif")
        # Type 4 = red power up
        elif type == 4:
            if fullscreen == 1:
                self.power_up.shape("Textures/Power_Ups/Red_Lightning_Power_Up_Scaled.gif")
            else:
                self.power_up.shape("Textures/Power_Ups/Red_Lightning_Power_Up.gif")
        # Spawn in a random location on the x-axis (y axis depends on the mode of the game)
        if mode == 1:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -300 * scale_factor_y)
        elif mode == 2:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -150 * scale_factor_y)
        if spawn_sound == 1:
            sound = pygame.mixer.Sound("Sound/Power_Up_Spawn_Sound.wav")
            sound.play()
        self.power_up.showturtle()

        self.type = type
        self.mode = mode

    def get_power_up(self):
        """
            Returns the power up sprite so its class attributes can be accessed

            :return: power_up: the power up sprite
            :type: turtle.Turtle()
        """

        return self.power_up

    def get_type(self):
        """
            Returns the type of power up that the current sprite is as an integer.

            :return: type: Determines the type of power up
            :type: int
        """

        return self.type

    def remove(self):
        """
            Removes the power up sprite form the screen and resets its attributes.

            :return: None
        """

        self.power_up.hideturtle()

    def spawn(self, spawn_sound):
        """
            Reuses the existing power up sprite and spawns it back on the screen. (This is when it is already actively
                in use)

            :param spawn_sound: Determines if the power up spawn sound is toggled on or off.
            :type spawn_sound: int

            :return: None
        """

        # If the power up is not visible
        if self.power_up.isvisible() == False:
            # Spawn it back
            self.power_up.showturtle()
            if spawn_sound == 1:
                sound = pygame.mixer.Sound("Sound/Power_Up_Spawn_Sound.wav")
                sound.play()

    def pick_up(self, pickup_sound, scale_factor_x, scale_factor_y):
        """
            Causes the current power up to be picked up when the player gets close enough to it.

            :param pickup_sound: Determines if the power up pickup sound is toggeled on or off
            :type pickup_sound: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :return: None
        """

        # Make the power up disappear and move it to a new random location on the screen
        self.power_up.hideturtle()
        if self.mode == 1:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -300 * scale_factor_y)
        elif self.mode == 2:
            self.power_up.goto(random.randint(int(-620 * scale_factor_x), int(620 * scale_factor_x)), -150 * scale_factor_y)
        if pickup_sound == 1:
            sound = pygame.mixer.Sound("Sound/Power_Up_Pickup_Sound.wav")
            sound.play()


class YellowIndicator:
    """
        Represents the yellow power up indicator at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the yellow power up is active or not.

        Attributes:
            power_up_indicator (turtle.Turtle()): The yellow power up indicator sprite
            yellow_power_up_active (int): Determines if the yellow power up is currently active or not
            activate_time (float): Used to calculate the duration of exactly how long the yellow power up can be active
                for.
            current_time (float): Also used in the calculation of how long the yellow power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)
    """

    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Create a yellow power up indicator object and spawns it at the top of the screen.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.power_up_indicator = turtle.Turtle()
        self.power_up_indicator.color("#737000")
        if fullscreen == 1:
            self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off_Scaled.gif")
        else:
            self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.power_up_indicator.penup()
        self.power_up_indicator.goto(-95 * scale_factor_x, 300 * scale_factor_y)

        self.yellow_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.power_up_indicator.clear()
        del self.power_up_indicator

    def reinstate(self, fullscreen):
        """
            Reuses the existing indicator sprite to spawn a yellow power up indicator at the top of the screen.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        self.power_up_indicator.color("#737000")
        if fullscreen == 1:
            self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off_Scaled.gif")
        else:
            self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")
        self.power_up_indicator.showturtle()

    def get_yellow_power_up_indicator(self):
        """
            Returns the yellow power up indicator sprite so its class attributes can be accessed

            :return: yellow_power_up_indicator: the yellow power up indicator sprite
            :type: turtle.Turtle()
        """

        return self.power_up_indicator

    def get_power_up_active(self):
        """
            Returns whether the yellow power up is currently active or not.

            :return: yellow_power_up_active: Whether the yellow power up is currently active or not
            :type: int
        """

        return self.yellow_power_up_active

    def get_power_up_timer(self):
        """
            Returns the amount of seconds left before the yellow power up deactivates (0 if it is currently not active)

            :return: time_value: The amount of seconds left before the yellow power up deactivates
        """

        return self.time_value

    def set_power_up_active(self, new_value):
        """
            Activates the yellow power up and starts its 20 second timer.

            :param new_value: The new value for the yellow_power_up_active variable
            :type new_value: int

            :return: None
        """

        self.yellow_power_up_active = new_value
        self.activate_time = time.time()
        self.time_value = 20

    def remove(self):
        """
            Removes the yellow power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.power_up_indicator.hideturtle()
        self.yellow_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self, fullscreen):
        """
            Makes the yellow power up indicator lit or unlit depending on if the yellow power up is active or not.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if self.yellow_power_up_active == 1:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_On_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif")
        else:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif")

    def set_timer(self):
        """
            Updates the timer for the the yellow power up indicator when the yellow power up is active.

            :return: None
        """

        if self.yellow_power_up_active == 1:
            current_time = time.time()
            elapsed_time = current_time - self.activate_time
            # Every second, the value of "time_value" drops by 1 since "time_value" represents a 20 second timer
            if elapsed_time >= 1.0:
                # See if more than 1 whole second has passed (Just in case there is EXTREME lag)
                # If it has, decrease the timer by the amount of whole seconds that have passed
                delta_movement = (elapsed_time - 1.0) / 1.0
                delta_movement = int(delta_movement)
                iterations = 1 + delta_movement
                for i in range(iterations):
                    if self.time_value != 0:
                        self.time_value = self.time_value - 1
                        self.activate_time = time.time()
                    else:
                        self.yellow_power_up_active = 0
                        self.activate_time = 0
                        break


class BlueIndicator:
    """
        Represents the blue power up indicator at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the blue power up is active or not.

        Attributes:
            power_up_indicator (turtle.Turtle()): The blue power up indicator sprite
            blue_power_up_active (int): Determines if the blue power up is currently active or not
            activate_time (float): Used to calculate the duration of exactly how long the blue power up can be active
                for.
            current_time (float): Also used in the calculation of how long the blue power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)
    """

    def __init__(self, scale_factor_x, scale_factor_y, fullscreen):
        """
            Create a blue power up indicator object and spawns it at the top of the screen.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.power_up_indicator = turtle.Turtle()
        self.power_up_indicator.color("#00004A")
        if fullscreen == 1:
            self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off_Scaled.gif")
        else:
            self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.power_up_indicator.penup()
        self.power_up_indicator.goto(-20 * scale_factor_x, 300 * scale_factor_y)

        self.blue_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.power_up_indicator.clear()
        del self.power_up_indicator

    def reinstate(self, fullscreen):
        """
            Reuses the existing indicator sprite to spawn a blue power up indicator at the top of the screen.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        self.power_up_indicator.color("#00004A")
        if fullscreen == 1:
            self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off_Scaled.gif")
        else:
            self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")
        self.power_up_indicator.showturtle()

    def get_blue_power_up_indicator(self):
        """
            Returns the blue power up indicator sprite so its class attributes can be accessed

            :return: blue_power_up_indicator: the blue power up indicator sprite
            :type: turtle.Turtle()
        """

        return self.power_up_indicator

    def get_power_up_active(self):
        """
            Returns whether the blue power up is currently active or not.

            :return: blue_power_up_active: Whether the blue power up is currently active or not
            :type: int
        """

        return self.blue_power_up_active

    def get_power_up_timer(self):
        """
            Returns the amount of seconds left before the blue power up deactivates (0 if it is currently not active)

            :return: time_value: The amount of seconds left before the blue power up deactivates
        """

        return self.time_value

    def set_power_up_active(self, new_value):
        """
            Activates the blue power up and starts its 45 second timer.

            :param new_value: The new value for the blue_power_up_active variable
            :type new_value: int

            :return: None
        """

        self.blue_power_up_active = new_value
        self.activate_time = time.time()
        self.time_value = 45

    def remove(self):
        """
            Removes the blue power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.power_up_indicator.hideturtle()
        self.blue_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self, fullscreen):
        """
            Makes the blue power up indicator lit or unlit depending on if the blue power up is active or not.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        if self.blue_power_up_active == 1:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_On_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif")
        else:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif")

    def set_timer(self):
        """
            Updates the timer for the the blue power up indicator when the blue power up is active.

            :return: None
        """

        if self.blue_power_up_active == 1:
            current_time = time.time()
            elapsed_time = current_time - self.activate_time
            # Every second, the value of "time_value" drops by 1 since "time_value" represents a 45 second timer
            if elapsed_time >= 1.0:
                # See if more than 1 whole second has passed (Just in case there is EXTREME lag)
                # If it has, decrease the timer by the amount of whole seconds that have passed
                delta_movement = (elapsed_time - 1.0) / 1.0
                delta_movement = int(delta_movement)
                iterations = 1 + delta_movement
                for i in range(iterations):
                    if self.time_value != 0:
                        self.time_value = self.time_value - 1
                        self.activate_time = time.time()
                    else:
                        self.blue_power_up_active = 0
                        self.activate_time = 0
                        break


class ExtraIndicator:
    """
        Represents the third power up indicator at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the yellow power up is active or not. It can also be green or red depending on the
            current mode of the game.

        Attributes:
            power_up_indicator (turtle.Turtle()): The third power up indicator sprite
            extra_power_up_active (int): Determines if the third power up is currently active or not (red or green)
            activate_time (float): Used to calculate the duration of exactly how long the third power up can be active
                for.
            current_time (float): Also used in the calculation of how long the third power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)
    """

    def __init__(self, mode, scale_factor_x, scale_factor_y, fullscreen):
        """
            Create a third power up indicator object and spawns it at the top of the screen.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int
        """

        self.power_up_indicator = turtle.Turtle()
        self.power_up_indicator.color("#001C00")
        # The color depends on the mode (Machine Mode = green and Alien Mode = red)
        if mode == 1:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
        else:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif")
        # Ensure that the turtle does not draw lines on the screen while moving
        self.power_up_indicator.penup()
        self.power_up_indicator.goto(50 * scale_factor_x, 300 * scale_factor_y)

        self.extra_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0
        self.mode = mode

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.power_up_indicator.clear()
        del self.power_up_indicator

    def reinstate(self, mode, fullscreen):
        """
            Reuses the existing indicator sprite to spawn a third power up indicator at the top of the screen.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        self.power_up_indicator.color("#001C00")
        # The color depends on the mode (Machine Mode = green and Alien Mode = red)
        if mode == 1:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
        else:
            if fullscreen == 1:
                self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off_Scaled.gif")
            else:
                self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif")
        self.power_up_indicator.showturtle()

        self.mode = mode

    def get_extra_power_up_indicator(self):
        """
            Returns the third power up indicator sprite so its class attributes can be accessed

            :return: extra_power_up_indicator: the third power up indicator sprite
            :type: turtle.Turtle()
        """

        return self.power_up_indicator

    def get_power_up_active(self):
        """
            Returns whether the extra power up is currently active or not.

            :return: extra_power_up_active: Whether the extra power up is currently active or not
            :type: int
        """

        return self.extra_power_up_active

    def get_power_up_timer(self):
        """
            Returns the amount of seconds left before the extra power up deactivates (0 if it is currently not active)

            :return: time_value: The amount of seconds left before the extra power up deactivates
        """

        return self.time_value

    def set_power_up_active(self, new_value):
        """
            Activates the third power up and starts its 15 second timer.

            :param new_value: The new value for the extra_power_up_active variable
            :type new_value: int

            :return: None
        """

        self.extra_power_up_active = new_value
        self.activate_time = time.time()
        self.time_value = 15

    def remove(self):
        """
            Removes the extra power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.power_up_indicator.hideturtle()
        self.extra_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self, fullscreen):
        """
            Makes the extra power up indicator lit or unlit depending on if the extra power up is active or not.

            :param fullscreen: The variable that determines if fullscreen is on or off
            :type fullscreen: int

            :return: None
        """

        # If the mode is Machine Mode
        if self.mode == 1:
            # Make the extra power up indicator green
            if self.extra_power_up_active == 1:
                if fullscreen == 1:
                    self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_On_Scaled.gif")
                else:
                    self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_On.gif")
            else:
                if fullscreen == 1:
                    self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off_Scaled.gif")
                else:
                    self.power_up_indicator.shape("Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif")
        # If the mode is Alien mode
        else:
            # Make the extra power up indicator red
            if self.extra_power_up_active == 1:
                if fullscreen == 1:
                    self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_On_Scaled.gif")
                else:
                    self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_On.gif")
            else:
                if fullscreen == 1:
                    self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off_Scaled.gif")
                else:
                    self.power_up_indicator.shape("Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif")

    def set_timer(self):
        """
            Updates the timer for the the extra power up indicator when the extra power up is active.

            :return: None
        """

        if self.extra_power_up_active == 1:
            current_time = time.time()
            elapsed_time = current_time - self.activate_time
            # Every second, the value of "time_value" drops by 1 since "time_value" represents a 15 second timer
            if elapsed_time >= 1.0:
                # See if more than 1 whole second has passed (Just in case there is EXTREME lag)
                # If it has, decrease the timer by the amount of whole seconds that have passed
                delta_movement = (elapsed_time - 1.0) / 1.0
                delta_movement = int(delta_movement)
                iterations = 1 + delta_movement
                for i in range(iterations):
                    if self.time_value != 0:
                        self.time_value = self.time_value - 1
                        self.activate_time = time.time()
                    else:
                        self.extra_power_up_active = 0
                        self.activate_time = 0
                        break
