import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from deploy.bundle import ROOT_FILES, allowed, build, unpack

ROOT = Path(__file__).resolve().parents[1]


class SLEBundleTests(unittest.TestCase):
    def test_dependencies_match_the_runtime_lock(self):
        parse = lambda name: dict(line.split("==") for line in (ROOT / name).read_text().splitlines() if "==" in line)
        direct, locked = parse("requirements.txt"), parse("requirements.lock")
        self.assertEqual(direct["Markdown"], "3.6")
        for name, version in direct.items():
            self.assertEqual(locked[name], version)
        self.assertEqual((ROOT / "requirements-production.txt").read_text().strip(), "-r requirements.lock")

    def test_sle_uses_existing_runtime_paths_without_widening_the_allowlist(self):
        for name in ["app.py", "templates/sle_resources.html", "static/css/sle-blog.css",
                     "content/blog/ScienceLastExam.md", "content/benchmarks/ScienceLastExam.md"]:
            self.assertTrue(allowed(name), name)
        for name in ["sle_research.py", "sle_publication.py", ".env", "artifacts/review.json", "tests/fixtures/sle-migration.json"]:
            self.assertFalse(allowed(name), name)
        self.assertFalse((ROOT / "scripts/install_staging_dependencies.py").exists())
        self.assertFalse((ROOT / ".github/workflows/deploy-test.yml").exists())

    def test_sle_routes_assets_and_contacts_survive_a_real_bundle_round_trip(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            for name in ROOT_FILES | {"deploy/validate.py"}:
                dest = source / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, dest)
            for name in ["templates", "content", "static/site", "static/favicon", "static/sle", "static/images/sle"]:
                shutil.copytree(ROOT / name, source / name)
            for name in ["static/css/sle-blog.css", "static/js/sle-blog.js", "static/data/ots.json"]:
                dest = source / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, dest)
            (source / ".env").write_text("PRIVATE_SENTINEL=never-package\n")
            archive, release = root / "site.tar.gz", root / "release"
            build(source, archive, "a" * 40)
            release.mkdir()
            manifest = unpack(archive, release, "a" * 40)
            self.assertFalse((release / ".env").exists())
            self.assertIn("static/sle/blog-2026-10-25/overview.png", manifest["files"])
            check = r"""
from html.parser import HTMLParser
from pathlib import Path
from wsgi import application
from werkzeug.test import Client
from werkzeug.wrappers import Response
c=Client(application, Response)
kw=dict(base_url='https://unipat.ai')
article=c.get('/blog/ScienceLastExam',**kw)
assert article.status_code==200
assert 'Soojung Yang<sup>2</sup>' in article.text and 'FutureHouse' in article.text
assert '<!-- SLE_' not in article.text and 'localhost:' not in article.text
class Assets(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('src','href') and value and value.startswith(('/static/sle/','/static/css/sle-','/static/js/sle-')):
    r=c.get(value,**kw);assert r.status_code==200,(value,r.status_code)
Assets().feed(article.text)
assert c.get('/benchmarks/SLE',**kw).headers['Location']=='https://sle.unipat.ai/#/home'
assert 'If you are not redirected automatically' in c.get('/benchmarks/SLE',**kw).text
assert 'href="https://sle.unipat.ai/#/home"' in c.get('/benchmarks').text
assert c.get('/blog/SLE',**kw).headers['Location']=='/blog/ScienceLastExam'
assert c.get('/_health',**kw).json['release']=='a'*40
assert c.get('/ots',**kw).status_code==200
assert not Path('sle_publication.py').exists()
"""
            result = subprocess.run([sys.executable, "-c", check], cwd=release, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
