# PScreenRec Helper for Adobe Marketplace

This guide is for the Windows UXP plugin installed from Adobe Creative Cloud Marketplace. The Marketplace plugin requires a local helper for storing frames and encoding MP4 videos.

The Marketplace helper installer is separate from the complete independent installer on the main project page. It does not install, sideload or remove a Photoshop plugin. Do not use the independent installer as the Marketplace companion installer.

## Install

1. Install PScreenRec from Adobe Creative Cloud Marketplace.
2. Save your drawings and close Photoshop.
3. [Download PScreenRec Helper for Windows x64](https://github.com/JazzyXP/PScreenRec/raw/refs/heads/main/downloads/PScreenRec-Helper-Setup.exe) and run it. [SHA-256](downloads/PScreenRec-Helper-Setup.exe.sha256). Python is included. The first FFmpeg download needs an internet connection.
4. Open Photoshop → Plugins → PScreenRec → PScreenRec.
5. If the panel requests a connection file, choose **Connection…** and select `%LOCALAPPDATA%\ProcessRecorder\connection.json`.

Enable **Record this document** to capture the current drawing. On large canvases, **High** is recommended over Original to reduce capture cost.

## Existing independent installation

The Marketplace plugin and the independent plugin have different Adobe plugin IDs. Do not run both panels at once: both use the same local helper and can record duplicate frames. Keep your data folder and configuration if moving between channels; no recording-folder deletion is needed.

## Uninstall

Remove the Marketplace plugin through Creative Cloud Desktop. Remove PScreenRec Helper through Windows Installed apps after saving your work and closing Photoshop. The recordings folder is preserved; delete recordings yourself only if you no longer need them.

Support: denp90@gmail.com. Never attach your connection token to a public issue.

The helper installer has no tip or payment button. All recording and export features are available without payment.
