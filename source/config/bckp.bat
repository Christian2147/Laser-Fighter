@echo off
setlocal
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