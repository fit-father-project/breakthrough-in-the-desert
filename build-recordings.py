#!/usr/bin/env python3
"""Build the Breakthrough 2026 recordings pages (sales + thank-you) for both brands.

  python3 build-recordings.py

Templates -> outputs:
  recordings.src.html           -> recordings.html, recordings-fmp.html              (non-attendees)
                                   recordings-ga.html, recordings-fmp-ga.html        (GA/GA+ attendees)
  thank-you-recordings.src.html -> thank-you-recordings.html, thank-you-recordings-fmp.html

In a template, <!--IF:ga-->attendee copy<!--ELSE-->default copy<!--END--> picks copy per variant.

Edit the .src.html templates for copy/design; edit BRANDS below for per-brand values.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

BRANDS = {
    "ff": {
        "SUFFIX": "",
        "BRAND": "Fit Father Project",
        "APP": "Fit Father app",
        "SALUTATION": "Brother",
        "SUPPORT": "support@fitfatherproject.com",
        "CHECKOUT_99": "https://secure.fitfatherproject.com/checkout/breakthrough-recordings-99",
        "CHECKOUT_159": "https://secure.fitfatherproject.com/checkout/breakthrough-recordings-159",
        # Mighty Networks "join space" link for the Breakthrough 2026 Recordings space
        "JOIN_URL": "https://app.fitfatherproject.com/users/onboarding/choose_plan?plan_id=2292414&bundle_token=99cceb4f94b5d04fd2e526ea239dd659&prefer_signup=true&utm_source=manual",
    },
    "fm": {
        "SUFFIX": "-fmp",
        "BRAND": "Fit Mother Project",
        "APP": "Fit Mother app",
        "SALUTATION": "Sister",
        "SUPPORT": "support@fitmotherproject.com",
        "CHECKOUT_99": "https://secure.fitmotherproject.com/checkout/breakthrough-recordings-99",
        "CHECKOUT_159": "https://secure.fitmotherproject.com/checkout/breakthrough-recordings-159",
        "JOIN_URL": "https://app.fitmotherproject.com/users/onboarding/choose_plan?plan_id=2292424&bundle_token=3fa550af8251f60afe8b7be321773b17&prefer_signup=true&utm_source=manual",
    },
}

# template -> variants ("" = default page, "-ga" = GA/GA+ attendee page)
TEMPLATES = {"recordings": ["", "-ga"], "thank-you-recordings": [""]}
IF_BLOCK = re.compile(r"<!--IF:(\w+)-->(.*?)<!--ELSE-->(.*?)<!--END-->", re.S)


def load(name):
    src = (ROOT / f"{name}.src.html").read_text()
    # swap the "edit this template" comment for a generated-file warning
    start = src.index("<!--")
    end = src.index("-->", start) + 3
    note = f"<!-- GENERATED from {name}.src.html by build-recordings.py. Do not edit directly. -->"
    return src[:start] + note + src[end:]


for name, variants in TEMPLATES.items():
    src = load(name)
    for variant in variants:
        flag = variant.lstrip("-")
        base = IF_BLOCK.sub(lambda m: m.group(2) if m.group(1) == flag else m.group(3), src)
        for vals in BRANDS.values():
            slug = f"{name}{vals['SUFFIX']}{variant}"
            html = base.replace("{{CANONICAL}}", f"https://event.fitfatherproject.com/{slug}")
            for k, v in vals.items():
                html = html.replace("{{" + k + "}}", v.replace("&", "&amp;") if k == "JOIN_URL" else v)
            assert "{{" not in html and "<!--IF:" not in html, f"unfilled token in {slug}"
            (ROOT / f"{slug}.html").write_text(html)
            print("wrote", f"{slug}.html")
