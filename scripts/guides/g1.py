# Guide text for tool pages, part 1 (PDF tools).
# Each entry: title, desc, sections [(heading, html)], faq [(q, a)], related [(label, href)]
G = {}

G["pdf-viewer.html"] = dict(
 title="Free Online PDF Viewer – Read, Zoom & Search PDFs | DailyPdfLife",
 desc="Open and read any PDF in your browser. Zoom, search for words, jump between pages and use night mode. Works offline on phones and computers, nothing is uploaded.",
 sections=[
  ("About the PDF viewer", "<p>The DailyPdfLife PDF viewer opens a PDF file directly on your phone or computer so you can read it without installing a separate reader app. Pick a file or drag it onto the page and it appears straight away. You can zoom in on small print, fit the page to the width of your screen, search for any word or number, and switch to night mode when you read late in the evening. Password-protected PDFs open too, as long as you know the password.</p>"),
  ("How to open and read a PDF", "<ol><li>Tap <b>Open a PDF</b> or drag the file onto the page.</li><li>Scroll to read. Use the arrows or type a page number to jump to a page.</li><li>Pinch, or use the <b>+</b> and <b>−</b> buttons, to zoom. The ↔ button fits the page to your screen width.</li><li>Tap 🔍 and type a word to find every place it appears in the document.</li><li>Tap 🌙 for night mode, or ⬇ to save a copy of the file.</li></ol>"),
  ("When it is useful", "<p>Many people receive bills, bank statements, tickets, salary slips and government letters as PDF files on WhatsApp or email. On a shared or office computer you may not want to install anything, and on a phone the built-in viewer is often slow or lacks search. This viewer loads in a second, works the same way on Android, iPhone, Windows and Mac, and keeps the file on your own device. It is also handy for checking a PDF you just made with one of our other tools before you send it.</p>"),
 ],
 faq=[
  ("Is my PDF uploaded to a server?", "No. The file is read by your browser on your own device. It is never sent to DailyPdfLife or anyone else."),
  ("Can I open a password-protected PDF?", "Yes. The viewer asks for the password and then opens the file. If you want to remove the password for good, use the Unlock PDF tool."),
  ("Does it work offline?", "Once the page has loaded, or if you installed DailyPdfLife as an app, you can open PDFs without an internet connection."),
  ("Can I search inside a scanned PDF?", "Search works on PDFs that contain real text. A scanned page is a picture, so run it through the OCR tool first to turn it into searchable text."),
 ],
 related=[("Edit PDF","pdf-editor.html"),("Unlock PDF","unlock-pdf.html"),("OCR","ocr.html")])

G["merge-and-jpg.html"] = dict(
 title="Merge PDF & JPG to PDF – Combine Files Free Online | DailyPdfLife",
 desc="Join several PDF files into one, or turn JPG and PNG images into a PDF. Free, fast and private: your files are processed in your browser and never uploaded.",
 sections=[
  ("About Merge PDF and JPG to PDF", "<p>This page has two everyday tools. <b>Merge PDF</b> joins several PDF files into a single document, in the order you choose. <b>JPG to PDF</b> turns one or more photos or screenshots into a PDF, with each image on its own page. Both run entirely in your browser, so they are quick even on a slow connection and your documents stay private.</p>"),
  ("How to merge PDF files", "<ol><li>Under <b>Merge PDF</b>, choose the PDF files you want to join. On a computer, hold Ctrl (or Cmd on Mac) to pick several at once.</li><li>The files are joined in the order you pick them, so select the first document first.</li><li>Tap <b>Merge PDF</b> and save the combined file.</li></ol><p>Need to change the page order afterwards or drop a page? Open the result in <a href=\"organize-pdf.html\">Organize PDF</a>.</p>"),
  ("How to turn images into a PDF", "<ol><li>Under <b>JPG to PDF</b>, choose one or more JPG or PNG images.</li><li>Tap <b>Convert to PDF</b>. Every image becomes one page.</li><li>Save the PDF and share it by email or WhatsApp.</li></ol>"),
  ("Common uses", "<p>Merging is ideal when an office or embassy asks for “one PDF file”: put your application form, passport copy, Iqama or ID copy and supporting letters into a single document. JPG to PDF is the quickest way to send photographed receipts, certificates or handwritten notes as a proper document. If your photos are of paper pages, <a href=\"scan-to-pdf.html\">Scan to PDF</a> also straightens and cleans them so they look like a real scan.</p>"),
 ],
 faq=[
  ("Is there a limit on the number of files?", "There is no fixed limit. Very large files depend on the memory of your device; most phones handle dozens of normal documents easily."),
  ("Will merging reduce the quality?", "No. Pages are copied as they are, so text stays sharp and selectable."),
  ("Can I merge password-protected PDFs?", "Remove the password first with the Unlock PDF tool (you need to know the password), then merge."),
  ("The merged file is too big to email. What can I do?", "Run it through Compress PDF to make it smaller before sending."),
 ],
 related=[("Organize PDF","organize-pdf.html"),("Compress PDF","split-and-compress.html#compress"),("Scan to PDF","scan-to-pdf.html")])

G["split-and-compress.html"] = dict(
 title="Split PDF & Compress PDF – Free Online, No Upload | DailyPdfLife",
 desc="Split a PDF into separate pages or page ranges, and compress PDF files to a smaller size for email and upload portals. Free, private and works on any device.",
 sections=[
  ("About Split PDF and Compress PDF", "<p><b>Split PDF</b> breaks a document apart, either into one file per page or into the page ranges you type, such as 1-3, 5, 8-10. <b>Compress PDF</b> makes a file smaller so it fits email attachment limits and the upload size limits of government, visa and job portals. Both tools work in your browser, so your documents are never uploaded.</p>"),
  ("How to split a PDF", "<ol><li>Choose your PDF under <b>Split PDF</b>.</li><li>Pick <b>Every page as its own file</b>, or choose <b>Specific pages</b> and type the pages you want, for example <code>1-3, 5, 8-10</code>.</li><li>Tap <b>Split PDF</b> and save the new files.</li></ol>"),
  ("How to compress a PDF", "<ol><li>Choose your PDF under <b>Compress PDF</b>.</li><li>Pick a level: <b>Light</b> keeps the best quality, <b>Medium</b> is the best balance for most files, and <b>Heavy</b> makes the smallest file.</li><li>Tap <b>Compress PDF</b>. The new size is shown so you can compare it with the original.</li></ol>"),
  ("Tips for the smallest file", "<p>Compression works best on PDFs made from scans and photos, because the images inside can be stored more efficiently. A PDF that is mostly text is usually small already and will shrink less. If a portal asks for a file under 1 MB or 2 MB, start with Medium and only try Heavy if it is still too big. You can also remove pages you don't need with <a href=\"remove-pages.html\">Remove pages</a> before compressing.</p>"),
 ],
 faq=[
  ("Does compressing a PDF reduce quality?", "Light and Medium keep text sharp and photos clear for normal viewing. Heavy compression lowers image quality more to reach the smallest size."),
  ("Can I split out just one page?", "Yes. Choose Specific pages and type the page number, for example 4."),
  ("Is my file uploaded anywhere?", "No. Splitting and compressing happen on your own device."),
  ("Why did my file barely get smaller?", "It probably contains mostly text, which is already compact. Scanned or photo-heavy PDFs shrink the most."),
 ],
 related=[("Remove pages","remove-pages.html"),("Merge PDF","merge-and-jpg.html#merge"),("Organize PDF","organize-pdf.html")])

G["pdf-editor.html"] = dict(
 title="Free PDF Editor Online – Add Text, Sign & Whiteout | DailyPdfLife",
 desc="Edit PDF files in your browser: add or change text, draw, highlight, add images and shapes, white out mistakes and sign. Works with Bangla, Arabic and English text.",
 sections=[
  ("About the PDF editor", "<p>The DailyPdfLife PDF editor lets you make changes to a PDF without Adobe Acrobat. You can type new text anywhere on a page, edit existing text, highlight lines, draw freehand, add boxes, circles and arrows, insert a picture, cover mistakes with whiteout, and draw your signature and place it on the page. Text in any language, including Bangla and Arabic, prints correctly in the saved file.</p>"),
  ("How to edit a PDF", "<ol><li>Open your PDF. The pages appear on the left and the selected page in the middle.</li><li>Choose a tool from the toolbar: <b>Text</b> to add words, <b>Edit text</b> to change existing words, <b>Highlight</b>, <b>Draw</b>, shapes, <b>Image</b> or <b>Whiteout</b>.</li><li>Click on the page to place it. Use the panel to change colour, size, font and thickness.</li><li>To sign, choose <b>Signature</b>, draw it with your finger or mouse, then place it and resize it.</li><li>Tap <b>Save PDF</b> to download the edited file.</li></ol>"),
  ("Good to know", "<p>Use <b>Whiteout</b> and then <b>Text</b> to correct a wrong date, name or amount on a form. Whiteout only covers the area visually; if you need to remove private information so it can never be recovered, use <a href=\"redact-pdf.html\">Redact PDF</a> instead. If the PDF has proper fillable boxes, <a href=\"fill-pdf-forms.html\">Fill PDF forms</a> is faster. Undo and redo are available for every change, so you can experiment freely.</p>"),
 ],
 faq=[
  ("Is the PDF editor free?", "Yes, every feature is free with no sign-up and no watermark on your file."),
  ("Can I sign a PDF with it?", "Yes. Draw your signature once, then place it on any page and resize it."),
  ("Can I edit a scanned PDF?", "You can add text, shapes, whiteout and signatures on top of a scanned page. Changing the original words of a scan is not possible because they are part of an image."),
  ("Does it work on a phone?", "Yes, it works in Chrome and Safari on Android and iPhone, as well as on computers."),
 ],
 related=[("Fill PDF forms","fill-pdf-forms.html"),("Stamp PDF","stamp-pdf.html"),("Redact PDF","redact-pdf.html")])

G["more-tools.html"] = dict(
 title="Rotate PDF, Add Page Numbers & Watermark PDF Free | DailyPdfLife",
 desc="Rotate PDF pages, add page numbers in the style you like, and stamp a text watermark across every page. Free online tools that run in your browser.",
 sections=[
  ("About these PDF tools", "<p>This page brings together three quick fixes for PDF files. <b>Rotate PDF</b> turns pages that were scanned sideways or upside down. <b>Add page numbers</b> puts a number on every page, at the bottom or top, as plain numbers or as “Page 1 of 10”. <b>Add watermark</b> writes a word such as DRAFT, CONFIDENTIAL or your company name across every page in the colour and strength you choose.</p>"),
  ("How to rotate a PDF", "<ol><li>Choose the PDF under <b>Rotate PDF</b>.</li><li>Pick 90° right, 180° or 90° left.</li><li>Tap <b>Rotate</b> and save. To rotate only some pages, use <a href=\"organize-pdf.html\">Organize PDF</a>.</li></ol>"),
  ("How to add page numbers", "<ol><li>Choose the PDF under <b>Add page numbers</b>.</li><li>Pick the position, such as bottom centre or bottom right, and the style “1, 2, 3” or “Page 1 of 10”.</li><li>Tap <b>Add numbers</b> and save.</li></ol>"),
  ("How to watermark a PDF", "<ol><li>Choose the PDF under <b>Add watermark</b> and type your text.</li><li>Choose a colour and how strong it should look: light, medium or strong.</li><li>Tap <b>Add watermark</b> and save the new file.</li></ol><p>A light watermark keeps the document easy to read while still showing that it is a draft or a copy. To add a stamp like PAID or APPROVED, or a company seal image, use <a href=\"stamp-pdf.html\">Stamp PDF</a>.</p>"),
 ],
 faq=[
  ("Will rotating change the quality of my PDF?", "No. Only the page direction changes; the text and images stay exactly the same."),
  ("Can I start page numbering from a different number?", "The tool numbers from the first page. Remove or split off a cover page first if you want numbering to start later."),
  ("Can the watermark be removed later?", "The watermark is written onto every page of the saved file, so keep your original if you may need a clean copy."),
  ("Are my files uploaded?", "No, all three tools work on your own device."),
 ],
 related=[("Organize PDF","organize-pdf.html"),("Stamp PDF","stamp-pdf.html"),("PDF editor","pdf-editor.html")])

G["pdf-password.html"] = dict(
 title="Protect PDF with Password – AES-256 Encryption Free | DailyPdfLife",
 desc="Add a password to a PDF with strong AES-256 encryption and control printing, copying and editing. Free, private and nothing is uploaded.",
 sections=[
  ("About Protect PDF", "<p>Protect PDF locks a document with a password so that nobody can open it without that password. It uses AES-256 encryption, the same strong standard used by Adobe Acrobat, and keeps your text, links and quality exactly as they were. You can also choose whether people who open the file may print it, copy its text or edit it.</p>"),
  ("How to password-protect a PDF", "<ol><li>Choose your PDF.</li><li>Type a password. Tick <b>Show password</b> to check it is typed correctly.</li><li>Choose what is allowed after opening: printing, copying text, editing.</li><li>Tap <b>Protect it</b> and save the locked file.</li></ol>"),
  ("Choosing a good password", "<p>Use at least 8 to 12 characters and mix words with numbers, for example a short phrase that only you and the receiver know. Do not send the password in the same email or chat message as the file; send it by SMS or say it on a call. Keep a copy of the password somewhere safe. Because the encryption is strong and done on your device, nobody, including DailyPdfLife, can open the file or recover the password for you.</p>"),
  ("When to protect a PDF", "<p>Protect salary slips, bank statements, contracts, medical reports, ID copies and customer invoices before sending them by email or storing them in shared folders. Many banks and companies already send statements this way; now you can do the same for your own documents.</p>"),
 ],
 faq=[
  ("How strong is the protection?", "The file is encrypted with AES-256, which cannot be broken by guessing in any practical amount of time if the password is good."),
  ("I forgot the password. Can you unlock it?", "No. The password never leaves your device and there is no back door, so keep it safe."),
  ("Can I remove the password later?", "Yes, open the file with its password in the Unlock PDF tool and save an unlocked copy."),
  ("Is my document uploaded?", "No. The encryption happens in your browser."),
 ],
 related=[("Unlock PDF","unlock-pdf.html"),("Redact PDF","redact-pdf.html"),("Compress PDF","split-and-compress.html#compress")])

G["organize-pdf.html"] = dict(
 title="Organize PDF Pages – Reorder, Rotate & Delete Free | DailyPdfLife",
 desc="Rearrange PDF pages by dragging, rotate single pages, delete pages and combine pages from several PDFs into one. Free and private, right in your browser.",
 sections=[
  ("About Organize PDF", "<p>Organize PDF shows every page of your document as a thumbnail so you can put it in the right order. Drag pages to move them, rotate any single page, remove pages you don't need, and add more PDFs to mix their pages together. When everything looks right, save it as one new PDF.</p>"),
  ("How to organize PDF pages", "<ol><li>Choose one or more PDFs, or drag them onto the page.</li><li>Drag a page thumbnail to its new place.</li><li>Use the buttons under a page to rotate it or remove it.</li><li>Tap <b>Add another PDF</b> to bring in pages from more files.</li><li>Use <b>Reverse order</b> if the pages were scanned back to front, or <b>Undo removals</b> to bring pages back.</li><li>Tap <b>Save PDF</b>.</li></ol>"),
  ("Typical jobs", "<p>Fix a scanned document where page 2 ended up at the end, turn the one page that was scanned sideways, take out blank pages, or build a single application file from several documents in the exact order an office asks for. Because you see every page while you work, it is easier than typing page numbers.</p>"),
 ],
 faq=[
  ("Can I combine pages from different PDFs?", "Yes. Add another PDF and drag its pages between the pages of the first one."),
  ("Does it change the quality of the pages?", "No. Pages are moved and rotated without being re-drawn, so text stays sharp."),
  ("How do I remove many pages at once?", "For large documents, Remove pages lets you select odd pages, even pages or ranges in one go."),
  ("Are my files uploaded?", "No, everything happens on your device."),
 ],
 related=[("Merge PDF","merge-and-jpg.html#merge"),("Remove pages","remove-pages.html"),("Rotate PDF","more-tools.html#rotate")])

G["unlock-pdf.html"] = dict(
 title="Unlock PDF – Remove Password from PDF Free | DailyPdfLife",
 desc="Remove the password and printing or copying restrictions from a PDF you can already open. Enter the password once and save an unlocked copy. Free and private.",
 sections=[
  ("About Unlock PDF", "<p>Banks, telecom companies and employers often send statements and salary slips as password-protected PDFs. Typing the password every time is tiresome, and some upload portals refuse locked files. Unlock PDF removes the password, and any printing or copying restrictions, from a PDF you are allowed to open. The text, pages and quality stay exactly the same.</p>"),
  ("How to unlock a PDF", "<ol><li>Choose the locked PDF.</li><li>Type its password. Tap <b>Show</b> to check it.</li><li>Tap <b>Unlock PDF</b> and save the unlocked copy.</li></ol>"),
  ("Finding the password", "<p>Banks usually explain the password in the email or SMS that came with the statement. It is often a combination such as part of your name with your date of birth, or the last digits of your account, ID or mobile number. Check that message carefully. This tool does not guess or crack passwords: you need to know the password, and you should only unlock files you own or have permission to change.</p>"),
 ],
 faq=[
  ("Can it unlock a PDF without the password?", "No. If a PDF needs a password to open, you must enter it. Only restrictions on printing and copying can be removed from files that open without a password."),
  ("Is the unlocked file the same quality?", "Yes. Nothing is converted or redrawn; only the encryption is removed."),
  ("Is it safe to unlock bank statements here?", "Yes. The file and password stay on your device and are never uploaded."),
  ("Can I add a new password afterwards?", "Yes, use Protect PDF to lock it again with a password of your choice."),
 ],
 related=[("Protect PDF","pdf-password.html"),("PDF viewer","pdf-viewer.html"),("PDF to Excel","pdf-to-excel.html")])

G["fill-pdf-forms.html"] = dict(
 title="Fill PDF Forms Online Free – Type Into Fillable PDFs | DailyPdfLife",
 desc="Fill in fillable PDF forms in your browser: type into text boxes, tick checkboxes and pick options, then save or lock the answers. Free and nothing is uploaded.",
 sections=[
  ("About Fill PDF forms", "<p>Many application forms from embassies, banks, schools and government offices are fillable PDFs with boxes you can type into. This tool lists every field in the form so you can fill it neatly on a phone or computer, then save a completed copy. You can also lock (flatten) the answers so they can no longer be changed.</p>"),
  ("How to fill a PDF form", "<ol><li>Choose the PDF form.</li><li>Type your answers in the field list, or click a box on the page preview to jump to that field.</li><li>Tick <b>Lock the answers (flatten)</b> if you are sending the final version.</li><li>Tap <b>Save PDF</b>.</li></ol>"),
  ("If your form has no boxes", "<p>Some PDFs are just printed forms without fillable fields. In that case nothing appears in the field list. Open the file in the <a href=\"pdf-editor.html\">PDF editor</a> instead and use the Text tool to type on the lines, then add your signature. Always check names, passport numbers and dates against your documents before submitting; a small typo can delay an application.</p>"),
 ],
 faq=[
  ("Which forms work?", "PDFs with fillable fields, also called AcroForms. Most official forms downloaded from websites are this type."),
  ("What does flatten mean?", "Flattening turns your answers into normal page content so they can't be edited any more. Use it for the final copy you send."),
  ("Can I sign the form too?", "Save the filled form, then open it in the PDF editor and add your signature."),
  ("Is my information uploaded?", "No. The form is filled on your device."),
 ],
 related=[("PDF editor","pdf-editor.html"),("Stamp PDF","stamp-pdf.html"),("Merge PDF","merge-and-jpg.html#merge")])
