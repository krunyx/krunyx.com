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

=== "Windows"

    | 파일 | 대상 |
    | --- | --- |
    | `HyperTeX-Setup-<버전>.exe` | Windows 10, 11 |

    관리자 권한 없이 설치됩니다. 설치하면 `.htex` 파일과 `htex://` 링크가 HyperTeX로 열립니다.

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
