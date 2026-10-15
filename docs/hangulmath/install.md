# Install hangulmath

The latest version is **v0.7** (2026-10-15). See [what's new](changelog.md).

## Requirements

- **XeLaTeX or LuaLaTeX.** The package uses `fontspec`; pdfLaTeX is not supported and stops with an error.
- A LaTeX kernel from 2022-06-01 or later.
- No Korean font: the symbols come from the bundled fonts.

## TeX Live and MiKTeX

`hangulmath` is distributed through [CTAN](https://ctan.org/pkg/hangulmath) and is part of TeX Live.

```bash
tlmgr install hangulmath
```

MiKTeX installs it automatically the first time a document loads it.

!!! note "Newest version"
    TeX distributions pick up a new release a few days after it reaches CTAN.
    If yours does not have v0.7 yet, install the files by hand as described below.

## Manual installation

Download the four package files from the [GitHub repository](https://github.com/krunyx/hangulmath):

- `hangulmath.sty`
- `hangulmath-metrics.def`
- `hangulmath-sans.otf`
- `hangulmath-sans-light.otf`

Put them next to your `.tex` file. For a permanent install, place them in your local `texmf` tree instead:

| Files | Folder |
| --- | --- |
| `hangulmath.sty`, `hangulmath-metrics.def` | `tex/latex/hangulmath/` |
| `hangulmath-sans.otf`, `hangulmath-sans-light.otf` | `fonts/opentype/public/hangulmath/` |

Then run `mktexlsr` if your distribution needs it.

## Overleaf

1. Upload the four files above into your project.
2. Set the compiler to **XeLaTeX** (Menu → Compiler), or add a file named `latexmkrc` containing:

    ```perl
    $pdf_mode = 5;
    ```

## Check that it works

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{hangulmath}
\begin{document}
\[ \giug + \niun = \diud, \qquad \hangulsum\tiut_{k=1}^{n} k = \frac{n(n+1)}{2} \]
\end{document}
```

Compile with `xelatex` or `lualatex`. Continue with [Usage](usage.md) for every symbol and option.
