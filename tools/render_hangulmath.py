"""Typeset the hangulmath example formulas on the website as SVG.

Each formula is compiled with XeLaTeX and the real hangulmath package,
then converted to SVG (glyphs become outlines, so the site needs no TeX).

Usage:
    python3 tools/render_hangulmath.py PATH/TO/hangulmath

PATH/TO/hangulmath is a checkout of https://github.com/krunyx/hangulmath.
Output: docs/assets/images/hangulmath/<name>.svg, enlarged by SCALE so that
formulas sit at a comfortable reading size next to 16px body text.
Requires: xelatex (with the standalone and amsmath packages) and pdftocairo.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# name -> display-math body. Keep these in sync with the code shown on the pages.
FORMULAS = {
    "hero": r"""
\hangulsum\tiut_{k=1}^{n} \giug_k^{\,2}
\;\le\; \Bigl(\hangulsum\tiut_{k=1}^{n} \giug_k\Bigr)^{2},
\qquad
\mium^2 \vec{A} = -\mu_0 \vec{J}
""",
    "functions": r"""
\giug(z) = \frac{1}{\Gamma(z)}, \qquad
\mium = \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}
""",
    "operators": r"""
\hangulsum\tiut_{k=1}^{n} k = \frac{n(n+1)}{2}, \qquad
\hangulint\diud_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}, \qquad
\hangullim\liul_{n\to\infty}\Bigl(1+\frac1n\Bigr)^{n} = e
""",
    "brackets": r"""
\eoh\psi|\phi\ah = \int \psi^*\phi\,dx, \qquad
\sum_n |n\ah\eoh n| = \mathbf{1}
""",
    "mechanics": r"""
i\hbar\,\frac{\partial}{\partial t}|\psi\ah = \piup\,|\psi\ah, \qquad
\piup = p\,\dot q - \liul
""",
    "superscript": r"""
A',\ A^*,\ A^\dagger,\ A^{\ciuc}, \qquad
(AB)^{\ciuc} = B^{\ciuc}A^{\ciuc}
""",
    "arrows": r"""
|\oh\ah,\ |\uh\ah \quad (\text{spin up, down}), \qquad
x \mathrel{\uh} 0 \quad (x \downarrow 0)
""",
    "chemistry": r"""
2\,\kiuk + \piup_2 \to 2\,\kiuk\piup, \qquad
2\,\giug_2 + \iung_2 \rightleftharpoons 2\,\giug_2\iung
""",
}

SCALE = 1.6

PACKAGE_FILES = [
    "hangulmath.sty",
    "hangulmath-metrics.def",
    "hangulmath-sans.otf",
    "hangulmath-sans-light.otf",
]

TEMPLATE = r"""\documentclass[border=2pt,12pt]{standalone}
\usepackage{amsmath}
\usepackage{hangulmath}
\begin{document}
$\displaystyle %s$
\end{document}
"""


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    package = Path(sys.argv[1]).resolve()
    site = Path(__file__).resolve().parent.parent
    out = site / "docs" / "assets" / "images" / "hangulmath"
    out.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for name in PACKAGE_FILES:
            shutil.copy(package / name, tmp / name)
        for name, body in FORMULAS.items():
            (tmp / f"{name}.tex").write_text(TEMPLATE % body.strip(), encoding="utf-8")
            run = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"],
                cwd=tmp, capture_output=True, text=True,
            )
            if run.returncode != 0:
                sys.exit(f"{name}: XeLaTeX failed\n{run.stdout[-2000:]}")
            subprocess.run(
                ["pdftocairo", "-svg", f"{name}.pdf", str(out / f"{name}.svg")],
                cwd=tmp, check=True,
            )
            svg = out / f"{name}.svg"
            text = svg.read_text(encoding="utf-8")
            text = re.sub(
                r'width="([\d.]+)" height="([\d.]+)"',
                lambda m: f'width="{float(m[1]) * SCALE:.2f}" height="{float(m[2]) * SCALE:.2f}"',
                text, count=1)
            svg.write_text(text, encoding="utf-8")
            print(f"wrote {svg}")


if __name__ == "__main__":
    main()
