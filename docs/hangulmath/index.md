# hangulmath

**Hangul letters as math symbols for LaTeX.**

Mathematical notation draws almost entirely on Latin and Greek letters, and a long paper soon runs out of distinct ones.
`hangulmath` adds the 40 letters (*jamo*) of modern Korean Hangul as math symbols.
They are built from simple geometric strokes, look nothing like Latin or Greek, and each one has an established name.

<figure class="kx-texfig" markdown>
![Typeset with hangulmath: giyeok with subscript a as a function defined by a power series with coefficients nieun, and the wave equation with mieum as the d'Alembertian](../assets/images/hangulmath/hero.svg){ .kx-tex }
</figure>

```latex
\usepackage{hangulmath}
...
\[ \giug_{\ah}(x) = \sum_{k} \niun_k\, x^k,
   \qquad \mium^2 \vec{A} = -\mu_0 \vec{J} \]
```

[Install](install.md){ .md-button .md-button--primary }
[Usage and symbol list](usage.md){ .md-button }
[hangulmath on CTAN](https://ctan.org/pkg/hangulmath){ .md-button }

## At a glance

- **40 symbols**: 14 consonants, 5 double consonants, 10 vowels and 11 compound vowels.
- **Easy to type**: `\giyeok` follows the official romanization, much as `\alpha` names α. Every consonant also has a four-letter alias such as `\giug`, `\niun`, `\diud`.
- **Real math symbols**: they take sub- and superscripts, scale in script styles, and work in running text too.
- **No Korean font needed**: the glyphs come from a bundled subset of Noto Sans CJK KR.
- **Works with kotex** in either package order.
- **pdfLaTeX, XeLaTeX and LuaLaTeX** all work, with identical output. On Overleaf the default pdfLaTeX compiler is fine.
- Released under the LaTeX Project Public License 1.3c; the font is under the SIL Open Font License 1.1.

## What you can write

Every example below was typeset with hangulmath itself.

### Consonants as function names

<span class="kx-jamo">ㄱ</span> reads naturally as a function, and <span class="kx-jamo">ㅁ</span>, which looks like a box, makes a fitting d'Alembertian.

<div class="kx-ex" markdown>

```latex
\giug(z) = \frac{1}{\Gamma(z)}, \qquad
\mium = \nabla^2 - \frac{1}{c^2}
        \frac{\partial^2}{\partial t^2}
```

![Typeset: giyeok of z equals one over Gamma of z, and mieum as the d'Alembertian](../assets/images/hangulmath/functions.svg){ .kx-tex }

</div>

### Limits and pre-scripts

A symbol takes limits below it with standard LaTeX `\mathop{...}\limits`, and scripts on both sides like any letter.

<div class="kx-ex" markdown>

```latex
\mathop{\liul}\limits_{n\to\infty}\Bigl(1+\frac1n\Bigr)^{n} = e, \qquad
{}_2\biub_1(a,b;c;z) = \sum_{n\ge0}
    \frac{(a)_n(b)_n}{(c)_n\,n!}\,z^n
```

![Typeset: rieul with n to infinity below it as a limit, and bieup with pre-subscript 2 and subscript 1 as a hypergeometric function](../assets/images/hangulmath/limits.svg){ .kx-tex }

</div>

### Vowels as brackets

<span class="kx-jamo">ㅓ</span> and <span class="kx-jamo">ㅏ</span> are mirror images, like ⟨ and ⟩.

<div class="kx-ex" markdown>

```latex
\eoh\psi|\phi\ah = \int \psi^*\phi\,dx, \qquad
\sum_n |n\ah\eoh n| = \mathbf{1}
```

![Typeset: a bra-ket inner product and a completeness relation using the vowels eo and a as angle brackets](../assets/images/hangulmath/brackets.svg){ .kx-tex }

</div>

### Hamiltonian and Lagrangian

<div class="kx-ex" markdown>

```latex
i\hbar\,\frac{\partial}{\partial t}|\psi\ah = \piup\,|\psi\ah,
\qquad \piup = p\,\dot q - \liul
```

![Typeset: the Schrödinger equation with pieup as the Hamiltonian, and pieup equals p q-dot minus rieul](../assets/images/hangulmath/mechanics.svg){ .kx-tex }

</div>

### A new superscript mark

<div class="kx-ex" markdown>

```latex
A',\ A^*,\ A^\dagger,\ A^{\ciuc}, \qquad
(AB)^{\ciuc} = B^{\ciuc}A^{\ciuc}
```

![Typeset: chieut used as a superscript mark beside prime, star and dagger](../assets/images/hangulmath/superscript.svg){ .kx-tex }

</div>

### Arrows

<span class="kx-jamo">ㅗ</span> and <span class="kx-jamo">ㅛ</span> point up, <span class="kx-jamo">ㅜ</span> and <span class="kx-jamo">ㅠ</span> point down.

<div class="kx-ex" markdown>

```latex
|\oh\ah,\ |\uh\ah \quad (\text{spin up, down}),
\qquad x \mathrel{\uh} 0
```

![Typeset: spin up and spin down kets using the vowels o and u as arrows](../assets/images/hangulmath/arrows.svg){ .kx-tex }

</div>

### Element symbols

<div class="kx-ex" markdown>

```latex
2\,\kiuk + \piup_2 \to 2\,\kiuk\piup, \qquad
2\,\giug_2 + \iung_2 \rightleftharpoons 2\,\giug_2\iung
```

![Typeset: chemical equations with Hangul consonants as element symbols](../assets/images/hangulmath/chemistry.svg){ .kx-tex }

</div>

## Get it

`hangulmath` is on [CTAN](https://ctan.org/pkg/hangulmath) and in TeX Live.
The source is on [GitHub](https://github.com/krunyx/hangulmath), and the full manual is
[hangulmath-doc.pdf](https://mirrors.ctan.org/fonts/hangulmath/hangulmath-doc.pdf).
See [Install](install.md) to set it up locally or on Overleaf.
