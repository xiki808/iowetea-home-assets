# IOweTea and Home assets

This repository contains the static brand files and public web documents used by
IOweTea. GitHub Pages serves the repository contents as-is at
`https://xiki808.github.io/iowetea-assets/`; there is no build or publish
command in this repository.

## Contents

```text
brand/
  iowetea.svg           Parent IOweTea cup mark
  iowetea-icon.svg      Parent icon on its brand-sheet background
  iowetea-light.svg     Parent mark for light surfaces
  iowetea-icon-light.svg  Parent light icon
  home.svg               IOweTea Home mark
  home-icon.svg          Home icon on its brand-sheet background
  home-light.svg        Home mark for light surfaces
  home-icon-light.svg   Home light icon
  home-icon-staging.svg  Home icon with a green staging ribbon
  home-icon-staging-light.svg  Light staging icon
  generate.py           Rebuilds the parent and Home icons
  sync-consumers.py     Refreshes the sibling web and app icon copies
  home/                  Default dark Home icons and PWA manifest
    light/               Matching light icons, favicon, and manifest
web-documents/
  privacy-policy.html   Public privacy policy
  account-deletion.html Public account deletion instructions
  support.html          Public support contact and help
store/
  google-play/          Listing icon, feature graphic, phone screenshots
  app-store/            iPhone and iPad screenshots, icon reference
```

`brand/home/` contains the default dark Home icon set. `brand/home/light/`
contains the matching light set:

- `icon-<size>.png` at 16, 32, 48, 72, 96, 144, 180, 192, 512, and
  1024 pixels.
- `favicon.ico` for browser tabs.
- `manifest.json` for PWA metadata; it references the 192 and 512 pixel icons.
- `staging/icon-1024.png` in each set, the staging icon with a green ribbon.

The parent cup in Hibiscus `#B55A70` is kept separately as `brand/iowetea.svg`,
`brand/iowetea-icon.svg`, and `brand/iowetea-icon-1024.png`. Home's Wi-Fi teabag
and circuit artwork comes from `brand/home.svg`. Run
`python3 brand/generate.py` to regenerate the icons, then
`python3 brand/sync-consumers.py` to refresh the sibling web favicons and app
launcher icons. The icon and manifest use the shared dark `#0A0F0A` background;
Home's cup liquid and circuits use the web app's primary green `#2A8744`.
The light icons use a warm `#F5F2EB` background and charcoal cup outlines;
leaf, teabag, product color, geometry, and spacing stay the same. The app and
current dark web interface continue to use the dark icons.
All icons center the shared cup and leaf while excluding the handle and the
Home circuits below the cup.

## Public paths

Files retain their repository-relative paths when published. For example:

- `https://xiki808.github.io/iowetea-assets/brand/home/icon-512.png`
- `https://xiki808.github.io/iowetea-assets/brand/home/manifest.json`
- `https://xiki808.github.io/iowetea-assets/web-documents/privacy-policy.html`

The privacy-policy page is used by the IOweTea app and web interface. The app
opens this page in the system browser, while the web interface links to it from
its menu.

See [store/README.md](store/README.md) for the store artwork inventory,
generation command, final native screenshot check, and console worksheets.

## Working safely

Because these files are publicly served, changes to a filename, directory, or
published document path can break existing links. The former `brand/dark/` and
`brand/light/` paths are replaced by `brand/home/`; update any external users of
those URLs. Review rendered documents and image dimensions before merging;
there is no local build step to catch broken static links.
