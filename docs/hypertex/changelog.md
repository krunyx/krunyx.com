# Changelog

Each new version is added at the top.

## v0.2.0 { #v0-2-0 }

October 2026. Much better support for existing LaTeX papers and books.

We tested compatibility mode against real public manuscripts (the HoTT book, the Stacks Project,
the amsmath test document) and fixed what they exposed. Error reports dropped by over 99%, and
almost every formula now renders as MathML.

- **Commutative diagrams**: `\xymatrix` (xy-pic), `tikzcd` and amscd `CD`, with arrow styles and labels
- **Unknown commands in math no longer break the whole formula**: only that command is marked, the rest is drawn
- **More math**: `\mathop`, `\mathbin` and the other TeX atom commands, `\ensuremath`, `\mathchoice`,
  `{\rm …}`-style font switches, `\over` and `\choose`, `\genfrac`, and about 150 more symbols
- **Real-world macros**: `\def` with arguments (including delimited ones), `\let`, `\newenvironment`,
  `\providecommand`, `\@ifnextchar`, `\makeatletter`, and the common TeX conditionals
- **Text**: `{\bf …}`-style font switches, `\cref` and `\autoref` with English names ("Theorem 2.1"),
  accented letters such as `\c{c}` and `\v{s}`, LaTeX quotes, and books with `\chapter`
- **Quieter**: typesetting packages such as `inputenc`, `geometry` and `microtype`, and index or counter
  commands, are ignored without warnings
- **Fix**: a `$` inside a box in a formula, such as `\raisebox{…}{$\cdot$}`, no longer splits the formula

## v0.1.0 { #v0-1-0 }

October 2026. First public release.

- HyperTeX 2.0 parser: macro expansion, arithmetic expressions, document tree
- HTML and MathML renderer
- Figure renderer for a subset of TikZ and pgfplots, output as SVG
- PySide6 desktop viewer: tabs, find, zoom, view source, themes
- `htex serve` and `htex build` for ordinary browsers and static websites
- Compatibility mode for existing `.tex` files
- Installers for macOS, Windows and Linux
- Released under the Apache License 2.0
