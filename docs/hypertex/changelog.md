# Changelog

Each new version is added at the top.

## v0.8.2 { #v0-8-2 }

November 2026. Copy equations as LaTeX, browsing history, and a notice when a new version is out.

- **Copy equations as LaTeX**: right-click an equation and choose **Copy equation as LaTeX** to copy its source.
  Select text that contains equations and copy it, and the equations come out as `$…$` and `$$…$$` instead of
  jumbled symbols. This also works in sites built with `htex build`
- **History**: Ctrl+H (Cmd+Y on macOS) opens your browsing history, grouped by day. Search it, remove single
  entries, or clear everything
- **Update notice**: once a day HyperTeX checks whether a newer version has been released. If there is one, an
  **Update** button appears next to the ⋮ menu and opens the [download page](download.md). Nothing is downloaded or
  installed automatically. Check now or turn this off under ⋮ › Update

## v0.8.1 { #v0-8-1 }

November 2026. Bring your bookmarks over, pick up where you left off, and print.

- **Import bookmarks**: ⋮ › Bookmarks › Import bookmarks lists the Chrome, Edge, Brave, Whale, Vivaldi and Chromium
  profiles on your computer. Pick one and its bookmarks come over with their folders. From Safari, Firefox or any
  other browser, import an exported HTML bookmarks file. Bookmarks you already have are skipped
- **Folders inside folders**: bookmark folders can contain other folders, and open as submenus on the bookmarks bar
- **Continue where you left off**: HyperTeX reopens last time's tabs. Change this under ⋮ › On startup
- **Reopen a closed tab** with Ctrl+Shift+T
- **Print and save as PDF**: Ctrl+P prints the page, and ⋮ › Save as PDF… saves it as a PDF file. Pages printed in the
  dark theme now come out on white paper

## v0.8.0 { #v0-8-0 }

November 2026. Open local files faster.

- **Open file button** at the left of the address bar (the same as Ctrl+O)
- **Drag and drop**: drop documents from your file manager anywhere in the window to open them. Drop several at once
  and the rest open in new tabs

## v0.7.2 { #v0-7-2 }

November 2026. Fixes opening online documents in the downloaded app.

- **Online documents failed with `CERTIFICATE_VERIFY_FAILED`**: the app could not verify HTTPS certificates on
  most computers, so `htex://` addresses showed "Can't open this document". HyperTeX now uses your operating
  system's trust store (the same one your browser uses), with a built-in certificate list as a fallback.
  Local files were not affected

## v0.7.1 { #v0-7-1 }

November 2026. Fixes found while writing the new [examples](examples.md).

- **Theorem names in English documents**: theorems, lemmas, propositions, corollaries, definitions, examples and
  remarks are labelled in English in English documents (they showed the Korean names before)
- **BibTeX bibliographies**: `\newblock` in `.bbl` files no longer shows an error, and like LaTeX, HyperTeX looks
  first for the `.bbl` named after the document (`paper.tex` → `paper.bbl`)
- **Tables**: short numbers such as `1.5` are no longer split across lines in narrow columns
- **pgfplots**: a formula that starts with a bracket, such as `\addplot {(2/pi)*sin(x)}`, now draws
- **Examples**: three sets of linked documents (oscillator, SIR epidemic model, heat diffusion) on the new
  [Examples](examples.md) page

## v0.7.0 { #v0-7-0 }

November 2026. Edit documents right in the viewer, with a live preview beside the source.

- **Edit source**: press the ✎ button in the toolbar (or Ctrl+E) and the tab splits in two: the source on the left,
  the rendered document on the right. Stop typing for a moment and the preview redraws, keeping your scroll position
- **Works with `.htex`, `.tex`, `.md` and `.html`**: syntax highlighting, line numbers, bracket matching,
  find and replace (Ctrl+F in the editor) and undo. The editor follows the light or dark theme
- **Errors on the line**: errors and warnings from the document are marked next to the source lines that caused them
- **Save local files** with Ctrl+S. Files stay UTF-8 with their original line endings. If another program changed the
  file meanwhile, you are asked before it is replaced, and the original is backed up the first time you save
- **Save a copy of an online document**: an `htex://` document cannot be saved back to its server, so Save As
  downloads it together with the files it pulls in (`\input`, `\usemacros`, `\usestyle`, the bibliography and figures)
  and keeps them in the same folder layout on your computer. You then keep editing your local copy
- **Online documents show their `\input` files**: parts that a remote document pulls in with `\input` and similar
  commands are now fetched from the same server and shown, instead of a "file not found" warning
- While you edit, links in the preview open in a new tab, so you never leave the document you are working on.
  Closing a tab or window with unsaved changes asks whether to save

## v0.6.0 { #v0-6-0 }

November 2026. PDF figures from pdflatex papers, and an English interface.

- **PDF figures**: `\includegraphics{fig.pdf}` now shows the figure. The viewer draws the first page at twice
  screen resolution, so figures keep their original size and stay sharp
- **Figures without an extension**: `\includegraphics{fig}` finds the file the way LaTeX does, trying
  `.svg`, `.png`, `.jpg` and then `.pdf`
- **English or Korean**: menus, buttons and messages follow your system language: Korean if your system is
  in Korean, English otherwise. Change it under ⋮ › Language (takes effect after restarting)
- **Document labels follow the document**: an English paper shows "Figure 1", "Proof" and "References";
  a Korean document shows 그림, 증명 and 참고문헌, whatever the interface language
- `htex build`: when a page uses a PDF figure, the site uses an SVG or PNG with the same name if there is one,
  and warns otherwise (web browsers cannot show PDF figures)
- EPS figures are not supported; you get a warning asking for PDF, SVG or PNG instead

## v0.5.0 { #v0-5-0 }

November 2026. On macOS, tabs now sit at the very top of the window, just like Chrome.

- **Tabs in the title bar (macOS)**: the tab strip moves up beside the red, yellow and green window buttons,
  so the window loses a row and looks like Chrome. The buttons are centered on the tabs
- **Works like a title bar**: drag an empty part of the tab strip to move the window; double-click it to
  zoom or minimize, following your setting in System Settings › Desktop & Dock. Full screen hides the buttons
  and the tabs move left
- **Turn it off** in the menu bar under 보기 (View) › 탭을 제목 막대에 표시 (show tabs in the title bar)
  if you prefer the old layout. It takes effect after restarting
- Windows and Linux keep the system title bar above the tabs, as before
- The download page now explains how to open the app on macOS 15 and later, where right-click › Open no longer works

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
