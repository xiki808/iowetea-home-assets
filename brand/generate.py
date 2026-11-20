#!/usr/bin/env python3
"""Render dark and light IOweTea and Home marks for web, mobile, and store."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
SIZES = (16, 32, 48, 72, 96, 144, 180, 192, 512, 1024)
DARK = "#0a0f0a"
LIGHT = "#f5f2eb"


def element(name, attrs=None):
    return ET.Element(f"{{{SVG}}}{name}", attrs or {})


def mark(source):
    tree = ET.parse(ROOT / source)
    return [deepcopy(child) for child in tree.getroot() if child.tag != f"{{{SVG}}}title"]


def light_mark(source, output):
    tree = ET.parse(ROOT / source)
    root = tree.getroot()
    for node in root.iter():
        if node.get("stroke") == "#fffdf8":
            node.set("stroke", "#242329")
        elif node.get("stroke") == DARK:
            node.set("stroke", "#242329")
        if node.get("fill") == DARK:
            node.set("fill", "#242329" if node.get("r") == "2.2" else "#fffdf8")
    title = root.find(f"{{{SVG}}}title")
    if title is not None:
        title.text += " — light mode"
    ET.indent(root, space="  ")
    (ROOT / output).write_text(ET.tostring(root, encoding="unicode") + "\n")


def icon(source, output, background, staging=False):
    svg = element("svg", {"viewBox": "0 0 1024 1024"})
    svg.append(element("rect", {"width": "1024", "height": "1024", "fill": background}))
    # Center the shared cup-and-leaf bounds, excluding the handle and
    # Home's circuits below the cup. Their center is (128, 116).
    scale = 3.1
    x = 512 - 128 * scale
    y = 512 - 116 * scale
    group = element("g", {"transform": f"translate({x} {y}) scale({scale})"})
    group.extend(mark(source))
    svg.append(group)
    if staging:
        svg.append(element("path", {"d": "M490 0h360l174 145v205z", "fill": "#2a8744"}))
        label = element("text", {
            "x": "830", "y": "125",
            "fill": "#fff", "font-family": "DejaVu Sans, sans-serif",
            "font-size": "44", "font-weight": "700", "text-anchor": "middle",
        })
        label.text = "DEV MODE"
        svg.append(label)
    ET.indent(svg, space="  ")
    (ROOT / output).write_text(ET.tostring(svg, encoding="unicode") + "\n")


def render(source, output, size):
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "convert", "-background", "none", "-density", "384", str(ROOT / source),
        "-resize", f"{size}x{size}!", "-strip", "-depth", "8", f"PNG24:{output}",
    ], check=True)


def main():
    light_mark("iowetea.svg", "iowetea-light.svg")
    light_mark("home.svg", "home-light.svg")

    icon("iowetea.svg", "iowetea-icon.svg", DARK)
    render("iowetea-icon.svg", ROOT / "iowetea-icon-1024.png", 1024)
    icon("iowetea-light.svg", "iowetea-icon-light.svg", LIGHT)
    render("iowetea-icon-light.svg", ROOT / "iowetea-icon-light-1024.png", 1024)

    icon("home.svg", "home-icon.svg", DARK)
    home_dir = ROOT / "home"
    for size in SIZES:
        render("home-icon.svg", home_dir / f"icon-{size}.png", size)
    subprocess.run([
        "convert",
        *(str(home_dir / f"icon-{size}.png") for size in (16, 32, 48)),
        str(home_dir / "favicon.ico"),
    ], check=True)
    icon("home.svg", "home-icon-staging.svg", "#0a0f0a", staging=True)
    render("home-icon-staging.svg", home_dir / "staging" / "icon-1024.png", 1024)

    icon("home-light.svg", "home-icon-light.svg", LIGHT)
    light_dir = home_dir / "light"
    for size in SIZES:
        render("home-icon-light.svg", light_dir / f"icon-{size}.png", size)
    subprocess.run([
        "convert",
        *(str(light_dir / f"icon-{size}.png") for size in (16, 32, 48)),
        str(light_dir / "favicon.ico"),
    ], check=True)
    light_manifest = json.loads((home_dir / "manifest.json").read_text())
    light_manifest["theme_color"] = LIGHT
    light_manifest["background_color"] = LIGHT
    (light_dir / "manifest.json").write_text(json.dumps(light_manifest, indent=2) + "\n")
    icon("home-light.svg", "home-icon-staging-light.svg", LIGHT, staging=True)
    render("home-icon-staging-light.svg", light_dir / "staging" / "icon-1024.png", 1024)


if __name__ == "__main__":
    main()
