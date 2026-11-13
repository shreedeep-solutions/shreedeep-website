"""Regenerates every generated page, refreshes header/footer on the city pages, and rewrites sitemap.xml.
Run from the repo root:  python3 _tools/build.py
"""
import os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from pages_services import airoli, services
from pages_guides import guides
from pages_tools import tools, downloads
from pages_other import marathi, software
from pages_s4s_guide import s4s_guide, GUIDE_CSS

TODAY = datetime.date.today().isoformat()

def write(path, html_text):
    rel = path.lstrip('/')
    if rel.endswith('/'):
        rel += 'index.html'
    os.makedirs(os.path.dirname(rel) or '.', exist_ok=True)
    with open(rel, 'w', encoding='utf-8') as f:
        f.write(html_text)
    return rel

generated = [airoli()] + services() + guides() + [tools(), downloads(), marathi(), software()] + s4s_guide()
files = [write(p, h) for p, h in generated]

# user-guide styles (added once to style.css)
css = open('style.css', encoding='utf-8').read()
if '/* S4S user guide */' in css:
    css = css.split('\n/* S4S user guide */')[0].rstrip('\n') + '\n'
open('style.css', 'w', encoding='utf-8').write(css + GUIDE_CSS.lstrip('\n') if css.endswith('\n') else css + '\n' + GUIDE_CSS.lstrip('\n'))

# City pages: keep their content, refresh shared chrome
CITY = {'housing-society-accounting-navi-mumbai.html': '', 'housing-society-accounting-thane.html': '', 'housing-society-accounting-mumbai.html': ''}
for f in CITY:
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'<svg width="0" height="0" style="position:absolute" aria-hidden="true">.*?</svg>\n', symbols() + '\n', s, count=1, flags=re.S)
    s = re.sub(r'<header>.*?</header>', header(), s, count=1, flags=re.S)
    s = re.sub(r'<footer>.*?</footer>', footer(), s, count=1, flags=re.S)
    s = s.replace('<link rel="icon" type="image/jpeg" href="/logo.jpg">', '<link rel="icon" type="image/png" href="/favicon.png">\n<link rel="apple-touch-icon" href="/favicon.png">')
    s = s.replace('content="https://shreedeepsolutions.com/logo.jpg"', 'content="%s"' % OG_IMAGE)
    if 'twitter:card' not in s:
        s = s.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', '<meta name="twitter:card" content="summary_large_image">\n<link rel="preconnect" href="https://fonts.googleapis.com">', 1)
    # service cards on city pages -> real service pages
    for h3, href in [('Society Management', '/society-management-services.html'), ('Statutory Audit', '/chs-statutory-audit.html'), ('Statutory Audit &amp; Form O', '/chs-statutory-audit.html'),
                     ('TDS Returns', '/tds-return-housing-society.html'), ('GST Returns', '/gst-for-housing-societies.html'), ('Society Income Tax (ITR-5)', '/housing-society-income-tax-itr-5.html')]:
        s = re.sub(r'<a class="card" href="/#services">(<div class="s-icon">.*?</div><h3>%s</h3>)' % re.escape(h3), r'<a class="card" href="%s">\1' % href, s)
    s = s.replace('<use href="#i-user"/></svg></div><h3>Society Income Tax (ITR-5)', '<use href="#i-shield"/></svg></div><h3>Society Income Tax (ITR-5)')
    open(f, 'w', encoding='utf-8').write(s)

# Navi Mumbai page links to the Airoli page
f = 'housing-society-accounting-navi-mumbai.html'
s = open(f, encoding='utf-8').read()
if 'society-accountant-airoli.html' not in s.split('<footer>')[0]:
    s = s.replace('<p class="chips-note">', '<p class="chips-note">Based in Airoli? See our <a href="/society-accountant-airoli.html">Airoli page</a>. ', 1)
open(f, 'w', encoding='utf-8').write(s)

# Sitemap
urls = ['/', '/mr/', '/society-accountant-airoli.html'] + [p for p, _ in AREA_PAGES[1:4]] + [p for p, _ in SERVICE_PAGES] + \
       ['/guides/'] + [g[0] for g in __import__('pages_guides').GUIDES] + ['/tools.html', '/downloads.html', '/software.html'] + [p for p, _ in s4s_guide()]
seen = []
for u in urls:
    if u not in seen:
        seen.append(u)
pri = lambda u: '1.0' if u == '/' else '0.9' if u in ('/mr/', '/society-accountant-airoli.html') or 'housing-society-accounting' in u else '0.8'
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for u in seen:
    alt = ''
    if u in ('/', '/mr/'):
        alt = ''.join('\n    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (h, SITE, p) for h, p in (('en', '/'), ('mr', '/mr/'), ('x-default', '/')))
    sm.append('  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n    <priority>%s</priority>%s\n  </url>' % (SITE, u, TODAY, pri(u), alt))
sm.append('</urlset>')
open('sitemap.xml', 'w').write('\n'.join(sm) + '\n')
open('robots.txt', 'w').write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)
print('built', len(files), 'pages;', len(seen), 'urls in sitemap')
