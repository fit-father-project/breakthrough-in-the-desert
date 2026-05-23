# Breakthrough in the Desert · Onboarding for Anthony

Hey Duzzi — this is the working document for your event landing page. James and I built it over the past few weeks. This file gives you (and your Claude) everything you need to review, share, and request changes.

## The live page

**Main URL to share and review:**
https://guldanjamax.github.io/anthonybalduzzi/breakthrough-in-the-desert.html

That's the canonical link. The Diehl hero you picked is in place. Open on mobile and desktop — both are fully designed.

**Once you hand over the Spiffy URLs and want this on `fitfatherproject.com/live-event-2026/`**, it deploys to Cloudflare Pages from this same repo.

## What's on the page (14 sections)

1. **Countdown bar** — live ticking countdown to Father's Day early-bird deadline
2. **Hero** — Diehl golden vista, "Breakthrough in the desert," date/venue/price meta, Reserve Your Spot button (glass halo style)
3. **Mirror** — "The mirror caught up with you" — three numbered stories (Physically / Mentally / In Your Relationships) ending in "Is this it?"
4. **Pivot** — "No. This isn't it. Unless you let it be." full-bleed Amazon walk photo behind
5. **Promise** — Full-bleed 2025 community photo (upscaled), frosted center panel with the Sunday cacao circle description
6. **Leave With** — Three cards with real event photo headers: Clarity, Energy, Circle of Aligned Friends
7. **Social Proof** — Couples Spotlight (Brian + Renee, Bruce + Donna), Glass Wall of 6 attendees with curated quotes Anthony provided, 6 more voices in supplementary cards
8. **Founder** — Family Letter, Anthony + Brooke full-screen background
9. **Speakers** — 8 faculty in Lead + Circle layout (Anthony lead, 7 others as circle cards)
10. **3-Day Arc Posters** — Awareness / Activation / Integration with real photos
11. **Agenda** — Schedule format for each day (Time → Activity → Speaker → Plain-English description)
12. **Venue** — Arizona Grand Resort cinematic plate + feature grid + August heat reassurance
13. **Pricing** — GA+ $845 / VIP $1,295 early-bird, partner add-ons, 3-pay option, "Only 150 seats" scarcity
14. **FAQ** — Full-bleed lake photo, 13 frosted accordion items
15. **Final CTA** — Full-bleed silhouette of Anthony in vast desert, "You've read this far for a reason."

## What's pending from you, Duzzi

1. **Spiffy checkout URLs** for GA+, VIP, GA+ partner, VIP partner — the four Reserve buttons currently fire `mailto:support@fitfatherproject.com` as an interim, so leads still come in.
2. **GA4 + Facebook Pixel IDs** — once you have them, we wire analytics in 10 minutes.
3. **Cleaner headshots** for John Salisbury / Maraya Brown / Luana Marzluff (current ones are workable but not tight studio quality). Or we get permission to use what's there.
4. **Real Arizona Grand Resort photos** (or use the AGR website assets — we already pulled lazy-river and palms-evening).
5. **15-25 candid headshots of yourself** if you want the LoRA likeness at 95%+ instead of the current 90%. See LoRA section below.

## Variants live for comparison

- Bee hero: https://guldanjamax.github.io/anthonybalduzzi/breakthrough-in-the-desert-v3.html
- Diehl hero (CURRENT WINNER): canonical URL above
- Sunset rock hero: https://guldanjamax.github.io/anthonybalduzzi/breakthrough-in-the-desert-v3-sunset.html

## DUZZI LoRA — your synthetic content engine

We trained a custom AI model on 19 of your photos. Trigger word: `DUZZI`.

- **v1:** `guldanjamax/anthony-balduzzi-lora:dbf08cafa8da68b40c99c9dc86edad6e542dfd8e7c4c5a58bdc1d01c3f44a0c2` (more polished / gigachad-leaning)
- **v2 (current):** `guldanjamax/anthony-balduzzi-lora:3581342165ae7e32cbb09d0aa85aea6915e70fb28be8b54bc3030bf9b5a2e559` (more natural, ~90% likeness)
- **Cost per image:** ~$0.04 on Replicate. Takes 22 seconds.

**Existing campaign asset library:**
- https://guldanjamax.github.io/anthonybalduzzi/duzzi-campaign.html (30 image campaign launcher, weekly drip calendar)
- https://guldanjamax.github.io/anthonybalduzzi/duzzi-v2.html (10 test renders showing v2 likeness improvement)
- https://guldanjamax.github.io/anthonybalduzzi/duzzi-lora-ideas.html (40 idea catalog with headlines for each funny one)

**Honest note on likeness:** Your LoRA is at about 90% likeness. James/Juliet/Re's LoRAs are 95%+ because they were trained on single-shoot photo sessions. Your training set spans 2017-2026 in many different lighting conditions, which averages out into a slightly-off "averaged" you. The fix: spend 30 minutes shooting 20 tight headshots in one session, then we retrain to 95%. Until then, use synthetic images only where face detail matters less (stylized art, silhouettes, mid-distance shots).

## Faculty section iterations

We built 6 design directions for the Faculty section (3 with regular headshots, 3 with Photoroom-removed-background composites):
https://guldanjamax.github.io/anthonybalduzzi/faculty-iterations-v2.html

Top picks:
1. Sandstone Pillars (90% conf) — red-rock backdrop with frosted ink pillar cards
2. Desert Gathering (92% conf) — all 8 faculty composited together in one Sonoran sunset scene
3. Twilight Council Cards (86% conf) — frosted glass cards on blue-hour mountains

## SEO + legal — already shipped

- JSON-LD schema (Event + FAQ + Person + Organization) for Google + ChatGPT/Perplexity
- robots.txt + sitemap.xml + llms.txt (AI crawler standard)
- privacy.html, terms.html, health-disclaimer.html (stub pages — replace with your legal team's review)
- OG image with Anthony on Sedona red rock + event details

## Mobile

The site is fully optimized for 40+ readability on mobile:
- Body text 16-18px minimum
- 60px touch targets
- Glass cards stack to 1 column
- Couples Spotlight reshapes to portrait crops
- Fade-in animations disabled on mobile (was making sections feel "blank")
- Strong text-shadows on photo-bg sections for older eyes

## Costs to date

- Site build: $0 (running on GitHub Pages)
- 2 LoRA trainings: $10
- ~70 image generations: ~$2.80
- Photoroom background removal: ~$0.16
- Replicate clarity-upscaler (Promise photo): ~$0.10
- **Total: ~$13.06**

## What I'd ask you to do today

1. **Open the live page on your phone and desktop** — scroll through every section, take notes
2. **Send back any copy or photo changes** you want
3. **Confirm whether Diehl is still the winning hero** (it is, but final lock-in is yours)
4. **Send Spiffy URLs** when ready — 10 minutes to wire them
5. **Decide on the funny campaign** — review the 30 DUZZI images, pick which ones go to email/social
6. **Optional: schedule a 30-min iPhone selfie shoot** if you want the LoRA at 95% likeness

That's everything. James and I are standing by.

— Claude (running in James's Cowork)
