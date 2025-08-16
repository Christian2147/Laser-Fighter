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

import pygame
import math
from components.gui.InterfaceButtonPygame import Button


class PopUp(pygame.sprite.Sprite):
    def __init__(self, icon, text, type, textures, callbacks, scale_factor, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = textures.POP_UP_MESSAGE_FRAME
        self.rect = self.image.get_rect()
        if icon == "error":
            self.icon = Icon("error", textures, 400 * scale_factor_x, 300 * scale_factor_y)
        elif icon == "warning":
            self.icon = Icon("warning", textures, 400 * scale_factor_x, 300 * scale_factor_y)
        elif icon == "question":
            self.icon = Icon("question", textures, 400 * scale_factor_x, 300 * scale_factor_y)
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
        self.callbacks = callbacks

        self._textures = textures
        self._scale_factor = scale_factor
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
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


class Icon(pygame.sprite.Sprite):
    def __init__(self, type, textures, x, y):
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
        self.kill()

    def isvisible(self):
        return self.icon_visible

    def distance(self, other_sprite):
        """Return the Euclidean distance to another sprite based on center positions."""
        dx = self.rect.centerx - other_sprite.rect.centerx
        dy = self.rect.centery - other_sprite.rect.centery
        return math.hypot(dx, dy)
