# Instructions for working with this program

## Creating your own virtual environment

These are the instructions if you want to use this source code and create your own virtual environment for it

1. Open command prompt by typing "cmd" in the search bar
2. type `cd path/to/your/project`
3. type:
    - `python -m venv venv` (Windows) 
    - `python3 -m venv venv` (Linux)
4. Now you must activate your virtual environment by typing: 
    - `venv\Scripts\activate` (Windows) 
    - `source venv/bin/activate` (Linux)
5. Install the reuired packages by typing `pip install -r requirements.txt` and press Enter
6. To verify the installation and see the installed packages, type `pip list`
7. Starting working!

**NOTE:** If you run into problems biulding the virtual environment, try installing the requirements one by one

## Packaging the game

These are the instructions to convert the source code into a package with the executable file that can be redistributed. 

1. Open command prompt by typing "cmd" in the search bar
2. type `cd path/to/your/python/file/to/convert`
3. Make sure you have pyinstaller installed
    - If not, type `pip install pyinstaller` in the terminal
4. Type `pyinstaller -F -w -i Icon/icon.ico main.py`
5. Go to the dist folder in your directory and put the executable in the main directory.
5. Copy the entire source folder to a zip file
6. Delete all folders and files within except the "Config" "Icon" "Sound" and "Textures" folders
7. Do not forget the LICENSE file!

### Additional Note

The recommended version of python to use is python 3.7.3. This is what the game was created in.

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
