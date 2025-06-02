#!/bin/bash

clear
echo "=== Art Automation Setup ==="

SCRIPT_PATH="$(pwd)"  # usa o diretório atual como base

if [ ! -f "$SCRIPT_PATH/art.py" ]; then
  echo "[X] Arquivo art.py nao encontrado em $SCRIPT_PATH."
  echo "Execute esse script na pasta onde está o art.py, ou mova o script para essa pasta."
  read -p "Pressione ENTER para sair..."
  exit 1
fi

if ! command -v python3 &> /dev/null; then
  echo "[X] Python 3 nao encontrado no PATH."
  echo "Instale o Python 3.x e configure no PATH para continuar."
  read -p "Pressione ENTER para sair..."
  exit 1
fi

if ! command -v magick &> /dev/null; then
  echo "[!] ImageMagick (comando 'magick') nao encontrado no PATH."
  echo "Verifique se o ImageMagick está instalado."
fi

python3 "$SCRIPT_PATH/art.py" "$@"

echo
echo "[✓] Configuracao concluida com sucesso."
echo "Reinicie o terminal para aplicar alteracoes no PATH, se necessario."
read -p "Pressione ENTER para sair..."
