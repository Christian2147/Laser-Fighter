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

from setup.WindowSetup import scale_factor_X
from setup.WindowSetup import scale_factor_Y


class AlienCollision:
    SMALL_ALIEN_Y_RANGE = (-193 * scale_factor_Y, -88 * scale_factor_Y)
    MEDIUM_ALIEN_Y_RANGE = (-196 * scale_factor_Y, -52 * scale_factor_Y)
    LARGE_ALIEN_Y_RANGE = (-197 * scale_factor_Y, 27 * scale_factor_Y)
    UFO_Y_RANGE = (-92 * scale_factor_Y, 52 * scale_factor_Y)

    SMALL_ALIEN_X_DISTANCE = 26 * scale_factor_X
    MEDIUM_ALIEN_X_DISTANCE = 36 * scale_factor_X
    LARGE_ALIEN_X_DISTANCE = 50 * scale_factor_X
    UFO_X_DISTANCE = 53 * scale_factor_X

    PLAYER_LASER_GAP = 30 * scale_factor_X

    def __init__(self, human_player, small_alien, medium_alien, large_alien, ufo, coin):
        self._human_player = human_player
        self._small_alien = small_alien
        self._medium_alien = medium_alien
        self._large_alien = large_alien
        self._ufo = ufo
        self._coin = coin

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._human_player
        del self._small_alien
        del self._medium_alien
        del self._large_alien
        del self._ufo
        del self._coin

    def calculate_collision(self):
        for h in self._human_player.current_human:
            for sa in self._small_alien.small_aliens:
                sa.got_hit = 0
                if sa.get_small_alien().xcor() - self.SMALL_ALIEN_X_DISTANCE >= (h.get_player().xcor() + self.PLAYER_LASER_GAP) or \
                        (sa.get_small_alien().xcor() - self.SMALL_ALIEN_X_DISTANCE < (h.get_player().xcor() - self.PLAYER_LASER_GAP) < sa.get_small_alien().xcor() + self.SMALL_ALIEN_X_DISTANCE and h.direction == 2):
                    sa.collision_point = -1
                else:
                    sa.collision_point = 1
                if h.get_player().xcor() > sa.get_small_alien().xcor() + (self.SMALL_ALIEN_X_DISTANCE * sa.collision_point):
                    sa.already_ahead = 1
                else:
                    sa.already_ahead = 0
                if h.get_player().xcor() < sa.get_small_alien().xcor() + (self.SMALL_ALIEN_X_DISTANCE * sa.collision_point):
                    sa.already_behind = 1
                else:
                    sa.already_behind = 0
            for ma in self._medium_alien.medium_aliens:
                ma.got_hit = 0
                if ma.get_medium_alien().xcor() - self.MEDIUM_ALIEN_X_DISTANCE >= (h.get_player().xcor() + self.PLAYER_LASER_GAP) or \
                        (ma.get_medium_alien().xcor() - self.MEDIUM_ALIEN_X_DISTANCE < (h.get_player().xcor() - self.PLAYER_LASER_GAP) < ma.get_medium_alien().xcor() + self.MEDIUM_ALIEN_X_DISTANCE and h.direction == 2):
                    ma.collision_point = -1
                else:
                    ma.collision_point = 1
                if h.get_player().xcor() > ma.get_medium_alien().xcor() + (self.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point):
                    ma.already_ahead = 1
                else:
                    ma.already_ahead = 0
                if h.get_player().xcor() < ma.get_medium_alien().xcor() + (self.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point):
                    ma.already_behind = 1
                else:
                    ma.already_behind = 0
            for la in self._large_alien.large_aliens:
                la.got_hit = 0
                if la.get_large_alien().xcor() - self.LARGE_ALIEN_X_DISTANCE >= (h.get_player().xcor() + self.PLAYER_LASER_GAP) or \
                        (la.get_large_alien().xcor() - self.LARGE_ALIEN_X_DISTANCE < (h.get_player().xcor() - self.PLAYER_LASER_GAP) < la.get_large_alien().xcor() + self.LARGE_ALIEN_X_DISTANCE and h.direction == 2):
                    la.collision_point = -1
                else:
                    la.collision_point = 1
                if h.get_player().xcor() > la.get_large_alien().xcor() + (self.LARGE_ALIEN_X_DISTANCE * la.collision_point):
                    la.already_ahead = 1
                else:
                    la.already_ahead = 0
                if h.get_player().xcor() < la.get_large_alien().xcor() + (self.LARGE_ALIEN_X_DISTANCE * la.collision_point):
                    la.already_behind = 1
                else:
                    la.already_behind = 0
            for u in self._ufo.ufos:
                u.got_hit = 0
                if u.get_ufo().xcor() - self.UFO_X_DISTANCE >= (h.get_player().xcor() + self.PLAYER_LASER_GAP) or \
                        (u.get_ufo().xcor() - self.UFO_X_DISTANCE < (h.get_player().xcor() - self.PLAYER_LASER_GAP) < u.get_ufo().xcor() + self.UFO_X_DISTANCE and h.direction == 2):
                    u.collision_point = -1
                else:
                    u.collision_point = 1
                if h.get_player().xcor() > u.get_ufo().xcor() + (self.UFO_X_DISTANCE * u.collision_point):
                    u.already_ahead = 1
                else:
                    u.already_ahead = 0
                if h.get_player().xcor() < u.get_ufo().xcor() + (self.UFO_X_DISTANCE * u.collision_point):
                    u.already_behind = 1
                else:
                    u.already_behind = 0

            for c in self._coin.coins_on_screen_list:
                if h.direction == 1:
                    if h.get_player().xcor() + self.PLAYER_LASER_GAP > c.coin.xcor():
                        c.relative_laser_position = 1
                    else:
                        c.relative_laser_position = -1
                elif h.direction == 2:
                    if h.get_player().xcor() - self.PLAYER_LASER_GAP > c.coin.xcor():
                        c.relative_laser_position = 1
                    else:
                        c.relative_laser_position = -1
