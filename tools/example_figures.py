"""examples/ 의 그림과 데이터를 다시 만든다.

    python tools/example_figures.py

numpy·matplotlib 이 필요하다 (사이트 빌드에는 필요 없다: 결과 파일을 저장소에 넣어 둔다).
- oscillator/figures/spring.svg   감쇠 진동하는 용수철 (SVG 애니메이션, <img> 로도 움직인다)
- oscillator/figures/resonance.png 공명 곡선 (웹·HyperTeX 용)
- oscillator/classic/figures/resonance.pdf 같은 그림의 PDF (LaTeX 원고용, 웹 사본용 같은 이름 PNG 도)
- sir/data/sir.csv                 SIR 모형의 수치 해 (R0 = 2.5)
- sir/figures/epidemic.png        R0 에 따른 감염자 곡선
- heat/figures/cooling.svg        식어 가는 막대의 온도 분포 (SVG 애니메이션)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1] / "examples"
INK, BLUE, ORANGE, GREEN, GREY = "#1f2937", "#2563eb", "#ea580c", "#16a34a", "#9ca3af"


def style() -> None:
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": INK, "axes.labelcolor": INK, "xtick.color": INK,
                         "ytick.color": INK, "savefig.dpi": 200, "svg.fonttype": "none",
                         "pdf.fonttype": 42})


# ------------------------------------------------------------------ 진동자
def spring_svg(out: Path) -> None:
    """천장에 매단 용수철과 물체. 처음 당긴 뒤 감쇠 진동하고 6초마다 다시."""
    zeta, w0, period, frames = 0.12, 2 * np.pi / 1.2, 6.0, 90
    t = np.linspace(0, period, frames)
    y = 38 * np.exp(-zeta * w0 * t) * np.cos(w0 * np.sqrt(1 - zeta ** 2) * t)   # 아래로 +
    top, rest, coils, half = 20, 110, 9, 16

    def spring_path(bottom: float) -> str:
        pts = [(100, top), (100, top + 8)]
        n = coils * 2
        for i in range(1, n):
            yy = top + 8 + (bottom - 8 - top - 8) * i / n
            pts.append((100 + (half if i % 2 else -half), yy))
        pts += [(100, bottom - 8), (100, bottom)]
        return "M" + " L".join(f"{x:.1f},{yy:.1f}" for x, yy in pts)

    paths = ";".join(spring_path(rest + v) for v in y)
    moves = ";".join(f"0,{v:.1f}" for v in y)
    trace = " ".join(f"{205 + 140 * k / (frames - 1):.1f},{rest + 22 + v * 0.9:.1f}" for k, v in enumerate(y))
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 220" width="360" height="220">
  <title>Damped oscillator: a mass on a spring</title>
  <rect x="60" y="8" width="80" height="12" fill="{GREY}"/>
  <path d="{spring_path(rest)}" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round">
    <animate attributeName="d" dur="{period}s" repeatCount="indefinite" values="{paths}"/>
  </path>
  <g>
    <animateTransform attributeName="transform" type="translate" dur="{period}s" repeatCount="indefinite"
                      values="{moves}"/>
    <rect x="76" y="{rest}" width="48" height="44" rx="4" fill="{BLUE}"/>
    <text x="100" y="{rest + 28}" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#fff">m</text>
  </g>
  <line x1="200" y1="{rest + 22}" x2="350" y2="{rest + 22}" stroke="{GREY}" stroke-dasharray="3 3"/>
  <polyline points="{trace}" fill="none" stroke="{ORANGE}" stroke-width="2"/>
  <circle r="4" fill="{ORANGE}">
    <animateMotion dur="{period}s" repeatCount="indefinite" path="M{trace.replace(' ', ' L')}"/>
  </circle>
  <text x="205" y="30" font-family="sans-serif" font-size="12" fill="{INK}">x(t), ζ = {zeta}</text>
</svg>
"""
    out.write_text(svg, encoding="utf-8")


def resonance(png: Path, pdf: Path) -> None:
    """png 은 HyperTeX·웹용, pdf 는 LaTeX 원고용. 원고 폴더에도 같은 이름의 png 를 두어
    htex build 가 웹 사본에서 PDF 대신 쓰게 한다."""
    r = np.linspace(0, 2.5, 600)
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    for z, c in ((0.05, ORANGE), (0.15, BLUE), (0.3, GREEN), (0.7, INK)):
        a = 1 / np.sqrt((1 - r ** 2) ** 2 + (2 * z * r) ** 2)
        ax.plot(r, a, color=c, lw=1.8, label=f"$\\zeta = {z}$")
    ax.set_ylim(0, 8)
    ax.set_xlabel(r"frequency ratio $\Omega/\omega_0$")
    ax.set_ylabel(r"amplitude $X k / F_0$")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(png)
    fig.savefig(pdf)
    fig.savefig(pdf.with_suffix(".png"))
    plt.close(fig)


# ------------------------------------------------------------------ SIR
def sir(r0: float, gamma: float = 0.1, days: float = 160, dt: float = 0.05, i0: float = 1e-3):
    """S, I, R (인구 비율) 을 4차 룽게-쿠타로."""
    beta = r0 * gamma

    def f(y):
        s, i, _ = y
        return np.array([-beta * s * i, beta * s * i - gamma * i, gamma * i])
    n = int(days / dt)
    ys = np.empty((n + 1, 3))
    ys[0] = (1 - i0, i0, 0)
    for k in range(n):
        y = ys[k]
        k1 = f(y); k2 = f(y + dt / 2 * k1); k3 = f(y + dt / 2 * k2); k4 = f(y + dt * k3)
        ys[k + 1] = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.linspace(0, days, n + 1), ys


def sir_files(csv: Path, png: Path) -> None:
    t, ys = sir(2.5)
    step = int(4 / 0.05)                # 4일마다
    lines = ["t,S,I,R"]
    for k in range(0, len(t), step):
        lines.append(f"{t[k]:.0f},{ys[k, 0]:.4f},{ys[k, 1]:.4f},{ys[k, 2]:.4f}")
    csv.write_text("\n".join(lines) + "\n", encoding="utf-8")
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    for r0, c in ((1.5, GREEN), (2.5, BLUE), (4.0, ORANGE)):
        t, ys = sir(r0)
        ax.plot(t, ys[:, 1], color=c, lw=1.8, label=f"$R_0 = {r0}$")
    ax.set_xlabel("days")
    ax.set_ylabel("infected fraction $I$")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(png)
    plt.close(fig)


# ------------------------------------------------------------------ 열 확산
def cooling_svg(out: Path) -> None:
    """양 끝을 0도로 둔 막대. 가운데가 뜨거운 처음 분포가 퍼지며 식는다 (푸리에 급수 40항)."""
    x = np.linspace(0, 1, 121)
    n = np.arange(1, 80)
    # u(x,0) = 1 (0.3<x<0.7), 0 그 밖. b_n = 2/(n pi) (cos(0.3 n pi) - cos(0.7 n pi))
    b = 2 / (n * np.pi) * (np.cos(0.3 * n * np.pi) - np.cos(0.7 * n * np.pi))
    times = list(np.linspace(0, 0.12, 60) ** 1.0)
    period = 6.0
    X0, Y0, W, H = 40, 170, 280, 130

    def path(tt: float) -> str:
        u = (b[:, None] * np.sin(np.pi * n[:, None] * x[None, :]) * np.exp(-(np.pi * n[:, None]) ** 2 * tt)).sum(0)
        u = np.clip(u, -0.05, 1.1)
        return "M" + " L".join(f"{X0 + W * xx:.1f},{Y0 - H * uu:.1f}" for xx, uu in zip(x, u))

    values = ";".join(path(tt) for tt in times + [times[-1]] * 12)
    first = path(0.0)
    ticks = "".join(f'<text x="{X0 + W * v}" y="{Y0 + 16}" text-anchor="middle">{v:g}</text>' for v in (0, 0.5, 1))
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="360" height="200">
  <title>A rod cooling down: the heat equation</title>
  <defs><linearGradient id="hot" x1="0" x2="0" y1="1" y2="0">
    <stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{ORANGE}"/></linearGradient></defs>
  <g font-family="sans-serif" font-size="11" fill="{INK}">
    <line x1="{X0}" y1="{Y0}" x2="{X0 + W}" y2="{Y0}" stroke="{INK}"/>
    <line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0 - H - 10}" stroke="{INK}"/>
    {ticks}
    <text x="{X0 + W + 6}" y="{Y0 + 4}">x</text>
    <text x="{X0 - 6}" y="{Y0 - H - 14}">u(x, t)</text>
  </g>
  <path d="{first}" fill="none" stroke="url(#hot)" stroke-width="2.5" stroke-linejoin="round">
    <animate attributeName="d" dur="{period}s" repeatCount="indefinite" values="{values}"/>
  </path>
  <path d="{first}" fill="none" stroke="{GREY}" stroke-width="1" stroke-dasharray="3 3"/>
</svg>
"""
    out.write_text(svg, encoding="utf-8")


def main() -> None:
    style()
    spring_svg(ROOT / "oscillator" / "figures" / "spring.svg")
    resonance(ROOT / "oscillator" / "figures" / "resonance.png",
              ROOT / "oscillator" / "classic" / "figures" / "resonance.pdf")
    sir_files(ROOT / "sir" / "data" / "sir.csv", ROOT / "sir" / "figures" / "epidemic.png")
    cooling_svg(ROOT / "heat" / "figures" / "cooling.svg")
    for p in sorted(ROOT.rglob("*")):
        if p.suffix in (".svg", ".png", ".pdf", ".csv"):
            print(f"{p.relative_to(ROOT)}  {p.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
