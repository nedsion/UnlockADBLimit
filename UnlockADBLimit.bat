@echo off
setlocal

REM Kill the ADB server
powershell Start-Process adb -ArgumentList "kill-server" -Verb RunAs

REM Set the variable name and value
set VARIABLE_NAME=ADB_LOCAL_TRANSPORT_MAX_PORT
set VARIABLE_VALUE=7000

REM Add the variable to the user environment
powershell -Command [Environment]::SetEnvironmentVariable('%VARIABLE_NAME%', '%VARIABLE_VALUE%', 'User')

echo Variable added to user environment: %VARIABLE_NAME%=%VARIABLE_VALUE%

endlocal
