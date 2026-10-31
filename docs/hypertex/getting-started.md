# Get started

## Open your first document

The repository includes `examples/oscillator.htex`, a set of notes on the harmonic oscillator.
It uses equation numbers, cross-references, theorem environments, a collapsible proof, a parameter slider and Hangul in math, all in one document.

=== "In the viewer"

    ```bash
    htex view examples/oscillator.htex
    ```

    With the installed app, you can also double-click the file or drag it onto the window.

=== "As HTML"

    ```bash
    htex html examples/oscillator.htex -o oscillator.html
    ```

    The resulting `oscillator.html` opens in any browser.

=== "Through the web server"

    ```bash
    htex serve tests/docs
    ```

    Then open `http://127.0.0.1:8000/` in your browser.

## Open Markdown and HTML files

The viewer also opens Markdown notes (`.md`) and HTML pages (`.html`) from your computer.
Markdown math is written as `$…$` inline or `$$…$$` on its own lines, and links to other notes open in the viewer.

```bash
htex view notes/README.md
htex html notes/README.md -o readme.html      # or convert one to HTML
htex build notes -o site                      # or a whole folder of .md and .htex files
```

## Write a document

A HyperTeX document is almost plain LaTeX. Set the document class to `hypertex`.

```latex
\documentclass{hypertex}
\title{Notes on the harmonic oscillator}
\author{Jane Doe}
\parameter{\omega}{0.5}{3}{1}[step=0.1]

\begin{document}
\maketitle

\section{The Hamiltonian}\label{sec:H}
\begin{equation}\label{eq:H}
  H = \frac{p^2}{2m} + \frac{1}{2} m\omega^2 x^2
\end{equation}
Move $\omega$ with the slider and watch equation~\eqref{eq:H}.
\end{document}
```

A value declared as `\parameter{name}{min}{max}{default}` appears as a slider in the viewer.

## Publish a static website

Turn a folder of `.htex` documents into an ordinary website:

```bash
htex build my-notes -o site
```

Upload the `site` folder to any static host, such as GitHub Pages or Cloudflare.

## The viewer window

The viewer is laid out like Google Chrome. From the top: tabs, the toolbar (back, forward, reload, home,
the address bar and the ⋮ menu), the bookmarks bar, and the page. New tabs and the home button open a start page
with an address box and shortcuts to your bookmarks.

The button at the left of the address bar shows the document's diagnostics, such as errors or compatibility mode.
Click ☆ at the right to bookmark the page.

## Viewer shortcuts

On macOS, use Cmd instead of Ctrl.

| Action | Keys |
| --- | --- |
| New tab, close tab | Ctrl+T, Ctrl+W |
| Switch tabs | Ctrl+Tab, Ctrl+1…9 |
| Open link in new tab | Middle-click or Ctrl+click |
| Close a tab | Middle-click the tab |
| Find | Ctrl+F (next: Enter or F3, previous: Shift+Enter) |
| Zoom in, out, reset | Ctrl+=, Ctrl+-, Ctrl+0 |
| View source (.htex) | Ctrl+U |
| Back, forward, home | Alt+←, Alt+→, Alt+Home |
| Reload, address bar | Ctrl+R, Ctrl+L |
| Bookmark this page, show or hide the bookmarks bar | Ctrl+D, Ctrl+Shift+B |

Choose the theme (system, light, dark) and the home page from the ⋮ menu. Local documents you have open redraw
automatically each time you save them.
