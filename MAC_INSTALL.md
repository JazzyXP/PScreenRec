# Install PScreenRec on Mac

[English](MAC_INSTALL.md) · [Русский](MAC_INSTALL.ru.md)

Apple Silicon (arm64), macOS 15+. Intel is not supported by these downloads. Python and FFmpeg are included; Homebrew and UXP Developer Tool are not required.

## Downloads

- **[Download for Mac](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Standalone-Experimental.dmg)**. The installer does not invoke CC/UPIA. Recording was tested with CC present; a Photoshop installation with CC completely absent has not yet been verified.
- [Install through Creative Cloud](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Adobe-CC.dmg). Installs the independent plugin and helper using Adobe's installer; requires Creative Cloud Desktop.

Both installers are version 0.5.10 and include the plugin and helper. Choose one, then follow the same installation steps below.

## Install

1. Save your drawings and quit Photoshop. Download one DMG above and open it in Finder.
2. Run the Install application inside the DMG and follow its instructions. On first installation, choose the parent folder for `ProcessRecorderData`; updates retain the existing location.
3. The installer is unsigned and not notarized. If macOS blocks it and you trust this download, follow [Apple's instructions](https://support.apple.com/en-us/102445): System Settings → Privacy & Security → Security → Open Anyway for this specific installer. You may need to attempt launching it first. Confirm with your password or Touch ID. Do not disable Gatekeeper/SIP or remove quarantine with Terminal commands.
4. If requested, allow the helper's bundled Python.app under Input Monitoring. The installed helper provides its path. Capture is blocked without the required permission.
5. Open Photoshop → Plugins → PScreenRec → PScreenRec. If prompted for a connection, select `~/Library/Application Support/ProcessRecorder/connection.json`. Never share this private file.
6. Enable **Record this document**. Save the drawing as PSD/PSB after starting recording to keep its link to the local timelapse.

Recordings are stored in your selected `ProcessRecorderData` folder; source frames are in `recordings.sqlite3`, exports in `exports`. Keep this folder when updating or uninstalling. Use the supplied removal command for the chosen installer; do not delete recordings unless you intend to lose them. Do not enable independent and Marketplace panels at the same time.




## Compatibility

The direct installer avoids CC/UPIA; recording was tested with CC present. Recording on a Mac with CC completely absent has not yet been verified. These downloads are independent installers, not the Adobe Marketplace helper.

[Download checksums](MAC_DOWNLOADS_SHA256.txt) · [Third-party notices](MAC_THIRD_PARTY.md)
