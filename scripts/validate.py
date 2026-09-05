#!/usr/bin/env python3
"""Validate the portable skill, asset provenance and release version contract."""
import argparse
import hashlib
from pathlib import Path
import re
import struct
import sys
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
SHEET_SHA = 'f85cf3e0b1ad946344a741ad3efc822ef286c78f9f9a4935392b37036567444e'
REFERENCE_FILES = (
    'character-lock.md', 'rendering-grounding.md', 'style-adapters.md',
    'game-profiles.md', 'modes.md', 'storyboard-continuity.md',
    'animation-rules.md', 'model-adapters.md', 'model-adapters/fal-h3-max.md',
    'repair-rules.md', 'community-boundaries.md', 'example-ideas.md',
)
FILES = {'SKILL.md', 'VERSION', 'agents/openai.yaml', 'assets/icon.svg',
         'assets/hotdog-character-sheet-v1.png'} | {'references/' + x for x in REFERENCE_FILES}
SEMVER = re.compile(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\Z')


def validate(skill: Path, tag=None):
    skill = skill.resolve()
    found = set()
    for p in skill.rglob('*'):
        if p.is_symlink():
            raise ValueError(f'Symlink is not portable: {p}')
        if p.is_file():
            found.add(p.relative_to(skill).as_posix())
    if found != FILES:
        raise ValueError(f'Package inventory mismatch; missing={FILES-found}, unexpected={found-FILES}')
    version = (skill / 'VERSION').read_text().strip()
    if not SEMVER.fullmatch(version):
        raise ValueError('VERSION must be a stable major.minor.patch version')
    if tag and tag != 'v' + version:
        raise ValueError(f'Tag {tag!r} does not match v{version}')
    entry = (skill / 'SKILL.md').read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', entry, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    meta = yaml.safe_load(match.group(1))
    if set(meta) != {'name', 'description'} or meta['name'] != 'hotdog':
        raise ValueError('Expected name hotdog and description frontmatter only')
    if not isinstance(meta['description'], str) or not meta['description'].strip():
        raise ValueError('Missing discovery description')
    if f'# Hotdog v{version}\n' not in entry:
        raise ValueError('Skill title and VERSION differ')
    ui = yaml.safe_load((skill / 'agents/openai.yaml').read_text())
    interface = ui['interface']
    if interface['display_name'] != 'Hotdog' or '$hotdog' not in interface['default_prompt']:
        raise ValueError('UI metadata does not identify Hotdog')
    if not 25 <= len(interface['short_description']) <= 64:
        raise ValueError('UI short description must contain 25-64 characters')
    if ui.get('policy', {}).get('allow_implicit_invocation', True) is not True:
        raise ValueError('Hotdog must be discoverable by default')
    for field in ('icon_small', 'icon_large'):
        target = (skill / interface[field]).resolve()
        if not target.is_relative_to(skill) or not target.is_file():
            raise ValueError('UI icon must resolve inside the package')
    sheet = (skill / 'assets/hotdog-character-sheet-v1.png').read_bytes()
    if hashlib.sha256(sheet).hexdigest() != SHEET_SHA:
        raise ValueError('Approved character-sheet bytes changed')
    if sheet[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', sheet[16:24]) != (1536, 1024) or sheet[25] != 2:
        raise ValueError('Expected approved RGB 1536x1024 PNG')
    # Walk linked local resources, checking portability and reachability.
    reached = set()
    pending = [skill / 'SKILL.md']
    while pending:
        p = pending.pop()
        if p in reached:
            continue
        reached.add(p)
        if p.suffix != '.md':
            continue
        body = p.read_text()
        if re.search(r'\bTODO\b|\bFIXME\b|/root/|/workspace/|skill://', body):
            raise ValueError(f'Unfinished or host-specific instruction: {p.name}')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            parsed = urlsplit(link)
            if parsed.scheme or not parsed.path:
                continue
            target = (p.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(skill) or not target.is_file():
                raise ValueError(f'Broken/nonportable reference in {p.name}: {link}')
            pending.append(target)
    unreachable = {skill / 'references' / f for f in REFERENCE_FILES} - reached
    if unreachable:
        raise ValueError(f'Unreachable references: {unreachable}')
    return version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skill', type=Path, default=ROOT / 'hotdog')
    parser.add_argument('--tag')
    args = parser.parse_args()
    try:
        version = validate(args.skill, args.tag)
        print(f'Validated Hotdog {version}: {len(FILES)} files, links, metadata, exact canonical asset')
    except (ValueError, KeyError, OSError, yaml.YAMLError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
