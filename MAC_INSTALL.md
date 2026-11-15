# PScreenRec on Mac / Установка на Mac

Apple Silicon (arm64), macOS 15+. Intel is not supported by these downloads. Python and FFmpeg are included; Homebrew and UXP Developer Tool are not required.

## Downloads

- **[Without Creative Cloud — experimental](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Standalone-Experimental.dmg)**. The installer does not invoke CC/UPIA. Recording was tested with CC present; a Photoshop installation with CC completely absent has not yet been verified.
- [Install through Creative Cloud](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/ProcessRecorder-0.5.10-Mac-arm64-Adobe-CC.dmg). Installs the independent plugin and helper using Adobe's installer; requires Creative Cloud Desktop.

Both independent installers are version 0.5.10. The separate Marketplace plugin is 0.5.13; these version numbers describe different packages.

## Install

1. Save your drawings and quit Photoshop. Download one DMG above and open it in Finder.
2. Run the Install application inside the DMG and follow its instructions. On first installation, choose the parent folder for `ProcessRecorderData`; updates retain the existing location.
3. The installer is unsigned and not notarized. If macOS blocks it and you trust this download, follow [Apple's instructions](https://support.apple.com/en-us/102445): System Settings → Privacy & Security → Security → Open Anyway for this specific installer. You may need to attempt launching it first. Confirm with your password or Touch ID. Do not disable Gatekeeper/SIP or remove quarantine with Terminal commands.
4. If requested, allow the helper's bundled Python.app under Input Monitoring. The installed helper provides its path. Capture is blocked without the required permission.
5. Open Photoshop → Plugins → PScreenRec → PScreenRec. If prompted for a connection, select `~/Library/Application Support/ProcessRecorder/connection.json`. Never share this private file.
6. Enable **Record this document**. Save the drawing as PSD/PSB after starting recording to keep its link to the local timelapse.

Recordings are stored in your selected `ProcessRecorderData` folder; source frames are in `recordings.sqlite3`, exports in `exports`. Keep this folder when updating or uninstalling. Use the supplied removal command for the chosen installer; do not delete recordings unless you intend to lose them. Do not enable independent and Marketplace panels at the same time.

Marketplace users need the separate [Mac helper](https://github.com/JazzyXP/PScreenRec/releases/download/mac-v0.5.13/PScreenRec-Helper-0.5.10-Mac-arm64-Marketplace.dmg), not either full independent installer. See [Marketplace setup](MARKETPLACE_SETUP.md). The Marketplace edition is still a draft, not an approved store listing.

## По-русски

Основной вариант — первая ссылка **без Creative Cloud**, дополнительный — установка через CC. Вариант без CC пока экспериментальный: установщик обходится без CC, но запись на Mac с полностью отсутствующим CC ещё не проверена. Оба независимых установщика имеют версию 0.5.10; магазинный плагин — 0.5.13.

1. Сохрани рисунки и закрой Photoshop. Скачай один DMG, открой его и запусти приложение Install внутри.
2. Следуй подсказкам. При первой установке выбери родительскую папку для `ProcessRecorderData`. Python и FFmpeg уже внутри, отдельно скачивать их не нужно.
3. Если macOS блокирует неподписанный установщик, открой **Системные настройки → Конфиденциальность и безопасность → Безопасность → Всё равно открыть** рядом с именем именно этого приложения. Подтверди пароль или Touch ID. Не отключай защиту системы. При предупреждении о вредоносном ПО или повреждении файла остановись и сообщи автору точный текст.
4. Если помощник запросит разрешение **Мониторинг ввода**, разреши его комплектному Python.app по указанному пути.
5. В Photoshop открой **Plugins → PScreenRec → PScreenRec** и включи запись документа. Если потребуется подключение, выбери `~/Library/Application Support/ProcessRecorder/connection.json`; этот файл никому не передавай.
6. После начала записи сохрани рисунок в PSD или PSB. Не удаляй папку записей при обновлении или удалении программы.

Сборки для Apple Silicon, macOS 15+. Intel не проверен. По отчётам с Mac магазинная версия проверена на macOS 15.6.1 и Photoshop 27.10.0; это не обещание проверки всех версий. Короткая смена курсора при захвате остаётся известным ограничением.

[Optional download checksums](MAC_DOWNLOADS_SHA256.txt) ? [Mac third-party notices](MAC_THIRD_PARTY.md)
