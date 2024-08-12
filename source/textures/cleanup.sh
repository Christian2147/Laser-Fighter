#!/bin/bash

# cleanup.sh: Clean up all of the duplicate scaled texture files from the texture folder.
# This is a port of cleanup.bat to Bash.
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

# change to script dir
# WARNING: don't move this script anywhere else. This could cause unintended side effects!
# I am not responsible for any damage caused my misuse of this file!
cd "$(dirname "$0")"

# Ensure the script is running in the "textures" directory
if [ "$(basename "$PWD")" != "textures" ]; then
    echo "cleanup.sh: FATAL: This script must be run from a directory named 'textures'."
    exit 1
fi

# Check this directory's write permission
if [ ! -r . ] || [ ! -w . ]; then
    echo "cleanup.sh: FATAL: no permission to read and/or write to textures dir"
fi

# Create deletion log file.
logfile="deletion_log.txt"
echo "Deletion Log - $(date +"%Y-%m-%d %H:%M:%S")" > $logfile

# Find all scaled textures and erase them.
find -type f -iname "*_Scaled*" | while read -r line; do
    echo "Deleting: ${line}"
    echo $line >> $logfile
    rm $line
done

exit 0

