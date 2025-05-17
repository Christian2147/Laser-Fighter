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

import win32api
import win32con
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

# Initialize PyGame and PyGame Sound Engine (Performance improvements and better sound)
pygame.init()
pygame.mixer.init()

display_info = pygame.display.Info()
current_screen_width = display_info.current_w
current_screen_height = display_info.current_h

# Default window size (1280x720)
base_width = 1280
base_height = 720

if settings.fullscreen == 1:
    screen = pygame.display.set_mode((current_screen_width, current_screen_height), pygame.FULLSCREEN)

    # Calculate aspect ratio
    aspect_ratio = Fraction(current_screen_width, current_screen_height)
    target_aspect_ratio = Fraction(16, 9)

    if current_screen_height < current_screen_width:
        scale_factor = current_screen_height / base_height
    else:
        scale_factor = current_screen_width / base_width

    scale_factor_X = current_screen_width / base_width
    scale_factor_Y = current_screen_height / base_height

    # Aspect ratio adjustment if screen is narrower than 16:9
    decimal_aspect_ratio = 1 / (current_screen_width / current_screen_height)
    if decimal_aspect_ratio > 0.5625:  # 9/16
        new_screen_height = current_screen_width * 9 / 16
        scale_factor = new_screen_height / base_height
else:
    screen = pygame.display.set_mode((base_width, base_height))
    current_screen_width = base_width
    current_screen_height = base_height

# Set window title
pygame.display.set_caption("Laser Fighter")

# Set window icon
icon_surface = pygame.image.load("icon/Icon.png")
pygame.display.set_icon(icon_surface)

# Load and scale background
background_path = "textures/background/Shooting_Game_Background.png"
background_image = Image.open(background_path)
new_width = int(background_image.width * scale_factor_X)
new_height = int(background_image.height * scale_factor_Y)
resized_image = background_image.resize((new_width, new_height))
scaled_background_path = "textures/background/Shooting_Game_Background_Scaled.png"
resized_image.save(scaled_background_path)
bg_surface = pygame.image.load(scaled_background_path).convert()
screen.blit(bg_surface, (0, 0))
pygame.display.flip()

# Extract the refresh rate of the users monitor through the windows API
# Remove this if you are trying to run this on Linux
DISPLAY_DEVICE = win32api.EnumDisplayDevices(None, 0)
SETTINGS = win32api.EnumDisplaySettings(DISPLAY_DEVICE.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
REFRESH_RATE = SETTINGS.DisplayFrequency

# Set the target FPS to the refresh rate for VSync, otherwise the FPS is not used since "unlimited" would be allowed
# Unlimited FPS means that the game loop executes as fast as possible
CLOCK = pygame.time.Clock()
TARGET_FPS = REFRESH_RATE
MONITOR_DELAY = 1.0/TARGET_FPS
