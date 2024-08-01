@echo off
setlocal

rem Loop through the current directory and all subdirectories
for /r %%i in (*_Scaled*) do (
    echo %%i
)

endlocal
pause