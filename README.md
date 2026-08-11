# Trippy Tattooz — Website

A 10-page website built for your shop — each section now lives on its own page instead of one long scroll. No build tools, no hosting cost required — you can put this online for free.

## File structure

```
index.html        → Home (hero + links to every other page)
studio.html        → The Studio
work.html          → Recent Work (portfolio grid + click-to-zoom)
menu.html          → Flash Menu & Pricing
about.html         → About Us
faq.html           → FAQ
aftercare.html     → Aftercare
reviews.html       → Reviews
instagram.html     → Instagram embeds
contact.html       → Contact & booking form

styles.css         → All the site's styling — edit once, every page updates
script.js          → Shared logic (mobile menu, footer year) — runs on every page
work.js            → Portfolio data + lightbox — only runs on work.html
instagram.js       → Instagram reel links — only runs on instagram.html
contact.js         → Booking form logic — only runs on contact.html

images/            → All photos and the logo
build_pages.py     → Regenerates all 10 pages from one script (see note below)
```

Every page shares the same nav bar, mobile drawer menu, and footer — editing `styles.css` changes the look everywhere at once, so you're not fixing the same thing 10 times.

**Editing text on a specific page** (like fixing a typo in the FAQ, or updating a price): just open that page's `.html` file directly and edit it like before — no need to touch `build_pages.py` for small text changes.

**Editing something shared across every page** (like adding a new nav link, or changing the WhatsApp number everywhere): tell me and I'll regenerate all 10 pages consistently — doing this by hand across 10 files risks missing one.

## 1. Your logo

`images/logo.jpg` is your real logo — color-boosted for a punchier neon glow, and already wired into the nav bar, the hero section, and the browser tab icon (favicon).

Any time you send a new photo (portfolio shots, your own picture, anything), it gets the same treatment before going into the site: saturation lifted, contrast punched up, a touch of sharpening — enough to make colors pop without introducing a color tint into grays, blacks, or whites. You don't need to do anything for this, just send photos.

## 2. Add your real photos

Save your tattoo photos from Instagram (open the post → save/screenshot) and drop them into the `images` folder using these **exact filenames**. Until you do, the site shows a "drop your photo here" placeholder in that spot, so you'll always know what's missing.

| Filename | Where it shows |
|---|---|
| `images/portfolio-1.jpg` through `images/portfolio-13.jpg` | The "Recent work" flash-sheet grid (work.html) |
| `images/artist-portrait.jpg` | The About page |
| `images/studio-1.jpg`, `images/studio-2.jpg` | The Studio page |

- Recommended: square-ish or portrait crop (4:5 ratio works best), at least 800px wide.

- Want more or fewer than 8 portfolio pieces? Open `index.html`, find the `PORTFOLIO` array near the bottom (inside the `<script>` tag), and add/remove lines. Each line needs a filename, a short style name, and a tag (e.g. "Fine Line", "Traditional", "Cover-Up").

## 3. Fill in your real details

Open `index.html` and update:

- **Reviews** — swap the three sample reviews for real client quotes/screenshots once you have a few saved.
- Your **WhatsApp number**, **address**, and **Google Maps link** are already filled in.

## 4. Embed real Instagram posts

Right now the "Follow the ink" section shows placeholder cards linking to your profile, because embedding needs specific post links.

To show real posts:
1. Open any Instagram post you want to feature → tap **⋯** → **Copy link** (looks like `https://www.instagram.com/p/XXXXXXXXXXX/`)
2. Open `index.html`, find `var INSTAGRAM_POSTS = [` near the bottom (inside the `<script>` tag)
3. Add each link as a new line, like:
   ```
   var INSTAGRAM_POSTS = [
     'https://www.instagram.com/p/C1a2B3cDeFg/',
     'https://www.instagram.com/p/C4h5I6jKlMn/',
   ];
   ```
4. Save and reopen the page — those posts will now embed live, with likes/comments, straight from Instagram.

## 5. About the Google Maps link

Your Google Maps share link (`maps.app.goo.gl/...`) is used for the **"Get directions"** buttons — those will take people straight to your exact pinned location.

The map preview embedded on the page itself uses a general "Virar, Maharashtra" map, because share links like yours can't be embedded directly as a live map — only used as a link. If you want the exact pin to show in the embedded map itself (not just the button), open Google Maps, search your shop, click **Share → Embed a map**, copy that `<iframe>` code, and send it to me — I'll drop it straight in.

## 6. The WhatsApp booking form

The form on the site ("Or send your idea straight to WhatsApp") doesn't need any backend or hosting cost. When someone fills it in and hits **Send on WhatsApp**, it opens WhatsApp (web or app) with a message pre-filled from their answers — they just have to tap send on their end. Nothing is emailed or stored anywhere; it's a pure convenience wrapper around your WhatsApp number.

## 7. Put it online for free

Any of these work with zero cost:

**Option A — Netlify Drop (easiest, 2 minutes)**
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the whole `trippy-tattooz-site` folder onto the page
3. You'll get a free live link instantly (you can rename it in site settings)

**Option B — GitHub Pages (free custom-ish URL, good if you already use GitHub)**
1. Create a new GitHub repo, upload the folder contents
2. Go to Settings → Pages → set source to the main branch
3. Your site goes live at `yourusername.github.io/reponame`

**Option C — Vercel**
1. Sign up at vercel.com, "Add New Project," drag/upload the folder
2. Deploy — free URL provided instantly

Once live, put the link in your Instagram bio and Google Business Profile.

## 8. Add free traffic analytics (optional)

Site doesn't currently track visitors — here's how to add it in 5 minutes:

1. Go to [analytics.google.com](https://analytics.google.com), create a free account, add your site, and copy the **Measurement ID** it gives you (looks like `G-XXXXXXXXXX`)
2. Open `index.html`, right before the closing `</head>` tag, paste:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```
3. Replace both `G-XXXXXXXXXX` with your real ID
4. Give it a day or two, then check Google Analytics to see visits, where people come from, and which pages they spend time on

## 9. Optional next steps

- Buy a `.com`/`.in` domain later (roughly ₹500–900/year) and point it at whichever free host you use — all three above support custom domains for free.
- Send me your Google Maps "Embed a map" iframe code (see step 5) if you want the exact pin shown live on the page.
