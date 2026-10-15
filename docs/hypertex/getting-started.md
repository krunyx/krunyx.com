# 시작하기

## 첫 문서 열기

저장소의 예제 문서 `examples/oscillator.htex`는 조화 진동자 노트입니다.
수식 번호, 상호참조, 정리 환경, 접힌 증명, 매개변수, 한글 수식이 한 문서에 들어 있습니다.

=== "뷰어로 열기"

    ```bash
    htex view examples/oscillator.htex
    ```

    설치한 앱에서는 파일을 더블클릭하거나 창으로 끌어 놓아도 됩니다.

=== "HTML로 바꾸기"

    ```bash
    htex html examples/oscillator.htex -o oscillator.html
    ```

    만들어진 `oscillator.html`은 어느 브라우저에서나 열립니다.

=== "웹 서버로 보기"

    ```bash
    htex serve tests/docs
    ```

    브라우저에서 `http://127.0.0.1:8000/`을 엽니다.

## 문서 쓰기

HyperTeX 문서는 LaTeX와 거의 같습니다. 문서 클래스를 `hypertex`로 두면 됩니다.

```latex
\documentclass{hypertex}
\title{조화 진동자 노트}
\author{홍길동}
\parameter{\omega}{0.5}{3}{1}[step=0.1]

\begin{document}
\maketitle

\section{해밀토니안}\label{sec:H}
\begin{equation}\label{eq:H}
  H = \frac{p^2}{2m} + \frac{1}{2} m\omega^2 x^2
\end{equation}
식~\eqref{eq:H}에서 $\omega$를 슬라이더로 바꿔 보세요.
\end{document}
```

`\parameter{이름}{최솟값}{최댓값}{기본값}`으로 선언한 값은 뷰어에서 슬라이더로 나타납니다.

## 정적 웹사이트로 발행하기

여러 `.htex` 문서가 든 폴더를 일반 웹사이트로 바꿀 수 있습니다.

```bash
htex build my-notes -o site
```

`site` 폴더를 GitHub Pages나 Cloudflare Pages 같은 정적 호스팅에 올리면 됩니다.

## 뷰어 단축키

macOS에서는 Ctrl 대신 Cmd를 씁니다.

| 동작 | 키 |
| --- | --- |
| 새 탭, 탭 닫기 | Ctrl+T, Ctrl+W |
| 탭 전환 | Ctrl+Tab, Ctrl+1…9 |
| 링크를 새 탭으로 | 가운데 클릭 또는 Ctrl+클릭 |
| 찾기 | Ctrl+F (다음 Enter 또는 F3, 이전 Shift+Enter) |
| 확대, 축소, 원래 크기 | Ctrl+=, Ctrl+-, Ctrl+0 |
| 원본(.htex) 보기 | Ctrl+U |
| 뒤로, 앞으로 | Alt+←, Alt+→ |
| 새로고침, 주소창 | Ctrl+R, Ctrl+L |

테마(시스템, 밝게, 어둡게)는 보기 메뉴에서 바꿉니다. 열어 둔 로컬 문서는 저장할 때마다 자동으로 다시 그려집니다.
