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

from components.enemy.AlienSmallAlien import SmallAlien
from components.enemy.AlienMediumAlien import MediumAlien
from components.enemy.AlienLargeAlien import LargeAlien
from components.enemy.AlienUFO import UFO


class SpawnSmallAlien:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_small_aliens = []
        self.small_aliens = []
        self.small_aliens_kill_values = []
        self.small_alien_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_small_aliens
        del self.small_aliens
        del self.small_aliens_kill_values
        del self.small_alien_index

    def spawn_small_alien(self, id):
        """
            Spawn a small alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        if len(self.all_small_aliens) <= len(self.small_aliens):
            small_alien = SmallAlien(id, self.scale_factor_x, self.scale_factor_y)
            self.small_aliens.append(small_alien)
            self.small_alien_index = self.small_alien_index + 1
            self.all_small_aliens.append(small_alien)
            self.small_aliens_kill_values.append(0)
        else:
            for sa in self.all_small_aliens:
                if sa.get_small_alien().isvisible():
                    continue
                else:
                    sa.reinstate(id)
                    self.small_aliens.append(sa)
                    self.small_alien_index = self.small_alien_index + 1
                    self.small_aliens_kill_values.append(0)
                    break


class SpawnMediumAlien:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_medium_aliens = []
        self.medium_aliens = []
        self.medium_aliens_kill_values = []
        self.medium_aliens_hit_values = []
        self.medium_alien_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_medium_aliens
        del self.medium_aliens
        del self.medium_aliens_kill_values
        del self.medium_aliens_hit_values
        del self.medium_alien_index

    def spawn_medium_alien(self, id):
        """
            Spawn a medium alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        if len(self.all_medium_aliens) <= len(self.medium_aliens):
            medium_alien = MediumAlien(id, self.scale_factor_x, self.scale_factor_y)
            self.medium_aliens.append(medium_alien)
            self.medium_alien_index = self.medium_alien_index + 1
            self.all_medium_aliens.append(medium_alien)
            self.medium_aliens_kill_values.append(0)
            self.medium_aliens_hit_values.append(0)
        else:
            for ma in self.all_medium_aliens:
                if ma.get_medium_alien().isvisible():
                    continue
                else:
                    ma.reinstate(id)
                    self.medium_aliens.append(ma)
                    self.medium_alien_index = self.medium_alien_index + 1
                    self.medium_aliens_kill_values.append(0)
                    self.medium_aliens_hit_values.append(0)
                    break


class SpawnLargeAlien:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_large_aliens = []
        self.large_aliens = []
        self.large_aliens_kill_values = []
        self.large_aliens_hit_values = []
        self.large_alien_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_large_aliens
        del self.large_aliens
        del self.large_aliens_kill_values
        del self.large_aliens_hit_values
        del self.large_alien_index

    def spawn_large_alien(self, id):
        """
            Spawn a large alien with the given id on the screen.

            :param id: The id that the alien should have (Determines initial location of the alien)
            :type id: int

            :return: None
        """

        if len(self.all_large_aliens) <= len(self.large_aliens):
            large_alien = LargeAlien(id, self.scale_factor_x, self.scale_factor_y)
            self.large_aliens.append(large_alien)
            self.large_alien_index = self.large_alien_index + 1
            self.all_large_aliens.append(large_alien)
            self.large_aliens_kill_values.append(0)
            self.large_aliens_hit_values.append(0)
        else:
            for la in self.all_large_aliens:
                if la.get_large_alien().isvisible():
                    continue
                else:
                    la.reinstate(id)
                    self.large_aliens.append(la)
                    self.large_alien_index = self.large_alien_index + 1
                    self.large_aliens_kill_values.append(0)
                    self.large_aliens_hit_values.append(0)
                    break


class SpawnUFO:
    def __init__(self, scale_factor_x, scale_factor_y):
        self.all_ufos = []
        self.ufos = []
        self.ufo_kill_value = 0
        self.ufo_hit_value = 0
        self.ufo_index = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        del self.all_ufos
        del self.ufos
        del self.ufo_kill_value
        del self.ufo_hit_value
        del self.ufo_index

    def spawn_alien_boss(self):
        """
            Spawn an alien UFO on the screen.

            :return: None
        """

        if len(self.all_ufos) <= len(self.ufos):
            spawn_ufo = UFO(self.scale_factor_x, self.scale_factor_y)
            self.ufos.append(spawn_ufo)
            self.ufo_index = self.ufo_index + 1
            self.all_ufos.append(spawn_ufo)
        else:
            for u in self.all_ufos:
                if u.get_ufo().isvisible():
                    continue
                else:
                    u.reinstate()
                    self.ufos.append(u)
                    self.ufo_index = self.ufo_index + 1
                    break
