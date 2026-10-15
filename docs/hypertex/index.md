# HyperTeX

<img src="../assets/images/hypertex-icon.svg" alt="" width="72" align="right">

HyperTeX는 HTML 대신 LaTeX 문법으로 쓰는 웹 문서 형식, **HyperTeX 2.0**과 그 문서를 읽는 브라우저입니다.

1990년대에 웹의 하이퍼텍스트 언어가 HTML이 아니라 TeX이었다면 어땠을까 하는 질문에서 출발했습니다.
과학자는 이미 LaTeX으로 생각하고 씁니다. 그 문서를 PDF로 굳히지 않고, 웹 페이지처럼 열고 서로 링크할 수 있게 하는 것이 목표입니다.

[내려받기](download.md){ .md-button .md-button--primary }
[시작하기](getting-started.md){ .md-button }

## 무엇을 할 수 있나요

- **`.htex` 문서 읽기**: 수식 번호, 상호참조, 정리 환경, 접힌 증명, 단계별 유도를 그대로 보여 줍니다.
- **기존 `.tex` 파일 열기**: 확장자를 그대로 두면 호환 모드로 읽습니다.
- **문서끼리 링크하기**: `htex://` 주소와 일반 웹 주소로 다른 문서에 연결합니다.
- **그림 그리기**: TikZ와 pgfplots의 부분집합을 SVG로 그립니다.
- **매개변수 움직이기**: `\parameter`로 선언한 값을 슬라이더로 바꾸면 수식과 그래프가 따라 바뀝니다.
- **한글 수식**: 수식 안의 한글을 그리스 문자처럼 다루고 고딕체로 씁니다.
- **일반 브라우저로도 보기**: 문서를 HTML과 MathML로 바꾸거나 정적 웹사이트로 빌드합니다.

## 모르는 명령은 건너뜁니다

HyperTeX는 처리하지 못하는 명령을 만나도 멈추지 않습니다. 그 명령만 그리지 않고 넘어가서 나머지 문서를 보여 줍니다.
매크로 확장이 한도를 넘으면 그 자리에 빨간 오류 표시를 남깁니다.

## 구성

| 구성 요소 | 하는 일 |
| --- | --- |
| 파서 | `.htex`와 `.tex` 원본을 문서 트리로 바꿉니다 |
| HTML 변환기 | 문서 트리를 HTML과 MathML로 그립니다 |
| 그림 렌더러 | TikZ와 pgfplots 그림을 SVG로 바꿉니다 |
| 뷰어 | 탭과 주소창을 갖춘 데스크톱 브라우저 (PySide6) |
| 웹 서버 | 일반 브라우저에서 문서를 볼 수 있게 제공합니다 |

파서, 변환기, 서버는 파이썬 표준 라이브러리만 씁니다.

## 명세

형식의 정의는 저장소의 문서에 있습니다.

- [HyperTeX 2.0 명세](https://github.com/msitsti2025/hypertex/blob/main/docs/spec.md)
- [상호작용 규약](https://github.com/msitsti2025/hypertex/blob/main/docs/interaction-protocol.md)
