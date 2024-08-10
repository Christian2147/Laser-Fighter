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
    - **ADDITIONAL NOTE**: Linux does not support batch, meaning that Linux users will have to manually clean these files up. Full support for Linux is planned in the future but not here yet :(

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
