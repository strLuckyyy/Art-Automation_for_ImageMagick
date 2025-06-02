@echo off
setlocal ENABLEEXTENSIONS
title Art Automation Setup

echo.
echo =========================================
echo Art Automation Setup
echo =========================================
echo.
:: Pega o diretirio onde o .bat está localizado
set "SCRIPT_DIR=%~dp0"

echo Localizando art.py...
echo.

:: Remove a barra final
if "%SCRIPT_DIR:~-1%"=="\" (
    set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
)

:: Define o caminho para o art.py
set "SCRIPT_PATH=%SCRIPT_DIR%\art.py"

:: Verifica se art.py existe
if not exist "%SCRIPT_PATH%" (
    echo [X] Arquivo art.py nao encontrado em:
    echo    %SCRIPT_PATH%
    echo Execute esse script no diretorio correto ou mova o .bat para a pasta certa.
    pause
    exit /b 1
) else (
    echo [v] art.py encontrado em:
    echo    %SCRIPT_PATH%
)


echo Verificando dependencias...
echo.

:: Verifica se python esta no PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo [x] Python nao encontrado no PATH. Instale o Python 3 e configure o PATH.
    pause
    exit /b 1
) else (
    echo [v] Python encontrado.
)

where magick >nul 2>&1
if errorlevel 1 (
    echo magick nao encontrado no PATH.
    pause
    exit /b 1
) else (
    echo [v] ImageMagick encontrado.
)

echo [v] Dependencias verificadas.

:: Executa o script Python com todos os argumentos recebidos
python "%SCRIPT_PATH%" %*

pause
endlocal
