# hwp2x

**Convert Hangul word processor documents (HWP) to HWPX, and to Word, Markdown, HTML and LaTeX.**

HWPX is the open, XML-based successor to the binary HWP format, and Korean public institutions are moving to it.
hwp2x converts HWP files one at a time or a whole folder at once, on Windows, macOS and Linux.
Java is bundled, so there is nothing else to install.

[Choose a version](#versions){ .md-button .md-button--primary }
[How to use](#use){ .md-button }
[Report a problem](#feedback){ .md-button }

- **Drag and drop app** for everyday use, plus a **command line** and a **Python library** for batch jobs.
- **Tested against 93 sample documents**, comparing the converted text with the original character by character.
- **Free and open source** under Apache-2.0. [Source on GitHub](https://github.com/krunyx/hwp2x).

!!! info "The app is in Korean"
    hwp2x is made for Korean documents, so its window and messages are in Korean.
    This page gives each Korean label with its meaning.

## Which version do you need? { #versions }

There are two releases. Both are maintained; pick the one that fits your job.

<div class="kx-points kx-points--two" markdown>

<div markdown>
### v0.1.0 — HWPX only
**For most people.** If you just need your `.hwp` files as `.hwpx`, use this one.

- HWP → HWPX, keeping the original layout as it is
- Every result is checked for a valid HWPX structure
- Smaller and simpler: no format to choose

[Download v0.1.0](#download-v010){ .md-button .md-button--primary }
</div>

<div markdown>
### v0.2.0 — more formats
**For a first draft in another format.** Converts to HWPX, **Word, Markdown, HTML, LaTeX and HyperTeX**, and also reads `.hwpx`.

- Text, headings, lists, tables, footnotes, images, links and equations are carried over
- **Page layout is not**: expect to tidy the result by hand
- HWPX output is the same as in v0.1.0

[Download v0.2.0](#download-v020){ .md-button }
</div>

</div>

| | v0.1.0 | v0.2.0 |
| --- | --- | --- |
| Input | `.hwp` | `.hwp`, `.hwpx` |
| Output | `.hwpx` | `.hwpx` `.docx` `.md` `.html` `.tex` `.htex` |
| Equations | kept as Hangul equations inside HWPX | also converted to LaTeX, MathML and Word equations |
| Result | a faithful HWPX copy | HWPX copy, or a draft to edit in the new format |

## Download v0.1.0 — HWPX only { #download-v010 }

Released October 2026. [Release page](https://github.com/krunyx/hwp2x/releases/tag/v0.1.0)

| System | Download | Size |
| --- | --- | --- |
| Windows 10/11, 64-bit | [hwp2x-0.1.0-windows-x64.zip](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-windows-x64.zip) | 60 MB |
| macOS, Apple silicon (M1 and later) | [hwp2x-0.1.0-macos-arm64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-macos-arm64.dmg) | 55 MB |
| macOS, Intel | [hwp2x-0.1.0-macos-x64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-macos-x64.dmg) | 59 MB |
| Linux, 64-bit | [hwp2x-0.1.0-linux-x64.tar.gz](https://github.com/krunyx/hwp2x/releases/download/v0.1.0/hwp2x-0.1.0-linux-x64.tar.gz) | 96 MB |

## Download v0.2.0 — more formats { #download-v020 }

Released October 2026. [Release page](https://github.com/krunyx/hwp2x/releases/tag/v0.2.0)

| System | Download | Size |
| --- | --- | --- |
| Windows 10/11, 64-bit | [hwp2x-0.2.0-windows-x64.zip](https://github.com/krunyx/hwp2x/releases/download/v0.2.0/hwp2x-0.2.0-windows-x64.zip) | 67 MB |
| macOS, Apple silicon (M1 and later) | [hwp2x-0.2.0-macos-arm64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.2.0/hwp2x-0.2.0-macos-arm64.dmg) | 59 MB |
| macOS, Intel | [hwp2x-0.2.0-macos-x64.dmg](https://github.com/krunyx/hwp2x/releases/download/v0.2.0/hwp2x-0.2.0-macos-x64.dmg) | 64 MB |
| Linux, 64-bit | [hwp2x-0.2.0-linux-x64.tar.gz](https://github.com/krunyx/hwp2x/releases/download/v0.2.0/hwp2x-0.2.0-linux-x64.tar.gz) | 102 MB |

Both versions install the same way, and installing one replaces the other.

## Install { #install }

=== "Windows"

    1. Right-click the zip file and choose **Extract All**. Keep the extracted folder together; the program needs the files next to it.
    2. Run **`hwp2x-gui.exe`** to open the app.
    3. If a "Windows protected your PC" window appears, click **More info → Run anyway**. This happens only the first time.

=== "macOS"

    1. Open the `.dmg` file and drag **hwp2x** into your Applications folder.
    2. Before the first launch, open Terminal and run this once:

        ```bash
        xattr -dr com.apple.quarantine /Applications/hwp2x.app
        ```

        Without it, macOS may say the app "is damaged" or "cannot be verified", because the app is not yet signed by Apple.
        Alternatively, try to open the app once, then go to **System Settings → Privacy & Security** and click **Open Anyway**.

=== "Linux"

    ```bash
    tar xzf hwp2x-*-linux-x64.tar.gz
    ./hwp2x/hwp2x-gui        # the app
    ./hwp2x/hwp2x --help     # the command line
    ```

    Requires glibc 2.35 or later (Ubuntu 22.04 and newer).
    On a minimal system install `libegl1` and `libxkbcommon0`, and a Korean font such as `fonts-noto-cjk` so file names display correctly.

!!! note "About the security warnings"
    hwp2x is not yet code-signed by Apple or Microsoft, so your system warns on first launch.
    The downloads are built by GitHub Actions directly from the [public source code](https://github.com/krunyx/hwp2x/blob/main/.github/workflows/build.yml).

## How to use { #use }

### The app

1. **Add files.** Drag files or whole folders onto the window, or use
   **파일 추가** (Add files) and **폴더 추가** (Add folder).
   **목록 비우기** (Clear list) empties the list.
2. **v0.2.0 only: choose the output** under **변환 형식** (Output format):
   HWPX, Word, Markdown, HTML, LaTeX or HyperTeX.
3. **Choose where to save** under **저장 위치** (Save location):
    - **원본과 같은 폴더** (Same folder as the original) — the default. `보고서.hwp` becomes `보고서.hwpx` next to it.
    - **다른 폴더** (Another folder) — pick a folder with **찾아보기** (Browse). Folder structure is kept.
4. **Set the options** if you need them:
    - **폴더 안의 하위 폴더까지 포함** — also convert files in sub-folders.
    - **같은 이름의 … 있으면 덮어쓰기** — overwrite an existing result file with the same name. Without it, such files are skipped.
5. **Click 변환 (Convert).** Click it again to stop after the files in progress.
6. **Check the results**, then open the output with **결과 폴더 열기** (Open result folder).

Each file gets one of these results. Files that failed or need checking move to the top of the list, with the reason.

| Result | Meaning |
| --- | --- |
| ✔ 완료 | Converted |
| △ 완료 (확인) | Converted, but check it. The message says why: something was cleaned up (usually a font name with characters XML does not allow), or, in v0.2.0, some content could not be carried into the chosen format. |
| – 건너뜀 | Skipped, because a result file with that name already exists |
| ✘ 실패 | Not converted. The reason is shown next to it. |

### The command line

The command line is handy for large folders and scripts.
It is `hwp2x.exe` in the Windows folder, `hwp2x/hwp2x` on Linux, and on macOS it lives inside the app:

```bash
alias hwp2x=/Applications/hwp2x.app/Contents/MacOS/hwp2x   # macOS: add to ~/.zshrc
```

```bash
hwp2x 보고서.hwp                       # creates 보고서.hwpx
hwp2x ./문서 -r -o ./변환결과          # include sub-folders; save into another folder, keeping the structure
hwp2x ./문서 -r -f -j 4                # overwrite existing results; convert 4 at a time

# v0.2.0
hwp2x 보고서.hwp -t docx               # creates 보고서.docx
hwp2x 보고서.hwpx -t md                # .hwpx files are accepted as input too
hwp2x ./문서 -r -t tex -o ./변환결과   # a whole folder to LaTeX
```

| Option | Meaning |
| --- | --- |
| `-t FORMAT` | **v0.2.0.** Output format: `hwpx` (default), `docx`, `md`, `html`, `tex`, `htex` |
| `-o FOLDER` | Save results in this folder (default: next to each original) |
| `-r` | Include sub-folders |
| `-f` | Overwrite existing result files |
| `-j N` | Number of files to convert at the same time |
| `--timeout SECONDS` | Time limit per file (default 300) |
| `-q` | Print only the files that failed |
| `-V` | Show the version |

Exit codes: `0` all succeeded, `1` some failed, `2` no files to convert, `3` the converter could not start.

### The Python library

```python
from hwp2x import convert, convert_all, plan

convert("보고서.hwp")                       # 보고서.hwpx
convert("보고서.hwp", "보고서.docx")        # v0.2.0: format follows the extension
results = convert_all(plan(["./문서"], "./변환결과", recursive=True, fmt="md"), overwrite=True)  # v0.2.0
```

The library is installed from source and needs Java 17 or later.
See the [README](https://github.com/krunyx/hwp2x#빌드) for the build steps.

## Other formats in v0.2.0 { #formats }

Formats other than HWPX carry over **content and structure**, not the look of the page.
Page size, text box positions and fonts are left behind, so treat the result as a first draft to finish by hand.

| Format | Extension | What you get |
| --- | --- | --- |
| HWPX | `.hwpx` | A faithful copy of the original (from `.hwp` input only) |
| Word | `.docx` | Headings, lists, tables with merged cells, footnotes, images and links; equations as Word equations |
| Markdown | `.md` | Content and structure; complex tables as HTML tables; equations as `$…$` |
| HTML | `.html` | A single web page with images; equations as MathML |
| LaTeX | `.tex` | A XeLaTeX/LuaLaTeX document; Hangul letters inside equations use [hangulmath](../hangulmath/index.md) |
| HyperTeX | `.htex` | A [HyperTeX](../hypertex/index.md) document |

For Markdown, LaTeX and HyperTeX, images are saved in a `name_files/` folder next to the result.
If both `보고서.hwp` and `보고서.hwpx` are in a folder, only the `.hwp` is converted.

**Equations.** Equations from Hangul's equation editor (`{a+b} over c`, `sqrt`, `sum from … to …`, `matrix`, `cases`, `left ( … right )` and so on)
are translated: `{a+b} over c` becomes `\frac{a+b}{c}` in LaTeX, MathML in HTML and a native equation in Word.

**Not carried over** to formats other than HWPX: headers and footers, page numbers, hidden comments, memos,
form controls (buttons, input fields) and OLE objects such as charts.
When something is left out, the file is marked **△ 완료 (확인)** with what was dropped.
HyperTeX has no vertical cell merging or strikethrough, so merged cells keep their content in the first cell and strikethrough is removed.

## Documents that are not converted { #limits }

These apply to both versions and every format.

| Document | Why, and what to do |
| --- | --- |
| Password-protected | Remove the password in Hangul, then convert. |
| Distribution documents (배포용 문서) | Their copy and print restrictions would be lost, so hwp2x leaves them as they are. |
| HWP 3.x (Hangul 97 and earlier) | Only HWP 5.x is supported. Open the file in Hangul, save it again, then convert. |

## Report a problem or send feedback { #feedback }

If a document does not convert, looks wrong after converting, or you have an idea, please tell us.
Reports on the v0.2.0 formats are especially welcome: they show us what to improve first.

[Email hello@krunyx.com](mailto:hello@krunyx.com?subject=%5Bhwp2x%5D%20){ .md-button .md-button--primary }
[Open a GitHub issue](https://github.com/krunyx/hwp2x/issues/new){ .md-button }

Writing in Korean is fine. It helps if you include:

- your operating system, and the hwp2x version (`hwp2x -V`)
- the output format you chose
- the result shown in the list and the message next to it
- what you expected and what you saw

A sample file helps us fix problems fastest. Only send one if it contains nothing confidential;
otherwise a description, or a copy with the text replaced, is enough.

## License

hwp2x is released under the [Apache License 2.0](https://github.com/krunyx/hwp2x/blob/main/LICENSE).
The conversion engine is built from neolord0's [hwplib](https://github.com/neolord0/hwplib),
[hwpxlib](https://github.com/neolord0/hwpxlib) and [hwp2hwpx](https://github.com/neolord0/hwp2hwpx), all Apache-2.0.
The bundled Java runtime is OpenJDK (GPLv2 with the Classpath Exception); v0.2.0 also bundles Pillow (HPND license) for image conversion.

“본 제품은 한글과컴퓨터의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.”
<br><small>(This product was developed with reference to Hancom's published HWP document file format specification.)</small>
