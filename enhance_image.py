#!/usr/bin/env python3
"""
Boosts color vibrancy/pop on an image without blowing out already-saturated
areas (like neon glow). Usage:
    python3 enhance_image.py input.jpg output.jpg
"""
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter


def vibrance_boost(img, amount=0.55):
    """Smart saturation boost: pushes low-saturation pixels harder than
    already-vivid ones, so neon colors glow without clipping into flat blobs."""
    hsv = np.array(img.convert("HSV"), dtype=np.float32)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    # weight is higher for low-saturation pixels, tapers off near max sat
    weight = 1.0 - (s / 255.0)
    s_new = s + (255.0 - s) * amount * weight * 0.6 + (s * amount * 0.15)
    s_new = np.clip(s_new, 0, 255)
    hsv[..., 1] = s_new
    out = Image.fromarray(hsv.astype(np.uint8), "HSV").convert("RGB")
    return out


def enhance(path_in, path_out):
    img = Image.open(path_in).convert("RGB")

    # 1. Pure saturation lift — only pushes pixels that already have color;
    #    true neutral grays/blacks/whites stay clean (no tint introduced).
    img = ImageEnhance.Color(img).enhance(1.45)

    # 2. Gentle contrast lift for more "pop"
    img = ImageEnhance.Contrast(img).enhance(1.14)

    # 3. Slight brightness lift so neon/glow areas read brighter
    img = ImageEnhance.Brightness(img).enhance(1.05)

    # 4. Subtle sharpen so linework/edges stay crisp after the above
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=50, threshold=3))

    img.save(path_out, quality=95)
    print(f"Saved enhanced image -> {path_out}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 enhance_image.py input output")
        sys.exit(1)
    enhance(sys.argv[1], sys.argv[2])
