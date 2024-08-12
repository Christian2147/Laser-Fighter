![Splash Text](img/Laser_Fighter_Splash_Text.png)

# Laser-Fighter

Laser Fighter is a 2D laser shooting game and is the first game that I have created. The first version was finished in December of 2021 and it has been growing ever since. About 600 hours of work have so far been put into this game and more is on the way. I created this game not only because it was fun but also because I wanted to learn more about the software development process by actually creating a real piece of software. Considering I am really familiar with gaming and indie games, I felt that a 2D pixel shooting game would be a good place to start. If you want to know more about the history of Laser Fighter and how it came to be, be sure to check out its [history](./docs/HISTORY.md).


## HOTFIX 1.2.1b:

This branch contains the source code for Laser Fighter v1.2.1b. This version was completed in August of 2024. This update is a small HOTFIX update released in order to patch some of the bugs found in MINOR update 1.2.0b. This update is also the first update to enable a pathway for Linux compatibility. This was achieved by making certain Windows only scripts, like the in-game message boxes and the sleep prevention, cross platform with the use of the os module and the tkinter module. While Linux compatibility is not a thing yet, this update along with the instructions provided on the [instructions page](./docs/INSTRUCTIONS.md) makes it possible to achieve Linux compatibility. 

NOTE: The exe file for this application is unsigned and has an unverified publisher. This means that Windows Defender and other antivirus software may be suspicious of the file. If this happens, simply select "Run Anyway". Make sure you are downloading Laser Fighter from the [Laser Fighter GitHub](https://github.com/Christian2147/Laser-Fighter) and no other external source. If you download Laser Fighter from any other source, I am not responsible for any damage that the executable may cause. Outside of this GitHub page, anyone is allowed to make whatever modifications they want to this software.

## Changelog:

### Additions
+ Added a pathway to Linux compatibility (Still not fully implemented)
+ Added a Laser Fighter icon to all message boxes

### Changes
* Fixed coins being picked up when they should not be in Alien Mode
* Fixed bugs regarding the naming of textures
* Fixed a vulnerability with cleanup.bat

## Helpful Links

For a full list of specifications and requirements, go to the [specifications page](./docs/SPECIFICATIONS.md)<br>
For instructions on how to install the game or use the source code, go to the [instructions page](./docs/INSTRUCTIONS.md)<br>
For a brief overview of the games features and storyline, go to the [features page](./docs/FEATURES.md)<br>

## Acknowledgments

I would like to thank the following contributors:

- **@yosoyducc**: Contributed to creating the `./source/textures/cleanup.sh` and the `./source/config/bckp.sh` shell scripts for Linux compatibility, which is copyrighted (c) 2024, yosoyducc. 

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)