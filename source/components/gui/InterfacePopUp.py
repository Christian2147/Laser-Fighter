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
from components.gui.InterfaceButton import Button


class PopUp(pygame.sprite.Sprite):
    def __init__(self, icon, text, type, textures, scale_factor, scale_factor_x, scale_factor_y, on_yes=None, on_no=None, on_ok=None):
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
        return self

    def get_pop_up_text(self):
        return self.rendered_text

    def get_pop_up_icon(self):
        return self.icon

    def get_yes_button(self):
        if hasattr(self, 'yesButton'):
            return self.yesButton

    def get_no_button(self):
        if hasattr(self, 'noButton'):
            return self.noButton

    def get_ok_button(self):
        if hasattr(self, 'okButton'):
            return self.okButton

    def remove(self):
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
        self.rendered_text = []

    def handle_event(self, event):
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
