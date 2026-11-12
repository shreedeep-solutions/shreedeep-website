"""Shared template for the Shreedeep Solutions sub-pages.

Run  python3 _tools/build.py  from the repo root to regenerate every generated page.
Folders that start with "_" are not published by GitHub Pages (Jekyll), so this
folder stays private to the repo.
"""
import html, json

SITE = 'https://shreedeepsolutions.com'
OG_IMAGE = SITE + '/og-image.jpg'
WA = 'https://wa.me/919004264282'

ICONS = {
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'check': '<polyline points="20 6 9 17 4 12"/>',
 'home': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
 'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'search': '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
 'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
 'briefcase': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 'calc': '<rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8" y2="11.01"/><line x1="12" y1="11" x2="12" y2="11.01"/><line x1="16" y1="11" x2="16" y2="11.01"/><line x1="8" y1="15" x2="8" y2="15.01"/><line x1="12" y1="15" x2="12" y2="15.01"/><line x1="16" y1="15" x2="16" y2="18"/><line x1="8" y1="18" x2="12" y2="18"/>',
 'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
 'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
 'monitor': '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
 'user': '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 'moon': '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
 'sun': '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>',
 'menu': '<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>',
 'wa': '<path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>',
}

def ic(name):
    return '<svg class="ic"><use href="#i-%s"/></svg>' % name

def symbols():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">\n' +
            '\n'.join('  <symbol id="i-%s" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in ICONS.items()) +
            '\n</svg>')

BUSINESS = {"@type": "AccountingService", "@id": SITE + "/#business", "name": "Shreedeep Solutions", "url": SITE + "/",
    "image": SITE + "/logo.jpg", "email": "shreedeepsolutions@gmail.com", "telephone": ["+91-9004264282", "+91-9004262639"],
    "address": {"@type": "PostalAddress", "streetAddress": "D204, Shankar Sheela CHS Ltd., Sector-8, Airoli", "addressLocality": "Navi Mumbai",
                "addressRegion": "Maharashtra", "postalCode": "400708", "addressCountry": "IN"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "09:00", "closes": "18:00"}],
    "areaServed": ["Navi Mumbai", "Thane", "Mumbai"]}

NAV = [('/', 'Home'), ('/#services', 'Services'), ('/#areas', 'Areas'), ('/guides/', 'Guides'), ('/tools.html', 'Tools'), ('/downloads.html', 'Downloads'), ('/#contact', 'Contact')]

def header(active='', lang='en'):
    items = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        items.append('      <li><a href="%s"%s>%s</a></li>' % (href, cls, label))
    if lang == 'mr':
        items.append('      <li><a href="/" lang="en">English</a></li>')
    else:
        items.append('      <li><a href="/mr/" lang="mr" hreflang="mr">मराठी</a></li>')
    est = 'मोफत अंदाज' if lang == 'mr' else 'Get Estimate'
    return '''<header>
  <nav class="container">
    <a href="/" class="brand">
      <img src="/logo.jpg" alt="Shreedeep Solutions logo" width="48" height="48">
      <span><span class="brand-name">Shreedeep Solutions</span><span class="brand-sub">Society Accounting &amp; Compliance</span></span>
    </a>
    <ul class="nav-links" id="navLinks">
%s
    </ul>
    <div class="nav-actions">
      <button class="icon-btn" id="themeBtn" aria-label="Toggle dark mode"><svg class="ic i-moon"><use href="#i-moon"/></svg><svg class="ic i-sun"><use href="#i-sun"/></svg></button>
      <a href="/#estimate" class="btn btn-maroon btn-sm nav-est">%s</a>
      <button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu"><svg class="ic"><use href="#i-menu"/></svg></button>
    </div>
  </nav>
</header>''' % ('\n'.join(items), est)

SERVICE_PAGES = [
    ('/chs-statutory-audit.html', 'Statutory Audit'),
    ('/society-management-services.html', 'Society Management'),
    ('/tds-return-housing-society.html', 'TDS Returns'),
    ('/gst-for-housing-societies.html', 'GST Returns'),
    ('/housing-society-income-tax-itr-5.html', 'Society ITR-5'),
    ('/software.html', 'Our Software'),
]
AREA_PAGES = [
    ('/society-accountant-airoli.html', 'Airoli'),
    ('/housing-society-accounting-navi-mumbai.html', 'Navi Mumbai'),
    ('/housing-society-accounting-thane.html', 'Thane'),
    ('/housing-society-accounting-mumbai.html', 'Mumbai'),
    ('/mr/', 'मराठी'),
]
RESOURCE_PAGES = [
    ('/guides/', 'Guides'),
    ('/tools.html', 'Free Calculators'),
    ('/downloads.html', 'Free Templates'),
    ('/#calendar', 'Due Dates Calendar'),
]

def _col(title, links):
    return '    <div>\n      <h4>%s</h4>\n      <ul>\n%s\n      </ul>\n    </div>' % (
        title, '\n'.join('        <li><a href="%s">%s</a></li>' % l for l in links))

def footer():
    return '''<footer>
  <div class="container f-grid f-grid-5">
    <div>
      <div class="f-brand"><img src="/logo.jpg" alt="Shreedeep Solutions logo" width="54" height="54"><b>Shreedeep Solutions</b></div>
      <p class="f-tag">Your Success = Our Accuracy + Efforts + Integrity + Trust</p>
      <ul class="f-contact">
        <li><a href="tel:+919004264282">+91 90042 64282</a></li>
        <li><a href="tel:+919004262639">+91 90042 62639</a></li>
        <li><a href="mailto:shreedeepsolutions@gmail.com">shreedeepsolutions@gmail.com</a></li>
        <li>D204, Shankar Sheela CHS Ltd., Sector-8, Airoli, Navi Mumbai – 400708</li>
      </ul>
    </div>
%s
%s
%s
  </div>
  <div class="f-bottom">© <span id="year">2026</span> Shreedeep Solutions. All rights reserved.</div>
</footer>''' % (_col('Services', SERVICE_PAGES), _col('Areas We Serve', AREA_PAGES), _col('Resources', RESOURCE_PAGES))

MBAR = '''<div class="mbar"><div class="mbar-in">
  <a class="mb-call" href="tel:+919004264282"><svg class="ic"><use href="#i-phone"/></svg>Call</a>
  <a class="mb-wa" href="https://wa.me/919004264282" target="_blank" rel="noopener"><svg class="ic"><use href="#i-wa"/></svg>WhatsApp</a>
  <a class="mb-est" href="/#estimate">Get Estimate</a>
</div></div>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">'''

def esc(s):
    return html.escape(s, quote=True)

def page(path, title, desc, body, crumbs, graph_extra=(), lang='en', alternates=None, active='', scripts='', faqs=None, article=None):
    """path like '/tools.html'. crumbs: list of (name, path) after Home."""
    url = SITE + path
    graph = [BUSINESS]
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (n, p) in enumerate(crumbs, 2):
        items.append({"@type": "ListItem", "position": i, "name": n, "item": SITE + p})
    graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if faqs:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]})
    if article:
        graph.append({"@type": "Article", "headline": title.split(' | ')[0], "description": desc, "inLanguage": lang,
                      "datePublished": article['published'], "dateModified": article.get('modified', article['published']),
                      "author": {"@type": "Organization", "name": "Shreedeep Solutions", "url": SITE + "/"},
                      "publisher": {"@id": SITE + "/#business"}, "mainEntityOfPage": url, "image": OG_IMAGE})
    graph.extend(graph_extra)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(',', ':'))
    alt = ''
    if alternates:
        alt = '\n'.join('<link rel="alternate" hreflang="%s" href="%s">' % (h, SITE + p) for h, p in alternates) + '\n'
    return '''<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
%(alt)s<meta name="theme-color" content="#7D2435">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/favicon.png">
<meta property="og:type" content="%(ogtype)s">
<meta property="og:site_name" content="Shreedeep Solutions">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(og)s">
<meta property="og:url" content="%(url)s">
<meta name="twitter:card" content="summary_large_image">
%(fonts)s
<link rel="stylesheet" href="/style.css">
<script>try{if(localStorage.getItem('ss-theme')==='dark')document.documentElement.setAttribute('data-theme','dark');}catch(e){}</script>
<script type="application/ld+json">%(ld)s</script>
</head>
<body>

%(sym)s

%(header)s

%(body)s

%(footer)s

%(mbar)s

<script src="/site.js"></script>
%(scripts)s</body>
</html>
''' % dict(lang=lang, title=esc(title), desc=esc(desc), url=url, alt=alt, og=OG_IMAGE, fonts=FONTS, ld=ld,
           sym=symbols(), header=header(active, lang), body=body, footer=footer(), mbar=MBAR, scripts=scripts,
           ogtype='article' if article else 'website')

import re
def strip_tags(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

def hero(crumbs, eyebrow_icon, eyebrow, h1, lead, buttons=True, trust=None, wa_text='Hello Shreedeep Solutions, I am enquiring for our housing society.'):
    c = ' › '.join(['<a href="/">Home</a>'] + ['<a href="%s">%s</a>' % (p, esc(n)) for n, p in crumbs[:-1]] + [esc(crumbs[-1][0])])
    btns = ''
    if buttons:
        from urllib.parse import quote
        btns = '''    <div class="hero-btns">
      <a href="/#estimate" class="btn btn-gold">Get Free Estimate</a>
      <a href="tel:+919004264282" class="btn btn-outline">%s Call +91 90042 64282</a>
      <a href="%s?text=%s" target="_blank" rel="noopener" class="btn btn-wa">%s WhatsApp</a>
    </div>''' % (ic('phone'), WA, quote(wa_text), ic('wa'))
    tr = ''
    if trust:
        tr = '    <div class="trust">\n%s\n    </div>' % '\n'.join('      <span>%s%s</span>' % (ic('check'), t) for t in trust)
    return '''<section class="hero">
  <div class="container">
    <div class="crumbs">%s</div>
    <span class="eyebrow">%s %s</span>
    <h1>%s</h1>
    <p class="lead">%s</p>
%s
%s
  </div>
</section>''' % (c, ic(eyebrow_icon), eyebrow, h1, lead, btns, tr)

def section(kicker, h2, inner, alt=False, sid=None, sub=None):
    return '''<section class="section%s"%s>
  <div class="container">
    <div class="sec-head">
      <span class="kicker">%s</span>
      <h2>%s</h2>%s
      <div class="divider"></div>
    </div>
%s
  </div>
</section>''' % (' alt' if alt else '', ' id="%s"' % sid if sid else '', kicker, h2, '\n      <p>%s</p>' % sub if sub else '', inner)

def cards(items):
    """items: (icon, title, text, href or None)"""
    out = []
    for icon, t, p, href in items:
        tag = ('<a class="card" href="%s">' % href) if href else '<div class="card">'
        end = '</a>' if href else '</div>'
        out.append('      %s<div class="s-icon">%s</div><h3>%s</h3><p>%s</p>%s' % (tag, ic(icon), t, p, end))
    return '    <div class="grid-3">\n%s\n    </div>' % '\n'.join(out)

def faq_html(faqs):
    return '    <div class="faq">\n%s\n    </div>' % '\n'.join(
        '      <details><summary>%s</summary><p>%s</p></details>' % (esc(q), a) for q, a in faqs)

def cta(h2='Get a Free Estimate for Your Society', p="Tell us your society's size and the work you need. We'll send a customised quote."):
    return '''<section class="section">
  <div class="container">
    <div class="cta">
      <h2>%s</h2>
      <p>%s</p>
      <div class="hero-btns">
        <a href="/#estimate" class="btn btn-gold">Get Free Estimate</a>
        <a href="tel:+919004262639" class="btn btn-outline">%s +91 90042 62639</a>
      </div>
    </div>
  </div>
</section>''' % (h2, p, ic('phone'))

def related(links, title='Related'):
    return '''<section class="section alt">
  <div class="container">
    <div class="sec-head"><span class="kicker">%s</span><h2>Keep Reading</h2><div class="divider"></div></div>
    <div class="related">%s</div>
  </div>
</section>''' % (title, ''.join('<a href="%s">%s →</a>' % (h, t) for h, t in links))
