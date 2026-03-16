# STL Viewer 🖨️

A lightweight, zero-dependency 3D STL file viewer that runs entirely in the browser. Built with [Three.js](https://threejs.org/) — no installation, no build step, no server required.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-4fffb0?style=flat-square&logo=github)](https://YOUR_USERNAME.github.io/stl-viewer)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Three.js](https://img.shields.io/badge/Three.js-r128-00c8ff?style=flat-square)](https://threejs.org/)

![STL Viewer Screenshot](docs/screenshot.png)

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

### Option A — Open locally
```bash
git clone https://github.com/YOUR_USERNAME/stl-viewer.git
cd stl-viewer
open index.html   # macOS
# or just double-click index.html in your file explorer
```

### Option B — GitHub Pages (live URL)
Push to `main` and enable GitHub Pages from **Settings → Pages → Source: main branch / root**.  
Your viewer will be live at `https://YOUR_USERNAME.github.io/stl-viewer`.

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
stl-viewer/
├── index.html                  # Main viewer (single-file, no build needed)
├── models/
│   └── pixel10a_holder.stl     # Sample model — Pixel 10a phone holder
├── scripts/
│   └── generate_holder.py      # Python script to regenerate the STL
├── docs/
│   └── screenshot.png          # README screenshot
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Pages auto-deploy workflow
├── .gitignore
├── LICENSE
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
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## License

MIT © [Your Name](https://github.com/YOUR_USERNAME)
