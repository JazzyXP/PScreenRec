"""Count installer downloads across all published releases, excluding checksums."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

repository = os.environ.get('GITHUB_REPOSITORY', 'JazzyXP/PScreenRec')
headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'PScreenRec-download-counts'}
if os.environ.get('GH_TOKEN'):
    headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
counts = {'windows': 0, 'mac': 0}
page = 1
while True:
    request = Request(f'https://api.github.com/repos/{repository}/releases?per_page=100&page={page}', headers=headers)
    with urlopen(request, timeout=30) as response:
        releases = json.load(response)
    if not releases:
        break
    for release in releases:
        if release.get('draft'):
            continue
        for asset in release['assets']:
            name = asset['name'].lower()
            platform = 'windows' if name.endswith('.exe') else 'mac' if name.endswith('.dmg') else None
            if platform:
                counts[platform] += asset['download_count']
    page += 1
folder = Path('assets/downloads')
folder.mkdir(parents=True, exist_ok=True)
for platform, count in counts.items():
    badge = {'schemaVersion': 1, 'label': 'Windows downloads' if platform == 'windows' else 'Mac downloads',
             'message': str(count), 'color': '0078D4' if platform == 'windows' else '8957E5'}
    (folder / f'{platform}.json').write_text(json.dumps(badge, indent=2) + '\n', encoding='utf-8')
print(json.dumps(counts))
