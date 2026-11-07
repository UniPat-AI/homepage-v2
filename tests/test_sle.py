import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from app import app, sle_project_origin, sle_project_target, sle_release_links

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.anchors, self.assets = [], [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.anchors.append(attrs.get("href", ""))
        for key in ["src", "href"]:
            value = attrs.get(key, "")
            if value.startswith("/static/"):
                self.assets.add(value)


class SLEMigrationTests(unittest.TestCase):
    def setUp(self):
        self.environment = patch.dict(os.environ, {"SLE_PROJECT_ORIGIN": "", "SLE_PAPER_URL": "", "SLE_REQUIRE_RELEASE": "0"})
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.client = app.test_client()

    def test_entry_is_direct_on_both_home_and_benchmark_list(self):
        for host, target in [
            ("http://localhost:18480", "https://spu.unipat.ai/#/home"),
            ("https://unipat.ai", "https://spu.unipat.ai/#/home"),
            ("http://feature.unipat.10.0.0.214.sslip.io", "https://spu.unipat.ai/#/home"),
        ]:
            for route in ["/", "/benchmarks"]:
                response = self.client.get(route, base_url=host)
                self.assertEqual(response.status_code, 200)
                links = Page(response.text).anchors
                self.assertIn(target, links)
                self.assertNotIn("/benchmarks/SciencePredictionUniverse", links)
                self.assertNotIn("/benchmarks/ScienceLastExam", links)
                self.assertIn("/benchmarks/PaperBenchX", links)

    def test_short_and_legacy_routes_resolve_without_query_control(self):
        for route in ["/benchmarks/SciencePredictionUniverse", "/benchmarks/SPU", "/benchmarks/ScienceLastExam", "/benchmarks/SLE", "/benchmarks/sciencelastexam?next=https://evil.example"]:
            response = self.client.get(route, base_url="https://unipat.ai")
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.headers["Location"], "https://spu.unipat.ai/#/home")
            self.assertIn("If you are not redirected automatically", response.text)
            self.assertIn('href="https://spu.unipat.ai/#/home"', response.text)
            self.assertIn("Open SPU", response.text)
            self.assertEqual(response.headers["Cache-Control"], "no-store")
        for route in ["/blog/SPU", "/blog/spu", "/blog/sciencepredictionuniverse", "/blog/SLE", "/blog/sciencelastexam", "/blog/sle"]:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 301)
            self.assertEqual(response.headers["Location"], "/blog/SciencePredictionUniverse")
        self.assertEqual(self.client.get("/blog/SciencePredictionUniverse").status_code, 200)
        self.assertEqual(self.client.get("/benchmarks/not-a-benchmark").status_code, 404)

    def test_origin_validation_and_intranet_preview_never_leak_localhost(self):
        for value in ["", "http://sle.example.org", "https://localhost", "https://x.example/path", "https://u:p@x.example", "https://x.example?key=secret", "javascript:alert(1)", "https://x.example:0", "https://x.example:\n443"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                sle_project_origin(value, required=True)
        for host in ["unipat.ai", "localhost.evil.example", "evil.example@localhost", "up-demo.unipat.10.0.0.214.sslip.io"]:
            self.assertEqual(sle_project_target("http://localhost:18476", host), "https://spu.unipat.ai")
        self.assertEqual(sle_project_target(None, "[::1]:18480"), "https://spu.unipat.ai")
        self.assertEqual(sle_project_target("http://localhost:18476", "localhost:18480"), "http://localhost:18476")
        self.assertEqual(sle_project_target(None, "localhost:18480", True), "https://spu.unipat.ai")
        with patch.dict(os.environ, {"SLE_PROJECT_ORIGIN": "https://sle.example.org"}):
            self.assertEqual(self.client.get("/benchmarks/SLE").headers["Location"], "https://sle.example.org/#/home")

    def test_blog_keeps_v2_shell_particles_and_scoped_article_assets(self):
        response = self.client.get("/blog/SciencePredictionUniverse")
        self.assertEqual(response.status_code, 200)
        for expected in ['id="field"', 'site/field.js', 'site/motion.js', 'href="#main">Skip to content', 'Off-the-Shelf', 'css/sle-blog.css', 'js/sle-blog.js', 'class="paper sle-paper"']:
            self.assertIn(expected, response.text)
        for route in ["/", "/ots", "/benchmarks/PaperBenchX", "/blog/ScienceVision"]:
            other = self.client.get(route)
            self.assertEqual(other.status_code, 200)
            self.assertNotIn("css/sle-blog.css", other.text)
            self.assertNotIn("js/sle-blog.js", other.text)

    def test_blog_has_no_retired_trace_ui_and_has_only_resolving_anchors(self):
        text = self.client.get("/blog/SciencePredictionUniverse", base_url="https://unipat.ai").text
        for stale in ["<!-- SLE_", "#/benchmarks", "sle-cases", "sle-model-row", "localhost:", "sle-research.js"]:
            self.assertNotIn(stale, text)
        page = Page(text)
        self.assertEqual(len(page.ids), len(set(page.ids)))
        self.assertFalse({a[1:] for a in page.anchors if a.startswith("#")} - set(page.ids))
        self.assertIn("#sle-results", page.anchors)
        self.assertIn("https://spu.unipat.ai/#/home", page.anchors)
        self.assertIn("https://github.com/UniPat-AI/SPU", page.anchors)
        self.assertIn("https://huggingface.co/datasets/UnipatAI/SPU", page.anchors)

    def test_author_order_affiliations_and_manuscript_counts_are_retained(self):
        text = self.client.get("/blog/SciencePredictionUniverse").text
        for heading in ["Project Team", "Advisory Committee", "Wet-Lab Collaborators"]:
            self.assertIn("<strong>" + heading + "</strong>", text)
        names = text.split('<div class="sle-contributor-list">')[1].split("</div>")[0]
        self.assertEqual(names.count('class="sle-author"'), 36)
        self.assertNotIn("<a ", names)
        advisory = names.split("<strong>Advisory Committee</strong>")[1]
        self.assertLess(advisory.index("Soojung Yang"), advisory.index("Jianjun Wu"))
        self.assertLess(advisory.index("Steven Dillmann"), advisory.index("Soojung Yang"))
        self.assertIn("Steven Dillmann<sup>2</sup>", advisory)
        self.assertIn("Yuanqi Du<sup>3</sup>", advisory)
        self.assertIn("Soojung Yang<sup>4</sup>", advisory)
        self.assertIn("Shizhe Diao<sup>5</sup>", advisory)
        self.assertIn("Liang Chen<sup>1†‡</sup>", names)
        self.assertIn("<sup>‡</sup>Project leader: Liang Chen.", text)
        self.assertIn("The Hong Kong University of Science and Technology</span>", text)
        self.assertLess(advisory.index("Yuanqi Du"), advisory.index("Soojung Yang"))
        self.assertIn("Cornell University", text)
        self.assertEqual(text.count('src="/static/sle/institution-marks/'), 13)
        self.assertIn("Stanford University", text)
        self.assertIn("FutureHouse", text)
        self.assertIn("Deep Principle", text)
        affiliations = text.split('<ol class="sle-affiliations"')[1].split("</ol>")[0]
        self.assertEqual(re.findall(r'<li value="(\d+)">', affiliations), [str(n) for n in range(1, 17)])
        for phrase in ["100 public tasks", "16 private tasks", "1,155 scored runs", "thirteen configurations"]:
            self.assertIn(phrase, text)

    def test_migrated_figures_match_the_source_and_every_local_asset_serves(self):
        evidence = json.loads((ROOT / "tests/fixtures/sle-migration.json").read_text())
        for name, digest in evidence["assets"].items():
            self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), digest, name)
        page = Page(self.client.get("/blog/SciencePredictionUniverse").text)
        figures = [a for a in page.assets if "/static/sle/blog-" in a and ".png" in a]
        self.assertEqual(len(figures), 9)
        for asset in page.assets:
            with self.client.get(asset) as response:
                self.assertEqual(response.status_code, 200, asset)

    def test_article_text_matches_the_approved_snapshot(self):
        evidence = json.loads((ROOT / "tests/fixtures/sle-migration.json").read_text())
        text = (ROOT / "content/blog/SciencePredictionUniverse.md").read_text()
        canonical = "\n".join(line for line in text.splitlines() if line.strip() and not line.startswith(("<link ", "<script ")))
        self.assertEqual(hashlib.sha256(canonical.encode()).hexdigest(), evidence["article_sha256"])

    def test_cdn_rewriting_and_canonical_sitemap(self):
        with patch("app.CDN_URL", "https://cdn.example.org"):
            text = self.client.get("/blog/SciencePredictionUniverse", base_url="https://unipat.ai").text
            self.assertIn("https://cdn.example.org/static/css/sle-blog.css", text)
            self.assertNotIn('href="/static/', text)
            self.assertNotIn('src="/static/', text)
        sitemap = self.client.get("/sitemap.xml", base_url="https://unipat.ai").text
        self.assertIn("/blog/SciencePredictionUniverse</loc>", sitemap)
        self.assertNotIn("/benchmarks/sciencelastexam", sitemap.lower())

    def test_optional_paper_requires_a_safe_https_url(self):
        self.assertEqual([label for label, _ in sle_release_links()], ["GitHub", "Dataset"])
        with patch.dict(os.environ, {"SLE_PAPER_URL": "https://arxiv.org/abs/2610.00001"}):
            self.assertIn('href="https://arxiv.org/abs/2610.00001"', self.client.get("/blog/SciencePredictionUniverse").text)
        for bad in ["http://arxiv.org/abs/1", "javascript:alert(1)", "https://u:p@x.org/", "https://x.org/\n"]:
            with self.assertRaises(ValueError):
                sle_release_links(bad)
