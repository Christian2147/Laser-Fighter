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

# This file sets up the application window and initializes all necessary processes

"""
    File: WindowSetup.py
    Author: Christian Marinkovich
    Date: 2024-07-06
    Description:
    This file contains the script to initialize the screen and start the game.
    First, a window is created a deployed. After that, all the textures are loaded into the game. The FPS is also
    set up here.
    If fullscreen is toggled, all the textures are scaled.
"""

import turtle
import tkinter
import win32api
import win32con
import os
import pygame
from PIL import Image
from fractions import Fraction
from setup.ConfigurationSetup import settings

# Scale Factors for fullscreen (1 when fullscreen is off)
# All raw coordinates, distances, and movements are multiplied by the scale factor to ensure that the game stays scaled
#   in fullscreen mode.
scale_factor = 1
scale_factor_X = 1
scale_factor_Y = 1

# Create Screen Object with "Laser Fighter" as the title
window = turtle.Screen()
window.title("Laser Fighter")
window.bgcolor("black")
if settings.fullscreen == 1:
    # Set the width and height to be the monitors width and height
    # The monitors width and height is retrieved from the windows API
    window.setup(width=win32api.GetSystemMetrics(0), height=win32api.GetSystemMetrics(1))
    window.cv._rootwindow.attributes("-fullscreen", True)

    # Calculating the scale factor:
    # Extract the screen width and height again
    current_screen_width = win32api.GetSystemMetrics(0)
    current_screen_height = win32api.GetSystemMetrics(1)
    # The main scale factor is based off the smallest of the two lengths
    if current_screen_height < current_screen_width:
        scale_factor = current_screen_height/720
    else:
        scale_factor = current_screen_width/1280
    # To find the scale factor (by what number must we scale all values and distances),
    # we find the ratio of the current screen width/height over the default screen width/height
    scale_factor_X = current_screen_width/1280
    scale_factor_Y = current_screen_height/720

    # What if the aspect ratio is lower than 16/9?
    # With the code above, that would cause the text to go off the screen, we need to take the width of th screen
    #   and manually find its height if it had a 16/9 aspect ratio. Then, we use that in our calculations.
    # Finding aspect ratio:
    aspect_ratio = Fraction(current_screen_width, current_screen_height)
    target_aspect_ratio = Fraction(16, 9)
    # Check if the ratio is the target ratio or not (16/9)
    if aspect_ratio != target_aspect_ratio:
        # If not, find the custom height to work with
        decimal_aspect_ratio = current_screen_width/current_screen_height
        decimal_aspect_ratio = 1/decimal_aspect_ratio
        if decimal_aspect_ratio > 0.5625:
            # Find the new scale factor based off of that height
            new_screen_height = current_screen_width * 9/16
            scale_factor = new_screen_height/720

    # Scale the background
    image = Image.open("textures/background/Shooting_Game_Background.gif")
    # Find the new width and height based on the scale factor
    new_width = int(image.width * scale_factor_X)
    new_height = int(image.height * scale_factor_Y)
    # Save the background and add "_Scaled" to its name in the files
    resized_image = image.resize((new_width, new_height))
    resized_image.save("textures/background/Shooting_Game_Background_Scaled.gif")
    window.bgpic("textures/background/Shooting_Game_Background_Scaled.gif")
else:
    # Default screen is created if fullscreen is not on
    window.bgpic("textures/background/Shooting_Game_Background.gif")
    window.setup(width=1280, height=720)

# Get rid of the gray border around the edge of the canvas
window.cv.config(highlightthickness=0)
# Make the window not resizable (Will hopefully change later)
window.cv._rootwindow.resizable(False, False)
# Set the window icon
img = tkinter.Image("photo", file="icon/Icon.png")
window._root.iconphoto(True, img)
tk_window = window.getcanvas().winfo_toplevel()
if os.name == 'nt':
    tk_window.iconbitmap('icon/Icon.ico')
elif os.name == 'posix':
    tk_window.iconbitmap('icon/Icon.png')
window.tracer(0)

# List of paths to all textures that need to be loaded
texture_paths = [
    "textures/player/Player.gif",
    "textures/player/Machine_Washer.gif",
    "textures/player/The_Incinerator.gif",
    "textures/player/The_Black_Hole.gif",
    "textures/player/The_Star_Killer.gif",
    "textures/lasers/Player_Laser.gif",
    "textures/lasers/Machine_Washer_Laser.gif",
    "textures/lasers/Incinerator_Laser.gif",
    "textures/lasers/The_Black_Hole_Laser.gif",
    "textures/lasers/The_Star_Killer_Laser.gif",
    "textures/machines/Enemy(1-5).gif",
    "textures/lasers/Enemy(1-5)_Laser.gif",
    "textures/machines/Enemy(6-10).gif",
    "textures/lasers/Enemy(6-10)_Laser.gif",
    "textures/machines/Enemy(11-15).gif",
    "textures/lasers/Enemy(11-15)_Laser.gif",
    "textures/machines/Boss.gif",
    "textures/lasers/Boss_Laser.gif",
    "textures/healthbars/HealthBar_2.2.gif",
    "textures/healthbars/HealthBar_2.1.gif",
    "textures/healthbars/HealthBar_10.10.gif",
    "textures/healthbars/HealthBar_10.9.gif",
    "textures/healthbars/HealthBar_10.8.gif",
    "textures/healthbars/HealthBar_10.7.gif",
    "textures/healthbars/HealthBar_10.6.gif",
    "textures/healthbars/HealthBar_10.5.gif",
    "textures/healthbars/HealthBar_10.4.gif",
    "textures/healthbars/HealthBar_10.3.gif",
    "textures/healthbars/HealthBar_10.2.gif",
    "textures/healthbars/HealthBar_10.1.gif",
    "textures/healthbars/HealthBar_3.3.gif",
    "textures/healthbars/HealthBar_3.2.gif",
    "textures/healthbars/HealthBar_3.1.gif",
    "textures/armor/ArmorBar_10.10.gif",
    "textures/armor/ArmorBar_10.9.gif",
    "textures/armor/ArmorBar_10.8.gif",
    "textures/armor/ArmorBar_10.7.gif",
    "textures/armor/ArmorBar_10.6.gif",
    "textures/armor/ArmorBar_10.5.gif",
    "textures/armor/ArmorBar_10.4.gif",
    "textures/armor/ArmorBar_10.3.gif",
    "textures/armor/ArmorBar_10.2.gif",
    "textures/armor/ArmorBar_10.1.gif",
    "textures/explosions/Explosion1.gif",
    "textures/explosions/Explosion2.gif",
    "textures/ground/Ground.gif",
    "textures/background/Sun.gif",
    "textures/background/Earth.gif",
    "textures/background/Space_Ship.gif",
    "textures/player/Player_Head_Still_Right.gif",
    "textures/player/Player_Head_Still_Left.gif",
    "textures/player/Player_Head_Walking_Right.gif",
    "textures/player/Player_Head_Walking_Left.gif",
    "textures/lasers/Player_Head_Laser.gif",
    "textures/lasers/The_Cooker_Laser.gif",
    "textures/lasers/Poison_Dart_Laser.gif",
    "textures/lasers/Meteor_Gun_Laser_Right.gif",
    "textures/lasers/Meteor_Gun_Laser_Left.gif",
    "textures/lasers/The_Supernova_Laser_Right.gif",
    "textures/lasers/The_Supernova_Laser_Left.gif",
    "textures/gun/Player_Gun_Right.gif",
    "textures/gun/Player_Gun_Left.gif",
    "textures/gun/The_Cooker_Right.gif",
    "textures/gun/The_Cooker_Left.gif",
    "textures/gun/Poison_Dart_Gun_Right.gif",
    "textures/gun/Poison_Dart_Gun_Left.gif",
    "textures/gun/Meteor_Gun_Right.gif",
    "textures/gun/Meteor_Gun_Left.gif",
    "textures/gun/Supernova_Right.gif",
    "textures/gun/Supernova_Left.gif",
    "textures/other/Oxygen_Tank.gif",
    "textures/aliens/Alien_Still_Left(1-5).gif",
    "textures/aliens/Alien_Still_Right(1-5).gif",
    "textures/aliens/Alien_Walking_Left(1-5).gif",
    "textures/aliens/Alien_Walking_Right(1-5).gif",
    "textures/aliens/Alien_Still_Left(6-10).gif",
    "textures/aliens/Alien_Still_Right(6-10).gif",
    "textures/aliens/Alien_Walking_Left(6-10).gif",
    "textures/aliens/Alien_Walking_Right(6-10).gif",
    "textures/aliens/Alien_Still_Left(11-15).gif",
    "textures/aliens/Alien_Still_Right(11-15).gif",
    "textures/aliens/Alien_Walking_Left(11-15).gif",
    "textures/aliens/Alien_Walking_Right(11-15).gif",
    "textures/aliens/Alien_Boss.gif",
    "textures/explosions/Alien_Death_1.gif",
    "textures/explosions/Alien_Death_2.gif",
    "textures/explosions/Player_Death_1.gif",
    "textures/explosions/Player_Death_2.gif",
    "textures/buttons/Sound_Button.gif",
    "textures/buttons/Control_Button.gif",
    "textures/buttons/Settings_Main_Menu_Button.gif",
    "textures/buttons/Main_Menu_Button_Main.gif",
    "textures/buttons/Title_Screen_Button.gif",
    "textures/buttons/Title_Screen_Button_Small.gif",
    "textures/buttons/Main_Menu_Button_Main_Highlighted.gif",
    "textures/buttons/Title_Screen_Button_Highlighted.gif",
    "textures/buttons/Title_Screen_Button_Small_Highlighted.gif",
    "textures/buttons/Buy_Button.gif",
    "textures/buttons/Buy_Button_Highlighted.gif",
    "textures/buttons/Inventory_Slot_Frame.gif",
    "textures/buttons/Inventory_Slot_Frame_Highlighted.gif",
    "textures/buttons/Tab.gif",
    "textures/buttons/Tab_Highlighted.gif",
    "textures/gui/Side_Panel_Shop.gif",
    "textures/gui/Pop_Up_Message_Frame.gif",
    "textures/gui/Locked.gif",
    "textures/gui/Tab_Selector.gif",
    "textures/gui/Slot_Selector.gif",
    "textures/buttons/Settings_And_Controls_Button.gif",
    "textures/buttons/Settings_And_Controls_Button_Highlighted.gif",
    "textures/interface/display/Machine_Default_Display_Icon.gif",
    "textures/interface/display/Machine_Washer_Display_Icon.gif",
    "textures/interface/display/The_Incinerator_Display_Icon.gif",
    "textures/interface/display/The_Black_Hole_Display_Icon.gif",
    "textures/interface/display/The_Star_Killer_Display_Icon.gif",
    "textures/interface/display/Alien_Default_Display_Icon.gif",
    "textures/interface/display/The_Cooker_Display_Icon.gif",
    "textures/interface/display/Poison_Dart_Display_Icon.gif",
    "textures/interface/display/Meteor_Gun_Display_Icon.gif",
    "textures/interface/display/Supernova_Display_Icon.gif",
    "textures/interface/display/Yellow_Power_Up_Display_Icon.gif",
    "textures/interface/display/Blue_Power_Up_Display_Icon.gif",
    "textures/interface/display/Green_Power_Up_Display_Icon.gif",
    "textures/interface/display/Red_Power_Up_Display_Icon.gif",
    "textures/interface/display/Coin_Magnet_Display_Icon.gif",
    "textures/interface/display/Armor_Display_Icon.gif",
    "textures/interface/display/Thorns_Display_Icon.gif",
    "textures/interface/display/Heart_Power_Up_Display_Icon.gif",
    "textures/interface/icons/tab/Machine_Mode_Tab_Icon.gif",
    "textures/interface/icons/tab/Gadgets_Tab_Icon.gif",
    "textures/interface/icons/slot/Machine_Default_Slot_Icon.gif",
    "textures/interface/icons/slot/Machine_Washer_Slot_Icon.gif",
    "textures/interface/icons/slot/The_Incinerator_Slot_Icon.gif",
    "textures/interface/icons/slot/The_Black_Hole_Slot_Icon.gif",
    "textures/interface/icons/slot/The_Star_Killer_Slot_Icon.gif",
    "textures/interface/icons/slot/Alien_Default_Slot_Icon.gif",
    "textures/interface/icons/slot/The_Cooker_Slot_Icon.gif",
    "textures/interface/icons/slot/Poison_Dart_Slot_Icon.gif",
    "textures/interface/icons/slot/Meteor_Gun_Slot_Icon.gif",
    "textures/interface/icons/slot/Supernova_Slot_Icon.gif",
    "textures/interface/icons/slot/Yellow_Power_Up_Slot_Icon.gif",
    "textures/interface/icons/slot/Red_Power_Up_Slot_Icon.gif",
    "textures/interface/icons/slot/Green_Power_Up_Slot_Icon.gif",
    "textures/interface/icons/slot/Blue_Power_Up_Slot_Icon.gif",
    "textures/interface/icons/slot/Coin_Magnet_Slot_Icon.gif",
    "textures/interface/icons/slot/Armor_Slot_Icon.gif",
    "textures/interface/icons/slot/Thorns_Slot_Icon.gif",
    "textures/interface/icons/slot/Heart_Power_Up_Slot_Icon.gif",
    "textures/powerups/Yellow_Lightning_Power_Up.gif",
    "textures/powerups/Green_Lightning_Power_Up.gif",
    "textures/powerups/Red_Lightning_Power_Up.gif",
    "textures/powerups/Blue_Lightning_Power_Up.gif",
    "textures/powerups/Heart_Power_Up.gif",
    "textures/powerups/Blue_Power_Up_Indicator_On.gif",
    "textures/powerups/Green_Power_Up_Indicator_On.gif",
    "textures/powerups/Yellow_Power_Up_Indicator_On.gif",
    "textures/powerups/Red_Power_Up_Indicator_On.gif",
    "textures/powerups/Blue_Power_Up_Indicator_Off.gif",
    "textures/powerups/Green_Power_Up_Indicator_Off.gif",
    "textures/powerups/Yellow_Power_Up_Indicator_Off.gif",
    "textures/powerups/Red_Power_Up_Indicator_Off.gif",
    "textures/coins/Copper_Coin.gif",
    "textures/coins/Silver_Coin.gif",
    "textures/coins/Gold_Coin.gif",
    "textures/coins/Platinum_Coin.gif",
    "textures/coins/Coin_Indicator.gif"
]

# Import the textures to the game
if settings.fullscreen == 1:
    # If fullscreen is on, scale the textures the same way that the background was scaled
    for texture in texture_paths:
        # All textures are rescaled here
        image = Image.open(texture)
        new_width = int(image.width * scale_factor_X)
        new_height = int(image.height * scale_factor_Y)
        resized_image = image.resize((new_width, new_height))
        base, ext = os.path.splitext(texture)
        # If fullscreen is on, the textures with "_Scaled" at the end of their name are implemented
        new_path = f"{base}_Scaled{ext}"
        resized_image.save(new_path)
        window.addshape(new_path)
else:
    # If fullscreen is off, textures are imported with names as is
    for texture in texture_paths:
        window.addshape(texture)

# Initialize PyGame and PyGame Sound Engine (Performance improvements and better sound)
pygame.init()
pygame.mixer.init()

# Extract the refresh rate of the users monitor through the windows API
DISPLAY_DEVICE = win32api.EnumDisplayDevices(None, 0)
SETTINGS = win32api.EnumDisplaySettings(DISPLAY_DEVICE.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
REFRESH_RATE = SETTINGS.DisplayFrequency

# Set the target FPS to the refresh rate for VSync, otherwise the FPS is not used since "unlimited" would be allowed
# Unlimited FPS means that the game loop executes as fast as possible
CLOCK = pygame.time.Clock()
TARGET_FPS = REFRESH_RATE
MONITOR_DELAY = 1.0/TARGET_FPS
