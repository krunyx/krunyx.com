---
template: home.html
title: krunyx
hide:
  - navigation
  - toc
---

## What we are building { #stack }

krunyx is building one computing environment that runs from the hardware up to the applications on it.
We are shipping it from the top down, one layer at a time.

<div class="kx-stack">
  <a class="kx-stack__layer kx-stack__layer--live" href="hypertex/">
    <span class="kx-stack__name">HyperTeX</span>
    <span class="kx-stack__desc">Web documents written in LaTeX syntax, and a browser built to read them</span>
    <span class="kx-stack__status">Available now</span>
  </a>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">AI layer</span>
    <span class="kx-stack__desc">An OS layer that lets AI agents act only within the limits you grant</span>
    <span class="kx-stack__status">In research</span>
  </div>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">krunyx OS</span>
    <span class="kx-stack__desc">A security-hardened operating system built on Linux</span>
    <span class="kx-stack__status">In development</span>
  </div>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">Hardware</span>
    <span class="kx-stack__desc">Computers designed around the three layers above</span>
    <span class="kx-stack__status">Planned</span>
  </div>
</div>

The full plan is on the [roadmap](roadmap.md).

## HyperTeX { #hypertex }

Math-heavy documents end up locked in PDFs, or lose their shape when converted to HTML.
HyperTeX lets you write web documents in the LaTeX you already know, link them together, and read them directly in a browser.

<div class="kx-points" markdown>

<div markdown>
### The syntax you already use
`\section`, `\label`, `\ref`, `equation`, `align` and theorem environments work as written.
Existing `.tex` files open in compatibility mode.
</div>

<div markdown>
### A browser made for reading
A dedicated viewer with tabs, find, zoom, view-source and dark mode.
Documents link to each other through `htex://` addresses.
</div>

<div markdown>
### Figures and interaction
TikZ and pgfplots figures render as SVG.
Parameter sliders let readers move equations and plots.
</div>

</div>

[Download HyperTeX](hypertex/download.md){ .md-button .md-button--primary }
[Get started](hypertex/getting-started.md){ .md-button }
