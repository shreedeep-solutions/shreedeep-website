"""Builds downloads/S4S-User-Manual.pdf from the same content as /s4s-guide/ (needs: pip install playwright && playwright install chromium).
Run from the repo root:  python3 _tools/make_s4s_manual_pdf.py"""
import os, sys, base64, datetime, asyncio
sys.path.insert(0, os.path.dirname(__file__))
from pages_s4s_guide import pdf_html
from playwright.async_api import async_playwright

def main():
    h = pdf_html(datetime.date.today().strftime('%d %B %Y'))
    logo = 'data:image/jpeg;base64,' + base64.b64encode(open('logo.jpg', 'rb').read()).decode()
    h = h.replace('https://shreedeepsolutions.com/logo.jpg', logo)
    tmp = os.path.abspath('_tools/.manual.html'); open(tmp, 'w', encoding='utf-8').write(h)
    async def run():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page()
            await pg.goto('file://' + tmp); await pg.wait_for_timeout(400)
            await pg.pdf(path='downloads/S4S-User-Manual.pdf', format='A4', print_background=True, display_header_footer=True,
                         header_template='<span></span>', footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#888">Solutions4Society User Manual · shreedeepsolutions.com/s4s-guide/ · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
                         margin={'top': '14mm', 'bottom': '16mm', 'left': '13mm', 'right': '13mm'})
            await b.close()
    asyncio.run(run()); os.remove(tmp)
    print('downloads/S4S-User-Manual.pdf', os.path.getsize('downloads/S4S-User-Manual.pdf') // 1024, 'KB')

if __name__ == '__main__':
    main()
