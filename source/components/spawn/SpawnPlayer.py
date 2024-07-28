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

from components.player.MachinePlayer import Player
from components.player.HumanPlayer import Human


class SpawnMachinePlayer:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_player = []
        self.current_player = []
        self.current_player_index = 0
        self.player_hit_value = 0
        self.player_update_value = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_player
        del self.current_player
        del self.current_player_index
        del self.player_hit_value
        del self.player_update_value

    def spawn_machine_player(self, god_mode):
        """
            Spawn the Machine Mode player on the screen.

            :return: None
        """

        if len(self.all_player) <= len(self.current_player):
            player = Player(god_mode, self.scale_factor_x, self.scale_factor_y)
            self.current_player.append(player)
            self.current_player_index = self.current_player_index + 1
            self.all_player.append(player)
        else:
            for p in self.all_player:
                if p.get_player().isvisible():
                    continue
                else:
                    p.reinstate(god_mode)
                    self.current_player.append(p)
                    self.current_player_index = self.current_player_index + 1
                    break


class SpawnHumanPlayer:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_human = []
        self.current_human = []
        self.current_human_index = 0
        self.human_hit_value = 0
        self.human_update_value = 0
        self.right_update = 0
        self.left_update = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_human
        del self.current_human
        del self.current_human_index
        del self.human_hit_value
        del self.human_update_value
        del self.right_update
        del self.left_update

    def spawn_human_player(self, god_mode):
        """
            Spawn the human player on the screen.

            :return: None
        """

        if len(self.all_human) <= len(self.current_human):
            human = Human(god_mode, self.scale_factor_x, self.scale_factor_y)
            self.current_human.append(human)
            self.current_human_index = self.current_human_index + 1
            self.all_human.append(human)
        else:
            for h in self.all_human:
                if h.get_player().isvisible():
                    continue
                else:
                    h.reinstate(god_mode)
                    self.current_human.append(h)
                    self.current_human_index = self.current_human_index + 1
                    break
