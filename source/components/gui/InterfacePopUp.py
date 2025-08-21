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
    File: InterfacePopUp.py
    Author: Christian Marinkovich
    Date: 2025-08-20
    Description:
    This file contains the logic for the pop up. This includes the pop up sprite and all the logic associated
        with the pop up.
"""

import pygame
import math
from components.gui.InterfaceButton import Button


class PopUp(pygame.sprite.Sprite):
    """
        Represents a pop-up message in Laser Fighter with icons and buttons.

        Attributes:
            overlay (pygame.Surface): Semi-transparent overlay covering the screen
                behind the pop-up.
            image (pygame.Surface): The pop-up frame texture loaded from `textures`.
            rect (pygame.Rect): The rectangle representing the position and dimensions
                of the pop-up frame.
            icon (Icon): The icon displayed in the pop-up (error, warning, or question),
                depending on the provided `icon` parameter.
            pop_up_visible (int): Determines if the pop-up is currently visible (1) or hidden (0).

            yesButton (Button): The "Yes" button, only created if `type == 1`.
            noButton (Button): The "No" button, only created if `type == 1`.
            okButton (Button): The "OK" button, only created if `type == 2`.

            rendered_text (list): A list of pre-rendered text surfaces displayed inside
                the pop-up.
            font_dict (dict): Dictionary mapping font size/style names to
                corresponding `pygame.font.SysFont` objects.

            _text (str): The message text displayed in the pop-up.
            on_yes (Callable): Function to be executed when the "Yes" button is clicked.
            on_no (Callable): Function to be executed when the "No" button is clicked.
            on_ok (Callable): Function to be executed when the "OK" button is clicked.

            _textures (TextureSetup): Reference to the `TextureSetup` object that holds
                all game textures.
            _scale_factor (float): General scale factor applied in fullscreen mode.
            _scale_factor_x (float): Scale factor applied to the x-axis in fullscreen mode.
            _scale_factor_y (float): Scale factor applied to the y-axis in fullscreen mode.
        """

    def __init__(self, icon, text, type, textures, scale_factor, scale_factor_x, scale_factor_y, on_yes=None, on_no=None, on_ok=None):
        """
            Initializes a popup panel with configurable options, icons, text, and callbacks.

            :param icon: The icon texture displayed in the popup
            :type icon: str

            :param text: The text content displayed in the popup
            :type text: list[str]

            :param type: The type of popup (e.g., confirmation, alert, info)
            :type type: str

            :param textures: An object containing texture resources for Laser Fighter
            :type textures: TextureSetup

            :param scale_factor: The overall scaling factor for fullscreen mode
            :type scale_factor: float

            :param scale_factor_x: The scale factor applied along the x-axis in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor applied along the y-axis in fullscreen mode
            :type scale_factor_y: float

            :param on_yes: Optional callback function executed when the "Yes" button is pressed
            :type on_yes: callable | None

            :param on_no: Optional callback function executed when the "No" button is pressed
            :type on_no: callable | None

            :param on_ok: Optional callback function executed when the "OK" button is pressed
            :type on_ok: callable | None
        """

        super().__init__()

        self.overlay = pygame.Surface((1280 * scale_factor_x, 720 * scale_factor_y), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 100))

        self.image = textures.POP_UP_MESSAGE_FRAME
        self.rect = self.image.get_rect()
        self.rect.center = (640 * scale_factor_x, 360 * scale_factor_y)
        if icon == "error":
            self.icon = Icon("error", textures, 500 * scale_factor_x, 320 * scale_factor_y)
        elif icon == "warning":
            self.icon = Icon("warning", textures, 500 * scale_factor_x, 320 * scale_factor_y)
        elif icon == "question":
            self.icon = Icon("question", textures, 500 * scale_factor_x, 320 * scale_factor_y)
        self.pop_up_visible = 1

        if type == 1:
            self.yesButton = Button("Pop_Up_Small", 1, textures, scale_factor, scale_factor_x, scale_factor_y)
            self.noButton = Button("Pop_Up_Small", 2, textures, scale_factor, scale_factor_x, scale_factor_y)
        elif type == 2:
            self.okButton = Button("Pop_Up_Large", 1, textures, scale_factor, scale_factor_x, scale_factor_y)

        self.rendered_text = []
        self.font_dict = {
            "super_tiny_regular": pygame.font.SysFont("Courier", int(21.6 * scale_factor)),
            "super_tiny_bold": pygame.font.SysFont("Courier", int(21.6 * scale_factor), bold=True),

            "tiny_regular": pygame.font.SysFont("Courier", int(24.3 * scale_factor)),
            "tiny_bold": pygame.font.SysFont("Courier", int(24.3 * scale_factor), bold=True),

            "semi_tiny_regular": pygame.font.SysFont("Courier", int(27 * scale_factor)),
            "semi_tiny_bold": pygame.font.SysFont("Courier", int(27 * scale_factor), bold=True),

            "small_regular": pygame.font.SysFont("Courier", int(29.5 * scale_factor)),
            "small_bold": pygame.font.SysFont("Courier", int(29.5 * scale_factor), bold=True),

            "normal_regular": pygame.font.SysFont("Courier", int(32.5 * scale_factor)),
            "normal_bold": pygame.font.SysFont("Courier", int(32.5 * scale_factor), bold=True),

            "semi_medium_regular": pygame.font.SysFont("Courier", int(37.8 * scale_factor)),
            "semi_medium_bold": pygame.font.SysFont("Courier", int(37.8 * scale_factor), bold=True),

            "semi_large_regular": pygame.font.SysFont("Courier", int(40.5 * scale_factor)),
            "semi_large_bold": pygame.font.SysFont("Courier", int(40.5 * scale_factor), bold=True),

            "large_regular": pygame.font.SysFont("Courier", int(48.5 * scale_factor)),
            "large_bold": pygame.font.SysFont("Courier", int(48.5 * scale_factor), bold=True),

            "subtitle_regular": pygame.font.SysFont("Courier", int(65 * scale_factor)),
            "subtitle_bold": pygame.font.SysFont("Courier", int(65 * scale_factor), bold=True),

            "title_regular": pygame.font.SysFont("Courier", int(97 * scale_factor)),
            "title_bold": pygame.font.SysFont("Courier", int(97 * scale_factor), bold=True),
        }

        self._text = text
        self.on_yes = on_yes
        self.on_no = on_no
        self.on_ok = on_ok

        self._textures = textures
        self._scale_factor = scale_factor
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        if hasattr(self, 'overlay'):
            del self.overlay
        if hasattr(self, 'icon'):
            del self.icon
        if hasattr(self, 'yesButton'):
            del self.yesButton
        if hasattr(self, 'noButton'):
            del self.noButton
        if hasattr(self, 'okButton'):
            del self.okButton
        self.rendered_text = []
        del self

    def get_pop_up_frame(self):
        """
            Returns the pop up frame sprite so that its class attributes can be accessed.

            :return: self: The pop up frame sprite
            :type: pygame.sprite.Sprite
        """

        return self

    def get_pop_up_text(self):
        """
            Returns the rendered text for the pop up.

            :return: self: The pop up rendered text
            :type: list[string]
        """

        return self.rendered_text

    def get_pop_up_icon(self):
        """
            Returns the pop up icon sprite so that its class attributes can be accessed.

            :return: icon: The pop up icon sprite
            :type: pygame.sprite.Sprite
        """

        return self.icon

    def get_yes_button(self):
        """
            Returns the yes button sprite if it exists.

            :return: yesButton: The yes button sprite
            :type: pygame.sprite.Sprite
        """

        if hasattr(self, 'yesButton'):
            return self.yesButton

    def get_no_button(self):
        """
            Returns the no button sprite if it exists.

            :return: noButton: The no button sprite
            :type: pygame.sprite.Sprite
        """

        if hasattr(self, 'noButton'):
            return self.noButton

    def get_ok_button(self):
        """
            Returns the ok button sprite if it exists.

            :return: okButton: The ok button sprite
            :type: pygame.sprite.Sprite
        """

        if hasattr(self, 'okButton'):
            return self.okButton

    def remove(self):
        """
            Removes the pop up form the screen and resets its attributes.

            :return: None
        """

        self.pop_up_visible = 0
        self.rendered_text = []
        if hasattr(self, 'icon'):
            self.icon.icon_visible = 0
        if hasattr(self, 'yesButton'):
            self.yesButton.button_frame_visible = 0
        if hasattr(self, 'noButton'):
            self.noButton.button_frame_visible = 0
        if hasattr(self, 'okButton'):
            self.okButton.button_frame_visible = 0

    def write_text(self):
        """
            Renders the pop up text onto the screen.

            :return: None
        """

        self.rendered_text = []

        font_key = "tiny_regular"
        font = self.font_dict.get(font_key, self.font_dict["normal_regular"])

        start_x = self.rect.centerx - 70 * self._scale_factor_x
        start_y = self.rect.centery - 90 * self._scale_factor_y

        line_spacing = int(22 * self._scale_factor_y)

        y = start_y
        for line in self._text:
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(topleft=(start_x, y))
            self.rendered_text.append((text_surface, text_rect))
            y += line_spacing

    def clear_text(self):
        """
            Clears the pop up text from the screen.

            :return: None
        """

        self.rendered_text = []

    def handle_event(self, event):
        """
            Handles user input events for the pop-up panel. Specifically checks
            for mouse clicks on available buttons ("Yes", "No", "OK") and calls
            the corresponding callback function if defined.

            :param event: The pygame event to process.
            :type event: pygame.event.Event

            :return: None
        """

        if not self.pop_up_visible:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if hasattr(self, "yesButton") and self.yesButton and self.yesButton.rect.collidepoint(event.pos):
                if self.on_yes:
                    self.on_yes()
                self.pop_up_visible = False

            if hasattr(self, "noButton") and self.noButton and self.noButton.rect.collidepoint(event.pos):
                if self.on_no:
                    self.on_no()
                self.pop_up_visible = False

            if hasattr(self, "okButton") and self.okButton and self.okButton.rect.collidepoint(event.pos):
                if self.on_ok:
                    self.on_ok()
                self.pop_up_visible = False


class Icon(pygame.sprite.Sprite):
    """
        A generic icon sprite used for displaying symbols such as errors, warnings,
        or questions within a Pygame application.

        This class extends `pygame.sprite.Sprite` and represents a simple
        image-based icon that can be placed on the screen at a given position.
        It supports checking visibility and calculating distances to other sprites.

        Attributes:
            self (pygame.sprite.Sprite): The icon sprite.
            icon_visible (int): Visibility flag (1 for visible, 0 for hidden).
            _textures (TextureSetup):  A container object holding references to loaded icon textures.
    """

    def __init__(self, type, textures, x, y):
        """
            Initialize the icon object with a type, textures, and position.

            :param type: The type of icon to display ("error", "warning", or "question").
            :type type: string

            :param textures: The texture manager that contains icon textures.
            :type textures: TextureSetup

            :param x: The x-coordinate of the icon’s center position.
            :type x: float

            :param y: The y-coordinate of the icon’s center position.
            :type y: float
        """

        super().__init__()
        if type == "error":
            self.image = textures.ERROR_ICON
        elif type == "warning":
            self.image = textures.WARNING_ICON
        elif type == "question":
            self.image = textures.QUESTION_ICON
        self.rect = self.image.get_rect()
        self.rect.center = (int(x), int(y))
        self.icon_visible = 1

        self._textures = textures

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()

    def isvisible(self):
        """
            Check if the icon is currently marked as visible.

            :return: icon_visible: Determines whether the icon is currently visible or not.
        """

        return self.icon_visible

    def distance(self, other_sprite):
        """
            Calculates the Euclidean distance to another sprite.

            :param other_sprite: Another sprite with a rect attribute
            :type: pygame.sprite.Sprite

            :return: The distance between the two sprites
            :type: float
        """

        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)
