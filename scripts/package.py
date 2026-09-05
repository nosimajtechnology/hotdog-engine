#!/usr/bin/env python3
"""Build a deterministic, installable Hotdog ZIP and verify its contents."""
import argparse
import hashlib
from pathlib import Path
import tempfile
import zipfile
from validate import FILES, ROOT, validate


def build(skill, output, tag=None):
    version = validate(skill, tag)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / 'hotdog.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_STORED) as z:
        for relative in sorted(FILES):
            info = zipfile.ZipInfo('hotdog/' + relative, date_time=(2026, 9, 5, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, (skill / relative).read_bytes())
    with tempfile.TemporaryDirectory() as temp:
        with zipfile.ZipFile(archive) as z:
            if z.testzip() or set(z.namelist()) != {'hotdog/' + f for f in FILES}:
                raise ValueError('Archive content verification failed')
            z.extractall(temp)
        validate(Path(temp) / 'hotdog', 'v' + version)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / 'hotdog.zip.sha256').write_text(f'{digest}  hotdog.zip\n')
    return archive


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--skill', type=Path, default=ROOT / 'hotdog')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    parser.add_argument('--tag')
    args = parser.parse_args()
    print(build(args.skill, args.output, args.tag))
