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
    When the hearts gadget is enabled, it allows for the hearts power up to spawn.
"""

import random
import time
import pygame
import math
from setup.ModeSetupMasterPygame import power_up_setup
from setup.TextureSetup import YELLOW_LIGHTNING_POWER_UP_TEXTURE
from setup.TextureSetup import BLUE_LIGHTNING_POWER_UP_TEXTURE
from setup.TextureSetup import GREEN_LIGHTNING_POWER_UP_TEXTURE
from setup.TextureSetup import RED_LIGHTNING_POWER_UP_TEXTURE
from setup.TextureSetup import HEART_POWER_UP_TEXTURE
from setup.TextureSetup import YELLOW_POWER_UP_INDICATOR_ON_TEXTURE
from setup.TextureSetup import YELLOW_POWER_UP_INDICATOR_OFF_TEXTURE
from setup.TextureSetup import BLUE_POWER_UP_INDICATOR_ON_TEXTURE
from setup.TextureSetup import BLUE_POWER_UP_INDICATOR_OFF_TEXTURE
from setup.TextureSetup import GREEN_POWER_UP_INDICATOR_ON_TEXTURE
from setup.TextureSetup import GREEN_POWER_UP_INDICATOR_OFF_TEXTURE
from setup.TextureSetup import RED_POWER_UP_INDICATOR_ON_TEXTURE
from setup.TextureSetup import RED_POWER_UP_INDICATOR_OFF_TEXTURE


class PowerUp(pygame.sprite.Sprite):
    """
        Represents a power up in Laser Fighter. Power ups have a random chance of spawning in both Machine Mode
            and Alien Mode.

        Attributes:
            power_up (pygame.sprite.Sprite): The power up sprite

            type (int): Determines the type of power up that this object is
            mode (int): Determines the current mode of the game (Machine mode or Alien mode)

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, mode, spawn_sound, scale_factor_x, scale_factor_y):
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
        """

        super().__init__()
        if type == 1:
            self.image = pygame.image.load(YELLOW_LIGHTNING_POWER_UP_TEXTURE).convert_alpha()
        # Type 2 = blue power up
        elif type == 2:
            self.image = pygame.image.load(BLUE_LIGHTNING_POWER_UP_TEXTURE).convert_alpha()
        # Type 3 = green power up
        elif type == 3:
            self.image = pygame.image.load(GREEN_LIGHTNING_POWER_UP_TEXTURE).convert_alpha()
        # Type 4 = red power up
        elif type == 4:
            self.image = pygame.image.load(RED_LIGHTNING_POWER_UP_TEXTURE).convert_alpha()
        # Type 5 = heart power up
        elif type == 5:
            self.image = pygame.image.load(HEART_POWER_UP_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (545 * scale_factor_x, 60 * scale_factor_y)
        if mode == 1:
            self.rect.center = (random.randint(int(20 * scale_factor_x), int(1260 * scale_factor_x)), 660 * scale_factor_y)
        elif mode == 2:
            self.rect.center = (random.randint(int(20 * scale_factor_x), int(1260 * scale_factor_x)), 510 * scale_factor_y)
        if spawn_sound == 1:
            sound = pygame.mixer.Sound("sound/Power_Up_Spawn_Sound.wav")
            sound.play()
        self.power_up_visible = 1

        self.type = type
        self.mode = mode

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_power_up(self):
        """
            Returns the power up sprite so its class attributes can be accessed

            :return: power_up: the power up sprite
            :type: turtle.Turtle()
        """

        return self

    def get_type(self):
        """
            Returns the type of power up that the current sprite is as an integer.

            :return: type: Determines the type of power up
            :type: int
        """

        return self.type

    def isvisible(self):
        return self.power_up_visible

    def distance(self, other_sprite):
        """
            Return the Euclidean distance to another sprite based on center positions.
        """

        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)

    def remove(self):
        """
            Removes the power up sprite form the screen and resets its attributes.

            :return: None
        """

        self.power_up_visible = 0

    def spawn(self, spawn_sound):
        """
            Reuses the existing power up sprite and spawns it back on the screen. (This is when it is already actively
                in use)

            :param spawn_sound: Determines if the power up spawn sound is toggled on or off.
            :type spawn_sound: int

            :return: None
        """

        # If the power up is not visible
        if not self.isvisible():
            # Spawn it back
            self.power_up_visible = 1
            if spawn_sound == 1:
                sound = pygame.mixer.Sound("sound/Power_Up_Spawn_Sound.wav")
                sound.play()

    def pick_up(self, pickup_sound):
        """
            Causes the current power up to be picked up when the player gets close enough to it.

            :param pickup_sound: Determines if the power up pickup sound is toggeled on or off
            :type pickup_sound: int

            :return: None
        """

        # Make the power up disappear and move it to a new random location on the screen
        self.power_up_visible = 0
        if self.mode == 1:
            self.rect.center = (random.randint(int(20 * self.scale_factor_x), int(1260 * self.scale_factor_x)), 660 * self.scale_factor_y)
        elif self.mode == 2:
            self.rect.center = (random.randint(int(20 * self.scale_factor_x), int(1260 * self.scale_factor_x)), 510 * self.scale_factor_y)
        if pickup_sound == 1:
            sound = pygame.mixer.Sound("sound/Power_Up_Pickup_Sound.wav")
            sound.play()


class YellowIndicator(pygame.sprite.Sprite):
    """
        Represents the yellow power up indicator sprite at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the yellow power up is active or not.

        Attributes:
            yellow_power_up_active (int): Determines if the yellow power up is currently active or not
            activate_time (float): Used to calculate the duration of exactly how long the yellow power up can be active
                for.
            current_time (float): Also used in the calculation of how long the yellow power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Create a yellow power up indicator object and spawns it at the top of the screen.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = pygame.image.load(YELLOW_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (545 * scale_factor_x, 60 * scale_factor_y)
        self.yellow_power_up_indicator_visible = 1

        self.yellow_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_yellow_power_up_indicator(self):
        """
            Returns the yellow power up indicator sprite so its class attributes can be accessed

            :return: yellow_power_up_indicator: the yellow power up indicator sprite
            :type: turtle.Turtle()
        """

        return self

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
        self.time_value = power_up_setup.yellow_power_up_duration

    def remove(self):
        """
            Removes the yellow power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.yellow_power_up_indicator_visible = 0
        self.yellow_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self):
        """
            Makes the yellow power up indicator lit or unlit depending on if the yellow power up is active or not.

            :return: None
        """

        if self.yellow_power_up_active == 1:
            self.image = pygame.image.load(YELLOW_POWER_UP_INDICATOR_ON_TEXTURE).convert_alpha()
        else:
            self.image = pygame.image.load(YELLOW_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()

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


class BlueIndicator(pygame.sprite.Sprite):
    """
        Represents the blue power up indicator sprite at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the blue power up is active or not.

        Attributes:
            blue_power_up_active (int): Determines if the blue power up is currently active or not
            activate_time (float): Used to calculate the duration of exactly how long the blue power up can be active
                for.
            current_time (float): Also used in the calculation of how long the blue power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, scale_factor_x, scale_factor_y):
        """
            Create a blue power up indicator object and spawns it at the top of the screen.

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        self.image = pygame.image.load(BLUE_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (620 * scale_factor_x, 60 * scale_factor_y)
        self.blue_power_up_indicator_visible = 1

        self.blue_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_blue_power_up_indicator(self):
        """
            Returns the blue power up indicator sprite so its class attributes can be accessed

            :return: blue_power_up_indicator: the blue power up indicator sprite
            :type: turtle.Turtle()
        """

        return self

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
        self.time_value = power_up_setup.blue_power_up_duration

    def remove(self):
        """
            Removes the blue power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.blue_power_up_indicator_visible = 0
        self.blue_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self):
        """
            Makes the blue power up indicator lit or unlit depending on if the blue power up is active or not.

            :return: None
        """

        if self.blue_power_up_active == 1:
            self.image = pygame.image.load(BLUE_POWER_UP_INDICATOR_ON_TEXTURE).convert_alpha()
        else:
            self.image = pygame.image.load(BLUE_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()

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


class ExtraIndicator(pygame.sprite.Sprite):
    """
        Represents the third power up indicator sprite at the top of the screen in Laser Fighter. This can either be lit or
            unlit depending on if the yellow power up is active or not. It can also be green or red depending on the
            current mode of the game.

        Attributes:
            extra_power_up_active (int): Determines if the third power up is currently active or not (red or green)
            activate_time (float): Used to calculate the duration of exactly how long the third power up can be active
                for.
            current_time (float): Also used in the calculation of how long the third power up can be active for by
                determining the current time at each iteration of the loop
            time_value (int): The amount of seconds left before the power up deactivates (0 when it is not active)
            mode (int): The current mode of the game

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, mode, scale_factor_x, scale_factor_y):
        """
            Create a third power up indicator object and spawns it at the top of the screen.

            :param mode: Determines the current mode of the game
            :type mode: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        super().__init__()
        if mode == 1:
            self.image = pygame.image.load(GREEN_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()
        else:
            self.image = pygame.image.load(RED_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (690 * scale_factor_x, 60 * scale_factor_y)
        self.extra_power_up_indicator_visible = 1

        self.extra_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0
        self.mode = mode

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_extra_power_up_indicator(self):
        """
            Returns the third power up indicator sprite so its class attributes can be accessed

            :return: extra_power_up_indicator: the third power up indicator sprite
            :type: turtle.Turtle()
        """

        return self

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
        if self.mode == 1:
            self.time_value = power_up_setup.green_power_up_duration
        else:
            self.time_value = power_up_setup.red_power_up_duration

    def remove(self):
        """
            Removes the extra power up indicator sprite form the screen and resets its attributes.

            :return: None
        """

        self.extra_power_up_indicator_visible = 0
        self.extra_power_up_active = 0
        self.activate_time = 0
        self.current_time = 0
        self.time_value = 0

    def set_texture(self):
        """
            Makes the extra power up indicator lit or unlit depending on if the extra power up is active or not.

            :return: None
        """

        # If the mode is Machine Mode
        if self.mode == 1:
            # Make the extra power up indicator green
            if self.extra_power_up_active == 1:
                self.image = pygame.image.load(GREEN_POWER_UP_INDICATOR_ON_TEXTURE).convert_alpha()
            else:
                self.image = pygame.image.load(GREEN_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()
        # If the mode is Alien mode
        else:
            # Make the extra power up indicator red
            if self.extra_power_up_active == 1:
                self.image = pygame.image.load(RED_POWER_UP_INDICATOR_ON_TEXTURE).convert_alpha()
            else:
                self.image = pygame.image.load(RED_POWER_UP_INDICATOR_OFF_TEXTURE).convert_alpha()

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
