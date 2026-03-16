# STL Viewer 🖨️

A lightweight, zero-dependency 3D STL file viewer that runs entirely in the browser. Built with [Three.js](https://threejs.org/) — no installation, no build step, no server required.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-4fffb0?style=flat-square&logo=github)](https://jonawilliams14.github.io/STL-viewer)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Three.js](https://img.shields.io/badge/Three.js-r128-00c8ff?style=flat-square)](https://threejs.org/)

---

## 🌐 Live Demo

**[jonawilliams14.github.io/STL-viewer](https://jonawilliams14.github.io/STL-viewer)**

---

## Features

- **Drag & drop** any `.stl` file or use the file browser
- Supports both **binary and ASCII** STL formats
- **Orbit, pan, and zoom** controls (mouse + touch)
- **Render modes** — Solid, Wireframe, or Both
- **6 material color presets** for filament visualization
- Adjustable **ambient/key lighting**, metalness, and roughness
- **Mesh stats** — triangle count, vertex count, bounding box dimensions (mm)
- **Snap views** — Front, Top, Isometric
- **Auto-rotate** toggle
- **Grid floor** toggle
- Live **XYZ axis gizmo**
- Fully **responsive** — works on desktop and mobile

---

## Included Models

| File | Description |
|------|-------------|
| `models/pixel10a_holder.stl` | Google Pixel 10a handheld phone holder with ergonomic grip and ventilation perforations |

---

## Usage

### Option A — GitHub Pages (live)
Visit **[jonawilliams14.github.io/STL-viewer](https://jonawilliams14.github.io/STL-viewer)** directly in any browser.

### Option B — Open locally
```bash
git clone https://github.com/jonawilliams14/STL-viewer.git
cd STL-viewer
open index.html   # macOS
# or double-click index.html in your file explorer
```

### Option C — Any static host
Upload `index.html` to Netlify, Vercel, S3, or any static host. No build step needed.

---

## Generating New STL Models

The included `scripts/generate_holder.py` script regenerates the Pixel 10a holder STL using only Python + NumPy:

```bash
pip install numpy
python scripts/generate_holder.py
# Output: models/pixel10a_holder.stl
```

Modify the constants at the top of the script to customize dimensions, wall thickness, perforation size, grip geometry, etc.

---

## Controls

| Input | Action |
|-------|--------|
| Left drag | Orbit |
| Right drag | Pan |
| Scroll wheel | Zoom |
| Pinch (touch) | Zoom |
| Swipe (touch) | Orbit |

---

## Project Structure

```
STL-viewer/
├── index.html                       ← Main viewer (single-file, no build needed)
├── models/
│   ├── pixel10a_holder.stl          ← Sample model: Pixel 10a phone holder
│   └── README.md
├── scripts/
│   └── generate_holder.py           ← Python script to regenerate the STL
├── docs/                            ← Screenshots and documentation assets
├── .github/
│   └── workflows/
│       └── deploy.yml               ← Auto-deploys to GitHub Pages on push to main
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

---

## Browser Support

| Browser | Status |
|---------|--------|
| Chrome 90+ | ✅ Full support |
| Firefox 88+ | ✅ Full support |
| Safari 15+ | ✅ Full support |
| Edge 90+ | ✅ Full support |
| Mobile Chrome/Safari | ✅ Touch controls |

---

## Tech Stack

- **[Three.js r128](https://threejs.org/)** — 3D rendering (loaded via CDN)
- **[Syne](https://fonts.google.com/specimen/Syne) + [Space Mono](https://fonts.google.com/specimen/Space+Mono)** — Typography (Google Fonts)
- Vanilla HTML/CSS/JS — zero npm, zero build tooling

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push and open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## License

MIT © [jonawilliams14](https://github.com/jonawilliams14)
