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
    File: InterfaceTextBox.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic for regular splash text and labeling in the game. This does not include text on
    buttons and only includes standalone text.
    It creates a text box and has functionality for hiding the text from being displayed on the screen.
"""

import pygame
import time


class Text(pygame.sprite.Sprite):
    """
        Represents a standalone textbox in the game.

        Attributes:
            self (pygame.sprite.Sprite): The text object itself

            moving (int): Determines the direction the text box will move
            start_time (float): Stores the timestamp for when the text box should move
            movement_activated (int): determines if the movement of the textbox has been activated or not.

            id (int): The id value assigned to each textbox
            in_use (int): Determines whether a text box object is currently on the screen or not

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
    """

    def __init__(self, id, x, y, color, scale_factor, scale_factor_x):
        """
            Creates a text box object on the screen

            :param id: The id of the given text box
            :type id: int

            :param x: The x-coordinate of where the text box should be placed
            :type x: float

            :param y: The y-coordinate of where the text box should be placed
            :type y: float

            :param color: The color of the text box
            :type color: string

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float
        """

        super().__init__()
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)  # Create transparent surface
        self.image.fill((0, 0, 0, 0))  # Fully transparent
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.color = color
        self.text_box_visible = 1

        self.small_font = pygame.font.SysFont("Courier", int(29.5 * scale_factor))
        self.normal_font = pygame.font.SysFont("Courier", int(32.5 * scale_factor))
        self.large_font = pygame.font.SysFont("Courier", int(48.5 * scale_factor))
        self.subtitle_font = pygame.font.SysFont("Courier", int(65 * scale_factor))
        self.title_font = pygame.font.SysFont("Courier", int(97 * scale_factor))

        self.small_font_bold = pygame.font.SysFont("Courier", int(29.5 * scale_factor), bold=True)
        self.normal_font_bold = pygame.font.SysFont("Courier", int(32.5 * scale_factor), bold=True)
        self.large_font_bold = pygame.font.SysFont("Courier", int(48.5 * scale_factor), bold=True)
        self.subtitle_font_bold = pygame.font.SysFont("Courier", int(65 * scale_factor), bold=True)
        self.title_font_bold = pygame.font.SysFont("Courier", int(97 * scale_factor), bold=True)

        self.moving = 1
        self.start_time = 0
        self.movement_activated = 0
        self.id = id
        self.in_use = 1

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def get_text_box(self):
        """
            Returns the text_box sprite so its class attributes can be accessed

            :return: self: the text box sprite
            :type: pygame.sprite.Sprite
        """

        return self

    def get_id(self):
        """
            Returns the id of the given text box

            :return: id: the id of the text box
            :type: int
        """

        return self.id

    def remove(self):
        """
            Removes the text box sprite form the screen and resets its attributes.

            :return: None
        """

        self.text_box_visible = 0
        self.in_use = 0
        self.movement_activated = 0

    def clear(self):
        """
            Removes the text box from the screen

            :return: None
        """

        self.text_box_visible = 0

    def write(self, text, size, type):
        """
            Writes the given text on the text box object and displays it on the screen.

            :param text: The text to be written
            :type text: string

            :param size: The font size of the text to be written
            :type size: int

            :param type: The type of text to be written (bold, underlines, normal, italic)
            :type type: string

            :return: None
        """

        old_center = self.rect.center
        if size == "small":
            if type == "bold":
                self.image = self.small_font_bold.render(text, True, self.color)
            else:
                self.image = self.small_font.render(text, True, self.color)

        elif size == "normal":
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)

        elif size == "large":
            if type == "bold":
                self.image = self.large_font_bold.render(text, True, self.color)
            else:
                self.image = self.large_font.render(text, True, self.color)

        elif size == "subtitle":
            if type == "bold":
                self.image = self.subtitle_font_bold.render(text, True, self.color)
            else:
                self.image = self.subtitle_font.render(text, True, self.color)

        elif size == "title":
            if type == "bold":
                self.image = self.title_font_bold.render(text, True, self.color)
            else:
                self.image = self.title_font.render(text, True, self.color)

        else:
            # fallback if size not recognized, default to normal
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)
        self.rect = self.image.get_rect(center=old_center)

    def write_left(self, text, size, type):
        """
            Writes the given text on the text box object and aligns it to the left and then displays it on the screen.

            :param text: The text to be written
            :type text: string

            :param size: The font size of the text to be written
            :type size: int

            :param type: The type of text to be written (bold, underlines, normal, italic)
            :type type: string

            :return: None
        """

        old_topleft = self.rect.topleft
        if size == "small":
            if type == "bold":
                self.image = self.small_font_bold.render(text, True, self.color)
            else:
                self.image = self.small_font.render(text, True, self.color)

        elif size == "normal":
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)

        elif size == "large":
            if type == "bold":
                self.image = self.large_font_bold.render(text, True, self.color)
            else:
                self.image = self.large_font.render(text, True, self.color)

        elif size == "subtitle":
            if type == "bold":
                self.image = self.subtitle_font_bold.render(text, True, self.color)
            else:
                self.image = self.subtitle_font.render(text, True, self.color)

        elif size == "title":
            if type == "bold":
                self.image = self.title_font_bold.render(text, True, self.color)
            else:
                self.image = self.title_font.render(text, True, self.color)

        else:
            # fallback if size not recognized, default to normal
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)
        self.rect = self.image.get_rect(topleft=old_topleft)

    def write_right(self, text, size, type):
        """
            Writes the given text on the text box object and aligns it to the right and then displays it on the screen.

            :param text: The text to be written
            :type text: string

            :param size: The font size of the text to be written
            :type size: int

            :param type: The type of text to be written (bold, underlines, normal, italic)
            :type type: string

            :return: None
        """

        old_topright = self.rect.topright

        if size == "small":
            if type == "bold":
                self.image = self.small_font_bold.render(text, True, self.color)
            else:
                self.image = self.small_font.render(text, True, self.color)

        elif size == "normal":
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)

        elif size == "large":
            if type == "bold":
                self.image = self.large_font_bold.render(text, True, self.color)
            else:
                self.image = self.large_font.render(text, True, self.color)

        elif size == "subtitle":
            if type == "bold":
                self.image = self.subtitle_font_bold.render(text, True, self.color)
            else:
                self.image = self.subtitle_font.render(text, True, self.color)

        elif size == "title":
            if type == "bold":
                self.image = self.title_font_bold.render(text, True, self.color)
            else:
                self.image = self.title_font.render(text, True, self.color)

        else:
            # fallback if size not recognized, default to normal
            if type == "bold":
                self.image = self.normal_font_bold.render(text, True, self.color)
            else:
                self.image = self.normal_font.render(text, True, self.color)

        self.rect = self.image.get_rect(topright=old_topright)

    def set_color(self, color):
        """
            Sets the color of the text in the text box.

            :param color: The new color of the text
            :type color: string

            :return: None
        """

        self.color = color

    def move(self, mode):
        """
            Moves the text side to side on the screen (Used for screen titles)

            :return: None
        """

        # If the movement has just started, a start time is created for it
        if self.movement_activated == 0:
            self.start_time = time.time()
            self.movement_activated = 1
        # Move the text box every 0.02 seconds
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= 0.02:
            if mode == "Shop":
                # Text box reaches the left limit
                if self.rect.centerx < 445 * self.scale_factor_x:
                    # Move right
                    self.moving = 1
                # Text box reaches the right limit
                if self.rect.centerx > 685 * self.scale_factor_x:
                    # Move left
                    self.moving = -1
            else:
                # Text box reaches the left limit
                if self.rect.centerx < 520 * self.scale_factor_x:
                    # Move right
                    self.moving = 1
                # Text box reaches the right limit
                if self.rect.centerx > 760 * self.scale_factor_x:
                    # Move left
                    self.moving = -1
            # Move 5 units each timed iteration
            if self.moving == 1:
                # Calculate the delta movement
                # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                # Done to ensure the game speed stays the same regardless of frame rate
                delta_movement = 5 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                self.rect.centerx = self.rect.centerx + 5 * self.scale_factor_x + delta_movement
            if self.moving == -1:
                delta_movement = 5 * self.scale_factor_x * ((elapsed_time - 0.02) / 0.02)
                self.rect.centerx = self.rect.centerx - 5 * self.scale_factor_x - delta_movement
            self.start_time = time.time()
