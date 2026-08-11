#!/usr/bin/env python3
"""Generates the multi-page version of the Trippy Tattooz site.
Each page shares the same nav/drawer/footer/floating elements, defined once
below, so editing the header/footer means editing this file, not 10 HTML files.
"""
import os

OUT = "/home/claude/trippy-tattooz-site"

NAV_LINKS = [
    ("index.html", "Home"),
    ("studio.html", "Studio"),
    ("work.html", "Work"),
    ("menu.html", "Menu"),
    ("about.html", "About"),
    ("faq.html", "FAQ"),
    ("aftercare.html", "Aftercare"),
    ("reviews.html", "Reviews"),
    ("instagram.html", "Instagram"),
    ("contact.html", "Contact"),
]

WHATSAPP_SVG = '<svg viewBox="0 0 24 24" fill="#0b0b0d"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.7.44 3.36 1.28 4.82L2.05 22l5.4-1.42a9.9 9.9 0 0 0 4.59 1.17h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm0 18.13h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.36c0-4.54 3.7-8.24 8.26-8.24 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.55-3.7 8.24-8.25 8.24zm4.52-6.16c-.25-.12-1.47-.72-1.7-.81-.23-.08-.4-.12-.56.13-.17.25-.65.81-.8.97-.14.17-.29.19-.54.06-.25-.12-1.04-.38-1.98-1.22-.73-.65-1.23-1.46-1.37-1.71-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.44.12-.14.16-.25.25-.41.08-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.08 0 1.23.89 2.41 1.02 2.58.12.17 1.75 2.67 4.24 3.74.59.26 1.06.41 1.42.52.6.19 1.14.16 1.57.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.15-1.18-.06-.1-.23-.16-.48-.28z"/></svg>'

WA_LINK = "https://wa.me/919145456658?text=Hi!%20I%27d%20like%20to%20book%20a%20tattoo%20appointment"


def nav_html(current):
    items = ""
    drawer_items = ""
    for href, label in NAV_LINKS:
        active = ' style="color:var(--green);"' if href == current else ""
        items += f'    <li><a href="{href}"{active}>{label}</a></li>\n'
        drawer_items += f'    <li><a href="{href}"{active}>{label}</a></li>\n'
    return f"""<nav class="nav">
  <a href="index.html" class="brand"><img src="images/logo.jpg" alt="Trippy Tattooz" class="nav-logo-img" onerror="window.__ph && window.__ph(this,'images/logo.jpg — your logo')"></a>
  <ul>
{items}  </ul>
  <a class="nav-cta" href="contact.html">Book Now</a>
  <button class="nav-menu-btn" id="navMenuBtn" aria-label="Open menu">☰</button>
</nav>

<div class="nav-drawer-overlay" id="navDrawerOverlay"></div>
<div class="nav-drawer" id="navDrawer">
  <div class="nav-drawer-head">
    <img src="images/logo.jpg" alt="Trippy Tattooz" class="nav-logo-img" onerror="this.style.display='none'">
    <button class="nav-drawer-close" id="navDrawerClose" aria-label="Close menu">✕</button>
  </div>
  <ul>
{drawer_items}  </ul>
  <a href="contact.html" class="nav-drawer-cta">Book Now</a>
</div>"""


FOOTER_HTML = f"""<footer>
  <div class="wrap">
    <div class="brand">TRIPPY<span>·</span>TATTOOZ</div>
    <p class="mono">VIRAR, MUMBAI — © <span id="year"></span> — BOOK ON WHATSAPP OR INSTAGRAM</p>
  </div>
</footer>

<a class="whatsapp-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Message on WhatsApp">
  {WHATSAPP_SVG}
</a>

<div class="mobile-book-bar">
  <a href="{WA_LINK}" target="_blank" rel="noopener">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="#0b0b0d"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.7.44 3.36 1.28 4.82L2.05 22l5.4-1.42a9.9 9.9 0 0 0 4.59 1.17h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm0 18.13h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.36c0-4.54 3.7-8.24 8.26-8.24 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.55-3.7 8.24-8.25 8.24zm4.52-6.16c-.25-.12-1.47-.72-1.7-.81-.23-.08-.4-.12-.56.13-.17.25-.65.81-.8.97-.14.17-.29.19-.54.06-.25-.12-1.04-.38-1.98-1.22-.73-.65-1.23-1.46-1.37-1.71-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.44.12-.14.16-.25.25-.41.08-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.08 0 1.23.89 2.41 1.02 2.58.12.17 1.75 2.67 4.24 3.74.59.26 1.06.41 1.42.52.6.19 1.14.16 1.57.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.15-1.18-.06-.1-.23-.16-.48-.28z"/></svg>
    Book on WhatsApp
  </a>
</div>"""


HEAD_COMMON = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Trippy Tattooz">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://trippytattooz.online/images/portfolio-11.jpg">
<meta property="og:url" content="https://trippytattooz.online/{page}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://trippytattooz.online/images/portfolio-11.jpg">

<link rel="icon" type="image/jpeg" href="images/logo.jpg">
<link rel="apple-touch-icon" href="images/logo.jpg">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "TattooParlor",
  "name": "Trippy Tattooz",
  "image": "https://trippytattooz.online/images/logo.jpg",
  "url": "https://trippytattooz.online/",
  "telephone": "+919145456658",
  "priceRange": "₹₹",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Virar",
    "addressRegion": "Maharashtra",
    "addressCountry": "IN"
  }},
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "11:00",
    "closes": "20:00"
  }},
  "sameAs": ["https://instagram.com/trippy_tattooz"]
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rye&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
"""


def page(filename, title, description, body, extra_scripts=None, include_lightbox=False):
    extra_scripts = extra_scripts or []
    scripts_html = "\n".join(f'<script src="{s}"></script>' for s in extra_scripts)
    lightbox_html = ""
    if include_lightbox:
        lightbox_html = """
<div class="lightbox" id="lightbox">
  <button class="lightbox-close" id="lightboxClose" aria-label="Close">✕</button>
  <button class="lightbox-nav lightbox-prev" id="lightboxPrev" aria-label="Previous">‹</button>
  <img class="lightbox-img" id="lightboxImg" src="" alt="">
  <button class="lightbox-nav lightbox-next" id="lightboxNext" aria-label="Next">›</button>
  <div class="lightbox-caption mono" id="lightboxCaption"></div>
</div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON.format(title=title, description=description, page=filename)}
</head>
<body>

{nav_html(filename)}
{lightbox_html}

{body}

{FOOTER_HTML}

<script src="script.js"></script>
{scripts_html}
</body>
</html>
"""
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print(f"wrote {filename}")


# ================= HOME =================
home_body = """<section class="hero" id="top">
  <div class="hero-bg-logo">
    <img src="images/logo.jpg" alt="" aria-hidden="true" onerror="this.parentElement.style.display='none'">
  </div>

  <div class="hero-eyebrow mono">Virar · Mumbai</div>

  <h1 class="hero-wordmark">TRIPPY <span>TATTOOZ</span></h1>

  <p class="hero-tag">Custom ink, cover-ups & fine line — hand-drawn for you, tattooed in Virar.
  <strong>3 years, one needle, no shortcuts.</strong></p>

  <div class="hero-ctas">
    <a href="contact.html" class="btn btn-primary">Book an appointment</a>
    <a href="work.html" class="btn btn-ghost">See the work</a>
  </div>

  <div class="hero-scroll"><span>Scroll</span><span class="line"></span></div>
</section>

<section class="section" id="explore">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Find your way around</div>
        <h2 class="section-title">Explore the studio</h2>
      </div>
    </div>
    <div class="explore-grid">
      <a href="studio.html" class="explore-card">
        <span class="explore-num mono">01</span>
        <h3>The Studio</h3>
        <p>Take a look inside — neon-lit, mural-walled, built for comfort.</p>
      </a>
      <a href="work.html" class="explore-card">
        <span class="explore-num mono">02</span>
        <h3>Recent Work</h3>
        <p>13 pieces from the last few months — click any photo to zoom.</p>
      </a>
      <a href="menu.html" class="explore-card">
        <span class="explore-num mono">03</span>
        <h3>The Flash Menu</h3>
        <p>Starting prices for fine line, traditional, custom & cover-ups.</p>
      </a>
      <a href="about.html" class="explore-card">
        <span class="explore-num mono">04</span>
        <h3>About Us</h3>
        <p>Three years in Virar, one honest tattoo at a time.</p>
      </a>
      <a href="faq.html" class="explore-card">
        <span class="explore-num mono">05</span>
        <h3>FAQ</h3>
        <p>Walk-ins, deposits, pain, touch-ups — answered.</p>
      </a>
      <a href="aftercare.html" class="explore-card">
        <span class="explore-num mono">06</span>
        <h3>Aftercare</h3>
        <p>Healing instructions to keep on hand after your session.</p>
      </a>
      <a href="reviews.html" class="explore-card">
        <span class="explore-num mono">07</span>
        <h3>Reviews</h3>
        <p>What clients say about getting tattooed here.</p>
      </a>
      <a href="contact.html" class="explore-card">
        <span class="explore-num mono">08</span>
        <h3>Book Now</h3>
        <p>WhatsApp, map, and a form that sends straight to us.</p>
      </a>
    </div>
  </div>
</section>"""

page(
    "index.html",
    "Trippy Tattooz — Virar, Mumbai",
    "Trippy Tattooz, Virar — custom tattoos, cover-ups, fine line & traditional work. 3 years in the craft. Book on WhatsApp.",
    home_body,
)

# ================= STUDIO =================
studio_body = """<section class="section" id="studio">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Step inside</div>
        <h2 class="section-title">The studio</h2>
      </div>
      <p class="section-sub">Neon-lit, mural-walled, and set up to make first-timers comfortable — this is where the work happens.</p>
    </div>
    <div class="studio-gallery">
      <div class="studio-img">
        <img src="images/studio-1.jpg" alt="Trippy Tattooz studio interior with neon lighting" loading="lazy">
      </div>
      <div class="studio-img">
        <img src="images/studio-2.jpg" alt="Trippy Tattooz studio interior with mural wall" loading="lazy">
      </div>
    </div>
  </div>
</section>"""

page(
    "studio.html",
    "The Studio — Trippy Tattooz",
    "Take a look inside Trippy Tattooz — our neon-lit, mural-walled studio in Virar, Mumbai.",
    studio_body,
)

# ================= WORK =================
work_body = """<section class="section" id="work">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Flash sheet</div>
        <h2 class="section-title">Recent work</h2>
      </div>
      <p class="section-sub">A working wall of what's come through the studio lately. Click any photo to zoom.</p>
    </div>

    <div class="flash-grid" id="flashGrid">
      <!-- Flash cards generated by work.js, edit the PORTFOLIO array there to change captions -->
    </div>
  </div>
</section>"""

page(
    "work.html",
    "Recent Work — Trippy Tattooz",
    "Browse recent tattoo work from Trippy Tattooz, Virar — fine line, traditional, realism, blackwork & more.",
    work_body,
    extra_scripts=["work.js"],
    include_lightbox=True,
)

# ================= MENU =================
menu_body = """<section class="section" id="menu">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Price of admission</div>
        <h2 class="section-title">The flash menu</h2>
      </div>
      <p class="section-sub">Starting prices — final quote depends on size, placement & detail. Ask on WhatsApp for an exact number.</p>
    </div>

    <div class="menu-board">
      <div class="menu-row">
        <div class="menu-left">
          <span class="menu-index mono">01</span>
          <div>
            <div class="menu-name">Fine line & minimal</div>
            <div class="menu-desc">Small symbols, script, single-needle detail</div>
          </div>
        </div>
        <div class="menu-price mono">From ₹1,500</div>
      </div>
      <div class="menu-row">
        <div class="menu-left">
          <span class="menu-index mono">02</span>
          <div>
            <div class="menu-name">Traditional / old school</div>
            <div class="menu-desc">Bold linework, flash-style colour pieces</div>
          </div>
        </div>
        <div class="menu-price mono">From ₹3,000</div>
      </div>
      <div class="menu-row">
        <div class="menu-left">
          <span class="menu-index mono">03</span>
          <div>
            <div class="menu-name">Custom design</div>
            <div class="menu-desc">Your idea, sketched & tattooed to fit</div>
          </div>
        </div>
        <div class="menu-price mono">Quoted per piece</div>
      </div>
      <div class="menu-row">
        <div class="menu-left">
          <span class="menu-index mono">04</span>
          <div>
            <div class="menu-name">Cover-up / rework</div>
            <div class="menu-desc">Turning old tattoos into something you'll actually wear</div>
          </div>
        </div>
        <div class="menu-price mono">Quoted per piece</div>
      </div>
      <div class="menu-row">
        <div class="menu-left">
          <span class="menu-index mono">05</span>
          <div>
            <div class="menu-name">Flash Tattoo Day</div>
            <div class="menu-desc">Pre-drawn designs, fixed price, limited slots — check Instagram for the next date</div>
          </div>
        </div>
        <div class="menu-price mono">Fixed rate</div>
      </div>
    </div>
  </div>
</section>"""

page(
    "menu.html",
    "Flash Menu & Pricing — Trippy Tattooz",
    "Starting prices for tattoos at Trippy Tattooz, Virar — fine line, traditional, custom design, cover-ups & more.",
    menu_body,
)

# ================= ABOUT =================
about_body = """<section class="section" id="about">
  <div class="wrap about-grid">
    <div class="about-photo">
      <img src="images/artist-portrait.jpg" alt="Orpheus Gonsalves, artist at Trippy Tattooz"
           onerror="window.__ph && window.__ph(this,'images/artist-portrait.jpg — artist portrait, 4:5')">
      <div class="about-ribbon mono">Est. Virar</div>
      <div class="about-name">
        <span class="about-name-main">Orpheus Gonsalves</span>
        <span class="about-name-sub mono">Founder & Tattoo Artist</span>
      </div>
    </div>
    <div class="about-body">
      <div class="section-eyebrow">About us</div>
      <h2 class="section-title" style="margin-bottom:22px;">Three years deep in the craft</h2>
      <p>Trippy Tattooz has been putting ink to skin in Virar for the last three years — built one honest tattoo at a time, mostly through word of mouth from clients who came back for a second, third, fifth piece.</p>
      <p>Every design starts as a conversation. Whether it's a small fine-line piece or a full cover-up, the work is planned, sketched and sized specifically for your skin — not pulled off a wall.</p>
      <div class="stat-row">
        <div class="stat"><div class="stat-num mono">3+</div><div class="stat-label">Years tattooing</div></div>
        <div class="stat"><div class="stat-num mono">100%</div><div class="stat-label">Hygiene-first setup</div></div>
        <div class="stat"><div class="stat-num mono">1:1</div><div class="stat-label">Custom design sessions</div></div>
      </div>
    </div>
  </div>
</section>"""

page(
    "about.html",
    "About Us — Trippy Tattooz",
    "Meet Orpheus Gonsalves, founder and tattoo artist at Trippy Tattooz, Virar — 3 years deep in the craft.",
    about_body,
)

# ================= FAQ =================
faq_body = """<section class="section" id="faq">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Before you book</div>
        <h2 class="section-title">Frequently asked</h2>
      </div>
      <p class="section-sub">Answers to what most people ask before their first visit.</p>
    </div>

    <div class="faq-list">
      <details class="faq-item" open>
        <summary>Do you take walk-ins, or is it appointment-only?</summary>
        <p>Walk-ins are welcome whenever there's an open slot, but booking ahead on WhatsApp guarantees your time — especially for bigger or custom pieces that need proper design time.</p>
      </details>
      <details class="faq-item">
        <summary>Is there a minimum age for getting tattooed?</summary>
        <p>Yes — you must be 18 or older with valid ID. No exceptions, no parental sign-offs for minors.</p>
      </details>
      <details class="faq-item">
        <summary>Do I need to pay a deposit to book?</summary>
        <p>For custom or larger pieces, a small deposit secures your slot and is adjusted against the final price. Flash Tattoo Day designs are usually paid on the day, first-come-first-served.</p>
      </details>
      <details class="faq-item">
        <summary>Does it hurt? How bad?</summary>
        <p>It varies by placement and your own pain tolerance — bony areas (ribs, spine, ankles) tend to feel sharper, fleshier areas (outer arm, thigh) are usually more manageable. Happy to talk through what to expect for your specific design when you message.</p>
      </details>
      <details class="faq-item">
        <summary>What about touch-ups?</summary>
        <p>Minor touch-ups within a reasonable window after healing are generally covered — message on WhatsApp with photos of how it's healed and we'll sort out timing.</p>
      </details>
      <details class="faq-item">
        <summary>What payment methods do you accept?</summary>
        <p>Cash and UPI both work. Let us know your preference when you come in.</p>
      </details>
    </div>
  </div>
</section>"""

page(
    "faq.html",
    "FAQ — Trippy Tattooz",
    "Frequently asked questions about booking, pricing, pain, and touch-ups at Trippy Tattooz, Virar.",
    faq_body,
)

# ================= AFTERCARE =================
aftercare_body = """<section class="section" id="aftercare">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Healing 101</div>
        <h2 class="section-title">Aftercare</h2>
      </div>
      <p class="section-sub">You'll get these instructions in person too — save this for reference during healing.</p>
    </div>

    <div class="aftercare-grid">
      <div class="aftercare-card">
        <div class="aftercare-num mono">01</div>
        <h3>First 24 hours</h3>
        <p>Keep the original bandage on for as long as advised (usually a few hours), then gently wash with clean hands and mild, unscented soap. Pat dry with a clean paper towel — don't rub.</p>
      </div>
      <div class="aftercare-card">
        <div class="aftercare-num mono">02</div>
        <h3>Days 2–14</h3>
        <p>Wash gently 2–3 times a day, then apply a thin layer of a fragrance-free healing ointment or lotion. Too much product traps moisture and slows healing — a light layer is enough.</p>
      </div>
      <div class="aftercare-card">
        <div class="aftercare-num mono">03</div>
        <h3>What to avoid</h3>
        <p>No swimming, soaking (baths, pools, the sea), or direct sun on the tattoo until fully healed. Avoid tight clothing rubbing on it, and resist picking at scabs or peeling skin — let it flake off naturally.</p>
      </div>
      <div class="aftercare-card">
        <div class="aftercare-num mono">04</div>
        <h3>When to reach out</h3>
        <p>Some redness, tenderness, and light scabbing is completely normal for the first week or two. If you notice spreading redness, warmth, swelling, or pus, message us on WhatsApp straight away.</p>
      </div>
    </div>
  </div>
</section>"""

page(
    "aftercare.html",
    "Aftercare — Trippy Tattooz",
    "Tattoo aftercare and healing instructions from Trippy Tattooz, Virar.",
    aftercare_body,
)

# ================= REVIEWS =================
reviews_body = """<section class="section" id="reviews">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Word on the street</div>
        <h2 class="section-title">What clients say</h2>
      </div>
      <p class="section-sub">Real messages from clients.</p>
    </div>

    <div class="review-strip">
      <div class="review-card">
        <p class="review-text">Best tattoo experience I've had — super clean setup and the design came out exactly how I imagined it.</p>
        <div class="review-name">— Nelson Anthony</div>
      </div>
      <div class="review-card">
        <p class="review-text">Got a cover-up done here and honestly it looks better than my original tattoo. Highly recommend.</p>
        <div class="review-name">— Jeff Lopes</div>
      </div>
      <div class="review-card">
        <p class="review-text">Booked last minute for a small piece, they still took the time to get the placement right. Will be back.</p>
        <div class="review-name">— Jess Tuscano</div>
      </div>
    </div>
  </div>
</section>"""

page(
    "reviews.html",
    "Reviews — Trippy Tattooz",
    "What clients say about getting tattooed at Trippy Tattooz, Virar.",
    reviews_body,
)

# ================= INSTAGRAM =================
instagram_body = """<section class="section" id="instagram">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">On the feed</div>
        <h2 class="section-title">Follow the ink</h2>
      </div>
      <a href="https://instagram.com/trippy_tattooz" target="_blank" rel="noopener" class="btn btn-ghost">@trippy_tattooz →</a>
    </div>
    <div class="insta-grid" id="instaGrid"></div>
  </div>
</section>"""

page(
    "instagram.html",
    "Instagram — Trippy Tattooz",
    "Follow Trippy Tattooz on Instagram — @trippy_tattooz. Recent reels and posts from the studio.",
    instagram_body,
    extra_scripts=["instagram.js"],
)

# ================= CONTACT =================
contact_body = """<section class="section" id="contact">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-eyebrow">Get inked</div>
        <h2 class="section-title">Book your appointment</h2>
      </div>
      <p class="section-sub">Fastest way in is WhatsApp — send a reference photo, size & placement and you'll get a slot back same day.</p>
    </div>

    <div class="contact-grid">
      <div class="contact-card">
        <h3>Studio details</h3>
        <div class="info-line"><span class="info-label mono">WhatsApp</span><a href="https://wa.me/919145456658?text=Hi!%20I%27d%20like%20to%20book%20a%20tattoo%20appointment" target="_blank" rel="noopener">+91 91454 56658</a></div>
        <div class="info-line"><span class="info-label mono">Instagram</span><a href="https://instagram.com/trippy_tattooz" target="_blank" rel="noopener">@trippy_tattooz</a></div>
        <div class="info-line"><span class="info-label mono">Address</span><span>Trippy Tattooz, Virar, Mumbai — <a href="https://maps.app.goo.gl/ye87wx7a8CCyBrqn6" target="_blank" rel="noopener">get directions</a></span></div>
        <div class="info-line"><span class="info-label mono">Hours</span><span>Mon–Sun, 11:00 AM – 8:00 PM</span></div>
        <a href="https://wa.me/919145456658?text=Hi!%20I%27d%20like%20to%20book%20a%20tattoo%20appointment" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:22px;">Message on WhatsApp</a>
      </div>
      <div class="map-frame">
        <iframe src="https://www.google.com/maps?q=Virar,Maharashtra&output=embed" loading="lazy" allowfullscreen title="Trippy Tattooz location map"></iframe>
        <a href="https://maps.app.goo.gl/ye87wx7a8CCyBrqn6" target="_blank" rel="noopener" class="map-pin-link mono">📍 Open exact pinned location</a>
      </div>
    </div>

    <div class="booking-card">
      <div class="booking-head">
        <h3>Or send your idea straight to WhatsApp</h3>
        <p class="section-sub" style="max-width:560px;">Fill this in — tapping "Send" opens WhatsApp with your message ready to go. Nothing is sent until you hit send there.</p>
      </div>
      <form id="bookingForm" class="booking-form">
        <div class="form-row">
          <label class="mono">Name*</label>
          <input type="text" name="name" required placeholder="Your name">
        </div>
        <div class="form-row">
          <label class="mono">Phone*</label>
          <input type="tel" name="phone" required placeholder="Your WhatsApp number">
        </div>
        <div class="form-row">
          <label class="mono">Tattoo idea*</label>
          <textarea name="idea" required placeholder="Describe the design, placement & rough size"></textarea>
        </div>
        <div class="form-row form-row-half">
          <div>
            <label class="mono">Preferred date</label>
            <input type="date" name="date">
          </div>
          <div>
            <label class="mono">Reference image?</label>
            <input type="text" name="ref" placeholder="e.g. I'll send a photo on WhatsApp">
          </div>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top:6px;">Send on WhatsApp</button>
      </form>
    </div>
  </div>
</section>"""

page(
    "contact.html",
    "Contact & Booking — Trippy Tattooz",
    "Book your tattoo appointment at Trippy Tattooz, Virar — WhatsApp, map, and booking form.",
    contact_body,
    extra_scripts=["contact.js"],
)

print("all pages generated")

