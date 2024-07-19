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
    File: Main.py
    Author: Christian Marinkovich
    Date: 2024-07-19
    Description:
    Main file for the image scaler sub application.
    This application is used to rescale textures in Laser Fighter. This is so that I do not have to manually rescale
        them myself.
"""

import tkinter
from tools.imagescaler.ImageScaler import ImageScalerApp


# Main function defined
def main():
    root = tkinter.Tk()
    app = ImageScalerApp(root)
    root.mainloop()

# Program started
if __name__ == "__main__":
    main()
