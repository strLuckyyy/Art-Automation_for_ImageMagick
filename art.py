import os
import sys
import shutil
import math
import subprocess
from zipfile import ZipFile

def check_imagemagick():
    try:
        result = subprocess.run(
            ["magick", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0 and "ImageMagick" in result.stdout:
            print("[✓] ImageMagick found.")
            return True
        else:
            print("[✗] ImageMagick not found or there's a problem with the installation.")
            return False

    except FileNotFoundError:
        print("[✗] The 'magick' command wasn't found. Make sure ImageMagick is installed and in the PATH.")
        return False


def create_folder(path):
    os.makedirs(path, exist_ok=True)


def move_frames(folder_name, start, end, root):
    dest = os.path.join(root, folder_name)
    create_folder(dest)

    print(f"[•] Moving frames from {start} to {end} into folder: {folder_name}")
    for i in range(start, end + 1):
        filename = f"{i:04}.png"
        src = os.path.join(root, filename)
        if os.path.isfile(src):
            shutil.move(src, os.path.join(dest, filename))
        else:
            print(f"[!] Frame not found: {filename}")


def calculate_grid(n):
    side = math.sqrt(n)
    rows = math.floor(side)
    cols = math.ceil(n / rows)
    best_rows, best_cols = rows, cols
    best_diff = abs(cols - rows)

    for r in range(rows + 1, cols + 1):
        c = math.ceil(n / r)
        diff = abs(c - r)
        if c * r >= n and diff < best_diff:
            best_diff = diff
            best_rows = r
            best_cols = c

    return best_cols, best_rows


def create_spritesheets(root, sprite_name):
    for folder_name in os.listdir(root):
        path = os.path.join(root, folder_name)

        if os.path.isdir(path):
            png_files = [f for f in os.listdir(path) if f.endswith(".png")]
            if not png_files:
                continue

            total = len(png_files)
            cols, rows = calculate_grid(total)
            tile = f"{cols}x{rows}"
            output_name = f"SS_{sprite_name}-{folder_name}.png"
            command = [
                "magick", "montage", "*",
                "-geometry", "1024x1024",
                "-tile", tile,
                "-background", "transparent",
                "-filter", "Catrom",
                output_name
            ]

            print(f"[→] Generating spritesheet: {output_name} with {tile}...")
            subprocess.run(" ".join(command), cwd=path, shell=True)


def zip_folder(folder, zip_name):
    zip_path = os.path.join(os.getcwd(), f"{zip_name}.zip")

    with ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder)
                zipf.write(abs_path, rel_path)
    print(f"[✓] Folder zipped: {zip_path}")


def organize_and_zip(zip_folder_name, base_sprite=None, new_name=None):
    root = os.getcwd()
    zip_path = os.path.join(root, zip_folder_name)
    create_folder(zip_path)
    print(f"[•] Creating organization folder: {zip_folder_name}")

    # Move spritesheets
    for folder_name in os.listdir(root):
        path = os.path.join(root, folder_name)
        if os.path.isdir(path):
            for file in os.listdir(path):
                if file.startswith("SS_") and file.endswith(".png"):
                    src = os.path.join(path, file)
                    dest = os.path.join(zip_path, file)
                    shutil.move(src, dest)
                    print(f"[✓] Spritesheet moved: {file}")

    # Move base sprite
    if base_sprite:
        base_path = os.path.join(root, base_sprite)
        if os.path.isfile(base_path):
            final_name = new_name if new_name else base_sprite
            dest = os.path.join(zip_path, final_name)
            shutil.move(base_path, dest)
            print(f"[✓] Base sprite moved: {base_sprite} → {final_name}")
        else:
            print(f"[!] Base sprite '{base_sprite}' not found.")

    zip_folder(zip_path, zip_folder_name)


def show_help():
    print("""\n\n
=========================================
                MagickArt
       SpriteSheet Auto-Organizer 
=========================================

Available commands:

1- Split and generate spritesheets:
Usage:
    > art <SpriteName> <N> <Name1> <Start1> <End1> <Name2> <Start2> <End2> ...
Example:
    > art Player 3 Idle 1 20 Walk 21 60 Run 61 90

What it does:
- Splits the frames based on given intervals and moves them to subfolders.
- Generates spritesheets inside those folders using ImageMagick.
- Output name format: SS_<SpriteName>-<FolderName>.png

⚠️ IMPORTANT:
- Make sure ImageMagick is installed and accessible from the terminal.

------------------------------------------------------------

2- Organize, move base sprite and zip:
Usage:
    > art -oaz <ZipFolderName> [BaseSprite] [NewBaseSpriteName]
Examples:
    > art -oaz PlayerZip                                  # Just moves the spritesheets to PlayerZip and zips it.
    > art -oaz PlayerZip SpriteBase.png                   # Moves the base sprite as is.
    > art -oaz PlayerZip SpriteBase.png NewNameSB.png     # Renames the base sprite when moving.

What it does:
- Creates folder <ZipFolderName>.
- Moves all SS_*.png files from subfolders there.
- Moves the base sprite (if provided), renaming it if needed.
- Creates a zip file <ZipFolderName>.zip with everything.

Base sprite is useful in case you need a specific reference or template for the project.

------------------------------------------------------------

3- Help:
Usage:
    > art -help
    > art --help

------------------------------------------------------------
""")


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-help", "--help"):
        show_help()
        return

    if args[0] == "-oaz":
        if len(args) >= 2:
            zip_name = args[1]
            base_sprite = args[2] if len(args) >= 3 else None
            new_name = args[3] if len(args) >= 4 else None
            organize_and_zip(zip_name, base_sprite, new_name)
        else:
            print("[!] Incorrect usage of the -oaz command. Use -help for more info.")
        return

    if not check_imagemagick():
        print("[!] Cancelling spritesheet generation.")
        return

    try:
        sprite_name = args[0]
        quantity = int(args[1])
        arguments = args[2:]
        current_folder = os.getcwd()

        for i in range(quantity):
            name = arguments[i * 3]
            start = int(arguments[i * 3 + 1])
            end = int(arguments[i * 3 + 2])
            move_frames(name, start, end, current_folder)
            print(f"[✓] {name}: frames {start} to {end} moved to {name}/")

        create_spritesheets(current_folder, sprite_name)
    except (IndexError, ValueError):
        print("[X] Error with arguments. Use 'art -help' to check correct syntax.")


if __name__ == "__main__":
    main()
