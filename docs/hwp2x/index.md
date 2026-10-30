# hwp2x

**Convert Hangul word processor documents (HWP) to HWPX.**

HWPX is the open, XML-based successor to the binary HWP format, and Korean public institutions are moving to it.
hwp2x converts HWP 5.x files to HWPX one at a time or a whole folder at once, on Windows, macOS and Linux.
Java is bundled, so there is nothing else to install.

[Download](#download){ .md-button .md-button--primary }
[How to use](#use){ .md-button }
[Report a problem](#feedback){ .md-button }

- **Drag and drop app** for everyday use, plus a **command line** and a **Python library** for batch jobs.
- **Every output is checked** right after it is written: ZIP integrity, the `mimetype` entry, every XML part, and the manifest.
- **Tested against 93 sample documents**, comparing the body text with the original character by character.
- **Free and open source** under Apache-2.0. [Source on GitHub](https://github.com/krunyx/hwp2x).

!!! info "The app is in Korean"
    hwp2x is made for Korean documents, so its window and messages are in Korean.
    This page gives each Korean label with its meaning.

## Download { #download }

The latest version is **v0.1.0** (October 2026).
All files are also on the [GitHub releases page](https://github.com/krunyx/hwp2x/releases/latest).

=== "Windows"

    | Download | Size | For |
    | --- | --- | --- |
    | [hwp2x-0.1.0-windows-x64.zip](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-windows-x64.zip) | 60 MB | Windows 10 and 11, 64-bit |

    1. Right-click the zip file and choose **Extract All**. Keep the extracted folder together; the program needs the files next to it.
    2. Run **`hwp2x-gui.exe`** to open the app.
    3. If a "Windows protected your PC" window appears, click **More info → Run anyway**.

=== "macOS"

    | Download | Size | For |
    | --- | --- | --- |
    | [hwp2x-0.1.0-macos-arm64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-macos-arm64.dmg) | 55 MB | Apple silicon (M1 and later) |
    | [hwp2x-0.1.0-macos-x64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-macos-x64.dmg) | 59 MB | Intel Macs |

    1. Open the `.dmg` file and drag **hwp2x** into your Applications folder.
    2. Before the first launch, open Terminal and run this once:

        ```bash
        xattr -dr com.apple.quarantine /Applications/hwp2x.app
        ```

        Without it, macOS may say the app "is damaged" or "cannot be verified", because the app is not yet signed by Apple.
        On older macOS versions, **right-clicking the app and choosing Open** also works.

=== "Linux"

    | Download | Size | For |
    | --- | --- | --- |
    | [hwp2x-0.1.0-linux-x64.tar.gz](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-linux-x64.tar.gz) | 96 MB | 64-bit Linux (glibc 2.35 or later, e.g. Ubuntu 22.04+) |

    ```bash
    tar xzf hwp2x-0.1.0-linux-x64.tar.gz
    ./hwp2x/hwp2x-gui        # the app
    ./hwp2x/hwp2x --help     # the command line
    ```

    The app needs the usual desktop libraries; on a minimal system install `libegl1` and `libxkbcommon0`.
    Install a Korean font such as `fonts-noto-cjk` so file names display correctly.

!!! note "About the security warnings"
    This version is not yet code-signed by Apple or Microsoft, so your system warns on first launch.
    The downloads are built by GitHub Actions directly from the [public source code](https://github.com/krunyx/hwp2x/blob/main/.github/workflows/build.yml).

## How to use { #use }

### The app

1. **Add files.** Drag `.hwp` files or whole folders onto the window, or use
   **파일 추가** (Add files) and **폴더 추가** (Add folder).
   **목록 비우기** (Clear list) empties the list.
2. **Choose where to save** under **저장 위치** (Save location):
    - **원본과 같은 폴더** (Same folder as the original) — the default. `보고서.hwp` becomes `보고서.hwpx` next to it.
    - **다른 폴더** (Another folder) — pick a folder with **찾아보기** (Browse). Folder structure is kept.
3. **Set the options** if you need them:
    - **폴더 안의 하위 폴더까지 포함** — also convert files in sub-folders.
    - **같은 이름의 .hwpx가 있으면 덮어쓰기** — overwrite an existing `.hwpx` with the same name. Without it, such files are skipped.
4. **Click 변환 (Convert).** Click it again to stop after the files in progress.
5. **Check the results**, then open the output with **결과 폴더 열기** (Open result folder).

Each file gets one of these results. Files that failed or need checking move to the top of the list, with the reason.

| Result | Meaning |
| --- | --- |
| ✔ 완료 | Converted |
| △ 완료 (확인) | Converted, but something was cleaned up. Usually a font name containing characters XML does not allow. Open the file to check it. |
| – 건너뜀 | Skipped, because an `.hwpx` with that name already exists |
| ✘ 실패 | Not converted. The reason is shown next to it. |

### The command line

The command line is handy for large folders and scripts.
It is `hwp2x.exe` in the Windows folder, `hwp2x/hwp2x` on Linux, and on macOS it lives inside the app:

```bash
alias hwp2x=/Applications/hwp2x.app/Contents/MacOS/hwp2x   # macOS: add to ~/.zshrc
```

```bash
hwp2x 보고서.hwp                    # creates 보고서.hwpx
hwp2x ./문서 -r -o ./변환결과       # include sub-folders; save into another folder, keeping the structure
hwp2x ./문서 -r -f -j 4             # overwrite existing .hwpx files; convert 4 at a time
```

| Option | Meaning |
| --- | --- |
| `-o FOLDER` | Save results in this folder (default: next to each original) |
| `-r` | Include sub-folders |
| `-f` | Overwrite existing `.hwpx` files |
| `-j N` | Number of files to convert at the same time |
| `--timeout SECONDS` | Time limit per file (default 300) |
| `-q` | Print only the files that failed |
| `-V` | Show the version |

Exit codes: `0` all succeeded, `1` some failed, `2` no files to convert, `3` the converter could not start.

### The Python library

```python
from hwp2x import convert, convert_all, plan

r = convert("보고서.hwp")          # Result(status='ok', dst=PosixPath('보고서.hwpx'), ...)
results = convert_all(plan(["./문서"], "./변환결과", recursive=True), overwrite=True)
```

The library is installed from source and needs Java 17 or later.
See the [README](https://github.com/krunyx/hwp2x#빌드) for the build steps.

## Documents that are not converted { #limits }

| Document | Why, and what to do |
| --- | --- |
| Password-protected | Remove the password in Hangul, then convert. |
| Distribution documents (배포용 문서) | Their copy and print restrictions would be lost in HWPX, so hwp2x leaves them as they are. |
| HWP 3.x (Hangul 97 and earlier) | Only HWP 5.x is supported. Open the file in Hangul, save it again, then convert. |

## Report a problem or send feedback { #feedback }

If a document does not convert, looks wrong after converting, or you have an idea, please tell us.

[Email hello@krunyx.com](mailto:hello@krunyx.com?subject=%5Bhwp2x%5D%20){ .md-button .md-button--primary }
[Open a GitHub issue](https://github.com/krunyx/hwp2x/issues/new){ .md-button }

Writing in Korean is fine. It helps if you include:

- your operating system, and the hwp2x version (`hwp2x -V`, or v0.1.0)
- the result shown in the list and the message next to it
- what you expected and what you saw

A sample file helps us fix problems fastest. Only send one if it contains nothing confidential;
otherwise a description, or a copy with the text replaced, is enough.

## License

hwp2x is released under the [Apache License 2.0](https://github.com/krunyx/hwp2x/blob/main/LICENSE).
The conversion engine is built from neolord0's [hwplib](https://github.com/neolord0/hwplib),
[hwpxlib](https://github.com/neolord0/hwpxlib) and [hwp2hwpx](https://github.com/neolord0/hwp2hwpx), all Apache-2.0.
The bundled Java runtime is OpenJDK (GPLv2 with the Classpath Exception).

“본 제품은 한글과컴퓨터의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.”
<br><small>(This product was developed with reference to Hancom's published HWP document file format specification.)</small>
