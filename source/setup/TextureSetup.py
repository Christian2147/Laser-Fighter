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

from setup.ConfigurationSetup import settings
fullscreen = settings.fullscreen

MACHINE_PLAYER_TEXTURE = "Textures/Player/Player.gif" if fullscreen == 0 else "Textures/Player/Player_Scaled.gif"
MACHINE_PLAYER_LASER_TEXTURE = "Textures/Lasers/Player_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Player_Laser_Scaled.gif"
MACHINE_WASHER_LASER_TEXTURE = "Textures/Lasers/Machine_Washer_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Machine_Washer_Laser_Scaled.gif"
INCINERATOR_LASER_TEXTURE = "Textures/Lasers/Incinerator_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Incinerator_Laser_Scaled.gif"
BLUE_MACHINE_TEXTURE = "Textures/Enemies/Enemy(1-5).gif" if fullscreen == 0 else "Textures/Enemies/Enemy(1-5)_Scaled.gif"
BLUE_MACHINE_LASER_TEXTURE = "Textures/Lasers/Enemy(1-5)_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Enemy(1-5)_Laser_Scaled.gif"
YELLOW_MACHINE_TEXTURE = "Textures/Enemies/Enemy(6-10).gif" if fullscreen == 0 else "Textures/Enemies/Enemy(6-10)_Scaled.gif"
YELLOW_MACHINE_LASER_TEXTURE = "Textures/Lasers/Enemy(6-10)_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Enemy(6-10)_Laser_Scaled.gif"
RED_MACHINE_TEXTURE = "Textures/Enemies/Enemy(11-15).gif" if fullscreen == 0 else "Textures/Enemies/Enemy(11-15)_Scaled.gif"
RED_MACHINE_LASER_TEXTURE = "Textures/Lasers/Enemy(11-15)_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Enemy(11-15)_Laser_Scaled.gif"
MACHINE_BOSS_TEXTURE = "Textures/Enemies/Boss.gif" if fullscreen == 0 else "Textures/Enemies/Boss_Scaled.gif"
MACHINE_BOSS_LASER_TEXTURE = "Textures/Lasers/Boss_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Boss_Laser_Scaled.gif"
HEALTH_BAR_22_TEXTURE = "Textures/Health_Bars/HealthBar_2.2.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_2.2_Scaled.gif"
HEALTH_BAR_12_TEXTURE = "Textures/Health_Bars/HealthBar_2.1.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_2.1_Scaled.gif"
HEALTH_BAR_1010_TEXTURE = "Textures/Health_Bars/HealthBar_10.10.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.10_Scaled.gif"
HEALTH_BAR_910_TEXTURE = "Textures/Health_Bars/HealthBar_10.9.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.9_Scaled.gif"
HEALTH_BAR_810_TEXTURE = "Textures/Health_Bars/HealthBar_10.8.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.8_Scaled.gif"
HEALTH_BAR_710_TEXTURE = "Textures/Health_Bars/HealthBar_10.7.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.7_Scaled.gif"
HEALTH_BAR_610_TEXTURE = "Textures/Health_Bars/HealthBar_10.6.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.6_Scaled.gif"
HEALTH_BAR_510_TEXTURE = "Textures/Health_Bars/HealthBar_10.5.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.5_Scaled.gif"
HEALTH_BAR_410_TEXTURE = "Textures/Health_Bars/HealthBar_10.4.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.4_Scaled.gif"
HEALTH_BAR_310_TEXTURE = "Textures/Health_Bars/HealthBar_10.3.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.3_Scaled.gif"
HEALTH_BAR_210_TEXTURE = "Textures/Health_Bars/HealthBar_10.2.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.2_Scaled.gif"
HEALTH_BAR_110_TEXTURE = "Textures/Health_Bars/HealthBar_10.1.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_10.1_Scaled.gif"
HEALTH_BAR_33_TEXTURE = "Textures/Health_Bars/HealthBar_3.3.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_3.3_Scaled.gif"
HEALTH_BAR_23_TEXTURE = "Textures/Health_Bars/HealthBar_3.2.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_3.2_Scaled.gif"
HEALTH_BAR_13_TEXTURE = "Textures/Health_Bars/HealthBar_3.1.gif" if fullscreen == 0 else "Textures/Health_Bars/HealthBar_3.1_Scaled.gif"
EXPLOSION_1_TEXTURE = "Textures/Explosions/Explosion1.gif" if fullscreen == 0 else "Textures/Explosions/Explosion1_Scaled.gif"
EXPLOSION_2_TEXTURE = "Textures/Explosions/Explosion2.gif" if fullscreen == 0 else "Textures/Explosions/Explosion2_Scaled.gif"
GROUND_TEXTURE = "Textures/Ground/Ground.gif" if fullscreen == 0 else "Textures/Ground/Ground_Scaled.gif"
SUN_TEXTURE = "Textures/Background/Sun.gif" if fullscreen == 0 else "Textures/Background/Sun_Scaled.gif"
EARTH_TEXTURE = "Textures/Background/Earth.gif" if fullscreen == 0 else "Textures/Background/Earth_Scaled.gif"
SPACE_SHIP_TEXTURE = "Textures/Background/Space_Ship.gif" if fullscreen == 0 else "Textures/Background/Space_Ship_Scaled.gif"
HUMAN_STILL_RIGHT_TEXTURE = "Textures/Player/Player_Head_Still_Right.gif" if fullscreen == 0 else "Textures/Player/Player_Head_Still_Right_Scaled.gif"
HUMAN_STILL_LEFT_TEXTURE = "Textures/Player/Player_Head_Still_Left.gif" if fullscreen == 0 else "Textures/Player/Player_Head_Still_Left_Scaled.gif"
HUMAN_WALKING_RIGHT_TEXTURE = "Textures/Player/Player_Head_Walking_Right.gif" if fullscreen == 0 else "Textures/Player/Player_Head_Walking_Right_Scaled.gif"
HUMAN_WALKING_LEFT_TEXTURE = "Textures/Player/Player_Head_Walking_Left.gif" if fullscreen == 0 else "Textures/Player/Player_Head_Walking_Left_Scaled.gif"
PLAYER_HEAD_LASER_TEXTURE = "Textures/Lasers/Player_Head_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Player_Head_Laser_Scaled.gif"
THE_COOKER_LASER_TEXTURE = "Textures/Lasers/The_Cooker_Laser.gif" if fullscreen == 0 else "Textures/Lasers/The_Cooker_Laser_Scaled.gif"
POISON_DART_LASER_TEXTURE = "Textures/Lasers/Poison_Dart_Laser.gif" if fullscreen == 0 else "Textures/Lasers/Poison_Dart_Laser_Scaled.gif"
METEOR_GUN_LASER_RIGHT_TEXTURE = "Textures/Lasers/Meteor_Gun_Laser_Right.gif" if fullscreen == 0 else "Textures/Lasers/Meteor_Gun_Laser_Right_Scaled.gif"
METEOR_GUN_LASER_LEFT_TEXTURE = "Textures/Lasers/Meteor_Gun_Laser_Left.gif" if fullscreen == 0 else "Textures/Lasers/Meteor_Gun_Laser_Left_Scaled.gif"
SUPERNOVA_LASER_RIGHT_TEXTURE = "Textures/Lasers/The_Supernova_Laser_Right.gif" if fullscreen == 0 else "Textures/Lasers/The_Supernova_Laser_Right_Scaled.gif"
SUPERNOVA_LASER_LEFT_TEXTURE = "Textures/Lasers/The_Supernova_Laser_Left.gif" if fullscreen == 0 else "Textures/Lasers/The_Supernova_Laser_Left_Scaled.gif"
PLAYER_GUN_RIGHT_TEXTURE = "Textures/Gun/Player_Gun_Right.gif" if fullscreen == 0 else "Textures/Gun/Player_Gun_Right_Scaled.gif"
PLAYER_GUN_LEFT_TEXTURE = "Textures/Gun/Player_Gun_Left.gif" if fullscreen == 0 else "Textures/Gun/Player_Gun_Left_Scaled.gif"
THE_COOKER_RIGHT_TEXTURE = "Textures/Gun/The_Cooker_Right.gif" if fullscreen == 0 else "Textures/Gun/The_Cooker_Right_Scaled.gif"
THE_COOKER_LEFT_TEXTURE = "Textures/Gun/The_Cooker_Left.gif" if fullscreen == 0 else "Textures/Gun/The_Cooker_Left_Scaled.gif"
POISON_DART_GUN_RIGHT_TEXTURE = "Textures/Gun/Poison_Dart_Gun_Right.gif" if fullscreen == 0 else "Textures/Gun/Poison_Dart_Gun_Right_Scaled.gif"
POISON_DART_GUN_LEFT_TEXTURE = "Textures/Gun/Poison_Dart_Gun_Left.gif" if fullscreen == 0 else "Textures/Gun/Poison_Dart_Gun_Left_Scaled.gif"
METEOR_GUN_RIGHT_TEXTURE = "Textures/Gun/Meteor_Gun_Right.gif" if fullscreen == 0 else "Textures/Gun/Meteor_Gun_Right_Scaled.gif"
METEOR_GUN_LEFT_TEXTURE = "Textures/Gun/Meteor_Gun_Left.gif" if fullscreen == 0 else "Textures/Gun/Meteor_Gun_Left_Scaled.gif"
SUPERNOVA_RIGHT_TEXTURE = "Textures/Gun/Supernova_Right.gif" if fullscreen == 0 else "Textures/Gun/Supernova_Right_Scaled.gif"
SUPERNOVA_LEFT_TEXTURE = "Textures/Gun/Supernova_Left.gif" if fullscreen == 0 else "Textures/Gun/Supernova_Left_Scaled.gif"
OXYGEN_TANK_TEXTURE = "Textures/Other/Oxygen_Tank.gif" if fullscreen == 0 else "Textures/Other/Oxygen_Tank_Scaled.gif"
ALIEN_STILL_LEFT_1_5_TEXTURE = "Textures/Aliens/Alien_Still_Left(1-5).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Left(1-5)_Scaled.gif"
ALIEN_STILL_RIGHT_1_5_TEXTURE = "Textures/Aliens/Alien_Still_Right(1-5).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Right(1-5)_Scaled.gif"
ALIEN_WALKING_LEFT_1_5_TEXTURE = "Textures/Aliens/Alien_Walking_Left(1-5).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Left(1-5)_Scaled.gif"
ALIEN_WALKING_RIGHT_1_5_TEXTURE = "Textures/Aliens/Alien_Walking_Right(1-5).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Right(1-5)_Scaled.gif"
ALIEN_STILL_LEFT_6_10_TEXTURE = "Textures/Aliens/Alien_Still_Left(6-10).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Left(6-10)_Scaled.gif"
ALIEN_STILL_RIGHT_6_10_TEXTURE = "Textures/Aliens/Alien_Still_Right(6-10).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Right(6-10)_Scaled.gif"
ALIEN_WALKING_LEFT_6_10_TEXTURE = "Textures/Aliens/Alien_Walking_Left(6-10).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Left(6-10)_Scaled.gif"
ALIEN_WALKING_RIGHT_6_10_TEXTURE = "Textures/Aliens/Alien_Walking_Right(6-10).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Right(6-10)_Scaled.gif"
ALIEN_STILL_LEFT_11_15_TEXTURE = "Textures/Aliens/Alien_Still_Left(11-15).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Left(11-15)_Scaled.gif"
ALIEN_STILL_RIGHT_11_15_TEXTURE = "Textures/Aliens/Alien_Still_Right(11-15).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Still_Right(11-15)_Scaled.gif"
ALIEN_WALKING_LEFT_11_15_TEXTURE = "Textures/Aliens/Alien_Walking_Left(11-15).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Left(11-15)_Scaled.gif"
ALIEN_WALKING_RIGHT_11_15_TEXTURE = "Textures/Aliens/Alien_Walking_Right(11-15).gif" if fullscreen == 0 else "Textures/Aliens/Alien_Walking_Right(11-15)_Scaled.gif"
ALIEN_BOSS_TEXTURE = "Textures/Aliens/Alien_Boss.gif" if fullscreen == 0 else "Textures/Aliens/Alien_Boss_Scaled.gif"
ALIEN_DEATH_1_TEXTURE = "Textures/Explosions/Alien_Death_1.gif" if fullscreen == 0 else "Textures/Explosions/Alien_Death_1_Scaled.gif"
ALIEN_DEATH_2_TEXTURE = "Textures/Explosions/Alien_Death_2.gif" if fullscreen == 0 else "Textures/Explosions/Alien_Death_2_Scaled.gif"
PLAYER_DEATH_1_TEXTURE = "Textures/Explosions/Player_Death_1.gif" if fullscreen == 0 else "Textures/Explosions/Player_Death_1_Scaled.gif"
PLAYER_DEATH_2_TEXTURE = "Textures/Explosions/Player_Death_2.gif" if fullscreen == 0 else "Textures/Explosions/Player_Death_2_Scaled.gif"
SOUND_BUTTON_TEXTURE = "Textures/Buttons/Sound_Button.gif" if fullscreen == 0 else "Textures/Buttons/Sound_Button_Scaled.gif"
CONTROL_BUTTON_TEXTURE = "Textures/Buttons/Control_Button.gif" if fullscreen == 0 else "Textures/Buttons/Control_Button_Scaled.gif"
SETTINGS_MAIN_MENU_BUTTON_TEXTURE = "Textures/Buttons/Settings_Main_Menu_Button.gif" if fullscreen == 0 else "Textures/Buttons/Settings_Main_Menu_Button_Scaled.gif"
MAIN_MENU_BUTTON_MAIN_TEXTURE = "Textures/Buttons/Main_Menu_Button_Main.gif" if fullscreen == 0 else "Textures/Buttons/Main_Menu_Button_Main_Scaled.gif"
TITLE_SCREEN_BUTTON_TEXTURE = "Textures/Buttons/Title_Screen_Button.gif" if fullscreen == 0 else "Textures/Buttons/Title_Screen_Button_Scaled.gif"
TITLE_SCREEN_BUTTON_SMALL_TEXTURE = "Textures/Buttons/Title_Screen_Button_Small.gif" if fullscreen == 0 else "Textures/Buttons/Title_Screen_Button_Small_Scaled.gif"
MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Main_Menu_Button_Main_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Main_Menu_Button_Main_Highlighted_Scaled.gif"
TITLE_SCREEN_BUTTON_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Title_Screen_Button_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Title_Screen_Button_Highlighted_Scaled.gif"
TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Title_Screen_Button_Small_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Title_Screen_Button_Small_Highlighted_Scaled.gif"
BUY_BUTTON_TEXTURE = "Textures/Buttons/Buy_Button.gif" if fullscreen == 0 else "Textures/Buttons/Buy_Button_Scaled.gif"
BUY_BUTTON_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Buy_Button_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Buy_Button_Highlighted_Scaled.gif"
INVENTORY_SLOT_FRAME_TEXTURE = "Textures/Buttons/Inventory_Slot_Frame.gif" if fullscreen == 0 else "Textures/Buttons/Inventory_Slot_Frame_Scaled.gif"
INVENTORY_SLOT_FRAME_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Inventory_Slot_Frame_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Inventory_Slot_Frame_Highlighted_Scaled.gif"
TAB_TEXTURE = "Textures/Buttons/Tab.gif" if fullscreen == 0 else "Textures/Buttons/Tab_Scaled.gif"
TAB_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Tab_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Tab_Highlighted_Scaled.gif"
SIDE_PANEL_SHOP_TEXTURE = "Textures/GUI/Side_Panel_Shop.gif" if fullscreen == 0 else "Textures/GUI/Side_Panel_Shop_Scaled.gif"
LOCKED_TEXTURE = "Textures/GUI/Locked.gif" if fullscreen == 0 else "Textures/GUI/Locked_Scaled.gif"
TAB_SELECTOR_TEXTURE = "Textures/GUI/Tab_Selector.gif" if fullscreen == 0 else "Textures/GUI/Tab_Selector_Scaled.gif"
SLOT_SELECTOR_TEXTURE = "Textures/GUI/Slot_Selector.gif" if fullscreen == 0 else "Textures/GUI/Slot_Selector_Scaled.gif"
SETTINGS_AND_CONTROLS_BUTTON_TEXTURE = "Textures/Buttons/Settings_And_Controls_Button.gif" if fullscreen == 0 else "Textures/Buttons/Settings_And_Controls_Button_Scaled.gif"
SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED_TEXTURE = "Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif" if fullscreen == 0 else "Textures/Buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif"
MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Machine_Default_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Machine_Default_Display_Icon_Scaled.gif"
ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Alien_Default_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Alien_Default_Display_Icon_Scaled.gif"
YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Yellow_Power_Up_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Yellow_Power_Up_Display_Icon_Scaled.gif"
BLUE_POWER_UP_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Blue_Power_Up_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Blue_Power_Up_Display_Icon_Scaled.gif"
GREEN_POWER_UP_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Green_Power_Up_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Green_Power_Up_Display_Icon_Scaled.gif"
RED_POWER_UP_DISPLAY_ICON_TEXTURE = "Textures/Interface/Display/Red_Power_Up_Display_Icon.gif" if fullscreen == 0 else "Textures/Interface/Display/Red_Power_Up_Display_Icon_Scaled.gif"
MACHINE_MODE_TAB_ICON_TEXTURE = "Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon_Scaled.gif"
MACHINE_DEFAULT_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon_Scaled.gif"
ALIEN_DEFAULT_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon_Scaled.gif"
YELLOW_POWER_UP_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon_Scaled.gif"
RED_POWER_UP_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon_Scaled.gif"
GREEN_POWER_UP_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon_Scaled.gif"
BLUE_POWER_UP_SLOT_ICON_TEXTURE = "Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon_Scaled.gif"
YELLOW_LIGHTNING_POWER_UP_TEXTURE = "Textures/Power_Ups/Yellow_Lightning_Power_Up.gif" if fullscreen == 0 else "Textures/Power_Ups/Yellow_Lightning_Power_Up_Scaled.gif"
GREEN_LIGHTNING_POWER_UP_TEXTURE = "Textures/Power_Ups/Green_Lightning_Power_Up.gif" if fullscreen == 0 else "Textures/Power_Ups/Green_Lightning_Power_Up_Scaled.gif"
RED_LIGHTNING_POWER_UP_TEXTURE = "Textures/Power_Ups/Red_Lightning_Power_Up.gif" if fullscreen == 0 else "Textures/Power_Ups/Red_Lightning_Power_Up_Scaled.gif"
BLUE_LIGHTNING_POWER_UP_TEXTURE = "Textures/Power_Ups/Blue_Lightning_Power_Up.gif" if fullscreen == 0 else "Textures/Power_Ups/Blue_Lightning_Power_Up_Scaled.gif"
BLUE_POWER_UP_INDICATOR_ON_TEXTURE = "Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif" if fullscreen == 0 else "Textures/Power_Ups/Blue_Power_Up_Indicator_On_Scaled.gif"
GREEN_POWER_UP_INDICATOR_ON_TEXTURE = "Textures/Power_Ups/Green_Power_Up_Indicator_On.gif" if fullscreen == 0 else "Textures/Power_Ups/Green_Power_Up_Indicator_On_Scaled.gif"
YELLOW_POWER_UP_INDICATOR_ON_TEXTURE = "Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif" if fullscreen == 0 else "Textures/Power_Ups/Yellow_Power_Up_Indicator_On_Scaled.gif"
RED_POWER_UP_INDICATOR_ON_TEXTURE = "Textures/Power_Ups/Red_Power_Up_Indicator_On.gif" if fullscreen == 0 else "Textures/Power_Ups/Red_Power_Up_Indicator_On_Scaled.gif"
BLUE_POWER_UP_INDICATOR_OFF_TEXTURE = "Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "Textures/Power_Ups/Blue_Power_Up_Indicator_Off_Scaled.gif"
GREEN_POWER_UP_INDICATOR_OFF_TEXTURE = "Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "Textures/Power_Ups/Green_Power_Up_Indicator_Off_Scaled.gif"
YELLOW_POWER_UP_INDICATOR_OFF_TEXTURE = "Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "Textures/Power_Ups/Yellow_Power_Up_Indicator_Off_Scaled.gif"
RED_POWER_UP_INDICATOR_OFF_TEXTURE = "Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "Textures/Power_Ups/Red_Power_Up_Indicator_Off_Scaled.gif"
COPPER_COIN_TEXTURE = "Textures/Coins/Copper_Coin.gif" if fullscreen == 0 else "Textures/Coins/Copper_Coin_Scaled.gif"
SILVER_COIN_TEXTURE = "Textures/Coins/Silver_Coin.gif" if fullscreen == 0 else "Textures/Coins/Silver_Coin_Scaled.gif"
GOLD_COIN_TEXTURE = "Textures/Coins/Gold_Coin.gif" if fullscreen == 0 else "Textures/Coins/Gold_Coin_Scaled.gif"
PLATINUM_COIN_TEXTURE = "Textures/Coins/Platinum_Coin.gif" if fullscreen == 0 else "Textures/Coins/Platinum_Coin_Scaled.gif"
COIN_INDICATOR_TEXTURE = "Textures/Coins/Coin_Indicator.gif" if fullscreen == 0 else "Textures/Coins/Coin_Indicator_Scaled.gif"
