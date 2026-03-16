# Models

This directory contains sample `.stl` files included with the STL Viewer.

| File | Dimensions | Description |
|------|-----------|-------------|
| `pixel10a_holder.stl` | 77.8 × 158.7 × 11.4 mm | Google Pixel 10a handheld phone holder |

## Pixel 10a Holder Specs

- **Phone fit:** 153.9 × 73 × 9 mm + 0.4 mm tolerance per side
- **Wall thickness:** 2.0 mm sides, 2.0 mm back plate
- **Front lip:** 2.5 mm retaining lip
- **Ventilation:** 105 × ⌀7 mm perforations on a 10 mm grid
- **Grip:** 72 × 45 × 14 mm ergonomic palm paddle
- **Total triangles:** 6,448

## Adding Your Own Models

Place any `.stl` file in this directory and load it via the viewer's drag-and-drop or file browser interface.

To regenerate `pixel10a_holder.stl`:
```bash
cd ..
python scripts/generate_holder.py
```
