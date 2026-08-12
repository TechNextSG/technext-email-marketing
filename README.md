# TechNext Email Marketing

Three production-ready HTML email campaigns for TechNext, plus a preview hub that hosts them.

**Live:** https://technextsg.github.io/technext-email-marketing/
**Local:** `serve-technext-email.bat` → http://localhost:3953 (launch.json name `technext-email`)

## Contents

| File | What it is |
|---|---|
| `index.html` | Preview hub — desktop/mobile previews, subject lines, copy-to-clipboard, Brevo steps, pre-send checklist |
| `emails/01-intro-service-offer.html` | Flagship service-offer campaign (warm list, evergreen) |
| `emails/02-odoo-erp.html` | Odoo ERP campaign with the Singapore InvoiceNow angle |
| `emails/03-newsletter-monthly.html` | Monthly "TechNext Insights" newsletter shell |
| `text/*.txt` | Plain-text alternate for each email — paste into Brevo's plain-text tab |
| `assets/logo-*.png` | Email-safe logos, pre-flattened onto their background colour: `-white-on-dark` for the #0B1220 top bar, `-blue-on-white` for the footer, `-white-on-blue` spare for a #3167CA header variant |

## Build rules these follow

- **600px, table-based, inline styles.** `role="presentation"` on every layout table.
- **Outlook:** `PixelsPerInch` reset, `mso-line-height-rule:exactly` on text, VML `roundrect`
  buttons with `arcsize="0%"` (brand uses sharp corners), and an mso-only 600px wrapper table.
- **Mobile:** one `@media (max-width:620px)` block; `.stack` collapses columns, `.pad` reduces
  gutters, `.btn a` goes full width.
- **Images:** absolute HTTPS URLs only, every one with `width`/`height`/`alt` and
  `display:block`. Logos are flattened onto their background colour rather than relying on PNG
  transparency, which some Outlook builds render as black.
- **No merge tags in visible copy**, so a browser preview and a test send look identical. The only
  tag is `{{ unsubscribe }}` in the footer href.
- **Dark mode:** declared light-only (`color-scheme: light`) so Apple Mail and Outlook.com do not
  invert the palette. Every text node has an explicit colour and every band an explicit `bgcolor`,
  which is the best available defence in Gmail's forced dark mode.
- **UTM on every link:** `utm_source=email`, `utm_medium=newsletter`, per-campaign
  `utm_campaign`, and `utm_content` naming the specific CTA.

## Where the copy comes from

Nothing is invented. The headline, sub-copy, stats (10+ countries, 11+ enterprise clients,
4 core AI disciplines), the four capability descriptions, the industry list, the client names
(Qualcomm, TSMC, Singapore Government) and the partner badges are taken from technext.asia as
read on 2026-08-12. The booking link `technext.odoo.com/book/c82cf8a9` and WhatsApp number
+65 8839 6998 are the ones the live site uses. The legal footer is the ACRA record:
TECHNEXT PTE. LTD., UEN 202699888G, 261 Waterloo Street #03-36, Waterloo Centre, Singapore 180261.

**"ISO 27001 (in progress)" keeps its qualifier** — TechNext is not certified, and dropping the
parenthesis would be a false claim.

**Resolved 2026-08-12:** Odoo's own partner directory lists
[TECHNEXT PTE. LTD](https://www.odoo.com/partners/technext-pte-ltd-28073844) as an
**"Odoo Ready Partner"**. Odoo's company tiers are only Ready / Silver / Gold — "Certified Partner"
is not a tier ("certified" refers to individual employee exams). Email 01 now says
**Odoo Ready Partner**, matching the badge asset and the directory.
**Still to do outside this repo:** technext.asia itself says "Certified Odoo Partner".

## Before sending

The sending domain has **no SPF record**, and `technextasia.com` is already at DMARC
`p=quarantine`. Brevo has no authenticated domain added. Fix DNS and authenticate the domain in
Brevo before any of this goes out — see the checklist at the bottom of `index.html`.

These templates are written for an **opted-in** list. For cold prospecting use the plain,
image-free copy in `00. TechNext Folder\Email Outreach\outreach-copy-v2.md` instead.
