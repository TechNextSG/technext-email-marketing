# TechNext email marketing: sending playbook

Campaigns 04-08 (BIR CAS hook series: one question each, then our service). Brevo drafts #29-#33. Written 22 Oct 2026, series rewritten 23 Oct 2026.

## 1. Who we send to (consent first)

Philippine Data Privacy Act: marketing consent must be freely given, specific, informed and recorded. Silence or a pre-ticked box is not consent.

| Source | Can they get campaigns 04-08? |
|---|---|
| People who ticked a marketing opt-in (form, event sign-up, written yes) | Yes |
| Existing clients | Only if they agreed to receive updates; otherwise ask them first (one personal email) |
| Website form leads (adviser form, quotation form) | **Not yet.** The form has no marketing opt-in box, so they only agreed to hear back about their enquiry. Reply to the enquiry; ask for opt-in in that reply. |
| Bought, scraped or cold lists, old April 2026 country lists | **Never** |

Before the first import:
- Load the suppression list first: everyone who ever unsubscribed or bounced. Never re-mail them.
- Record where each contact's consent came from (a Brevo attribute such as `CONSENT_SOURCE` and date).
- Owner rule: no contacts go into Brevo without the owner's go-ahead for that batch.

Fix for the future: add an unticked checkbox to the website forms, "Email me BIR and Odoo updates. Unsubscribe any time.", and pass it to Odoo CRM as a tag.

## 2. Start small (warm-up)

The domain is young and the April 2026 cold blasts (about 5,500 sends) may have hurt its reputation.

| Send | Audience size | Go on only if |
|---|---|---|
| 1 | Up to 50 most engaged contacts | bounces < 2%, spam complaints < 0.1%, unsubscribes < 1% |
| 2 | Up to 150 | same |
| 3 | Up to 400 | same |
| 4+ | Grow about 2x per send | same |

If any limit is broken: stop, find out why, fix the list. Do not send to "everyone" in one go.

Suggested order: 04 (is your system registered?) first, then 05, 06, 07 and 08 a week apart. Skip anyone who already booked a call. Resend to non-clickers at most once, with the alternative subject.

Measure clicks, form submissions and replies. Ignore open rates (Apple Mail opens everything).

## 3. Keep every fact true

Every fact in 04-08 comes from technext.asia/bir-cas. Before each send, check that page has not changed (new RMC, a published list of accredited e-invoicing providers, new dates). The old 10-slot offer was removed on 23 Oct 2026: it is not on the website.

## 4. Replies

- Replies go to hello@technext.asia (Brevo reply-to); the emails show sales@technext.asia, the address on the website. Both inboxes must be read every working day.
- Answer within one working day.
- Adviser-call requests and enquiries go into Odoo CRM, unassigned, with @Jeric mentioned (he takes them himself).
- Unsubscribe requests sent by reply: unsubscribe them in Brevo the same day.

## 5. Account fixes (owner)

**Brevo company address** (reads "Taguig, Metro Manila, Tanay 1634")
Brevo, top right account menu, Settings, Company / My information. Set: Street `Level 9, IP Center (Intellectual Property Center)`, City `Taguig City`, Region `Metro Manila`, ZIP `1634`, Country `Philippines`. Save.

**Old sender hello@technext.asia**
Already done by Claude: the two transactional templates that used it (#3, #12) now send from hello@technextasia.com, names unchanged.
Owner: Brevo, Senders, Domains & Dedicated IPs, Senders, hello@technext.asia, menu, Delete. (Brevo has no "deactivate".)

**technext.asia DNS (Namecheap, Advanced DNS)**
1. SPF, TXT record, host `@`: `v=spf1 include:_spf.google.com ~all` (add `include:_spf.odoo.com` before `~all` only if Odoo sends mail as @technext.asia).
2. DKIM: Google Admin, Apps, Google Workspace, Gmail, Authenticate email, technext.asia, Generate new record (2048-bit). Add the TXT record it shows (host `google._domainkey`) in Namecheap, wait an hour, click Start authentication.
3. DMARC, keep `p=none` for two weeks while reports come in, then move to `p=quarantine`.

**Empty Brevo lists**
Brevo, Contacts, Lists. Delete the 40 empty lists: 3, 5-10, 13-34, 36, 38-47. Keep #2 (test list) and #12 (system list).

**API key**
Brevo, SMTP & API, API keys: generate a new key, then delete the old one (it was pasted in a chat). Keep the new key out of chats; if Claude should use it, store it as an environment variable on this PC.

**IP allowlist**
This PC's internet connection switches between two addresses (103.43.215.54 and 126.209.111.210); both are on the list. If the provider changes them, API access stops until the new one is added.

**Gmail connector**
Claude settings, Connectors, Gmail, Reconnect. Then Claude can check where the test emails land and read their headers.

**Sender avatar**
Set `sender-logo/technext-sender-avatar-512.png` as the profile photo of the hello@technextasia.com Google account.

## 6. Before every send

- [ ] Contacts have recorded consent; suppression list loaded
- [ ] technext.asia/bir-cas re-read; email facts still match
- [ ] Test sent to hello@technextasia.com and hello@technext.asia, checked in Gmail web, Gmail app (dark mode) and Outlook
- [ ] Audience size within the warm-up step
- [ ] Someone is reading replies that day
