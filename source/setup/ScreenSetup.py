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
    File: ScreenSetup.py
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
from setup.Initialization import fullscreen

# Scale Factors for fullscreen (1 when fullscreen is off)
# All raw coordinates, distances, and movements are multiplied by the scale factor to ensure that the game stays scaled
#   in fullscreen mode.
scale_factor = 1
scale_factor_X = 1
scale_factor_Y = 1

# Create Screen Object with "Laser Fighter" as the title
wn = turtle.Screen()
wn.title("Laser Fighter")
wn.bgcolor("black")
if fullscreen == 1:
    # Set the width and height to be the monitors width and height
    # The monitors width and height is retrieved from the windows API
    wn.setup(width=win32api.GetSystemMetrics(0), height=win32api.GetSystemMetrics(1))
    wn.cv._rootwindow.attributes("-fullscreen", True)

    # Calculating the scale factor:
    # Extract the screen width and height agian
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
    image = Image.open("Textures/Background/Shooting_Game_Background.gif")
    # Find the new width and height based on the scale factor
    new_width = int(image.width * scale_factor_X)
    new_height = int(image.height * scale_factor_Y)
    # Save the background and add "_Scaled" to its name in the files
    resized_image = image.resize((new_width, new_height))
    resized_image.save("Textures/Background/Shooting_Game_Background_Scaled.gif")
    wn.bgpic("Textures/Background/Shooting_Game_Background_Scaled.gif")
else:
    # Default screen is created if fullscreen is not on
    wn.bgpic("Textures/Background/Shooting_Game_Background.gif")
    wn.setup(width=1280, height=720)

# Get rid of the gray border around the edge of the canvas
wn.cv.config(highlightthickness=0)
#wn.cv.config(borderwidth=0)
# Make the window not resizable (Will hopefully change later)
wn.cv._rootwindow.resizable(False, False)
# Set the window icon
img = tkinter.Image("photo", file="Icon/Icon.png")
wn._root.iconphoto(True, img)
tk_window = wn.getcanvas().winfo_toplevel()
tk_window.iconbitmap('Icon/Icon.ico')
wn.tracer(0)

# List of paths to all textures that need to be loaded
texture_paths = [
    "Textures/Player/Player.gif",
    "Textures/Lasers/Player_Laser.gif",
    "Textures/Lasers/Machine_Washer_Laser.gif",
    "Textures/Lasers/Incinerator_Laser.gif",
    "Textures/Enemies/Enemy(1-5).gif",
    "Textures/Lasers/Enemy(1-5)_Laser.gif",
    "Textures/Enemies/Enemy(6-10).gif",
    "Textures/Lasers/Enemy(6-10)_Laser.gif",
    "Textures/Enemies/Enemy(11-15).gif",
    "Textures/Lasers/Enemy(11-15)_Laser.gif",
    "Textures/Enemies/Boss.gif",
    "Textures/Lasers/Boss_Laser.gif",
    "Textures/Health_Bars/HealthBar_2.2.gif",
    "Textures/Health_Bars/HealthBar_2.1.gif",
    "Textures/Health_Bars/HealthBar_10.10.gif",
    "Textures/Health_Bars/HealthBar_10.9.gif",
    "Textures/Health_Bars/HealthBar_10.8.gif",
    "Textures/Health_Bars/HealthBar_10.7.gif",
    "Textures/Health_Bars/HealthBar_10.6.gif",
    "Textures/Health_Bars/HealthBar_10.5.gif",
    "Textures/Health_Bars/HealthBar_10.4.gif",
    "Textures/Health_Bars/HealthBar_10.3.gif",
    "Textures/Health_Bars/HealthBar_10.2.gif",
    "Textures/Health_Bars/HealthBar_10.1.gif",
    "Textures/Health_Bars/HealthBar_3.3.gif",
    "Textures/Health_Bars/HealthBar_3.2.gif",
    "Textures/Health_Bars/HealthBar_3.1.gif",
    "Textures/Explosions/Explosion1.gif",
    "Textures/Explosions/Explosion2.gif",
    "Textures/Ground/Ground.gif",
    "Textures/Background/Sun.gif",
    "Textures/Background/Earth.gif",
    "Textures/Background/Space_Ship.gif",
    "Textures/Player/Player_Head_Still_Right.gif",
    "Textures/Player/Player_Head_Still_Left.gif",
    "Textures/Player/Player_Head_Walking_Right.gif",
    "Textures/Player/Player_Head_Walking_Left.gif",
    "Textures/Lasers/Player_Head_Laser.gif",
    "Textures/Lasers/Meteor_Gun_Laser_Right.gif",
    "Textures/Lasers/Meteor_Gun_Laser_Left.gif",
    "Textures/Lasers/The_Supernova_Laser_Right.gif",
    "Textures/Lasers/The_Supernova_Laser_Left.gif",
    "Textures/Gun/Player_Gun_Right.gif",
    "Textures/Gun/Player_Gun_Left.gif",
    "Textures/Other/Oxygen_Tank.gif",
    "Textures/Aliens/Alien_Still_Left(1-5).gif",
    "Textures/Aliens/Alien_Still_Right(1-5).gif",
    "Textures/Aliens/Alien_Walking_Left(1-5).gif",
    "Textures/Aliens/Alien_Walking_Right(1-5).gif",
    "Textures/Aliens/Alien_Still_Left(6-10).gif",
    "Textures/Aliens/Alien_Still_Right(6-10).gif",
    "Textures/Aliens/Alien_Walking_Left(6-10).gif",
    "Textures/Aliens/Alien_Walking_Right(6-10).gif",
    "Textures/Aliens/Alien_Still_Left(11-15).gif",
    "Textures/Aliens/Alien_Still_Right(11-15).gif",
    "Textures/Aliens/Alien_Walking_Left(11-15).gif",
    "Textures/Aliens/Alien_Walking_Right(11-15).gif",
    "Textures/Aliens/Alien_Boss.gif",
    "Textures/Explosions/Alien_Death_1.gif",
    "Textures/Explosions/Alien_Death_2.gif",
    "Textures/Explosions/Player_Death_1.gif",
    "Textures/Explosions/Player_Death_2.gif",
    "Textures/Buttons/Sound_Button.gif",
    "Textures/Buttons/Control_Button.gif",
    "Textures/Buttons/Settings_Main_Menu_Button.gif",
    "Textures/Buttons/Main_Menu_Button_Main.gif",
    "Textures/Buttons/Title_Screen_Button.gif",
    "Textures/Buttons/Title_Screen_Button_Small.gif",
    "Textures/Buttons/Main_Menu_Button_Main_Highlighted.gif",
    "Textures/Buttons/Title_Screen_Button_Highlighted.gif",
    "Textures/Buttons/Title_Screen_Button_Small_Highlighted.gif",
    "Textures/Buttons/Inventory_Slot_Frame.gif",
    "Textures/Buttons/Inventory_Slot_Frame_Highlighted.gif",
    "Textures/Buttons/Tab.gif",
    "Textures/Buttons/Tab_Highlighted.gif",
    "Textures/GUI/Side_Panel_Shop.gif",
    "Textures/GUI/Locked.gif",
    "Textures/GUI/Tab_Selector.gif",
    "Textures/GUI/Slot_Selector.gif",
    "Textures/Buttons/Settings_And_Controls_Button.gif",
    "Textures/Buttons/Settings_And_Controls_Button_Highlighted.gif",
    "Textures/Interface/Icons/Tab/Machine_Mode_Tab_Icon.gif",
    "Textures/Interface/Icons/Slot/Machine_Default_Slot_Icon.gif",
    "Textures/Interface/Icons/Slot/Alien_Default_Slot_Icon.gif",
    "Textures/Interface/Icons/Slot/Yellow_Power_Up_Slot_Icon.gif",
    "Textures/Interface/Icons/Slot/Red_Power_Up_Slot_Icon.gif",
    "Textures/Interface/Icons/Slot/Green_Power_Up_Slot_Icon.gif",
    "Textures/Interface/Icons/Slot/Blue_Power_Up_Slot_Icon.gif",
    "Textures/Power_Ups/Yellow_Lightning_Power_Up.gif",
    "Textures/Power_Ups/Green_Lightning_Power_Up.gif",
    "Textures/Power_Ups/Red_Lightning_Power_Up.gif",
    "Textures/Power_Ups/Blue_Lightning_Power_Up.gif",
    "Textures/Power_Ups/Blue_Power_Up_Indicator_On.gif",
    "Textures/Power_Ups/Green_Power_Up_Indicator_On.gif",
    "Textures/Power_Ups/Yellow_Power_Up_Indicator_On.gif",
    "Textures/Power_Ups/Red_Power_Up_Indicator_On.gif",
    "Textures/Power_Ups/Blue_Power_Up_Indicator_Off.gif",
    "Textures/Power_Ups/Green_Power_Up_Indicator_Off.gif",
    "Textures/Power_Ups/Yellow_Power_Up_Indicator_Off.gif",
    "Textures/Power_Ups/Red_Power_Up_Indicator_Off.gif",
    "Textures/Coins/Copper_Coin.gif",
    "Textures/Coins/Silver_Coin.gif",
    "Textures/Coins/Gold_Coin.gif",
    "Textures/Coins/Platinum_Coin.gif",
    "Textures/Coins/Coin_Indicator.gif"
]

# Import the textures to the game
if fullscreen == 1:
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
        wn.addshape(new_path)
else:
    # If fullscreen is off, textures are imported with names as is
    for texture in texture_paths:
        wn.addshape(texture)

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
start_ticks = pygame.time.get_ticks()
MONITOR_DELAY = 1.0/TARGET_FPS
