#!/usr/bin/env python3
"""
Batch-processes tattoo portfolio photos:
  1. Vibrancy/contrast/sharpen boost (same recipe as enhance_image.py)
  2. Downscale if oversized (keeps file sizes web-friendly)
  3. Stamps a small semi-transparent "TRIPPY TATTOOZ" watermark, bottom-right
Usage: python3 process_portfolio.py
Edit the SOURCES list below to point at input files -> output names.
"""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np
import os

LOGO_PATH = "images/logo.jpg"
MAX_DIM = 1600


def enhance(img):
    img = ImageEnhance.Color(img).enhance(1.4)
    img = ImageEnhance.Contrast(img).enhance(1.12)
    img = ImageEnhance.Brightness(img).enhance(1.03)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=45, threshold=3))
    return img


def resize_if_needed(img, max_dim=MAX_DIM):
    w, h = img.size
    if max(w, h) <= max_dim:
        return img
    scale = max_dim / max(w, h)
    return img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)


def make_logo_stamp(logo_path, target_width, opacity=0.92):
    """Turns the logo into a glow-only stamp: its black background becomes
    transparent (based on brightness), so only the neon pink/white artwork
    shows — no black box sitting on top of the photo."""
    logo = Image.open(logo_path).convert("RGB")
    scale = target_width / logo.width
    logo = logo.resize((target_width, int(logo.height * scale)), Image.LANCZOS)

    arr = np.array(logo).astype(np.float32)
    brightness = arr.max(axis=2)  # near-black bg -> low, neon/white artwork -> high
    alpha = np.clip((brightness - 18) / (255 - 18), 0, 1) ** 0.85
    alpha = (alpha * 255 * opacity).astype(np.uint8)

    rgba = np.dstack([arr.astype(np.uint8), alpha])
    return Image.fromarray(rgba, mode="RGBA")


def add_watermark(img):
    img = img.convert("RGBA")
    w, h = img.size
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))

    stamp_w = max(90, int(w * 0.16))
    stamp = make_logo_stamp(LOGO_PATH, stamp_w)

    margin = int(w * 0.025)
    pos = (w - margin - stamp.width, h - margin - stamp.height)

    # soft dark backing glow behind the logo so it stays legible on bright photos
    pad = int(stamp_w * 0.12)
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle(
        [pos[0] - pad, pos[1] - pad, pos[0] + stamp.width + pad, pos[1] + stamp.height + pad],
        radius=pad * 1.4, fill=(10, 9, 11, 110)
    )
    overlay.paste(stamp, pos, stamp)

    out = Image.alpha_composite(img, overlay).convert("RGB")
    return out


def process(src_path, out_path):
    img = Image.open(src_path).convert("RGB")
    img = enhance(img)
    img = resize_if_needed(img)
    img = add_watermark(img)
    img.save(out_path, quality=90)
    print(f"{os.path.basename(src_path)} -> {out_path}")


if __name__ == "__main__":
    UPLOAD_DIR = "/mnt/user-data/uploads"
    OUT_DIR = "/home/claude/trippy-tattooz-site/images"
    os.makedirs(OUT_DIR, exist_ok=True)

    SOURCES = [
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__6_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__5_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__4_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__3_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__2_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM__1_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_54_PM.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM__5_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM__4_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM__3_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM__2_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM__1_.jpeg",
        "WhatsApp_Image_2026-07-16_at_10_55_53_PM.jpeg",
    ]

    for i, fname in enumerate(SOURCES, start=1):
        src = os.path.join(UPLOAD_DIR, fname)
        out = os.path.join(OUT_DIR, f"portfolio-{i}.jpg")
        process(src, out)
