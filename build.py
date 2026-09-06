#!/usr/bin/env python3
"""
Build yourstackdoesthat.com.

Reads:
  pages/*.html        page bodies with a small front matter block
  content/does/*.md   Does entries (one file each)
  content/ledger/*.md Cancel Ledger lines (one file each)
  static/*            copied as-is

Writes everything into site/ which is what gets deployed.

No server-side build is required. Run this on a laptop, commit site/,
deploy site/. Python 3 standard library only.
"""

import html
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT / "site"
BASE = "https://yourstackdoesthat.com"
SITE_NAME = "Your stack does that"
REPO = "https://github.com/johnrector/yourstackdoesthat"

NAV = [
    ("/", "Home"),
    ("/idea/", "The idea"),
    ("/stack/", "Your stack"),
    ("/does/", "Does"),
    ("/stack-test/", "The Stack Test"),
    ("/ledger/", "Cancel Ledger"),
    ("/companies/", "For companies"),
    ("/contribute/", "Contribute"),
    ("/check-back/", "Check back"),
    ("/reading/", "Reading"),
]

DOMAINS = [
    ("household", "Household"),
    ("money", "Money"),
    ("health", "Health"),
    ("work", "Work"),
    ("school", "School"),
    ("small-business", "Small business"),
]

DOES_SECTIONS = [
    ("need", "The need"),
    ("bought", "What you used to buy"),
    ("does", "Your stack does that"),
    ("how", "How, in plain terms"),
]


# ---------------------------------------------------------------- helpers

def read_front_matter(text):
    """Return (meta dict, body) from a file starting with a --- block."""
    meta = {}
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        return meta, body.strip()
    return meta, text.strip()


def md_inline(s):
    """Tiny markdown: links, emphasis, code. Escapes HTML first."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


NUMBERED = re.compile(r"^\d+\.\s")


def md_block(text):
    """Paragraphs and simple lists only. Enough for entries."""
    out = []
    for chunk in re.split(r"\n\s*\n", text.strip()):
        lines = chunk.strip().splitlines()
        if all(l.lstrip().startswith(("- ", "* ")) for l in lines):
            items = "".join(f"<li>{md_inline(l.lstrip()[2:])}</li>" for l in lines)
            out.append(f"<ul>{items}</ul>")
        elif all(NUMBERED.match(l.lstrip()) for l in lines):
            items = "".join(
                "<li>" + md_inline(NUMBERED.sub("", l.lstrip())) + "</li>" for l in lines
            )
            out.append(f"<ol>{items}</ol>")
        else:
            out.append(f"<p>{md_inline(' '.join(l.strip() for l in lines))}</p>")
    return "\n".join(out)


def strip_tags(fragment):
    """Plain text of an HTML fragment, for articleBody and feeds."""
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    t = re.sub(r"</(p|li|h[1-6]|dt|dd|dl|blockquote|tr|article|section|div)>", "\n", t)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ---------------------------------------------------------------- content

def load_does():
    entries = []
    for path in sorted((ROOT / "content" / "does").glob("*.md")):
        meta, body = read_front_matter(path.read_text(encoding="utf-8"))
        sections = {}
        current = None
        for line in body.splitlines():
            m = re.match(r"^##\s+(.*)$", line)
            if m:
                current = m.group(1).strip().lower()
                sections[current] = []
            elif current:
                sections[current].append(line)
        key_for = {label.lower(): key for key, label in DOES_SECTIONS}
        parts = {}
        for label, lines in sections.items():
            key = key_for.get(label)
            if key:
                parts[key] = "\n".join(lines).strip()
        missing = [k for k, _ in DOES_SECTIONS if k not in parts]
        if missing:
            raise SystemExit(f"{path.name}: missing sections {missing}")
        entries.append(
            {
                "slug": path.stem,
                "title": meta["title"],
                "domain": meta["domain"],
                "added": meta["added"],
                "uses": [u.strip() for u in meta.get("uses", "").split(",") if u.strip()],
                "setup": meta.get("setup", ""),
                "parts": parts,
            }
        )
    return entries


def load_ledger():
    lines = []
    for path in sorted((ROOT / "content" / "ledger").glob("*.md")):
        meta, body = read_front_matter(path.read_text(encoding="utf-8"))
        lines.append(
            {
                "slug": path.stem,
                "replaced": meta["replaced"],
                "cost": meta.get("cost", ""),
                "replaced_by": meta.get("replaced_by", ""),
                "result": meta.get("result", "replaced"),
                "date": meta["date"],
                "note": body,
            }
        )
    lines.sort(key=lambda l: (l["date"], l["slug"]), reverse=True)
    return lines


# ---------------------------------------------------------------- rendering

def render_does_entry(e, level=3):
    h = f"h{level}"
    uses = ", ".join(e["uses"]) if e["uses"] else "—"
    dl = []
    for key, label in DOES_SECTIONS:
        dl.append(f"<dt>{label}</dt><dd>{md_block(e['parts'][key])}</dd>")
    setup = ""
    if e["setup"]:
        setup = f'<p class="setup"><span class="label">Setup</span> {md_inline(e["setup"])}</p>'
    return (
        f'<article class="does" id="{e["slug"]}">\n'
        f'<{h}><a href="/does/#{e["slug"]}">{html.escape(e["title"])}</a></{h}>\n'
        f'<p class="meta"><span class="label">Uses</span> {html.escape(uses)}'
        f' <span class="sep">·</span> <span class="label">Added</span> '
        f'<time datetime="{e["added"]}">{pretty_date(e["added"])}</time></p>\n'
        f'<dl>{"".join(dl)}</dl>\n{setup}'
        f"</article>"
    )


def pretty_date(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    return f"{d.day} {d.strftime('%B %Y')}"


def render_ledger_line(l):
    result = "Kept" if l["result"] == "kept" else "Replaced"
    cost = f' <span class="sep">·</span> {html.escape(l["cost"])}' if l["cost"] else ""
    by = (
        f"<dt>Replaced by</dt><dd>{md_inline(l['replaced_by'])}</dd>"
        if l["result"] != "kept"
        else f"<dt>Kept because</dt><dd>{md_inline(l['replaced_by'])}</dd>"
    )
    note = f"<dd class=\"note\">{md_block(l['note'])}</dd>" if l["note"] else ""
    return (
        f'<li class="ledger-line {l["result"]}" id="{l["slug"]}">'
        f'<p class="meta"><span class="result">{result}</span>{cost}'
        f' <span class="sep">·</span> <time datetime="{l["date"]}">{pretty_date(l["date"])}</time></p>'
        f"<dl><dt>What it was</dt><dd>{md_inline(l['replaced'])}</dd>{by}"
        f"{('<dt>Note</dt>' + note) if note else ''}</dl></li>"
    )


def layout(meta, body, jsonld, path):
    title = meta["title"]
    full_title = SITE_NAME if path == "/" else f"{title} · {SITE_NAME}"
    desc = meta.get("description", "")
    nav = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        nav += f'<li><a href="{href}"{cur}>{label}</a></li>'
    ld = json.dumps(jsonld, ensure_ascii=False, indent=None)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{BASE}{path}">
<link rel="stylesheet" href="/style.css">
<link rel="alternate" type="application/rss+xml" title="New entries" href="{BASE}/feed.xml">
<link rel="alternate" type="application/feed+json" title="New entries" href="{BASE}/feed.json">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="{html.escape(full_title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:type" content="website">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
<p class="brand"><a href="/">Your stack does that.</a></p>
<nav aria-label="Site"><ul>{nav}</ul></nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
<p>Every word on this site, including the slogan, is released to the public domain under <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a>. Nobody owns this phrase, including us. Copy it, print it, say it.</p>
<p>No accounts, no tracking, no cookies, nothing for sale. Entries come from <a href="{REPO}">a public repository</a>. <a href="/check-back/">Have your stack check back</a> instead of subscribing.</p>
<p>Maintained by <a href="https://johnrector.me/">John Rector</a>.</p>
</footer>
</body>
</html>
"""


def person():
    return {"@type": "Person", "name": "John Rector", "url": "https://johnrector.me/"}


def website_ld():
    return {
        "@type": "WebSite",
        "@id": f"{BASE}/#website",
        "url": f"{BASE}/",
        "name": SITE_NAME,
        "description": "Your stack does that. The slogan of the era after apps, and a useful place for people who believe it.",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "inLanguage": "en",
        "publisher": person(),
    }


def article_ld(meta, path, body_html):
    return {
        "@type": "Article",
        "@id": f"{BASE}{path}#article",
        "mainEntityOfPage": f"{BASE}{path}",
        "url": f"{BASE}{path}",
        "headline": meta["title"],
        "description": meta.get("description", ""),
        "author": person(),
        "publisher": person(),
        "datePublished": meta.get("date", "2026-09-06"),
        "dateModified": meta.get("modified", meta.get("date", "2026-09-06")),
        "inLanguage": "en",
        "isPartOf": {"@id": f"{BASE}/#website"},
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "articleBody": strip_tags(body_html),
    }


def does_item_ld(e, position):
    text = "\n\n".join(
        f"{label}: {strip_tags(md_block(e['parts'][key]))}" for key, label in DOES_SECTIONS
    )
    return {
        "@type": "ListItem",
        "position": position,
        "item": {
            "@type": "Article",
            "@id": f"{BASE}/does/#{e['slug']}",
            "url": f"{BASE}/does/#{e['slug']}",
            "headline": e["title"],
            "datePublished": e["added"],
            "keywords": ", ".join([e["domain"]] + e["uses"]),
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "articleBody": text,
        },
    }


def ledger_item_ld(l, position):
    return {
        "@type": "ListItem",
        "position": position,
        "item": {
            "@type": "Thing",
            "@id": f"{BASE}/ledger/#{l['slug']}",
            "name": l["replaced"],
            "description": (
                ("Kept because " if l["result"] == "kept" else "Replaced by ")
                + l["replaced_by"]
                + (". " + strip_tags(md_block(l["note"])) if l["note"] else "")
            ),
        },
    }


# ---------------------------------------------------------------- pages

def build():
    # Overwrite in place. If you remove a page, delete its folder from site/ by hand.
    SITE.mkdir(exist_ok=True)
    shutil.copytree(ROOT / "static", SITE, dirs_exist_ok=True)

    does = load_does()
    ledger = load_ledger()
    does_sorted = sorted(does, key=lambda e: (e["added"], e["slug"]), reverse=True)

    # Rendered fragments that pages can include with {{...}}
    by_domain = {}
    for e in does:
        by_domain.setdefault(e["domain"], []).append(e)
    does_html = []
    toc = []
    for key, label in DOMAINS:
        items = by_domain.get(key, [])
        if not items:
            continue
        toc.append(f'<li><a href="#{key}">{label}</a> <span class="count">{len(items)}</span></li>')
        does_html.append(f'<section class="domain" id="{key}"><h2>{label}</h2>')
        does_html.extend(render_does_entry(e) for e in items)
        does_html.append("</section>")
    fragments = {
        "does_all": "\n".join(does_html),
        "does_toc": f'<ul class="toc">{"".join(toc)}</ul>',
        "does_count": str(len(does)),
        "does_recent": "\n".join(render_does_entry(e) for e in does_sorted[:6]),
        "ledger_all": '<ol class="ledger" reversed>' + "".join(render_ledger_line(l) for l in ledger) + "</ol>",
        "ledger_count": str(len(ledger)),
        "repo": REPO,
        "base": BASE,
    }

    pages = []
    for path in sorted((ROOT / "pages").glob("*.html")):
        meta, body = read_front_matter(path.read_text(encoding="utf-8"))
        url = meta["path"]
        for k, v in fragments.items():
            body = body.replace("{{" + k + "}}", v)
        kind = meta.get("type", "article")
        graph = [website_ld()]
        if kind == "article":
            graph.append(article_ld(meta, url, body))
        elif kind == "does":
            graph.append(article_ld(meta, url, body))
            graph.append(
                {
                    "@type": "ItemList",
                    "@id": f"{BASE}{url}#list",
                    "name": "Does",
                    "numberOfItems": len(does),
                    "itemListOrder": "https://schema.org/ItemListUnordered",
                    "itemListElement": [does_item_ld(e, i + 1) for i, e in enumerate(does)],
                }
            )
        elif kind == "ledger":
            graph.append(article_ld(meta, url, body))
            graph.append(
                {
                    "@type": "ItemList",
                    "@id": f"{BASE}{url}#list",
                    "name": "The Cancel Ledger",
                    "numberOfItems": len(ledger),
                    "itemListElement": [ledger_item_ld(l, i + 1) for i, l in enumerate(ledger)],
                }
            )
        elif kind == "home":
            graph.append(
                {
                    "@type": "WebPage",
                    "@id": f"{BASE}/#page",
                    "url": f"{BASE}/",
                    "name": SITE_NAME,
                    "isPartOf": {"@id": f"{BASE}/#website"},
                    "text": strip_tags(body),
                }
            )
        elif kind == "reading":
            graph.append(article_ld(meta, url, body))
        jsonld = {"@context": "https://schema.org", "@graph": graph}
        out = SITE / url.strip("/") / "index.html" if url != "/" else SITE / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(layout(meta, body, jsonld, url), encoding="utf-8")
        pages.append((url, meta.get("modified", meta.get("date", "2026-09-06")), meta.get("noindex") == "true"))

    # 404
    meta = {"title": "Not here", "description": "That page does not exist."}
    body = "<h1>Not here.</h1><p>That page does not exist. Try the <a href=\"/does/\">Does list</a> or the <a href=\"/\">front page</a>.</p>"
    (SITE / "404.html").write_text(
        layout(meta, body, {"@context": "https://schema.org", "@graph": [website_ld()]}, "/404.html"),
        encoding="utf-8",
    )

    write_feeds(does_sorted, ledger)
    write_sitemap(pages)
    print(f"built {len(pages)} pages, {len(does)} Does entries, {len(ledger)} ledger lines")


def write_feeds(does_sorted, ledger):
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    def rfc822(iso):
        return datetime.strptime(iso, "%Y-%m-%d").strftime("%a, %d %b %Y 06:00:00 +0000")

    def esc(s):
        return html.escape(s, quote=False)

    items = []
    for e in does_sorted:
        text = "\n\n".join(
            f"{label}: {strip_tags(md_block(e['parts'][key]))}" for key, label in DOES_SECTIONS
        )
        items.append(
            f"<item><title>{esc(e['title'])}</title>"
            f"<link>{BASE}/does/#{e['slug']}</link>"
            f"<guid isPermaLink=\"true\">{BASE}/does/#{e['slug']}</guid>"
            f"<pubDate>{rfc822(e['added'])}</pubDate>"
            f"<category>does</category><category>{esc(e['domain'])}</category>"
            f"<description>{esc(text)}</description></item>"
        )
    for l in ledger:
        verb = "Kept" if l["result"] == "kept" else "Replaced"
        by = ("Kept because " if l["result"] == "kept" else "Replaced by ") + l["replaced_by"]
        text = by + (". " + strip_tags(md_block(l["note"])) if l["note"] else "")
        items.append(
            f"<item><title>{esc(verb + ': ' + l['replaced'])}</title>"
            f"<link>{BASE}/ledger/#{l['slug']}</link>"
            f"<guid isPermaLink=\"true\">{BASE}/ledger/#{l['slug']}</guid>"
            f"<pubDate>{rfc822(l['date'])}</pubDate>"
            f"<category>ledger</category>"
            f"<description>{esc(text)}</description></item>"
        )
    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
        f"<title>{SITE_NAME}</title>\n<link>{BASE}/</link>\n"
        "<description>New Does entries and Cancel Ledger lines. Give your stack a scheduled task to read this once a week.</description>\n"
        f'<atom:link href="{BASE}/feed.xml" rel="self" type="application/rss+xml"/>\n'
        "<language>en</language>\n"
        f"<lastBuildDate>{now}</lastBuildDate>\n"
        '<copyright>CC0 1.0 Universal. Public domain.</copyright>\n'
        + "\n".join(items)
        + "\n</channel>\n</rss>\n"
    )
    (SITE / "feed.xml").write_text(rss, encoding="utf-8")

    does_json = {
        "site": BASE,
        "title": "Does",
        "description": "Every Does entry on yourstackdoesthat.com. Newest first. Public domain (CC0).",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "format": "Each entry has the same four parts: need, bought, does, how. 'uses' names the parts of a stack involved: connector, skill, scheduled task, memory.",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(does_sorted),
        "entries": [
            {
                "id": e["slug"],
                "url": f"{BASE}/does/#{e['slug']}",
                "title": e["title"],
                "domain": e["domain"],
                "added": e["added"],
                "uses": e["uses"],
                "setup": e["setup"],
                "need": strip_tags(md_block(e["parts"]["need"])),
                "bought": strip_tags(md_block(e["parts"]["bought"])),
                "does": strip_tags(md_block(e["parts"]["does"])),
                "how": strip_tags(md_block(e["parts"]["how"])),
            }
            for e in does_sorted
        ],
    }
    (SITE / "does.json").write_text(json.dumps(does_json, ensure_ascii=False, indent=1), encoding="utf-8")

    ledger_json = {
        "site": BASE,
        "title": "The Cancel Ledger",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "updated": does_json["updated"],
        "count": len(ledger),
        "lines": [
            {
                "id": l["slug"],
                "url": f"{BASE}/ledger/#{l['slug']}",
                "date": l["date"],
                "result": l["result"],
                "what_it_was": l["replaced"],
                "cost": l["cost"],
                "replaced_by" if l["result"] != "kept" else "kept_because": l["replaced_by"],
                "note": strip_tags(md_block(l["note"])) if l["note"] else "",
            }
            for l in ledger
        ],
    }
    (SITE / "ledger.json").write_text(json.dumps(ledger_json, ensure_ascii=False, indent=1), encoding="utf-8")

    # JSON Feed 1.1, for stacks that prefer it over RSS
    jf_items = []
    for e in does_sorted:
        text = "\n\n".join(
            f"{label}: {strip_tags(md_block(e['parts'][key]))}" for key, label in DOES_SECTIONS
        )
        jf_items.append(
            {
                "id": f"{BASE}/does/#{e['slug']}",
                "url": f"{BASE}/does/#{e['slug']}",
                "title": e["title"],
                "content_text": text,
                "date_published": f"{e['added']}T06:00:00Z",
                "tags": ["does", e["domain"]] + e["uses"],
            }
        )
    for l in ledger:
        verb = "Kept" if l["result"] == "kept" else "Replaced"
        jf_items.append(
            {
                "id": f"{BASE}/ledger/#{l['slug']}",
                "url": f"{BASE}/ledger/#{l['slug']}",
                "title": f"{verb}: {l['replaced']}",
                "content_text": (("Kept because " if l["result"] == "kept" else "Replaced by ") + l["replaced_by"]
                                 + (". " + strip_tags(md_block(l["note"])) if l["note"] else "")),
                "date_published": f"{l['date']}T06:00:00Z",
                "tags": ["ledger", l["result"]],
            }
        )
    jf_items.sort(key=lambda i: i["date_published"], reverse=True)
    jf = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": SITE_NAME,
        "home_page_url": f"{BASE}/",
        "feed_url": f"{BASE}/feed.json",
        "description": "New Does entries and Cancel Ledger lines. Give your stack a scheduled task to read this once a week.",
        "language": "en",
        "items": jf_items,
    }
    (SITE / "feed.json").write_text(json.dumps(jf, ensure_ascii=False, indent=1), encoding="utf-8")


def write_sitemap(pages):
    urls = []
    for url, mod, noindex in pages:
        if noindex:
            continue
        urls.append(f"<url><loc>{BASE}{url}</loc><lastmod>{mod}</lastmod></url>")
    sm = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (SITE / "sitemap.xml").write_text(sm, encoding="utf-8")


if __name__ == "__main__":
    build()
