# Changelog

Each new version is added at the top.

## v0.9 { #v0-9 }

2026-10-21.

- **One font, fewer files.** The operator commands `\hangulsum`, `\hangulint`, `\hangullim` and `\hangulopscale`
  have been removed, together with the lighter operator font, the option `opfont` and `\hangulmathopfont`.
  pdfLaTeX now needs four files and XeLaTeX three.
- To put limits below a symbol, use standard LaTeX: `\mathop{\liul}\limits_{n\to\infty}`.
- The option `opfont` is still accepted, with a warning, so old documents compile.
  Documents that use the removed commands need to be updated.
- The manual compiles with pdfLaTeX as well as XeLaTeX.

## v0.8 { #v0-8 }

2026-10-21.

- **Works with pdfLaTeX**, and with `latex` followed by `dvips` or `dvipdfmx`.
  The bundled font is also shipped as a Type 1 font with TFM metrics and a map file; the output matches XeLaTeX.
- The symbols can be copied and searched in PDFs made with pdfLaTeX.
- Under pdfLaTeX the option `font` is ignored with a warning, since only XeLaTeX and LuaLaTeX can load other fonts.

## v0.7 { #v0-7 }

2026-10-15.

- **Works with kotex** (xetexko and luatexko) in either package order. The symbols always use the bundled symbol font, never kotex's Korean text font.
- **New `\hangulsym{<name>}`** reaches any symbol by its official name or alias, even when another package has taken the command name.
- kotex uses `\rieul` for its own purposes, so hangulmath now leaves that name alone and prints a warning. Write ㄹ as `\liul` or `\hangulsym{rieul}`.
- New one-page English example, `hangulmath-minimal.tex`, that needs no Korean font.

## v0.6 { #v0-6 }

2026-10-11. Documentation only.

- The examples section of the manual is greatly expanded, each shown as LaTeX input and typeset output: vowels as brackets, consonants as function names, the Hamiltonian and Lagrangian, a superscript mark, arrows and element symbols.

## v0.5 { #v0-5 }

2026-10-10. First public release, on CTAN.
