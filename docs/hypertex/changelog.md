# Changelog

Each new version is added at the top.

## v0.4.0 { #v0-4-0 }

October 2026. Read Markdown notes and open local HTML files.

- **Markdown (`.md`)**: opens like a HyperTeX document, so tabs, find, themes, bookmarks, view source and
  auto-reload all work. Supports headings, lists and task lists, quotes, code, GitHub tables, footnotes,
  images, front matter (title, author, date, tags), GitHub and MkDocs alert boxes and `<details>` blocks
- **Math in Markdown**: `$…$`, `$$…$$`, `\[…\]`, ```` ```math ```` blocks and numbered
  `equation` / `align` environments, rendered as MathML. A price like "$5 and $10" stays plain text
- **Links between notes**: `[next](#heading)` jumps within the page; links to other `.md`, `.htex` or
  `.html` files open in the viewer. `htex build` turns a folder of Markdown into a website with working links
- **Local HTML files**: open `.html` pages from your computer with their own styles and images.
  Scripts run in an isolated sandbox and cannot read your other files
- **Not planned**: HyperTeX does not open `.hwpx` or `.docx` directly. To read a Korean HWP document,
  convert it with [hwp2x](../hwp2x/index.md), which can write Markdown or HyperTeX

## v0.3.0 { #v0-3-0 }

October 2026. A browser window that looks and works like Google Chrome.

- **Familiar layout**: tabs on top, then the toolbar (back, forward, reload, home, address bar, ⋮ menu),
  then the bookmarks bar, then the page
- **Tabs**: rounded Chrome-style tabs with icons, a loading indicator and a **+** button; they shrink
  as you open more, middle-click closes, right-click offers duplicate, close others and close to the right
- **Address bar**: a page-info button on the left shows a document's diagnostics (errors, compatibility mode),
  a zoom chip appears when you are not at 100%, and a ☆ adds or edits a bookmark
- **Bookmarks**: a bookmarks bar with folders, an overflow » menu and right-click editing;
  Ctrl+D to bookmark, Ctrl+Shift+B to show or hide the bar
- **New tab page**: new tabs and the home button open a start page with an address box and shortcut tiles
  for your bookmarks
- **⋮ menu** with a zoom row, theme and home page settings; find opens as a box at the top right;
  link addresses appear in a bubble at the bottom left; light and dark themes follow Chrome's colors

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
