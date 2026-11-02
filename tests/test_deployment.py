import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest

from deploy.bundle import ROOT_FILES, allowed, build, unpack


class ReleaseBundleTests(unittest.TestCase):
    def test_only_public_runtime_is_allowed(self):
        for name in (".env", "../app.py", "/app.py", "static/../secrets", "static/.env", "content/blog_previews/fellows-v3.md", "templates/designs/v8.html", ".git/config"):
            self.assertFalse(allowed(name), name)
        self.assertTrue(allowed("static/sciencevision/viewer/shared/vendor/build/three.js"))
        self.assertTrue(allowed("static/data/ots.json"))

    def fixture(self, path):
        for name in ROOT_FILES | {"deploy/validate.py", "static/site/site.css"}:
            target = path / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("test content\n")

    def test_bundle_round_trip_and_commit_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"
            src.mkdir()
            self.fixture(src)
            (src / ".env").write_text("not for publication")
            archive = root / "site.tar.gz"
            build(src, archive, "a" * 40)
            dest = root / "release"
            dest.mkdir()
            manifest = unpack(archive, dest, "a" * 40)
            self.assertEqual(manifest["commit"], "a" * 40)
            self.assertFalse((dest / ".env").exists())
            other = root / "other"
            other.mkdir()
            with self.assertRaisesRegex(ValueError, "manifest mismatch"):
                unpack(archive, other, "b" * 40)

    def test_ots_renders_from_unpacked_release(self):
        project = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            source.mkdir()
            for name in ROOT_FILES | {"deploy/validate.py", "static/data/ots.json"}:
                target = source / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(project / name, target)
            shutil.copytree(project / "templates", source / "templates")
            archive = root / "site.tar.gz"
            build(source, archive, "a" * 40)
            release = root / "release"
            release.mkdir()
            unpack(archive, release, "a" * 40)

            # A fresh process must render using only the packaged files, with no
            # access to the source checkout's catalog or imported Flask app.
            result = subprocess.run(
                [sys.executable, "-c", """
import json
from pathlib import Path
from wsgi import app
app.testing = True
catalog = json.loads(Path('static/data/ots.json').read_text(encoding='utf-8'))
response = app.test_client().get('/ots')
assert response.status_code == 200
for card in catalog['cards']:
    assert 'id="' + card['id'] + '"' in response.text
    assert card['before_display'] in response.text
    assert card['after_display'] in response.text
"""],
                cwd=release, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_symlinks_before_extracting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "bad.tar.gz"
            with tarfile.open(archive, "w:gz") as tar:
                info = tarfile.TarInfo("static/link")
                info.type, info.linkname = tarfile.SYMTYPE, "/etc/passwd"
                tar.addfile(info)
            dest = root / "release"
            dest.mkdir()
            with self.assertRaisesRegex(ValueError, "Unsafe archive"):
                unpack(archive, dest, "a" * 40)
            self.assertEqual(list(dest.iterdir()), [])

    def test_rejects_modified_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "bad.tar.gz"
            manifest = {"commit": "a" * 40, "files": {"app.py": "0" * 64}}
            with tarfile.open(archive, "w:gz") as tar:
                for name, data in (("app.py", b"modified"), ("release.json", json.dumps(manifest).encode())):
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    tar.addfile(info, io.BytesIO(data))
            dest = root / "release"
            dest.mkdir()
            with self.assertRaisesRegex(ValueError, "Checksum mismatch"):
                unpack(archive, dest, "a" * 40)


if __name__ == "__main__":
    unittest.main()
