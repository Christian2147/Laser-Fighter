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
    File: AlienCollision.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the logic for calculating collisions in Alien Mode.
"""


class AlienCollision:
    """
        Represents Alien Collision Calculations in Laser Fighter.

        Class Variables:
            SMALL_ALIEN_Y_RANGE (tuple): Stores the y axis range in which the laser has to be in order to hit a small
                alien.
            MEDIUM_ALIEN_Y_RANGE (tuple): Stores the y axis range in which the laser has to be in order to hit a medium
                alien.
            LARGE_ALIEN_Y_RANGE (tuple): Stores the y axis range in which the laser has to be in order to hit a large
                alien.
            UFO_Y_RANGE (tuple): Stores the y axis range in which the laser has to be in order to hit the UFO.

            SMALL_ALIEN_X_DISTANCE (float): Stores the distance away from the center of the Small Alien that the laser
                can be on the x-axis in order to still hit the Alien.
            MEDIUM_ALIEN_X_DISTANCE (float): Stores the distance away from the center of the Medium Alien that the laser
                can be on the x-axis in order to still hit the Alien.
            LARGE_ALIEN_X_DISTANCE (float): Stores the distance away from the center of the Large Alien that the laser
                can be on the x-axis in order to still hit the Alien.
            UFO_X_DISTANCE (float): Stores the distance away from the center of the UFO that the laser
                can be on the x-axis in order to still hit the Alien.

            PLAYER_LASER_GAP (float): The gap between the starting point of the laser and the player.

        Pointers:
            _human_player (SpawnHumanPlayer()): A pointer to the human player object
            _small_alien (SpawnSmallAlien()): A pointer to the small alien object
            _medium_alien (SpawnMediumAlien()): A pointer to the medium alien object
            _large_alien (SpawnLargeAlien()): A pointer to the large alien object
            _ufo (SpawnUFO()): A pointer to the UFO object
            _coin (SpawnCoin()): A pointer to the coin object
    """

    def __init__(self,
                 human_player,
                 small_alien,
                 medium_alien,
                 # large_alien,
                 # ufo,
                 coin,
                 scale_factor_x,
                 scale_factor_y
    ):
        """
            Represents the hitboxes in Alien Mode.

            :param human_player: A pointer to the human player object
            :type human_player: SpawnHumanPlayer()

            :param small_alien: A pointer to the small alien object
            :type small_alien: SpawnSmallAlien()

            :param medium_alien: A pointer to the medium alien object
            :type medium_alien: SpawnMediumAlien()

            :param large_alien: A pointer to the large alien object
            :type large_alien: SpawnLargeAlien()

            :param ufo: A pointer to the UFO object
            :type ufo: SpawnUFO()

            :param coin: A pointer to the coin object
            :type coin: SpawnCoin()
        """

        self.SMALL_ALIEN_Y_RANGE = (448 * scale_factor_y, 553 * scale_factor_y)
        self.MEDIUM_ALIEN_Y_RANGE = (412 * scale_factor_y, 556 * scale_factor_y)
        self.LARGE_ALIEN_Y_RANGE = (333 * scale_factor_y, 557 * scale_factor_y)
        self.UFO_Y_RANGE = (308 * scale_factor_y, 452 * scale_factor_y)

        self.SMALL_ALIEN_X_DISTANCE = 26 * scale_factor_x
        self.MEDIUM_ALIEN_X_DISTANCE = 36 * scale_factor_x
        self.LARGE_ALIEN_X_DISTANCE = 50 * scale_factor_x
        self.UFO_X_DISTANCE = 53 * scale_factor_x

        self.PLAYER_LASER_GAP = 30 * scale_factor_x

        self._human_player = human_player
        self._small_alien = small_alien
        self._medium_alien = medium_alien
        # self._large_alien = large_alien
        # self._ufo = ufo
        self._coin = coin

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._human_player
        del self._small_alien
        del self._medium_alien
        # del self._large_alien
        # del self._ufo
        del self._coin
        del self.scale_factor_x
        del self.scale_factor_y

    def calculate_collision(self):
        """
            Calculates the collision hitboxes for Alien Mode based on the new laser that was just fired.

            :return: None
        """

        for h in self._human_player.current_human:
            # Each Small Aliens Hitbox is calculated
            for sa in self._small_alien.small_aliens:
                # Make sure that the alien is not dying before resetting its status as being hit
                if sa.death_animation == 0:
                    sa.got_hit = 0
                # If the collision lines for the Alien should be on the left (-1) or right (1) side
                # Depends where the player is relative to the Alien.
                if sa.rect.centerx - self.SMALL_ALIEN_X_DISTANCE >= (h.rect.centerx + self.PLAYER_LASER_GAP) or \
                        (sa.rect.centerx - self.SMALL_ALIEN_X_DISTANCE < (h.rect.centerx - self.PLAYER_LASER_GAP) < sa.rect.centerx + self.SMALL_ALIEN_X_DISTANCE and h.direction == "left"):
                    sa.collision_point = -1
                else:
                    sa.collision_point = 1
                # If the player already has a greater x coordinate than the collision line
                if h.rect.centerx > sa.rect.centerx + (self.SMALL_ALIEN_X_DISTANCE * sa.collision_point):
                    sa.already_ahead = 1
                else:
                    sa.already_ahead = 0
                # If the player already has a smaller x coordinate than the collision line
                if h.rect.centerx < sa.rect.centerx + (self.SMALL_ALIEN_X_DISTANCE * sa.collision_point):
                    sa.already_behind = 1
                else:
                    sa.already_behind = 0

            # Each Medium Aliens Hitbox is calculated
            for ma in self._medium_alien.medium_aliens:
                if ma.death_animation == 0:
                    ma.got_hit = 0
                if ma.rect.centerx - self.MEDIUM_ALIEN_X_DISTANCE >= (h.rect.centerx + self.PLAYER_LASER_GAP) or \
                        (ma.rect.centerx - self.MEDIUM_ALIEN_X_DISTANCE < (h.rect.centerx - self.PLAYER_LASER_GAP) < ma.rect.centerx + self.MEDIUM_ALIEN_X_DISTANCE and h.direction == 2):
                    ma.collision_point = -1
                else:
                    ma.collision_point = 1
                if h.rect.centerx > ma.rect.centerx + (self.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point):
                    ma.already_ahead = 1
                else:
                    ma.already_ahead = 0
                if h.rect.centerx < ma.rect.centerx + (self.MEDIUM_ALIEN_X_DISTANCE * ma.collision_point):
                    ma.already_behind = 1
                else:
                    ma.already_behind = 0

            # # Each Large Aliens Hitbox is calculated
            # for la in self._large_alien.large_aliens:
            #     if la.death_animation == 0:
            #         la.got_hit = 0
            #     if la.rect.centerx - self.LARGE_ALIEN_X_DISTANCE >= (h.rect.centerx + self.PLAYER_LASER_GAP) or \
            #             (la.rect.centerx - self.LARGE_ALIEN_X_DISTANCE < (h.rect.centerx - self.PLAYER_LASER_GAP) < la.rect.centerx + self.LARGE_ALIEN_X_DISTANCE and h.direction == 2):
            #         la.collision_point = -1
            #     else:
            #         la.collision_point = 1
            #     if h.rect.centerx > la.rect.centerx + (self.LARGE_ALIEN_X_DISTANCE * la.collision_point):
            #         la.already_ahead = 1
            #     else:
            #         la.already_ahead = 0
            #     if h.rect.centerx < la.rect.centerx + (self.LARGE_ALIEN_X_DISTANCE * la.collision_point):
            #         la.already_behind = 1
            #     else:
            #         la.already_behind = 0
            #
            # # Each UFOs Hitbox is calculated
            # for u in self._ufo.ufos:
            #     if u.death_animation == 0:
            #         u.got_hit = 0
            #     if u.rect.centerx - self.UFO_X_DISTANCE >= (h.rect.centerx + self.PLAYER_LASER_GAP) or \
            #             (u.rect.centerx - self.UFO_X_DISTANCE < (h.rect.centerx - self.PLAYER_LASER_GAP) < u.rect.centerx + self.UFO_X_DISTANCE and h.direction == 2):
            #         u.collision_point = -1
            #     else:
            #         u.collision_point = 1
            #     if h.rect.centerx > u.rect.centerx + (self.UFO_X_DISTANCE * u.collision_point):
            #         u.already_ahead = 1
            #     else:
            #         u.already_ahead = 0
            #     if h.rect.centerx < u.rect.centerx + (self.UFO_X_DISTANCE * u.collision_point):
            #         u.already_behind = 1
            #     else:
            #         u.already_behind = 0

            # Each Coins Hitbox is calculated
            for c in self._coin.coins_on_screen_list:
                # If the player is facing right (1) or left (2)
                if h.direction == "right":
                    # If the player is ahead (1) or behind (-1) the coin hit box
                    if h.rect.centerx + self.PLAYER_LASER_GAP > c.rect.centerx:
                        c.relative_laser_position = 1
                    else:
                        c.relative_laser_position = -1
                elif h.direction == "left":
                    if h.rect.centerx - self.PLAYER_LASER_GAP > c.rect.centerx:
                        c.relative_laser_position = 1
                    else:
                        c.relative_laser_position = -1
                c.just_fired = 1
