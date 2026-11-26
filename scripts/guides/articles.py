# Long-form how-to articles. Each: slug, title, h1, desc, date, body (HTML), tools [(label, href)]
ARTICLES = []

ARTICLES.append(dict(
 slug="guide-unlock-bank-statement-pdf",
 h1="How to remove the password from a bank statement PDF",
 title="How to Remove the Password from a Bank Statement PDF | DailyPdfLife",
 desc="Step-by-step: find the password for your bank or salary statement PDF, remove it safely in your browser, and keep a password-free copy for visa and loan applications.",
 date="2026-11-27",
 tools=[("Unlock PDF","unlock-pdf.html"),("PDF to Excel","pdf-to-excel.html"),("Merge PDF","merge-and-jpg.html#merge")],
 body="""
<p>Most banks in Saudi Arabia, the UAE, Bangladesh and India now email monthly statements, credit card statements and salary certificates as password-protected PDF files. That is good for security, but it becomes a problem the moment you need to use the file: visa portals, embassies, loan applications and landlords often reject locked PDFs, and typing a long password every time you open the file gets tiring. This guide explains how to find the password, remove it safely and keep an unlocked copy.</p>

<h2>Step 1: Find the password</h2>
<p>A bank does not choose a random password. It builds one from information it already has about you and explains the pattern in the email or SMS that came with the statement. Read that message carefully, including the small print at the bottom. Common patterns are:</p>
<ul>
<li>The first four letters of your name in capitals plus your date of birth, for example <code>AHME0105</code> for Ahmed born on 1 May.</li>
<li>Your date of birth in DDMMYYYY format.</li>
<li>The last four or six digits of your account number, card number, mobile number or national ID / Iqama number.</li>
<li>A combination of two of these, such as the last four digits of your mobile followed by your birth year.</li>
</ul>
<p>Passwords are case sensitive, so <code>ahme</code> and <code>AHME</code> are different. If you still cannot work it out, call the bank or check its website's FAQ for “e-statement password”. No tool can legally or practically guess a strong PDF password for you.</p>

<h2>Step 2: Remove the password</h2>
<ol>
<li>Open the <a href="unlock-pdf.html">Unlock PDF</a> tool on your phone or computer.</li>
<li>Choose the locked statement.</li>
<li>Type the password and tap <b>Unlock PDF</b>.</li>
<li>Save the unlocked copy. Give it a clear name such as <code>Statement-2026-10-unlocked.pdf</code>.</li>
</ol>
<p>The unlocked file is identical to the original: same pages, same text, same quality. Only the encryption is removed. Because DailyPdfLife works inside your browser, the statement and the password are never uploaded to any server, which matters for a document that shows your balance and transactions.</p>

<h2>Step 3: Put several months into one file</h2>
<p>Visa and loan applications usually ask for the last three or six months of statements as one document. Unlock each month first, then open <a href="merge-and-jpg.html#merge">Merge PDF</a> and pick the files in date order. If the combined file is too large for the portal, run it through <a href="split-and-compress.html#compress">Compress PDF</a> on the Medium setting.</p>

<h2>Step 4 (optional): Get the transactions into Excel</h2>
<p>If you want to check your spending or total your salary credits, open the unlocked statement in <a href="pdf-to-excel.html">PDF to Excel</a> and choose “All pages in one sheet”. You get a spreadsheet of transactions you can sort, filter and add up.</p>

<h2>Keep your documents safe</h2>
<p>An unlocked statement can be read by anyone who gets hold of it. Store it in a private folder, don't leave it in shared WhatsApp groups, and delete copies you no longer need. If you must email it to someone, consider locking it again with your own password using <a href="pdf-password.html">Protect PDF</a> and sending the password separately by SMS. When sharing a statement only as proof of address or salary, you can hide unrelated transactions with <a href="redact-pdf.html">Redact PDF</a>.</p>

<h2>Common problems</h2>
<p><b>“Wrong password” even though I'm sure it's right.</b> Check capital letters, the date format (DDMMYYYY or DDMMYY) and whether there should be no spaces. Some banks changed their pattern recently, so look at the email for that exact statement.</p>
<p><b>The PDF opens without a password but I can't print or copy.</b> That file has only restrictions, not an opening password. Unlock PDF removes those restrictions too.</p>
<p><b>The portal still rejects the file.</b> Check the size limit and the format. Some portals require a file under 2 MB; compress it, then try again.</p>
"""))

ARTICLES.append(dict(
 slug="guide-passport-photo-size",
 h1="Passport and visa photo sizes by country, and how to make one at home",
 title="Passport & Visa Photo Size by Country – Make One at Home | DailyPdfLife",
 desc="Official passport and visa photo sizes for Saudi Arabia, UAE, Bangladesh, India, Pakistan, UK, USA and more, with tips for taking a photo that gets accepted.",
 date="2026-11-27",
 tools=[("Passport photo maker","passport-photo.html"),("Remove background","remove-bg.html"),("Compress image","image-tools.html#compress")],
 body="""
<p>A rejected photo is one of the most common reasons a passport, visa or residency application is delayed. The rules are strict about size, background, head position and lighting, and they differ from country to country. The good news is that with a phone camera, a plain wall and the free <a href="passport-photo.html">Passport photo maker</a> you can make a photo that meets the rules and print it for very little money.</p>

<h2>Common photo sizes</h2>
<table class="gt">
<tr><th>Country / use</th><th>Size</th><th>Background</th></tr>
<tr><td>Saudi Arabia (passport, Iqama, visa)</td><td>4 × 6 cm or 35 × 45 mm, check the specific service</td><td>White</td></tr>
<tr><td>UAE (visa, Emirates ID)</td><td>35 × 45 mm (43 × 55 mm for some services)</td><td>White</td></tr>
<tr><td>Bangladesh (visa and most forms)</td><td>35 × 45 mm (e-passport photos are taken at the passport office)</td><td>White</td></tr>
<tr><td>India (passport)</td><td>35 × 45 mm; OCI and visa: 51 × 51 mm (2 × 2 in)</td><td>White</td></tr>
<tr><td>Pakistan (visa and most forms)</td><td>35 × 45 mm (passport photos are taken at the passport office)</td><td>White</td></tr>
<tr><td>UK, Schengen / EU</td><td>35 × 45 mm</td><td>Light grey or white</td></tr>
<tr><td>USA (passport and visa)</td><td>2 × 2 inches (51 × 51 mm)</td><td>White or off-white</td></tr>
</table>
<p>Rules change, and different offices sometimes ask for slightly different sizes, so always confirm with the official website or the embassy before printing. If a size isn't in the list, use <b>Custom size</b> in the tool.</p>

<h2>How to take the photo</h2>
<ol>
<li><b>Stand in front of a plain, light wall</b>, about half a metre away from it so there's no shadow behind you.</li>
<li><b>Face a window or a bright light.</b> Light from the front makes the face even; light from behind makes it dark.</li>
<li><b>Ask someone else to take it</b> from about 1.5 metres away, with the phone at your eye level. Selfies make the nose look bigger and are often rejected.</li>
<li><b>Look straight at the camera</b> with a neutral face, mouth closed, eyes open, and both ears and the full face visible. Remove glasses unless the rules allow them. Religious head coverings are normally allowed if the face from chin to forehead is visible.</li>
<li>Take several shots and pick the sharpest.</li>
</ol>

<h2>How to make the photo</h2>
<ol>
<li>Open the <a href="passport-photo.html">Passport photo maker</a> and choose your photo.</li>
<li>Select the size for your country.</li>
<li>Drag and zoom until your face fits the red oval: the top of the head near the top line and the chin near the bottom.</li>
<li>Tap <b>Remove background</b> and choose white or the colour your country asks for.</li>
<li>Adjust brightness and contrast only slightly; heavy editing can get a photo rejected.</li>
<li>Download a <b>single JPG</b> for online forms, or a <b>4×6 print sheet</b> to print at a photo shop. One 4×6 print gives you several copies.</li>
</ol>

<h2>Uploading to an online portal</h2>
<p>Many portals have a file size limit, often between 50 KB and 240 KB, and sometimes a pixel size such as 600 × 600. If your photo is too big, use <a href="image-tools.html#resize">Resize image</a> to set the exact pixels and <a href="image-tools.html#compress">Compress image</a> to reduce the file size. Keep the quality around 80% so the face stays clear.</p>

<h2>Reasons photos get rejected</h2>
<ul>
<li>Shadows on the face or on the background.</li>
<li>Head too small or too large in the frame, or tilted.</li>
<li>Blurry, grainy or over-edited photo.</li>
<li>Smiling with teeth, closed eyes or hair covering the eyes.</li>
<li>Wrong background colour or a background with patterns.</li>
<li>Photo older than six months, or no longer looks like you.</li>
</ul>
"""))

ARTICLES.append(dict(
 slug="guide-reduce-pdf-size",
 h1="How to reduce PDF file size for email and online portals",
 title="How to Reduce PDF File Size Under 1 MB, 500 KB or 200 KB | DailyPdfLife",
 desc="Practical ways to make a PDF smaller for email and upload limits: compress, remove pages, scan at the right settings and avoid giant phone photos.",
 date="2026-11-27",
 tools=[("Compress PDF","split-and-compress.html#compress"),("Remove pages","remove-pages.html"),("Scan to PDF","scan-to-pdf.html")],
 body="""
<p>“File size must not exceed 1 MB.” Anyone who has applied for a visa, a job, a university place or a government service online has seen a message like this. Phone cameras now take 12 to 50 megapixel photos, so a PDF made from a few photographed pages can easily be 10 or 20 MB. Here is how to bring it down, starting with the quickest fix.</p>

<h2>1. Compress the PDF</h2>
<p>Open <a href="split-and-compress.html#compress">Compress PDF</a>, choose your file and start with <b>Medium</b>. This lowers the resolution and quality of the images inside the PDF to a level that still looks sharp on screen and prints well, and it usually cuts scanned documents by 60 to 90 percent. If the file is still too big, try <b>Heavy</b>. Check the result by zooming in on small text to make sure it's still readable.</p>

<h2>2. Remove pages you don't need</h2>
<p>Every page adds size. Blank pages, cover pages, adverts and terms-and-conditions pages are often not required. Use <a href="remove-pages.html">Remove pages</a> to delete them, then compress. If the portal asks for a single document, send only what they asked for.</p>

<h2>3. Split a large file across several uploads</h2>
<p>Some portals allow several files but limit each one. Use <a href="split-and-compress.html#split">Split PDF</a> with page ranges, for example pages 1-5 in one file and 6-10 in another.</p>

<h2>4. Make it smaller from the start</h2>
<ul>
<li><b>Use Scan to PDF instead of plain photos.</b> <a href="scan-to-pdf.html">Scan to PDF</a> crops the page and the “Document” look turns it into clean black and white, which is far smaller than a colour photo of paper on a table.</li>
<li><b>Choose A4 page size</b> rather than “same as photo”, so huge photos are scaled to a normal page.</li>
<li><b>Resize photos before turning them into a PDF.</b> A width of 1600 pixels is plenty for a document page. Use <a href="image-tools.html#resize">Resize image</a>, then <a href="merge-and-jpg.html#jpg">JPG to PDF</a>.</li>
<li><b>Export from Word or Excel directly to PDF</b> rather than printing and scanning. A text PDF of 10 pages is often under 200 KB.</li>
</ul>

<h2>Typical sizes you can expect</h2>
<table class="gt">
<tr><th>Document</th><th>Before</th><th>After Medium compression</th></tr>
<tr><td>3 phone photos of A4 pages</td><td>8-15 MB</td><td>0.5-1.5 MB</td></tr>
<tr><td>Same pages via Scan to PDF (Document look)</td><td>1-2 MB</td><td>200-500 KB</td></tr>
<tr><td>10-page Word document saved as PDF</td><td>150-400 KB</td><td>Little change, already small</td></tr>
</table>
<p>These are typical ranges; your results depend on the content of the pages.</p>

<h2>Why some PDFs don't shrink</h2>
<p>A PDF that is mostly text, such as a contract exported from Word, is already compact; there are no big images to compress. Large embedded fonts can also add a few hundred kilobytes. In that case, removing pages or splitting the file are the best options.</p>

<h2>Keep your files private</h2>
<p>Many free compression sites upload your documents to their servers. DailyPdfLife compresses in your browser, so passports, bank statements and certificates never leave your device.</p>
"""))

ARTICLES.append(dict(
 slug="guide-saudi-vat-15-percent",
 h1="Saudi VAT at 15%: how to add and remove VAT, with examples",
 title="Saudi VAT 15% – How to Add & Remove VAT with Examples | DailyPdfLife",
 desc="Simple formulas and worked examples for adding 15% VAT to a price, removing VAT from a VAT-inclusive total, and checking invoices in Saudi Arabia.",
 date="2026-11-27",
 tools=[("Saudi VAT calculator","saudi-vat-calculator.html"),("Invoice maker","invoice-maker.html"),("Percentage calculator","percentage-calculator.html")],
 body="""
<p>Value Added Tax (VAT) in Saudi Arabia has been 15% since July 2020. Shop prices are normally shown including VAT, while business quotations are often written before VAT. Mixing the two up is an easy way to lose money on a deal, so it helps to know the two basic calculations. You can always use the <a href="saudi-vat-calculator.html">Saudi VAT calculator</a>, but here is what it does.</p>

<h2>Adding 15% VAT to a price</h2>
<p>Multiply the price before VAT by <b>1.15</b>.</p>
<ul>
<li>SAR 1,000 before VAT → VAT is 1,000 × 0.15 = SAR 150 → total SAR 1,150.</li>
<li>SAR 2,480 before VAT → 2,480 × 1.15 = SAR 2,852.</li>
</ul>

<h2>Removing VAT from a VAT-inclusive total</h2>
<p>Divide the total by <b>1.15</b>. Don't subtract 15% of the total: that gives the wrong answer.</p>
<ul>
<li>SAR 1,150 including VAT → 1,150 ÷ 1.15 = SAR 1,000 before VAT, and VAT is SAR 150.</li>
<li>SAR 575 including VAT → 575 ÷ 1.15 = SAR 500, VAT SAR 75.</li>
</ul>
<p>The common mistake: taking 15% off 1,150 gives 977.50, which is SAR 22.50 too low. The VAT inside a total is always 15/115 of it, which is about 13.04%.</p>

<h2>Checking an invoice</h2>
<ol>
<li>Add up the line items before VAT.</li>
<li>Subtract any discount <b>before</b> calculating VAT; VAT is charged on the discounted amount.</li>
<li>Multiply the result by 0.15 to get the VAT and add it to get the total.</li>
<li>A tax invoice from a VAT-registered business should show the seller's VAT number, the date, the amount before VAT, the VAT amount and the total.</li>
</ol>

<h2>Quick reference</h2>
<table class="gt">
<tr><th>Before VAT</th><th>VAT 15%</th><th>Total</th></tr>
<tr><td>100</td><td>15</td><td>115</td></tr>
<tr><td>500</td><td>75</td><td>575</td></tr>
<tr><td>1,000</td><td>150</td><td>1,150</td></tr>
<tr><td>5,000</td><td>750</td><td>5,750</td></tr>
<tr><td>10,000</td><td>1,500</td><td>11,500</td></tr>
</table>

<h2>Small businesses and freelancers</h2>
<p>Businesses must register for VAT with ZATCA once taxable sales pass the mandatory threshold (SAR 375,000 a year at the time of writing), and may register voluntarily above a lower threshold. Registered businesses must also follow the e-invoicing (Fatoora) rules, which require approved software. If you are not registered, you must not charge VAT on your invoices. For simple invoices and quotations, try the <a href="invoice-maker.html">Invoice &amp; Quotation maker</a>, and always confirm current rules on the official ZATCA website, as thresholds and requirements can change.</p>

<h2>UAE and other Gulf countries</h2>
<p>The UAE charges 5% VAT, Bahrain 10% and Oman 5%. The same method works: multiply by 1 plus the rate to add VAT, divide to remove it. The <a href="vat-calculator.html">VAT calculator</a> has these rates built in.</p>
"""))

ARTICLES.append(dict(
 slug="guide-scan-documents-phone",
 h1="How to scan documents with your phone and send them as one PDF",
 title="How to Scan Documents with Your Phone into One PDF | DailyPdfLife",
 desc="Turn paper documents into a clean, readable PDF using only your phone camera: lighting, angles, cleaning, combining pages, making text searchable and sending.",
 date="2026-11-27",
 tools=[("Scan to PDF","scan-to-pdf.html"),("OCR","ocr.html"),("Compress PDF","split-and-compress.html#compress")],
 body="""
<p>You don't need a scanner to send a professional-looking copy of a contract, a certificate or a signed form. A modern phone camera is sharp enough, as long as you take the photo well and clean it up afterwards. Sending a plain photo taken at an angle on a kitchen table looks careless and is often hard to read; a proper scan looks like it came from an office machine.</p>

<h2>Before you start</h2>
<ul>
<li><b>Light:</b> daylight near a window is best. Avoid the flash, which creates a bright spot, and make sure your own shadow is not over the page.</li>
<li><b>Background:</b> put white paper on a dark table so the edges are easy to detect.</li>
<li><b>Flatness:</b> unfold the page and hold the corners down if it curls.</li>
<li><b>Clean lens:</b> wipe the camera lens; fingerprints make photos hazy.</li>
</ul>

<h2>Scanning step by step</h2>
<ol>
<li>Open <a href="scan-to-pdf.html">Scan to PDF</a> and tap <b>Take a photo</b>.</li>
<li>Hold the phone straight above the page so the page fills most of the frame.</li>
<li>Tap <b>Find page edges</b>. Check the corners and drag any that are wrong.</li>
<li>Choose a look. <b>Document</b> gives clean black and white, best for printed text. <b>Enhanced colour</b> keeps stamps, logos and blue-ink signatures. <b>Grayscale</b> is a middle ground.</li>
<li>Repeat for each page, in order.</li>
<li>Pick A4 page size and tap <b>Make PDF</b>.</li>
</ol>
<p>On Android, the DailyPdfLife app also includes Google's document scanner, which detects the page and takes the photo automatically.</p>

<h2>After scanning</h2>
<p><b>Fix the order or rotation</b> in <a href="organize-pdf.html">Organize PDF</a> if a page ended up in the wrong place or sideways.</p>
<p><b>Make the text searchable or editable</b> with <a href="ocr.html">OCR</a>, which reads English, Bangla, Arabic, Hindi and Urdu. This is useful for long documents you need to search or for retyping a letter.</p>
<p><b>Sign it</b> by opening the PDF in the <a href="pdf-editor.html">PDF editor</a> and drawing your signature, so you don't need to print, sign and scan again.</p>
<p><b>Reduce the size</b> with <a href="split-and-compress.html#compress">Compress PDF</a> if it's too large for email or a portal.</p>

<h2>Scanning ID cards and passports</h2>
<p>For an ID card, scan the front and back as two pages of the same PDF, or put both photos on one page with <a href="photo-collage.html">Photo collage</a> using the A4 layout. Use Enhanced colour so the holograms and photo stay clear. Before sending a copy of an ID, consider writing its purpose across it with <a href="image-watermark.html">Image watermark</a>, for example “Copy for tenancy contract only”, so it can't easily be misused.</p>

<h2>Privacy</h2>
<p>Many scanner apps upload your documents to the cloud. DailyPdfLife's Scan to PDF works inside your browser, so your contracts, IDs and certificates stay on your phone until you choose to send them.</p>
"""))

ARTICLES.append(dict(
 slug="guide-flat-vs-reducing-rate",
 h1="Flat rate vs reducing balance: what your car or personal loan really costs",
 title="Flat Rate vs Reducing Balance Loan – Real Cost Explained | DailyPdfLife",
 desc="Why a 4% flat rate costs almost twice as much as a 4% reducing rate, with worked examples, and how to compare car and personal finance offers properly.",
 date="2026-11-27",
 tools=[("Loan & EMI calculator","loan-calculator.html"),("Percentage calculator","percentage-calculator.html"),("Zakat calculator","zakat-calculator.html")],
 body="""
<p>Car dealers and finance companies in the Gulf and South Asia often advertise a low “flat rate”, such as 3.5% or 4%. Bank home finance and many personal loans use a “reducing balance” rate instead. The two numbers look similar but are calculated differently, and the difference in what you actually pay can be thousands. This guide explains both with simple examples you can check in the <a href="loan-calculator.html">Loan &amp; EMI calculator</a>.</p>

<h2>Flat rate</h2>
<p>With a flat rate, profit (interest) is calculated on the <b>full original amount</b> for every year of the loan, even though you are paying it back month by month.</p>
<p>Example: SAR 100,000 for 5 years at 4% flat.</p>
<ul>
<li>Profit per year: 100,000 × 4% = SAR 4,000.</li>
<li>Total profit over 5 years: SAR 20,000.</li>
<li>Total to pay: SAR 120,000, or SAR 2,000 a month for 60 months.</li>
</ul>

<h2>Reducing balance</h2>
<p>With a reducing balance rate, each month's profit is calculated only on <b>what you still owe</b>. As you pay off the loan, the profit part of each payment gets smaller.</p>
<p>Same example: SAR 100,000 for 5 years at 4% reducing.</p>
<ul>
<li>Monthly payment: about SAR 1,842.</li>
<li>Total profit: about SAR 10,500.</li>
<li>Total to pay: about SAR 110,500.</li>
</ul>
<p>So at the same 4%, the flat-rate loan costs roughly SAR 9,500 more, nearly double the profit.</p>

<h2>Converting a flat rate</h2>
<p>As a rough rule, a flat rate is equal to a reducing rate of about <b>1.8 to 1.9 times</b> as much for typical 3 to 5 year loans. A 4% flat rate over 5 years works out to about a 7.4% reducing rate. Enter the offer in the loan calculator with “Flat rate”, note the monthly payment, then switch to “Reducing balance” and raise the rate until the payment matches. That's the true comparable rate.</p>

<h2>How to compare offers</h2>
<ol>
<li>Ask each lender whether the rate is <b>flat</b> or <b>reducing</b>, and ask for the <b>APR</b> (annual percentage rate), which includes fees.</li>
<li>Add the admin or processing fee, insurance and any compulsory extras to the total.</li>
<li>Compare the <b>total amount you will pay</b>, not only the monthly instalment. A longer period gives a smaller instalment but a bigger total.</li>
<li>Check the early settlement terms: how much do you save if you pay off early?</li>
</ol>

<h2>A larger down payment</h2>
<p>Every riyal or taka you pay upfront is a riyal you don't pay profit on. Try entering different down payments in the calculator to see the effect on both the monthly payment and the total cost.</p>

<p class="note">This article is general information, not financial advice. Banks' actual terms, fees and calculation methods vary; always read the official offer and the key facts statement before signing.</p>
"""))

ARTICLES.append(dict(
 slug="guide-sign-pdf-on-phone",
 h1="How to sign a PDF on your phone without printing it",
 title="How to Sign a PDF on Your Phone Without Printing | DailyPdfLife",
 desc="Sign contracts, forms and offer letters on your phone in a few minutes: draw your signature, place it on the PDF, add the date and your company seal, and send it back.",
 date="2026-11-27",
 tools=[("PDF editor","pdf-editor.html"),("Fill PDF forms","fill-pdf-forms.html"),("Stamp PDF","stamp-pdf.html")],
 body="""
<p>An offer letter, a tenancy contract or a school form arrives on WhatsApp with the message “please sign and send back today”. Printing it, signing with a pen and scanning it again takes time, and you may not even have a printer. You can do the whole job on your phone in a few minutes, and the result looks cleaner than a photographed page.</p>

<h2>Step 1: Open the PDF in the editor</h2>
<p>Save the PDF to your phone, then open the <a href="pdf-editor.html">PDF editor</a> and choose the file. The pages appear on screen. If the document is password-protected, unlock it first with <a href="unlock-pdf.html">Unlock PDF</a>.</p>

<h2>Step 2: Fill in the blanks</h2>
<p>If the PDF has proper fillable boxes, <a href="fill-pdf-forms.html">Fill PDF forms</a> is the fastest way to type your answers; save it, then come back to the editor to sign. If the form is just printed lines, choose the <b>Text</b> tool in the editor, tap on the line and type your name, the date, your ID or Iqama number and any other details. Make the text size match the form so it looks neat.</p>

<h2>Step 3: Draw your signature</h2>
<ol>
<li>Tap <b>Signature</b>.</li>
<li>Turn your phone sideways for more room and sign with your finger, slowly, the way you sign on paper. A stylus gives an even better result.</li>
<li>Tap <b>Clear</b> to try again, or <b>Use it</b> when you're happy.</li>
<li>Drag the signature onto the signature line and resize it so it fits naturally, not too big.</li>
</ol>
<p>Choose dark blue or black ink. Many offices prefer blue because it shows the document was signed rather than photocopied.</p>

<h2>Step 4: Add the date, initials and seal</h2>
<p>Contracts often need your initials at the bottom of every page. Add a small text box with your initials on each page, or place a small copy of your signature. Businesses can add the company seal with <a href="stamp-pdf.html">Stamp PDF</a>: upload a photo of the seal on white paper and turn on “make the white background see-through” so it looks like a real stamp.</p>

<h2>Step 5: Save and send</h2>
<p>Tap <b>Save PDF</b>, open the saved file once to check every page, then send it back by email or WhatsApp. If the file is large, use <a href="split-and-compress.html#compress">Compress PDF</a> first.</p>

<h2>Is a drawn signature legally valid?</h2>
<p>For everyday documents such as offer letters, school forms, quotations and many private contracts, a signature drawn on a PDF is widely accepted, in the same way as a scanned signed copy. Some government transactions, banking documents and high-value contracts require a certified digital signature or an official e-signature service, such as those offered through national platforms. When in doubt, ask the person who sent the document which form of signature they accept.</p>

<h2>Keep your signature safe</h2>
<p>Don't send a clean image of your signature to people you don't know, and don't leave it in shared folders. DailyPdfLife's editor runs in your browser, so your signature and documents are not uploaded to any server.</p>
"""))

ARTICLES.append(dict(
 slug="guide-zakat-on-gold-and-savings",
 h1="How to calculate zakat on gold, cash and savings: a worked example",
 title="How to Calculate Zakat on Gold, Cash & Savings – Worked Example | DailyPdfLife",
 desc="A simple step-by-step method to work out zakat at 2.5%: nisab by gold or silver, 21K and 22K gold, savings, debts, with a full worked example in riyals.",
 date="2026-11-27",
 tools=[("Zakat calculator","zakat-calculator.html"),("Hijri date converter","hijri-converter.html"),("Unit converter","unit-converter.html")],
 body="""
<p>Zakat is one of the five pillars of Islam: 2.5% of qualifying wealth, paid once a lunar year by every Muslim whose wealth stays above a minimum amount called the nisab. The idea is simple, but questions come up every year: Which gold counts? How do I value 21-karat jewellery? Do I subtract my loan? This guide walks through the usual method with an example. The <a href="zakat-calculator.html">Zakat calculator</a> does the arithmetic for you.</p>

<h2>Step 1: Choose your zakat date</h2>
<p>Zakat is due when your wealth has stayed at or above the nisab for one full lunar (Hijri) year, called the hawl. Many people pick a fixed date, such as 1 Ramadan, and calculate every year on that day. Use the <a href="hijri-converter.html">Hijri date converter</a> to find the matching Gregorian date each year.</p>

<h2>Step 2: Work out the nisab</h2>
<p>The nisab is the value of <b>85 grams of gold</b> or <b>595 grams of silver</b> on your zakat date. Check today's price per gram with a jeweller or bank.</p>
<ul>
<li>If 24K gold is SAR 400 per gram: gold nisab = 85 × 400 = SAR 34,000.</li>
<li>If silver is SAR 5 per gram: silver nisab = 595 × 5 = SAR 2,975.</li>
</ul>
<p>Because silver is much cheaper, the silver nisab is far lower, so more people pass it. Many scholars recommend the silver nisab as the more cautious choice for cash savings; others use gold. Follow the view of a scholar you trust.</p>

<h2>Step 3: Add up what you own</h2>
<ul>
<li>Cash at home and in your wallet.</li>
<li>Money in current and savings accounts.</li>
<li>Gold and silver, valued at today's price.</li>
<li>Money others owe you that you expect to receive.</li>
<li>Shares, funds and investments at today's value.</li>
<li>Goods you hold for sale in a business, at selling price.</li>
</ul>
<p>Your home, car, furniture, clothes and the tools you use for work do not count.</p>

<h2>Valuing 21K and 22K gold</h2>
<p>Jewellery in the Gulf and South Asia is usually 21K or 22K, which is not pure gold. Multiply the weight by the karat and divide by 24 to get the pure gold content: 50 grams of 21K gold = 50 × 21 ÷ 24 = 43.75 grams of pure gold. Multiply by the 24K price to get its value. For weights in tola, 1 tola = 11.664 grams; the <a href="unit-converter.html">Unit converter</a> converts for you. Scholars differ on whether gold jewellery that is worn regularly is zakatable; many say it is, others exempt it.</p>

<h2>Step 4: Subtract debts due now</h2>
<p>Subtract debts and bills you must pay soon, such as an instalment due this month, unpaid rent or salaries you owe. For long-term loans such as home finance, many scholars allow subtracting only the payments currently due, not the whole balance.</p>

<h2>Worked example</h2>
<table class="gt">
<tr><th>Item</th><th>Value (SAR)</th></tr>
<tr><td>Bank savings</td><td>28,000</td></tr>
<tr><td>Cash at home</td><td>2,000</td></tr>
<tr><td>50 g of 21K gold (43.75 g pure × 400)</td><td>17,500</td></tr>
<tr><td>Money a friend owes you</td><td>3,000</td></tr>
<tr><td>Minus: credit card bill due now</td><td>−2,500</td></tr>
<tr><td><b>Net zakatable wealth</b></td><td><b>48,000</b></td></tr>
</table>
<p>48,000 is above the nisab whether you use gold (34,000) or silver (2,975), so zakat is due: 48,000 × 2.5% = <b>SAR 1,200</b>. The prices in this example are only for illustration.</p>

<h2>Who receives zakat</h2>
<p>The Quran (9:60) names eight groups, including the poor, the needy and those in debt. Many people give through trusted charities or official platforms, or directly to relatives in need who are eligible. This guide explains a general method; for your own situation, especially business assets, pensions or shared property, ask a qualified scholar.</p>
"""))

ARTICLES.append(dict(
 slug="guide-cv-for-gulf-jobs",
 h1="How to write a CV for jobs in Saudi Arabia, UAE and the Gulf",
 title="CV Format for Saudi Arabia, UAE & Gulf Jobs – Tips & Example | DailyPdfLife",
 desc="What Gulf employers expect on a CV: personal details, visa status, photo, experience written as results, skills, languages and certificates, with a section-by-section layout.",
 date="2026-11-27",
 tools=[("CV maker","cv-maker.html"),("Cover letter","cover-letter.html"),("Passport photo","passport-photo.html")],
 body="""
<p>Recruiters in Saudi Arabia, the UAE, Qatar and the rest of the Gulf often receive hundreds of CVs for one job and spend less than a minute on each. A clear CV that gives them the details they care about, in the order they expect, makes a real difference. Gulf CVs also differ from UK or US CVs in a few ways, mainly in personal details. Here is a section-by-section guide you can follow in the free <a href="cv-maker.html">CV maker</a>.</p>

<h2>1. Header and personal details</h2>
<p>Put your full name as it appears in your passport, your job title (for example “Mechanical Site Engineer – MEP”), mobile number with country code, email and city. Gulf employers commonly expect a few more details than Western ones:</p>
<ul>
<li><b>Nationality</b> and, if you are already in the country, your <b>visa or Iqama status</b>, for example “Iqama transferable” or “Available on visit visa”.</li>
<li><b>Driving licence</b>, especially a Saudi, UAE or GCC licence, which matters for field and sales roles.</li>
<li><b>Notice period</b> or availability date.</li>
<li>A <b>professional photo</b> is common and often expected. Use a plain background and business clothes; the <a href="passport-photo.html">Passport photo</a> tool can clean up the background.</li>
</ul>
<p>Date of birth and marital status are still often included in the region, but they are optional. Never include your passport or Iqama number on a CV you send to many companies.</p>

<h2>2. Profile</h2>
<p>Three or four lines that say who you are, your years of experience, your main area and what you're looking for. Example: “MEP engineer with 8 years in hospital and residential projects in Saudi Arabia. Experienced in plumbing and fire-fighting design review, site supervision and handover. Saudi Council of Engineers registered.”</p>

<h2>3. Work experience</h2>
<p>List jobs from newest to oldest with job title, company, city and dates. Under each, write two to five bullet points that show <b>results</b>, not just duties. Compare:</p>
<ul>
<li>Weak: “Responsible for site supervision.”</li>
<li>Strong: “Supervised 25 technicians on a 300-bed hospital project; handed over on schedule with zero lost-time incidents.”</li>
</ul>
<p>Numbers such as project size, budget, team size, sales targets or time saved make your experience easy to judge. Mention well-known clients or projects; recognisable names help in the Gulf.</p>

<h2>4. Education and certificates</h2>
<p>Give your highest qualification, the institution and the year. Professional registrations and certificates often matter as much as degrees: Saudi Council of Engineers or UAE engineering registration, NEBOSH or OSHA safety, PMP, accounting qualifications, nursing and medical licences (often with DataFlow verification). List them clearly with the year.</p>

<h2>5. Skills and languages</h2>
<p>List specific skills: software (AutoCAD, Revit, SAP, Excel, Tally), equipment and technical areas. For languages, English and Arabic are especially valued; give an honest level for each, plus your other languages such as Bangla, Urdu, Hindi or Tagalog, which can help in teams and customer roles.</p>

<h2>6. Length, format and file</h2>
<ul>
<li>Keep it to <b>two pages</b>, or one if you have under five years' experience.</li>
<li>Use a simple layout. Many companies use applicant tracking systems that read text, so avoid putting important words inside images.</li>
<li>Use words from the job advert, such as the exact job title and required skills, where they truthfully describe you.</li>
<li>Send it as a <b>PDF</b> named clearly, for example <code>Ahmed-Rahman-MEP-Engineer-CV.pdf</code>.</li>
</ul>

<h2>7. Add a short cover letter</h2>
<p>A brief cover letter or email that names the job and gives two reasons you fit helps you stand out. The <a href="cover-letter.html">Cover letter</a> maker gives you a starting draft to edit. Finally, check spelling, phone number and email twice; a single wrong digit can cost you an interview.</p>
"""))
