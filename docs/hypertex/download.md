# Download HyperTeX

The latest version is **v0.1.0**. All installers are on the [GitHub releases page](https://github.com/krunyx/hypertex/releases/latest).

[Open the latest release](https://github.com/krunyx/hypertex/releases/latest){ .md-button .md-button--primary }

## Install by operating system

=== "macOS"

    | File | For |
    | --- | --- |
    | `HyperTeX-<version>-macos-arm64.dmg` | Apple silicon (M1 and later) |
    | `HyperTeX-<version>-macos-x86_64.dmg` | Intel Macs |

    1. Open the `.dmg` file.
    2. Drag HyperTeX into your Applications folder.
    3. If the first launch warns about an unidentified developer, **right-click HyperTeX in Applications and choose Open**. You only need to do this once.

=== "Windows"

    | File | For |
    | --- | --- |
    | `HyperTeX-Setup-<version>.exe` | Windows 10 and 11 |

    Installs without administrator rights. After installing, `.htex` files and `htex://` links open in HyperTeX.

    If a "Windows protected your PC" window appears, click **More info → Run anyway**.

=== "Linux"

    | File | How to install |
    | --- | --- |
    | `HyperTeX-<version>-x86_64.AppImage` | Make it executable and run it |
    | `HyperTeX-<version>-linux-x86_64.tar.gz` | Unpack and run `install.sh` |

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
