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
    File: InterfacePanel.py
    Author: Christian Marinkovich
    Date: 2024-07-14
    Description:
    This file contains the logic for the side panel. This includes updating the description on the side panel and
        loading all of the preview data of the item currently selected.
"""

import pygame
from setup.ConfigurationSetupPygame import shop_config
from setup.data.MilestoneMessagesPygame import MILESTONE_1_MESSAGE
from setup.data.MilestoneMessagesPygame import MILESTONE_2_MESSAGE
from setup.data.MilestoneMessagesPygame import MILESTONE_3_MESSAGE
from setup.data.MilestoneMessagesPygame import MILESTONE_4_MESSAGE
from setup.data.ShopDescriptionsPygame import MAIN_DESCRIPTION
from setup.data.ShopDescriptionsPygame import ALIEN_LOCKED_DESCRIPTION
from setup.data.ShopDescriptionsPygame import MACHINE_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import ALIEN_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import YELLOW_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import BLUE_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import GREEN_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import RED_POWER_UP_DESCRIPTIONS
from setup.data.ShopDescriptionsPygame import GADGET_DESCRIPTIONS
from setup.TextureSetup import SIDE_PANEL_SHOP_TEXTURE
from setup.TextureSetup import POP_UP_MESSAGE_FRAME_TEXTURE
from setup.TextureSetup import MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import MACHINE_WASHER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_INCINERATOR_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_BLACK_HOLE_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_STAR_KILLER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THE_COOKER_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import POISON_DART_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import METEOR_GUN_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import SUPERNOVA_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import BLUE_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import GREEN_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import RED_POWER_UP_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import COIN_MAGNET_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import ARMOR_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import THORNS_DISPLAY_ICON_TEXTURE
from setup.TextureSetup import HEART_POWER_UP_DISPLAY_ICON_TEXTURE


class Panel(pygame.sprite.Sprite):
    """
        Represents the panel in Laser Fighter for displaying important information.

        Attributes:
            panel_indicator (turtle.Turtle()): The sprite that displays the visual element on the panel

            type (string): The type of panel generated (depending on the current screen)
            category (string): The current type of description being displayed
            id (int): The id for the specific description being displayed

            scale_factor (float): The general scale factor used in fullscreen mode based off of the shortest axis
            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, type, scale_factor, scale_factor_x, scale_factor_y, id=1):
        """
            Creates a panel object to be displayed on the screen.

            :param type: The type of panel to create
            :type type: string

            :param scale_factor: The general scale factor used in fullscreen mode based off of the shortest axis
            :type scale_factor: float

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float

            :param id: The id of the milestone to display (Only for Machine Mode and Alien Mode)
            :type id: int
        """

        super().__init__()
        if type == "Shop":
            self.image = pygame.image.load(SIDE_PANEL_SHOP_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (int(1090 * scale_factor_x), int(360 * scale_factor_y))
        elif type == "Machine_Mode":
            self.image = pygame.image.load(POP_UP_MESSAGE_FRAME_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (int(640 * scale_factor_x), int(360 * scale_factor_y))
        elif type == "Alien_Mode":
            self.image = pygame.image.load(POP_UP_MESSAGE_FRAME_TEXTURE)
            self.rect = self.image.get_rect()
            self.rect.center = (int(240 * scale_factor_x), int(260 * scale_factor_y))
        self.panel_visible = 1

        self.color = "white"
        self.rendered_text = []
        self.font_dict = {
            "super_tiny_regular": pygame.font.SysFont("Courier", int(21.6 * scale_factor)),
            "super_tiny_bold": pygame.font.SysFont("Courier", int(21.6 * scale_factor), bold=True),
            
            "tiny_regular": pygame.font.SysFont("Courier", int(24.3 * scale_factor)),
            "tiny_bold": pygame.font.SysFont("Courier", int(24.3 * scale_factor), bold=True),

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
        self.text_visible = 1

        if type == "Shop":
            self.panel_indicator = PanelIndicator(self.rect.centerx, self.rect.centery + 190 * scale_factor_y, scale_factor_x, scale_factor_y)
            self.indicator_created = 1
        else:
            self.indicator_created = 0

        # Display the welcome message by default in the shop
        self.type = type
        self.category = "Welcome"
        self.id = id

        self.scale_factor = scale_factor
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.kill()
        self.rendered_text = []
        del self

    def get_panel_frame(self):
        """
            Returns the panel frame so that its class attributes can be accessed.

            :return: panel_frame: the panel frame
            :type: turtle.Turtle()
        """

        return self

    def get_panel_text(self):
        """
            Returns the panel text so that its class attributes can be accessed.

            :return: panel_text: the panel text
            :type: turtle.Turtle()
        """

        return self.rendered_text

    def get_panel_indicator(self):
        """
            Returns the panel indicator so that its class attributes can be accessed.

            :return: panel_indicator: the panel indicator
            :type: turtle.Turtle()
        """

        return self.panel_indicator

    def get_panel_id(self):
        """
            Returns the panel id so that its class attributes can be accessed.

            :return: id: the panel id
            :type: int
        """

        return self.id

    def set_panel_text(self, new_category, new_id):
        """
            Sets the panel text to show the information of the shop slot specified by the new category and the new id.

            :param new_category: The new category to be displayed (Machine Mode, Alien Mode, Power Ups)
            :type new_category: string

            :param new_id: The new id of the slot to display
            :type new_id: int

            :return: None
        """

        self.category = new_category
        self.id = new_id

    def remove(self):
        """
            Removes the panel from the screen and resets its attributes.

            :return: None
        """

        self.panel_visible = 0
        if self.indicator_created:
            self.panel_indicator.indicator_visible = 0
        self.rendered_text = []
        self.text_visible = 0

    def write_text(self):
        """
            Writes the panels text based on the category of the slot to display and the id of the slot to display.
            These descriptions are extracted from ShopDescriptions.py

            :return: None
        """

        self.clear_text()

        size_map = {
            16: "super_tiny",
            18: "tiny",
            22: "small",
            24: "normal",
            28: "semi_medium",
            30: "semi_large",
            36: "large",
            48: "subtitle",
            72: "title",
        }

        if self.type == "Shop":
            if self.category == "Welcome":
                description_obj = MAIN_DESCRIPTION[self.id - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 36
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery - 325 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Machine_Mode":
                description_obj = MACHINE_DESCRIPTIONS[self.id - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 24
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Alien_Mode":
                if shop_config.alien_slots_unlocked[self.id - 1] != -1:
                    description_obj = ALIEN_DESCRIPTIONS[self.id - 1]
                    lines = description_obj.get_text()
                    raw_size = int(description_obj.get_size())
                    font_size_key = size_map.get(raw_size, "normal")
                    font_type = "regular"
                    line_spacing = 24
                    start_x = self.rect.centerx - 155 * self.scale_factor_x
                    start_y = self.rect.centery + 55 * self.scale_factor_y

                    self.rendered_text = self.render_multiline_text(
                        lines=lines,
                        font_size=font_size_key,
                        font_type=font_type,
                        start_x=start_x,
                        start_y=start_y,
                        line_spacing=line_spacing,
                        scale_factor=self.scale_factor_y
                    )
                else:
                    description_obj = ALIEN_LOCKED_DESCRIPTION[0]
                    lines = description_obj.get_text()
                    raw_size = int(description_obj.get_size())
                    font_size_key = size_map.get(raw_size, "normal")
                    font_type = "regular"
                    line_spacing = 24
                    start_x = self.rect.centerx - 155 * self.scale_factor_x
                    start_y = self.rect.centery + 55 * self.scale_factor_y

                    self.rendered_text = self.render_multiline_text(
                        lines=lines,
                        font_size=font_size_key,
                        font_type=font_type,
                        start_x=start_x,
                        start_y=start_y,
                        line_spacing=line_spacing,
                        scale_factor=self.scale_factor_y
                    )
            elif self.category == "Yellow_Power_Up":
                check_setting = shop_config.yellow_power_up_level

                description_obj = YELLOW_POWER_UP_DESCRIPTIONS[check_setting - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 30
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Blue_Power_Up":
                check_setting = shop_config.blue_power_up_level

                description_obj = BLUE_POWER_UP_DESCRIPTIONS[check_setting - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 30
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Green_Power_Up":
                check_setting = shop_config.green_power_up_level

                description_obj = GREEN_POWER_UP_DESCRIPTIONS[check_setting - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 30
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Red_Power_Up":
                check_setting = shop_config.red_power_up_level

                description_obj = RED_POWER_UP_DESCRIPTIONS[check_setting - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 30
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            elif self.category == "Gadget":
                description_obj = GADGET_DESCRIPTIONS[self.id - 1]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 27
                start_x = self.rect.centerx - 155 * self.scale_factor_x
                start_y = self.rect.centery + 40 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            self.set_indicator()
        elif self.type == "Machine_Mode":
            if self.id == 1:
                description_obj = MILESTONE_1_MESSAGE[0]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 24
                start_x = self.rect.centerx
                start_y = self.rect.centery + 105 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            else:
                description_obj = MILESTONE_2_MESSAGE[0]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 24
                start_x = self.rect.centerx
                start_y = self.rect.centery + 105 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
        elif self.type == "Alien_Mode":
            if self.id == 1:
                description_obj = MILESTONE_3_MESSAGE[0]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 24
                start_x = self.rect.centerx
                start_y = self.rect.centery + 105 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )
            else:
                description_obj = MILESTONE_4_MESSAGE[0]
                lines = description_obj.get_text()
                raw_size = int(description_obj.get_size())
                font_size_key = size_map.get(raw_size, "normal")
                font_type = "regular"
                line_spacing = 24
                start_x = self.rect.centerx
                start_y = self.rect.centery + 105 * self.scale_factor_y

                self.rendered_text = self.render_multiline_text(
                    lines=lines,
                    font_size=font_size_key,
                    font_type=font_type,
                    start_x=start_x,
                    start_y=start_y,
                    line_spacing=line_spacing,
                    scale_factor=self.scale_factor_y
                )

    def render_multiline_text(self, lines, font_size, font_type, start_x, start_y, line_spacing, scale_factor):
        rendered_lines = []
        y = start_y

        font_key = f"{font_size}_{font_type}"
        font = self.font_dict.get(font_key)
        if font is None:
            font = self.font_dict["normal_regular"]

        for line in lines:
            text_surface = font.render(line, True, self.color)
            text_rect = text_surface.get_rect(topleft=(start_x, y))
            rendered_lines.append((text_surface, text_rect))
            y += int(line_spacing * scale_factor)

        return rendered_lines

    def clear_text(self):
        self.rendered_text = []

    def set_indicator(self):
        """
            Sets the panel indicator (Icon) based on the category (Page of the slot) and the id (Id of the slot).

            :return: None
        """

        if self.category == "Welcome":
            # Do not need the panel indicator if the welcome message is being displayed.
            self.panel_indicator.indicator_visible = 0
        else:
            if self.category == "Machine_Mode":
                if self.id == 1:
                    self.panel_indicator.image = pygame.image.load(MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE)
                elif self.id == 2:
                    self.panel_indicator.image = pygame.image.load(MACHINE_WASHER_DISPLAY_ICON_TEXTURE)
                elif self.id == 3:
                    self.panel_indicator.image = pygame.image.load(THE_INCINERATOR_DISPLAY_ICON_TEXTURE)
                elif self.id == 4:
                    self.panel_indicator.image = pygame.image.load(THE_BLACK_HOLE_DISPLAY_ICON_TEXTURE)
                elif self.id == 5:
                    self.panel_indicator.image = pygame.image.load(THE_STAR_KILLER_DISPLAY_ICON_TEXTURE)
            elif self.category == "Alien_Mode":
                if self.id == 1:
                    self.panel_indicator.image = pygame.image.load(ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE)
                elif self.id == 2:
                    self.panel_indicator.image = pygame.image.load(THE_COOKER_DISPLAY_ICON_TEXTURE)
                elif self.id == 3:
                    self.panel_indicator.image = pygame.image.load(POISON_DART_DISPLAY_ICON_TEXTURE)
                elif self.id == 4:
                    self.panel_indicator.image = pygame.image.load(METEOR_GUN_DISPLAY_ICON_TEXTURE)
                elif self.id == 5:
                    self.panel_indicator.image = pygame.image.load(SUPERNOVA_DISPLAY_ICON_TEXTURE)
            elif self.category == "Yellow_Power_Up":
                self.panel_indicator.image = pygame.image.load(YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Blue_Power_Up":
                self.panel_indicator.image = pygame.image.load(BLUE_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Green_Power_Up":
                self.panel_indicator.image = pygame.image.load(GREEN_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Red_Power_Up":
                self.panel_indicator.image = pygame.image.load(RED_POWER_UP_DISPLAY_ICON_TEXTURE)
            elif self.category == "Gadget":
                if self.id == 1:
                    self.panel_indicator.image = pygame.image.load(COIN_MAGNET_DISPLAY_ICON_TEXTURE)
                elif self.id == 2:
                    self.panel_indicator.image = pygame.image.load(ARMOR_DISPLAY_ICON_TEXTURE)
                elif self.id == 3:
                    self.panel_indicator.image = pygame.image.load(THORNS_DISPLAY_ICON_TEXTURE)
                elif self.id == 4:
                    self.panel_indicator.image = pygame.image.load(HEART_POWER_UP_DISPLAY_ICON_TEXTURE)
            self.panel_indicator.rect = self.panel_indicator.image.get_rect()
            self.panel_indicator.indicator_visible = 1


class PanelIndicator(pygame.sprite.Sprite):
    def __init__(self, x, y, scale_factor_x, scale_factor_y):
        super().__init__()
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.indicator_visible = 1

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        self.kill()
        del self

    def remove(self):
        self.indicator_visible = 0
