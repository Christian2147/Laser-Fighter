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

import ctypes

# Constants for preventing system sleep
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001


class MonitorSleepController:
    def __init__(self):
        pass

    def prevent_sleep(self):
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

    def allow_sleep(self):
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

    def __enter__(self):
        self.prevent_sleep()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.allow_sleep()

# Put game loop in: with MonitorSleepController():