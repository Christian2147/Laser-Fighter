#!/bin/bash

# bckp.sh: backup configuration files
# This is a port of bckp.bat to Bash. Backs up configuration files.
#
# Copyright (C) [2024] [Christian Marinkovich]
# Copyright (C) 2024 yosoyducc
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

# create the new directory
newDir="bak"
mkdir -p "${newDir}"
if [ $? -ne 0 ]; then
    echo "bckp.sh: WARNING: failed to create backup dir. Check permissions."
fi

# copy files to backup
cp *.ini "${newDir}"
if [ $? -ne 0 ]; then
    echo "bckp.sh: ERROR: couldn't back up config files"
fi

exit 0

