# PScreenRec Helper for Adobe Marketplace

This guide is for the Windows UXP plugin installed from Adobe Creative Cloud Marketplace. The Marketplace plugin requires a local helper for storing frames and encoding MP4 videos.

This edition is being prepared for Adobe review and is not yet published in the Marketplace. During review, use the separately supplied Marketplace CCX. A directly installed CCX is not evidence of Marketplace approval.

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

The helper installer has no tip or payment button. All recording and export features are available without payment. Adobe's review team confirmed on 11 November 2026 that optional non-blocking support links are permitted; no payment is needed for any feature.

## Mac (Apple Silicon)

The Mac Marketplace candidate is 0.5.13 and requires macOS 15+, Photoshop 27.10+ and the separate [Mac helper 0.5.10](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/PScreenRec-Helper-0.5.10-Mac-arm64-Marketplace.dmg). See [Mac installation and security prompts](MAC_INSTALL.md). The helper installs no Photoshop plugin; obtain the panel through Adobe after approval. This channel was tested locally on macOS 15.6.1 / Photoshop 27.10.0, not through a published store listing. Do not run both independent and Marketplace panels.
