@echo off
setlocal ENABLEEXTENSIONS
title MagickArt - SpriteSheet Auto-Organizer

echo.
echo =========================================
echo                 MagickArt
echo =========================================
echo.

:: Get the directory where the .bat file is located
set "SCRIPT_DIR=%~dp0"

echo Searching for art.py...
echo.

:: Remove the trailing backslash if it exists
if "%SCRIPT_DIR:~-1%"=="\" (
    set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
)

:: Define the path to art.py
set "SCRIPT_PATH=%SCRIPT_DIR%\art.py"

:: Check if art.py exists
if not exist "%SCRIPT_PATH%" (
    echo [ERROR] art.py file not found at:
    echo    %SCRIPT_PATH%
    echo Run this script in the correct directory or move the .bat file to the right folder.
    pause
    exit /b 1
) else (
    echo [OK] art.py found at:
    echo    %SCRIPT_PATH%
)

echo.
echo Checking dependencies...
echo.

:: Check if Python is in the PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH. Install Python 3 and configure your PATH.
    pause
    exit /b 1
) else (
    echo [OK] Python found.
)

:: Check if ImageMagick (magick) is in the PATH
where magick >nul 2>&1
if errorlevel 1 (
    echo [ERROR] ImageMagick (magick) not found in PATH.
    pause
    exit /b 1
) else (
    echo [OK] ImageMagick found.
)

echo.
echo [OK] All dependencies verified.
echo.

:: Run the Python script with all passed arguments
cmd /k python "%SCRIPT_PATH%" %*

pause
endlocal
