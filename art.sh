#!/bin/bash
# MagickArt - Automatic SpriteSheet Builder

echo
echo "========================================="
echo "               MagickArt"
echo "========================================="
echo

# Obtém o diretório do script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Localizando art.py..."
echo

# Caminho completo para art.py
SCRIPT_PATH="$SCRIPT_DIR/art.py"

# Verifica se art.py existe
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "[X] Arquivo art.py nao encontrado em:"
    echo "    $SCRIPT_PATH"
    echo "Execute esse script no diretorio correto ou mova o .sh para a pasta certa."
    read -p "Pressione Enter para sair..."
    exit 1
else
    echo "[v] art.py encontrado em:"
    echo "    $SCRIPT_PATH"
fi

echo
echo "Verificando dependencias..."
echo

# Verifica se python está disponível
if ! command -v python3 &>/dev/null; then
    echo "[x] Python3 nao encontrado no PATH. Instale o Python 3 e configure o PATH."
    read -p "Pressione Enter para sair..."
    exit 1
else
    echo "[v] Python encontrado."
fi

# Verifica se ImageMagick (magick) está disponível
if ! command -v magick &>/dev/null; then
    echo "[x] ImageMagick (magick) nao encontrado no PATH."
    read -p "Pressione Enter para sair..."
    exit 1
else
    echo "[v] ImageMagick encontrado."
fi

echo
echo "[v] Dependencias verificadas."
echo

# Executa o script Python com os argumentos recebidos
python3 "$SCRIPT_PATH" "$@"

# Aguarda o usuário pressionar Enter antes de fechar (opcional)
read -p "Pressione Enter para finalizar..."
