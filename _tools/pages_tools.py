from common import *

TOOLS_JS = r'''<script>
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var inr = function (n) { return '₹' + Math.round(n).toLocaleString('en-IN'); };
  var num = function (id) { var v = parseFloat(($(id).value || '').replace(/,/g, '')); return isNaN(v) ? 0 : v; };
  var parse = function (v) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || ''); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; };
  var fmt = function (d) { return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }); };

  /* 1. Interest on late payment */
  function interest() {
    var amt = num('#i-amt'), rate = num('#i-rate'), due = parse($('#i-due').value), paid = parse($('#i-paid').value), out = $('#i-out');
    if (!amt || !due || !paid) { out.innerHTML = '<p class="t-hint">Enter the amount, due date and payment date.</p>'; return; }
    var days = Math.round((paid - due) / 86400000);
    if (days <= 0) { out.innerHTML = '<p class="t-big">No interest</p><p class="t-hint">Paid on or before the due date.</p>'; return; }
    var i = amt * rate / 100 * days / 365;
    var warn = rate > 12 ? '<p class="t-warn">The rate is above 12%. Under Rule 106C-12, a housing society cannot charge more than 12% per annum simple interest.</p>' : '';
    out.innerHTML = '<p class="t-label">Interest payable</p><p class="t-big">' + inr(i) + '</p>' +
      '<p class="t-hint">' + inr(amt) + ' × ' + rate + '% × ' + days + ' days ÷ 365 (from ' + fmt(due) + ' to ' + fmt(paid) + '). Total due: <b>' + inr(amt + i) + '</b></p>' + warn;
  }
  ['#i-amt', '#i-rate', '#i-due', '#i-paid'].forEach(function (s) { $(s).addEventListener('input', interest); });

  /* 2. Sinking & repair fund */
  function funds() {
    var mode = $('#f-mode').value, cost;
    $('#f-cost-row').hidden = mode !== 'cost';
    $('#f-area-row').hidden = mode !== 'area';
    cost = mode === 'cost' ? num('#f-cost') : num('#f-area') * num('#f-rate');
    var flats = Math.max(1, Math.round(num('#f-flats')) || 1), out = $('#f-out');
    if (!cost) { out.innerHTML = '<p class="t-hint">Enter the construction cost of one flat, or its area and the construction rate.</p>'; return; }
    var s = cost * 0.0025, r = cost * 0.0075;
    out.innerHTML = '<table class="t-table"><thead><tr><th></th><th>Per year</th><th>Per month</th></tr></thead><tbody>' +
      '<tr><td>Sinking Fund (0.25%)</td><td>' + inr(s) + '</td><td>' + inr(s / 12) + '</td></tr>' +
      '<tr><td>Repair &amp; Maintenance Fund (0.75%)</td><td>' + inr(r) + '</td><td>' + inr(r / 12) + '</td></tr>' +
      '<tr class="t-total"><td>Total per flat</td><td>' + inr(s + r) + '</td><td>' + inr((s + r) / 12) + '</td></tr>' +
      (flats > 1 ? '<tr><td>Whole society (' + flats + ' flats)</td><td>' + inr((s + r) * flats) + '</td><td>' + inr((s + r) * flats / 12) + '</td></tr>' : '') +
      '</tbody></table><p class="t-hint">These are the minimum yearly contributions under Rule 106C-11, on a construction cost of ' + inr(cost) + ' per flat. Your general body can fix higher rates.</p>';
  }
  ['#f-mode', '#f-cost', '#f-area', '#f-rate', '#f-flats'].forEach(function (s) { $(s).addEventListener('input', funds); });

  /* 3. TDS checker – Income-tax Act, 2025, section 393 */
  var TDS = {
    ci: { name: 'Contractor – individual / HUF', rate: 1, code: '1023', single: 30000, agg: 100000 },
    co: { name: 'Contractor – firm, company or other', rate: 2, code: '1024', single: 30000, agg: 100000 },
    pf: { name: 'Professional fees', rate: 10, code: '1027', agg: 50000 },
    ts: { name: 'Technical services', rate: 2, code: '1026', agg: 50000 },
    rb: { name: 'Rent – land, building or furniture', rate: 10, code: '1009', month: 50000 },
    rm: { name: 'Rent – plant or machinery', rate: 2, code: '1008', month: 50000 }
  };
  function tds() {
    var t = TDS[$('#t-type').value], pay = num('#t-pay'), ytd = num('#t-ytd'), pan = $('#t-pan').value === 'yes', out = $('#t-out');
    $('#t-ytd-row').hidden = !!t.month;
    $('#t-pay-label').textContent = t.month ? 'Rent for the month (₹)' : 'This payment (₹)';
    if (!pay) { out.innerHTML = '<p class="t-hint">Enter the payment amount.</p>'; return; }
    var need, why;
    if (t.month) { need = pay > t.month; why = need ? 'Rent is above ₹50,000 for the month.' : 'Rent is not above ₹50,000 for the month.'; }
    else if (t.single) {
      var total = ytd + pay;
      need = pay > t.single || total > t.agg;
      why = pay > t.single ? 'This single payment is above ₹30,000.' : total > t.agg ? 'Total paid to this contractor this year (' + inr(total) + ') is above ₹1,00,000.' : 'This payment is not above ₹30,000 and the year\'s total (' + inr(total) + ') is not above ₹1,00,000.';
    } else {
      var tot = ytd + pay;
      need = tot > t.agg;
      why = need ? 'Total paid to this person this year (' + inr(tot) + ') is above ₹50,000.' : 'Total paid this year (' + inr(tot) + ') is not above ₹50,000.';
    }
    if (!need) { out.innerHTML = '<p class="t-big">No TDS yet</p><p class="t-hint">' + why + ' Keep tracking the total for the year.</p>'; return; }
    var rate = pan ? t.rate : Math.max(20, t.rate);
    // Crossing the yearly limit with this payment: TDS is due on the whole year's payments, including earlier ones
    var crossing = !t.month && ytd > 0 && ytd <= t.agg && (ytd + pay) > t.agg && !(t.single && pay > t.single);
    var base = crossing ? ytd + pay : pay, tax = base * rate / 100;
    out.innerHTML = '<p class="t-label">Deduct TDS</p><p class="t-big">' + inr(tax) + ' <small>at ' + rate + '%</small></p>' +
      '<p class="t-hint">' + why + (pan ? '' : ' No PAN, so the higher rate of 20% applies.') +
      (crossing ? ' The yearly limit is crossed with this payment, so TDS is due on the whole year\'s total of ' + inr(base) + ', including earlier payments on which no TDS was deducted.' : '') + '</p>' +
      '<ul class="t-list"><li>Pay to the vendor: <b>' + inr(Math.max(0, pay - tax)) + '</b>' + (crossing && tax > pay ? ' (TDS is more than this payment; adjust the balance from the next payment)' : '') + '</li><li>Deposit the TDS by the 7th of next month (30 April for March).</li>' +
      '<li>Report it in the quarterly Form 140 return, payment code ' + t.code + '.</li></ul>';
  }
  ['#t-type', '#t-pay', '#t-ytd', '#t-pan'].forEach(function (s) { $(s).addEventListener('input', tds); });
  interest(); funds(); tds();
})();
</script>
'''

def tools():
    path = '/tools.html'
    crumbs = [('Free Calculators', path)]
    body = hero(crumbs, 'calc', 'Free · No sign-up', 'Free Calculators for <em>Housing Societies</em>',
        'Quick answers to everyday questions in society accounts: interest on late maintenance, minimum sinking and repair fund, and whether a payment needs TDS.', buttons=False)
    body += '''
<section class="section">
  <div class="container">
    <div class="tool-nav"><a href="#interest">Interest on late payment</a><a href="#funds">Sinking &amp; repair fund</a><a href="#tds">TDS checker</a></div>

    <div class="tool card" id="interest">
      <div class="tool-head"><div class="s-icon">%(calc)s</div><div><h2>Interest on Late Maintenance</h2><p>Simple interest, day-wise, from the due date to the payment date.</p></div></div>
      <div class="tool-grid">
        <div class="tool-form">
          <div class="fg"><label for="i-amt">Amount overdue (₹)</label><input id="i-amt" type="number" inputmode="decimal" min="0" value="10000"></div>
          <div class="fg"><label for="i-rate">Interest rate (%% per year)</label><input id="i-rate" type="number" inputmode="decimal" min="0" max="21" step="0.5" value="12"></div>
          <div class="fg"><label for="i-due">Due date</label><input id="i-due" type="date" value="2026-10-20"></div>
          <div class="fg"><label for="i-paid">Payment date</label><input id="i-paid" type="date" value="2026-11-12"></div>
        </div>
        <div class="tool-out" id="i-out" aria-live="polite"></div>
      </div>
      <p class="tool-note">Rule 106C-12 of the Maharashtra Co-operative Societies Rules (amended 2026) caps interest at 12%% per year simple interest. Use the rate fixed by your general body. Some societies charge interest by full month instead of by day; the method in your resolution applies. Read <a href="/guides/mcs-rules-2026-housing-society-changes.html">what changed in 2026</a>.</p>
    </div>

    <div class="tool card" id="funds">
      <div class="tool-head"><div class="s-icon">%(home)s</div><div><h2>Sinking &amp; Repair Fund</h2><p>Minimum yearly contribution under Rule 106C-11.</p></div></div>
      <div class="tool-grid">
        <div class="tool-form">
          <div class="fg"><label for="f-mode">Work out from</label><select id="f-mode"><option value="cost">Construction cost of one flat</option><option value="area">Area × construction rate</option></select></div>
          <div class="fg" id="f-cost-row"><label for="f-cost">Construction cost per flat (₹, as per architect)</label><input id="f-cost" type="number" inputmode="decimal" min="0" value="1500000"></div>
          <div id="f-area-row" hidden>
            <div class="fg"><label for="f-area">Area of flat (sq ft)</label><input id="f-area" type="number" inputmode="decimal" min="0" value="600"></div>
            <div class="fg"><label for="f-rate">Construction rate (₹ per sq ft)</label><input id="f-rate" type="number" inputmode="decimal" min="0" value="2500"></div>
          </div>
          <div class="fg"><label for="f-flats">Number of flats (optional)</label><input id="f-flats" type="number" inputmode="numeric" min="1" value="1"></div>
        </div>
        <div class="tool-out" id="f-out" aria-live="polite"></div>
      </div>
      <p class="tool-note">The construction cost should be the figure certified by the society's architect. If your society does not have one, we can help you arrange it.</p>
    </div>

    <div class="tool card" id="tds">
      <div class="tool-head"><div class="s-icon">%(file)s</div><div><h2>TDS Checker for Society Payments</h2><p>Does this payment need TDS? Income-tax Act, 2025, tax year 2026-27.</p></div></div>
      <div class="tool-grid">
        <div class="tool-form">
          <div class="fg"><label for="t-type">Type of payment</label><select id="t-type">
            <option value="ci">Contractor – individual / HUF (AMC, housekeeping, repairs)</option>
            <option value="co">Contractor – firm, company or other</option>
            <option value="pf">Professional fees (legal, architect, audit)</option>
            <option value="ts">Technical services</option>
            <option value="rb">Rent – land, building or furniture</option>
            <option value="rm">Rent – plant or machinery</option>
          </select></div>
          <div class="fg"><label for="t-pay" id="t-pay-label">This payment (₹)</label><input id="t-pay" type="number" inputmode="decimal" min="0" value="45000"></div>
          <div class="fg" id="t-ytd-row"><label for="t-ytd">Already paid to the same person this year (₹)</label><input id="t-ytd" type="number" inputmode="decimal" min="0" value="0"></div>
          <div class="fg"><label for="t-pan">Has the payee given a PAN?</label><select id="t-pan"><option value="yes">Yes</option><option value="no">No</option></select></div>
        </div>
        <div class="tool-out" id="t-out" aria-live="polite"></div>
      </div>
      <p class="tool-note">Thresholds and rates as per section 393 of the Income-tax Act, 2025 for tax year 2026-27. This is a quick check, not tax advice. Lower-deduction certificates and special cases are not covered. <a href="/tds-return-housing-society.html">We handle TDS for societies.</a></p>
    </div>
  </div>
</section>''' % dict(calc=ic('calc'), home=ic('home'), file=ic('file'))
    body += '\n' + related([('/guides/mcs-rules-2026-housing-society-changes.html', 'New Housing Society Rules 2026'), ('/downloads.html', 'Free Templates'), ('/#calendar', 'Due Dates Calendar')], 'More Resources')
    body += '\n' + cta()
    apps = [{"@type": "WebApplication", "name": n, "url": SITE + path + a, "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"}, "provider": {"@id": SITE + "/#business"}}
            for n, a in [('Housing Society Interest on Late Payment Calculator', '#interest'), ('Sinking and Repair Fund Calculator', '#funds'), ('TDS Checker for Housing Society Payments', '#tds')]]
    return path, page(path, 'Free Housing Society Calculators: Interest, Sinking Fund, TDS | Shreedeep Solutions',
        'Free calculators for co-operative housing societies: interest on late maintenance (12% cap), minimum sinking and repair fund, and a TDS checker for contractor, professional and rent payments.',
        body, crumbs, graph_extra=apps, scripts=TOOLS_JS, active='/tools.html')


DL_JS = r'''<script>
(function () {
  var KEY = '499e48d0-4507-41d3-97ff-ec1b83372fe3';
  var form = document.getElementById('dlForm'), msg = document.getElementById('dlMsg'), box = document.getElementById('dlLinks');
  var unlock = function () { box.classList.add('open'); form.hidden = true; document.getElementById('dlIntro').hidden = true; };
  try { if (localStorage.getItem('ss-dl') === '1') unlock(); } catch (e) {}
  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    var name = form.name.value.trim(), phone = form.phone.value.replace(/\D/g, '').slice(-10), soc = form.society.value.trim(), role = form.role.value;
    var ok = true;
    form.name.closest('.fg').classList.toggle('err', !name); if (!name) ok = false;
    form.phone.closest('.fg').classList.toggle('err', !/^[6-9]\d{9}$/.test(phone)); if (!/^[6-9]\d{9}$/.test(phone)) ok = false;
    if (!ok) return;
    var btn = form.querySelector('button'); btn.disabled = true; btn.textContent = 'Please wait…';
    try {
      await fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ access_key: KEY, subject: 'Template download – ' + (soc || name), from_name: 'Shreedeep Website', Name: name, Phone: phone, Society: soc || '-', Role: role, Source: 'Free templates page' }) });
    } catch (err) {}
    try { localStorage.setItem('ss-dl', '1'); } catch (e) {}
    unlock();
    msg.textContent = 'Thank you, ' + name + '! Your downloads are ready below.';
  });
})();
</script>
'''

DOWNLOADS = [
    ('/downloads/agm-notice-template.docx', 'AGM Notice Template (Word)', 'Notice of the Annual General Meeting with a standard agenda, ready to edit and print on your letterhead.', 'file'),
    ('/downloads/noc-sale-of-flat-template.docx', 'NOC for Sale of Flat (Word)', 'No Objection Certificate format for a member selling a flat, with the society signatory block.', 'file'),
    ('/downloads/accountant-handover-checklist.pdf', 'Accountant Handover Checklist (PDF)', 'Everything to collect from your previous accountant: books, vouchers, bank and tax portal access.', 'download'),
]

def downloads():
    path = '/downloads.html'
    crumbs = [('Free Templates', path)]
    body = hero(crumbs, 'download', 'Free for managing committees', 'Free Templates for <em>Housing Societies</em>',
        'Editable Word templates and printable checklists that our team uses every day. Tell us who you are and download all of them instantly.', buttons=False)
    items = ''.join('<div class="dl-item"><div class="s-icon">%s</div><div><h3>%s</h3><p>%s</p></div></div>' % (ic(i), t, d) for h, t, d, i in DOWNLOADS)
    links = ''.join('<a class="btn btn-maroon" href="%s" download>%s %s</a>' % (h, ic('download'), t) for h, t, d, i in DOWNLOADS)
    body += '''
<section class="section">
  <div class="container dl-wrap">
    <div class="dl-list">%s</div>
    <div class="card dl-card">
      <h2>Get the templates</h2>
      <p id="dlIntro">Enter your details once to unlock all downloads. We will not share your number.</p>
      <form id="dlForm" novalidate>
        <div class="fg"><label for="dl-name">Your name *</label><input id="dl-name" name="name" autocomplete="name"><div class="err-msg">Please enter your name</div></div>
        <div class="fg"><label for="dl-phone">Mobile number *</label><input id="dl-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" placeholder="10-digit mobile"><div class="err-msg">Enter a valid 10-digit mobile number</div></div>
        <div class="fg"><label for="dl-soc">Society name</label><input id="dl-soc" name="society"></div>
        <div class="fg"><label for="dl-role">You are</label><select id="dl-role" name="role"><option>Chairman</option><option>Secretary</option><option>Treasurer</option><option>Committee member</option><option>Member</option><option>Other</option></select></div>
        <button type="submit" class="btn btn-gold">%s Unlock downloads</button>
      </form>
      <p class="dl-msg" id="dlMsg" aria-live="polite"></p>
      <div class="dl-links" id="dlLinks">%s</div>
    </div>
  </div>
</section>''' % (items, ic('download'), links)
    body += '\n' + related([('/guides/agm-checklist-housing-society.html', 'AGM Checklist'), ('/guides/how-to-change-society-accountant.html', 'How to Change Your Society Accountant'), ('/tools.html', 'Free Calculators')], 'More Resources')
    body += '\n' + cta()
    return path, page(path, 'Free Housing Society Templates: AGM Notice, NOC, Handover Checklist | Shreedeep Solutions',
        'Download free templates for co-operative housing societies: AGM notice, NOC for sale of flat and an accountant handover checklist.', body, crumbs, scripts=DL_JS, active='/downloads.html')
