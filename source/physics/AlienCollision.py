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

from setup.ScreenSetup import scale_factor_X
from setup.ScreenSetup import scale_factor_Y


class AlienCollision:
    SMALL_ALIEN_Y_RANGE = (-193 * scale_factor_Y, -88 * scale_factor_Y)
    MEDIUM_ALIEN_Y_RANGE = (-196 * scale_factor_Y, -52 * scale_factor_Y)
    LARGE_ALIEN_Y_RANGE = (-197 * scale_factor_Y, 27 * scale_factor_Y)
    UFO_Y_RANGE = (-92 * scale_factor_Y, 52 * scale_factor_Y)

    SMALL_ALIEN_X_DISTANCE = 26 * scale_factor_X
    MEDIUM_ALIEN_X_DISTANCE = 36 * scale_factor_X
    LARGE_ALIEN_X_DISTANCE = 50 * scale_factor_X
    UFO_X_DISTANCE = 53 * scale_factor_X
