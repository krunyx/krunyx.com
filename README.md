# krunyx.com

krunyx 홈페이지 소스입니다. [MkDocs](https://www.mkdocs.org/)와 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)로 만들고, Cloudflare Pages가 배포합니다.

## 내 컴퓨터에서 미리 보기

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

브라우저에서 <http://127.0.0.1:8000/>을 엽니다. 파일을 저장하면 바로 다시 그려집니다.

## 어디를 고치면 되나요

| 바꾸고 싶은 것 | 파일 |
| --- | --- |
| 메뉴 순서, 사이트 이름, HyperTeX 버전 | `mkdocs.yml` |
| 첫 화면(제목, 원본과 화면 예시) | `overrides/home.html` |
| 홈 아래쪽(스택, HyperTeX 소개) | `docs/index.md` |
| HyperTeX 페이지들 | `docs/hypertex/*.md` |
| 색, 글꼴 크기, 여백 | `docs/assets/stylesheets/extra.css` 맨 위 색 토큰 |
| 로고 | `docs/assets/images/brand/` (브랜드 키트에서 `python tools/brand_assets.py <키트 폴더>`로 다시 만든다) |

새 페이지는 `docs/` 안에 `.md` 파일을 만들고 `mkdocs.yml`의 `nav`에 한 줄 추가하면 됩니다.

## HyperTeX 예제 (`examples/`)

`examples/` 의 파일은 사이트를 만들 때 **그대로** `https://krunyx.com/examples/` 에 올라간다 (`.md` 도 MkDocs 가 바꾸지 않는다).
그래서 HyperTeX 에서 `htex://krunyx.com/examples/oscillator/report.htex` 처럼 바로 열린다.
이 일은 `hooks/examples.py` 가 한다.

- 원본 파일 복사 → `site/examples/<예제>/`
- 모든 예제 목록 `site/examples/index.htex` 를 만든다 (HyperTeX 용)
- `htex build` 로 일반 브라우저용 사본 → `site/examples/web/` (`requirements.txt` 의 htex 패키지)
- 안내 페이지 `docs/hypertex/examples.md` 의 `<!-- examples:gallery -->` 자리에 예제 목록을 채운다

**예제 추가하기**: `examples/<새 이름>/` 폴더를 만들고 파일과 `example.yml` 을 넣으면 끝이다. 다른 곳은 고치지 않는다.

```yaml
title: "예제 제목"
order: 40                 # 작을수록 앞
summary: >-
  한두 문장 소개.
main: report.htex         # "Open in HyperTeX" 단추가 여는 파일
files:                    # 목록에 보일 파일 (없는 파일을 적으면 빌드가 멈춘다)
  - path: report.htex
    about: 이 파일이 보여 주는 것.
```

주의: 예제 안의 `\input`·`\usemacros`·그림은 같은 폴더나 그 아래만 가리킨다 (`../` 는 원격에서 막힌다).
다른 예제로 가는 `\href{../sir/report.htex}{…}` 링크는 괜찮다.
그림과 데이터는 `python tools/example_figures.py` 로 다시 만든다 (numpy·matplotlib 필요).

## 새 HyperTeX 버전을 냈을 때

1. `mkdocs.yml`의 `extra.hypertex.version` 값을 바꿉니다 (첫 화면에 표시).
2. `docs/hypertex/download.md` 맨 위의 버전을 바꿉니다.
3. `docs/hypertex/changelog.md` 맨 위에 항목을 추가합니다.
4. `docs/hypertex/cite.md`의 `version`을 바꿉니다.
5. 예제 빌드에 쓰는 버전: `requirements.txt` 의 `htex @ …/v<버전>.tar.gz` 를 바꿉니다.

## 배포 (Cloudflare Workers)

Cloudflare Workers가 저장소를 보고 빌드와 배포를 합니다. 설정은 저장소의 두 파일에 들어 있습니다.

- `wrangler.jsonc`: 빌드 결과 `site/` 폴더를 정적 파일로 올리고, 없는 주소는 `404.html`로 보냅니다.
- `.python-version`: 빌드에 쓸 파이썬 버전(3.12).

처음 한 번만 대시보드에서 연결합니다.

1. Cloudflare 대시보드 → **Workers & Pages** → **Create application** → **Continue with GitHub**
2. `krunyx/krunyx.com` 저장소를 고릅니다.
3. 빌드 설정:
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Deploy command: `npx wrangler deploy` (기본값)
4. 배포가 끝나면 Worker의 **Settings → Domains & Routes**에서 `krunyx.com`과 `www.krunyx.com`을 추가합니다.

그다음부터는 `main` 브랜치에 push할 때마다 자동으로 배포됩니다.

## 참고

- `requirements.txt`에서 MkDocs를 2.0 미만으로 고정해 두었습니다. MkDocs 2.0은 테마와 플러그인 구조가 바뀌어 이 사이트가 그대로는 동작하지 않습니다.
- 수식은 MathJax(CDN)로 그립니다.
