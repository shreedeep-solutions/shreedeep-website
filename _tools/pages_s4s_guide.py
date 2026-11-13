# -*- coding: utf-8 -*-
"""Solutions4Society user guide: /s4s-guide/ (index + one page per menu section) and the HTML used for the PDF manual."""
import json, os, re
from common import *
import s4s_manual as MAN

HERE = os.path.dirname(__file__)
INV = json.load(open(os.path.join(HERE, 's4s_inventory.json'), encoding='utf-8'))
PDF = '/downloads/S4S-User-Manual.pdf'
BASE = '/s4s-guide/'
SLUG = {'Home': 'home', 'Entries': 'entries', 'Billing': 'billing', 'Banking': 'banking', 'Members & Registers': 'members-registers',
        'Accounts & Reports': 'accounts-reports', 'Office & Settings': 'office-settings'}
BLURB = {'Home': 'Dashboard and the set-up wizard.', 'Entries': 'Receipts, payments, journals, bulk entry, notes, vendor bills, cheques.',
         'Billing': 'Bills, charges per flat, rules, collections and dues follow-up.', 'Banking': 'Statement upload with automatic head sorting, BRS, cheque deposit, cash and bank books.',
         'Members & Registers': 'Members, transfers, I / J / Share / Nomination registers, KYC, member app, committee, tenants, vendors.',
         'Accounts & Reports': 'Ledgers, final accounts, registers, budgets, GST, TDS, income-tax, FDs, fixed assets, audit tools, heads and opening balances.',
         'Office & Settings': 'Year-end, meetings, notices, complaints, gate, compliance, team, audit trail, backup and settings.'}


def btn_rows(p):
    out, seen = [], set()
    for t, ti in p['btns']:
        if t.startswith(MAN.COMMON_SKIP) or t in seen:
            continue
        seen.add(t)
        why = MAN.BTN.get(t) or ti or ''
        if not why and t.startswith('🖨'):
            why = 'Print / save as PDF.'
        out.append((t, why))
    return out


def missing():
    return sorted({t for _, L in INV for p in L for t, w in btn_rows(p) if not w})


def screen_html(p, h='h3'):
    steps = MAN.STEPS.get(p['id'], [])
    rows = btn_rows(p)
    s = ['<div class="g-scr" id="%s">' % p['id'], '<%s>%s %s</%s>' % (h, p['ic'], esc(p['nm']), h)]
    if p['help']:
        s.append('<p class="g-what">%s</p>' % esc(p['help']))
    if p['mr']:
        s.append('<p class="g-mr" lang="mr">%s</p>' % esc(p['mr']))
    if steps:
        s.append('<div class="g-lbl">Step by step</div><ol class="g-steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in steps))
    if rows:
        s.append('<div class="g-lbl">Buttons on this screen</div><table class="g-btns"><tbody>%s</tbody></table>' % ''.join(
            '<tr><td class="g-b">%s</td><td>%s</td></tr>' % (esc(t), esc(w)) for t, w in rows))
    s.append('</div>')
    return '\n'.join(s)


def common_html():
    return '<table class="g-btns"><tbody>%s</tbody></table>' % ''.join('<tr><td class="g-b">%s</td><td>%s</td></tr>' % (esc(a), esc(b)) for a, b in MAN.COMMON)


def keys_html():
    return '<table class="g-btns"><tbody>%s</tbody></table>' % ''.join('<tr><td class="g-b"><kbd>%s</kbd></td><td>%s</td></tr>' % (esc(a), esc(b)) for a, b in MAN.SHORTCUTS)


def routine_html():
    return '<ol class="g-steps">%s</ol>' % ''.join('<li><b>%s</b><ul>%s</ul></li>' % (esc(h), ''.join('<li>%s</li>' % x for x in L)) for h, L in MAN.ROUTINE)


def roles_html(h='h3'):
    return '\n'.join('<div class="g-scr"><%s>%s</%s><ul class="g-list">%s</ul></div>' % (h, esc(t), h, ''.join('<li>%s</li>' % x for x in L)) for t, L in MAN.ROLES)


def intro_html(h='h3'):
    return '\n'.join('<div class="g-scr"><%s>%s</%s>%s</div>' % (h, esc(t), h, ''.join('<p>%s</p>' % x for x in L)) for t, L in MAN.INTRO)


def toc_html(cur=None):
    li = ['<li><a href="%s"%s>Getting started</a></li>' % (BASE, ' class="on"' if cur == 'start' else '')]
    for sec, L in INV:
        li.append('<li><a href="%s%s.html"%s>%s</a></li>' % (BASE, SLUG[sec], ' class="on"' if cur == sec else '', esc(sec)))
    li.append('<li><a href="%sroles.html"%s>Member, committee, security &amp; vendor</a></li>' % (BASE, ' class="on"' if cur == 'roles' else ''))
    li.append('<li><a href="%s">📥 Download the PDF manual</a></li>' % PDF)
    return '<div class="g-toc" role="navigation" aria-label="Guide contents"><div class="g-lbl">User guide</div><ol>%s</ol></div>' % ''.join(li)


def layout(cur, inner):
    return '<section class="section"><div class="container g-wrap">%s<div class="g-main prose">%s</div></div></section>' % (toc_html(cur), inner)


def s4s_guide():
    pages = []
    n_scr = sum(len(L) for _, L in INV)
    crumbs0 = [('Our Software', '/software.html'), ('S4S User Guide', BASE)]
    # index
    body = hero(crumbs0, 'file', 'Solutions4Society · version %s' % MAN.VERSION, 'Solutions4Society <em>User Guide</em>',
                'Every screen and every button of our society accounting software, explained step by step — %d screens, for accountants, committee members, members and security staff.' % n_scr, buttons=False)
    cards_ = ''.join('<a class="card" href="%s%s.html"><h3>%s</h3><p>%s</p><p class="small">%d screens →</p></a>' % (BASE, SLUG[s], esc(s), esc(BLURB[s]), len(L)) for s, L in INV)
    cards_ += '<a class="card" href="%sroles.html"><h3>Other roles</h3><p>Member app, committee, security guard, vendor and auditor.</p><p class="small">5 roles →</p></a>' % BASE
    inner = ('<p class="g-dl"><a class="btn btn-maroon" href="%s">📥 Download the complete manual (PDF)</a></p>' % PDF +
             '<h2>Getting started</h2>' + intro_html() +
             '<h2 id="routine">Your monthly routine</h2>' + routine_html() +
             '<h2 id="sections">Screens, by menu section</h2><div class="grid-3 g-cards">%s</div>' % cards_ +
             '<h2 id="common">Buttons you see on every screen</h2>' + common_html() +
             '<h2 id="keys">Keyboard shortcuts</h2>' + keys_html() +
             '<h2 id="faq">Common questions</h2>' + faq_html(MAN.FAQ))
    body += '\n' + layout('start', inner)
    body += '\n' + cta('Want Your Society on Solutions4Society?', 'We set it up, bring across your old data and keep the books for you.')
    pages.append((BASE, page(BASE, 'Solutions4Society User Guide — Society Accounting Software | Shreedeep Solutions',
                             'Step-by-step guide to Solutions4Society: billing, receipts, bank statement upload, BRS, member ledgers, final accounts, year-end, member app and security app. Free PDF manual.',
                             body, crumbs0, faqs=MAN.FAQ, article={'published': '2026-11-13'})))
    # one page per section
    for sec, L in INV:
        path = '%s%s.html' % (BASE, SLUG[sec])
        crumbs = crumbs0 + [(sec, path)]
        b = hero(crumbs, 'file', 'S4S User Guide', esc(sec), esc(BLURB[sec]), buttons=False)
        jump = '<p class="g-jump">%s</p>' % ' · '.join('<a href="#%s">%s</a>' % (p['id'], esc(p['nm'].split(' › ')[-1].lstrip('📥📤 '))) for p in L)
        b += '\n' + layout(sec, jump + '\n'.join(screen_html(p) for p in L) + '<p class="g-note small">Buttons found on every screen (❓, ✨ AI, ⬇ Export, 🖨 Print, 🖼 Picture, 📋 Copy, ↶ History) are explained on the <a href="%s#common">guide home page</a>.</p>' % BASE)
        pages.append((path, page(path, '%s — Solutions4Society User Guide | Shreedeep Solutions' % sec,
                                 'Solutions4Society %s screens explained step by step: %s' % (sec, BLURB[sec]), b, crumbs, article={'published': '2026-11-13'})))
    path = BASE + 'roles.html'
    crumbs = crumbs0 + [('Other roles', path)]
    b = hero(crumbs, 'users', 'S4S User Guide', 'Member, committee, security &amp; vendor', 'What each of the other roles sees and how to use it.', buttons=False)
    b += '\n' + layout('roles', roles_html())
    pages.append((path, page(path, 'Member App, Committee & Security App — Solutions4Society User Guide | Shreedeep Solutions',
                             'How members, committee members, security guards, vendors and auditors use Solutions4Society.', b, crumbs, article={'published': '2026-11-13'})))
    return pages


GUIDE_CSS = '''
/* S4S user guide */
.g-wrap{display:grid;grid-template-columns:240px 1fr;gap:36px;align-items:start}
.g-toc{display:block!important;position:sticky;top:90px;max-height:calc(100vh - 110px);overflow:auto;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:16px 18px;font-size:.92rem}
.g-toc ol{display:block!important;list-style:none;margin:6px 0 0;padding:0}.g-toc li{display:block}.g-toc li{margin:4px 0}.g-toc a{color:var(--text);text-decoration:none}.g-toc a:hover,.g-toc a.on{color:var(--maroon);font-weight:700}
.g-main{min-width:0}.g-main h2{margin-top:34px}.g-lbl{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:12px 0 4px}
.g-scr{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px 22px;margin:16px 0;scroll-margin-top:90px}.g-scr h3{margin:0 0 6px}
.g-what{margin:0 0 4px}.g-mr{color:var(--muted);margin:0 0 6px}.g-steps{padding-left:22px;margin:4px 0}.g-steps li{margin:4px 0}.g-list{padding-left:20px}
.g-btns{width:100%;border-collapse:collapse;font-size:.92rem;margin:4px 0}.g-btns td{border:1px solid var(--border);padding:6px 10px;vertical-align:top}.g-btns .g-b{width:36%;font-weight:600;white-space:normal}
.g-jump{font-size:.9rem;line-height:2}.g-jump a{white-space:nowrap}.g-dl{margin:6px 0 18px}.g-cards .card p.small{color:var(--maroon);font-weight:600;margin:6px 0 0}
a.btn-maroon,.prose a.btn-maroon{color:#fff!important;text-decoration:none}a.btn-outline-d{text-decoration:none;border:2px solid var(--maroon);color:var(--maroon);background:transparent}a.btn-outline-d:hover{background:var(--maroon);color:#fff}
kbd{background:var(--bg-alt);border:1px solid var(--border);border-radius:5px;padding:1px 6px;font-size:.85rem}
@media(max-width:860px){.g-wrap{grid-template-columns:1fr;gap:16px}.g-toc{position:static}.g-scr{padding:14px 14px}.g-btns .g-b{width:42%}}
'''


def pdf_html(version_date):
    """Stand-alone HTML for the PDF (no site header / footer)."""
    css = '''@page{size:A4;margin:14mm 13mm 16mm}body{font-family:'Inter',system-ui,'Segoe UI',sans-serif;color:#222;font-size:10.5pt;line-height:1.5}
h1{color:#7D2435;font-size:26pt;margin:0}h2{color:#7D2435;font-size:16pt;border-bottom:2px solid #C9A24A;padding-bottom:4px;margin:18px 0 8px;page-break-after:avoid}
h3{font-size:12pt;margin:0 0 4px;color:#4A1521;page-break-after:avoid}.pb{page-break-before:always}.g-scr{border:1px solid #e3d8cc;border-radius:8px;padding:9px 12px;margin:8px 0;page-break-inside:avoid}
.g-what{margin:0 0 3px}.g-mr{color:#555;margin:0 0 4px}.g-lbl{font-size:7.5pt;letter-spacing:.08em;text-transform:uppercase;color:#7a6a6e;font-weight:700;margin:6px 0 2px}
.g-steps{padding-left:18px;margin:2px 0}.g-steps li{margin:2px 0}.g-btns{width:100%;border-collapse:collapse;font-size:9pt}.g-btns td{border:1px solid #ddd;padding:3px 6px;vertical-align:top}.g-btns .g-b{width:34%;font-weight:600}
.cover{height:250mm;display:flex;flex-direction:column;justify-content:center;text-align:center}.cover img{width:110px;margin:0 auto 18px}.cover p{color:#555}
.toc{columns:2;font-size:10pt}.toc li{margin:2px 0}kbd{border:1px solid #ccc;border-radius:3px;padding:0 4px;font-size:9pt}a{color:#7D2435;text-decoration:none}details summary{font-weight:700}details p{margin:2px 0 8px}
.faq details{page-break-inside:avoid}'''
    toc = '<ol class="toc"><li>Getting started</li><li>Your monthly routine</li><li>Buttons on every screen &amp; shortcuts</li>%s<li>Member, committee, security, vendor &amp; auditor</li><li>Common questions</li></ol>' % ''.join('<li>%s — %s</li>' % (esc(s), esc(BLURB[s])) for s, _ in INV)
    parts = ['<div class="cover"><img src="https://shreedeepsolutions.com/logo.jpg" alt=""><h1>Solutions4Society</h1><p style="font-size:15pt;color:#7D2435;margin:6px 0 20px">User Manual — every screen and button, step by step</p>'
             '<p>Version %s · %s</p><p>Shreedeep Solutions · D204, Shankar Sheela CHS Ltd., Sector-8, Airoli, Navi Mumbai 400708<br>+91 90042 64282 · +91 90042 62639 · shreedeepsolutions.com</p>'
             '<p style="margin-top:14px">Read online: shreedeepsolutions.com/s4s-guide/</p></div>' % (MAN.VERSION, version_date),
             '<div class="pb"></div><h2>Contents</h2>' + toc,
             '<div class="pb"></div><h2>1. Getting started</h2>' + intro_html(),
             '<h2>2. Your monthly routine</h2>' + routine_html(),
             '<div class="pb"></div><h2>3. Buttons on every screen</h2>' + common_html() + '<h2>Keyboard shortcuts</h2>' + keys_html()]
    for i, (sec, L) in enumerate(INV, 4):
        parts.append('<div class="pb"></div><h2>%d. %s</h2><p>%s</p>' % (i, esc(sec), esc(BLURB[sec])) + '\n'.join(screen_html(p) for p in L))
    n = 4 + len(INV)
    parts.append('<div class="pb"></div><h2>%d. Member, committee, security, vendor &amp; auditor</h2>' % n + roles_html())
    parts.append('<h2>%d. Common questions</h2><div class="faq">%s</div>' % (n + 1, ''.join('<details open><summary>%s</summary><p>%s</p></details>' % (esc(q), a) for q, a in MAN.FAQ)))
    return '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Solutions4Society User Manual</title><style>%s</style></head><body>%s</body></html>' % (css, '\n'.join(parts))
