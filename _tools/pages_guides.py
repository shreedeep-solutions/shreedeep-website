from common import *

PUB = '2026-11-12'

GUIDES = [
    ('/guides/mcs-rules-2026-housing-society-changes.html', 'New Housing Society Rules 2026: What Changed',
     'Interest on dues capped at 12%, minimum sinking and repair fund rates, a new recovery procedure and more. What the 2026 amendment rules mean for your society.'),
    ('/guides/form-o-audit-rectification-report.html', 'Form O: The Audit Rectification Report Explained',
     'What Form O is, who prepares it, when it is due and how to close audit objections so they do not repeat next year.'),
    ('/guides/agm-checklist-housing-society.html', 'AGM Checklist for Housing Societies',
     'A step-by-step checklist for the managing committee: dates, notice, agenda, documents, quorum and minutes.'),
    ('/guides/how-to-change-society-accountant.html', 'How to Change Your Society Accountant Smoothly',
     'Everything to collect from your previous accountant, from ledgers and bank statements to portal logins, so billing continues without a break.'),
]

def article_page(path, title, h1, lead, desc, body_html, faqs=None, related_links=None):
    crumbs = [('Guides', '/guides/'), (h1.replace('<em>', '').replace('</em>', ''), path)]
    body = hero(crumbs, 'book', 'Guide · Updated 12 Nov 2026', h1, lead, buttons=False)
    body += '''
<section class="section">
  <div class="container">
    <article class="article">
%s
      <p class="disclaimer">This guide is general information for managing committees, based on the Maharashtra Co-operative Societies Act, 1960, the rules made under it and the model bye-laws as of the date above. Your society's registered bye-laws and any later notification prevail. Call us before acting on a specific case.</p>
    </article>
  </div>
</section>''' % body_html
    if faqs:
        body += '\n' + section('FAQ', 'Common Questions', faq_html(faqs), alt=True)
    body += '\n' + related(related_links or [(g[0], g[1]) for g in GUIDES if g[0] != path][:3], 'More Guides')
    body += '\n' + cta('Need Help With Your Society?', 'Our team handles accounts, audit and compliance for 120+ housing societies.')
    return path, page(path, title + ' | Shreedeep Solutions', desc, body, crumbs, faqs=faqs, article={'published': PUB})


def guides():
    out = []
    # index
    path = '/guides/'
    crumbs = [('Guides', path)]
    body = hero(crumbs, 'book', 'Free guides for managing committees', 'Housing Society <em>Guides</em>',
        'Plain-language guides on accounts, audit, AGMs and compliance for co-operative housing societies in Maharashtra, written by the team that handles them every day.', buttons=False)
    body += '\n' + section('Guides', 'Read and Share With Your Committee', cards([('book', t, d, h) for h, t, d in GUIDES]))
    body += '\n' + section('Also Useful', 'Free Tools &amp; Templates', cards([
        ('calc', 'Free Calculators', 'Interest on late payment, sinking and repair fund, and a TDS checker for society payments.', '/tools.html'),
        ('download', 'Free Templates', 'AGM notice, NOC for sale of flat, and a handover checklist when changing accountants.', '/downloads.html'),
        ('calendar', 'Due Dates Calendar', 'Every CHS, TDS, GST and ITR deadline, updated when the Government extends a date.', '/#calendar'),
    ]), alt=True)
    body += '\n' + cta()
    itemlist = {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i, "url": SITE + h, "name": t} for i, (h, t, d) in enumerate(GUIDES, 1)]}
    out.append((path + 'index.html', page(path, 'Housing Society Guides: Audit, AGM, Form O & Rules | Shreedeep Solutions',
        'Free guides for co-operative housing society committees in Maharashtra: new 2026 rules, Form O, AGM checklist and changing your society accountant.', body, crumbs, graph_extra=[itemlist])))

    # 1. MCS rules 2026
    out.append(article_page(GUIDES[0][0], GUIDES[0][1], 'New Housing Society Rules 2026: <em>What Changed</em>',
        'In June 2026 Maharashtra notified amendment rules with a separate chapter for co-operative housing societies. Here is what the managing committee needs to change in billing, funds and recovery.',
        GUIDES[0][2], '''      <p>The Maharashtra Co-operative Societies (Amendment) Rules, 2026 were notified on <strong>18 June 2026</strong>. They insert a new <strong>Chapter XI-B (Rules 106C-1 to 106C-14)</strong> that applies specifically to co-operative housing societies, alongside the housing-society chapter of the Act (sections 154B-1 onwards). A revised set of model bye-laws for housing societies has also been published in draft for public comments.</p>

      <h2>1. Interest on delayed payment: maximum 12%</h2>
      <p>Under <strong>Rule 106C-12</strong>, interest on charges paid late is fixed by the general body, but it cannot exceed <strong>12% per annum, simple interest</strong>. The older model bye-laws allowed up to 21%, and many societies still have 18% or 21% in their resolutions.</p>
      <ul>
        <li>Check the rate in your last general body resolution and in your billing software.</li>
        <li>If it is above 12%, place a resolution before the general body to bring it within the limit.</li>
        <li>Interest must be simple interest. Interest on interest is not allowed.</li>
      </ul>
      <p>Work out the interest on any overdue amount with our <a href="/tools.html#interest">interest calculator</a>.</p>

      <h2>2. Sinking fund and repair fund: minimum rates</h2>
      <p><strong>Rule 106C-11</strong> sets minimum yearly contributions, based on the construction cost of each flat as certified by the society's architect:</p>
      <table>
        <thead><tr><th>Fund</th><th>Minimum contribution</th><th>Used for</th></tr></thead>
        <tbody>
          <tr><td>Sinking Fund</td><td>0.25% per year of construction cost</td><td>Heavy repairs and reconstruction, as approved by the general body</td></tr>
          <tr><td>Repair &amp; Maintenance Fund</td><td>0.75% per year of construction cost</td><td>Routine, recurring repairs</td></tr>
        </tbody>
      </table>
      <p>Use our <a href="/tools.html#funds">sinking and repair fund calculator</a> to check whether your current billing meets the minimum.</p>

      <h2>3. Reserve Fund</h2>
      <p>The rules spell out what goes into the Reserve Fund: entrance fees, transfer fees and transfer premium received when membership is transferred, the share of annual surplus allocated under section 66, and donations that are not earmarked for a specific purpose.</p>

      <h2>4. Nomination</h2>
      <p>Under <strong>Rules 106C-8 and 106C-9</strong>, a member or joint member may nominate one or more persons for provisional membership. Each joint member files a separate nomination for their own share, and every nomination is entered in the society's nomination register.</p>

      <h2>5. Recovery of dues under section 154B-29</h2>
      <p><strong>Rule 106C-14</strong> lays down the procedure for recovering dues from defaulting members:</p>
      <ul>
        <li>Application to the Registrar in <strong>Form Y-6</strong> with a court fee of ₹100.</li>
        <li>Attach an authority letter, a certified updated account of dues or the member's ledger, the relevant resolutions and proof of fee payment.</li>
        <li>Defects must be rectified within the time allowed (up to 7 days), or the application can be dismissed.</li>
        <li>The Registrar issues notice to the member, hears both sides and aims to decide within three months of the first hearing. A recovery certificate is issued in <strong>Form Y-7</strong>.</li>
      </ul>
      <p>A clean, up-to-date member ledger is the most important document in this process. If your ledgers have unexplained balances or missing interest entries, fix them before applying.</p>

      <h2>6. Meetings</h2>
      <p><strong>Rule 106C-13</strong> requires the AGM to be held every year under section 75, with notice and agenda as per the Act and bye-laws. A special general meeting needs at least 5 clear days' notice, and a meeting for redevelopment needs 14 clear days' notice. See our <a href="/guides/agm-checklist-housing-society.html">AGM checklist</a>.</p>

      <h2>What your committee should do now</h2>
      <ol>
        <li>Check the interest rate on arrears and bring it to 12% or less.</li>
        <li>Get the architect's construction cost certificate if you do not have one, and check fund contributions against the minimum rates.</li>
        <li>Review how transfer fees and premium are accounted for.</li>
        <li>Update the nomination register for joint members.</li>
        <li>Reconcile member ledgers before starting any recovery case.</li>
      </ol>''',
        faqs=[('What is the maximum interest a housing society can charge on late maintenance?', 'Under Rule 106C-12 of the Maharashtra Co-operative Societies Rules, as amended in 2026, the general body fixes the rate, up to a maximum of 12% per annum simple interest.'),
              ('What is the minimum sinking fund contribution?', '0.25% per year of the construction cost of the flat, as certified by the architect. The repair and maintenance fund is a minimum of 0.75% per year.'),
              ('Which form is used to recover dues from a defaulting member?', 'An application in Form Y-6 to the Registrar under section 154B-29, with a ₹100 court fee. The recovery certificate is issued in Form Y-7.')]))

    # 2. Form O
    out.append(article_page(GUIDES[1][0], GUIDES[1][1], 'Form O: The Audit <em>Rectification Report</em>',
        'Every audit ends with remarks. Form O is how the managing committee answers them, and it has a fixed deadline.',
        GUIDES[1][2], '''      <h2>What is Form O?</h2>
      <p>After the statutory audit, the auditor gives the society an audit report with an audit class and a list of defects or irregularities. <strong>Form O is the audit rectification report</strong>: the managing committee's written reply showing, point by point, what has been done to correct each defect, or why it could not be corrected yet.</p>

      <h2>When is it due?</h2>
      <p>The managing committee must submit Form O <strong>within three months of the date of the audit report</strong>, and place it before the general body. If the audit report is dated 31 July, Form O is due by 31 October. Our <a href="/#calendar">compliance calendar</a> shows this date.</p>

      <h2>Who prepares it?</h2>
      <p>The managing committee is responsible for it. In practice, the society's accountant drafts the replies because most audit remarks relate to the books, and the committee reviews and approves them.</p>

      <h2>How to prepare a good Form O</h2>
      <ol>
        <li><strong>List every remark</strong> from the audit report, in the same order and with the same numbering.</li>
        <li><strong>Act first, then write.</strong> Pass the missing entry, collect the missing voucher, get the resolution, recover the amount. A reply that only says "noted" will come back next year.</li>
        <li><strong>State what was done and when</strong>, with voucher numbers, resolution dates or bank references.</li>
        <li><strong>For remarks that cannot be fixed immediately</strong>, give the reason and the step being taken, for example legal recovery already filed.</li>
        <li><strong>Get it approved</strong> at a managing committee meeting, then place it before the general body.</li>
      </ol>

      <h2>Remarks we see most often</h2>
      <table>
        <thead><tr><th>Audit remark</th><th>Typical rectification</th></tr></thead>
        <tbody>
          <tr><td>Large arrears from members</td><td>Member-wise outstanding statement, reminders by the committee, recovery under section 154B-29 where needed</td></tr>
          <tr><td>Interest on arrears not charged or charged above the limit</td><td>General body resolution on the rate (maximum 12%), corrected bills</td></tr>
          <tr><td>Sinking or repair fund below the minimum</td><td>Revised contribution based on the architect's cost certificate</td></tr>
          <tr><td>Bank reconciliation differences</td><td>Reconciliation statement with every entry explained</td></tr>
          <tr><td>Vouchers without approval or bills</td><td>Committee approval and supporting bills collected</td></tr>
          <tr><td>TDS not deducted or returns not filed</td><td>TDS deposited with interest, returns filed</td></tr>
          <tr><td>Registers not updated</td><td>I, J, share and nomination registers updated</td></tr>
        </tbody>
      </table>
      <p>Most of these are prevented by correct monthly accounting. That is the work we do for our societies, so that the audit report gets shorter every year.</p>''',
        faqs=[('What is Form O in a housing society?', 'Form O is the audit rectification report. The managing committee uses it to explain how each defect pointed out in the statutory audit report has been corrected.'),
              ('What is the deadline for Form O?', 'Within three months of the date of the audit report. It is then placed before the general body.')],
        related_links=[('/chs-statutory-audit.html', 'Statutory Audit for Housing Societies'), ('/guides/agm-checklist-housing-society.html', 'AGM Checklist'), ('/guides/mcs-rules-2026-housing-society-changes.html', 'New Housing Society Rules 2026')]))

    # 3. AGM checklist
    out.append(article_page(GUIDES[2][0], GUIDES[2][1], 'AGM Checklist for <em>Housing Societies</em>',
        'The annual general meeting has to be held by 30 September. Use this checklist to plan it from the close of the year to the final minutes.',
        GUIDES[2][2], '''      <h2>Key dates for a year ending 31 March</h2>
      <table>
        <thead><tr><th>By</th><th>What</th></tr></thead>
        <tbody>
          <tr><td>15 May</td><td>Accounts finalised and handed to the statutory auditor (within 45 days)</td></tr>
          <tr><td>31 July</td><td>Statutory audit completed (within 4 months)</td></tr>
          <tr><td>Mid-September</td><td>AGM notice sent, with at least 14 clear days before the meeting</td></tr>
          <tr><td>30 September</td><td>AGM held (within 6 months of year end)</td></tr>
        </tbody>
      </table>
      <p>All of these dates are on our <a href="/#calendar">compliance calendar</a>, with one-tap Google Calendar reminders.</p>

      <h2>Before the notice</h2>
      <ul>
        <li>Audited Income &amp; Expenditure Account, Balance Sheet and audit report received.</li>
        <li>Form O for the previous year's audit ready, if not already placed.</li>
        <li>Budget for the next year prepared by the managing committee.</li>
        <li>Names of auditors from the approved panel collected, with their fee quotes.</li>
        <li>Managing committee meeting held to approve the agenda and the date, time and venue.</li>
      </ul>

      <h2>The notice</h2>
      <ul>
        <li>Send it at least <strong>14 clear days</strong> before the meeting, or as your bye-laws require.</li>
        <li>Include the date, time, venue and the full agenda. Attach or make available the audited accounts.</li>
        <li>Mention the adjourned meeting time if quorum is not met.</li>
        <li>Keep proof of delivery: signatures, email log or WhatsApp delivery, and a copy on the notice board.</li>
      </ul>
      <p>Download our free <a href="/downloads.html">AGM notice template</a>.</p>

      <h2>A typical agenda</h2>
      <ol>
        <li>Read and confirm the minutes of the previous general meeting.</li>
        <li>Receive and adopt the managing committee's annual report.</li>
        <li>Receive and adopt the audited accounts and the statutory audit report.</li>
        <li>Consider the audit rectification report (Form O) for the previous year.</li>
        <li>Appoint the statutory auditor for the current year and fix the remuneration.</li>
        <li>Approve the budget and any change in maintenance charges or interest rate.</li>
        <li>Any other item with the permission of the chair.</li>
      </ol>

      <h2>On the day</h2>
      <ul>
        <li>Attendance register signed by every member present.</li>
        <li>Check quorum as per your bye-laws before starting.</li>
        <li>Record each resolution with proposer, seconder and voting result.</li>
      </ul>

      <h2>After the meeting</h2>
      <ul>
        <li>Write the minutes and get them signed by the chairperson.</li>
        <li>Implement the decisions: auditor appointment letter, revised bills, fund changes.</li>
        <li>File the annual returns with the Registrar within the time allowed.</li>
      </ul>''',
        faqs=[('When must a housing society hold its AGM?', 'Within six months of the end of the financial year, that is by 30 September for a year ending 31 March.'),
              ('How much notice is needed for a housing society AGM?', 'At least 14 clear days under the model bye-laws, unless your registered bye-laws say otherwise.')],
        related_links=[('/downloads.html', 'Free AGM Notice Template'), ('/guides/form-o-audit-rectification-report.html', 'Form O Explained'), ('/society-management-services.html', 'Society Management Services')]))

    # 4. Change accountant
    out.append(article_page(GUIDES[3][0], GUIDES[3][1], 'How to Change Your <em>Society Accountant</em>',
        'Changing accountants is easy when you know what to collect. Use this checklist so billing, audit and tax filings continue without a gap.',
        GUIDES[3][2], '''      <h2>When should you change?</h2>
      <p>Common reasons we hear: bills that go out late or with errors, interest on arrears calculated inconsistently, bank reconciliations that never match, audit remarks that repeat every year, and missed TDS or ITR deadlines. The best time to switch is at the start of a quarter or the financial year, but a mid-year change works fine with a proper handover.</p>

      <h2>Step 1: Managing committee decision</h2>
      <p>Pass a managing committee resolution appointing the new accountant, with the date from which they take over and the scope of work. Inform the previous accountant in writing and ask for the handover by a fixed date.</p>

      <h2>Step 2: Collect these from the previous accountant</h2>
      <h3>Books and statements</h3>
      <ul>
        <li>Trial balance, ledgers and day books up to the handover date</li>
        <li>Member-wise outstanding statement with principal and interest shown separately</li>
        <li>Last audited accounts and audit report, and the Form O submitted</li>
        <li>Bank reconciliation statements for every bank account</li>
        <li>Fixed deposit list with receipts, maturity dates and interest certificates</li>
        <li>Backup of the accounting software data, with the software name and version</li>
      </ul>
      <h3>Vouchers and records</h3>
      <ul>
        <li>Payment and receipt vouchers with bills, for the current year and at least the last audited year</li>
        <li>Receipt books, cheque books and stamp details</li>
        <li>Vendor and AMC contract list with rates and renewal dates</li>
        <li>Billing heads and rates, and the general body resolution on interest</li>
      </ul>
      <h3>Tax and portal access</h3>
      <ul>
        <li>TAN, TRACES login and copies of TDS returns filed</li>
        <li>PAN, income tax portal login and copies of ITRs filed</li>
        <li>GST registration and login, if applicable</li>
        <li>Any pending notices from income tax, TDS or GST departments</li>
      </ul>
      <p>Change every password once the handover is complete, and make sure the society, not an individual, holds the registered email and mobile number on each portal.</p>

      <h2>Step 3: Reconcile the opening position</h2>
      <p>The new accountant should check that the trial balance agrees with the last audited balance sheet, that bank balances match the bank statements, and that member arrears add up to the total in the books. Differences found now are much easier to resolve than at audit time.</p>

      <h2>Step 4: Tell the members</h2>
      <p>Inform members of the new accountant, the contact person for bill queries, and any change in bank details or payment process.</p>

      <h2>Get the checklist</h2>
      <p>Download the printable <a href="/downloads.html">handover checklist</a> and give a copy to your previous accountant. If you are considering a change, <a href="/#estimate">ask us for a free estimate</a>. We take care of the handover for you.</p>''',
        faqs=[('Can we change our society accountant in the middle of the year?', 'Yes. With a proper handover of ledgers, vouchers, bank reconciliations and portal logins, the new accountant can continue billing from the next cycle.'),
              ('Who decides to change the society accountant?', 'The managing committee, by a resolution recorded in the minutes.')],
        related_links=[('/downloads.html', 'Download the Handover Checklist'), ('/society-accountant-airoli.html', 'Society Accountant in Airoli'), ('/guides/form-o-audit-rectification-report.html', 'Form O Explained')]))
    return out
