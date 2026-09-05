"""Protect distribution integrity; these do not claim visual model reliability."""
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from package import build
from validate import ROOT, SHEET_SHA, validate
VERSION = (ROOT / 'hotdog/VERSION').read_text().strip()


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'hotdog'
        shutil.copytree(ROOT / 'hotdog', self.skill)

    def test_isolated_archive_is_reproducible_and_preserves_asset(self):
        first = build(self.skill, self.root / 'a', 'v' + VERSION).read_bytes()
        second = build(self.skill, self.root / 'b', 'v' + VERSION).read_bytes()
        self.assertEqual(first, second)
        archive = self.root / 'a/hotdog.zip'
        checksum = (self.root / 'a/hotdog.zip.sha256').read_text().split()[0]
        self.assertEqual(checksum, hashlib.sha256(first).hexdigest())
        with zipfile.ZipFile(archive) as z:
            self.assertEqual(hashlib.sha256(z.read('hotdog/assets/hotdog-character-sheet-v1.png')).hexdigest(), SHEET_SHA)
            z.extractall(self.root / 'isolated')
        self.assertEqual(validate(self.root / 'isolated/hotdog'), VERSION)

    def test_altered_identity_asset_is_rejected(self):
        p = self.skill / 'assets/hotdog-character-sheet-v1.png'
        p.write_bytes(p.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'bytes changed'):
            validate(self.skill)

    def test_broken_reference_is_rejected(self):
        p = self.skill / 'SKILL.md'
        p.write_text(p.read_text() + '\n[missing](references/missing.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken/nonportable'):
            validate(self.skill)

    def test_external_local_reference_is_rejected(self):
        (self.root / 'outside.md').write_text('external dependency')
        p = self.skill / 'SKILL.md'
        p.write_text(p.read_text() + '\n[external](../outside.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken/nonportable'):
            validate(self.skill)

    def test_unexpected_content_is_rejected(self):
        (self.skill / 'references/legacy-adapter.md').write_text('unexpected inherited module')
        with self.assertRaisesRegex(ValueError, 'inventory'):
            validate(self.skill)

    def test_wrong_release_version_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'does not match'):
            build(self.skill, self.root / 'bad', 'v9.9.9')


if __name__ == '__main__':
    unittest.main()
