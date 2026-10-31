# Install hangulmath

The latest version is **v0.9** (2026-10-21). See [what's new](changelog.md).

## Requirements

- **pdfLaTeX, XeLaTeX or LuaLaTeX.** pdfLaTeX uses the bundled Type 1 font; XeLaTeX and LuaLaTeX use the same font as OpenType. The output is the same. `latex` followed by `dvips` or `dvipdfmx` also works.
- A LaTeX kernel from 2022-06-01 or later.
- No Korean font: the symbols come from the bundled font.

## TeX Live and MiKTeX

`hangulmath` is distributed through [CTAN](https://ctan.org/pkg/hangulmath) and is part of TeX Live.

```bash
tlmgr install hangulmath
```

MiKTeX installs it automatically the first time a document loads it.

!!! note "Newest version"
    TeX distributions pick up a new release a few days after it reaches CTAN.
    If yours does not have v0.9 yet, install the files by hand as described below.

## Manual installation

Download [hangulmath.zip](https://mirrors.ctan.org/fonts/hangulmath.zip) from CTAN and unpack it.
Only a few of its files are needed, depending on the engine:

| Engine | Files |
| --- | --- |
| pdfLaTeX (4 files) | `hangulmath.sty`, `hangulmath-metrics.def`, `hangulmath-sans.pfb`, `hangulmath-sans.tfm` |
| XeLaTeX, LuaLaTeX (3 files) | `hangulmath.sty`, `hangulmath-metrics.def`, `hangulmath-sans.otf` |

Put them next to your `.tex` file. For a permanent install, place them in your local `texmf` tree instead:

| Files | Folder |
| --- | --- |
| `hangulmath.sty`, `hangulmath-metrics.def` | `tex/latex/hangulmath/` |
| `hangulmath-sans.otf` | `fonts/opentype/public/hangulmath/` |
| `hangulmath-sans.pfb` | `fonts/type1/public/hangulmath/` |
| `hangulmath-sans.tfm` | `fonts/tfm/public/hangulmath/` |
| `hangulmath.map` | `fonts/map/dvips/hangulmath/` |

Then run `mktexlsr`, and enable the map for the DVI drivers:

```bash
updmap-user --enable Map=hangulmath.map
```

With pdfLaTeX the package registers the map itself, so the font works even without `updmap`.

## Overleaf

1. Upload the four pdfLaTeX files from the table above into your project.
2. Compile with the default compiler, **pdfLaTeX**. Nothing else to set.

If your project uses XeLaTeX or LuaLaTeX instead, upload the three files for those engines.
Once Overleaf's TeX Live includes v0.9, no files need uploading at all; then delete the uploaded copies,
because files in the project take precedence over the installed package.

## Check that it works

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{hangulmath}
\begin{document}
\[ \giug + \niun = \diud, \qquad \giug_{\ah}(x) = \sum_{k} \niun_k\, x^k \]
\end{document}
```

Compile with `pdflatex`, `xelatex` or `lualatex`. Continue with [Usage](usage.md) for every symbol and option.
