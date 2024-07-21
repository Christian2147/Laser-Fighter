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

from components.ItemCoin import CoinIndicator


class SpawnCoinIndicator:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.coin_indicator_turtle = []
        self.coin_indicator_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.coin_indicator_turtle
        del self.coin_indicator_index

    def spawn_coin_indicator(self):
        """
            Spawn a coin indicator at the top of the screen.

            :return: None
        """

        if len(self.coin_indicator_turtle) == 0:
            coin_ind = CoinIndicator(self.scale_factor_x, self.scale_factor_y)
            self.coin_indicator_turtle.append(coin_ind)
            self.coin_indicator_index = self.coin_indicator_index + 1
        else:
            for ci in self.coin_indicator_turtle:
                if ci.get_coin_indicator().isvisible():
                    continue
                else:
                    ci.reinstate()
                    self.coin_indicator_index = self.coin_indicator_index + 1
