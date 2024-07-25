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

from setup.ScreenSetup import wn
from setup.SpriteSetup import button
from setup.SpriteSetup import textbox
from setup.SpriteSetup import panel
from setup.SpriteSetup import price_label
from setup.SpriteSetup import yellow_power_up_indicator
from setup.SpriteSetup import blue_power_up_indicator
from setup.SpriteSetup import extra_power_up_indicator
from setup.SpriteSetup import machine_player
from setup.SpriteSetup import human_player
from setup.SpriteSetup import small_alien
from setup.SpriteSetup import medium_alien
from setup.SpriteSetup import large_alien
from setup.SpriteSetup import ufo
from setup.ConfigurationSetup import shop_config
from setup.ConfigurationSetup import settings
from setup.ConfigurationSetup import controls_toggle
from setup.ConfigurationSetup import statistics
from setup.ConfigurationSetup import refresh_variables
from setup.ScreenSetup import scale_factor_X
from setup.ScreenSetup import scale_factor_Y
from utils.ScreenManager import ScreenUpdate
from utils.MovementManager import Movement
from utils.HoverManager import Hover
from utils.ShopManager import Shop
from utils.SettingsManager import SettingsToggle
from utils.ControlsManager import Controls
from utils.UpdateText import TextRefresh

screen = ScreenUpdate(wn, button, settings, refresh_variables,
                      scale_factor_X, scale_factor_Y)

movement = Movement(screen, machine_player, human_player,
                    settings, statistics,
                    scale_factor_Y)

hover = Hover(screen, button)

shop = Shop(wn, screen, button,
            panel, textbox, price_label,
            settings, refresh_variables, shop_config,
            scale_factor_X, scale_factor_Y)

settings_toggle = SettingsToggle(wn, screen, button,
                                 settings, refresh_variables, scale_factor_X,
                                 scale_factor_Y)

controls = Controls(wn, screen, settings,
                    controls_toggle, refresh_variables, scale_factor_X,
                    scale_factor_Y)

text_refresh = TextRefresh(screen, button, panel,
                           textbox, yellow_power_up_indicator, blue_power_up_indicator,
                           extra_power_up_indicator, settings,
                           settings_toggle, statistics, shop,
                           shop_config, controls, controls_toggle,
                           refresh_variables)

# Set the keybinds for the turtle graphics window:
# Bind the current keybinds to their appropriate functions
wn.listen()
wn.onkeypress(movement.go_left, controls_toggle.go_left_key)
wn.onkeypress(movement.go_right, controls_toggle.go_right_key)
wn.onkeypress(movement.shoot, controls_toggle.shoot_key)
wn.onkeypress(movement.jump, controls_toggle.jump_key)

# Detect when the user wants to close the window and terminate the game loop.
# "WM_DELETE_WINDOW" is the parameter used to determine if the user has clicked the red x in the corner of the window
# If so, run the "on_quit" function which terminates the window
wn._root.protocol("WM_DELETE_WINDOW", screen.on_quit)

# The two lines of code below are used to collect the position of the users mouse on the canvas
mouse_position = wn.getcanvas()
mouse_position.bind('<Motion>', hover.hover)
