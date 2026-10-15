# HyperTeX

<img src="../assets/images/hypertex-icon.svg" alt="" width="72" align="right">

HyperTeX is **HyperTeX 2.0**, a web document format that uses LaTeX syntax instead of HTML, together with a browser for reading it.

It started from a question: what if the web's hypertext language had been TeX rather than HTML in the 1990s?
Scientists already think and write in LaTeX. HyperTeX aims to let those documents open like web pages and link to one another, instead of being frozen into PDFs.

[Download](download.md){ .md-button .md-button--primary }
[Get started](getting-started.md){ .md-button }

## What it does

- **Reads `.htex` documents**: equation numbers, cross-references, theorem environments, collapsible proofs and step-by-step derivations, exactly as written.
- **Opens existing `.tex` files**: keep the extension and they load in compatibility mode, including common preamble macros, `\cref` and commutative diagrams (`\xymatrix`, `tikzcd`).
- **Links documents together**: through `htex://` addresses and ordinary web URLs.
- **Draws figures**: a subset of TikZ and pgfplots rendered as SVG.
- **Makes parameters interactive**: values declared with `\parameter` become sliders, and equations and plots follow them.
- **Handles Hangul in math**: Korean letters in formulas are treated like Greek letters and set in a sans-serif face.
- **Works in ordinary browsers too**: convert documents to HTML with MathML, or build them into a static website.

## Unknown commands are skipped

When HyperTeX meets a command it cannot handle, it does not stop. It leaves that command out and shows the rest of the document.
If macro expansion exceeds its limit, a red error marker appears in place.

## Components

| Component | What it does |
| --- | --- |
| Parser | Turns `.htex` and `.tex` sources into a document tree |
| HTML renderer | Renders the tree as HTML with MathML |
| Figure renderer | Converts TikZ and pgfplots figures to SVG |
| Viewer | A desktop browser with tabs and an address bar (PySide6) |
| Web server | Serves documents to ordinary browsers |

The parser, renderer and server use only the Python standard library.

## Specification

The format is defined in the repository.

- [HyperTeX 2.0 specification](https://github.com/krunyx/hypertex/blob/main/docs/spec.md)
- [Interaction protocol](https://github.com/krunyx/hypertex/blob/main/docs/interaction-protocol.md)

## License

HyperTeX is open source under the [Apache License 2.0](https://github.com/krunyx/hypertex/blob/main/LICENSE).
You may use, modify and distribute it freely for personal, research and commercial work.
