# HyperTeX 내려받기

최신 버전은 **v0.1.0**입니다. 모든 설치 파일은 [GitHub 릴리스 페이지](https://github.com/krunyx/hypertex/releases/latest)에 있습니다.

[최신 릴리스 열기](https://github.com/krunyx/hypertex/releases/latest){ .md-button .md-button--primary }

## 운영체제별 설치

=== "macOS"

    | 파일 | 대상 |
    | --- | --- |
    | `HyperTeX-<버전>-macos-arm64.dmg` | Apple Silicon (M1 이후) |
    | `HyperTeX-<버전>-macos-x86_64.dmg` | Intel Mac |

    1. `.dmg` 파일을 엽니다.
    2. HyperTeX를 응용 프로그램 폴더로 끌어 놓습니다.
    3. 처음 열 때 "확인되지 않은 개발자" 경고가 뜨면, 응용 프로그램 폴더에서 HyperTeX를 **오른쪽 클릭 → 열기**로 엽니다. 한 번만 하면 됩니다.

=== "Windows"

    | 파일 | 대상 |
    | --- | --- |
    | `HyperTeX-Setup-<버전>.exe` | Windows 10, 11 |

    관리자 권한 없이 설치됩니다. 설치하면 `.htex` 파일과 `htex://` 링크가 HyperTeX로 열립니다.

    "Windows의 PC 보호" 창이 뜨면 **추가 정보 → 실행**을 누릅니다.

=== "Linux"

    | 파일 | 설치 방법 |
    | --- | --- |
    | `HyperTeX-<버전>-x86_64.AppImage` | 실행 권한을 주고 바로 실행 |
    | `HyperTeX-<버전>-linux-x86_64.tar.gz` | 압축을 풀고 `install.sh` 실행 |

    AppImage:

    ```bash
    chmod +x HyperTeX-*-x86_64.AppImage
    ./HyperTeX-*-x86_64.AppImage
    ```

    tar.gz (`~/.local`에 설치하고 `.htex`, `htex://`를 연결합니다):

    ```bash
    tar xzf HyperTeX-*-linux-x86_64.tar.gz
    cd HyperTeX-*/
    ./install.sh              # 제거할 때는 ./install.sh --uninstall
    ```

!!! note "설치 경고에 대해"
    지금 버전은 운영체제 제조사의 코드 서명을 받지 않은 상태라 처음 실행할 때 경고가 뜹니다.
    설치 파일은 공개된 소스 코드를 GitHub Actions가 직접 빌드한 것입니다. 서명은 다음 버전부터 적용할 예정입니다.

## 파이썬으로 설치

파이썬 3.10 이상이 필요합니다.

```bash
git clone https://github.com/krunyx/hypertex.git
cd hypertex
pip install .              # 파서, HTML 변환, 웹 서버 (추가 의존성 없음)
pip install ".[viewer]"    # 전용 뷰어까지 (PySide6)
```

pip로 설치한 뷰어를 리눅스 데스크톱에 연결하려면 `packaging/linux/install.sh --pip`을 실행합니다.

## 다음 단계

설치했다면 [시작하기](getting-started.md)에서 예제 문서를 열어 보세요.
