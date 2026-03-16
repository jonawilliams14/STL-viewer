"""
generate_holder.py
==================
Generates the Google Pixel 10a phone holder STL using only Python + NumPy.
No external 3D library required.

Usage:
    pip install numpy
    python scripts/generate_holder.py

Output:
    models/pixel10a_holder.stl

Customization:
    Edit the constants in the "Configuration" section below.
"""

import numpy as np
import struct
import os

# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────

# Google Pixel 10a dimensions (mm)
PHONE_HEIGHT    = 153.9
PHONE_WIDTH     = 73.0
PHONE_THICKNESS = 9.0

# Case geometry
WALL_THICKNESS  = 2.0    # side/top/bottom wall thickness (mm)
LIP_DEPTH       = 2.5    # front retaining lip depth (mm)
BACK_WALL       = 2.0    # back plate thickness (mm)
TOLERANCE       = 0.4    # per-side fit clearance (mm)

# Grip / handle (ergonomic paddle below phone)
GRIP_WIDTH      = 72.0   # handle width (mm) — approx palm width
GRIP_HEIGHT     = 45.0   # handle height for fingers (mm)
GRIP_THICKNESS  = 14.0   # handle depth — comfortable palm hold (mm)
GRIP_RADIUS     = 6.0    # corner fillet radius (mm)
NECK_HEIGHT     = 6.0    # transition neck height (mm)
NECK_WIDTH      = 42.0   # neck width — narrower than grip for ergonomics (mm)

# Ventilation perforations (back plate)
PERF_RADIUS     = 3.5    # hole radius (mm)
PERF_SPACING    = 10.0   # center-to-center grid spacing (mm)
PERF_SEGMENTS   = 16     # polygon approximation segments per hole

# Output path (relative to repo root)
OUTPUT_PATH     = os.path.join(os.path.dirname(__file__), '..', 'models', 'pixel10a_holder.stl')

# ─────────────────────────────────────────────────────────────────────────────
# Triangle accumulator
# ─────────────────────────────────────────────────────────────────────────────

triangles = []  # list of (normal, v0, v1, v2)

def add_tri(v0, v1, v2):
    v0, v1, v2 = np.array(v0, float), np.array(v1, float), np.array(v2, float)
    n = np.cross(v1 - v0, v2 - v0)
    ln = np.linalg.norm(n)
    n = n / ln if ln > 1e-12 else np.array([0, 0, 1])
    triangles.append((n, v0, v1, v2))

def add_quad(v0, v1, v2, v3):
    add_tri(v0, v1, v2)
    add_tri(v0, v2, v3)

# ─────────────────────────────────────────────────────────────────────────────
# Geometry helpers
# ─────────────────────────────────────────────────────────────────────────────

def extrude_polygon(poly_xy, z0, z1, cap_bottom=True, cap_top=True, flip_winding=False):
    """Extrude a 2D polygon (CCW) along Z from z0 to z1."""
    n = len(poly_xy)
    vb = [np.array([x, y, z0]) for x, y in poly_xy]
    vt = [np.array([x, y, z1]) for x, y in poly_xy]
    if flip_winding:
        vb, vt = vt, vb
    for i in range(n):
        j = (i + 1) % n
        add_quad(vb[i], vb[j], vt[j], vt[i])
    if flip_winding:
        vb, vt = vt, vb
    if cap_bottom:
        for i in range(1, n - 1):
            if flip_winding:
                add_tri(vb[0], vb[i + 1], vb[i])
            else:
                add_tri(vb[0], vb[i], vb[i + 1])
    if cap_top:
        for i in range(1, n - 1):
            if flip_winding:
                add_tri(vt[0], vt[i], vt[i + 1])
            else:
                add_tri(vt[0], vt[i + 1], vt[i])

def rect_poly(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]

def circle_poly(cx, cy, r, segs=PERF_SEGMENTS):
    return [(cx + r * np.cos(2 * np.pi * i / segs),
             cy + r * np.sin(2 * np.pi * i / segs)) for i in range(segs)]

def rounded_rect_poly(x0, y0, x1, y1, r, segs=8):
    pts = []
    corners = [
        (x0 + r, y0 + r, np.pi,       1.5 * np.pi),
        (x1 - r, y0 + r, 1.5 * np.pi, 2 * np.pi),
        (x1 - r, y1 - r, 0,           0.5 * np.pi),
        (x0 + r, y1 - r, 0.5 * np.pi, np.pi),
    ]
    for cx, cy, a0, a1 in corners:
        for s in range(segs + 1):
            a = a0 + (a1 - a0) * s / segs
            pts.append((cx + r * np.cos(a), cy + r * np.sin(a)))
    return pts

# ─────────────────────────────────────────────────────────────────────────────
# Computed dimensions
# ─────────────────────────────────────────────────────────────────────────────

OW = PHONE_WIDTH     + 2 * (WALL_THICKNESS + TOLERANCE)
OH = PHONE_HEIGHT    + 2 * (WALL_THICKNESS + TOLERANCE)
OT = PHONE_THICKNESS + TOLERANCE + BACK_WALL

cav_x0, cav_x1 = WALL_THICKNESS, OW - WALL_THICKNESS
cav_y0, cav_y1 = WALL_THICKNESS, OH - WALL_THICKNESS
cav_z0, cav_z1 = BACK_WALL, OT

lip_x0, lip_x1 = WALL_THICKNESS, OW - WALL_THICKNESS
lip_y0, lip_y1 = WALL_THICKNESS, OH - WALL_THICKNESS
open_x0 = WALL_THICKNESS + LIP_DEPTH
open_x1 = OW - WALL_THICKNESS - LIP_DEPTH
open_y0 = WALL_THICKNESS + LIP_DEPTH
open_y1 = OH - WALL_THICKNESS - LIP_DEPTH

cx_case = OW / 2
grip_z0 = (OT - GRIP_THICKNESS) / 2
grip_z1 = grip_z0 + GRIP_THICKNESS

# ─────────────────────────────────────────────────────────────────────────────
# Build geometry
# ─────────────────────────────────────────────────────────────────────────────

def build():
    # Outer shell
    extrude_polygon(rect_poly(0, 0, OW, OH), 0, OT, cap_bottom=True, cap_top=False)

    # Front lip ring
    z = OT
    add_quad([lip_x0, lip_y0, z], [lip_x1, lip_y0, z], [lip_x1, open_y0, z], [lip_x0, open_y0, z])
    add_quad([lip_x0, open_y1, z], [lip_x1, open_y1, z], [lip_x1, lip_y1, z], [lip_x0, lip_y1, z])
    add_quad([lip_x0, open_y0, z], [lip_x0, open_y1, z], [open_x0, open_y1, z], [open_x0, open_y0, z])
    add_quad([open_x1, open_y0, z], [open_x1, open_y1, z], [lip_x1, open_y1, z], [lip_x1, open_y0, z])

    # Inner cavity (inward-facing walls)
    extrude_polygon(rect_poly(cav_x0, cav_y0, cav_x1, cav_y1),
                    cav_z0, cav_z1, cap_bottom=True, cap_top=False, flip_winding=True)

    # Ventilation perforations
    x = cav_x0 + PERF_SPACING / 2
    while x <= cav_x1 - PERF_SPACING / 2:
        y = cav_y0 + PERF_SPACING / 2
        while y <= cav_y1 - PERF_SPACING / 2:
            cpts = circle_poly(x, y, PERF_RADIUS)
            segs = PERF_SEGMENTS
            extrude_polygon(cpts, 0, BACK_WALL, cap_bottom=False, cap_top=False, flip_winding=True)
            for i in range(1, segs - 1):
                add_tri([cpts[0][0], cpts[0][1], 0],
                        [cpts[i+1][0], cpts[i+1][1], 0],
                        [cpts[i][0], cpts[i][1], 0])
                add_tri([cpts[0][0], cpts[0][1], BACK_WALL],
                        [cpts[i][0], cpts[i][1], BACK_WALL],
                        [cpts[i+1][0], cpts[i+1][1], BACK_WALL])
            y += PERF_SPACING
        x += PERF_SPACING

    # Neck
    neck_x0 = cx_case - NECK_WIDTH / 2
    neck_x1 = cx_case + NECK_WIDTH / 2
    extrude_polygon(rect_poly(neck_x0, -NECK_HEIGHT, neck_x1, 0), grip_z0, grip_z1,
                    cap_bottom=True, cap_top=True)

    # Grip
    grip_x0 = cx_case - GRIP_WIDTH / 2
    grip_x1 = cx_case + GRIP_WIDTH / 2
    grip_pts = rounded_rect_poly(grip_x0, -NECK_HEIGHT - GRIP_HEIGHT, grip_x1, -NECK_HEIGHT,
                                  r=GRIP_RADIUS, segs=6)
    extrude_polygon(grip_pts, grip_z0, grip_z1, cap_bottom=True, cap_top=True)

# ─────────────────────────────────────────────────────────────────────────────
# Write binary STL
# ─────────────────────────────────────────────────────────────────────────────

def write_stl(path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    header = b"Pixel 10a Phone Holder - Snorlax 3D Printing" + b" " * (80 - 45)
    with open(path, 'wb') as f:
        f.write(header[:80])
        f.write(struct.pack('<I', len(triangles)))
        for (n, v0, v1, v2) in triangles:
            f.write(struct.pack('<fff', *n))
            f.write(struct.pack('<fff', *v0))
            f.write(struct.pack('<fff', *v1))
            f.write(struct.pack('<fff', *v2))
            f.write(struct.pack('<H', 0))

if __name__ == '__main__':
    print("Building geometry...")
    build()
    print(f"Writing {len(triangles):,} triangles → {OUTPUT_PATH}")
    write_stl(OUTPUT_PATH)
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"\n✓ Done! ({size_kb:.1f} KB)")
    print(f"  Case outer:  {OW:.1f} × {OH:.1f} × {OT:.1f} mm")
    print(f"  Grip:        {GRIP_WIDTH:.0f} × {GRIP_HEIGHT:.0f} × {GRIP_THICKNESS:.0f} mm")
