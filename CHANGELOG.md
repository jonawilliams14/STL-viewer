# Changelog

All notable changes to this project will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2026-03-16

### Added
- Initial release of STL Viewer
- Binary and ASCII STL parsing (pure browser, no server)
- Three.js r128 WebGL renderer with ACES filmic tone mapping
- Orbit, pan, and zoom controls (mouse + multi-touch)
- Render modes: Solid, Wireframe, Both
- 6 material color presets
- Ambient/key light intensity sliders
- Metalness and roughness material controls
- Mesh stats panel (triangles, vertices, bounding box in mm)
- Snap views: Front, Top, Isometric
- Auto-rotate toggle
- Grid floor toggle
- Live XYZ axis gizmo (2D canvas overlay)
- Drag-and-drop STL loading
- File browser STL loading
- Mobile touch support (swipe orbit, pinch zoom)
- Google Pixel 10a holder sample model (`models/pixel10a_holder.stl`)
- Python STL generator script (`scripts/generate_holder.py`)
- GitHub Pages auto-deploy workflow

### Fixed
- `ReferenceError: Cannot access 'gctx' before initialization` — moved gizmo
  canvas setup above the `animate()` call so `drawGizmo()` is never invoked
  before `gctx` is declared

---

## [Unreleased]

### Planned
- Section cut / clipping plane tool
- Measurement tool (point-to-point distance)
- Export screenshot (PNG)
- Multiple model loading / scene management
- Model info extraction (volume, surface area estimation)
