from common import *

def marathi():
    path = '/mr/'
    crumbs = [('मराठी', path)]
    faqs = [
        ('तुम्ही कोणत्या भागातील सोसायट्यांचे काम करता?', 'नवी मुंबई (ऐरोली, घणसोली, रबाळे, कोपरखैरणे, वाशी, नेरुळ, खारघर इ.), ठाणे आणि मुंबईतील सहकारी गृहनिर्माण संस्थांचे काम आम्ही करतो. आमचे ऑफिस सेक्टर-८, ऐरोली येथे आहे.'),
        ('ऑडिट रिपोर्ट मराठीत मिळेल का?', 'हो. वैधानिक लेखापरीक्षण (स्टॅच्युटरी ऑडिट) अहवाल मराठी किंवा इंग्रजीत, संस्थेच्या पसंतीनुसार तयार केला जातो.'),
        ('थकबाकीवर किती व्याज आकारता येते?', 'महाराष्ट्र सहकारी संस्था नियम (२०२६ सुधारणा) नियम 106C-12 नुसार सर्वसाधारण सभा व्याजदर ठरवते, पण तो वार्षिक १२% सरळ व्याजापेक्षा जास्त असू शकत नाही.'),
        ('वार्षिक सर्वसाधारण सभा (AGM) कधीपर्यंत घ्यावी लागते?', 'आर्थिक वर्ष संपल्यानंतर सहा महिन्यांच्या आत, म्हणजे ३१ मार्चला संपणाऱ्या वर्षासाठी ३० सप्टेंबरपर्यंत.'),
        ('तुमची फी कशी ठरते?', 'सोसायटीतील फ्लॅट व दुकानांची संख्या आणि कामाच्या स्वरूपावर फी ठरते. मोफत अंदाजासाठी आम्हाला कॉल किंवा WhatsApp करा.'),
    ]
    body = '''<section class="hero">
  <div class="container">
    <div class="crumbs"><a href="/">Home</a> › मराठी</div>
    <span class="eyebrow">%(pin)s ऑफिस: सेक्टर-८, ऐरोली, नवी मुंबई</span>
    <h1>सहकारी गृहनिर्माण संस्थांसाठी <em>अकाउंटिंग, ऑडिट</em> व कायदेशीर पूर्तता</h1>
    <p class="lead">मेंटेनन्स बिल, पावत्या, बँक रिकन्सिलिएशन, वार्षिक हिशोब, स्टॅच्युटरी ऑडिट, TDS, GST आणि सोसायटीचा इन्कम टॅक्स रिटर्न — नवी मुंबई, ठाणे व मुंबईतील १२०+ सोसायट्यांचे काम आम्ही वेळेवर व अचूक करतो.</p>
    <div class="hero-btns">
      <a href="/#estimate" class="btn btn-gold">मोफत अंदाज मिळवा</a>
      <a href="tel:+919004264282" class="btn btn-outline">%(phone)s कॉल करा: 90042 64282</a>
      <a href="%(waurl)s" target="_blank" rel="noopener" class="btn btn-wa">%(wa)s WhatsApp</a>
    </div>
    <div class="trust"><span>%(check)s१२०+ सोसायट्यांचा विश्वास</span><span>%(check)sऑडिट रिपोर्ट मराठीत</span><span>%(check)sनवी मुंबई, ठाणे व मुंबई</span></div>
  </div>
</section>''' % dict(pin=ic('pin'), phone=ic('phone'), wa=ic('wa'), check=ic('check'), waurl=WA + '?text=' + __import__('urllib.parse').parse.quote('नमस्कार, आमच्या सोसायटीसाठी चौकशी करायची आहे.'))
    body += '\n' + section('आमच्याबद्दल', 'मॅनेजिंग कमिटीचा भार हलका करणारी सेवा', '''    <div class="prose">
      <p>सोसायटीचे चेअरमन, सेक्रेटरी आणि ट्रेझरर हे स्वतःची नोकरी-व्यवसाय सांभाळून संस्थेचे काम करतात. बिल उशिरा जाणे, थकबाकीवरील व्याज चुकीचे लागणे, बँक बॅलन्स न जुळणे आणि दरवर्षी तेच ऑडिट रिमार्क येणे — या अडचणी आम्ही रोज पाहतो.</p>
      <p><strong>श्रीदीप सोल्युशन्स</strong> दर महिन्याला मेंटेनन्स बिल तयार करते, पावत्या नोंदवते, बँक रिकन्सिलिएशन करते आणि सभासदनिहाय लेजर अद्ययावत ठेवते. वर्षअखेरीस आय-व्यय खाते (Income &amp; Expenditure), बॅलन्स शीट आणि जमा-खर्च पत्रक ऑडिटसाठी तयार करून देते.</p>
      <p>ऑडिटनंतर फॉर्म O (दोषदुरुस्ती अहवाल) तयार करण्यात मदत करतो, जेणेकरून पुढच्या वर्षी तेच मुद्दे पुन्हा येऊ नयेत. सर्व महत्त्वाच्या तारखा आमच्या <a href="/#calendar">कंप्लायन्स कॅलेंडर</a>वर पाहता येतात.</p>
    </div>''')
    body += '\n' + section('सेवा', 'आमच्या सेवा', cards([
        ('home', 'सोसायटी अकाउंटिंग', 'मेंटेनन्स बिल, पावत्या, बँक रिकन्सिलिएशन, सभासद लेजर आणि वार्षिक हिशोब.', '/#services'),
        ('users', 'सोसायटी मॅनेजमेंट', 'आय/जे रजिस्टर, शेअर सर्टिफिकेट, नॉमिनेशन, AGM/SGM नोटीस व इतिवृत्त, NOC.', '/society-management-services.html'),
        ('search', 'स्टॅच्युटरी ऑडिट', 'महाराष्ट्र सहकारी संस्था अधिनियम, १९६० नुसार वार्षिक लेखापरीक्षण, मराठी अहवाल.', '/chs-statutory-audit.html'),
        ('file', 'TDS रिटर्न', 'कॉन्ट्रॅक्टर व प्रोफेशनल पेमेंटवर TDS, मासिक चलन आणि तिमाही Form 140 रिटर्न.', '/tds-return-housing-society.html'),
        ('briefcase', 'GST रिटर्न', 'GST लागू आहे का हे तपासणे, नोंदणी आणि रिटर्न फाइलिंग.', '/gst-for-housing-societies.html'),
        ('shield', 'सोसायटी इन्कम टॅक्स (ITR-5)', 'ऑडिट झालेल्या हिशोबावरून सोसायटीचा आयकर रिटर्न वेळेत दाखल.', '/housing-society-income-tax-itr-5.html'),
    ]), alt=True)
    body += '\n' + section('२०२६ चे नवे नियम', 'सोसायट्यांसाठी महत्त्वाचे बदल', '''    <div class="prose">
      <p>१८ जून २०२६ रोजी महाराष्ट्र सहकारी संस्था (सुधारणा) नियम, २०२६ अधिसूचित झाले. त्यात गृहनिर्माण संस्थांसाठी स्वतंत्र प्रकरण XI-B (नियम 106C-1 ते 106C-14) आहे.</p>
      <ul class="ticks">
        <li>%(c)sथकबाकीवरील व्याज: कमाल वार्षिक <strong>१२%% सरळ व्याज</strong> (नियम 106C-12).</li>
        <li>%(c)sसिंकिंग फंड: बांधकाम खर्चाच्या किमान <strong>०.२५%%</strong> दरवर्षी; दुरुस्ती व देखभाल निधी किमान <strong>०.७५%%</strong> (नियम 106C-11).</li>
        <li>%(c)sथकबाकी वसुली: कलम 154B-29 अंतर्गत Form Y-6 मध्ये अर्ज, ₹१०० कोर्ट फी (नियम 106C-14).</li>
      </ul>
      <p>सविस्तर माहिती (इंग्रजीत): <a href="/guides/mcs-rules-2026-housing-society-changes.html">New Housing Society Rules 2026</a>. व्याज व सिंकिंग फंड मोजण्यासाठी आमचे <a href="/tools.html">मोफत कॅल्क्युलेटर</a> वापरा.</p>
    </div>''' % dict(c=ic('check')))
    body += '\n' + section('प्रश्नोत्तरे', 'नेहमी विचारले जाणारे प्रश्न', faq_html(faqs), alt=True)
    body += '''
<section class="section">
  <div class="container">
    <div class="cta">
      <h2>आपल्या सोसायटीसाठी मोफत अंदाज</h2>
      <p>फ्लॅट/दुकानांची संख्या आणि हवे असलेले काम सांगा. आम्ही खास अंदाजपत्रक पाठवू.</p>
      <div class="hero-btns">
        <a href="/#estimate" class="btn btn-gold">मोफत अंदाज मिळवा</a>
        <a href="tel:+919004262639" class="btn btn-outline">%s 90042 62639</a>
      </div>
      <p class="cta-small">कार्यालयीन वेळ: मंगळवार सोडून दररोज, सकाळी ९ ते सायं. ६. भेटीपूर्वी कृपया फोन करा.</p>
    </div>
  </div>
</section>''' % ic('phone')
    return path + 'index.html', page(path, 'सोसायटी अकाउंटंट व ऑडिटर – नवी मुंबई, ठाणे, मुंबई | Shreedeep Solutions',
        'सहकारी गृहनिर्माण संस्थांसाठी अकाउंटिंग, मेंटेनन्स बिल, स्टॅच्युटरी ऑडिट (मराठी अहवाल), TDS, GST व ITR. ऑफिस: सेक्टर-८, ऐरोली. कॉल: 90042 64282.',
        body, crumbs, lang='mr', alternates=[('en', '/'), ('mr', '/mr/'), ('x-default', '/')], faqs=faqs)


def software():
    path = '/software.html'
    crumbs = [('Our Software', path)]
    body = hero(crumbs, 'monitor', 'Technology behind our service', 'Software Built for <em>Housing Societies</em>',
        'We do not depend on generic accounting packages. Our team built its own software for society accounts and statutory registers, designed around the way Maharashtra housing societies actually work.', buttons=False)
    body += '\n' + section('Accounting', 'Solutions4Society', '''    <div class="sw-row">
      <div class="prose">
        <p><strong>Solutions4Society</strong> is the cloud accounting system we use to keep your society's books. It is built specifically for co-operative housing societies, so billing, interest and year-end statements follow society practice out of the box.</p>
        <ul class="ticks">
          <li>%(c)sMaintenance bills with all standard heads, supplementary bills and GST where applicable</li>
          <li>%(c)sInterest on arrears calculated consistently by the method your general body has fixed</li>
          <li>%(c)sReceipts, member ledgers and outstanding dues, always up to date</li>
          <li>%(c)sBank statement import with automatic entry posting and reconciliation</li>
          <li>%(c)sIncome &amp; Expenditure Account, Balance Sheet, Receipts &amp; Payments and the complete books of account as one PDF</li>
          <li>%(c)sFixed deposit and interest tracking, depreciation and fund accounting</li>
          <li>%(c)sMembers receive their bills and receipts by email</li>
          <li>%(c)sMoving from another software? We bring across previous years' data so your history is not lost</li>
        </ul>
      </div>
    </div>''' % dict(c=ic('check')))
    body += '\n' + section('Registers', 'Society Register Manager', '''    <div class="prose">
      <p><strong>Society Register Manager</strong> keeps the statutory registers that auditors and the Registrar ask for, in the standard formats.</p>
      <ul class="ticks">
        <li>%(c)sI Register, J Register, Share Register and Nomination Register</li>
        <li>%(c)sMember numbers assigned automatically by date of admission</li>
        <li>%(c)sShare certificates printed for new members and transfers</li>
        <li>%(c)sMember names in Marathi and English</li>
        <li>%(c)sOld registers in Excel or typed PDF brought in, so nothing has to be re-typed</li>
      </ul>
    </div>''' % dict(c=ic('check')), alt=True)
    body += '\n' + section('What It Means for You', 'Why It Matters to Your Committee', cards([
        ('calendar', 'Bills on time', 'Billing runs on a fixed schedule, so members get their bills when they expect them.', None),
        ('search', 'Fewer audit remarks', 'Consistent interest, reconciled banks and complete registers mean shorter audit reports.', None),
        ('file', 'Records you can trust', 'Every entry links back to its voucher or bank line, so any figure can be explained.', None),
    ]))
    body += '\n' + cta('Want Your Society on Our System?', 'Ask for a free estimate. We handle the data transfer from your current accountant.')
    return path, page(path, 'Housing Society Accounting & Register Software | Shreedeep Solutions',
        'The software behind our service: Solutions4Society for society accounting and billing, and Society Register Manager for I, J, share and nomination registers.',
        body, crumbs)
