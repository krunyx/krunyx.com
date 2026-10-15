---
template: home.html
title: krunyx
hide:
  - navigation
  - toc
---

## 우리가 만드는 것 { #stack }

krunyx는 하드웨어부터 응용 프로그램까지 이어지는 하나의 컴퓨팅 환경을 만듭니다.
위에서부터 한 층씩 내놓고 있습니다.

<div class="kx-stack">
  <a class="kx-stack__layer kx-stack__layer--live" href="hypertex/">
    <span class="kx-stack__name">HyperTeX</span>
    <span class="kx-stack__desc">LaTeX 문법으로 쓰는 웹 문서와 그 전용 브라우저</span>
    <span class="kx-stack__status">지금 내려받기 가능</span>
  </a>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">AI 계층</span>
    <span class="kx-stack__desc">AI 에이전트가 허락한 범위 안에서만 일하도록 하는 OS 계층</span>
    <span class="kx-stack__status">연구 중</span>
  </div>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">krunyx OS</span>
    <span class="kx-stack__desc">보안을 강화한 리눅스 기반 운영체제</span>
    <span class="kx-stack__status">개발 중</span>
  </div>
  <div class="kx-stack__layer">
    <span class="kx-stack__name">하드웨어</span>
    <span class="kx-stack__desc">위 세 층에 맞춰 설계한 컴퓨터</span>
    <span class="kx-stack__status">계획</span>
  </div>
</div>

자세한 계획은 [로드맵](roadmap.md)에 있습니다.

## HyperTeX { #hypertex }

수식이 많은 문서는 PDF로 닫혀 있거나, HTML로 옮기며 모양이 깨지곤 합니다.
HyperTeX는 LaTeX을 쓰던 그대로 웹 문서를 쓰고, 링크로 잇고, 브라우저에서 바로 읽게 합니다.

<div class="kx-points" markdown>

<div markdown>
### 쓰던 문법 그대로
`\section`, `\label`, `\ref`, `equation`, `align`, 정리 환경을 그대로 씁니다.
기존 `.tex` 파일도 호환 모드로 열립니다.
</div>

<div markdown>
### 읽기 위한 브라우저
탭, 찾기, 확대, 원본 보기, 다크 모드를 갖춘 전용 뷰어로 문서를 읽습니다.
`htex://` 주소로 문서끼리 링크합니다.
</div>

<div markdown>
### 그림과 상호작용
TikZ와 pgfplots 그림을 SVG로 그리고,
매개변수 슬라이더로 수식과 그래프를 움직여 볼 수 있습니다.
</div>

</div>

[HyperTeX 내려받기](hypertex/download.md){ .md-button .md-button--primary }
[시작하기](hypertex/getting-started.md){ .md-button }
