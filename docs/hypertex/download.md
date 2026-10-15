# Download HyperTeX

The latest version is **v0.2.0** (October 2026). See [what's new](changelog.md#v0-2-0).
All installers are also on the [GitHub releases page](https://github.com/krunyx/hypertex/releases/latest).

[Open the latest release](https://github.com/krunyx/hypertex/releases/latest){ .md-button .md-button--primary }

## Install by operating system

=== "macOS"

    | Download | For |
    | --- | --- |
    | [HyperTeX-0.2.0-macos-arm64.dmg](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-0.2.0-macos-arm64.dmg) | Apple silicon (M1 and later) |
    | [HyperTeX-0.2.0-macos-x86_64.dmg](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-0.2.0-macos-x86_64.dmg) | Intel Macs |

    1. Open the `.dmg` file.
    2. Drag HyperTeX into your Applications folder.
    3. If the first launch warns about an unidentified developer, **right-click HyperTeX in Applications and choose Open**. You only need to do this once.

=== "Windows"

    | Download | For |
    | --- | --- |
    | [HyperTeX-Setup-0.2.0.exe](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-Setup-0.2.0.exe) | Installer for Windows 10 and 11 |
    | [HyperTeX-0.2.0-windows-x64.zip](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-0.2.0-windows-x64.zip) | Portable version: unzip and run `htex-viewer\htex-viewer.exe` |

    The installer works without administrator rights. After installing, `.htex` files and `htex://` links open in HyperTeX.
    The portable version does not register file types or links.

    If a "Windows protected your PC" window appears, click **More info → Run anyway**.

=== "Linux"

    | Download | How to install |
    | --- | --- |
    | [HyperTeX-0.2.0-x86_64.AppImage](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-0.2.0-x86_64.AppImage) | Make it executable and run it |
    | [HyperTeX-0.2.0-linux-x86_64.tar.gz](https://github.com/krunyx/hypertex/releases/download/v0.2.0/HyperTeX-0.2.0-linux-x86_64.tar.gz) | Unpack and run `install.sh` |

    AppImage:

    ```bash
    chmod +x HyperTeX-*-x86_64.AppImage
    ./HyperTeX-*-x86_64.AppImage
    ```

    tar.gz (installs into `~/.local` and registers `.htex` and `htex://`):

    ```bash
    tar xzf HyperTeX-*-linux-x86_64.tar.gz
    cd HyperTeX-*/
    ./install.sh              # to remove: ./install.sh --uninstall
    ```

!!! note "About the install warnings"
    This version is not yet code-signed by Apple or Microsoft, so your system warns on first launch.
    The installers are built by GitHub Actions directly from the public source code. Signing is planned for a future release.
    To check a download, compare its SHA-256 with [SHA256SUMS.txt](https://github.com/krunyx/hypertex/releases/download/v0.2.0/SHA256SUMS.txt).

## Install with Python

Requires Python 3.10 or later.

```bash
git clone https://github.com/krunyx/hypertex.git
cd hypertex
pip install .              # parser, HTML renderer, web server (no extra dependencies)
pip install ".[viewer]"    # plus the desktop viewer (PySide6)
```

To register a pip-installed viewer with a Linux desktop, run `packaging/linux/install.sh --pip`.

## Next step

Once installed, open the example document in [Get started](getting-started.md).
