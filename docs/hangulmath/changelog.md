# Changelog

Each new version is added at the top.

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
