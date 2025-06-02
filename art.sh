#!/bin/bash
# MagickArt - Automatic SpriteSheet Builder

echo
echo "========================================="
echo "                MagickArt                "
echo "       SpriteSheet  Auto-Organizer       "
echo "========================================="
echo

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Searching for art.py..."
echo

# Full path to art.py
SCRIPT_PATH="$SCRIPT_DIR/art.py"

# Check if art.py exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "[ERROR] art.py file not found at:"
    echo "    $SCRIPT_PATH"
    echo "Run this script in the correct directory or move the .sh to the right folder."
    read -p "Press Enter to exit..."
    exit 1
else
    echo "[OK] art.py found at:"
    echo "    $SCRIPT_PATH"
fi

echo
echo "Checking dependencies..."
echo

# Check if python is available
if ! command -v python3 &>/dev/null; then
    echo "[ERROR] Python3 not found in PATH. Install Python 3 and configure your PATH."
    read -p "Press Enter to exit..."
    exit 1
else
    echo "[OK] Python found."
fi

# Check if ImageMagick (magick) is available
if ! command -v magick &>/dev/null; then
    echo "[ERROR] ImageMagick (magick) not found in PATH."
    read -p "Press Enter to exit..."
    exit 1
else
    echo "[OK] ImageMagick found."
fi

echo
echo "[OK] Dependencies verified."
echo

# Run the Python script with passed arguments
python3 "$SCRIPT_PATH" "$@"

# Wait for user input before closing (optional)
read -p "Press Enter to finish..."
