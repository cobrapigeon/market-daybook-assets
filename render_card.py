#!/usr/bin/env python3
"""Market Daybook — branded headline card renderer.

Renders a "bland" brand-colored background with a headline set in Sora.
Reusable by the daily social engine.

CLI:
  python3 render_card.py --headline "Your hook here" \
      --size portrait --style dark --out generated/2026-07-14_ig.png

Library:
  from render_card import render_card
  render_card("hook", size="portrait", style="dark", out="card.png")

Sizes:  square (1080x1080) · portrait (1080x1350) · story (1080x1920)
Styles: dark (Graphite bg) · light (Ledger Bone bg)
Font:   fonts/Sora[wght].ttf  (vendored in this repo so headless runs need no download)
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont

# ---- Brand palette (Market Daybook brand system) ----
GRAPHITE = (25, 27, 32)     # #191B20
RED      = (227, 75, 62)    # #E34B3E  Recovery Red
BONE     = (241, 237, 227)  # #F1EDE3  Ledger Bone

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "Sora[wght].ttf")

SIZES = {"square": (1080, 1080), "portrait": (1080, 1350), "story": (1080, 1920)}
STYLES = {
    "dark":  {"bg": GRAPHITE, "ink": BONE,     "accent": RED, "sub": (150, 150, 158)},
    "light": {"bg": BONE,     "ink": GRAPHITE, "accent": RED, "sub": (120, 118, 110)},
}

def _font(px, weight):
    f = ImageFont.truetype(FONT, px)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f

def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def render_card(headline, size="portrait", style="dark", out="out.png"):
    W, H = SIZES[size]
    s = STYLES[style]
    img = Image.new("RGB", (W, H), s["bg"])
    d = ImageDraw.Draw(img)

    M = int(W * 0.093)  # ~100px margin
    # top accent rule
    d.rectangle([M, int(H * 0.115), M + int(W * 0.14), int(H * 0.115) + 8], fill=s["accent"])

    # headline auto-fit
    box_w = W - 2 * M
    px = int(W * 0.082)
    lines, line_h, hf = [headline], 0, None
    while px > 38:
        hf = _font(px, 700)
        lines = _wrap(d, headline, hf, box_w)
        line_h = int(px * 1.16)
        if line_h * len(lines) <= int(H * 0.52) and len(lines) <= 7:
            break
        px -= 3
    y = int(H * 0.185)
    for ln in lines:
        d.text((M, y), ln, font=hf, fill=s["ink"])
        y += line_h

    # footer: mark + wordmark + tagline
    wm = _font(int(W * 0.030), 700)
    tag = _font(int(W * 0.020), 600)
    fy = int(H * (0.905 if size != "story" else 0.93))
    ms = int(W * 0.030)
    d.rectangle([M, fy, M + ms, fy + ms], fill=s["accent"])
    d.text((M + ms + 18, fy - 2), "MARKET DAYBOOK", font=wm, fill=s["ink"])
    d.text((M + ms + 18, fy + int(ms * 0.9)), "PLAN · RECORD · REVIEW", font=tag, fill=s["sub"])

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.save(out)
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--headline", required=True)
    ap.add_argument("--size", default="portrait", choices=list(SIZES))
    ap.add_argument("--style", default="dark", choices=list(STYLES))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    print(render_card(a.headline, a.size, a.style, a.out))
