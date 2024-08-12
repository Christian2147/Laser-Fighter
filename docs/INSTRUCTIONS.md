# Instructions for working with this program

## Creating your own virtual environment

These are the instructions if you want to use this source code and create your own virtual environment:

1. Open command prompt (Windows) or the terminal (Linux)
2. type 
    ```cmd
    cd path/to/your/project
    ```
3. type:
    -   (Windows)
        ```cmd
        python -m venv venv
        ```
    -   (Linux)
        ```bash
        python3 -m venv venv
        ```
4. Now you must activate your virtual environment by typing: 
    -   (Windows)
        ```cmd 
        venv\Scripts\activate
        ```
    -   (Linux) 
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages by typing 
    ```cmd
    pip install -r requirements.txt
    ``` 
    and press Enter
6. To verify the installation and see the installed packages, type 
    ```cmd
    pip list
    ```
7. Begin working with the source code!

### If you are facing issues installing the virtual environment:

Try removing the following libraries from requirements.txt:
- pip
- setuptools
- memory-profiler
- psutil

If you are still having problems, remember that all directory names MUST be lowercase.
All Texture files must be in the following naming format: Word_Word_Word.gif
All Python files must be in the following naming format: WordWordWord.py

If any of these files are named incorrectly, simply manually rename them.

### If you are on Linux (Not Directly supported):

1. Additionally to removing the libraries listed above, remove the following from the requirements.txt:
    - pywin32
    - pywin32-ctypes
2. If you installed Python on Linux, the modules above should have came with Linux alternatives by default. The only exceptions to this rule are win32api and win32con.
3. You will have to manually replace these libraries in the game code in order for it to run. These libraries are only used to access the users monitor properties. You can do this using the xrandr function under the subprocess module. Here is an example:

```python
import subprocess

def get_screen_resolution():
    # Run the `xrandr` command
    result = subprocess.run(['xrandr'], capture_output=True, text=True)
    
    # Decode the output and find the line containing the current resolution
    output = result.stdout
    lines = output.splitlines()
    
    for line in lines:
        if '*' in line:  # '*' indicates the current resolution and refresh rate
            parts = line.split()
            resolution = parts[0]  # The resolution is the first part of the line
            refresh_rate = parts[1]  # The refresh rate is the second part
            width, height = resolution.split('x')
            return int(width), int(height), float(refresh_rate[:-2])  # Remove 'Hz' from refresh rate

    return None, None, None

# Example usage (These are the actual parameters in the games code you have to set using this function. You also have to remove the old way they are declared)
current_screen_width, current_screen_height, REFRESH_RATE = get_screen_resolution()
```
On top of this: 
1. Comment out the DISPLAY_DEVICE and SETTINGS parameters.
2. Remove the setter for the REFRESH_RATE variable (It has already been set in the function above)
3. Change 
    ```python 
    window.setup(width=win32api.GetSystemMetrics(0), height=win32api.GetSystemMetrics(1)) 
    ```
    to
    ```python
    window.setup(width=current_screen_width, height=current_screen_height)
    ```
    and make sure to calculate these parameters with the function given above before executing this function.
    
4. Your virtual environment should work on Linux at this point if you managed to perform the setup correctly.

#### **Note**:

The instructions above are just mere suggestions and guidelines for how to get the virtual environment to work on Linux. I cannot guarentee that it will in fact be a 100% solution as Linux support has not been implemented yet. The performance of this software on Linus may also be unpredictable. In the future when Linux support is implemented, there will be a streamlined way to set the venv up for Linux.
    
#### **Special Thanks**:

Special Thanks to @yosoyducc for helping me with the Linux instructions on this page!

## Cleaning Up And Resetting The Game

These instructions are for factory resetting the games state.

1. Navigate to the `config` directory, which is in the `source` directory
2. Reset the config.ini file to its default state, which is the following:
```ini
[Settings]
god_mode = 0
button_sound = 1
player_shooting_sound = 1
enemy_shooting_sound = 1
player_death_sound = 1
enemy_death_sound = 1
player_hit_sound = 1
enemy_hit_sound = 1
power_up_pickup_sound = 1
power_up_spawn_sound = 1
coin_pick_up_sound = 1
fullscreen = 0
vsync = 1

[Controls]
go_right = d
go_left = a
shoot = space
jump = w
```

3. Reset the keyUpdate.ini file to its default state, which is the following:
```ini
[Key_Update]
key_1 = 0
key_2 = 0
key_3 = 0
key_4 = 0
```

4. Reset the playerData.ini file to its default state, which is the following:
```ini
[High_Score]
high_score_machine_war = 0
high_score_alien_mode = 0

[Coins]
coins = 0

[Machine_Mode_First_Time]
ran_first_time = False

[Machine_Mode_Beat]
machine_mode_beat = False

[Alien_Mode_Played]
alien_mode_played = False

[Alien_Mode_Beat]
alien_mode_beat = False

[Statistics_Machine_Mode]
bosses_killed = 0
red_bots_killed = 0
yellow_bots_killed = 0
blue_bots_killed = 0
deaths = 0
damage_taken = 0
lasers_fired = 0
power_ups_picked_up = 0
coins_collected = 0

[Statistics_Alien_Mode]
ufos_killed = 0
big_aliens_killed = 0
medium_aliens_killed = 0
small_aliens_killed = 0
deaths = 0
damage_taken = 0
lasers_fired = 0
jumps = 0
power_ups_picked_up = 0
coins_collected = 0

[Machine_Player_Enabled]
type_enabled = 1

[Alien_Mode_Gun_Enabled]
type_enabled = 0

[Machine_Unlocked]
slot_1 = 1
slot_2 = 0
slot_3 = 0
slot_4 = 0
slot_5 = 0

[Alien_Unlocked]
slot_1 = -1
slot_2 = -1
slot_3 = -1
slot_4 = -1
slot_5 = -1

[Power_Up_Levels]
yellow_power_up = 1
blue_power_up = 1
green_power_up = 1
red_power_up = 0

[Gadgets_Unlocked]
coin_magnet_unlocked = False
armor_unlocked = False
thorns_unlocked = False
hearts_unlocked = False

[Gadgets_Enabled]
coin_magnet_enabled = False
armor_enabled = False
thorns_enabled = False
hearts_enabled = False
```
5. Remove the `bak` folder in that same `config` directory
6. Finally, go to the `textures` directory also located in the `source` directory
7. Run the `cleanup.bat` file to clean up all the extra texture files created from scaling in fullscreen mode
    - **WARNING**: Please **NEVER** move this file, as it could cause unintended consequences!
    - **ADDITIONAL NOTE**: Linux does not support batch, meaning that Linux users will have to run the `cleanup.sh` file instead.

## Packaging the game

These are the instructions to convert the source code into a package with the executable file that can be redistributed. 

1. Open command prompt by typing "cmd" in the search bar
2. type 
    ```cmd
    cd path/to/your/python/file/to/convert
    ``` 
    which would be the path to "main.py" in the "source" directory
3. Make sure you have pyinstaller installed
    - If not, type 
        ```cmd
        pip install pyinstaller
        ``` 
        in the terminal
4. Type:
    -   (Windows)
        ```cmd 
        pyinstaller -F -w -i icon/icon.ico main.py
        ``` 
    -   (Linux)
        ```bash 
        pyinstaller -F -w -i icon/icon.png main.py
        ```
5. Go to the dist folder in your directory and put the executable in the main directory.
5. Copy the entire source folder to a zip file
6. Delete all folders and files within except the "config" "icon" "sound" and "textures" folders
7. Do not forget to include the LICENSE file!

### Note

The recommended version of python to use is python 3.7.3. This is what the game was created in.

## Packaging the Image Scaler:

These are the instructions for generating an executable for the Laser Fighter Image Scaler.

1. Set the "source" pointer of the venv to "imagescaler" instead of "source"
2. Open command prompt by typing "cmd" in the search bar
3. Type 
    ```cmd
    cd path/to/your/python/file/to/convert
    ``` 
    which would be the path to the "Main.py" in the "imagescaler" directory
4. Type 
    ```cmd
    pyinstaller -F -w -i Main.py
    ```
5. Go to the dist folder in your directory and put the executable in the main directory.
6. Run the executable!
7. You can now set the source pointer for the venv back to the "source" directory

### Note

The recommended version of python to use is python 3.7.3. This is what the game was created in.

### Additional Note

In order to package the image scaler in Linux, you first must convert the .ico file to a .png file and change the source code to use the .png file as an icon instead of the .ico file. 

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
