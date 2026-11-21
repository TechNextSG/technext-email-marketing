# TechNext BIR CAS email series, 21 Nov 2026 redesign (Brevo #39-#43, NCR fresh list #75).
# Live technext.asia look (site.css tokens, Plus Jakarta Sans + Inter), light only, real company facts.
# Usage: python build_nov21.py  -> technext-email-marketing/emails/nov21/*.html + text/nov21/*.txt
import html, pathlib, re

ROOT = pathlib.Path.home() / 'ClaudeWork/technext-email-marketing'
OUT_H, OUT_T = ROOT / 'emails/nov21', ROOT / 'text/nov21'
SITE = 'https://technext.asia'
BOOK = 'https://technext.odoo.com/book/c82cf8a9'
ASSET = 'https://technextsg.github.io/technext-email-marketing/assets'
SIG = 'https://technextsg.github.io/technext-branding-miscellaneous/sig'

# ---- real company facts (live site technext.asia/company + ACRA profile, checked 21 Nov 2026)
LEGAL = 'TECHNEXT PTE. LTD. (UEN 202699888G) &middot; 261 Waterloo Street, #03-36, Waterloo Centre, Singapore 180261'
OFFICES = [('Singapore HQ', '261 Waterloo Street #03-36, Singapore 180261'),
           ('Philippines', 'Level 9, IP Center, Taguig City, Metro Manila 1634')]
MAIL = 'sales@technext.asia'
PROOF = [('142', 'projects delivered'), ('90+', 'enterprise clients'), ('25+', 'countries')]
DEADLINES = [('E-invoicing', '31 Dec 2026'), ('2026 books in ORUS', '30 Jan 2027')]
CTA = 'Start my 5 Day Express'
CTA_NOTE = 'It starts with a 15-minute Technical Readiness Call with a BIR CAS adviser, at no charge. Your current system stays.'
OFFER = '5 Day Express BIR CAS Set-up'
STAR = ('*The 5 days cover the system set-up once your data is ready. Registration timing is set by your RDO, '
        'and filing stays with your business.')
DISCLAIMER = ('TechNext is an Odoo Ready Partner. We are not affiliated with, accredited by or acting for the BIR or any government agency, '
              'and we do not file or register on your behalf. General guidance, not tax advice: confirm with your accountant or RDO.')
WHY_YOU = ('You are receiving this because your company is listed as a business contact in Metro Manila and the BIR&rsquo;s CAS rules may apply to it. '
           'Not relevant? Unsubscribe below and we will stop.')
SOCIAL = [('fb', 'https://www.facebook.com/technextasia', 'Facebook'), ('li', 'https://www.linkedin.com/company/technextasia/', 'LinkedIn'),
          ('ig', 'https://www.instagram.com/technextasia/', 'Instagram'), ('yt', 'https://www.youtube.com/@technextasia', 'YouTube')]

# ---- tokens (live site.css)
BLUE, BLUE7, BLUE3, BLUE1, BLUE05 = '#3167CA', '#1E4691', '#6FA0F5', '#DDE7F8', '#EAF0FB'
INK, BODY, MUTED, LINE, ALT = '#1F1F3D', '#4C4C63', '#8888A0', '#E7E4E9', '#FAF9FB'
OK, OK05, AMB, AMB05 = '#137A4A', '#E7F4ED', '#A96B00', '#FDF6E9'
FH = "font-family:'Plus Jakarta Sans',Arial,Helvetica,sans-serif;"
FB = "font-family:Inter,Arial,Helvetica,sans-serif;"
PILL = {'ok': (OK05, OK), 'blue': (BLUE05, BLUE7), 'amb': (AMB05, AMB), 'mut': (ALT, BODY)}


def u(path, content, camp):
    base = path if path.startswith('http') else SITE + path
    j = '&amp;' if '?' in base else '?'
    return f'{base}{j}utm_source=brevo&amp;utm_medium=email&amp;utm_campaign={camp}&amp;utm_content={content}'


def plain(s):
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\xa0', ' ')
    for a, b in (('‘', "'"), ('’', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-'), ('‑', '-'), ('→', '->')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


def hl(t):  # blue highlight phrase, like .hl on the site
    return f'<span style="color:{BLUE};">{t}</span>'


OFFER_HL = f'{hl("5 Day")} Express {hl("BIR CAS")} Set-up*'


def offer_card():
    """5 Day Express offer strip under the hero: speed + topic, no day-by-day breakdown (Sky 10 Nov)."""
    pts = [('Starting today', 'Book a slot this week. We plan your sprint on the call.'),
           ('As quick as 5 days*', 'Your BIR CAS set-up in Odoo, run as one short sprint.'),
           ('Your system stays', 'Odoo plugs in to your current accounting software or POS.')]
    cells = ''.join(f'<td class="stack" width="33%" valign="top" style="padding:14px 14px 4px 0;">'
                    f'<div style="{FH}font-size:15px;line-height:20px;font-weight:800;color:{BLUE7};padding-bottom:4px;">{a}</div>'
                    f'<div style="{FB}font-size:13px;line-height:20px;color:{BODY};">{b}</div></td>' for a, b in pts)
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {BLUE1};border-radius:14px;border-collapse:separate;background-color:#FFFFFF;" bgcolor="#FFFFFF">'
            f'<tr><td style="padding:20px 22px 16px 22px;">'
            f'<div style="{FB}font-size:11px;line-height:15px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;color:{MUTED};padding-bottom:6px;">The offer</div>'
            f'<div class="h2" style="{FH}font-size:22px;line-height:29px;font-weight:800;color:{INK};">{OFFER_HL}</div>'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table>'
            f'</td></tr></table>')


# ---------------------------------------------------------------- blocks
def row(inner, top=36, bg='#FFFFFF', bottom=0, cls='pad'):
    return (f'<tr><td class="{cls}" bgcolor="{bg}" style="background-color:{bg};padding:{top}px 36px {bottom}px 36px;">\n{inner}\n</td></tr>\n')


def eyebrow(t, color=BLUE):
    return f'<p style="margin:0 0 10px 0;{FB}font-size:12px;line-height:16px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;color:{color};">{t}</p>'


def h2(t, mb=12, size=22, lh=29, color=INK):
    return f'<h2 class="h2" style="margin:0 0 {mb}px 0;{FH}font-size:{size}px;line-height:{lh}px;font-weight:800;color:{color};mso-line-height-rule:exactly;">{t}</h2>'


def p(t, mb=14, size=15, lh=24, color=BODY):
    return f'<p style="margin:0 0 {mb}px 0;{FB}font-size:{size}px;line-height:{lh}px;color:{color};">{t}</p>'


def button(label, href, light=False, w=None):
    fill, txt = ('#FFFFFF', BLUE7) if light else (BLUE, '#FFFFFF')
    w = w or int(len(plain(label)) * 8.4 + 70)
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" class="btn"><tr><td align="center" bgcolor="{fill}" style="background-color:{fill};border-radius:8px;">'
            f'<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{href}" style="height:50px;v-text-anchor:middle;width:{w}px;" arcsize="16%" stroke="f" fillcolor="{fill}">'
            f'<w:anchorlock/><center style="color:{txt};font-family:Arial,sans-serif;font-size:15px;font-weight:bold;">{label} &rarr;</center></v:roundrect><![endif]-->'
            f'<!--[if !mso]><!--><a href="{href}" style="display:inline-block;padding:15px 24px;{FH}font-size:15px;line-height:20px;font-weight:700;color:{txt};text-decoration:none;border-radius:8px;">{label}&nbsp;&rarr;</a><!--<![endif]-->'
            '</td></tr></table>')


def pill(t, kind):
    bg, fg = PILL[kind]
    return f'<span style="display:inline-block;padding:3px 9px;border-radius:999px;background-color:{bg};{FB}font-size:11px;line-height:15px;font-weight:600;color:{fg};white-space:nowrap;">{t}</span>'


def window(title, rows):
    """Odoo-style UI card with traffic-light dots and a Sample data tag, as on the site hero."""
    dots = ''.join(f'<span style="display:inline-block;width:9px;height:9px;border-radius:9px;background-color:{c};margin-right:5px;"></span>' for c in ('#FF5F57', '#FEBC2E', '#28C840'))
    out = [f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};border-radius:14px;border-collapse:separate;background-color:#FFFFFF;">',
           f'<tr><td bgcolor="{ALT}" style="background-color:{ALT};border-bottom:1px solid {LINE};border-radius:14px 14px 0 0;padding:11px 16px;">'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
           f'<td style="{FB}font-size:12px;line-height:16px;color:{BODY};">{dots}<span style="padding-left:6px;font-weight:600;color:{INK};">{title}</span></td>'
           f'<td align="right" style="{FB}font-size:10px;line-height:14px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:{MUTED};">Sample data</td></tr></table></td></tr>',
           '<tr><td style="padding:4px 16px 6px 16px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">']
    for i, (label, val, kind) in enumerate(rows):
        bb = '' if i == len(rows) - 1 else f'border-bottom:1px solid {LINE};'
        out.append(f'<tr><td style="padding:11px 0;{bb}{FB}font-size:13px;line-height:18px;font-weight:600;color:{INK};">{label}</td>'
                   f'<td align="right" style="padding:11px 0;{bb}">{pill(val, kind)}</td></tr>')
    out.append('</table></td></tr></table>')
    return ''.join(out)


def facts(rows, label_w=150):
    out = [f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};">']
    for l, v in rows:
        out.append(f'<tr><td class="stack lbl" width="{label_w}" valign="top" style="padding:13px 14px 13px 0;border-bottom:1px solid {LINE};{FB}font-size:13px;line-height:20px;font-weight:600;color:{INK};">{l}</td>'
                   f'<td class="stack" valign="top" style="padding:13px 0;border-bottom:1px solid {LINE};{FB}font-size:14px;line-height:22px;color:{BODY};">{v}</td></tr>')
    out.append('</table>')
    return ''.join(out)


def compare(head, rows):
    out = [f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};border-radius:14px;border-collapse:separate;">',
           f'<tr><td width="26%" style="padding:12px 12px;border-bottom:1px solid {LINE};"></td>'
           + ''.join(f'<td width="37%" valign="top" bgcolor="{BLUE05}" style="background-color:{BLUE05};padding:12px 12px;border-bottom:1px solid {LINE};border-left:1px solid {LINE};{FH}font-size:14px;line-height:19px;font-weight:800;color:{BLUE7};">{h}</td>' for h in head) + '</tr>']
    for i, r in enumerate(rows):
        bb = '' if i == len(rows) - 1 else f'border-bottom:1px solid {LINE};'
        lab = f'<td valign="top" style="padding:12px 12px;{bb}{FB}font-size:12px;line-height:18px;font-weight:600;color:{INK};">{r[0]}</td>'
        if len(r) == 2:
            out.append(f'<tr>{lab}<td colspan="2" valign="top" style="padding:12px 12px;{bb}border-left:1px solid {LINE};{FB}font-size:13px;line-height:20px;color:{BODY};">{r[1]}</td></tr>')
        else:
            out.append(f'<tr>{lab}' + ''.join(f'<td valign="top" style="padding:12px 12px;{bb}border-left:1px solid {LINE};{FB}font-size:13px;line-height:20px;color:{BODY};">{c}</td>' for c in r[1:]) + '</tr>')
    out.append('</table>')
    return ''.join(out)


def checks(items, bg=ALT, title=None):
    out = [f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-radius:14px;border-collapse:separate;background-color:{bg};" bgcolor="{bg}"><tr><td style="padding:20px 22px 10px 22px;">']
    if title:
        out.append(f'<div style="{FB}font-size:12px;line-height:16px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;color:{MUTED};padding-bottom:12px;">{title}</div>')
    out.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">')
    for it in items:
        out.append(f'<tr><td width="26" valign="top" style="padding:0 0 11px 0;{FB}font-size:14px;line-height:22px;font-weight:700;color:{OK};">&#10003;</td>'
                   f'<td valign="top" style="padding:0 0 11px 0;{FB}font-size:14px;line-height:22px;color:{INK};">{it}</td></tr>')
    out.append('</table></td></tr></table>')
    return ''.join(out)


def steps(items):
    out = ['<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">']
    for i, (t, d) in enumerate(items):
        pb = 0 if i == len(items) - 1 else 16
        out.append(f'<tr><td width="44" valign="top" style="padding:0 0 {pb}px 0;"><div style="width:30px;height:30px;line-height:30px;border-radius:30px;background-color:{BLUE05};text-align:center;{FH}font-size:13px;font-weight:800;color:{BLUE};">{i + 1}</div></td>'
                   f'<td valign="top" style="padding:3px 0 {pb}px 0;"><div style="{FH}font-size:15px;line-height:21px;font-weight:700;color:{INK};padding-bottom:3px;">{t}</div>'
                   f'<div style="{FB}font-size:14px;line-height:22px;color:{BODY};">{d}</div></td></tr>')
    out.append('</table>')
    return ''.join(out)


def split(we, you):
    def col(title, tag, items, bg, mark, mc, cls):
        lis = ''.join(f'<tr><td width="22" valign="top" style="padding:0 0 10px 0;{FB}font-size:14px;line-height:21px;font-weight:700;color:{mc};">{mark}</td>'
                      f'<td valign="top" style="padding:0 0 10px 0;"><div style="{FB}font-size:14px;line-height:21px;font-weight:600;color:{INK};">{t}</div>'
                      + (f'<div style="{FB}font-size:13px;line-height:20px;color:{BODY};">{d}</div>' if d else '') + '</td></tr>' for t, d in items)
        return (f'<td class="stack {cls}" width="50%" valign="top" style="padding:0;">'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};border-radius:14px;border-collapse:separate;background-color:{bg};" bgcolor="{bg}"><tr><td style="padding:20px 20px 10px 20px;">'
                f'<div style="{FB}font-size:11px;line-height:15px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;color:{mc};padding-bottom:6px;">{tag}</div>'
                f'<div style="{FH}font-size:17px;line-height:23px;font-weight:800;color:{INK};padding-bottom:14px;">{title}</div>'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{lis}</table></td></tr></table></td>')
    return ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            + col('What TechNext does', 'Our part', we, '#FFFFFF', '&#10003;', BLUE, 'gapr')
            + '<td class="stack" width="14" style="font-size:0;line-height:0;">&nbsp;</td>'
            + col('What stays with you', 'Your part', you, ALT, '&rarr;', AMB, '')
            + '</tr></table>')


YOU = [('You file at your RDO', 'In person or by email. The decision is the BIR&rsquo;s.'),
       ('You register your books in ORUS', 'Every year. We prepare the exports from Odoo.'),
       ('Your accountant confirms coverage', 'Which rules apply to you and from when.')]


# ---------------------------------------------------------------- the five emails
E = {}
E['01-cas-registered'] = dict(
    n=39, camp='ncr_cas_registered', subject='5 Day Express BIR CAS Set-up: is your system registered?',
    pre='Our 5 Day Express BIR CAS Set-up*, as quick as 5 days. The BIR registers your business&rsquo;s use of a system at your RDO, not a software brand. Here is what that means for you.',
    h1=f'Is your accounting system {hl("registered with the BIR")}?',
    lead=('If you are not sure, start there. The BIR registers your business&rsquo;s <b>use</b> of a system at your Revenue District Office (RDO). '
          'It does not register a software brand, so buying &ldquo;registered&rdquo; software is not the same as being registered.'),
    win=('Odoo &middot; Accounting', [('Journal entries', 'Posted and locked', 'ok'), ('Audit trail', 'Every change logged', 'ok'),
                                       ('Invoice numbers', 'System-generated', 'ok'), ('Book of Accounts', 'CAS and CBA', 'blue')]),
    body=lambda: eyebrow('At a glance') + h2('BIR CAS registration in four lines', 16) + facts([
        ('What a CAS is', 'A system that records your transactions, generates your invoices and produces your books of accounts and BIR reports.'),
        ('What you register', 'Your business&rsquo;s use of a system, at your own RDO. Head office and branches each count.'),
        ('Who decides', 'Your RDO, after it reviews your application.'),
        ('Every year', 'Computerised books are registered online in ORUS. For 2026 books: by 30 January 2027 (calendar-year taxpayers).')]),
    we=[('Map your registration path', 'CAS or CBA, head office and branches, any old Permit to Use.'),
        ('Connect your current system', 'By API, daily batch or flat file. Your POS or accounting software stays.'),
        ('Set up Odoo for BIR requirements', 'Audit trail, locked entries, invoice series, user roles.'),
        ('Prepare your samples with you', 'Invoices, books, reports and the audit trail printout.')],
    read=('How BIR CAS set-up works', '/bir-cas'))

E['02-cas-or-cba'] = dict(
    n=40, camp='ncr_cas_or_cba', subject='5 Day Express BIR CAS Set-up: CAS or CBA for your business?',
    pre='Our 5 Day Express BIR CAS Set-up*, as quick as 5 days. One question decides it: does your system issue your invoices? The two options side by side.',
    h1=f'CAS or CBA: {hl("which one")} does your business need?',
    lead=('It comes down to your invoices. RMO 9-2021 draws the line there: if your system issues them, it is a CAS. '
          'If invoices are issued by hand, the system counts as a CBA.'),
    win=('Registration path', [('Invoices issued by the system', 'CAS', 'blue'), ('Invoices issued by hand', 'CBA', 'amb'),
                               ('Large taxpayer', 'CAS required', 'blue'), ('Odoo Online or Odoo.sh', 'Joint sworn statement', 'mut')]),
    body=lambda: eyebrow('Side by side') + h2('The two options', 16) + compare(
        ['CAS<br><span style="font-weight:500;font-size:12px;">Computerized Accounting System</span>', 'CBA<br><span style="font-weight:500;font-size:12px;">Computerized Books of Accounts</span>'],
        [('What it covers', 'The full cycle, from the transaction and the invoice to the financial reports', 'Books of accounts only: journals, ledger, sales and purchase books, inventory book'),
         ('Invoices', 'System-generated', 'Issued manually'),
         ('Who must use it', 'Large taxpayers (RR 9-2009, restated in RMO 9-2021)', 'Optional for non-large taxpayers, who may choose a CAS or a CBA'),
         ('Cloud set-ups', 'Registered too. Odoo Online or Odoo.sh needs a joint sworn statement with the provider that the system cannot suppress sales.')]),
    we=[('CAS or CBA', 'Which one fits how you invoice and keep your books today.'),
        ('Head office and branches', 'Affiliates and branches register separately, even on a shared system.'),
        ('Any old Permit to Use', 'A PTU stays valid unless it is revoked or the system has a major enhancement.'),
        ('Connect, do not replace', 'Your current software stays; we connect it by API, batch or flat file.')],
    read=('Read the CAS and CBA guide', '/blog/register-odoo-cas-cba-bir'))

E['03-cas-rdo-checks'] = dict(
    n=41, camp='ncr_cas_rdo_checks', subject='5 Day Express BIR CAS Set-up: would you pass the RDO’s checks?',
    pre='Our 5 Day Express BIR CAS Set-up*, as quick as 5 days. The RDO evaluates your system after it registers it, against Annex B of RMC 5-2021. See the checklist first.',
    h1=f'Would your system {hl("pass the RDO&rsquo;s checks")}?',
    lead=('Worth knowing before you file. The RDO evaluates your system <b>after</b> registration, using the requirements in Annex B of RMC 5-2021. '
          'If it finds gaps, it can revoke the registration. So look at the list first.'),
    win=('Annex B &middot; sample items', [('Audit trail', 'Printable, protected', 'ok'), ('Posted entries', 'Voided, never edited', 'ok'),
                                            ('Report headers', 'TIN + branch code', 'ok'), ('Backups', 'Kept 10 years', 'blue')]),
    body=lambda: eyebrow('What the RDO looks at') + h2('A sample of the requirements checklist', 16) + checks(
        ['Audit trail, printable and protected', 'Posted entries voided, never edited', 'System-generated invoice numbers', 'User stamp on every record',
         'Report headers with TIN and branch code', 'CSV or DAT exports; 2306, 2307, 2316', 'Unique user IDs and logged changes', 'Backups kept for ten years'],
        title='CAS requirements checklist (sample)')
        + '<div style="height:28px;line-height:28px;font-size:0;">&nbsp;</div>' + h2('What Odoo 20 already has', 14, 19, 25) + facts([
            ('Audit trail', 'Logs changes to accounting records'),
            ('Locked entries', 'Posted entries secured with a hash chain, plus irreversible hard lock dates'),
            ('Books and invoices', 'A Book of Accounts for CAS and CBA; Philippine invoices updated for BIR and CAS requirements'),
            ('Reports', '2307, SLSP, SAWT, QAP and the 2550Q summary, from the Philippine localisation')])
        + p('Whether a set-up meets every item depends on its configuration and hosting. We review that with you before you apply; the RDO makes the evaluation.', 0, 13, 21, MUTED).replace('margin:0 0 0px', 'margin:14px 0 0'),
    we=[('Annex B, item by item', 'Checked against your configuration and hosting.'),
        ('Invoice layout and series', 'Six running digits, your control number, &ldquo;REPRINT&rdquo; on copies.'),
        ('Users and report headers', 'Roles, password rules, headers with TIN, branch code and software version.'),
        ('Backups', 'A plan that keeps your records for ten years.')],
    read=('See the full CAS checklist', '/bir-cas'))

E['04-cas-application'] = dict(
    n=42, camp='ncr_cas_application', subject='5 Day Express BIR CAS Set-up: what goes into your application?',
    pre='Our 5 Day Express BIR CAS Set-up*, as quick as 5 days. Five items, from Annex A of RMC 5-2021. Every sample comes from the system you will actually run.',
    h1=f'What goes into a {hl("CAS application")}?',
    lead=('Five items, listed in Annex A of RMC 5-2021. Every sample should come from the system you will actually use, '
          'so what the RDO sees is what you run.'),
    win=('CAS application &middot; 5 items', [('Sworn statement', 'Drafted with you', 'blue'), ('Sample invoices', 'From Odoo', 'ok'),
                                              ('Books and reports', 'From Odoo', 'ok'), ('Audit trail printout', 'From Odoo', 'ok'), ('Signed checklist', 'Your RDO&rsquo;s template', 'amb')]),
    body=lambda: eyebrow('The application checklist') + h2('The five items in Annex A', 18) + steps([
        ('A sworn statement', 'Or a joint sworn statement for a cloud or outsourced system, describing the system, your invoices and the reports it produces.'),
        ('Sample invoices', 'Printouts of your invoices and supplementary documents, as the system generates them.'),
        ('Sample books and reports', 'Your books of accounts and the other system reports.'),
        ('An audit trail printout', 'Printed from the system, showing who did what and when.'),
        ('The signed requirements checklist', 'The Annex B requirements. Ask your RDO for its current templates, as annex labels differ between issuances.')]),
    we=[('Samples from your Odoo', 'Invoices, books and reports printed from the system you will run.'),
        ('Audit trail and system description', 'Prepared with you, with the sample printouts.'),
        ('On call for the RDO', 'We answer the technical questions about the set-up.'),
        ('Sample BIR reports', '2307, SLSP, QAP, SAWT and 2550Q layouts to show you the outputs.')],
    read=('Download sample BIR reports (PDF)', '/assets/docs/technext-sample-bir-reports.pdf'))

E['05-bir-accredited'] = dict(
    n=43, camp='ncr_bir_accredited', subject='5 Day Express BIR CAS Set-up: is your software really “BIR-accredited”?',
    pre='Our 5 Day Express BIR CAS Set-up*, as quick as 5 days. No software is BIR-accredited. What to look for instead before you register.',
    h1=f'Was your software sold as {hl("&ldquo;BIR&#8209;accredited&rdquo;")}?',
    lead=('Be careful with that claim. The BIR registers your business&rsquo;s use of a system. '
          'It does not approve software brands, and it has said so in public.'),
    win=('Claim check', [('&ldquo;BIR-accredited software&rdquo;', 'Not a BIR category', 'amb'), ('Your use of the system', 'Registered at your RDO', 'blue'),
                         ('Annex B requirements', 'Checked item by item', 'ok'), ('Samples for your RDO', 'From your own set-up', 'ok')]),
    body=lambda: eyebrow('The short answer') + h2('No software is BIR-accredited', 16) + facts([
        ('What the BIR registers', 'Your business&rsquo;s use of a system. Not a software brand.'),
        ('14 September 2026', 'In a public advisory, the BIR said it has not accredited, certified or endorsed any e-invoicing service provider, and warned against claims such as &ldquo;BIR-accredited&rdquo;.'),
        ('RMC 110-2026', 'Dated 12 October 2026. It sets accreditation rules for e-invoicing service providers. No list had been published when we wrote this.')], 160)
        + '<div style="height:28px;line-height:28px;font-size:0;">&nbsp;</div>' + h2('What to ask instead', 14, 19, 25) + checks([
            'Does it meet the Annex B requirements: audit trail, posted entries voided and never edited, system-generated invoice numbers, user stamps, report headers, exports, unique user IDs, backups?',
            'Can it produce the sample invoices, books, reports and audit trail your RDO asks for?',
            'Will <b>your</b> business register its own use of the system at your RDO?'], bg=BLUE05),
    we=[('Set Odoo up for BIR requirements', 'Checked against Annex B for your configuration and hosting.'),
        ('Prepare your samples with you', 'Invoices, books, reports and the audit trail printout.'),
        ('Connect what you already use', 'Your current software stays; no system swap.'),
        ('Say plainly what we are', 'An Odoo Ready Partner. Not the BIR, and not acting for it.')],
    read=('BIR rules for your accounting system', '/blog/bir-rules-for-your-accounting-system'))


# ---------------------------------------------------------------- shell
HEAD = '''<!doctype html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting"><meta name="format-detection" content="telephone=no,address=no,email=no,date=no">
<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">
<title>{title}</title>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap');
:root{{color-scheme:light;supported-color-schemes:light;}}
body,table,td,div,p,a{{-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}
table,td{{mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;}}
img{{-ms-interpolation-mode:bicubic;border:0;height:auto;line-height:100%;outline:none;text-decoration:none;display:block;}}
a{{text-decoration:none;}} .lnk:hover{{text-decoration:underline !important;}}
@media only screen and (max-width:620px){{
 .wrap{{width:100% !important;max-width:100% !important;}}
 .pad{{padding-left:20px !important;padding-right:20px !important;}}
 .stack{{display:block !important;width:100% !important;max-width:100% !important;}}
 .gapr{{padding-bottom:14px !important;}}
 .lbl{{padding-bottom:0 !important;border-bottom:0 !important;}}
 .h1{{font-size:28px !important;line-height:35px !important;}}
 .h2{{font-size:20px !important;line-height:27px !important;}}
 .btn{{width:100% !important;}} .btn a{{display:block !important;text-align:center !important;}}
 .stat{{font-size:24px !important;}}
 .chip{{display:block !important;padding:2px 0 !important;}}
}}
</style>
</head>
<body style="margin:0;padding:0;background-color:#F3F5FA;" bgcolor="#F3F5FA">
'''


def build(slug, d):
    camp = d['camp']
    book = u(BOOK, 'cta', camp)
    o = [HEAD.format(title=html.escape(d['subject']) + ' &middot; TechNext'),
         f'<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#F3F5FA;opacity:0;">{d["pre"]}' + '&#847; &zwnj; &nbsp; ' * 40 + '</div>',
         '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F3F5FA" style="background-color:#F3F5FA;"><tr><td align="center" style="padding:24px 10px 32px 10px;">',
         '<!--[if mso]><table role="presentation" width="640" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->',
         f'<table role="presentation" class="wrap" width="640" cellpadding="0" cellspacing="0" border="0" style="width:640px;max-width:640px;background-color:#FFFFFF;border-radius:16px;border-collapse:separate;overflow:hidden;" bgcolor="#FFFFFF">']
    # header
    o.append(f'<tr><td class="pad" style="padding:22px 36px;border-bottom:1px solid {LINE};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
             f'<td valign="middle"><a href="{u("/", "logo", camp)}"><img src="{ASSET}/logo-blue-on-white.png" width="132" alt="TechNext" style="width:132px;height:auto;"></a></td>'
             f'<td valign="middle" align="right" style="{FB}font-size:12px;line-height:16px;"><a class="lnk" href="{{{{ mirror }}}}" style="color:{MUTED};">View in browser</a></td></tr></table></td></tr>')
    # deadline strip
    chips = ''.join(f'<span class="chip" style="display:inline-block;padding:0 14px 0 0;"><b style="color:{INK};">{a}</b> by <b style="color:#B4321F;">{b}</b></span>' for a, b in DEADLINES)
    o.append(f'<tr><td class="pad" bgcolor="{AMB05}" style="background-color:{AMB05};padding:12px 36px;border-bottom:1px solid #F1E3C4;{FB}font-size:13px;line-height:20px;color:{AMB};">'
             f'<span style="font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:11px;color:{AMB};padding-right:12px;">BIR deadlines</span>{chips}</td></tr>')
    # hero
    o.append(row(eyebrow(f'5 Day Express &middot; BIR CAS Set-up')
                 + f'<h1 class="h1" style="margin:0 0 16px 0;{FH}font-size:32px;line-height:40px;font-weight:800;letter-spacing:-.4px;color:{INK};mso-line-height-rule:exactly;">{d["h1"]}</h1>'
                 + p(d['lead'], 14, 16, 26)
                 + p(f'With our <b style="color:{INK};">{OFFER}*</b>, we set Odoo up for BIR CAS requirements as a plug-in to your current system, as quick as 5 days.', 22, 16, 26)
                 + button(CTA, book)
                 + p(CTA_NOTE, 0, 13, 20, MUTED).replace('margin:0 0 0px', 'margin:12px 0 0'), 38, BLUE05.replace('#EAF0FB', '#F5F8FD'), 34))
    # sample window
    o.append(row(window(*d['win']), 0, '#F5F8FD', 16))
    o.append(row(offer_card(), 0, '#F5F8FD', 36))
    # topic body
    o.append(row(d['body'](), 40))
    # split
    o.append(row(eyebrow('Inside the 5 Day Express') + h2('We set it up with you. You file.', 18) + split(d['we'], YOU), 40))
    # proof
    cells = ''.join(f'<td width="33%" align="center" valign="top" style="padding:18px 6px;{"border-left:1px solid " + LINE + ";" if i else ""}">'
                    f'<div class="stat" style="{FH}font-size:28px;line-height:34px;font-weight:800;color:{BLUE};">{a}</div>'
                    f'<div style="{FB}font-size:12px;line-height:17px;color:{BODY};">{b}</div></td>' for i, (a, b) in enumerate(PROOF))
    o.append(row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};border-radius:14px;border-collapse:separate;"><tr>{cells}</tr></table>', 32))
    # read link
    rl, rp = d['read']
    o.append(row(p(f'Want to read first? <a class="lnk" href="{u(rp, "read", camp)}" style="color:{BLUE};font-weight:600;">{rl}&nbsp;&rarr;</a>', 0, 14, 22), 24))
    # CTA band
    band = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BLUE}" style="background-color:{BLUE};background-image:linear-gradient(135deg,{BLUE} 0%,{BLUE7} 100%);border-radius:16px;border-collapse:separate;">'
            f'<tr><td style="padding:32px 30px;">'
            + eyebrow('Not sure where you stand?', '#CFE0FF')
            + h2(f'Start your {OFFER}*', 10, 22, 29, '#FFFFFF')
            + p('It starts with a 15-minute Technical Readiness Call. A BIR CAS adviser goes through how you invoice and keep your books today, and plans your 5 Day Express around it. Your current system stays.', 20, 15, 24, '#E3ECFB')
            + button(CTA, book, light=True)
            + p(f'Prefer email? Reply to this message or write to <a class="lnk" href="mailto:{MAIL}" style="color:#FFFFFF;font-weight:600;">{MAIL}</a>.', 0, 13, 20, '#CFE0FF').replace('margin:0 0 0px', 'margin:14px 0 0')
            + '</td></tr></table>')
    o.append(row(band, 32, '#FFFFFF', 36))
    # footer
    soc = ''.join(f'<a href="{h}" style="display:inline-block;margin-right:8px;"><img src="{SIG}/{k}.png" width="24" height="24" alt="{a}" style="width:24px;height:24px;"></a>' for k, h, a in SOCIAL)
    offices = '<br>'.join(f'<b style="color:{INK};">{a}:</b> {b}' for a, b in OFFICES)
    o.append(f'<tr><td class="pad" bgcolor="{ALT}" style="background-color:{ALT};padding:28px 36px 30px 36px;border-top:1px solid {LINE};{FB}font-size:12px;line-height:19px;color:{BODY};">'
             f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
             f'<td class="stack" valign="top"><img src="{ASSET}/logo-blue-on-white.png" width="110" alt="TechNext" style="width:110px;height:auto;margin-bottom:10px;">'
             f'<p style="margin:0 0 10px 0;">{OFFER}, with Odoo.</p><p style="margin:0 0 10px 0;">{offices}</p>'
             f'<p style="margin:0;"><a class="lnk" href="mailto:{MAIL}" style="color:{BLUE};">{MAIL}</a> &middot; <a class="lnk" href="{u("/", "footer", camp)}" style="color:{BLUE};">technext.asia</a></p></td>'
             f'<td class="stack" valign="top" align="right" style="padding-top:4px;">{soc}</td></tr></table>'
             f'<p style="margin:20px 0 8px 0;padding-top:18px;border-top:1px solid {LINE};color:{MUTED};">{WHY_YOU}</p>'
             f'<p style="margin:0 0 8px 0;color:{MUTED};">{STAR}</p>'
             f'<p style="margin:0 0 8px 0;color:{MUTED};">{DISCLAIMER}</p>'
             f'<p style="margin:0 0 12px 0;color:{MUTED};">{LEGAL}</p>'
             f'<p style="margin:0;"><a class="lnk" href="{{{{ unsubscribe }}}}" style="color:{BODY};text-decoration:underline;">Unsubscribe</a> &nbsp;&middot;&nbsp; '
             f'<a class="lnk" href="{SITE}/privacy" style="color:{BODY};text-decoration:underline;">Privacy policy</a></p></td></tr>')
    o.append('</table><!--[if mso]></td></tr></table><![endif]--></td></tr></table>\n</body>\n</html>\n')
    return '\n'.join(o)


def text(d):
    camp = d['camp']
    book = plain(u(BOOK, 'cta', camp))
    body_txt = plain(re.sub(r'</(p|h2|tr|div)>', '\n', d['body']()))
    t = [plain(d['pre']), '', 'BIR deadlines: ' + ' | '.join(f'{a} by {b}' for a, b in DEADLINES), '',
         OFFER.upper() + '*', '', plain(d['h1']).upper(), '', plain(d['lead']), '', f'With our {OFFER}*, we set Odoo up for BIR CAS requirements as a plug-in to your current system, as quick as 5 days.', '', f'{CTA}: {book}', plain(CTA_NOTE), '',
         'Starting today | As quick as 5 days* | Your system stays', '', body_txt, '', 'INSIDE THE 5 DAY EXPRESS: WHAT TECHNEXT DOES'] + [f'- {plain(a)}: {plain(b)}' for a, b in d['we']] + \
        ['', 'WHAT STAYS WITH YOU'] + [f'- {plain(a)}: {plain(b)}' for a, b in YOU] + \
        ['', ' | '.join(f'{a} {b}' for a, b in PROOF), '', f'Want to read first? {plain(d["read"][0])}: {plain(u(d["read"][1], "read", camp))}', '',
         f'Start your {OFFER}*. It starts with a 15-minute Technical Readiness Call: {book}', f'Prefer email? Reply or write to {MAIL}.', '', '--',
         f'TechNext - {OFFER}, with Odoo'] + [f'{a}: {b}' for a, b in OFFICES] + \
        [MAIL + ' | technext.asia', '', plain(WHY_YOU), plain(STAR), plain(DISCLAIMER), plain(LEGAL), '', 'View in browser: {{ mirror }}', 'Unsubscribe: {{ unsubscribe }}']
    out = '\n'.join(t)
    return re.sub(r'\n{3,}', '\n\n', out) + '\n'


BANNED = [r'\bfixed\b', r'\bERP\b', r'six sigma', r'\bagile\b', r'\blean\b', r'\bday [1-5]\b', r'coffee', r'BIR-ready', r'guarantee', r'three working days',
          r'gave TechNext', r'\bhandled\b', r'world-class', r'\bfree\b', r'30-minute', r'Acknowledgement Certificate']

if __name__ == '__main__':
    OUT_H.mkdir(parents=True, exist_ok=True); OUT_T.mkdir(parents=True, exist_ok=True)
    bad = 0
    for slug, d in E.items():
        h, t = build(slug, d), text(d)
        (OUT_H / f'{slug}.html').write_text(h, encoding='utf-8', newline='\n')
        (OUT_T / f'{slug}.txt').write_text(t, encoding='utf-8', newline='\n')
        vis = plain(re.sub(r'(?s)<style.*?</style>|<!--.*?-->', '', h))
        for pat in BANNED:
            for m in re.finditer(pat, vis, re.I):
                bad += 1; print(f'  BANNED {slug}: {pat!r} -> ...{vis[max(0, m.start() - 40):m.end() + 40]}...')
        n5 = len(__import__('re').findall(r'5 Day Express', vis)); nt = t.count('5 Day Express')
        if n5 < 5 or nt < 5 or '5 Day Express' not in d['subject']: bad += 1; print(f'  LOW 5 DAY EXPRESS {slug}: html {n5}, text {nt}')
        print(f'{slug}: html {len(h.encode()) // 1024} KB, text {len(t)} chars, 5 Day Express x{n5} (text x{nt}) | {d["subject"]}')
    print('banned hits:', bad)
