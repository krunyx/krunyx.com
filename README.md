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
| 로고 | `docs/assets/images/krunyx-mark.svg` |

새 페이지는 `docs/` 안에 `.md` 파일을 만들고 `mkdocs.yml`의 `nav`에 한 줄 추가하면 됩니다.

## 새 HyperTeX 버전을 냈을 때

1. `mkdocs.yml`의 `extra.hypertex.version` 값을 바꿉니다 (첫 화면에 표시).
2. `docs/hypertex/download.md` 맨 위의 버전을 바꿉니다.
3. `docs/hypertex/changelog.md` 맨 위에 항목을 추가합니다.
4. `docs/hypertex/cite.md`의 `version`을 바꿉니다.

## 배포 (Cloudflare Pages)

처음 한 번만 설정합니다.

1. Cloudflare 대시보드 → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. GitHub에서 `krunyx/krunyx.com` 저장소를 고릅니다.
3. 빌드 설정:
   - Framework preset: **None**
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Build output directory: `site`
   - Environment variable: `PYTHON_VERSION` = `3.12`
4. 배포가 끝나면 **Custom domains**에서 `krunyx.com`과 `www.krunyx.com`을 추가합니다.

그다음부터는 `main` 브랜치에 push할 때마다 자동으로 배포됩니다. 다른 브랜치에 push하면 미리보기 주소가 따로 생깁니다.

## 참고

- `requirements.txt`에서 MkDocs를 2.0 미만으로 고정해 두었습니다. MkDocs 2.0은 테마와 플러그인 구조가 바뀌어 이 사이트가 그대로는 동작하지 않습니다.
- 수식은 MathJax(CDN)로 그립니다.
