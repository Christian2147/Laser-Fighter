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