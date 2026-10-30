#!/usr/bin/env python3
"""Parametric flag SVG generator. PROTOTYPE.

Proportions, colours, ray count and sun size come from kurdistanflag.com (not an official
text). Ray base width and angles are placeholders. Do not publish output as the official
flag until checked against the enacted legislation.

Usage: python make_flag_svg.py out.svg
"""
import math
import sys

SPEC = {
    # Proportions: height:length 2:3 (kurdistanflag.com), so width = 1.5 * height.
    "width": 900,
    "height": 600,
    # Colours: 1998-1999 specification hex (Pantone 032C, 355C, 116C) per kurdistanflag.com.
    # White is not given a Pantone number in the source. Web set is in WEB_COLOURS below.
    "stripes": ["#F32837", "#FFFFFF", "#009A3D"],   # red, white, green
    "sun_color": "#FFCC00",                          # Pantone 116C
    # Sun: 21 equal rays, one pointing straight up (kurdistanflag.com).
    "rays": 21,
    # Sun size: full diameter incl. rays = height/2 -> tip radius = 0.25 * height.
    # Disc diameter = height/4 -> disc radius = 0.125 * height.
    "disc_ratio": 0.125,
    "tip_ratio": 0.25,
    # Ray base width and angles are NOT given by any source checked. PLACEHOLDER.
    "base_fill": 0.55,
}

WEB_COLOURS = {"red": "#ED2024", "white": "#FFFFFF", "green": "#278E43", "gold": "#FEBD11"}


def build_svg(spec=SPEC):
    w, h = spec["width"], spec["height"]
    cx, cy = w / 2, h / 2
    band = h / 3
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">']
    for i, color in enumerate(spec["stripes"]):
        out.append(f'<rect x="0" y="{i * band:.3f}" width="{w}" height="{band:.3f}" fill="{color}"/>')
    r_disc = spec["disc_ratio"] * h
    r_tip = spec["tip_ratio"] * h
    n = spec["rays"]
    pitch = 2 * math.pi / n
    half = spec["base_fill"] * pitch / 2
    sun = spec["sun_color"]

    def pt(r, t):
        return f"{cx + r * math.cos(t):.3f},{cy + r * math.sin(t):.3f}"

    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r_disc:.3f}" fill="{sun}"/>')
    for k in range(n):
        a = -math.pi / 2 + k * pitch  # ray 0 points straight up
        d = f"M{pt(r_disc * 0.9, a - half)} L{pt(r_tip, a)} L{pt(r_disc * 0.9, a + half)} Z"
        out.append(f'<path d="{d}" fill="{sun}"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: make_flag_svg.py out.svg")
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        f.write(build_svg())
    print(f"Wrote {sys.argv[1]} (PLACEHOLDER geometry)")
