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

from utils.PlayerDataManager import PlayerDataManager


class MilestoneConfig:
    def __init__(self):
        """
            Initializes and loads the current milestones.
        """

        # Initialize the playerData.ini parser
        self.player_data_manager = PlayerDataManager()

        self.milestone_1_displayed = 0
        self.milestone_2_displayed = 0
        self.milestone_3_displayed = 0

        self.milestone_start_time = 0

        # Initialize the milestone variables
        self.game_played = False
        self.machine_mode_beaten = False
        self.alien_mode_beaten = False

        self.load()

    def __del__(self):
        del self.player_data_manager
        del self.milestone_1_displayed
        del self.milestone_2_displayed
        del self.milestone_3_displayed
        del self.milestone_start_time

    def load(self):
        self.game_played = self.player_data_manager.getboolean('Machine_Mode_First_Time', 'Ran_First_Time')
        self.machine_mode_beaten = self.player_data_manager.getboolean('Machine_Mode_Beat', 'Machine_Mode_Beat')
        self.alien_mode_beaten = self.player_data_manager.getboolean('Alien_Mode_Beat', 'Alien_Mode_Beat')

    def save(self):
        self.player_data_manager.set('Machine_Mode_First_Time', 'Ran_First_Time', str(self.game_played))
        self.player_data_manager.set('Machine_Mode_Beat', 'Machine_Mode_Beat', str(self.machine_mode_beaten))
        self.player_data_manager.set('Alien_Mode_Beat', 'Alien_Mode_Beat', str(self.alien_mode_beaten))

    def __repr__(self):
        return (f"game_played={self.game_played}, "
                f"machine_mode_beaten={self.machine_mode_beaten}, "
                f"alien_mode_beaten={self.alien_mode_beaten})")
