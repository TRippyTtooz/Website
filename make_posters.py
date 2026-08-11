#!/usr/bin/env python3
"""Generates branded promotional posters for Trippy Tattooz."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

W, H = 1080, 1350  # Instagram portrait / A4-ish flyer ratio

INK = (11, 11, 13)
BONE = (239, 231, 216)
NEON = (255, 46, 166)
DEEP_PINK = (200, 30, 111)

POPPINS_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
POPPINS_MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

IMG_DIR = "images"
OUT_DIR = "posters"
os.makedirs(OUT_DIR, exist_ok=True)


def font(path, size):
    return ImageFont.truetype(path, size)


def bg_from_photo(photo_path, darken=0.30, blur=2):
    """Cover-crop a studio/portfolio photo to poster size, darken + blur it
    so it reads as atmospheric texture behind bold text."""
    img = Image.open(photo_path).convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = W / H
    if img_ratio > target_ratio:
        new_h = H
        new_w = int(H * img_ratio)
    else:
        new_w = W
        new_h = int(W / img_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - W) // 2
    top = (new_h - H) // 2
    img = img.crop((left, top, left + W, top + H))
    img = img.filter(ImageFilter.GaussianBlur(blur))
    img = ImageEnhance.Brightness(img).enhance(darken)
    img = ImageEnhance.Color(img).enhance(1.3)
    return img


def add_vignette_and_border(img):
    # Uniform dark veil so the photo reads as atmospheric texture, not a
    # blown-out background — plus extra darkening at top/bottom for text.
    black = Image.new("RGB", (W, H), INK)
    img = Image.blend(img, black, 0.35)

    grad = Image.new("L", (1, H), 0)
    for y in range(H):
        d_top = max(0, 1 - y / (H * 0.30))
        d_bot = max(0, 1 - (H - y) / (H * 0.40))
        val = int(255 * max(d_top, d_bot) * 0.75)
        grad.putpixel((0, y), val)
    grad = grad.resize((W, H))
    img = Image.composite(black, img, grad)

    draw = ImageDraw.Draw(img)
    m = 28
    draw.rectangle([m, m, W - m, H - m], outline=BONE, width=2)
    return img


def paste_logo(img, logo_path, size=110, pos="bottom-right", margin=46):
    if not os.path.exists(logo_path):
        return img
    logo = Image.open(logo_path).convert("RGBA")
    logo.thumbnail((size, size), Image.LANCZOS)
    if pos == "bottom-right":
        xy = (W - margin - logo.width, H - margin - logo.height)
    elif pos == "top-left":
        xy = (margin, margin)
    else:
        xy = (margin, margin)
    img = img.convert("RGBA")
    img.paste(logo, xy, logo)
    return img.convert("RGB")


def center_text(draw, text, y, f, fill, tracking=0, max_width=None):
    if tracking:
        text = (" " * 0).join(list(text))
    w = draw.textlength(text, font=f)
    draw.text(((W - w) / 2, y), text, font=f, fill=fill)
    return w


def poster_flash_day(date_str="THIS SATURDAY", slots="10 SLOTS ONLY"):
    img = bg_from_photo(f"{IMG_DIR}/portfolio-9.jpg", darken=0.35, blur=3)
    img = add_vignette_and_border(img)
    draw = ImageDraw.Draw(img)

    center_text(draw, "TRIPPY TATTOOZ", 130, font(MONO_BOLD, 26), NEON)
    center_text(draw, "FLASH DAY", 200, font(POPPINS_BOLD, 108), BONE)

    draw.rectangle([W/2 - 160, 340, W/2 + 160, 344], fill=NEON)

    center_text(draw, date_str, 380, font(POPPINS_MED, 40), BONE)
    center_text(draw, slots, 440, font(MONO_BOLD, 28), NEON)

    # bottom CTA block
    cta_y = H - 230
    draw.rounded_rectangle([90, cta_y, W - 90, cta_y + 110], radius=8, fill=NEON)
    d2 = ImageDraw.Draw(img)
    cta_text = "BOOK ON WHATSAPP"
    f_cta = font(POPPINS_BOLD, 34)
    w = d2.textlength(cta_text, font=f_cta)
    d2.text(((W - w) / 2, cta_y + 30), cta_text, font=f_cta, fill=INK)

    phone_text = "+91 91454 56658"
    f_phone = font(MONO_BOLD, 24)
    w2 = draw.textlength(phone_text, font=f_phone)
    draw.text(((W - w2) / 2, cta_y + 130), phone_text, font=f_phone, fill=BONE)

    img = paste_logo(img, f"{IMG_DIR}/logo.jpg", size=90, pos="top-left")
    img.save(f"{OUT_DIR}/poster-flash-day.jpg", quality=92)
    print("saved poster-flash-day.jpg")


def poster_walkins():
    img = bg_from_photo(f"{IMG_DIR}/studio-2.jpg", darken=0.32, blur=3)
    img = add_vignette_and_border(img)
    draw = ImageDraw.Draw(img)

    center_text(draw, "TRIPPY TATTOOZ · VIRAR", 130, font(MONO_BOLD, 24), NEON)
    center_text(draw, "WALK-INS", 210, font(POPPINS_BOLD, 92), BONE)
    center_text(draw, "WELCOME", 310, font(POPPINS_BOLD, 92), NEON)

    draw.rectangle([W/2 - 160, 430, W/2 + 160, 434], fill=BONE)
    center_text(draw, "Mon – Sun · 11 AM – 8 PM", 470, font(POPPINS_MED, 34), BONE)

    cta_y = H - 230
    draw.rounded_rectangle([90, cta_y, W - 90, cta_y + 110], radius=8, fill=NEON)
    cta_text = "COME SAY HI TODAY"
    f_cta = font(POPPINS_BOLD, 32)
    w = draw.textlength(cta_text, font=f_cta)
    draw.text(((W - w) / 2, cta_y + 30), cta_text, font=f_cta, fill=INK)

    phone_text = "+91 91454 56658"
    f_phone = font(MONO_BOLD, 24)
    w2 = draw.textlength(phone_text, font=f_phone)
    draw.text(((W - w2) / 2, cta_y + 130), phone_text, font=f_phone, fill=BONE)

    img = paste_logo(img, f"{IMG_DIR}/logo.jpg", size=90, pos="top-left")
    img.save(f"{OUT_DIR}/poster-walkins.jpg", quality=92)
    print("saved poster-walkins.jpg")


def poster_referral():
    img = bg_from_photo(f"{IMG_DIR}/portfolio-4.jpg", darken=0.30, blur=3)
    img = add_vignette_and_border(img)
    draw = ImageDraw.Draw(img)

    center_text(draw, "TRIPPY TATTOOZ", 130, font(MONO_BOLD, 26), NEON)
    center_text(draw, "BRING A", 205, font(POPPINS_BOLD, 90), BONE)
    center_text(draw, "FRIEND", 305, font(POPPINS_BOLD, 90), NEON)

    draw.rectangle([W/2 - 160, 425, W/2 + 160, 429], fill=BONE)
    center_text(draw, "You both get 10% off", 465, font(POPPINS_MED, 38), BONE)

    cta_y = H - 230
    draw.rounded_rectangle([90, cta_y, W - 90, cta_y + 110], radius=8, fill=NEON)
    cta_text = "BOOK ON WHATSAPP"
    f_cta = font(POPPINS_BOLD, 34)
    w = draw.textlength(cta_text, font=f_cta)
    draw.text(((W - w) / 2, cta_y + 30), cta_text, font=f_cta, fill=INK)

    phone_text = "+91 91454 56658"
    f_phone = font(MONO_BOLD, 24)
    w2 = draw.textlength(phone_text, font=f_phone)
    draw.text(((W - w2) / 2, cta_y + 130), phone_text, font=f_phone, fill=BONE)

    img = paste_logo(img, f"{IMG_DIR}/logo.jpg", size=90, pos="top-left")
    img.save(f"{OUT_DIR}/poster-referral.jpg", quality=92)
    print("saved poster-referral.jpg")


if __name__ == "__main__":
    poster_flash_day()
    poster_walkins()
    poster_referral()
