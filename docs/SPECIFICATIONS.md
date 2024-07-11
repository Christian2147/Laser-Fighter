# Specifications

Listed here are both the software and hardware specifications for the game and the source code. 

## Hardware specifications:

Listed here are the hardware requirements for playing the game. If your hardware is below the minimum specs, I cannot garentee that the game will run correctly for you. The most immportant one here is the screen configuration. Please do not download this game if your resolution is lower than 1280 x 720, the game window will simply not load correctly and be inaccessible. Also, make sure your at least in Windows 7, as the game has not been tested for any earlier version. If your in an aspect ratio other than 16/9, text on the screen may load out of bounds.

|  Type             | Minimum    |   Recommended      |
|-------------------|------------|--------------------|
| Operating System  | Windows 7x | Windows 11x or 10x |
| Screen Resolution | 1280 x 720 | 1920 x 1080        |
| Aspect Ratio      | <=16/9     | 16/9               |
| CPU               | 4 Core     | 8 core             |
| GPU               | Optional   | NVIDIA RTX 3060 Ti |
| Memory            | 4 GB       | 16 GB              |

## Software Requirements

### For playing the game

Here is the software needed for playing the game through the executable:

1. Have the Windows operating system.
2. Must have Visual C++ Redistributable 2015 or later.
3. You do not need to have python installed on your computer! 

### For the source code

Here is the software you should install if you want to look at and work with the source code and the software used to create the game:

1. Python version 3.7.3
2. Visual Studio Code or PyCharm Community Edition 2019.1.3 x64 (Both were used for the games development)
3. Any version of Git
4. Any version of Krita for texture drawing
5. Any version of Audacity
6. Paint 3D (To save a gif with transparency)

## External libraries used to create Laser Fighter

Listed here are all the external libraries used to create Laser Fighter. You must have these installed in order to run the source code.

1. turtle
2. TKinter
3. win32api
4. win32con 
5. pygame
6. os
7. Pillow Image
8. configparser
9. subprocess
10. math
11. time
12. random
13. ctypes

These libraries were NOT created by me and were simply used in the production of this software. Some of these are installed with Python by default, some have to be installed manually.

## Additonal Note

If you are still having problems running the game, try disabling any antivirus software for a short period of time. Since the executable is unsigned, some antivirus software may detect it as a threat (The only threat is my poor coding skills).

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)