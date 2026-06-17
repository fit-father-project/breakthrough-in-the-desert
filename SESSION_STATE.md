# SESSION_STATE — Breakthrough in the Desert site

**Last updated:** 2026-06-16
**Purpose:** Snapshot for any new Claude session picking up this work. Read this first.

---

## Repo + deploy

- Local: `/Users/anthonybalduzzi/Code/anthonybalduzzi/`
- GitHub: `fit-father-project/breakthrough-in-the-desert`
- Deploys via Cloudflare Pages on push to `main`
- Production URLs:
  - `event.fitfatherproject.com/` → `index.html` (FFP audience — Father's Day Flash Sale active)
  - `event.fitfatherproject.com/breakthrough` → `breakthrough.html` (cold/non-FFP audience — Summer Launch Pricing)

---

## Active sale state (as of 2026-06-16)

### Page 1: `index.html` — Father's Day Flash Sale
- **Hero price:** "From $597" (was $845)
- **Tier prices:** GA+ $597 (was $845), VIP $999 (was $1,295)
- **Countdown bar:** `$250+ OFF TICKETS · 150 seats · Sale ends: [countdown] Mon, June 22 (midnight AZ)`
- **JS target:** `2026-06-23T00:00:00-07:00`
- **Spiffy URLs:** `breakthrough-in-the-desert-ga-promo` and `-vip-promo`
- **Revert tag:** `pre-flash-sale-2026`
- **Revert markers:** `<!-- FLASH SALE: ... -->` HTML comments throughout

### Page 2: `breakthrough.html` — Summer Launch
- **Hero price:** "From $597"
- **Tier prices:** GA+ $597 (was $845), VIP $999 (was $1,295)
- **Countdown bar:** `$250+ OFF TICKETS · 150 seats · Sale ends: [countdown] Tue, July 15 (midnight AZ)`
- **JS target:** `2026-07-16T00:00:00-07:00`
- **Spiffy URLs:** Same `-ga-promo` / `-vip-promo` (load-bearing on BOTH pages now)

### LOAD-BEARING WARNING ⚠️

The `-ga-promo` and `-vip-promo` Spiffy URLs now serve BOTH pages. They were created for the Father's Day Flash Sale (ends June 22). If Stuart set them to auto-expire June 22, `breakthrough.html` checkouts will break. **Verify with Stuart whether these URLs remain valid through July 15** before/at the June 22 cutover.

---

## Revert playbook

### To end Father's Day Flash Sale on `index.html` (most likely ask)

User language: *"End the Father's Day Flash Sale on index.html. Keep everything else."*

What to do:
- Restore hero "From $597" → "From $845"
- Restore tier prices to $845 / $1,295, remove strikethroughs + savings badges + sale ribbons
- Restore countdown bar to original early-bird Father's Day messaging
- Restore JS countdown target to original (check `// Original target:` comments)
- Restore JSON-LD prices, validThrough fields
- Remove "FLASH SALE styles" CSS block
- Keep "Travel Made Easy" section unless user says otherwise (it's useful info regardless)
- Use the `<!-- FLASH SALE: ... -->` HTML markers as the revert map
- **Do NOT** wipe Dean, Suivera, Troy, agenda changes, hook framework, etc.

### To archive `breakthrough.html`

User language: *"Archive breakthrough.html — take it down."* → delete the file, commit, push.

### Nuclear (avoid unless catastrophic)

User language: *"Hard reset to pre-flash-sale tag."* → `git reset --hard pre-flash-sale-2026 && git push --force-with-lease`. **Wipes Dean, hook lockdown, breakthrough.html, all recent CTA fixes.** Warn user before executing.

---

## Speaker card hook framework (LOCKED)

All 11 spk-hook lines follow one of three patterns. When adding a new speaker, plug into one:

| Pattern | When to use | Examples |
|---|---|---|
| **"How to [outcome]"** | Teachers | Amie, Jamil, Maraya, Ovadia, Caroline |
| **"[Do/Experience X] with [pronoun] [when] to [outcome]"** | Experiential leaders | Troy, Makenzie, Ryan/Shelby, Dean, Suivera |
| **"A living example of..."** | Special (Jim Flaherty) | Jim only |

Display order on page: Amie, Troy, Jamil, Maraya, Jim, Ovadia, Caroline, Makenzie, Ryan/Shelby, Dean, Suivera.

---

## Mighty Networks broadcast templates (Father's Day promo)

### FFP version
```
Brother,

Some of the deepest transformation work I've done has been in person, not online.

That's what Breakthrough is — three days, 150 people, real work on your body, mind, and spirit. August 7-9, Phoenix.

Tickets are $250+ off this week for Father's Day. Sale ends Monday.

event.fitfatherproject.com

I want you with us in the room.
```

### FMP version
```
Sister,

Some of the deepest transformation work I've done has been in person, not online.

That's what Breakthrough is — three days, 150 people, real work on your body, mind, and spirit. August 7-9, Phoenix.

Tickets are $250+ off this week. Sale ends Monday.

event.fitfatherproject.com

I want you with us in the room.
```

**Differences:** "Brother" ↔ "Sister"; FMP drops "for Father's Day" framing.

---

## Open items / pending decisions

1. **GA4 + Facebook Pixel wiring** — still pending (Task #5 in old task list). Spiffy checkout URLs done 2026-05-26.
2. **Father's Day Flash Sale revert** — needs to happen on/after 2026-06-22. Use revert playbook above.
3. **Confirm `-promo` Spiffy URLs survive past June 22** — Stuart's call. Affects `breakthrough.html` checkout integrity through July 15.
4. **Email 6 (Why Now)** — drafted, not yet sent.
5. **Phase 2 daily emails** — not yet drafted.

---

## Image asset locations (for marketing reuse)

- Composite speaker grid — portrait 600x1866: `~/Downloads/breakthrough-composite-v5.jpg`
- Composite speaker grid — landscape 1920x1080: `~/Downloads/breakthrough-composite-wide-v7.jpg`
- Composite speaker grid — square 1080x1080: `~/Downloads/breakthrough-composite-square-v9.jpg`
- Brian & Renee with baked caption: `~/Downloads/brian-renee-with-caption.jpg`
- Faculty zip for Stuart: `~/Downloads/breakthrough-faculty-photos.zip` (9 numbered files)

---

## Anthony's working preferences (carry forward)

- Wants honest pushback, not yes-manning
- Prefers terse responses, surgical fixes
- "Naturopathic doctor" for breakthrough.html; "Founder of FFP/FMP" for index.html
- Stuart owns Spiffy URLs — don't touch checkout hrefs without flagging
- Replicate API token at `~/.config/replicate/token` — never print to logs/commits/memory
- Never skip git hooks, never amend, never force push to main, use HEREDOC for commits
- Jim Flaherty: actual age 89, display as "at 90"
