"""Builds the free templates in /downloads. Run from repo root: python3 _tools/make_downloads.py"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = 'downloads'
os.makedirs(OUT, exist_ok=True)
GREY = RGBColor(0x55, 0x55, 0x55)

def base():
    d = Document()
    s = d.sections[0]
    s.page_height, s.page_width = Cm(29.7), Cm(21.0)
    s.top_margin = s.bottom_margin = Cm(1.6)
    s.left_margin = s.right_margin = Cm(2.2)
    st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    st.paragraph_format.space_after = Pt(6)
    return d

def para(d, text='', bold=False, size=None, align=None, italic=False, color=None, after=None):
    p = d.add_paragraph()
    if text:
        r = p.add_run(text); r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    if align is not None: p.alignment = align
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p

def no_borders(table):
    tbl = table._tbl
    pr = tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + e); el.set(qn('w:val'), 'nil'); b.append(el)
    pr.append(b)

def letterhead(d):
    para(d, '[ SOCIETY NAME ] CO-OPERATIVE HOUSING SOCIETY LTD.', bold=True, size=15, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    para(d, 'Registration No.: [ ______________ ]', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    para(d, 'Address: [ ______________________________________________ ]', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    p = para(d, '', after=8)
    pPr = p._p.get_or_add_pPr(); bdr = OxmlElement('w:pBdr'); bot = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '12'), ('space', '1'), ('color', '000000')): bot.set(qn('w:' + k), v)
    bdr.append(bot); pPr.append(bdr)

def sign_block(d, lines, left_text=''):
    """Signatory block on the RIGHT; its contents centre-aligned."""
    t = d.add_table(rows=1, cols=2); no_borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.columns[0].width = Cm(8.3); t.columns[1].width = Cm(8.3)
    l, r = t.rows[0].cells
    l.width = Cm(8.3); r.width = Cm(8.3)
    if left_text:
        l.paragraphs[0].add_run(left_text).font.size = Pt(10.5)
    first = True
    for txt, bold, gap in lines:
        p = r.paragraphs[0] if first else r.add_paragraph()
        first = False
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(gap)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(txt); run.bold = bold

def footer_note(d, txt):
    para(d, '')
    para(d, txt, italic=True, size=8.5, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)

# ---------- AGM notice ----------
d = base(); letterhead(d)
t = d.add_table(rows=1, cols=2); no_borders(t)
t.rows[0].cells[0].paragraphs[0].add_run('Ref. No.: [ ____ ]')
c = t.rows[0].cells[1].paragraphs[0]; c.add_run('Date: [ __ / __ / ____ ]'); c.alignment = WD_ALIGN_PARAGRAPH.RIGHT
para(d, '')
para(d, 'NOTICE OF THE ANNUAL GENERAL MEETING', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER)
para(d, 'Notice is hereby given that the [ __th ] Annual General Meeting of the members of [ Society Name ] Co-operative Housing Society Ltd. will be held on [ Day ], [ Date ] at [ Time ] at [ Venue ] to transact the following business:')
agenda = [
    'To read and confirm the minutes of the previous General Body Meeting held on [ date ].',
    'To receive and adopt the Annual Report of the Managing Committee for the year ended 31st March [ year ].',
    'To receive and adopt the audited Income & Expenditure Account and Balance Sheet for the year ended 31st March [ year ], together with the Statutory Audit Report.',
    'To consider the Audit Rectification Report (Form O) for the year [ ____ ].',
    'To appoint the Statutory Auditor for the year [ ____ ] from the panel approved by the Registrar and to fix the remuneration.',
    'To approve the budget for the year [ ____ ] and to decide the rate of interest on delayed payment of society charges (not exceeding 12% per annum simple interest).',
    'To consider any other subject with the permission of the Chair.',
]
for i, a in enumerate(agenda, 1):
    p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(1.6); p.paragraph_format.first_line_indent = Cm(-1.6)
    r = p.add_run('Subject No. %d:\t' % i); r.bold = True
    p.add_run(a)
para(d, '')
para(d, 'Notes:', bold=True, after=2)
for n in ['If there is no quorum at the appointed time, the meeting will be adjourned and held [ half an hour later ] at the same place, and the business will be transacted irrespective of quorum.',
          'Copies of the audited accounts and audit report are available for inspection at the society office on all working days between [ __ ] and [ __ ].',
          'Members who wish to raise any query on the accounts are requested to send it in writing to the Secretary at least [ 7 ] days before the meeting.',
          'Members are requested to attend in person.']:
    p = d.add_paragraph(n, style='List Number')
para(d, '')
sign_block(d, [('By order of the Managing Committee', False, 0), ('For [ Society Name ] Co-op. Hsg. Soc. Ltd.', True, 4), ('', False, 28), ('Hon. Secretary', True, 0)])
footer_note(d, 'Template by Shreedeep Solutions · shreedeepsolutions.com · 90042 64282. Check the notice period, quorum and agenda against your registered bye-laws.')
d.save(os.path.join(OUT, 'agm-notice-template.docx'))

# ---------- NOC for sale of flat ----------
d = base(); letterhead(d)
t = d.add_table(rows=1, cols=2); no_borders(t)
t.rows[0].cells[0].paragraphs[0].add_run('Ref. No.: [ ____ ]')
c = t.rows[0].cells[1].paragraphs[0]; c.add_run('Date: [ __ / __ / ____ ]'); c.alignment = WD_ALIGN_PARAGRAPH.RIGHT
para(d, '')
para(d, 'NO OBJECTION CERTIFICATE', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
para(d, '(For sale / transfer of flat)', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
para(d, 'TO WHOMSOEVER IT MAY CONCERN', bold=True)
para(d, 'This is to certify that Mr./Mrs./Ms. [ Name of Member ] is a bona fide member of [ Society Name ] Co-operative Housing Society Ltd., holding Share Certificate No. [ ___ ] for [ ___ ] shares of ₹[ ___ ] each, bearing distinctive Nos. [ ___ ] to [ ___ ], in respect of Flat No. [ ___ ], [ ___ ] Wing, admeasuring [ ___ ] sq. ft. (carpet area).')
para(d, 'The Society has no objection to the said member selling / transferring the said flat to Mr./Mrs./Ms. [ Name of Purchaser ], subject to the following:')
for n in ['As on [ date ], the member has paid all dues of the Society up to [ month / year ], and nothing is outstanding [ OR: an amount of ₹[ ___ ] is outstanding, to be cleared before transfer ].',
          'The transfer of membership and shares shall be effected only on receipt of the application for transfer and membership in the prescribed forms, along with the transfer fee and premium, if any, as per the bye-laws and the rules in force.',
          'The purchaser shall abide by the bye-laws of the Society and the decisions of the General Body and Managing Committee.',
          'The flat is [ not mortgaged / mortgaged to [ Bank ] ] as per the records of the Society.',
          'This certificate is issued at the request of the member and is valid for [ 3 months ] from the date of issue.']:
    d.add_paragraph(n, style='List Number')
para(d, '')
sign_block(d, [('For [ Society Name ] Co-op. Hsg. Soc. Ltd.', True, 0), ('', False, 28), ('Hon. Secretary', True, 0)], left_text='(Society seal)')
footer_note(d, 'Template by Shreedeep Solutions · shreedeepsolutions.com · 90042 64282. Edit the conditions to match your society\'s bye-laws and records.')
d.save(os.path.join(OUT, 'noc-sale-of-flat-template.docx'))

# ---------- Handover checklist PDF ----------
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob
font, fontb = 'Helvetica', 'Helvetica-Bold'
for f in glob.glob('/usr/share/fonts/**/DejaVuSans.ttf', recursive=True):
    pdfmetrics.registerFont(TTFont('DJ', f)); pdfmetrics.registerFont(TTFont('DJB', f.replace('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'))); font, fontb = 'DJ', 'DJB'; break
ss = getSampleStyleSheet()
H = ParagraphStyle('h', fontName=fontb, fontSize=17, leading=21, textColor=colors.black, spaceAfter=4)
S = ParagraphStyle('s', fontName=font, fontSize=9.5, leading=13, textColor=colors.HexColor('#444444'), spaceAfter=10)
H2 = ParagraphStyle('h2', fontName=fontb, fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=4)
B = ParagraphStyle('b', fontName=font, fontSize=9.6, leading=12.5)
sections = [
 ('A. Books of account', ['Trial balance as on handover date', 'General ledger and cash / bank books for the current year', 'Member-wise outstanding statement (principal and interest separately)',
   'Last audited accounts, audit report and Form O submitted', 'Bank reconciliation statements for every account', 'Fixed deposit list with receipts, maturity dates and interest certificates',
   'Backup of accounting software data (software name and version)']),
 ('B. Vouchers and records', ['Payment vouchers with bills and approvals', 'Receipt books (used and unused) and receipt register', 'Cheque books (used counterfoils and unused leaves)',
   'Vendor / AMC contracts with rates and renewal dates', 'Billing heads, rates and the General Body resolution on interest', 'Pending bills and advances to be adjusted']),
 ('C. Tax and portal access', ['TAN, TRACES login and copies of TDS returns (Form 140 / 26Q)', 'TDS challans and TDS certificates issued', 'PAN, income tax portal login and copies of ITR-5 filed',
   'GST registration and login, with returns filed (if applicable)', 'Any pending notices: income tax, TDS, GST, Registrar']),
 ('D. Society registers (if kept by the accountant)', ['I Register, J Register, Share Register, Nomination Register', 'Share certificate book', 'Minutes books of General Body and Managing Committee meetings']),
 ('E. After handover', ['Change passwords on every portal and email', 'Registered email and mobile on portals belong to the society', 'Opening trial balance agreed with the last audited balance sheet',
   'Bank balances agreed with bank statements', 'Members informed of the new accountant and contact person']),
]
story = [Paragraph('Accountant Handover Checklist', H), Paragraph('For co-operative housing societies changing their accountant. Tick each item as it is received. Society: ____________________   Handover date: ___________', S)]
for title, items in sections:
    rows = [[Paragraph('☐' if font == 'DJ' else '[ ]', B), Paragraph(i, B), Paragraph('', B)] for i in items]
    tbl = Table([[Paragraph('', B), Paragraph('<b>Item</b>', B), Paragraph('<b>Remarks</b>', B)]] + rows, colWidths=[0.8 * cm, 11.2 * cm, 5 * cm])
    tbl.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')), ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EEEEEE')),
                             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    story.append(KeepTogether([Paragraph(title, H2), tbl]))
story += [Spacer(1, 18), Table([[Paragraph('Handed over by (previous accountant)<br/><br/><br/>Name & signature', B), Paragraph('Received by (for the society)<br/><br/><br/>Name, designation & signature', B)]], colWidths=[8.5 * cm, 8.5 * cm]),
          Spacer(1, 14), Paragraph('Prepared by Shreedeep Solutions · shreedeepsolutions.com · +91 90042 64282 · +91 90042 62639', S)]
SimpleDocTemplate(os.path.join(OUT, 'accountant-handover-checklist.pdf'), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                  title='Accountant Handover Checklist', author='Shreedeep Solutions').build(story)
print('downloads built')
