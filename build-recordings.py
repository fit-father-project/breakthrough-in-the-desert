#!/usr/bin/env python3
"""Build the Breakthrough 2026 recordings pages (sales + thank-you) for both brands.

  python3 build-recordings.py

Templates -> outputs:
  recordings.src.html           -> recordings.html,           recordings-fmp.html
  thank-you-recordings.src.html -> thank-you-recordings.html, thank-you-recordings-fmp.html

Edit the .src.html templates for copy/design; edit BRANDS below for per-brand values.
"""
from pathlib import Path

ROOT = Path(__file__).parent

BRANDS = {
    "ff": {
        "SUFFIX": "",
        "BRAND": "Fit Father Project",
        "APP": "Fit Father app",
        "SALUTATION": "Brother",
        "SUPPORT": "support@fitfatherproject.com",
        "CANONICAL": "https://event.fitfatherproject.com/recordings",
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
        "CANONICAL": "https://event.fitfatherproject.com/recordings-fmp",
        "CHECKOUT_99": "https://secure.fitmotherproject.com/checkout/breakthrough-recordings-99",
        "CHECKOUT_159": "https://secure.fitmotherproject.com/checkout/breakthrough-recordings-159",
        "JOIN_URL": "https://app.fitmotherproject.com/users/onboarding/choose_plan?plan_id=2292424&bundle_token=3fa550af8251f60afe8b7be321773b17&prefer_signup=true&utm_source=manual",
    },
}

TEMPLATES = ["recordings", "thank-you-recordings"]


def load(name):
    src = (ROOT / f"{name}.src.html").read_text()
    # swap the "edit this template" comment for a generated-file warning
    start = src.index("<!--")
    end = src.index("-->", start) + 3
    note = f"<!-- GENERATED from {name}.src.html by build-recordings.py. Do not edit directly. -->"
    return src[:start] + note + src[end:]


for name in TEMPLATES:
    src = load(name)
    for vals in BRANDS.values():
        html = src
        for k, v in vals.items():
            html = html.replace("{{" + k + "}}", v.replace("&", "&amp;") if k == "JOIN_URL" else v)
        out = f"{name}{vals['SUFFIX']}.html"
        assert "{{" not in html, f"unfilled token in {out}"
        (ROOT / out).write_text(html)
        print("wrote", out)
