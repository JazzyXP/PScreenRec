# PScreenRec privacy information

Last updated: 4 November 2026

PScreenRec is developed by JazzyXP (Den Mitin). Contact: denp90@gmail.com.

## Data stored on your computer

When recording is enabled, PScreenRec stores canvas images, document names and available document paths, recording identifiers, frame timestamps, quality and capture settings, and work/recording timer values. Recordings are kept in the chosen local data folder. A temporary frame queue is also stored in Photoshop's plugin data folder so captured frames can survive a restart.

The local helper stores its configuration and a per-user connection token under `%LOCALAPPDATA%\ProcessRecorder`. Treat the token like a local password and do not publish `connection.json` or `helper-config.json`.

## Activity checks

The Windows helper checks the foreground application's executable and the elapsed time since the last input to estimate active Photoshop work time. It samples pointer buttons and a small set of modifier keys to avoid capturing during drawing. It does not record typed text, key sequences or window titles.

The helper can retain a bounded in-memory list of capture timing measurements, including canvas dimensions and processing times. This list is local, contains no image data, and is cleared when the helper restarts. Installer and FFmpeg error logs can also exist locally.

## Network use

The plugin communicates with its helper on the same computer at `127.0.0.1:48173`, authenticated with the local token. PScreenRec has no account system, advertising SDK or analytics endpoint and does not send your artwork to the developer or an AI service.

The installer may download FFmpeg from its upstream distribution on GitHub, with a pinned checksum. If you open a project, support or other external link, your browser contacts that service under its own privacy policy. Adobe, GitHub and any optional third-party support/payment service are separate services and may process information when you use them. No donation is required to use PScreenRec.

## Retention and removal

Turning off recording does not delete previous frames. Uninstalling the application preserves the chosen recordings folder. Exported videos are also retained. You can remove those files and folders yourself when they are no longer needed; close Photoshop and the helper first, and keep backups of work you need.

## Support

If you email us or create a GitHub issue, we receive what you choose to send. Share only the information needed to reproduce a problem. Remove private artwork, document paths and connection tokens before uploading logs or screenshots. GitHub issues are public; email denp90@gmail.com for a private support request or a request concerning information you previously sent.
