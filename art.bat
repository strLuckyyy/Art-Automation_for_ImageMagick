@echo off
setlocal ENABLEEXTENSIONS
title Art Automation Setup

:: Pega o diretório onde o .bat está localizado
set "SCRIPT_DIR=%~dp0"

:: Remove a barra final (opcional, só pra ficar bonito)
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

:: Define o caminho para o art.py - aqui assumindo que está na mesma pasta do .bat
set "SCRIPT_PATH=%SCRIPT_DIR%\art.py"

:: Verifica se art.py existe
if not exist "%SCRIPT_PATH%" (
    echo [X] Arquivo art.py nao encontrado em:
    echo    %SCRIPT_PATH%
    echo Execute esse script no diretorio correto ou mova o .bat para a pasta certa.
    pause
    exit /b 1
)

:: Verifica se python está no PATH
where python >nul 2>nul
if errorlevel 1 (
    echo [X] Python nao encontrado no PATH. Instale o Python 3 e configure o PATH.
    pause
    exit /b 1
)

:: Verifica se ImageMagick está no PATH (comando magick)
where magick >nul 2>nul
if errorlevel 1 (
    echo [!] ImageMagick (comando magick) nao encontrado no PATH.
    echo Verifique se o ImageMagick esta instalado.
)

:: Executa o script Python com todos os argumentos recebidos
python "%SCRIPT_PATH%" %*

echo.
echo [✓] Configuracao concluida com sucesso.
echo Reinicie o terminal para aplicar alteracoes no PATH, se necessario.

pause
