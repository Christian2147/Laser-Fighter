![Splash Text](img/Laser_Fighter_Splash_Text.png)

# Laser-Fighter

Laser Fighter is a 2D laser shooting game and is the first game that I have created. The first versions was finished in December of 2021 and it has been growing ever since. About 500 hours of work have so far been put into this game and more is along the way. I created this game not only because it was fun but also because I wanted to learn more about the software development process by actually creating a real piece of software. Considering I am really familiter with gaming and indie games, I felt that a 2D pixel shooting game would be a good place to start.


## Version 1.0.0b:

This branch contains the source code for Laser Fighter v1.0.0b. This version was completed in July of 2024. This was one of the biggest updates the game has ever had and was the first update I made during my college years. In this update, I vastly changed the source code to be across multiple files and organized into classes. This took sveeral weeks but it needed to be done since having it all in one file was just too messy. There were also vast optimization improvements in this version of the game. I implimented several optimization techniques based on the concepts I learned in college to achieve this. One thing I did was be sure to reuse already created turtle sprites to avoid lag. I also made sure that no extra conditionals were being checked at every iteration. PyGames preformance acceleration also helped speed up the game. This update was more of a quality of life update. Rather than adding dozens of features, it improved upon what already exists. The graphics and gameplay was also improved along with the performance. 

NOTE: The exe file for this application is unsigned and has an unverified publisher. This means that windows defender and other antiviruses may be suspicious of the file. If this happens, simply select "Run Anyway". Make sure you are downloading Laser Figher from the [Laser Fighter GitHub](https://github.com/Christian2147/Laser-Fighter) and no other external source. If you download Laser Fighter from any other source, I am not responsible for any damage that the executable may cause. Outside of this GitHub page, anyone is allowed to make whatever modifications they want to this software.

## Changelog:

### Additions
+ Added Coins! Coins come in 4 different types and spawn wherever you kill an enemy (Which type depeneds on the enemy killed)
+ Added fullscreen mode! You can finally fullscreen your game
+ Added a health bar in Machine Mode (Felt that it was unproportionally hard to Alien Mode)
+ Graphics Update! Replaced dozens of in game graphics with better, up to date ones
+ Added more randomness to enemy spawning in Machine Mode
+ Added a float effect to the enemies in Machine Mode
+ Added a day/night cycle in Alien Mode
+ Added VSync and framerate!
+ Added an exit button
+ Added automatic player data and configuration backups
+ Added some variation to enemy sizes in Machine Mode

### Changes
* MAJOR preformance improvements
* Created Better in game timing
* Fixed the sound cutting out (Works perfectly now and multiple sounds can play at once)
* Fixed a bug that caused you to get stuck and not be able to move in Alien Mode after dying
* Fixed the jumping animation in Alien Mode (USes real phsyics now and is more realistic)
* Fixed the power up timers not actually counting in real seconds (They count accuratly now)
* Fixed several other minor in game bugs

## License

Copyright (c) [2024] [Christian Marinkovich]

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)