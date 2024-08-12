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
    File: PreventSleep.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic related to the system sleep settings.
    If the game is running, this code will elt the system know that it is a critical application and to not enter
        sleep mode.
    When the program terminates, either normally or with an error, the setting will be reversed back to the
        default state.
"""

import os
import ctypes

# Constants for preventing system sleep:
# ES_CONTINUOUS: System should continue to use the current state
# ES_SYSTEM_REQUIRED: Indicates that the system is in use
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001


class MonitorSleepController:
    """
        Represents the sleep controller which prevents the system from entering sleep mode.
    """

    def __init__(self):
        self.os_name = os.name

    def prevent_sleep(self):
        """
            Lets the system know that this is a critical application and prevents it from entering sleep mode

            :return: None
        """

        # For windows
        if self.os_name == 'nt':
            # Let the system know to stay awake
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
        # For Linux
        elif self.os_name == 'posix':
            # Turn off screen saver
            os.system('xset s off')
            # Disable DPMS (Energy Star) features
            os.system('xset -dpms')
            # Prevent screen blanking
            os.system('xset s noblank')

    def allow_sleep(self):
        """
            Allows the system to enter sleep mode once the application has terminated

            :return: None
        """

        # For Windows
        if self.os_name == 'nt':
            # Allow the system to sleep
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        # For Linux
        elif self.os_name == 'posix':
            # Turn on screen saver
            os.system('xset s on')
            # Enable DPMS (Energy Star) features
            os.system('xset +dpms')
            # Allow screen blanking
            os.system('xset s blank')

    def __enter__(self):
        """
            Enter a non sleep state.

            :return MonitorSleepController: The sleep controller
            :type: MonitorSleepController()
        """

        self.prevent_sleep()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Exit the non sleep state.

            :param exc_type: NA
            :param exc_val: NA
            :param exc_tb: NA

            :return: None
        """

        self.allow_sleep()
