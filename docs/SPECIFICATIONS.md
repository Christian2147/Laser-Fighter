# Specifications

Listed here are both the software and hardware specifications for the game and for running the source code. 

## Hardware specifications:

Listed here are the hardware requirements for playing the game. If your hardware is below the minimum specs, I cannot guarentee that the game will run correctly for you or perform well. The most important requirement here is the screen configuration. Please do not download this game if your resolution is lower than 1280 x 720, as the game window will not load correctly and may be inaccessible. Also, make sure you are at least in Windows 7, as the game has not been tested on any earlier version. Finally, the game is mostly run on the CPU, however based on previous testing, having a GPU does tend to help increase performance.

|  Type             | Minimum    |   Recommended      |
|-------------------|------------|--------------------|
| Operating System  | Windows 7  | Windows 11x or 10x |
| Screen Resolution | 1280 x 720 | 1920 x 1080        |
| Aspect Ratio      | Any        | 16/9               |
| CPU               | 4 Core     | 8 core             |
| GPU               | Optional   | NVIDIA RTX 3060 Ti |
| Memory            | 4 GB       | 16 GB              |

## Software Requirements

### For playing the game

Here is the software needed for playing the game through the current executable:

1. Have any recent version of the Windows operating system.
2. Must have Microsoft Visual C++ Redistributable 2015 or later.
3. **Note**: You do not need to have Python installed on your computer to run the executable! 

### For the source code

Here is the software you should install if you want to look at and work with the source code and also the software used to create the game:

1. <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" width="25"/> Python version 3.7.3 (Recommended to avoid potential compatibility issues and was used for the game development)  
2. <img src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Visual_Studio_Code_Logo.png" alt="Visual Studio Code Logo" width="25"/> Visual Studio Code or PyCharm Community Edition 2019.1.3 x64 (Both were used for the games development)
3. <img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Git-logo.svg" alt="Git Logo" width="25"/> Any version of Git - For organizing the project
4. <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Krita_Logo.svg" alt="Krita Logo" width="25"/> Any version of Krita - For creating textures
5. <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Audacity_Logo.png" alt="Audacity Logo" width="25"/> Any version of Audacity - For creating and editing game sounds
6. <img src="https://upload.wikimedia.org/wikipedia/commons/4/43/Paint_3D_Logo.png" alt="Paint 3D Logo" width="25"/> Paint 3D - For saving a gif with transparency
7. The Laser Fighter Image scaler provided in the "tools" directory of this repo - For scaling .gif texture files

## External libraries used to create Laser Fighter

The following is a list of external libraries used in the development of Laser Fighter. These libraries must be installed to run the source code. Note that some of these libraries are included with Python by default, while others require manual installation.

### Core Libraries:

1. **os** - Provides functions to interact with the operating system, such as file handling.
2. **math** - Offers mathematical functions like trigonometric operations, logarithms, etc.
3. **time** - Handles time-related functions, such as frame rate and delta time
4. **random** - Used for generating random numbers, essential for various game mechanics like spawn chances

### GUI And Graphics:

1. **turtle** - A standard Python library used for basic graphics and drawing, forming the core of the game's visual elements.
2. **TKinter** - Python's standard GUI toolkit, utilized for creating button functions and configuring the screen
3. **Pillow (PIL)** - An external library for image processing, used here for handling and manipulating textures.
4. **pygame** - A set of Python modules designed for writing video games, used for handling frame rate, sound, and improving performance

### Windows Specific Libraries:

**IMPORTANT**: For Linux users wishing to work with the source code, you will need to manually change these with Linux compatible libraries in order to run the source code!

1. **win32api** - Part of the PyWin32 library and used to interact with the Windows API. Here it was used to extract the users monitor information
2. **win32con** - Another component of PyWin32, providing constants used in various Windows API functions. Used for extracting the monitors refresh rate
3. **ctypes** - A foreign function library for Python, allowing the calling of functions in DLLs or shared libraries.

### File Handling And Configuration:

1. **configparser** - Used for reading and writing configuration files, enabling easy management of game settings.
2. **subprocess** - Allows the spawning of new processes, connecting to their input/output/error pipes, and obtaining their return codes. Used to backup the configuration files.

### Advanced Libraries:

1. **scipy.optimize** - Part of the SciPy library, providing optimization algorithms. Used for the calculation of hitboxes.
2. **gc** - Controls the garbage collector in Python, useful for managing memory in a complex game environment.
3. **fractions** - Provides support for rational number arithmetic, and used for calculating the scaling of text.

### Concurrency

1. **threading** - Supports multi-threaded execution, allowing the game to perform tasks like background loading or parallel processing.

**NOTE**: These libraries were NOT created by me and were simply used in the production of this software.

## Additional Note

If you are still having problems running the game, try disabling any antivirus software for a short period of time. Since the executable is unsigned, some antivirus software may detect it as a threat.

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)