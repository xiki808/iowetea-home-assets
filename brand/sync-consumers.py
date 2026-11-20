#!/usr/bin/env python3
"""Copy the single Home palette into the sibling web and app icon assets."""

from pathlib import Path
import shutil
import subprocess


ASSETS = Path(__file__).resolve().parents[1]
SIBLINGS = ASSETS.parent
HOME = ASSETS / "brand" / "home"
WEB = SIBLINGS / "web" / "public" / "favicons"
APP = SIBLINGS / "app"


def native_icon(source, destination):
    dimensions = subprocess.check_output(
        ["identify", "-format", "%wx%h", str(destination)], text=True
    )
    subprocess.run(
        ["convert", str(source), "-resize", f"{dimensions}!", "-strip", "-alpha", "off",
         f"PNG24:{destination}"],
        check=True,
    )


def main():
    for size in (16, 32, 180, 192, 512):
        shutil.copyfile(HOME / f"icon-{size}.png", WEB / f"home-{size}x{size}.png")
    shutil.copyfile(HOME / "favicon.ico", WEB / "favicon.ico")
    for pattern in ("iowetea-*.png", "hub-*.png"):
        for legacy in WEB.glob(pattern):
            legacy.unlink()

    launchers = APP / "assets" / "launcher_icon"
    prod = launchers / "home-icon-prod.png"
    staging = launchers / "home-icon-staging.png"
    shutil.copyfile(HOME / "icon-1024.png", prod)
    shutil.copyfile(HOME / "staging" / "icon-1024.png", staging)
    for pattern in ("iowetea-icon-*.png", "hub-icon-*.png"):
        for legacy in launchers.glob(pattern):
            legacy.unlink()

    android = APP / "android" / "app" / "src"
    for flavor in ("main", "prod", "staging"):
        source = staging if flavor == "staging" else prod
        for destination in (android / flavor / "res").glob("mipmap-*/ic_launcher.png"):
            native_icon(source, destination)

    ios = APP / "ios" / "Runner" / "Assets.xcassets"
    for icon_set in ("AppIcon", "AppIcon-prod", "AppIcon-staging"):
        source = staging if icon_set.endswith("staging") else prod
        for destination in (ios / f"{icon_set}.appiconset").glob("*.png"):
            native_icon(source, destination)


if __name__ == "__main__":
    main()
