# Third-party components

The Windows companion installer includes the official CPython embedded runtime. Python's license and notices are included in the runtime directory. Python is a project of the Python Software Foundation: https://www.python.org/ .

FFmpeg 9.0.1 essentials is downloaded separately from Gyan's upstream GitHub distribution and checked against the pinned SHA-256 value `fec81ae03971d9dd4be3ebe02e263bd2ec1d789483f931bdba5f5715e65da2e9`. The archive includes LICENSE and README.txt; these remain in the installed ffmpeg-package directory. This build enables GPL components and version 3. Its FFmpeg and third-party component licenses apply independently of the PScreenRec plugin.

Upstream distribution and build information: https://www.gyan.dev/ffmpeg/builds/ . FFmpeg source and licensing information: https://ffmpeg.org/ . The companion invokes FFmpeg as a separate executable to encode frames and videos.

PScreenRec is an independent project. Adobe Photoshop and Creative Cloud are separate Adobe products and are not included in the installer.
