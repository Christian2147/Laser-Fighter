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

from setup.WindowSetup import scale_factor_X
from setup.WindowSetup import scale_factor_Y
from setup.ConfigurationSetup import shop_config
from setup.PowerUpSetup import PowerUpSetup
from setup.AlienModeSetup import AlienModeSetup
from setup.MachineModeSetup import MachineModeSetup

power_up_setup = PowerUpSetup(shop_config)

alien_mode_setup = AlienModeSetup(shop_config, power_up_setup, scale_factor_X, scale_factor_Y)

machine_mode_setup = MachineModeSetup(shop_config, power_up_setup, scale_factor_X, scale_factor_Y)
