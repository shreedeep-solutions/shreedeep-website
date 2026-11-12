from common import *

def airoli():
    path = '/society-accountant-airoli.html'
    crumbs = [('Navi Mumbai', '/housing-society-accounting-navi-mumbai.html'), ('Airoli', path)]
    faqs = [
        ('Where is your office in Airoli?', 'Our office is at D204, Shankar Sheela CHS Ltd., near Kesar Sweets, Sector-8, Airoli, Navi Mumbai – 400708. We are open every day except Tuesday, 9 AM to 6 PM. Please call before visiting so the right person is available.'),
        ('Which parts of Airoli do you cover?', 'All sectors of Airoli from Sector 1 to Sector 20, along with nearby Rabale, Ghansoli, Diva Gaon, Mukund Nagar and Dighe. Being in Airoli ourselves, we can visit your society office quickly when documents need to be checked or signed.'),
        ('Can you take over our accounts in the middle of the year?', 'Yes. We collect the opening balances, member ledgers, bank statements and pending vouchers from your previous accountant, reconcile them, and continue billing without a break. See our <a href="/guides/how-to-change-society-accountant.html">handover checklist</a> for what to collect.'),
        ('Do you prepare maintenance bills and send them to members?', 'Yes. We prepare monthly, bi-monthly or quarterly maintenance bills with interest on arrears as per your general body resolution, and email them to members along with receipts.'),
        ('How are your fees decided?', 'Fees depend on the number of flats and shops and the scope of work. Fill in our <a href="/#estimate">free estimate form</a> or call us for a customised quote.'),
    ]
    body = hero(crumbs, 'pin', 'Our office is in Sector-8, Airoli',
        'Housing Society Accountant &amp; Auditor in <em>Airoli</em>',
        'We are an Airoli-based firm that handles society accounting, maintenance billing, statutory audit, TDS and the society\'s income tax return for co-operative housing societies across every sector of Airoli.',
        trust=['Office in Sector-8, Airoli', '120+ housing societies served', 'Quick visits to your society office'],
        wa_text='Hello Shreedeep Solutions, I am enquiring for a housing society in Airoli.')
    body += '\n' + section('Your Neighbourhood Accountant', 'Why Airoli Societies Work With Us', '''    <div class="prose">
      <p>Most housing society work still needs paper: cheque books, vouchers, receipt books, bank statements and signatures from the Chairman, Secretary and Treasurer. When your accountant is in the same node, those small trips stop being a problem.</p>
      <p><strong>Shreedeep Solutions has its office in Sector-8, Airoli.</strong> Our team can collect documents, meet your managing committee and attend your AGM without long travel. We work with societies of every size, from small 12-flat buildings to large complexes with shops and multiple wings.</p>
      <p>Every month we prepare maintenance bills, record receipts, reconcile your bank accounts and keep member ledgers up to date. At year end we prepare the Income &amp; Expenditure Account, Balance Sheet and Receipts &amp; Payments statement ready for audit, and we track every deadline on our <a href="/#calendar">compliance calendar</a>.</p>
    </div>''')
    body += '\n' + section('What We Do', 'Services for Airoli Societies', cards([
        ('home', 'Society Accounting', 'Maintenance billing, receipts, bank reconciliation, member ledgers and year-end statements.', '/#services'),
        ('users', 'Society Management', 'Registers, AGM and SGM notices and minutes, member correspondence and outstanding dues statements.', '/society-management-services.html'),
        ('search', 'Statutory Audit', 'Annual audit under the MCS Act and help with the Form O rectification report.', '/chs-statutory-audit.html'),
        ('file', 'TDS Returns', 'TDS on contractor and professional payments, monthly challans and quarterly Form 140 returns.', '/tds-return-housing-society.html'),
        ('briefcase', 'GST Returns', 'GST applicability check, registration and monthly or quarterly returns.', '/gst-for-housing-societies.html'),
        ('shield', 'Society Income Tax (ITR-5)', "The society's income tax return, prepared from the audited accounts.", '/housing-society-income-tax-itr-5.html'),
    ]), alt=True)
    body += '\n' + section('Areas We Cover', 'Across Airoli and Nearby', '''    <div class="chips">
      %s
    </div>
    <p class="chips-note">Also serving all of <a href="/housing-society-accounting-navi-mumbai.html">Navi Mumbai</a>, <a href="/housing-society-accounting-thane.html">Thane</a> and <a href="/housing-society-accounting-mumbai.html">Mumbai</a>.</p>''' % ''.join('<span>%s</span>' % s for s in
        ['Sector 1', 'Sector 2', 'Sector 3', 'Sector 4', 'Sector 5', 'Sector 6', 'Sector 7', 'Sector 8', 'Sector 8A', 'Sector 9', 'Sector 10', 'Sector 10A', 'Sector 14', 'Sector 15', 'Sector 16', 'Sector 17', 'Sector 19', 'Sector 20', 'Diva Gaon', 'Rabale', 'Ghansoli', 'Mukund Nagar', 'Dighe']))
    body += '\n' + section('FAQ', 'Questions from Airoli Societies', faq_html(faqs), alt=True)
    body += '\n' + cta('Get a Free Estimate for Your Airoli Society')
    return path, page(path, 'Society Accountant & Auditor in Airoli, Navi Mumbai | Shreedeep Solutions',
        'Airoli-based accountants for co-operative housing societies: maintenance billing, accounts, statutory audit, TDS and society ITR. Office in Sector-8, Airoli. Call 90042 64282.',
        body, crumbs, faqs=faqs)


def service_page(path, crumb, title, desc, eyebrow_icon, eyebrow, h1, lead, intro, includes, faqs, related_links, trust=None):
    crumbs = [('Services', '/#services'), (crumb, path)]
    body = hero(crumbs, eyebrow_icon, eyebrow, h1, lead, trust=trust or ['120+ housing societies served', 'Navi Mumbai, Thane & Mumbai', 'Office in Airoli, Navi Mumbai'])
    body += '\n' + section('Overview', 'How We Help', '    <div class="prose">\n%s\n    </div>' % intro)
    body += '\n' + section("What's Included", 'Scope of Work', '    <ul class="ticks">\n%s\n    </ul>' % '\n'.join('      <li>%s%s</li>' % (ic('check'), i) for i in includes), alt=True)
    body += '\n' + section('FAQ', 'Common Questions', faq_html(faqs))
    body += '\n' + related(related_links, 'Related')
    body += '\n' + cta()
    svc = {"@type": "Service", "name": crumb, "serviceType": crumb, "provider": {"@id": SITE + "/#business"},
           "areaServed": ["Navi Mumbai", "Thane", "Mumbai"], "audience": {"@type": "Audience", "audienceType": "Co-operative housing societies"}}
    return path, page(path, title, desc, body, crumbs, graph_extra=[svc], faqs=faqs)


def services():
    out = []
    out.append(service_page('/chs-statutory-audit.html', 'Statutory Audit',
        'Statutory Audit of Co-operative Housing Societies | Shreedeep Solutions',
        'Annual statutory audit of co-operative housing societies under the MCS Act, 1960, audit reports in English or Marathi, and help with the Form O rectification report. Navi Mumbai, Thane & Mumbai.',
        'search', 'Audit under the MCS Act, 1960',
        'Statutory Audit for <em>Co-operative Housing Societies</em>',
        'Independent annual audit of your society\'s accounts, with a clear audit report, practical remarks your committee can act on, and support to close every objection through Form O.',
        '''      <p>Every co-operative housing society in Maharashtra must get its accounts audited every year by an auditor appointed by the general body. The audit is meant to be completed within four months of the end of the financial year, so that the audited accounts and the audit report can be placed before the AGM.</p>
      <p>We audit the society's books, vouchers, bank accounts, member ledgers, funds and statutory compliances, and give an audit report with an audit class and specific remarks. Reports can be prepared in <strong>English or Marathi</strong>.</p>
      <p>After the audit, the managing committee has to submit the audit rectification report in <strong>Form O</strong> within three months of the audit report. We help you prepare it so the same objections do not come back next year. Read our <a href="/guides/form-o-audit-rectification-report.html">Form O guide</a>.</p>''',
        ['Verification of receipts, payments, vouchers and bank reconciliation', 'Member-wise dues, interest on arrears and recovery position', 'Sinking fund, repair fund and other funds as per the rules and bye-laws',
         'Fixed assets, depreciation and fixed deposits', 'TDS, GST and income tax compliance check', 'Audit report with audit class and remarks, in English or Marathi',
         'Guidance on the Form O rectification report', 'Presentation of audit findings to the managing committee'],
        [('Who appoints the statutory auditor of a housing society?', 'The general body appoints the auditor, usually at the AGM, from the panel approved by the Registrar, and fixes the auditor\'s remuneration.'),
         ('When should the audit be completed?', 'Within four months of the close of the financial year, that is by 31 July for a year ending 31 March, so the audited accounts can be placed before the AGM by 30 September.'),
         ('Can the same firm maintain our accounts and audit them?', 'No. An auditor cannot audit books they have written. If we maintain your accounts, your statutory audit must be done by an independent auditor, and the other way round.'),
         ('Can the audit report be in Marathi?', 'Yes. We prepare audit reports in Marathi or English, whichever your society prefers.')],
        [('/guides/form-o-audit-rectification-report.html', 'Form O: Audit Rectification Report Explained'), ('/guides/agm-checklist-housing-society.html', 'AGM Checklist for Housing Societies'), ('/#calendar', 'Compliance Due Dates')]))

    out.append(service_page('/society-management-services.html', 'Society Management',
        'Housing Society Management Services | Registers, AGM & Documentation | Shreedeep Solutions',
        'Society management for co-operative housing societies: statutory registers, I and J registers, share certificates, AGM and SGM notices and minutes, NOCs and member records. Navi Mumbai, Thane & Mumbai.',
        'users', 'Paperwork handled for your committee',
        'Housing Society <em>Management</em> &amp; Documentation',
        'Statutory registers, share certificates, nominations, meeting notices and minutes, NOCs and member correspondence, kept up to date so your managing committee is always ready for an audit or an inspection.',
        '''      <p>Managing committee members are volunteers with jobs and families. The paperwork behind a housing society, from the I and J registers to AGM minutes and member transfer files, is easy to let slip, and it is usually the first thing an auditor or Registrar asks to see.</p>
      <p><strong>We keep your society's records complete and current.</strong> We update the statutory registers when flats are transferred, prepare share certificates and nomination records, draft AGM and SGM notices with agendas, write the minutes, and prepare NOCs and letters on your society's letterhead in English or Marathi.</p>
      <p>We use our own register software for the I Register, J Register, Share Register and Nomination Register, so records stay consistent and can be printed in the standard formats at any time. <a href="/software.html">See the software we use</a>.</p>''',
        ['I Register, J Register, Share Register and Nomination Register', 'Share certificates for new members and transfers', 'AGM and SGM notices, agenda and minutes (English or Marathi)',
         'Managing committee meeting minutes', 'NOCs for sale, loan, passport, electricity and other purposes', 'Member-wise outstanding dues statements for the committee',
         'Correspondence with members, the Registrar and service providers', 'Record keeping for redevelopment and conveyance documentation'],
        [('Which registers must a housing society maintain?', 'Among others, the I Register (members), J Register (list of members), Share Register, Nomination Register, minute books and the registers of property and investments. We keep these updated as members join and transfer flats.'),
         ('Can you prepare documents in Marathi?', 'Yes. Notices, minutes, NOCs and letters can be prepared in Marathi, English, or both.'),
         ('Do you call members for unpaid dues?', 'No. We prepare member-wise outstanding statements for the managing committee, and the committee decides how to follow up.')],
        [('/guides/agm-checklist-housing-society.html', 'AGM Checklist for Housing Societies'), ('/downloads.html', 'Free AGM Notice & NOC Templates'), ('/guides/mcs-rules-2026-housing-society-changes.html', 'New Housing Society Rules 2026')]))

    out.append(service_page('/tds-return-housing-society.html', 'TDS Returns',
        'TDS for Housing Societies | Form 140 Quarterly Returns | Shreedeep Solutions',
        'TDS deduction, monthly challans and quarterly Form 140 returns for co-operative housing societies under the Income-tax Act, 2025. TAN registration, TDS certificates and TRACES notices.',
        'file', 'Income-tax Act, 2025',
        'TDS Returns for <em>Housing Societies</em>',
        'When your society pays contractors, professionals or rent above the limits, it must deduct TDS, deposit it every month and file a quarterly return. We handle all of it, including TDS certificates and TRACES notices.',
        '''      <p>A co-operative housing society is a deductor like any other organisation. Payments for lift and pump AMCs, housekeeping and security contracts, repairs, painting, legal fees, audit fees and rent can all attract TDS once they cross the threshold for the year.</p>
      <p>From 1 April 2026, TDS is governed by <strong>section 393 of the Income-tax Act, 2025</strong>, and the quarterly return for non-salary payments is filed in <strong>Form 140</strong> (earlier Form 26Q). Tax deducted in a month must be deposited by the 7th of the following month, and by 30 April for deductions made in March.</p>
      <p>Not sure whether a payment needs TDS? Try our free <a href="/tools.html#tds">TDS checker</a>.</p>''',
        ['TAN application and TRACES registration', 'Section-wise TDS computation on every payment', 'Monthly TDS challan payment by the 7th',
         'Quarterly Form 140 returns, including correction returns', 'TDS certificates (Form 131) to contractors and professionals', 'Handling TRACES defaults, late fee and interest notices'],
        [('What are the TDS rates for contractors?', '1% for individual or HUF contractors and 2% for others, when a single payment exceeds ₹30,000 or total payments in the year exceed ₹1,00,000.'),
         ('Is TDS needed on professional fees paid by the society?', 'Yes, at 10% once total professional fees to that person in the year exceed ₹50,000. Technical services are at 2%.'),
         ('What happens if the society files the TDS return late?', 'A late fee of ₹200 per day applies until the return is filed, capped at the TDS amount, plus interest on late deposit. Penalties can also apply.'),
         ('Does the society need to deduct TDS on salary?', 'Only if it has employees on its payroll whose salary is taxable. Most housing societies hire security and housekeeping through contractors, so contractor TDS applies instead.')],
        [('/tools.html#tds', 'Free TDS Checker'), ('/#calendar', 'TDS Due Dates'), ('/housing-society-income-tax-itr-5.html', 'Society Income Tax (ITR-5)')]))

    out.append(service_page('/gst-for-housing-societies.html', 'GST Returns',
        'GST for Housing Societies | Registration & Returns | Shreedeep Solutions',
        'GST applicability check, registration and GSTR-1, GSTR-3B and GSTR-9 returns for co-operative housing societies in Navi Mumbai, Thane and Mumbai.',
        'briefcase', 'GST for societies',
        'GST Returns for <em>Housing Societies</em>',
        'Not every society needs GST. We check whether yours does, register it if required, charge GST correctly in the maintenance bills and file every return on time.',
        '''      <p>Maintenance charges collected by a housing society from its members are a supply of services. GST becomes relevant when <strong>both</strong> of these apply: the society's aggregate turnover is above ₹20 lakh in a year, and a member's maintenance contribution is above ₹7,500 per month. Below these limits, the contribution is exempt.</p>
      <p>When it applies, GST is calculated on the full monthly contribution of members above ₹7,500, not only the excess. Some items, such as property tax and electricity charges collected on behalf of authorities, are treated differently.</p>
      <p>We review your society's billing, register it under GST if needed, configure the bills to show GST correctly, and file the monthly or quarterly returns and the annual return where applicable.</p>''',
        ['GST applicability review based on your billing and turnover', 'GST registration and amendments', 'Correct GST treatment in maintenance bills',
         'GSTR-1 and GSTR-3B (monthly or quarterly)', 'GSTR-9 annual return where required', 'Replies to GST notices'],
        [('Does our housing society need GST registration?', 'Only if aggregate turnover in the financial year exceeds ₹20 lakh. If it does, maintenance above ₹7,500 per member per month becomes taxable.'),
         ('Is GST charged only on the amount above ₹7,500?', 'No. As per the CBIC clarification, once a member\'s monthly maintenance exceeds ₹7,500, GST applies to the whole amount, subject to the specific exclusions.'),
         ('Can the society claim input tax credit?', 'A registered society can claim input tax credit on eligible expenses such as repairs and AMC services, subject to GST rules. We check eligibility item by item.')],
        [('/#calendar', 'GST Due Dates'), ('/tds-return-housing-society.html', 'TDS for Housing Societies'), ('/guides/', 'All Guides')]))

    out.append(service_page('/housing-society-income-tax-itr-5.html', 'Society ITR-5',
        'Income Tax Return (ITR-5) for Housing Societies | Shreedeep Solutions',
        'ITR-5 filing for co-operative housing societies, prepared from the audited accounts with deductions available to co-operative societies, TDS credit matching and notice support.',
        'shield', 'Income tax for co-operative societies',
        'Society Income Tax Return (<em>ITR-5</em>)',
        'A co-operative housing society must file its own income tax return every year, even if most of its income is not taxable. We prepare it from the audited accounts and file it by the due date.',
        '''      <p>Members' contributions to their own society are generally not taxable because of the principle of mutuality. But a society also earns income from outsiders and investments: interest on fixed deposits and savings accounts, rent from mobile towers or hoardings, and parking or hall charges from non-members. That income must be reported.</p>
      <p>A co-operative society files <strong>ITR-5</strong>. Because its accounts are audited under the Maharashtra Co-operative Societies Act, the due date is the audit-case date, normally <strong>31 October</strong>, unless the CBDT extends it. Our <a href="/#calendar">compliance calendar</a> always shows the current date.</p>
      <p>Co-operative societies can claim specific deductions, for example on interest earned from investments with co-operative banks and societies. Filing on time is important to keep these deductions available.</p>''',
        ['Computation of taxable income from the audited accounts', 'Mutuality and exempt income review', 'Deductions available to co-operative societies',
         'Interest income and TDS credit matched with the AIS', 'ITR-5 preparation and e-filing', 'Refund tracking and replies to income tax notices'],
        [('Does a housing society have to file an income tax return?', 'Yes. A co-operative housing society is a taxable entity and must file ITR-5 every year.'),
         ('What is the due date for a society\'s ITR?', 'Normally 31 October, because society accounts are audited under the MCS Act. For AY 2026-27 the CBDT extended it to 21 November 2026.'),
         ('Is interest on fixed deposits taxable for the society?', 'Interest from deposits with co-operative banks can be eligible for a deduction for a co-operative society. Interest from other banks is generally taxable. We check each investment.')],
        [('/#calendar', 'ITR Due Dates'), ('/tds-return-housing-society.html', 'TDS for Housing Societies'), ('/chs-statutory-audit.html', 'Statutory Audit')]))
    return out
