"""Copy the krunyx Flow brand kit into the site.

Usage:
    python tools/brand_assets.py /path/to/krunyx-flow-1.0

What it does:
  * copies the symbol, the horizontal logo lockups and the vertical logo into
    docs/assets/images/brand/, with the viewBox trimmed to the drawing so the
    logos line up with text;
  * copies the favicons to the site root (docs/), where browsers look for them;
  * builds the home-page hero backgrounds (hero-waves-dark.svg and
    hero-waves-light.svg) from the brand wallpapers: the ribbons only, without
    the sky, the centred logo or the tagline, so the page colour shows through.

Run it again whenever the brand kit changes, then rebuild the site.
"""

import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BRAND = DOCS / "assets" / "images" / "brand"

# source file -> (file name in the site, trimmed viewBox or None)
LOGOS = {
    "02-symbols/symbol-primary.svg": ("symbol.svg", "18 18 284 284"),
    "05-web-headers/web-logo-dark.svg": ("logo-on-dark.svg", "12 22 968 243"),
    "05-web-headers/web-logo-light.svg": ("logo-on-light.svg", "12 22 968 243"),
    "01-logos/logo-vertical-primary.svg": ("logo-vertical.svg", "60 16 530 722"),
}
FAVICONS = {
    "04-favicons/favicon.svg": "favicon.svg",
    "04-favicons/favicon.ico": "favicon.ico",
    "04-favicons/favicon-180x180.png": "apple-touch-icon.png",
    "04-favicons/favicon-192x192.png": "icon-192.png",
}
# The hero shows the lower part of the wallpaper, where the ribbons are.
HERO_VIEWBOX = "0 360 3840 1800"


def tag(el):
    return el.tag.split("}")[-1]


def write(tree, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=False)
    print("wrote", path.relative_to(ROOT))


def copy_logo(src, dest, viewbox):
    tree = ET.parse(src)
    svg = tree.getroot()
    if viewbox:
        x, y, w, h = viewbox.split()
        svg.set("viewBox", viewbox)
        svg.set("width", w)
        svg.set("height", h)
    write(tree, dest)


def hero_waves(src, dest):
    tree = ET.parse(src)
    svg = tree.getroot()
    for child in list(svg):
        name = tag(child)
        # Drop the sky (the page background shows instead), the centred
        # symbol and wordmark (both placed with a transform) and the tagline.
        if name in ("rect", "text", "g", "title", "desc") or child.get("transform"):
            svg.remove(child)
    svg.set("viewBox", HERO_VIEWBOX)
    svg.set("preserveAspectRatio", "xMidYMax slice")
    svg.attrib.pop("width", None)
    svg.attrib.pop("height", None)
    svg.set("aria-hidden", "true")
    svg.attrib.pop("role", None)
    svg.attrib.pop("aria-label", None)
    write(tree, dest)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    kit = Path(sys.argv[1]).expanduser()
    for src, (name, viewbox) in LOGOS.items():
        copy_logo(kit / src, BRAND / name, viewbox)
    for src, name in FAVICONS.items():
        shutil.copyfile(kit / src, DOCS / name)
        print("wrote", (DOCS / name).relative_to(ROOT))
    hero_waves(kit / "07-wallpapers/wallpaper-dark.svg", BRAND / "hero-waves-dark.svg")
    hero_waves(kit / "07-wallpapers/wallpaper-light.svg", BRAND / "hero-waves-light.svg")


if __name__ == "__main__":
    main()
