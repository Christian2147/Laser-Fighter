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
    File: ConfigManager.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
        Manages the parser for the config.ini file. This class is here to make sure that only one parser is being
            used at all times for this file to avoid any potential conflicts.
"""

import configparser
import threading
from tkinter import messagebox


class ConfigManager:
    """
        Represents the parser for the config.ini file in the config folder.

        Attributes:
            _file_path (string): The path to the config file
            config (configparser.ConfigParser()): The parser object for the file.
    """

    # Sets the instance to "None" at the beginning
    _instance = None
    # Ensure thread-safe access
    _lock = threading.Lock()

    def __new__(cls, file_path='config/config.ini'):
        """
            Creates the One and only instance of this class

            :param file_path: The path to the config file
            :type file_path: string

            :return cls._instance: The class instance
            :type: ConfigManager()
        """

        with cls._lock:
            # Ensures only one instance of this class can exist
            if cls._instance is None:
                cls._instance = super(ConfigManager, cls).__new__(cls)
                cls._instance._file_path = file_path
                cls._instance.config = configparser.ConfigParser()
                cls._instance.load()
        return cls._instance

    def load(self):
        """
            Reads the given config file to the config parser using the file path.

            :return: None
        """

        self.config.read(self._file_path)

    def save(self):
        """
            Saves the new data to the config file and updates it.

            :return: None
        """

        with open(self._file_path, 'w') as configfile:
            self.config.write(configfile)

    def set(self, section, key, value):
        """
            Used to set values in the config file.

            :param section: The name of the list in the config file to modify
            :type section: string

            :param key: The name of the variable in the config file to modify
            :type key: string

            :param value: The value to set the variable to (Must be a string)
            :type value: string

            :return: None
        """

        try:
            if not self.config.has_section(section):
                self.config.add_section(section)
            self.config.set(section, key, value)
            self.save()
        except configparser.Error as e:
            messagebox.showerror("Error", f"Error saving config file: {e}")

    def get(self, section, key):
        """
            Used to retrieve a string value from the config file.

            :param section: The name of the list in the config file to access
            :type section: string

            :param key: The name of the variable in the config file to access
            :type key: string

            :return: The string value that was requested
            :type: string
        """

        try:
            return self.config.get(section, key, fallback="")
        except configparser.Error as e:
            messagebox.showerror("Error", f"Error reading config file: {e}")
            return ""

    def getint(self, section, key):
        """
            Used to retrieve a integer value from the config file.

            :param section: The name of the list in the config file to access
            :type section: string

            :param key: The name of the variable in the config file to access
            :type key: string

            :return: The integer value that was requested
            :type: int
        """

        try:
            return self.config.getint(section, key, fallback=0)
        except configparser.Error as e:
            messagebox.showerror("Error", f"Error reading config file: {e}")
            return 0
