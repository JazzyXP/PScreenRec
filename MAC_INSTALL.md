# Install PScreenRec on Mac

[English](MAC_INSTALL.md) · [Русский](MAC_INSTALL.ru.md)

Apple Silicon (M1 or newer), macOS 15+. Photoshop 27.10+ is recommended. These downloads do not support Intel Macs. Choose one installation method. Both installers are 0.5.10 and include the same independent plugin, local helper, Python and FFmpeg.

## Direct install

1. Save your drawings and quit Photoshop.
2. [Download the direct installer](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Standalone-Experimental.dmg) and open the DMG.
3. Run the Install application inside and follow the prompts. On first installation, choose the parent folder for ProcessRecorderData.
4. Follow the security and first-launch steps below.

The installer does not invoke Creative Cloud or Adobe's installation service. Recording with Creative Cloud completely absent has not yet been verified.

## Install via Adobe CC

1. Install Creative Cloud Desktop and Photoshop, and sign in to Creative Cloud.
2. Save your drawings and quit Photoshop.
3. [Download the CC installer](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Adobe-CC.dmg), open the DMG and run Install inside. Follow its prompts.
4. Follow the security and first-launch steps below.

This uses Adobe's installation mechanism and does not require a published Marketplace listing. Do not install both variants.

## Security and first launch

1. The installer is unsigned and not notarized. If macOS blocks it because the developer cannot be verified, open **System Settings → Privacy & Security → Open Anyway** for this application. Confirm with your password or Touch ID. If macOS reports malware or a damaged file, stop and report the exact message. Do not disable system protection.
2. If requested, allow the helper's bundled Python.app under **Input Monitoring**, using the path shown by the installer.
3. Open Photoshop → **Plugins → PScreenRec → PScreenRec** and enable **Record this document**.
4. If a connection file is requested, select `~/Library/Application Support/ProcessRecorder/connection.json`. Never share this private file.
5. Save the drawing as PSD/PSB after starting recording to continue the same timelapse later.

## Updating and recordings

Quit Photoshop and run the chosen installer over the previous installation. Keep your selected ProcessRecorderData folder: it contains the recordings, with source frames in recordings.sqlite3 and videos in exports. Do not enable independent and Marketplace panels at the same time.

For large canvases, use **High**. A brief cursor change during capture remains a known limitation. The Mac installers do not yet include the Windows frame-folder and diagnostics shortcuts. The panel uses English or Russian according to Photoshop.

[Third-party notices](MAC_THIRD_PARTY.md) · [Back to PScreenRec](README.md)
