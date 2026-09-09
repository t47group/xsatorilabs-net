#!/usr/bin/env python3
"""
Static blog generator. Zero dependencies (stdlib only) so the daily cron
cannot rot when a pip package changes.

- Reads posts/*.md with simple `key: value` frontmatter between --- fences.
- Renders only posts whose `date` is <= today (UTC). Future-dated posts stay
  invisible until their day arrives -> that is the drip.
- Emits clean URLs: blog/<slug>/index.html
- Emits blog/index.html, rss.xml, sitemap.xml, robots.txt
- Theme + identity come from site.json so one engine serves every property.
"""
import json, os, re, html, datetime, xml.sax.saxutils as sx

ROOT = os.path.dirname(os.path.abspath(__file__))
CFG  = json.load(open(os.path.join(ROOT, "site.json"), encoding="utf-8"))
POSTS_DIR = os.path.join(ROOT, "posts")
BLOG_DIR  = os.path.join(ROOT, "blog")
TODAY = datetime.date.today()

# ---------------------------------------------------------------- frontmatter
def parse_post(path):
    raw = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    if not raw.startswith("---"):
        raise ValueError(f"{path}: missing frontmatter")
    _, fm, body = raw.split("---", 2)
    meta = {}
    for line in fm.strip().split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        meta[k.strip()] = v
    meta["tags"] = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
    meta["date"] = datetime.date.fromisoformat(meta["date"])
    meta["slug"] = meta.get("slug") or os.path.basename(path)[:-3]
    meta["body"] = body.strip()
    return meta

# ---------------------------------------------------------------- md -> html
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    return t

def md(body):
    out, i = [], 0
    lines = body.split("\n")
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        if s.startswith("### "):
            out.append(f"<h3>{inline(s[4:])}</h3>"); i += 1; continue
        if s.startswith("## "):
            out.append(f"<h2>{inline(s[3:])}</h2>"); i += 1; continue
        if s in ("---", "***"):
            out.append("<hr />"); i += 1; continue
        if s.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                buf.append(lines[i].strip()[2:]); i += 1
            out.append(f"<blockquote><p>{inline(' '.join(buf))}</p></blockquote>"); continue
        if re.match(r"^[-*] ", s):
            buf = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i].strip()):
                buf.append(lines[i].strip()[2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in buf) + "</ul>"); continue
        if re.match(r"^\d+\. ", s):
            buf = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                buf.append(re.sub(r"^\d+\.\s*", "", lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in buf) + "</ol>"); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{2,3} |[-*] |\d+\. |> |---$)", lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)

# ---------------------------------------------------------------- shell/theme
def head(title, desc, canonical, extra_ld=None, og_type="article"):
    t = CFG["theme"]
    css = f""":root{{{';'.join(f'--{k}:{v}' for k,v in t['vars'].items())};--serif:{t['serif']}}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:{t['sans']};color:var(--ink);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased;
background-image:{t['bgimage']};background-attachment:fixed}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:{t.get('wrap','760px')};margin:0 auto;padding:0 26px}}
header{{position:sticky;top:0;z-index:10;backdrop-filter:blur(10px);background:{t['headerbg']};border-bottom:1px solid var(--line)}}
.nav{{display:flex;align-items:center;justify-content:space-between;height:70px;max-width:1120px;margin:0 auto;padding:0 26px}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:.3px;font-size:17px}}
.logo{{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;font-family:var(--serif);font-weight:700;font-size:15px;color:{t['logoink']};background:{t['accentgrad']};box-shadow:{t['logoshadow']}}}
.brand small{{display:block;color:var(--muted);font-weight:600;font-size:11px;letter-spacing:1.4px;text-transform:uppercase;margin-top:2px}}
nav .links{{display:flex;gap:28px;align-items:center}}
nav .links a{{color:var(--muted);font-size:14.5px;font-weight:600;transition:color .15s}}
nav .links a:hover{{color:var(--ink)}}
nav .links a.on{{color:var(--ink)}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;border-radius:10px;font-weight:700;font-size:14px;background:{t['accentgrad']};color:{t['logoink']};transition:transform .15s,box-shadow .15s}}
.btn:hover{{transform:translateY(-1px);box-shadow:{t['logoshadow']}}}
@media(max-width:760px){{nav .links a:not(.btn){{display:none}}}}
.phead{{padding:74px 0 34px;border-bottom:1px solid var(--line)}}
.kicker{{font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent2);margin-bottom:18px;display:block}}
h1{{font-family:var(--serif);font-size:clamp(30px,5vw,48px);line-height:1.1;font-weight:700;letter-spacing:-.5px;margin-bottom:18px}}
.meta{{color:var(--faint);font-size:13.5px;display:flex;gap:14px;flex-wrap:wrap;align-items:center}}
.meta .dot{{opacity:.5}}
article{{padding:38px 0 20px;font-size:17px}}
article p{{margin-bottom:22px;color:var(--prose)}}
article h2{{font-family:var(--serif);font-size:clamp(22px,3.4vw,29px);font-weight:700;letter-spacing:-.3px;margin:42px 0 16px}}
article h3{{font-size:19px;font-weight:800;margin:30px 0 12px}}
article ul,article ol{{margin:0 0 22px 22px;color:var(--prose)}}
article li{{margin-bottom:9px}}
article a{{color:var(--accent2);border-bottom:1px solid var(--line)}}
article a:hover{{border-bottom-color:var(--accent2)}}
article blockquote{{border-left:3px solid var(--accent);padding:4px 0 4px 20px;margin:0 0 22px;color:var(--muted);font-style:italic}}
article code{{background:var(--card);border:1px solid var(--line);border-radius:5px;padding:2px 6px;font-size:14.5px}}
article hr{{border:none;border-top:1px solid var(--line);margin:34px 0}}
article strong{{color:var(--ink)}}
.tags{{display:flex;gap:8px;flex-wrap:wrap;margin:34px 0 0}}
.tag{{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--accent2);border:1px solid var(--line);border-radius:999px;padding:6px 12px;background:var(--card)}}
.bio{{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;margin:38px 0 0}}
.bio .av{{width:46px;height:46px;border-radius:50%;flex:none;display:grid;place-items:center;font-family:var(--serif);font-weight:700;color:{t['logoink']};background:{t['accentgrad']}}}
.bio b{{font-size:15px}}
.bio p{{color:var(--muted);font-size:14px;margin:5px 0 0}}
.bio a{{color:var(--accent2)}}
.postlist{{padding:14px 0 40px}}
.item{{display:block;border-bottom:1px solid var(--line);padding:26px 0;transition:opacity .15s}}
.item:hover{{opacity:.82}}
.item .d{{font-size:12.5px;color:var(--faint);letter-spacing:.4px;margin-bottom:9px}}
.item h2{{font-family:var(--serif);font-size:clamp(20px,3vw,26px);font-weight:700;letter-spacing:-.3px;margin-bottom:9px}}
.item p{{color:var(--muted);font-size:15px}}
.item .more{{display:inline-block;margin-top:12px;font-size:13.5px;font-weight:700;color:var(--accent2)}}
.cta{{text-align:center;background:{t['ctabg']};border:1px solid var(--line);border-radius:22px;padding:46px 28px;margin:46px 0}}
.cta h2{{font-family:var(--serif);font-size:clamp(23px,3.6vw,31px);font-weight:700;margin-bottom:11px}}
.cta p{{color:var(--muted);max-width:52ch;margin:0 auto 22px}}
footer{{border-top:1px solid var(--line);margin-top:40px;padding:32px 0}}
.foot{{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;color:var(--faint);font-size:13.5px;max-width:1120px;margin:0 auto;padding:0 26px}}
.foot a{{color:var(--muted)}} .foot a:hover{{color:var(--ink)}}
.backlink{{display:inline-block;margin:26px 0 0;font-size:14px;color:var(--muted);font-weight:600}}"""
    ld = json.dumps(extra_ld, ensure_ascii=False, indent=None) if extra_ld else None
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="{og_type}" />
<meta property="og:title" content="{html.escape(title, quote=True)}" />
<meta property="og:description" content="{html.escape(desc, quote=True)}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="{html.escape(CFG['name'])}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{html.escape(title, quote=True)}" />
<meta name="twitter:description" content="{html.escape(desc, quote=True)}" />
<link rel="alternate" type="application/rss+xml" title="{html.escape(CFG['name'])} — Insights" href="{CFG['url']}/rss.xml" />
<style>{css}</style>
{f'<script type="application/ld+json">{ld}</script>' if ld else ''}
</head>
<body>
<header><div class="nav">
  <a class="brand" href="{CFG['url']}/">
    <div class="logo">{CFG['logo']}</div>
    <div>{CFG['name']} <small>{CFG['tagline']}</small></div>
  </a>
  <nav class="links">
    {''.join(f'<a href="{h}">{n}</a>' for n,h in CFG['nav'])}
    <a class="on" href="{CFG['url']}/blog/">Insights</a>
    <a class="btn" href="{CFG['cta_href']}">{CFG['cta_label']}</a>
  </nav>
</div></header>
<main>"""

def foot():
    links = " · ".join(f'<a href="{h}">{n}</a>' for n, h in CFG["footer_links"])
    return f"""</main>
<footer><div class="foot">
  <div>{CFG['footer_note']}</div>
  <div>{links}</div>
</div></footer>
</body>
</html>"""

# ---------------------------------------------------------------- schema
def person_ld():
    a = CFG.get("author")
    if not a: return None
    return {"@type": "Person", "name": a["name"], "url": a["url"],
            "jobTitle": a.get("jobTitle", ""), "sameAs": a.get("sameAs", [])}

def org_ld():
    o = {"@type": "Organization", "name": CFG["name"], "url": CFG["url"] + "/"}
    if CFG.get("org_sameas"): o["sameAs"] = CFG["org_sameas"]
    if CFG.get("author"): o["founder"] = person_ld()
    return o

def article_ld(p, url):
    author = person_ld() or {"@type": "Organization", "name": CFG["name"], "url": CFG["url"] + "/"}
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "headline": p["title"], "description": p["description"],
         "datePublished": p["date"].isoformat(), "dateModified": p["date"].isoformat(),
         "url": url, "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "author": author, "publisher": org_ld(),
         "keywords": ", ".join(p["tags"]), "inLanguage": "en-US"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": CFG["url"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": CFG["url"] + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}]}

# ---------------------------------------------------------------- render
def render_post(p):
    url = f"{CFG['url']}/blog/{p['slug']}/"
    out = [head(f"{p['title']} — {CFG['name']}", p["description"], url, article_ld(p, url))]
    byline = CFG["author"]["name"] if CFG.get("author") else CFG["name"]
    out.append(f"""<div class="wrap phead">
  <span class="kicker">{html.escape(p.get('kicker','Insights'))}</span>
  <h1>{html.escape(p['title'])}</h1>
  <div class="meta"><span>{byline}</span><span class="dot">·</span>
  <time datetime="{p['date'].isoformat()}">{p['date'].strftime('%B %-d, %Y')}</time>
  <span class="dot">·</span><span>{p['readtime']} min read</span></div>
</div>
<div class="wrap"><article>{md(p['body'])}</article>""")
    if p["tags"]:
        out.append('<div class="tags">' + "".join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"]) + "</div>")
    if CFG.get("author"):
        a = CFG["author"]
        out.append(f"""<div class="bio"><div class="av">{a['initials']}</div>
        <div><b>{a['name']}</b><p>{a['bio']} <a href="{a['url']}">{a['url'].replace('https://','')}</a></p></div></div>""")
    out.append(f"""<div class="cta"><h2>{CFG['cta_head']}</h2><p>{CFG['cta_copy']}</p>
      <a class="btn" href="{CFG['cta_href']}">{CFG['cta_label']}</a></div>
      <a class="backlink" href="{CFG['url']}/blog/">← All insights</a></div>""")
    out.append(foot())
    d = os.path.join(BLOG_DIR, p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write("\n".join(out))

def render_index(posts):
    url = f"{CFG['url']}/blog/"
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": f"{CFG['name']} — Insights",
          "url": url, "description": CFG["blog_desc"], "publisher": org_ld(),
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"],
                        "url": f"{CFG['url']}/blog/{p['slug']}/",
                        "datePublished": p["date"].isoformat()} for p in posts[:20]]}
    out = [head(f"Insights — {CFG['name']}", CFG["blog_desc"], url, ld, og_type="website")]
    out.append(f"""<div class="wrap phead"><span class="kicker">Insights</span>
      <h1>{CFG['blog_head']}</h1><div class="meta"><span>{CFG['blog_desc']}</span></div></div>
      <div class="wrap postlist">""")
    if not posts:
        out.append('<p style="color:var(--muted);padding:40px 0">First posts publishing shortly.</p>')
    for p in posts:
        out.append(f"""<a class="item" href="{CFG['url']}/blog/{p['slug']}/">
          <div class="d">{p['date'].strftime('%B %-d, %Y')} · {p['readtime']} min read</div>
          <h2>{html.escape(p['title'])}</h2><p>{html.escape(p['description'])}</p>
          <span class="more">Read →</span></a>""")
    out.append(f"""</div><div class="wrap"><div class="cta"><h2>{CFG['cta_head']}</h2>
      <p>{CFG['cta_copy']}</p><a class="btn" href="{CFG['cta_href']}">{CFG['cta_label']}</a></div></div>""")
    out.append(foot())
    os.makedirs(BLOG_DIR, exist_ok=True)
    open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8").write("\n".join(out))

def render_feeds(posts):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    items = "".join(f"""<item><title>{sx.escape(p['title'])}</title>
<link>{CFG['url']}/blog/{p['slug']}/</link>
<guid isPermaLink="true">{CFG['url']}/blog/{p['slug']}/</guid>
<description>{sx.escape(p['description'])}</description>
<pubDate>{datetime.datetime.combine(p['date'], datetime.time(13,0,tzinfo=datetime.timezone.utc)).strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
</item>""" for p in posts[:30])
    open(os.path.join(ROOT, "rss.xml"), "w", encoding="utf-8").write(
f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>{sx.escape(CFG['name'])} — Insights</title>
<link>{CFG['url']}/blog/</link>
<description>{sx.escape(CFG['blog_desc'])}</description>
<language>en-us</language><lastBuildDate>{now}</lastBuildDate>
{items}</channel></rss>""")

    urls = [(CFG["url"] + "/", "1.0", "weekly"), (CFG["url"] + "/blog/", "0.9", "daily")]
    urls += [(f"{CFG['url']}/blog/{p['slug']}/", "0.8", "monthly") for p in posts]
    body = "".join(f"<url><loc>{u}</loc><changefreq>{c}</changefreq><priority>{pr}</priority></url>"
                   for u, pr, c in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        f"""<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>""")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {CFG['url']}/sitemap.xml\n")

# ---------------------------------------------------------------- main
def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    allp = [parse_post(os.path.join(POSTS_DIR, f))
            for f in sorted(os.listdir(POSTS_DIR)) if f.endswith(".md")]
    for p in allp:
        words = len(re.sub(r"[#*`>\[\]()-]", " ", p["body"]).split())
        p["readtime"] = max(2, round(words / 220))
    live = sorted([p for p in allp if p["date"] <= TODAY], key=lambda p: p["date"], reverse=True)
    queued = [p for p in allp if p["date"] > TODAY]
    for p in live:
        render_post(p)
    render_index(live); render_feeds(live)
    print(f"[{CFG['name']}] live={len(live)} queued={len(queued)} today={TODAY}")
    if queued:
        nxt = min(queued, key=lambda p: p["date"])
        print(f"  next: {nxt['date']} — {nxt['title']}")

if __name__ == "__main__":
    main()
