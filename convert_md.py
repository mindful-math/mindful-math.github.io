#!/usr/bin/env python3
"""
convert_md.py

Converts Hugo-flavoured (or plain) Markdown files in the current directory
into site-ready HTML thought pages, with a thoughts/index.html listing snippet
printed at the end.

Usage:
    python3 convert_md.py                      # convert all .md in current dir
    python3 convert_md.py post1.md post2.md   # convert specific files
    python3 convert_md.py --site ~/my-site    # point to a non-default site root
    python3 convert_md.py --section thoughts  # target section (thoughts|notebooks)
    python3 convert_md.py --dry-run           # preview without writing files

Requirements: Python 3.8+, no third-party packages.
"""

import argparse
import os
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path


# ── Front matter parser ──────────────────────────────────────────────────────

def parse_front_matter(text: str) -> tuple[dict, str]:
    """Strip Hugo TOML (+++...+++) or YAML (---...---) front matter.
    Returns (meta_dict, body_text)."""
    meta = {}

    # TOML front matter
    m = re.match(r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n', text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r'^\s*(\w+)\s*=\s*"?([^"]*)"?\s*$', line)
            if kv:
                meta[kv.group(1)] = kv.group(2).strip()
        return meta, text[m.end():]

    # YAML front matter
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r'^\s*(\w+):\s*(.+)$', line)
            if kv:
                meta[kv.group(1)] = kv.group(2).strip().strip('"\'')
        return meta, text[m.end():]

    return meta, text


# ── Markdown → HTML ──────────────────────────────────────────────────────────

def md_to_html(text: str) -> str:
    """
    Converts a subset of Markdown to HTML.
    Handles: headings, paragraphs, bold, italic, inline code, code fences,
    blockquotes, unordered lists, ordered lists, links, images, horizontal rules,
    Hugo <!--more--> tag, and LaTeX delimiters (passed through unchanged for MathJax).
    """

    # Remove Hugo more tag
    text = text.replace('<!--more-->', '')

    # ── Fenced code blocks (``` ... ```) — protect before other processing
    code_blocks: list[str] = []
    def save_code(m):
        lang = m.group(1).strip()
        code = _escape_html(m.group(2))
        lang_attr = f' class="language-{lang}"' if lang else ''
        code_blocks.append(f'<pre><code{lang_attr}>{code}</code></pre>')
        return f'\x00CODE{len(code_blocks)-1}\x00'
    text = re.sub(r'```(\w*)\n(.*?)```', save_code, text, flags=re.DOTALL)

    # ── Inline LaTeX — protect $...$ and $$...$$ so we don't mangle them
    math_blocks: list[str] = []
    def save_math_display(m):
        math_blocks.append(m.group(0))
        return f'\x00MATH{len(math_blocks)-1}\x00'
    def save_math_inline(m):
        math_blocks.append(m.group(0))
        return f'\x00MATH{len(math_blocks)-1}\x00'
    text = re.sub(r'\$\$.+?\$\$', save_math_display, text, flags=re.DOTALL)
    text = re.sub(r'\$[^$\n]+?\$', save_math_inline, text)

    lines = text.split('\n')
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append('</ul>')
            in_ul = False
        if in_ol:
            out.append('</ol>')
            in_ol = False

    while i < len(lines):
        line = lines[i]

        # Headings
        hm = re.match(r'^(#{1,6})\s+(.+)$', line)
        if hm:
            close_lists()
            level = len(hm.group(1))
            content = inline_md(hm.group(2))
            out.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^[-*_]{3,}\s*$', line):
            close_lists()
            out.append('<hr>')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            close_lists()
            content = inline_md(line[1:].strip())
            # Merge consecutive blockquote lines
            bq_lines = [content]
            while i + 1 < len(lines) and lines[i+1].startswith('>'):
                i += 1
                bq_lines.append(inline_md(lines[i][1:].strip()))
            out.append('<blockquote><p>' + '<br>'.join(bq_lines) + '</p></blockquote>')
            i += 1
            continue

        # Unordered list
        ulm = re.match(r'^[\-\*\+]\s+(.+)$', line)
        if ulm:
            if not in_ul:
                close_lists()
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{inline_md(ulm.group(1))}</li>')
            i += 1
            continue

        # Ordered list
        olm = re.match(r'^\d+\.\s+(.+)$', line)
        if olm:
            if not in_ol:
                close_lists()
                out.append('<ol>')
                in_ol = True
            out.append(f'<li>{inline_md(olm.group(1))}</li>')
            i += 1
            continue

        # Blank line
        if line.strip() == '':
            close_lists()
            out.append('')
            i += 1
            continue

        # Code block placeholder
        if '\x00CODE' in line:
            close_lists()
            out.append(line)
            i += 1
            continue

        # Regular paragraph line — collect until blank line or block element
        close_lists()
        para_lines = []
        while i < len(lines) and lines[i].strip() != '':
            l = lines[i]
            if (re.match(r'^#{1,6}\s', l) or re.match(r'^[-*_]{3,}\s*$', l)
                    or re.match(r'^[\-\*\+]\s', l) or re.match(r'^\d+\.\s', l)
                    or l.startswith('>')  or '\x00CODE' in l):
                break
            para_lines.append(l)
            i += 1
        if para_lines:
            content = inline_md(' '.join(para_lines))
            out.append(f'<p>{content}</p>')
        continue

    close_lists()

    result = '\n'.join(out)

    # Restore code blocks and math
    for idx, block in enumerate(code_blocks):
        result = result.replace(f'\x00CODE{idx}\x00', block)
    for idx, block in enumerate(math_blocks):
        result = result.replace(f'\x00MATH{idx}\x00', block)

    return result


def inline_md(text: str) -> str:
    """Process inline Markdown: bold, italic, code, links, images."""
    # Images before links
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
                  lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}">', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__',     r'<strong>\1</strong>', text)
    # Italic (avoid matching lone * in math)
    text = re.sub(r'\*(?!\s)(.+?)(?<!\s)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(?!\s)(.+?)(?<!\s)_',   r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`',
                  lambda m: f'<code>{_escape_html(m.group(1))}</code>', text)
    return text


def _escape_html(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ── HTML page wrapper ────────────────────────────────────────────────────────

def wrap_in_page(title: str, date: str, body_html: str, has_math: bool) -> str:
    math_head = ''
    if has_math:
        math_head = textwrap.dedent("""\
          <script>
            window.MathJax = {
              tex: { inlineMath: [['$','$'],['\\\\(','\\\\)']], displayMath: [['$$','$$'],['\\\\[','\\\\]']] },
              options: { skipHtmlTags: ['script','noscript','style','textarea','pre'] }
            };
          </script>
          <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
        """)

    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{_escape_html(title)} · thoughts · notebook</title>
          <link rel="stylesheet" href="../assets/css/main.css">
          {math_head}
        </head>
        <body>
        <div class="site-wrap">

          <header>
            <nav>
              <a href="../index.html" class="site-title">ikigai</a>
              <a href="../notebooks/index.html">experiments</a>
              <a href="../thoughts/index.html">thoughts</a>
              <a href="../quotes/index.html">quotes</a>
              <a href="../books/index.html">books</a>
              <a href="../photos/index.html">photos</a>
            </nav>
          </header>

          <main>
            <div class="page-header">
              <h1>{_escape_html(title)}</h1>
              <p class="meta">{date}</p>
            </div>

            <article class="prose">
        {textwrap.indent(body_html, '      ')}
            </article>

            <div style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--rule);">
              <a href="index.html" style="font-size:0.85rem;color:var(--ink-light);text-decoration:none;">← all thoughts</a>
            </div>
          </main>

          <footer>
            <span>built with plain html &amp; css · no framework</span>
            <a href="#">↑ top</a>
          </footer>

        </div>
        <script src="../assets/js/main.js"></script>
        </body>
        </html>
    """)


def index_entry(slug: str, title: str, date: str, excerpt: str) -> str:
    return textwrap.dedent(f"""\
        <div class="thought-card">
          <p class="thought-date">{date}</p>
          <a href="{slug}.html" class="thought-title">{_escape_html(title)}</a>
          <p class="thought-excerpt">{_escape_html(excerpt)}</p>
        </div>
    """)


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


def first_paragraph(html: str) -> str:
    """Extract text of first <p> tag for use as excerpt."""
    m = re.search(r'<p>(.*?)</p>', html, re.DOTALL)
    if not m:
        return ''
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = text.replace('\n', ' ').strip()
    return text[:180] + ('…' if len(text) > 180 else '')


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='*', help='.md files to convert')
    parser.add_argument('--site', default=None,
                        help='Path to site root (default: script directory)')
    parser.add_argument('--section', default='thoughts',
                        choices=['thoughts'],
                        help='Target section (default: thoughts)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview without writing files')
    args = parser.parse_args()

    # Resolve site root
    script_dir = Path(__file__).parent.resolve()
    site_root  = Path(args.site).resolve() if args.site else script_dir
    out_dir    = site_root / args.section

    if not out_dir.exists():
        print(f'❌  Output directory not found: {out_dir}')
        print(f'    Use --site to point to your site root.')
        sys.exit(1)

    # Collect input files
    if args.files:
        targets = [Path(f) for f in args.files]
    else:
        targets = sorted(Path('.').glob('*.md'))

    if not targets:
        print('No .md files found.')
        sys.exit(0)

    print(f'Site root : {site_root}')
    print(f'Output    : {out_dir}')
    print(f'Files     : {len(targets)}')
    if args.dry_run:
        print('DRY RUN   : no files will be written\n')
    else:
        print()

    entries = []   # (slug, title, date, excerpt) for index listing

    for md_path in targets:
        if not md_path.exists():
            print(f'⚠️  Not found: {md_path} — skipping')
            continue
        if md_path.suffix.lower() != '.md':
            print(f'⚠️  Not a .md file: {md_path} — skipping')
            continue

        text = md_path.read_text(encoding='utf-8')
        meta, body = parse_front_matter(text)

        title = meta.get('title') or md_path.stem.replace('-', ' ').replace('_', ' ')
        date  = meta.get('date') or datetime.today().strftime('%Y-%m-%d')
        slug  = slugify(md_path.stem)
        has_math = meta.get('math', '').lower() in ('true', '1', 'yes')

        # Also auto-detect math if the body contains $ signs
        if not has_math and ('$' in body or '\\(' in body):
            has_math = True

        body_html = md_to_html(body)
        excerpt   = first_paragraph(body_html)
        page_html = wrap_in_page(title, date, body_html, has_math)

        out_path = out_dir / f'{slug}.html'

        print(f'▶  {md_path.name}')
        print(f'   title   : {title}')
        print(f'   date    : {date}')
        print(f'   slug    : {slug}')
        print(f'   math    : {has_math}')
        print(f'   output  : {out_path}')

        if not args.dry_run:
            if out_path.exists():
                print(f'   ⚠️  file exists — overwriting')
            out_path.write_text(page_html, encoding='utf-8')
            print(f'   ✓ written')
        print()

        entries.append((slug, title, date, excerpt))

    # ── Print index snippet ──────────────────────────────────────────────────
    print('═' * 56)
    print(f'Converted {len(entries)} file(s).')
    print()
    print(f'Paste into {args.section}/index.html:')
    print()
    for slug, title, date, excerpt in sorted(entries, key=lambda e: e[2], reverse=True):
        print(index_entry(slug, title, date, excerpt))
    print('═' * 56)


if __name__ == '__main__':
    main()