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
    File: UpdateMilestones.py
    Author: Christian Marinkovich
    Date: 2024-08-07
    Description:
    This file contains the logic for the in game milestones.
    This includes keeping track of which milestone is displayed on the screen and which milestones have been completed.
"""

from utils.PlayerDataManager import PlayerDataManager


class MilestoneConfig:
    """
        Represents the parser object for the milestones data in both the playerData.ini file.

        Attributes:
            player_data_manager (PlayerDataManager()): The parser for the playerData.ini file

            milestone_1_displayed (int): Checks if the first milestone is being displayed or not
            milestone_2_displayed (int): Checks if the second milestone is being displayed or not
            milestone_3_displayed (int): Checks if the third milestone is being displayed or not
            milestone_4_displayed (int): Checks if the fourth milestone is being displayed or not

            milestone_start_time (float): This start time variable keeps track of how much time it has been since a
                milestone began getting displayed on the screen

            game_played (boolean): Determines if the first milestone has been accomplished or not
            machine_mode_beaten (boolean): Determines if the second milestone has been accomplished or not
            alien_mode_played (boolean): Determines if the third milestone has been accomplished or not
            alien_mode_beaten (boolean): Determines if the fourth milestone has been accomplished or not
    """

    def __init__(self):
        """
            Initializes and loads the current milestones.
        """

        # Initialize the playerData.ini parser
        self.player_data_manager = PlayerDataManager()

        # Initialize the display variables
        self.milestone_1_displayed = 0
        self.milestone_2_displayed = 0
        self.milestone_3_displayed = 0
        self.milestone_4_displayed = 0

        # Initialize the time variable
        self.milestone_start_time = 0

        # Initialize the milestone variables
        self.game_played = False
        self.machine_mode_beaten = False
        self.alien_mode_played = False
        self.alien_mode_beaten = False

        # Load the milestone data from the playerData.ini file
        self.load()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.player_data_manager
        del self.milestone_1_displayed
        del self.milestone_2_displayed
        del self.milestone_3_displayed
        del self.milestone_4_displayed
        del self.milestone_start_time

    def load(self):
        """
            Loads the current milestone configuration from the player data file.

            :return: None
        """

        self.game_played = self.player_data_manager.getboolean('Machine_Mode_First_Time', 'Ran_First_Time')
        self.machine_mode_beaten = self.player_data_manager.getboolean('Machine_Mode_Beat', 'Machine_Mode_Beat')
        self.alien_mode_played = self.player_data_manager.getboolean('Alien_Mode_Played', 'Alien_Mode_Played')
        self.alien_mode_beaten = self.player_data_manager.getboolean('Alien_Mode_Beat', 'Alien_Mode_Beat')

    def save(self):
        """
            Saves the current milestone configuration to the player data file.

            :return: None
        """

        self.player_data_manager.set('Machine_Mode_First_Time', 'Ran_First_Time', str(self.game_played))
        self.player_data_manager.set('Machine_Mode_Beat', 'Machine_Mode_Beat', str(self.machine_mode_beaten))
        self.player_data_manager.set('Alien_Mode_Played', 'Alien_Mode_Played', str(self.alien_mode_played))
        self.player_data_manager.set('Alien_Mode_Beat', 'Alien_Mode_Beat', str(self.alien_mode_beaten))

    def __repr__(self):
        """
            Creates a print statement for the current milestone configuration where they are all listed out in order.

            :return: Prints the current milestone configuration in a list.
            :type: string
        """

        return (f"game_played={self.game_played}, "
                f"machine_mode_beaten={self.machine_mode_beaten}, "
                f"alien_mode_played={self.alien_mode_played}, "
                f"alien_mode_beaten={self.alien_mode_beaten})")
