"""Build Main/final_Content.md from the module overview and the eight chapter files.

Run from the repository root:  python3 tools/build_final_content.py
- Chapter headings become "Chapter N: Title".
- Repeated headings (Learning Outcomes, Answer Key, Glossary, ...) get a chapter suffix,
  so every heading has a unique anchor; links inside each chapter are updated to match.
- Relative image and file links are rewritten so they work from Main/.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, 'Main')
SRC = os.path.join(MAIN, 'study-guide', 'V3.0-final')
OUT = os.path.join(MAIN, 'final_Content.md')
GENERIC = ['Table of Contents', 'Learning Outcomes', 'Where This Chapter Fits',
           'Answer Key', 'Glossary', 'References']

def slug(h):
    s = h.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')

def relink(text, folder):
    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|#)', target):
            return m.group(0)
        path, _, frag = target.partition('#')
        new = os.path.relpath(os.path.normpath(os.path.join(folder, path)), MAIN).replace(os.sep, '/')
        return f'{label}({new}{"#" + frag if frag else ""})'
    return re.sub(r'(!?\[[^\]]*\])\(([^)\s]+)\)', fix, text)

def chapter_files():
    files = [os.path.join(SRC, '00-module-overview', 'module-overview.md')]
    chs = sorted(glob.glob(os.path.join(SRC, 'chapter-*', '*.md')),
                 key=lambda p: int(re.search(r'chapter-(\d+)', p).group(1)))
    return files + chs

parts, toc = [], []
for path in chapter_files():
    folder = os.path.dirname(path)
    text = open(path, encoding='utf-8').read()
    m = re.search(r'chapter-(\d+)', path)
    n = int(m.group(1)) if m else 0
    lines = text.split('\n')
    title = lines[0].lstrip('# ').strip()
    if n:
        lines[0] = f'# Chapter {n}: {title}'
        body = '\n'.join(lines)
        for g in GENERIC:
            body = re.sub(rf'^## {re.escape(g)}$', f'## {g} (Chapter {n})', body, flags=re.M)
            body = body.replace(f'(#{slug(g)})', f'(#{slug(g + f" (Chapter {n})")})')
    else:
        body = '\n'.join(lines)
    body = relink(body, folder)
    toc.append(f'- [{lines[0].lstrip("# ").strip()}](#{slug(lines[0].lstrip("# "))})')
    parts.append(body.strip())

header = """# AI Overview: Final Markdown Content (V3.0)

**Team:** BABI GULING · **Module:** AI Overview · **Version:** V3.0 (Final, Stage 3) · **Date:** November 2026

This file combines the module overview and the eight final chapters. It is generated from `Main/study-guide/V3.0-final/` by `tools/build_final_content.py`; edit the chapter files, not this file. Earlier versions are kept in `archive/`.

## Contents

""" + '\n'.join(toc) + '\n\n---\n'
open(OUT, 'w', encoding='utf-8').write(header + '\n' + '\n\n---\n\n'.join(parts) + '\n')
print('wrote', os.path.relpath(OUT, ROOT)) 
