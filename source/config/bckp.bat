@echo off
setlocal

:: Copyright (C) [2024] [Christian Marinkovich]
::
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with this program. If not, see <https://www.gnu.org/licenses/>.

rem echo off turns off the display of commands in the command window

rem Create a new directory named "bak" to store the backup
set "newDir=bak"
mkdir "%newDir%" > nul 2>&1

rem Iterate over files in the main directory and copy them to the backup directory
for %%I in ("%CD%\*.*") do (
    if /I NOT "%%~nxI"=="bckp.bat" (
        copy "%%I" "%newDir%\" > nul
    )
)

exit