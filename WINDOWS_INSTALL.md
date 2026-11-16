# Install PScreenRec on Windows

[English](WINDOWS_INSTALL.md) · [Русский](WINDOWS_INSTALL.ru.md)

Windows 10 / 11, x64, Photoshop 2024 (25.0) or newer. Choose one installation method below. Both include the same independent plugin and local helper; Python is included.

## Direct install

1. Save your drawings and close Photoshop.
2. [Download the direct installer](https://github.com/JazzyXP/PScreenRec/releases/download/v0.5.9/PScreenRec-0.5.9-Setup.exe), run it and follow the prompts.
3. Open Photoshop → **Plugins → PScreenRec → PScreenRec**.
4. Enable **Record this document**. Use **Record new documents** to automatically record future new files.

Creative Cloud Desktop and UXP Developer Tool are not required. The initial FFmpeg download requires internet access.

## Install via Adobe CC

1. Install Creative Cloud Desktop and Photoshop, and sign in to Creative Cloud.
2. Save your drawings and close Photoshop.
3. [Download the CC installer](https://github.com/JazzyXP/PScreenRec/releases/download/v0.5.9/PScreenRec-0.5.9-Setup-CC.exe), run it and follow the prompts.
4. Open Photoshop → **Plugins → PScreenRec → PScreenRec** and enable **Record this document**.

This uses Adobe's installation mechanism; it does not require a published Marketplace listing. The initial FFmpeg download requires internet access.

## Updating and recordings

Close Photoshop and run the chosen installer over the previous version. Recordings and settings are preserved; uninstalling first is not necessary. Do not run independent and Marketplace panels together.

Save your drawing as PSD/PSB after starting recording to continue the same timelapse later. Keep your recording data folder. If the panel requests a connection file, select `%LOCALAPPDATA%\ProcessRecorder\connection.json`; never share this file.

For large canvases, use **High** to reduce capture load. The panel uses English or Russian according to Photoshop.

[Back to PScreenRec](README.md)
