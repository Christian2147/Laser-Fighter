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

rem Clean Up File:
rem Purpose: Clean up all of the duplicate scaled texture files from the texture folder.

@echo off
setlocal

rem Change to the directory where the batch script is located.
rem WARNING: Do NOT move the batch script to ANY other directory. This could cause unintended side effects!
rem I am not responsible for any damage caused my misuse of this file!
cd /d "%~dp0"

rem Create Deletion Log File
set "logfile=deletion_log.txt"
echo Deletion Log - %date% %time% > "%logfile%"

rem Loop through the current directory and all subdirectories
for /r %%i in (*_Scaled*) do (
    echo Deleting: %%i
    echo %%i >> "%logfile%"
    del "%%i"
)

endlocal
pause