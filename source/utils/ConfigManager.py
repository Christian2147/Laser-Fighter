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
import configparser
import threading


class ConfigManager:
    _instance = None
    _lock = threading.Lock()  # Ensure thread-safe access

    def __new__(cls, file_path='config/config.ini'):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ConfigManager, cls).__new__(cls)
                cls._instance._file_path = file_path
                cls._instance.config = configparser.ConfigParser()
                cls._instance.load()
        return cls._instance

    def load(self):
        self.config.read(self._file_path)

    def save(self):
        with open(self._file_path, 'w') as configfile:
            self.config.write(configfile)

    def set(self, section, key, value):
        try:
            if not self.config.has_section(section):
                self.config.add_section(section)
            self.config.set(section, key, value)
            self.save()
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)

    def get(self, section, key):
        try:
            return self.config.get(section, key, fallback="")
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)
            return ""

    def getint(self, section, key):
        try:
            return self.config.getint(section, key, fallback=0)
        except configparser.Error as e:
            ctypes.windll.user32.MessageBoxW(0, f"Error reading config file: {e}", "Error", 0x10)
            return 0
