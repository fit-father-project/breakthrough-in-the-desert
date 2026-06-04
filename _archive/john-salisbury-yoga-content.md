# John Salisbury — archived speaker content

**Status:** Removed from event 2026-06-04. John can't participate. We'll replace him with a different yoga instructor; this file preserves his card structure and copy so the slot can be repopulated cleanly.

---

## Speaker card (was in index.html ~line 3471-3479)

```html
<div class="spk-card">
  <img src="speakers/salisbury.webp" alt="John Salisbury" loading="lazy" />
  <div class="spk-name">John Salisbury</div>
  <div class="spk-title">Master Yoga Instructor, Modern Yoga Scottsdale</div>
  <div class="spk-hook">Stretch and open your body to melt tension and prepare for the deepest work of the weekend.</div>
  <div class="spk-toggle">Read bio +</div>
  <div class="spk-bio">John is the owner and head teacher at Modern Yoga in Scottsdale, one of Arizona's most respected yoga communities. With over 25 years of teaching, he blends authentic tradition with a modern, accessible approach. On Saturday morning, he leads the community through a powerful 60-minute yoga and movement session.</div>
</div>
```

## JSON-LD Person entry (was in index.html ~line 108)

```json
{ "@type": "Person", "name": "John Salisbury", "jobTitle": "Master Yoga Instructor, Modern Yoga Scottsdale" }
```

## Agenda line (was in index.html ~line 3614, Saturday Sunrise slot)

Before:
```
Sunrise — Morning Yoga — Led by John Salisbury, 60 minutes on the mat as the sun rises over South Mountain.
```

After (current live):
```
Sunrise — Morning Yoga — 60 minutes on the mat as the sun rises over South Mountain.
```

## Image assets preserved

- `speakers/salisbury.jpg` (80KB)
- `speakers/salisbury.webp` (35KB)
- `speakers/salisbury-cut.png` (243KB)
- `speakers/salisbury-cut.webp` (33KB)

Left in place — not referenced anywhere in the live page after removal, but kept so they don't need re-uploading if John ever rejoins. Safe to delete in a hygiene pass if we want.

## Template for replacement yoga instructor

When the new instructor is confirmed, the card slot can be filled with this same structure:

```html
<div class="spk-card">
  <img src="speakers/[lastname].webp" alt="[Full Name]" loading="lazy" />
  <div class="spk-name">[Full Name]</div>
  <div class="spk-title">[Title or Studio Affiliation]</div>
  <div class="spk-hook">[One-line hook of what they'll do for the attendee]</div>
  <div class="spk-toggle">Read bio +</div>
  <div class="spk-bio">[Full bio, including specific Saturday morning session reference.]</div>
</div>
```

Re-add the JSON-LD Person entry and update the agenda line ("Led by [Name], 60 minutes on the mat...") at the same time.
