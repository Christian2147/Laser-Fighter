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

from setup.SpriteSetup import machine_player
from setup.SpriteSetup import blue_machine
from setup.SpriteSetup import yellow_machine
from setup.SpriteSetup import red_machine
from setup.SpriteSetup import machine_boss
from setup.SpriteSetup import human_player
from setup.SpriteSetup import small_alien
from setup.SpriteSetup import medium_alien
from setup.SpriteSetup import large_alien
from setup.SpriteSetup import ufo
from setup.SpriteSetup import coin
from physics.MachineCollision import MachineCollision
from physics.AlienCollision import AlienCollision

machine_collision = MachineCollision(machine_player, blue_machine, yellow_machine, red_machine, machine_boss)

alien_collision = AlienCollision(human_player, small_alien, medium_alien, large_alien, ufo, coin)
