#!/usr/bin/env python3
"""Insert GitHub-rendered README HTML into the site template.

Usage: build.py TEMPLATE RENDERED_HTML OUTPUT

RENDERED_HTML is the body returned by GitHub's Markdown API. GitHub's own
renderer produces it, so the result matches github.com exactly. The only
edit is removing the heading permalink anchors, which are page chrome.
"""
import re
import sys

template_path, readme_path, out_path = sys.argv[1:4]

html = open(readme_path, encoding="utf-8").read()

# Unwrap <div id="readme"><article>...</article></div> if the readme endpoint added it.
m = re.search(r"<article[^>]*>(.*)</article>", html, re.S)
if m:
    html = m.group(1)

# Drop heading permalink widgets (<a class="anchor" ...><svg ...></svg></a>).
html = re.sub(r'<a [^>]*class="anchor"[^>]*>.*?</a>', "", html, flags=re.S)

template = open(template_path, encoding="utf-8").read()
marker = "<!-- README -->"
if marker not in template:
    sys.exit("template is missing the README marker")

open(out_path, "w", encoding="utf-8").write(template.replace(marker, html.strip()))
print(f"wrote {out_path}")
