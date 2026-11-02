"""Check public routes and their local assets before activating a release."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from wsgi import app, application, RELEASE  # noqa: E402
from werkzeug.test import Client  # noqa: E402
from werkzeug.wrappers import Response  # noqa: E402


def validate():
    client = Client(application, Response)
    assets = set()

    class Assets(HTMLParser):
        def handle_starttag(self, tag, attributes):
            for key, value in attributes:
                if key in ("src", "href") and value and value.startswith("/static/"):
                    assets.add(value)

    def get(path, status=200):
        response = client.get(path, base_url="http://unipat.ai", headers={"X-Forwarded-Proto": "https"})
        assert response.status_code == status, (path, response.status_code)
        return response

    paths = ["/", "/blog", "/benchmarks", "/ots", "/joinus"]
    for area in ("blog", "benchmarks"):
        paths.extend("/" + area + "/" + p.stem for p in (ROOT / "content" / area).glob("*.md"))
    for path in paths:
        Assets().feed(get(path).text)
    for path in assets:
        get(path)
    home = get("/").text
    assert 'content="https://unipat.ai/"' in home
    assert "https://x.com/UniPat_AI" in home
    assert "Allow: /" in get("/robots.txt").text
    get("/sitemap.xml")
    assert get("/_health").json == {"status": "ok", "release": RELEASE}
    for path in ("/design", "/design/8", "/designs", "/blog/preview/fellows-v3"):
        get(path, 404)
    for viewer in (ROOT / "static/sciencevision/viewer").glob("*/*.html"):
        if viewer.name in {"molstar.html", "niivue.html", "occt.html", "gltf.html"}:
            get("/sciencevision/viewer/" + viewer.parent.name + "/" + viewer.name)
    print(f"Validated {len(paths)} public pages, {len(assets)} assets, HTTPS metadata and release health")


if __name__ == "__main__":
    validate()
