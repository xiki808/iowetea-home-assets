# CONTEXT.md

## Repo Overview

A static asset repository for the IOweTea project. It holds the parent and Home marks, matching dark and light icon palettes in multiple sizes, and web documents (such as the privacy policy) that need to be publicly accessible. The repository is deployed via **GitHub Pages**, making all files available at:

```
https://xiki808.github.io/iowetea-assets/
```

There is no build step — files are served as-is.

## Directory Structure

```
brand/
├── iowetea.svg                 # Parent cup source
├── iowetea-icon.svg            # Parent cup on brand-sheet background
├── iowetea-icon-1024.png       # Parent icon reference
├── iowetea-light.svg           # Parent light mark
├── iowetea-icon-light.svg      # Parent light icon
├── iowetea-icon-light-1024.png # Parent light icon reference
├── home.svg                     # Home source
├── home-icon.svg                # Home on dark background
├── home-light.svg               # Home mark for light surfaces
├── home-icon-light.svg          # Home on warm light background
├── home-icon-staging.svg        # Home with green staging ribbon
├── home-icon-staging-light.svg  # Light staging icon
├── generate.py                 # Regenerate the icon set
├── sync-consumers.py           # Refresh sibling web and app icon copies
└── home/
    ├── icon-*.png              # 16, 32, 48, 72, 96, 144, 180, 192, 512, 1024
    ├── favicon.ico             # Browser favicon
    ├── manifest.json           # PWA web app manifest
    ├── staging/icon-1024.png   # Staging icon
    └── light/                  # Light sizes, favicon, and PWA manifest
web-documents/
├── privacy-policy.html         # Required by Google Play and Apple App Store for app approval
├── account-deletion.html       # Google Play account-deletion URL
└── support.html                # Store support URL
store/                          # Store artwork and listing worksheets (see Store Artwork)
```

## Web Documents

### privacy-policy.html

The privacy policy is a required document for app store submissions. It is referenced by both the Flutter app and the Vue web app, pointing to the GitHub Pages URL:

```
https://xiki808.github.io/iowetea-assets/web-documents/privacy-policy.html
```

**Consumers:**

- **app** (`app/lib/helpers/configs.dart`) — defines `privacyPolicyURL` constant; the WebView intercepts navigation to this URL and opens it in the system browser
- **web** (`src/components/common/ThreeDotMenuComponent.vue`) — links to it from the three-dot menu

### account-deletion.html

Public account-deletion page, used as the Google Play account-deletion URL. It explains how to delete an account in the app (Dashboard > Users > My Account > Delete Account), what is deleted, and how to request deletion without the app. Same plain markup as the privacy policy, which it links to.

```
https://xiki808.github.io/iowetea-assets/web-documents/account-deletion.html
```

It is not linked from the web app.

### support.html

Public app support contact page for the App Store Support URL and Google Play
website/contact field. It gives the existing `info.iowetea@gmail.com` address,
getting-started instructions, and links to the privacy and deletion pages.

```
https://xiki808.github.io/iowetea-assets/web-documents/support.html
```

### Customer-facing naming

Public documents and store listing copy describe IOweTea features ("device
control", "VPN", "DNS filtering service") rather than the services installed on
the home server (Home Assistant, AdGuard, Frigate, WireGuard, WGDashboard), per
the workspace rule `context/iowetea-customer-facing-naming.md` (tsk-473).
Outside processors whose identity matters to the privacy disclosure (Firebase
Cloud Messaging/Google, Apple Push Notification service, Cloudflare, Quad9,
OpenStreetMap) keep their names. Owner-only notes in the store worksheets
(VpnService declaration, export compliance) may name WireGuard, because those
answers must describe the actual implementation. Any wording change in a
privacy or deletion document goes to the owner for review, even when no claim
changes.

## Brand Assets

The parent IOweTea cup source is `brand/iowetea.svg`. The product mark is
`brand/home.svg`, with a Wi-Fi teabag and circuits inside and below the cup.
Both icons use the shared dark `#0A0F0A` background, warm white cup outlines,
green leaf, and bronze teabag. The parent cup uses Hibiscus `#B55A70`; Home uses
the web app's primary green `#2A8744` for its liquid and circuits. The liquid
extends beneath the cup outline so no dark seam appears at the lower edge.
Light variants use a warm `#F5F2EB` background and charcoal outline, with the
same leaf, teabag, and product accents. Follow the shared
[branding contract](../../../branding/contract.md). Run
`python3 brand/generate.py` and
`python3 brand/sync-consumers.py` to rebuild and distribute them. Square icons
center the combined cup and leaf with equal opposite margins to the border;
the handle and Home circuits below the cup are excluded from that measurement.
The single `brand/home/` set includes:

- **PNG sizes**: 16×16, 32×32, 48×48, 72×72, 96×96, 144×144, 180×180, 192×192, 512×512, 1024×1024
- **favicon.ico**: Multi-resolution icon for browser tabs
- **manifest.json**: PWA manifest referencing the 192×192 and 512×512 PNGs
- **staging/**: A staging-specific 1024×1024 variant (used to distinguish staging builds visually)

## Store Artwork

`store/` contains the Google Play icon, feature graphic, phone, tablet and
Chromebook screenshots, plus App Store iPhone, iPhone Duo and iPad screenshots,
optional header and search-result artwork, and an opaque icon reference. The
screenshots come from the sibling web repo's disposable demo bundle. See
`store/README.md` for exact sizes, regeneration, the final native review step,
and platform-specific console worksheets. The privacy-policy page was rewritten
for the current app, home server and linked services on 2026-10-27; check its
claims against the final builds and store privacy answers before submission.
Icons and promotional graphics now use the Home brand. Screenshots and listing
worksheets still describe the current IOweTea app UI; update and review them
with the app/web naming rollout before publishing a rebranded listing.

## Related Repos

- **app** - Repository Path: `@../app`
  Loads the privacy policy URL via system browser when the user taps the link inside the WebView.
- **web** - Repository Path: `@../web`
  Links to the privacy policy from the three-dot menu in `ThreeDotMenuComponent.vue`.
