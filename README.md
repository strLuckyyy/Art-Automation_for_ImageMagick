
# MagickArt - SpriteSheet Auto-Organizer 🗃️

## Goal 🎯

A Python utility to make it easier to organize sprites into subfolders and generate optimized spritesheets using **ImageMagick**, all automated. Focused on people working with 2D animations for games or any visual tool that involves a lot of frames.

---

## What does it do? 👀

* Organizes frames into subfolders based on name and interval. All set by you.
* Creates optimized spritesheets, always trying to keep a square (or near square) shape for better use and readability.
* Groups and compresses the spritesheets, with an option to include a base reference image if needed.
* Fully controlled via terminal.
* Free to edit or adapt for specific use cases.
* Works on **Windows** and **Linux**.

---

## Motivation 🤔

While working on the game StarDusk, which I'm currently developing, I had some issues with time vs. workload. So I started looking for faster ways to make the game’s animations.
After a lot of searching, I ended up using **Blender** for animations, with the cut-out technique, rendering everything and making the spritesheets with **ImageMagick**.
But organizing and compressing everything after rendering was still taking a lot of time, so I had the idea to automate it all to help speed things up.
With this automation, I managed to reduce the time spent organizing and compressing the sprites and spritesheets from an average of almost 4 hours to about 5 minutes.

---

## Requirements 🛑

* **Python 3.x** installed and set up in the system PATH.
* **ImageMagick** installed ([https://imagemagick.org/script/download.php](https://imagemagick.org/script/download.php)) and the `magick` command working in the terminal.
* The `art.bat` file available (inside the `/scripts` folder).

---

## Installing on Windows 🪟

1. **Clone the repository**

```bash
git clone https://github.com/strLuckyyy/MagickArt-SpriteSheet_Auto-Organizer.git
cd MagickArt-SpriteSheet_Auto-Organizer
```

2. **Add the cloned folder to the Windows PATH**

* Press `Win + R`, type `sysdm.cpl`, and press Enter.
* Go to the **Advanced** tab > **Environment Variables**.
* Under **System variables**, find `Path` and click **Edit**.
* Click **New** and add the folder path (like `C:\Art`).
* Confirm everything.

3. **Restart your terminal or PowerShell** so the PATH update works.

---

## Installing on Linux 🐧

1. **Clone the repository**

```bash
git clone https://github.com/strLuckyyy/MagickArt-SpriteSheet_Auto-Organizer.git
cd MagickArt-SpriteSheet_Auto-Organizer
```

2. **Give execute permission to the `art.sh` script**

```bash
chmod +x scripts/art.sh
```

3. **(Optional) Add the script to your PATH**

To use `art` from anywhere, you can either create a symbolic link or move the script to a folder that’s already in your PATH:

**Option 1 – Symbolic link (recommended):**

```bash
sudo ln -s $(pwd)/scripts/art.sh /usr/local/bin/art
```

**Option 2 – Move to `/usr/local/bin`:**

```bash
sudo cp scripts/art.sh /usr/local/bin/art
```

---

## How to use 🛠️

Once installed, you can run `art` from any folder using the terminal.
Just make sure you’re in the folder where your frames/sprites are.

For info and options, run:

```bash
art
OR
art -help
```

---
