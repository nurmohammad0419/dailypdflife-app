# Guide text, part 4 (tools added in November 2026)
G = {}

def T(title, desc, about, steps, tips_h, tips, faq, related):
    return dict(title=title, desc=desc, sections=[(about[0], about[1]), (steps[0], steps[1]), (tips_h, tips)], faq=faq, related=related)

G["sign-pdf.html"] = T(
 "Sign PDF Online Free – Draw, Type or Upload Signature | DailyPdfLife",
 "Sign a PDF in your browser: draw your signature with your finger, type it in a handwriting font or upload a photo of it, then place it on any page and add the date.",
 ("About Sign PDF", "<p>Sign PDF lets you sign contracts, offer letters, tenancy agreements and school forms without printing them. Make your signature once by drawing it with your finger or mouse, typing your name in a handwriting style, or uploading a photo of your real signature on paper. Then tap anywhere on a page to place it, drag it into position, resize it and add today's date or your initials. The signed PDF keeps all the original text sharp.</p>"),
 ("How to sign a PDF", "<ol><li>Choose your PDF. Every page appears on the right.</li><li>Make your signature: <b>Draw</b>, <b>Type</b> or <b>Upload</b>, and pick black, blue or green ink.</li><li>Tap the page where you want to sign. Drag the signature to move it and use the red dot to resize it.</li><li>Add the date or extra text such as your initials if needed.</li><li>Tap <b>Sign &amp; save PDF</b>.</li></ol>"),
 "Tips",
 "<p>Blue ink makes it obvious that a copy was signed rather than photocopied. For the most natural result, photograph your real signature on clean white paper and use <b>Upload</b>; the paper is removed automatically. A signature you create in the <a href=\"signature-maker.html\">Signature maker</a> is remembered on this device and appears here ready to use. Some banks and government services need a certified digital signature instead of a drawn one, so check if you're unsure.</p>",
 [("Is a drawn signature legally valid?", "For most private documents such as offer letters, quotations and many contracts, yes. Some official transactions require a certified e-signature service."),
  ("Can I sign several pages?", "Yes, tap each page where a signature or initials are needed."),
  ("Can I write in Bangla or Arabic?", "Yes. Text you add is saved as a sharp image, so any language works."),
  ("Is my document uploaded?", "No, signing happens on your own device.")],
 [("Signature maker", "signature-maker.html"), ("Fill PDF forms", "fill-pdf-forms.html"), ("Stamp PDF", "stamp-pdf.html")])

G["compare-pdf.html"] = T(
 "Compare PDF Files – Find Differences Between Two PDFs | DailyPdfLife",
 "Compare two PDF versions and see every added, removed and changed line highlighted. Ideal for contracts, offers and reports. Free and private, nothing uploaded.",
 ("About Compare PDF", "<p>When someone sends you “the updated contract”, it is hard to see what actually changed. Compare PDF reads the text of the old and the new version and lists every line that was added, removed or changed, with the exact words highlighted: deleted words in red and new words in green. You can choose to see only the changes or the whole document.</p>"),
 ("How to compare two PDFs", "<ol><li>Choose the original (old) PDF and the new (changed) PDF.</li><li>Keep <b>Ignore extra spaces</b> on so layout changes don't show as differences.</li><li>Tap <b>Compare PDFs</b>.</li><li>Read the summary, then check each highlighted line.</li></ol>"),
 "What to look for",
 "<p>In contracts and tenancy agreements, pay special attention to amounts, dates, notice periods, penalties and the names of the parties; a single changed number can matter a lot. Compare PDF works on the text inside the file, so it is best for documents made on a computer. Scanned PDFs contain pictures instead of text; run them through <a href=\"ocr.html\">OCR</a> first.</p>",
 [("Does it compare pictures and layout?", "No, it compares the text. Changes in images, colours or fonts are not shown."),
  ("Can it compare scanned documents?", "Use OCR on both files first, then compare the results."),
  ("Is there a size limit?", "Very long documents can be slow on phones; split them into parts if needed."),
  ("Are my files uploaded?", "No, both files are read on your device.")],
 [("PDF to text", "pdf-to-text.html"), ("OCR", "ocr.html"), ("PDF to Word", "pdf-to-word.html")])

G["flatten-pdf.html"] = T(
 "Flatten PDF Online – Lock Form Fields & Annotations | DailyPdfLife",
 "Flatten a PDF so filled-in form fields, comments and stamps become part of the page and can't be edited. Keep text sharp or flatten everything into images.",
 ("About Flatten PDF", "<p>A filled PDF form can still be edited by anyone who opens it, and some programs show the answers differently or even lose them. Flattening turns the answers, ticks and dropdown choices into normal page content, so the document looks the same everywhere and can no longer be changed. Choose <b>Lock form fields</b> to keep text sharp and searchable, or <b>Flatten everything</b> to turn each page into a single picture, including comments, highlights and stamps.</p>"),
 ("How to flatten a PDF", "<ol><li>Choose your PDF.</li><li>Pick <b>Lock form fields</b> or <b>Flatten everything</b>.</li><li>For “Flatten everything”, choose the quality.</li><li>Tap <b>Flatten PDF</b> and save the new file.</li></ol>"),
 "When to flatten",
 "<p>Flatten the final copy of an application form before you send it, invoices and quotations you don't want changed, and documents with comments or stamps that must print correctly. Keep your editable original in case you need to change something later. To fill the form first, use <a href=\"fill-pdf-forms.html\">Fill PDF forms</a>.</p>",
 [("Will the text stay searchable?", "With Lock form fields, yes. Flatten everything turns pages into pictures, so text can't be selected."),
  ("Can I undo flattening?", "No, so keep your original file."),
  ("Why does my PDF say it has no form fields?", "It may be a printed form without fillable boxes. Use Flatten everything instead."),
  ("Is my file uploaded?", "No, flattening happens in your browser.")],
 [("Fill PDF forms", "fill-pdf-forms.html"), ("Sign PDF", "sign-pdf.html"), ("Protect PDF", "pdf-password.html")])

G["grayscale-pdf.html"] = T(
 "Grayscale PDF – Convert Colour PDF to Black & White Free | DailyPdfLife",
 "Turn a colour PDF into grayscale or crisp black and white to save printer ink and meet upload rules. Free, private and works on phones.",
 ("About Grayscale PDF", "<p>Printing colour pages on a colour printer uses expensive ink, and some offices and portals ask for black-and-white copies. Grayscale PDF turns every page into shades of grey, or into crisp black and white that makes scanned text easier to read. It also often makes scanned documents smaller.</p>"),
 ("How to make a PDF grayscale", "<ol><li>Choose your PDF.</li><li>Pick <b>Grayscale</b> for photos and charts, or <b>Black &amp; white</b> for text documents.</li><li>Choose the quality: Normal for email, Print for paper.</li><li>Tap <b>Make it grayscale</b> and save.</li></ol>"),
 "Good to know",
 "<p>Pages are redrawn as images, so text in the new file can't be selected or searched. If you need that, keep the colour original for searching and use the grayscale copy for printing. To reduce the size further, run the result through <a href=\"split-and-compress.html#compress\">Compress PDF</a>.</p>",
 [("Will this save printer ink?", "Yes, printers use only black ink for grayscale pages when set to print in black and white."),
  ("Which option is best for scanned letters?", "Black &amp; white usually gives the cleanest, most readable result."),
  ("Is the text still selectable?", "No, pages become images."),
  ("Is my file uploaded?", "No.")],
 [("Compress PDF", "split-and-compress.html#compress"), ("Scan to PDF", "scan-to-pdf.html"), ("PDF to PNG", "pdf-to-png.html")])

G["pdf-to-png.html"] = T(
 "PDF to PNG Converter – High Quality, Transparent Option | DailyPdfLife",
 "Convert PDF pages to sharp PNG, WEBP or JPG images at screen or 300 dpi print quality. Pick the pages you need. Free and private.",
 ("About PDF to PNG", "<p>PNG keeps text and lines perfectly sharp, which makes it the best image format for documents, diagrams, certificates and slides. This tool turns the pages you choose into PNG images at screen, high or 300 dpi print resolution. It can also make WEBP images for websites or JPG for smaller files, and PNG pages can have a transparent background.</p>"),
 ("How to convert PDF to PNG", "<ol><li>Choose your PDF.</li><li>Pick the format and resolution. 144 dpi is ideal for screens; 300 dpi for printing.</li><li>Type page numbers such as <code>1-3, 5</code>, or leave empty for all pages.</li><li>Tap <b>Convert to images</b> and save the pictures.</li></ol>"),
 "PNG, JPG or WEBP?",
 "<p>Choose PNG for documents and anything with text; it never adds blurry edges. JPG files are smaller and fine for photos. WEBP gives the smallest files with good quality and works in all modern browsers. A transparent background is useful for logos and signatures exported from a PDF.</p>",
 [("What resolution should I choose?", "High (144 dpi) for screens and sharing, Print (300 dpi) for paper."),
  ("Can I convert only one page?", "Yes, type its number in the Pages box."),
  ("Why are 300 dpi PNG files large?", "PNG is lossless. Choose WEBP or JPG for smaller files."),
  ("Is my PDF uploaded?", "No.")],
 [("PDF to JPG", "pdf-to-jpg.html"), ("JPG to PDF", "merge-and-jpg.html#jpg"), ("Compress image", "image-tools.html#compress")])

G["ppt-to-pdf.html"] = T(
 "PowerPoint to PDF – Convert PPTX to PDF Free Online | DailyPdfLife",
 "Convert PowerPoint .pptx slides to a PDF in your browser, no Office needed. Keeps text, pictures, shapes, tables and backgrounds. Free and private.",
 ("About PowerPoint to PDF", "<p>A PDF is the safest way to send a presentation: it opens on any phone or computer, looks the same everywhere and can't be changed by accident. This tool reads your .pptx file and draws each slide, with its text, pictures, coloured shapes, tables and background, into a PDF page with the same size as your slides. You don't need PowerPoint installed.</p>"),
 ("How to convert PowerPoint to PDF", "<ol><li>Choose your .pptx file.</li><li>Choose the quality and whether to add slide numbers.</li><li>Tap <b>Convert to PDF</b>. A preview of every slide appears.</li><li>Save the PDF.</li></ol>"),
 "What is supported",
 "<p>Text boxes, titles, bullet points, pictures, simple shapes, tables and slide backgrounds are drawn. Charts, SmartArt, videos, animations and some special effects are not, and the tool tells you when it skips something. Slides are saved as high-resolution pictures, so the text in the PDF can't be selected. For perfect results with complex designs, use “Save as PDF” in PowerPoint or Google Slides. Old .ppt files must first be saved as .pptx.</p>",
 [("Do I need Microsoft Office?", "No, the conversion runs in your browser."),
  ("Are animations kept?", "No, a PDF shows each slide as a still page."),
  ("Can I open .ppt files?", "Save them as .pptx in PowerPoint or Google Slides first."),
  ("Is my presentation uploaded?", "No.")],
 [("Word to PDF", "word-to-pdf.html"), ("Excel to PDF", "excel-to-pdf.html"), ("Compress PDF", "split-and-compress.html#compress")])

G["pdf-to-text.html"] = T(
 "PDF to Text – Extract All Text from a PDF to TXT Free | DailyPdfLife",
 "Pull all the text out of a PDF into a plain .txt file or copy it in one tap. Keeps line breaks, marks page starts and can join broken lines.",
 ("About PDF to text", "<p>Sometimes you just need the words: to paste a paragraph into an email, to translate a document, to search it, or to feed it into another program. PDF to text pulls every word out of a PDF, page by page, into plain text you can copy or save as a .txt file. Bangla, Arabic and English text all work when the PDF contains real text.</p>"),
 ("How to extract text from a PDF", "<ol><li>Choose your PDF.</li><li>Keep <b>Mark where each page starts</b> on if you want page numbers in the text.</li><li>Turn on <b>Join broken lines</b> to turn short PDF lines back into flowing paragraphs.</li><li>Tap <b>Extract text</b>, then copy it or save the .txt file.</li></ol>"),
 "If you get no text",
 "<p>A scanned PDF or a photo of a page contains a picture of the words, not the words themselves, so there is nothing to extract. Use <a href=\"ocr.html\">OCR</a> instead, which reads the text from the picture. If copied Bangla text looks broken, read our guide on <a href=\"guide-bangla-pdf-text-copy-broken.html\">why Bangla PDF text breaks</a>.</p>",
 [("Does it keep formatting?", "No, it produces plain text. Use PDF to Word to keep paragraphs in a document."),
  ("Can it read scanned PDFs?", "No, use OCR for those."),
  ("Which encoding is the .txt file?", "UTF-8, which opens correctly in Notepad, Word and phones."),
  ("Is my PDF uploaded?", "No.")],
 [("PDF to Word", "pdf-to-word.html"), ("OCR", "ocr.html"), ("Compare PDF", "compare-pdf.html")])

G["html-to-pdf.html"] = T(
 "HTML to PDF Converter – Turn HTML Files or Text into PDF | DailyPdfLife",
 "Convert an .html file, pasted HTML code or plain text into a clean PDF. Choose A4, Letter or Legal and margins. Free and safe: scripts are never run.",
 ("About HTML to PDF", "<p>Email templates, saved web pages, reports exported from systems and simple notes are often HTML files. HTML to PDF shows a preview of your file or pasted content and saves it as a PDF with the page size and margins you choose. Styles inside the HTML are kept, so headings, colours and tables look right.</p>"),
 ("How to convert HTML to PDF", "<ol><li>Upload an .html file, or paste HTML code or plain text.</li><li>Check the preview.</li><li>Choose the page size and margins.</li><li>Tap <b>Save as PDF</b>. In the print window, choose <b>Save as PDF</b> and tick <b>Background graphics</b>.</li></ol>"),
 "Safety and limits",
 "<p>For your safety, scripts and embedded frames in the HTML are removed and never run. Pictures appear only when they use full web addresses (starting with https://) or are embedded in the file. To save a live website as a PDF, open it in your browser and use Print → Save as PDF. For Word documents use <a href=\"word-to-pdf.html\">Word to PDF</a>.</p>",
 [("Can I convert a website address?", "Open the site in your browser and use Print → Save as PDF; browsers don't let other pages load a site for you."),
  ("Why are my images missing?", "Images with relative paths can't be found. Use full https:// addresses."),
  ("Will JavaScript run?", "No, scripts are removed for safety."),
  ("Is my content uploaded?", "No.")],
 [("Word to PDF", "word-to-pdf.html"), ("PDF to text", "pdf-to-text.html"), ("Merge PDF", "merge-and-jpg.html#merge")])

G["zip-files.html"] = T(
 "ZIP Files Online – Create ZIP or Unzip Files Free | DailyPdfLife",
 "Put many files into one ZIP to send as a single attachment, or open a ZIP on your phone and save the files inside. Free, private, no app needed.",
 ("About ZIP files", "<p>A ZIP file packs many files into one, which makes them easy to attach to an email or upload to a portal that accepts only one file. Phones often can't open ZIP files someone sends you. This page does both: make a ZIP from any files, and open a ZIP to see and save what's inside.</p>"),
 ("How to make or open a ZIP", "<ol><li>To make one: choose your files (you can add more in several goes), type a name and tap <b>Create ZIP</b>.</li><li>To open one: choose the .zip file. The files inside are listed; save one with ⬇ or tap <b>Save all files</b>.</li></ol>"),
 "Good to know",
 "<p>ZIP compression shrinks text files, spreadsheets and Word documents a lot, but photos, videos and PDFs are already compressed and barely get smaller; use <a href=\"split-and-compress.html#compress\">Compress PDF</a> or <a href=\"image-tools.html#compress\">Compress image</a> for those first. Password-protected ZIP files can't be opened here.</p>",
 [("Can I open RAR or 7z files?", "No, only ZIP files."),
  ("Does it work on iPhone and Android?", "Yes, in Safari and Chrome."),
  ("Is there a size limit?", "It depends on your device's memory; a few hundred MB is usually fine."),
  ("Are my files uploaded?", "No.")],
 [("Compress PDF", "split-and-compress.html#compress"), ("Merge PDF", "merge-and-jpg.html#merge"), ("Compress image", "image-tools.html#compress")])

G["image-to-kb.html"] = T(
 "Resize Image to KB – Reduce Photo to 20KB, 50KB, 100KB | DailyPdfLife",
 "Make a photo exactly the file size an online form needs: 20 KB, 50 KB, 100 KB, 200 KB or any size, with optional exact pixels. Free, private and fast.",
 ("About Resize image to KB", "<p>Job portals, visa and Iqama services, university admissions and exam forms often say “photo must be under 50 KB” or “signature under 20 KB”. This tool finds the best quality that fits the size you choose, and makes the picture smaller only if it has to. If the form also asks for exact pixels, such as 300 × 300, type them in and the photo is cropped neatly to fit.</p>"),
 ("How to reduce a photo to a size in KB", "<ol><li>Choose your photo.</li><li>Tap a target size such as <b>50 KB</b>, or type your own.</li><li>Fill in width and height only if the form asks for exact pixels.</li><li>Tap <b>Make it this size</b> and compare before and after.</li><li>Save the photo and upload it.</li></ol>"),
 "Tips",
 "<p>For passport-style photos, make the photo first in the <a href=\"passport-photo.html\">Passport photo maker</a> and then reduce it here. For a signature under 20 KB, create it in the <a href=\"signature-maker.html\">Signature maker</a> and save as JPG. iPhone HEIC photos must be converted with <a href=\"heic-to-jpg.html\">HEIC to JPG</a> first.</p>",
 [("Will the photo look blurry?", "The tool keeps the highest quality that fits. Very small targets on large photos may soften details."),
  ("How do I make a 300×300 photo under 50 KB?", "Type 300 in width and height and choose 50 KB."),
  ("Which format do forms accept?", "Most want JPG, which is the default."),
  ("Is my photo uploaded?", "No.")],
 [("Passport photo", "passport-photo.html"), ("Compress image", "image-tools.html#compress"), ("Signature maker", "signature-maker.html")])

G["signature-maker.html"] = T(
 "Signature Maker – Create Transparent PNG Signature Free | DailyPdfLife",
 "Draw or type your signature, or clean up a photo of it, and download a transparent PNG to use on PDFs, Word documents and forms. Free and private.",
 ("About the Signature maker", "<p>A clean digital signature is handy for signing PDFs, adding to Word letters and invoices, and uploading to job or exam forms. Draw your signature with your finger or mouse, type your name in one of five handwriting styles, or photograph your real signature on paper and let the tool remove the background. Choose the ink colour and download a transparent PNG or a JPG on white.</p>"),
 ("How to make your signature", "<ol><li>Choose <b>Draw</b>, <b>Type</b> or <b>From photo</b>.</li><li>Draw slowly, or type your name and pick a style, or upload your photo and adjust the clean-up strength.</li><li>Pick black, blue, green or dark red ink.</li><li>Download the PNG (transparent) or JPG.</li></ol>"),
 "Using your signature",
 "<p>The PNG has no background, so it sits naturally on any document. Open a PDF in <a href=\"sign-pdf.html\">Sign PDF</a> and your new signature is already loaded. In Word, insert it as a picture and set wrapping to “In front of text”. If a form needs a signature under 20 KB, use <a href=\"image-to-kb.html\">Resize image to KB</a>. Keep your signature file private.</p>",
 [("What is a transparent PNG?", "An image without a background, so only the ink shows on top of your document."),
  ("Is a typed signature valid?", "For many everyday documents yes, but a drawn or photographed signature looks more personal."),
  ("Can I use it on my phone?", "Yes, draw with your finger."),
  ("Is my signature uploaded?", "No, it stays on your device.")],
 [("Sign PDF", "sign-pdf.html"), ("Resize image to KB", "image-to-kb.html"), ("PDF editor", "pdf-editor.html")])

G["photo-enhancer.html"] = T(
 "Photo Enhancer Online – Brighten, Sharpen & Fix Colours | DailyPdfLife",
 "Improve dark, dull or blurry photos in one tap with Auto enhance, or adjust brightness, contrast, colour, warmth, shadows and sharpness. Free, private, no upload.",
 ("About the Photo enhancer", "<p>Phone photos taken indoors or in the evening often come out dark, grey or slightly soft. The Photo enhancer fixes that: <b>Auto enhance</b> balances the light and colours and sharpens the details in one tap, and the sliders let you fine-tune brightness, contrast, colour, warmth, shadows, sharpness and vignette. Presets give quick looks for documents, vivid colours, warm tones or black and white.</p>"),
 ("How to enhance a photo", "<ol><li>Choose a photo.</li><li>Tap <b>Auto enhance</b>, or a preset such as <b>Document</b> for photographed papers.</li><li>Adjust the sliders if you like. Hold <b>See original</b> to compare.</li><li>Choose JPG, PNG or WEBP and save. The full-resolution photo is processed.</li></ol>"),
 "Tips",
 "<p>The Document preset makes photographed papers whiter and the text darker, which is great for receipts and notes; for a proper scan with straightened pages use <a href=\"scan-to-pdf.html\">Scan to PDF</a>. Increase Shadows to brighten faces in backlit photos. Small amounts of sharpness look natural; too much creates halos.</p>",
 [("Can it fix very blurry photos?", "It sharpens slightly soft photos. Badly blurred or shaky photos can't be fully fixed."),
  ("Is the full resolution kept?", "Yes, settings are applied to the original size (up to 4000 pixels)."),
  ("Does it work offline?", "Yes, once the page has loaded."),
  ("Is my photo uploaded?", "No.")],
 [("Remove background", "remove-bg.html"), ("Crop image", "crop-image.html"), ("Compress image", "image-tools.html#compress")])

G["meme-maker.html"] = T(
 "Meme Maker Online Free – Add Top & Bottom Text | DailyPdfLife",
 "Make a meme from your own photo in seconds: classic bold top and bottom text, or a modern white caption bar. Bangla and Arabic text work too. No watermark.",
 ("About the Meme maker", "<p>Turn any photo into a meme. Choose the classic look with big white letters and a black outline at the top and bottom, or the modern caption style with a white bar of text above the picture, as seen on social media. You can also start with a plain coloured background for text-only posts. There's no watermark and nothing is uploaded.</p>"),
 ("How to make a meme", "<ol><li>Choose a photo, or a plain background colour.</li><li>Pick <b>Classic</b> or <b>Caption bar on top</b>.</li><li>Type your text, and adjust the size and colour.</li><li>Tap <b>Save meme</b> and share it.</li></ol>"),
 "Make it land",
 "<p>Short text works best: a few words at the top set up the joke and the bottom line delivers it. Use photos you took yourself or have permission to use, and keep jokes kind. For more text styles and several text boxes, try <a href=\"text-on-photo.html\">Text on photo</a>; to combine pictures first, use <a href=\"photo-collage.html\">Photo collage</a>.</p>",
 [("Can I write in Bangla?", "Yes, Bangla and Arabic text appear correctly."),
  ("Is there a watermark?", "No."),
  ("What size is the saved meme?", "Up to 2000 pixels wide, sharp enough for any social network."),
  ("Is my photo uploaded?", "No.")],
 [("Text on photo", "text-on-photo.html"), ("Photo collage", "photo-collage.html"), ("Crop image", "crop-image.html")])

G["gratuity-calculator.html"] = T(
 "End of Service Calculator Saudi & UAE – Gratuity (EOSB) | DailyPdfLife",
 "Calculate your end-of-service benefit (gratuity) under Saudi and UAE labour law: years of service, wage, resignation or termination, with a full breakdown.",
 ("About the End of service calculator", "<p>When a job ends in Saudi Arabia or the UAE, the employer usually owes an end-of-service benefit, also called gratuity or EOSB. The amount depends on how long you worked, your wage and, in Saudi Arabia, how the job ended. Enter your dates and wage to see the amount and how it was worked out.</p>"),
 ("How it is calculated", "<ul><li><b>Saudi Arabia</b> (Labour Law Articles 84 and 85): half a month's wage for each of the first five years and one month's wage for each year after, based on the last wage, with part-years counted. If you resign, you get nothing under 2 years, one third for 2 to 5 years, two thirds for 5 to 10 years and the full amount after 10 years.</li><li><b>UAE</b> (Decree-Law 33 of 2021, Article 51): 21 days of basic wage per year for the first five years and 30 days per year after, for at least one year of full-time service, up to a maximum of two years' wage. Under the current law, resigning does not reduce it.</li></ul>"),
 "Important",
 "<p>This calculator gives an estimate for typical cases. Special situations change the result: dismissal under Saudi Article 80, leaving under Article 81, women resigning within set periods after marriage or childbirth, part-time contracts, unpaid absences and amounts the employer may legally deduct. Check your contract and confirm with the Ministry of Human Resources (HRSD) in Saudi Arabia or MOHRE in the UAE before you rely on the figure.</p>",
 [("Which wage is used in Saudi Arabia?", "The last actual wage, which normally includes basic salary and fixed allowances such as housing."),
  ("Which wage is used in the UAE?", "The basic salary only."),
  ("Do I get gratuity if I resign in Saudi Arabia before 2 years?", "Not under Article 85, unless a legal exception applies."),
  ("Is my data saved?", "No, the calculation happens on your device.")],
 [("Loan & EMI", "loan-calculator.html"), ("Date calculator", "date-calculator.html"), ("Currency converter", "currency-converter.html")])

G["currency-converter.html"] = T(
 "Currency Converter – SAR to BDT, AED, USD Today's Rate | DailyPdfLife",
 "Convert Saudi riyal, taka, dirham, dollar, rupee and 20+ more currencies at today's mid-market rate, with a quick table of 1 SAR in every currency.",
 ("About the Currency converter", "<p>Whether you're sending money home, paying a supplier abroad or comparing prices, this converter shows how much your money is worth in another currency. It includes the Gulf currencies, taka, Indian and Pakistani rupee, and the world's main currencies, and shows a table of your currency against all the others. Rates update daily and the last update time is shown.</p>"),
 ("How to convert", "<ol><li>Type the amount.</li><li>Choose the currency you have and the one you want. Tap ⇄ to swap them.</li><li>Read the result and the rate in both directions.</li></ol>"),
 "Rates you see vs. rates you get",
 "<p>The rate shown is the mid-market rate, halfway between buying and selling prices. Banks, exchange houses and money transfer apps add a margin and sometimes a fee, so the amount your family receives will be slightly lower. Compare the final amount, not only the advertised rate, before you send. Your last choice of currencies is remembered on this device.</p>",
 [("How often are rates updated?", "Once a day, from Exchange Rate API."),
  ("Does it work offline?", "It uses the last rates saved on your device, and you can type a rate yourself."),
  ("Why is the bank's rate different?", "Banks add a margin to the mid-market rate."),
  ("Which currencies are included?", "More than 20, including SAR, BDT, AED, USD, EUR, GBP, INR and PKR.")],
 [("VAT calculator", "vat-calculator.html"), ("Percentage", "percentage-calculator.html"), ("Zakat calculator", "zakat-calculator.html")])

G["bmi-calculator.html"] = T(
 "BMI Calculator – Body Mass Index with Asian Cut-offs | DailyPdfLife",
 "Calculate your BMI in kg/cm or lb/ft, see your category and the healthy weight range for your height, with the WHO Asian scale for South Asian and Gulf users.",
 ("About the BMI calculator", "<p>Body mass index (BMI) compares your weight with your height. It is a quick way to see whether your weight is in a healthy range. Enter your height and weight in metric or imperial units to see your BMI, your category and the healthy weight range for your height.</p>"),
 ("How BMI is worked out", "<p>BMI = weight in kg ÷ (height in metres)². For example, 70 kg and 1.70 m gives 70 ÷ 2.89 = 24.2. The international WHO categories are: under 18.5 underweight, 18.5 to 24.9 healthy, 25 to 29.9 overweight and 30 or more obesity. The WHO also suggests lower cut-offs for Asian populations, because health risks such as diabetes start at lower BMI: 23 for overweight and 27.5 for obesity. Choose “WHO Asian” if that applies to you.</p>"),
 "Limits of BMI",
 "<p>BMI doesn't tell muscle from fat, so very muscular people can score high, and older adults can score low while carrying extra fat. Waist size matters too: a large waist increases health risk at any BMI. For children and teenagers, BMI must be compared with growth charts by age and sex. Use the result as a starting point and talk to a doctor about your own health.</p>",
 [("What is a healthy BMI?", "18.5 to 24.9 on the international scale, or 18.5 to 22.9 on the Asian scale."),
  ("Why is there an Asian scale?", "People of South and East Asian origin tend to develop weight-related illness at lower BMI."),
  ("Does it work for children?", "Not directly; children need age-based growth charts."),
  ("Is my data saved?", "No.")],
 [("Age calculator", "age-calculator.html"), ("Unit converter", "unit-converter.html"), ("Percentage", "percentage-calculator.html")])

G["date-calculator.html"] = T(
 "Date Calculator – Days Between Dates & Add Days | DailyPdfLife",
 "Count the days, weeks and working days between two dates with a Friday–Saturday or Saturday–Sunday weekend, or add and subtract days, months and years.",
 ("About the Date calculator", "<p>How many days until a visa expires? What date is 90 days after the contract starts? How many working days are in this month? The Date calculator answers these in two modes: <b>Days between dates</b> gives the total days, years-months-days, weeks and working days; <b>Add or subtract</b> gives the date after or before a number of days, weeks, months or years.</p>"),
 ("How to use it", "<ol><li>Choose a mode.</li><li>For days between: pick the start and end dates and your weekend, such as Friday + Saturday for Saudi Arabia or Saturday + Sunday for the UAE.</li><li>Tick <b>Count the end date too</b> if both days should count, as with leave requests.</li><li>For add or subtract: pick a date and the amount to add, and optionally skip weekends.</li></ol>"),
 "Useful for",
 "<p>Notice periods, probation end dates, visit visa and Iqama validity, payment due dates, pregnancy and exam countdowns, project deadlines and leave planning. Public holidays are not subtracted from working days, so remove them yourself if needed. To convert a date to Hijri, use the <a href=\"hijri-converter.html\">Hijri date converter</a>.</p>",
 [("Does it count public holidays?", "No, only the weekend days you choose are skipped."),
  ("Should I count the end date?", "For leave and contract periods, usually yes. For “days until”, no."),
  ("How are months added to the 31st?", "If the month is shorter, the last day of that month is used."),
  ("Is anything saved?", "No.")],
 [("Age calculator", "age-calculator.html"), ("Hijri converter", "hijri-converter.html"), ("End of service", "gratuity-calculator.html")])

G["prayer-times.html"] = T(
 "Prayer Times Today – Riyadh, Dhaka, Dubai & More | DailyPdfLife",
 "Accurate salah times for Fajr, Dhuhr, Asr, Maghrib and Isha in Saudi Arabia, UAE, Bangladesh and more, with Umm al-Qura and other methods and a live countdown.",
 ("About Prayer times", "<p>See today's prayer times for your city, a live countdown to the next prayer, and a table for the next seven days. Pick from cities across Saudi Arabia, the Gulf, Bangladesh, Pakistan, India and beyond, or use your phone's location. Times are calculated on your device from the sun's position, so they work even offline once the page has loaded.</p>"),
 ("How to use it", "<ol><li>Choose your city, or tap <b>Use my location</b>.</li><li>The calculation method is set for your country, for example Umm al-Qura in Saudi Arabia or Karachi in Bangladesh. You can change it.</li><li>Choose Hanafi for a later Asr time if you follow that school.</li><li>Pick another date to see times for any day.</li></ol>"),
 "About the methods",
 "<p>Methods differ mainly in the sun angle used for Fajr and Isha. Umm al-Qura, used in Saudi Arabia, sets Isha 90 minutes after Maghrib; in Ramadan many mosques there use 120 minutes. Bangladesh and Pakistan commonly use the University of Islamic Sciences, Karachi method. Your local mosque's timetable may differ by a few minutes; follow it where you pray.</p>",
 [("Which method should I choose?", "The one used by your local mosques; the default for your country is a good start."),
  ("What does the Hanafi option change?", "Only Asr, which becomes later."),
  ("Does it need internet?", "Only to load the page; times are calculated on your device."),
  ("Is my location sent anywhere?", "No, it is used only on your device.")],
 [("Hijri converter", "hijri-converter.html"), ("Zakat calculator", "zakat-calculator.html"), ("Date calculator", "date-calculator.html")])
