"""MkDocs hook: HyperTeX examples (examples/ → https://krunyx.com/examples/).

Each folder under examples/ with an example.yml is one example. At build time this hook

1. copies the example files unchanged to site/examples/<name>/, so HyperTeX can open them at
   htex://krunyx.com/examples/<name>/<file> (MkDocs never touches them, not even the .md files);
2. writes site/examples/index.htex, a HyperTeX page listing every example;
3. runs `htex build` (the hypertex package from requirements.txt) to make plain-web copies under
   site/examples/web/ for readers without HyperTeX;
4. fills the gallery on docs/hypertex/examples.md where the page says <!-- examples:gallery -->.

example.yml fields: title, summary, order (smaller first), main (file opened first), and files: a list of
{path, about}. Adding an example = adding a folder with its files and an example.yml. Nothing else to edit.
"""
from __future__ import annotations

import logging
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import yaml

log = logging.getLogger("mkdocs.hooks.examples")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "examples"
SITE_HOST = "krunyx.com"
URL_PATH = "examples"                 # site/examples/…
WEB_DIR = "web"                       # site/examples/web/… (htex build output)
SOURCE_URL = "https://github.com/krunyx/krunyx.com/blob/main/examples"
MARKER = "<!-- examples:gallery -->"
SKIP = {"example.yml", ".DS_Store"}
DOC_EXTS = (".htex", ".tex", ".md", ".markdown")
KIND = {".htex": "HyperTeX", ".tex": "LaTeX", ".md": "Markdown", ".html": "HTML", ".csv": "Data",
        ".pdf": "PDF", ".bib": "BibTeX"}


@dataclass
class Example:
    name: str
    title: str
    summary: str
    order: int
    main: str
    files: list[dict] = field(default_factory=list)


def load_examples() -> list[Example]:
    out = []
    for meta in sorted(SRC.glob("*/example.yml")):
        d = yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
        folder = meta.parent
        files = d.get("files") or []
        for f in files:
            if not (folder / f["path"]).is_file():
                raise FileNotFoundError(f"{meta}: listed file {f['path']} does not exist")
        out.append(Example(folder.name, d["title"], " ".join(str(d.get("summary", "")).split()),
                           int(d.get("order", 100)), d.get("main") or (files[0]["path"] if files else ""),
                           files))
    return sorted(out, key=lambda e: (e.order, e.name))


# ------------------------------------------------------------------ addresses
def htex_url(ex: Example, path: str) -> str:
    return f"htex://{SITE_HOST}/{URL_PATH}/{ex.name}/{path}"


def web_url(ex: Example, path: str) -> str:
    """Plain-web copy: documents become .html (htex build), other files stay as they are."""
    p = Path(path)
    if p.suffix.lower() in DOC_EXTS:
        p = p.with_suffix(".html")
    return f"/{URL_PATH}/{WEB_DIR}/{ex.name}/{p.as_posix()}"


def source_url(ex: Example, path: str) -> str:
    return f"{SOURCE_URL}/{ex.name}/{path}"


def opens_in_viewer(path: str) -> bool:
    return Path(path).suffix.lower() in DOC_EXTS + (".html",)


# ------------------------------------------------------------------ gallery (MkDocs page)
def gallery_markdown(examples: list[Example]) -> str:
    parts = []
    for ex in examples:
        rows = ["| File | What it shows | Open |", "| --- | --- | --- |"]
        for f in ex.files:
            path, about = f["path"], " ".join(str(f.get("about", "")).split()).replace("|", "\\|")
            kind = KIND.get(Path(path).suffix.lower(), "File")
            links = []
            if opens_in_viewer(path):
                links.append(f"[HyperTeX]({htex_url(ex, path)})")
            links.append(f"[web]({web_url(ex, path)})")
            links.append(f"[source]({source_url(ex, path)})")
            rows.append(f"| <code class=\"ex-file\">{path}</code><br><small>{kind}</small> | {about} | {' · '.join(links)} |")
        parts.append(
            f"## {ex.title}\n\n{ex.summary}\n\n"
            f"[Open in HyperTeX]({htex_url(ex, ex.main)}){{ .md-button .md-button--primary }} "
            f"[Read on the web]({web_url(ex, ex.main)}){{ .md-button }}\n\n" + "\n".join(rows) + "\n")
    return "\n".join(parts)


# ------------------------------------------------------------------ hub page (HyperTeX)
_TEX_ESC = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "$": r"\$",
            "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def tex(s: str) -> str:
    return "".join(_TEX_ESC.get(c, c) for c in s)


def hub_htex(examples: list[Example]) -> str:
    lines = [r"\documentclass{hypertex}", r"\title{HyperTeX examples}", r"\author{krunyx}",
             r"\abstract{Short documents that show what HyperTeX can do. Each example is a small set of linked "
             r"files: open one, follow its links, move the sliders, and press the edit button to change the "
             r"source and see the result at once.}",
             r"\begin{document}", r"\maketitle", ""]
    for ex in examples:
        lines.append(rf"\section{{{tex(ex.title)}}}")
        lines.append(tex(ex.summary))
        lines.append(r"\begin{itemize}")
        for f in ex.files:
            about = " ".join(str(f.get("about", "")).split())
            lines.append(rf"  \item \href{{{ex.name}/{f['path']}}}{{\texttt{{{tex(f['path'])}}}}} --- {tex(about)}")
        lines.append(r"\end{itemize}")
        lines.append("")
    lines.append(r"More about HyperTeX at \href{https://krunyx.com/hypertex/}{krunyx.com/hypertex}.")
    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ MkDocs events
_examples: list[Example] = []


def on_config(config, **kwargs):
    global _examples
    _examples = load_examples()
    return config


def on_page_markdown(markdown, page, config, files, **kwargs):
    if MARKER in markdown:
        return markdown.replace(MARKER, gallery_markdown(_examples))
    return markdown


def on_post_build(config, **kwargs):
    site = Path(config["site_dir"])
    out = site / URL_PATH
    if out.exists():
        shutil.rmtree(out)
    with tempfile.TemporaryDirectory(prefix="examples-") as tmp:
        stage = Path(tmp) / "examples"
        shutil.copytree(SRC, stage, ignore=shutil.ignore_patterns(*SKIP))
        (stage / "index.htex").write_text(hub_htex(_examples), encoding="utf-8")
        shutil.copytree(stage, out)                                   # 1, 2: files as they are
        try:
            from htex.web.build import build as htex_build
        except ImportError as e:  # hypertex is in requirements.txt
            raise RuntimeError("examples: the htex package is missing (pip install -r requirements.txt)") from e
        rep = htex_build(stage, out / WEB_DIR)                       # 3: plain-web copies
        for w in rep.warnings:
            log.info("examples (htex build): %s", w)
        if rep.errors:
            raise RuntimeError(f"examples: htex build could not convert {rep.errors}")
    log.info("examples: %d examples, %d web pages", len(_examples), len(rep.documents))
