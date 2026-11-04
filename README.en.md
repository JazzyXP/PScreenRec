# PScreenRec

[Русский](README.md) · [English](README.en.md)

**Record drawing timelapses directly in Photoshop.**

Process Recorder captures canvas changes without Photoshop panels and exports them as MP4. Recordings stay on your computer.

## Features

- Separate recording control for each document and a remembered preference for new documents.
- Full-canvas capture, with an option to include zoom and pan.
- Recording quality and change frequency controls.
- Active work time and a resettable stage timer.
- Timelapse preview in the panel, frame range selection and cropping.
- MP4 export at the original 10 fps timing or a target duration of 15, 30 or 60 seconds, including a final-frame hold.
- Russian and English interface, selected automatically from Photoshop’s language.

## Windows installation

1. Save your drawings and close Photoshop.
2. Run the Process Recorder installer and follow the prompts.
3. Open Photoshop → **Plugins → Process Recorder → Recorder**.
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

Cropping and output size do not modify the original recorded frames. Export cannot restore details missing from the recording.

## Availability and limitations

The current build is for Windows. A macOS release is not ready yet.

The plugin captures canvas states rather than every individual Photoshop action. Several rapid changes may be combined into one frame. Some Photoshop versions may briefly change the cursor during capture. Original-size recording of large canvases requires more processing time and disk space.

## Report a problem

[Open an issue](https://github.com/JazzyXP/ScrenRec/issues/new) with your Photoshop and Windows versions, canvas dimensions, recording quality and steps to reproduce. Remove private information from screenshots before sharing them.
