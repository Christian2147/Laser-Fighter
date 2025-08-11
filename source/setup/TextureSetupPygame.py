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
    File: TextureSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file is used to correctly load all of the textures into the game based off whether fullscreen mode is on
        or off.
"""

# Import the current fullscreen configuration
import pygame
# from setup.ConfigurationSetupPygame import settings
# fullscreen = settings.fullscreen


class TextureSetup:
    def __init__(self, scale_factor_x=1.0, scale_factor_y=1.0):
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

        # Attributes for all textures, initialized None
        self.MACHINE_PLAYER = None
        self.MACHINE_WASHER = None
        self.THE_INCINERATOR = None
        self.THE_BLACK_HOLE = None
        self.THE_STAR_KILLER = None
        self.MACHINE_PLAYER_LASER = None
        self.MACHINE_WASHER_LASER = None
        self.INCINERATOR_LASER = None
        self.BLACK_HOLE_LASER = None
        self.STAR_KILLER_LASER = None
        self.BLUE_MACHINE = None
        self.BLUE_MACHINE_LASER = None
        self.YELLOW_MACHINE = None
        self.YELLOW_MACHINE_LASER = None
        self.RED_MACHINE = None
        self.RED_MACHINE_LASER = None
        self.MACHINE_BOSS = None
        self.MACHINE_BOSS_LASER = None
        self.HEALTH_BAR_22 = None
        self.HEALTH_BAR_12 = None
        self.HEALTH_BAR_1010 = None
        self.HEALTH_BAR_910 = None
        self.HEALTH_BAR_810 = None
        self.HEALTH_BAR_710 = None
        self.HEALTH_BAR_610 = None
        self.HEALTH_BAR_510 = None
        self.HEALTH_BAR_410 = None
        self.HEALTH_BAR_310 = None
        self.HEALTH_BAR_210 = None
        self.HEALTH_BAR_110 = None
        self.HEALTH_BAR_33 = None
        self.HEALTH_BAR_23 = None
        self.HEALTH_BAR_13 = None
        self.ARMOR_BAR_10_10 = None
        self.ARMOR_BAR_10_9 = None
        self.ARMOR_BAR_10_8 = None
        self.ARMOR_BAR_10_7 = None
        self.ARMOR_BAR_10_6 = None
        self.ARMOR_BAR_10_5 = None
        self.ARMOR_BAR_10_4 = None
        self.ARMOR_BAR_10_3 = None
        self.ARMOR_BAR_10_2 = None
        self.ARMOR_BAR_10_1 = None
        self.EXPLOSION_1 = None
        self.EXPLOSION_2 = None
        self.GROUND = None
        self.SUN = None
        self.EARTH = None
        self.SPACE_SHIP = None
        self.HUMAN_STILL_RIGHT = None
        self.HUMAN_STILL_LEFT = None
        self.HUMAN_WALKING_RIGHT = None
        self.HUMAN_WALKING_LEFT = None
        self.PLAYER_HEAD_LASER = None
        self.THE_COOKER_LASER = None
        self.POISON_DART_LASER = None
        self.METEOR_GUN_LASER_RIGHT = None
        self.METEOR_GUN_LASER_LEFT = None
        self.SUPERNOVA_LASER_RIGHT = None
        self.SUPERNOVA_LASER_LEFT = None
        self.PLAYER_GUN_RIGHT = None
        self.PLAYER_GUN_LEFT = None
        self.THE_COOKER_RIGHT = None
        self.THE_COOKER_LEFT = None
        self.POISON_DART_GUN_RIGHT = None
        self.POISON_DART_GUN_LEFT = None
        self.METEOR_GUN_RIGHT = None
        self.METEOR_GUN_LEFT = None
        self.SUPERNOVA_RIGHT = None
        self.SUPERNOVA_LEFT = None
        self.OXYGEN_TANK = None
        self.ALIEN_STILL_LEFT_1_5 = None
        self.ALIEN_STILL_RIGHT_1_5 = None
        self.ALIEN_WALKING_LEFT_1_5 = None
        self.ALIEN_WALKING_RIGHT_1_5 = None
        self.ALIEN_STILL_LEFT_6_10 = None
        self.ALIEN_STILL_RIGHT_6_10 = None
        self.ALIEN_WALKING_LEFT_6_10 = None
        self.ALIEN_WALKING_RIGHT_6_10 = None
        self.ALIEN_STILL_LEFT_11_15 = None
        self.ALIEN_STILL_RIGHT_11_15 = None
        self.ALIEN_WALKING_LEFT_11_15 = None
        self.ALIEN_WALKING_RIGHT_11_15 = None
        self.ALIEN_BOSS = None
        self.ALIEN_DEATH_1 = None
        self.ALIEN_DEATH_2 = None
        self.PLAYER_DEATH_1 = None
        self.PLAYER_DEATH_2 = None
        self.MAIN_MENU_BUTTON_MAIN = None
        self.TITLE_SCREEN_BUTTON = None
        self.TITLE_SCREEN_BUTTON_SMALL = None
        self.MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED = None
        self.TITLE_SCREEN_BUTTON_HIGHLIGHTED = None
        self.TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED = None
        self.BUY_BUTTON = None
        self.BUY_BUTTON_HIGHLIGHTED = None
        self.POP_UP_BUTTON_SMALL = None
        self.POP_UP_BUTTON_SMALL_HIGHLIGHTED = None
        self.POP_UP_BUTTON_LARGE = None
        self.POP_UP_BUTTON_LARGE_HIGHLIGHTED = None
        self.INVENTORY_SLOT_FRAME = None
        self.INVENTORY_SLOT_FRAME_HIGHLIGHTED = None
        self.TAB = None
        self.TAB_HIGHLIGHTED = None
        self.SIDE_PANEL_SHOP = None
        self.POP_UP_MESSAGE_FRAME = None
        self.LOCKED = None
        self.TAB_SELECTOR = None
        self.SLOT_SELECTOR = None
        self.ERROR_ICON = None
        self.SETTINGS_AND_CONTROLS_BUTTON = None
        self.SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED = None
        self.MACHINE_DEFAULT_DISPLAY_ICON = None
        self.MACHINE_WASHER_DISPLAY_ICON = None
        self.THE_INCINERATOR_DISPLAY_ICON = None
        self.THE_BLACK_HOLE_DISPLAY_ICON = None
        self.THE_STAR_KILLER_DISPLAY_ICON = None
        self.ALIEN_DEFAULT_DISPLAY_ICON = None
        self.THE_COOKER_DISPLAY_ICON = None
        self.POISON_DART_DISPLAY_ICON = None
        self.METEOR_GUN_DISPLAY_ICON = None
        self.SUPERNOVA_DISPLAY_ICON = None
        self.YELLOW_POWER_UP_DISPLAY_ICON = None
        self.BLUE_POWER_UP_DISPLAY_ICON = None
        self.GREEN_POWER_UP_DISPLAY_ICON = None
        self.RED_POWER_UP_DISPLAY_ICON = None
        self.COIN_MAGNET_DISPLAY_ICON = None
        self.ARMOR_DISPLAY_ICON = None
        self.THORNS_DISPLAY_ICON = None
        self.HEART_POWER_UP_DISPLAY_ICON = None
        self.MACHINE_MODE_TAB_ICON = None
        self.GADGETS_TAB_ICON = None
        self.MACHINE_DEFAULT_SLOT_ICON = None
        self.MACHINE_WASHER_SLOT_ICON = None
        self.THE_INCINERATOR_SLOT_ICON = None
        self.THE_BLACK_HOLE_SLOT_ICON = None
        self.THE_STAR_KILLER_SLOT_ICON = None
        self.ALIEN_DEFAULT_SLOT_ICON = None
        self.THE_COOKER_SLOT_ICON = None
        self.POISON_DART_SLOT_ICON = None
        self.METEOR_GUN_SLOT_ICON = None
        self.SUPERNOVA_SLOT_ICON = None
        self.YELLOW_POWER_UP_SLOT_ICON = None
        self.RED_POWER_UP_SLOT_ICON = None
        self.GREEN_POWER_UP_SLOT_ICON = None
        self.BLUE_POWER_UP_SLOT_ICON = None
        self.COIN_MAGNET_SLOT_ICON = None
        self.ARMOR_SLOT_ICON = None
        self.THORNS_SLOT_ICON = None
        self.HEART_POWER_UP_SLOT_ICON = None
        self.YELLOW_LIGHTNING_POWER_UP = None
        self.GREEN_LIGHTNING_POWER_UP = None
        self.RED_LIGHTNING_POWER_UP = None
        self.BLUE_LIGHTNING_POWER_UP = None
        self.HEART_POWER_UP = None
        self.BLUE_POWER_UP_INDICATOR_ON = None
        self.GREEN_POWER_UP_INDICATOR_ON = None
        self.YELLOW_POWER_UP_INDICATOR_ON = None
        self.RED_POWER_UP_INDICATOR_ON = None
        self.BLUE_POWER_UP_INDICATOR_OFF = None
        self.GREEN_POWER_UP_INDICATOR_OFF = None
        self.YELLOW_POWER_UP_INDICATOR_OFF = None
        self.RED_POWER_UP_INDICATOR_OFF = None
        self.COPPER_COIN = None
        self.SILVER_COIN = None
        self.GOLD_COIN = None
        self.PLATINUM_COIN = None
        self.COIN_INDICATOR = None

    def load_scaled_texture(self, path):
        image = pygame.image.load(path).convert_alpha()
        width = int(image.get_width() * self.scale_factor_x)
        height = int(image.get_height() * self.scale_factor_y)
        return pygame.transform.scale(image, (width, height))

    def load_all_textures(self):
        self.MACHINE_PLAYER = self.load_scaled_texture("textures/player/Player.png")
        self.MACHINE_WASHER = self.load_scaled_texture("textures/player/Machine_Washer.png")
        self.THE_INCINERATOR = self.load_scaled_texture("textures/player/The_Incinerator.png")
        self.THE_BLACK_HOLE = self.load_scaled_texture("textures/player/The_Black_Hole.png")
        self.THE_STAR_KILLER = self.load_scaled_texture("textures/player/The_Star_Killer.png")
        self.MACHINE_PLAYER_LASER = self.load_scaled_texture("textures/lasers/Player_Laser.png")
        self.MACHINE_WASHER_LASER = self.load_scaled_texture("textures/lasers/Machine_Washer_Laser.png")
        self.INCINERATOR_LASER = self.load_scaled_texture("textures/lasers/Incinerator_Laser.png")
        self.BLACK_HOLE_LASER = self.load_scaled_texture("textures/lasers/The_Black_Hole_Laser.png")
        self.STAR_KILLER_LASER = self.load_scaled_texture("textures/lasers/The_Star_Killer_Laser.png")
        self.BLUE_MACHINE = self.load_scaled_texture("textures/machines/Enemy(1-5).png")
        self.BLUE_MACHINE_LASER = self.load_scaled_texture("textures/lasers/Enemy(1-5)_Laser.png")
        self.YELLOW_MACHINE = self.load_scaled_texture("textures/machines/Enemy(6-10).png")
        self.YELLOW_MACHINE_LASER = self.load_scaled_texture("textures/lasers/Enemy(6-10)_Laser.png")
        self.RED_MACHINE = self.load_scaled_texture("textures/machines/Enemy(11-15).png")
        self.RED_MACHINE_LASER = self.load_scaled_texture("textures/lasers/Enemy(11-15)_Laser.png")
        self.MACHINE_BOSS = self.load_scaled_texture("textures/machines/Boss.png")
        self.MACHINE_BOSS_LASER = self.load_scaled_texture("textures/lasers/Boss_Laser.png")
        self.HEALTH_BAR_22 = self.load_scaled_texture("textures/healthbars/HealthBar_2.2.png")
        self.HEALTH_BAR_12 = self.load_scaled_texture("textures/healthbars/HealthBar_2.1.png")
        self.HEALTH_BAR_1010 = self.load_scaled_texture("textures/healthbars/HealthBar_10.10.png")
        self.HEALTH_BAR_910 = self.load_scaled_texture("textures/healthbars/HealthBar_10.9.png")
        self.HEALTH_BAR_810 = self.load_scaled_texture("textures/healthbars/HealthBar_10.8.png")
        self.HEALTH_BAR_710 = self.load_scaled_texture("textures/healthbars/HealthBar_10.7.png")
        self.HEALTH_BAR_610 = self.load_scaled_texture("textures/healthbars/HealthBar_10.6.png")
        self.HEALTH_BAR_510 = self.load_scaled_texture("textures/healthbars/HealthBar_10.5.png")
        self.HEALTH_BAR_410 = self.load_scaled_texture("textures/healthbars/HealthBar_10.4.png")
        self.HEALTH_BAR_310 = self.load_scaled_texture("textures/healthbars/HealthBar_10.3.png")
        self.HEALTH_BAR_210 = self.load_scaled_texture("textures/healthbars/HealthBar_10.2.png")
        self.HEALTH_BAR_110 = self.load_scaled_texture("textures/healthbars/HealthBar_10.1.png")
        self.HEALTH_BAR_33 = self.load_scaled_texture("textures/healthbars/HealthBar_3.3.png")
        self.HEALTH_BAR_23 = self.load_scaled_texture("textures/healthbars/HealthBar_3.2.png")
        self.HEALTH_BAR_13 = self.load_scaled_texture("textures/healthbars/HealthBar_3.1.png")
        self.ARMOR_BAR_10_10 = self.load_scaled_texture("textures/armor/ArmorBar_10.10.png")
        self.ARMOR_BAR_10_9 = self.load_scaled_texture("textures/armor/ArmorBar_10.9.png")
        self.ARMOR_BAR_10_8 = self.load_scaled_texture("textures/armor/ArmorBar_10.8.png")
        self.ARMOR_BAR_10_7 = self.load_scaled_texture("textures/armor/ArmorBar_10.7.png")
        self.ARMOR_BAR_10_6 = self.load_scaled_texture("textures/armor/ArmorBar_10.6.png")
        self.ARMOR_BAR_10_5 = self.load_scaled_texture("textures/armor/ArmorBar_10.5.png")
        self.ARMOR_BAR_10_4 = self.load_scaled_texture("textures/armor/ArmorBar_10.4.png")
        self.ARMOR_BAR_10_3 = self.load_scaled_texture("textures/armor/ArmorBar_10.3.png")
        self.ARMOR_BAR_10_2 = self.load_scaled_texture("textures/armor/ArmorBar_10.2.png")
        self.ARMOR_BAR_10_1 = self.load_scaled_texture("textures/armor/ArmorBar_10.1.png")
        self.EXPLOSION_1 = self.load_scaled_texture("textures/explosions/Explosion1.png")
        self.EXPLOSION_2 = self.load_scaled_texture("textures/explosions/Explosion2.png")
        self.GROUND = self.load_scaled_texture("textures/ground/Ground.png")
        self.SUN = self.load_scaled_texture("textures/background/Sun.png")
        self.EARTH = self.load_scaled_texture("textures/background/Earth.png")
        self.SPACE_SHIP = self.load_scaled_texture("textures/background/Space_Ship.png")
        self.HUMAN_STILL_RIGHT = self.load_scaled_texture("textures/player/Player_Head_Still_Right.png")
        self.HUMAN_STILL_LEFT = self.load_scaled_texture("textures/player/Player_Head_Still_Left.png")
        self.HUMAN_WALKING_RIGHT = self.load_scaled_texture("textures/player/Player_Head_Walking_Right.png")
        self.HUMAN_WALKING_LEFT = self.load_scaled_texture("textures/player/Player_Head_Walking_Left.png")
        self.PLAYER_HEAD_LASER = self.load_scaled_texture("textures/lasers/Player_Head_Laser.png")
        self.THE_COOKER_LASER = self.load_scaled_texture("textures/lasers/The_Cooker_Laser.png")
        self.POISON_DART_LASER = self.load_scaled_texture("textures/lasers/Poison_Dart_Laser.png")
        self.METEOR_GUN_LASER_RIGHT = self.load_scaled_texture("textures/lasers/Meteor_Gun_Laser_Right.png")
        self.METEOR_GUN_LASER_LEFT = self.load_scaled_texture("textures/lasers/Meteor_Gun_Laser_Left.png")
        self.SUPERNOVA_LASER_RIGHT = self.load_scaled_texture("textures/lasers/The_Supernova_Laser_Right.png")
        self.SUPERNOVA_LASER_LEFT = self.load_scaled_texture("textures/lasers/The_Supernova_Laser_Left.png")
        self.PLAYER_GUN_RIGHT = self.load_scaled_texture("textures/gun/Player_Gun_Right.png")
        self.PLAYER_GUN_LEFT = self.load_scaled_texture("textures/gun/Player_Gun_Left.png")
        self.THE_COOKER_RIGHT = self.load_scaled_texture("textures/gun/The_Cooker_Right.png")
        self.THE_COOKER_LEFT = self.load_scaled_texture("textures/gun/The_Cooker_Left.png")
        self.POISON_DART_GUN_RIGHT = self.load_scaled_texture("textures/gun/Poison_Dart_Gun_Right.png")
        self.POISON_DART_GUN_LEFT = self.load_scaled_texture("textures/gun/Poison_Dart_Gun_Left.png")
        self.METEOR_GUN_RIGHT = self.load_scaled_texture("textures/gun/Meteor_Gun_Right.png")
        self.METEOR_GUN_LEFT = self.load_scaled_texture("textures/gun/Meteor_Gun_Left.png")
        self.SUPERNOVA_RIGHT = self.load_scaled_texture("textures/gun/Supernova_Right.png")
        self.SUPERNOVA_LEFT = self.load_scaled_texture("textures/gun/Supernova_Left.png")
        self.OXYGEN_TANK = self.load_scaled_texture("textures/other/Oxygen_Tank.png")
        self.ALIEN_STILL_LEFT_1_5 = self.load_scaled_texture("textures/aliens/Alien_Still_Left(1-5).png")
        self.ALIEN_STILL_RIGHT_1_5 = self.load_scaled_texture("textures/aliens/Alien_Still_Right(1-5).png")
        self.ALIEN_WALKING_LEFT_1_5 = self.load_scaled_texture("textures/aliens/Alien_Walking_Left(1-5).png")
        self.ALIEN_WALKING_RIGHT_1_5 = self.load_scaled_texture("textures/aliens/Alien_Walking_Right(1-5).png")
        self.ALIEN_STILL_LEFT_6_10 = self.load_scaled_texture("textures/aliens/Alien_Still_Left(6-10).png")
        self.ALIEN_STILL_RIGHT_6_10 = self.load_scaled_texture("textures/aliens/Alien_Still_Right(6-10).png")
        self.ALIEN_WALKING_LEFT_6_10 = self.load_scaled_texture("textures/aliens/Alien_Walking_Left(6-10).png")
        self.ALIEN_WALKING_RIGHT_6_10 = self.load_scaled_texture("textures/aliens/Alien_Walking_Right(6-10).png")
        self.ALIEN_STILL_LEFT_11_15 = self.load_scaled_texture("textures/aliens/Alien_Still_Left(11-15).png")
        self.ALIEN_STILL_RIGHT_11_15 = self.load_scaled_texture("textures/aliens/Alien_Still_Right(11-15).png")
        self.ALIEN_WALKING_LEFT_11_15 = self.load_scaled_texture("textures/aliens/Alien_Walking_Left(11-15).png")
        self.ALIEN_WALKING_RIGHT_11_15 = self.load_scaled_texture("textures/aliens/Alien_Walking_Right(11-15).png")
        self.ALIEN_BOSS = self.load_scaled_texture("textures/aliens/Alien_Boss.png")
        self.ALIEN_DEATH_1 = self.load_scaled_texture("textures/explosions/Alien_Death_1.png")
        self.ALIEN_DEATH_2 = self.load_scaled_texture("textures/explosions/Alien_Death_2.png")
        self.PLAYER_DEATH_1 = self.load_scaled_texture("textures/explosions/Player_Death_1.png")
        self.PLAYER_DEATH_2 = self.load_scaled_texture("textures/explosions/Player_Death_2.png")
        self.MAIN_MENU_BUTTON_MAIN = self.load_scaled_texture("textures/buttons/Main_Menu_Button_Main.png")
        self.TITLE_SCREEN_BUTTON = self.load_scaled_texture("textures/buttons/Title_Screen_Button.png")
        self.TITLE_SCREEN_BUTTON_SMALL = self.load_scaled_texture("textures/buttons/Title_Screen_Button_Small.png")
        self.MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Main_Menu_Button_Main_Highlighted.png")
        self.TITLE_SCREEN_BUTTON_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Title_Screen_Button_Highlighted.png")
        self.TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Title_Screen_Button_Small_Highlighted.png")
        self.BUY_BUTTON = self.load_scaled_texture("textures/buttons/Buy_Button.png")
        self.BUY_BUTTON_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Buy_Button_Highlighted.png")
        self.POP_UP_BUTTON_SMALL = self.load_scaled_texture("textures/buttons/Pop_Up_Button_Small.png")
        self.POP_UP_BUTTON_SMALL_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Pop_Up_Button_Small_Highlighted.png")
        self.POP_UP_BUTTON_LARGE = self.load_scaled_texture("textures/buttons/Pop_Up_Button_Large.png")
        self.POP_UP_BUTTON_LARGE_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Pop_Up_Button_Large_Highlighted.png")
        self.INVENTORY_SLOT_FRAME = self.load_scaled_texture("textures/buttons/Inventory_Slot_Frame.png")
        self.INVENTORY_SLOT_FRAME_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Inventory_Slot_Frame_Highlighted.png")
        self.TAB = self.load_scaled_texture("textures/buttons/Tab.png")
        self.TAB_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Tab_Highlighted.png")
        self.SIDE_PANEL_SHOP = self.load_scaled_texture("textures/gui/Side_Panel_Shop.png")
        self.POP_UP_MESSAGE_FRAME = self.load_scaled_texture("textures/gui/Pop_Up_Message_Frame.png")
        self.LOCKED = self.load_scaled_texture("textures/gui/Locked.png")
        self.TAB_SELECTOR = self.load_scaled_texture("textures/gui/Tab_Selector.png")
        self.SLOT_SELECTOR = self.load_scaled_texture("textures/gui/Slot_Selector.png")
        self.ERROR_ICON = self.load_scaled_texture("textures/gui/Error_Icon.png")
        self.SETTINGS_AND_CONTROLS_BUTTON = self.load_scaled_texture("textures/buttons/Settings_And_Controls_Button.png")
        self.SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED = self.load_scaled_texture("textures/buttons/Settings_And_Controls_Button_Highlighted.png")
        self.MACHINE_DEFAULT_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Machine_Default_Display_Icon.png")
        self.MACHINE_WASHER_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Machine_Washer_Display_Icon.png")
        self.THE_INCINERATOR_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/The_Incinerator_Display_Icon.png")
        self.THE_BLACK_HOLE_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/The_Black_Hole_Display_Icon.png")
        self.THE_STAR_KILLER_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/The_Star_Killer_Display_Icon.png")
        self.ALIEN_DEFAULT_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Alien_Default_Display_Icon.png")
        self.THE_COOKER_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/The_Cooker_Display_Icon.png")
        self.POISON_DART_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Poison_Dart_Display_Icon.png")
        self.METEOR_GUN_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Meteor_Gun_Display_Icon.png")
        self.SUPERNOVA_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Supernova_Display_Icon.png")
        self.YELLOW_POWER_UP_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Yellow_Power_Up_Display_Icon.png")
        self.BLUE_POWER_UP_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Blue_Power_Up_Display_Icon.png")
        self.GREEN_POWER_UP_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Green_Power_Up_Display_Icon.png")
        self.RED_POWER_UP_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Red_Power_Up_Display_Icon.png")
        self.COIN_MAGNET_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Coin_Magnet_Display_Icon.png")
        self.ARMOR_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Armor_Display_Icon.png")
        self.THORNS_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Thorns_Display_Icon.png")
        self.HEART_POWER_UP_DISPLAY_ICON = self.load_scaled_texture("textures/interface/display/Heart_Power_Up_Display_Icon.png")
        self.MACHINE_MODE_TAB_ICON = self.load_scaled_texture("textures/interface/icons/tab/Machine_Mode_Tab_Icon.png")
        self.GADGETS_TAB_ICON = self.load_scaled_texture("textures/interface/icons/tab/Gadgets_Tab_Icon.png")
        self.MACHINE_DEFAULT_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Machine_Default_Slot_Icon.png")
        self.MACHINE_WASHER_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Machine_Washer_Slot_Icon.png")
        self.THE_INCINERATOR_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/The_Incinerator_Slot_Icon.png")
        self.THE_BLACK_HOLE_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/The_Black_Hole_Slot_Icon.png")
        self.THE_STAR_KILLER_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/The_Star_Killer_Slot_Icon.png")
        self.ALIEN_DEFAULT_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Alien_Default_Slot_Icon.png")
        self.THE_COOKER_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/The_Cooker_Slot_Icon.png")
        self.POISON_DART_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Poison_Dart_Slot_Icon.png")
        self.METEOR_GUN_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Meteor_Gun_Slot_Icon.png")
        self.SUPERNOVA_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Supernova_Slot_Icon.png")
        self.YELLOW_POWER_UP_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Yellow_Power_Up_Slot_Icon.png")
        self.RED_POWER_UP_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Red_Power_Up_Slot_Icon.png")
        self.GREEN_POWER_UP_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Green_Power_Up_Slot_Icon.png")
        self.BLUE_POWER_UP_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Blue_Power_Up_Slot_Icon.png")
        self.COIN_MAGNET_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Coin_Magnet_Slot_Icon.png")
        self.ARMOR_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Armor_Slot_Icon.png")
        self.THORNS_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Thorns_Slot_Icon.png")
        self.HEART_POWER_UP_SLOT_ICON = self.load_scaled_texture("textures/interface/icons/slot/Heart_Power_Up_Slot_Icon.png")
        self.YELLOW_LIGHTNING_POWER_UP = self.load_scaled_texture("textures/powerups/Yellow_Lightning_Power_Up.png")
        self.GREEN_LIGHTNING_POWER_UP = self.load_scaled_texture("textures/powerups/Green_Lightning_Power_Up.png")
        self.RED_LIGHTNING_POWER_UP = self.load_scaled_texture("textures/powerups/Red_Lightning_Power_Up.png")
        self.BLUE_LIGHTNING_POWER_UP = self.load_scaled_texture("textures/powerups/Blue_Lightning_Power_Up.png")
        self.HEART_POWER_UP = self.load_scaled_texture("textures/powerups/Heart_Power_Up.png")
        self.BLUE_POWER_UP_INDICATOR_ON = self.load_scaled_texture("textures/powerups/Blue_Power_Up_Indicator_On.png")
        self.GREEN_POWER_UP_INDICATOR_ON = self.load_scaled_texture("textures/powerups/Green_Power_Up_Indicator_On.png")
        self.YELLOW_POWER_UP_INDICATOR_ON = self.load_scaled_texture("textures/powerups/Yellow_Power_Up_Indicator_On.png")
        self.RED_POWER_UP_INDICATOR_ON = self.load_scaled_texture("textures/powerups/Red_Power_Up_Indicator_On.png")
        self.BLUE_POWER_UP_INDICATOR_OFF = self.load_scaled_texture("textures/powerups/Blue_Power_Up_Indicator_Off.png")
        self.GREEN_POWER_UP_INDICATOR_OFF = self.load_scaled_texture("textures/powerups/Green_Power_Up_Indicator_Off.png")
        self.YELLOW_POWER_UP_INDICATOR_OFF = self.load_scaled_texture("textures/powerups/Yellow_Power_Up_Indicator_Off.png")
        self.RED_POWER_UP_INDICATOR_OFF = self.load_scaled_texture("textures/powerups/Red_Power_Up_Indicator_Off.png")
        self.COPPER_COIN = self.load_scaled_texture("textures/coins/Copper_Coin.png")
        self.SILVER_COIN = self.load_scaled_texture("textures/coins/Silver_Coin.png")
        self.GOLD_COIN = self.load_scaled_texture("textures/coins/Gold_Coin.png")
        self.PLATINUM_COIN = self.load_scaled_texture("textures/coins/Platinum_Coin.png")
        self.COIN_INDICATOR = self.load_scaled_texture("textures/coins/Coin_Indicator.png")
