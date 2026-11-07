import os
import re
import pathlib
import hashlib
from datetime import datetime
from typing import List, Dict, Any
from urllib.parse import urlsplit

import json

from flask import Flask, has_request_context, render_template, abort, url_for, jsonify, request, Response, redirect, send_from_directory
from markupsafe import Markup, escape
import markdown


BASE_DIR = pathlib.Path(__file__).parent.resolve()
BLOG_DIR = BASE_DIR / "content" / "blog"
BENCHMARKS_DIR = BASE_DIR / "content" / "benchmarks"
# 待定稿的 Blog 候选版本：只能通过 /blog/preview/<slug> 访问，不进列表和 sitemap
BLOG_PREVIEW_DIR = BASE_DIR / "content" / "blog_previews"
# Public OTS data lives under static/ so the trusted preview packager includes it.
OTS_CATALOG = BASE_DIR / "static" / "data" / "ots.json"

# CDN URL 配置 (仅生产环境设置，staging 留空使用 OSS 直连)
CDN_URL = os.environ.get("CDN_URL", "").rstrip("/")

app = Flask(__name__, template_folder="templates", static_folder="static")

# Keep SLE's small routing adapter in the existing runtime entrypoint. The trusted
# main-branch packager and installed host unpacker already allow app.py.
SPU_SLUG = "SciencePredictionUniverse"
SLE_ALIASES = {"spu", "sciencepredictionuniverse", "sle", "sciencelastexam"}
SPU_PUBLIC_ORIGIN = SLE_PUBLIC_ORIGIN = "https://spu.unipat.ai"
SLE_LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}


def sle_project_origin(value, required=False):
    if not value:
        if required:
            raise ValueError("A public SLE project origin is required")
        return None
    if not isinstance(value, str) or any(c.isspace() or ord(c) < 32 for c in value):
        raise ValueError("Invalid SLE project origin")
    try:
        u = urlsplit(value)
        port = u.port
        if (u.scheme not in ("http", "https") or not u.hostname or u.username or u.password
                or u.path not in ("", "/") or u.query or u.fragment
                or (port is not None and port < 1)
                or (u.scheme != "https" and u.hostname not in SLE_LOCAL_HOSTS)
                or (required and (u.scheme != "https" or u.hostname in SLE_LOCAL_HOSTS))):
            raise ValueError()
    except ValueError:
        raise ValueError("Invalid SLE project origin") from None
    return value.rstrip("/")


def sle_project_target(origin, request_host, require_release=False):
    try:
        host = urlsplit("//" + request_host)
        local = host.hostname in SLE_LOCAL_HOSTS and not (host.username or host.password or host.path or host.query or host.fragment)
    except ValueError:
        local = False
    target = sle_project_origin(origin) if origin else None
    if target and urlsplit(target).hostname not in SLE_LOCAL_HOSTS:
        return sle_project_origin(target, required=True)
    if target and local and not require_release:
        return target
    # Local and intranet previews use the official site by default. A local
    # development target requires an explicit environment setting.
    return SLE_PUBLIC_ORIGIN


def sle_homepage():
    host = request.host if has_request_context() else ""
    return sle_project_target(os.environ.get("SLE_PROJECT_ORIGIN", ""), host,
                              os.environ.get("SLE_REQUIRE_RELEASE") == "1") + "/#/home"


def sle_release_links(paper_url=""):
    links = []
    if paper_url:
        u = urlsplit(paper_url)
        if any(c.isspace() or ord(c) < 32 for c in paper_url) or u.scheme != "https" or not u.hostname or u.username or u.password:
            raise ValueError("SLE_PAPER_URL must be an HTTPS URL")
        links.append(("Paper", paper_url))
    return links + [("GitHub", "https://github.com/UniPat-AI/SPU"),
                    ("Dataset", "https://huggingface.co/datasets/UnipatAI/SPU")]

# 静态文件版本号缓存（启动时计算，用于 CSS/JS 缓存失效）
# 只对 CSS 和 JS 文件加版本号，图片/字体等大文件保持原样
_STATIC_HASH_CACHE: Dict[str, str] = {}

def _get_static_version(filename: str) -> str:
    """计算静态文件内容的 MD5 短 hash，结果缓存到内存。
    仅对 .css 和 .js 文件生效，其他文件返回空字符串。
    """
    if not (filename.endswith(".css") or filename.endswith(".js")):
        return ""
    if filename not in _STATIC_HASH_CACHE:
        path = BASE_DIR / "static" / filename
        try:
            content = path.read_bytes()
            _STATIC_HASH_CACHE[filename] = hashlib.md5(content).hexdigest()[:8]
        except OSError:
            _STATIC_HASH_CACHE[filename] = ""
    return _STATIC_HASH_CACHE[filename]


@app.context_processor
def inject_static_cdn():
    """注入 static_cdn 函数到所有模板"""
    def static_cdn(filename):
        v = _get_static_version(filename)
        qs = f"?v={v}" if v else ""
        if CDN_URL:
            # 生产环境：使用 CDN
            return f"{CDN_URL}/static/{filename}{qs}"
        else:
            # Staging 环境：使用默认 url_for (Nginx 代理到 OSS)
            return url_for('static', filename=filename) + qs
    return dict(static_cdn=static_cdn)

HEADER_IMAGES = [
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1487058792275-0ad4aaf24ca7?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1471357674240-e1a485acb3e1?auto=format&fit=crop&w=900&q=80",
]


def _choose_header_image(meta: Dict[str, Any], slug: str) -> str:
    explicit = meta.get("headerimage") or meta.get("header_image")
    if explicit:
        # 如果配置了 CDN，替换静态资源路径
        if CDN_URL and explicit.startswith("/static/"):
            return explicit.replace("/static/", f"{CDN_URL}/static/")
        return explicit
    h = hashlib.sha256(slug.encode("utf-8")).hexdigest()
    idx = int(h, 16) % len(HEADER_IMAGES)
    return HEADER_IMAGES[idx]


def _parse_markdown(file_path: pathlib.Path) -> Dict[str, Any]:
    """Read a markdown file and return metadata and rendered HTML."""
    text = file_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["fenced_code", "tables", "meta", "toc"])
    html = md.convert(text)

    if file_path.name == SPU_SLUG + ".md" and file_path.parent == BLOG_DIR:
        homepage = sle_homepage()
        html = html.replace("<!-- SLE_RESOURCES -->", render_template(
            "sle_resources.html", project_homepage=homepage,
            release_links=sle_release_links(os.environ.get("SLE_PAPER_URL", "")),
        ))
        html = html.replace("<!-- SLE_PROJECT_LINKS -->", render_template(
            "sle_project_link.html", project_homepage=homepage,
        ))
    
    # 如果配置了 CDN，替换静态资源路径
    if CDN_URL:
        html = html.replace('="/static/', f'="{CDN_URL}/static/')
        html = html.replace("='/static/", f"='{CDN_URL}/static/")
    
    meta = {k.lower(): " ".join(v).strip() for k, v in md.Meta.items()} if hasattr(md, "Meta") else {}
    return {
        "slug": file_path.stem,
        "html": Markup(html),
        "meta": meta,
        "source": text,
    }


def _load_entries(directory: pathlib.Path) -> List[Dict[str, Any]]:
    entries = []
    for file_path in sorted(directory.glob("*.md")):
        parsed = _parse_markdown(file_path)
        meta = parsed["meta"]
        # Attempt to parse date for ordering; fallback to file modified time.
        date_str = meta.get("date")
        try:
            parsed_date = datetime.fromisoformat(date_str)
        except Exception:
            parsed_date = datetime.fromtimestamp(file_path.stat().st_mtime)
        parsed["date"] = parsed_date
        parsed["title"] = meta.get("title", file_path.stem.replace("-", " ").title())
        parsed["summary"] = meta.get("summary") or meta.get("tagline") or ""
        parsed["header_image"] = _choose_header_image(meta, parsed["slug"])
        if directory == BENCHMARKS_DIR and parsed["slug"] == SPU_SLUG:
            parsed["project_url"] = sle_homepage()
        entries.append(parsed)
    # Sort newest first
    return sorted(entries, key=lambda e: e["date"], reverse=True)


def _load_entry(directory: pathlib.Path, slug: str) -> Dict[str, Any]:
    target = directory / f"{slug}.md"
    if not target.exists():
        abort(404)
    parsed = _parse_markdown(target)
    meta = parsed["meta"]
    parsed["title"] = meta.get("title", slug.replace("-", " ").title())
    parsed["date_str"] = meta.get("date") or ""
    parsed["summary"] = meta.get("summary") or meta.get("tagline") or ""
    parsed["header_image"] = _choose_header_image(meta, parsed["slug"])
    return parsed


@app.template_filter("slugify")
def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def _role_teams() -> List[Any]:
    """Open roles grouped by team, in the order teams first appear in OPEN_ROLES."""
    teams: Dict[str, List[Dict[str, str]]] = {}
    for role in OPEN_ROLES:
        teams.setdefault(role["team"], []).append(role)
    return list(teams.items())


@app.route("/")
def landing():
    return render_template(
        "landing.html",
        posts=_load_entries(BLOG_DIR)[:3],
        benchmarks=_load_entries(BENCHMARKS_DIR),
        roles=OPEN_ROLES,
    )


@app.route("/designs")
@app.route("/designs/")
def design_collection():
    """Preview the ten homepage directions without changing the existing homepage."""
    return redirect(url_for("static", filename="designs/index.html"))


@app.route("/joinus")
def joinus():
    return render_template("joinus.html", teams=_role_teams())


def _load_ots() -> Dict[str, Any]:
    """Read the OTS catalog on each request so data updates need no restart."""
    data = json.loads(OTS_CATALOG.read_text(encoding="utf-8"))
    note = data["footer_note"]
    link = Markup('<a href="{}">{}</a>').format(note["email_href"], note["email"])
    # 说明文字里的邮箱地址渲染成 mailto 链接，其余文字照常转义
    note["html"] = [link.join(escape(part) for part in p.split(note["email"])) for p in note["paragraphs"]]
    for card in data["cards"]:
        # "+13.05pp" -> "13.05"：页面上只让数字部分滚动
        card["delta_value"] = card["delta_display"].lstrip("+").removesuffix("pp")
    return data


@app.route("/ots")
def ots():
    return render_template("ots.html", ots=_load_ots())


@app.route("/blog")
def blog_list():
    posts = _load_entries(BLOG_DIR)
    return render_template("blog_list.html", posts=posts)


@app.route("/blog/<slug>")
def blog_detail(slug: str):
    if slug.lower() in SLE_ALIASES and slug != SPU_SLUG:
        return redirect(url_for("blog_detail", slug=SPU_SLUG), code=301)
    post = _load_entry(BLOG_DIR, slug)
    return render_template("blog_detail.html", post=post)


@app.route("/blog/preview/<slug>")
def blog_preview(slug: str):
    post = _load_entry(BLOG_PREVIEW_DIR, slug)
    # 同一篇文章的其它候选版本（文件名前缀相同，如 fellows-v1 / fellows-v2）
    group = slug.rsplit("-v", 1)[0]
    siblings = sorted(p.stem for p in BLOG_PREVIEW_DIR.glob(f"{group}-v*.md"))
    return render_template("blog_detail.html", post=post, preview_siblings=siblings)


# OSS serves static HTML as attachments, so viewer pages need an inline route.
VIEWER_PAGES = {"molstar.html", "niivue.html", "occt.html", "gltf.html"}


@app.route("/sciencevision/viewer/<version>/<filename>")
def sciencevision_viewer(version: str, filename: str):
    if not re.fullmatch(r"[0-9a-f]{8}", version) or filename not in VIEWER_PAGES:
        abort(404)
    directory = BASE_DIR / "static" / "sciencevision" / "viewer" / version
    return send_from_directory(str(directory), filename, mimetype="text/html")


@app.route("/benchmarks")
def benchmarks_list():
    entries = _load_entries(BENCHMARKS_DIR)
    return render_template("benchmarks_list.html", entries=entries)


@app.route("/benchmarks/<slug>")
def benchmarks_detail(slug: str):
    if slug.lower() in SLE_ALIASES:
        destination = sle_homepage()
        response = redirect(destination, code=302)
        response.set_data(render_template("sle_redirect.html", destination=destination))
        response.headers["Cache-Control"] = "no-store"
        return response
    entry = _load_entry(BENCHMARKS_DIR, slug)
    return render_template("benchmarks_detail.html", entry=entry)


# 首页改版候选方案（/design 预览，/design/<n> 查看单个方案）
DESIGN_VARIANTS = [
    {"n": 1, "name": "Contour", "desc": "Sea-glass survey map: a living terrain whose summit is the UniPat mark, reshaped by the cursor."},
    {"n": 2, "name": "Loom", "desc": "Night-plum and peach: the mark is woven thread by thread, with a spool-and-swatch benchmark browser."},
    {"n": 3, "name": "Horizon", "desc": "Dark sky breaking at a blue-to-gold horizon into a bright editorial page."},
    {"n": 4, "name": "Pattern Tunnel", "desc": "A WebGL field of light-streak patterns with frosted bento panels."},
    {"n": 5, "name": "Kinetic", "desc": "Cobalt on cool paper: variable-width type that stretches under the cursor and a scroll-driven benchmark rail."},
    {"n": 6, "name": "Constellation", "desc": "Every benchmark as a star, orbiting its domain around the UniPat mark."},
    {"n": 7, "name": "Aurora", "desc": "A slow WebGL aurora behind glass, with large calm typography."},
    {"n": 8, "name": "Assembly", "desc": "Scroll-driven particles that assemble the mark, a grid, then the team."},
    {"n": 9, "name": "Data Bloom", "desc": "Fibre-lit glass cubes bursting from the centre, after the brand reference art."},
    {"n": 10, "name": "Dusk", "desc": "The mark sets like a sun over still water; the sky deepens to night as you read and dawns at Join us."},
]

OPEN_ROLES = [
    {"title": "Research Scientist", "team": "Research"},
    {"title": "Research Intern", "team": "Research"},
    {"title": "AI for Science Fellow", "team": "Research"},
    {"title": "Agent Systems Engineer", "team": "Engineering"},
    {"title": "Agent Sandbox Engineer", "team": "Engineering"},
    {"title": "GPU Platform Engineer", "team": "Engineering"},
    {"title": "Infra Engineer", "team": "Engineering"},
    {"title": "Full-Stack Engineer", "team": "Engineering"},
    {"title": "Expert Community Lead", "team": "Operations"},
    {"title": "AI Data Product Manager", "team": "Product"},
    {"title": "Frontier Development Researcher", "team": "Research"},
    {"title": "Business Development", "team": "Operations"},
    {"title": "Design Technologist", "team": "Design"},
    {"title": "Senior Tax Specialist", "team": "Operations"},
    {"title": "Senior Recruiter", "team": "Operations"},
]


@app.route("/design")
def design_index():
    return render_template("designs/index.html", variants=DESIGN_VARIANTS)


@app.route("/design/<int:n>")
def design_variant(n: int):
    if not any(v["n"] == n for v in DESIGN_VARIANTS):
        abort(404)
    posts = _load_entries(BLOG_DIR)[:3]
    benchmarks = _load_entries(BENCHMARKS_DIR)
    return render_template(
        f"designs/v{n}.html",
        posts=posts,
        benchmarks=benchmarks,
        roles=OPEN_ROLES,
        variants=DESIGN_VARIANTS,
        current=n,
    )


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


TRAJECTORIES_DIR = BASE_DIR / "static" / "images" / "SWE-Vision" / "trajectories"

# 生产域名列表
PROD_HOSTS = {"unipat.ai", "www.unipat.ai"}


def _is_production() -> bool:
    return request.host.split(":")[0] in PROD_HOSTS


@app.route("/robots.txt")
def robots_txt():
    if _is_production():
        content = (
            "User-agent: *\n"
            "Allow: /\n"
            "\n"
            "Sitemap: https://unipat.ai/sitemap.xml\n"
        )
    else:
        # Staging 及其他非生产环境：禁止所有爬虫抓取
        content = "User-agent: *\nDisallow: /\n"
    return Response(content, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap_xml():
    if not _is_production():
        abort(404)

    base = "https://unipat.ai"
    today = datetime.utcnow().strftime("%Y-%m-%d")

    urls = [
        {"loc": f"{base}/",            "priority": "1.0", "changefreq": "weekly",  "lastmod": today},
        {"loc": f"{base}/blog",         "priority": "0.8", "changefreq": "weekly",  "lastmod": today},
        {"loc": f"{base}/benchmarks",   "priority": "0.8", "changefreq": "weekly",  "lastmod": today},
        {"loc": f"{base}/ots",          "priority": "0.8", "changefreq": "monthly", "lastmod": today},
        {"loc": f"{base}/joinus",       "priority": "0.6", "changefreq": "monthly", "lastmod": today},
    ]

    # 动态加入博客文章
    for fp in sorted(BLOG_DIR.glob("*.md")):
        parsed = _parse_markdown(fp)
        meta = parsed["meta"]
        date_str = meta.get("date", today)
        slug = fp.stem if fp.stem == SPU_SLUG else fp.stem.lower()
        urls.append({
            "loc": f"{base}/blog/{slug}",
            "priority": "0.9",
            "changefreq": "monthly",
            "lastmod": date_str,
        })

    # 动态加入 benchmarks 条目
    for fp in sorted(BENCHMARKS_DIR.glob("*.md")):
        if fp.stem == SPU_SLUG:
            continue
        parsed = _parse_markdown(fp)
        meta = parsed["meta"]
        date_str = meta.get("date", today)
        slug = fp.stem.lower()
        urls.append({
            "loc": f"{base}/benchmarks/{slug}",
            "priority": "0.9",
            "changefreq": "monthly",
            "lastmod": date_str,
        })

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{u['loc']}</loc>")
        lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        lines.append(f"    <priority>{u['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    return Response("\n".join(lines), mimetype="application/xml")


@app.route("/api/swe-vision/tasks")
def swe_vision_tasks():
    tasks = []
    if not TRAJECTORIES_DIR.is_dir():
        return jsonify(tasks)
    for folder in sorted(TRAJECTORIES_DIR.iterdir()):
        if not folder.is_dir() or not folder.name.startswith("task_"):
            continue
        traj_file = folder / "trajectory.json"
        if not traj_file.exists():
            continue
        meta_file = folder / "meta.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            title = meta.get("title", folder.name)
            tag_labels = meta.get("tags", [])
        else:
            # Fallback: use truncated query from trajectory.json
            traj = json.loads(traj_file.read_text(encoding="utf-8"))
            query = traj.get("metadata", {}).get("query", folder.name)
            title = (query[:60] + "...") if len(query) > 60 else query
            tag_labels = []
        task_id = folder.name.replace("_", "")
        path = f"{CDN_URL}/static/images/SWE-Vision/trajectories/{folder.name}" if CDN_URL else f"/static/images/SWE-Vision/trajectories/{folder.name}"
        tags = [{"l": t, "c": f"swev-tag-{t.lower()}"} for t in tag_labels]
        tasks.append({"id": task_id, "path": path, "title": title, "tags": tags})
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5589, debug=True)
