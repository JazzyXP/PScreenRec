# PScreenRec

[English](README.md) · [Русский](README.ru.md)

![Windows](https://img.shields.io/badge/Windows-10%20%2F%2011-0078D4) ![Photoshop](https://img.shields.io/badge/Adobe-Photoshop-31A8FF) ![Version](https://img.shields.io/badge/version-0.5.6-555)

**Timelapses in Photoshop.**

PScreenRec captures canvas changes without Photoshop panels and exports them as MP4. Recordings stay on your computer.

### Download for Windows

**[Download installer 0.5.6 — no Creative Cloud required](https://github.com/JazzyXP/PScreenRec/raw/refs/heads/main/downloads/PScreenRec-0.5.6-Setup.exe)** · [SHA-256](downloads/PScreenRec-0.5.6-Setup.exe.sha256)

[Thank the developer](https://app.lava.top/dnso?tabId=about)

Windows x64 · Python included · revision 22.

### Interface

<table><tr><th>Recording</th><th>Timelapse and export</th></tr><tr><td><img src="assets/recorder.png" alt="PScreenRec recording panel in Photoshop" width="360"></td><td><img src="assets/timelapse.png" alt="Frame selection, cropping and MP4 export" width="360"></td></tr></table>

### Video examples

[Knight and mosquito — view MP4](https://github.com/JazzyXP/PScreenRec/raw/refs/heads/main/assets/knight-and-mosquito.mp4) · [Another timelapse — view MP4](https://github.com/JazzyXP/PScreenRec/raw/refs/heads/main/assets/timelapse-example.mp4)

## Features

- Separate recording control for each document and a remembered preference for new documents.
- Full-canvas capture, with an option to include zoom and pan.
- Recording quality and change frequency controls.
- Active work time and a resettable stage timer.
- Timelapse preview in the panel, frame range selection and cropping.
- MP4 export at the original 10 fps timing or a target duration of 15, 30 or 60 seconds, including a final-frame hold.
- Interface language selected automatically from Photoshop’s language.

## Windows installation

The installer selects a default language from Windows: English, Russian, German, French, Spanish, Brazilian Portuguese or Ukrainian. You can change it at startup. Other system languages default to English. The plugin panel still follows the Photoshop language (Russian or English).

1. Save your drawings and close Photoshop.
2. Run the PScreenRec installer and follow the prompts.
3. Open Photoshop → **Plugins → PScreenRec → PScreenRec**.
4. Enable **Record this document** for the current drawing. Enable **Record new documents** to record subsequently created files.

The installer without Creative Cloud includes Python. You do not need to install Creative Cloud, Python or UXP Developer Tool separately. An internet connection is required for the initial FFmpeg download.

## Recording quality

| Quality | Maximum long edge |
| --- | --- |
| Normal | 1920 px |
| High | 3840 px |
| Original | Canvas size within supported capture limits |

Aspect ratio is preserved and small canvases are not upscaled. The panel displays the actual recorded frame dimensions. Quality changes apply to future frames.

**High is recommended for large canvases.** Original-size capture can put more load on Photoshop and briefly show a busy cursor. High reduces the workload; it does not change previously recorded frames.

## Export

Open **Timelapse**, choose the frame range, crop, duration and video size, then click **Export MP4** and choose a destination in the system save dialog.

## Availability and limitations

The current build is for Windows. A macOS release is not ready yet.

The plugin captures canvas states rather than every individual Photoshop action. Several rapid changes may be combined into one frame. Some Photoshop versions may briefly change the cursor during capture. Original-size recording of large canvases requires more processing time and disk space.

## Report a problem

[Open an issue](https://github.com/JazzyXP/PScreenRec/issues/new).

Include your Photoshop and Windows versions, canvas dimensions, recording quality and steps to reproduce. Remove private information from screenshots before sharing them.
