import json, re, sys
BN = {
# names + descriptions (nav, home)
"Sign PDF": "PDF সাইন", "Draw, type or upload your signature and place it on a PDF.": "সাইন আঁকুন, টাইপ করুন বা ছবি দিন, তারপর PDF-এ বসান।",
"Compare PDF": "PDF তুলনা", "See what changed between two versions of a PDF.": "একই PDF-এর দুই সংস্করণে কী বদলেছে দেখুন।",
"Flatten PDF": "PDF ফ্ল্যাটেন", "Lock form fields and comments so they can't be changed.": "ফর্মের ঘর ও কমেন্ট লক করুন, যাতে আর বদলানো না যায়।",
"Grayscale PDF": "সাদাকালো PDF", "Turn a colour PDF into grayscale or black and white.": "রঙিন PDF-কে ধূসর বা সাদাকালো করুন।",
"PDF to PNG": "PDF থেকে PNG", "Turn PDF pages into sharp PNG or WEBP images.": "PDF-এর পাতাগুলো ঝকঝকে PNG বা WEBP ছবি করুন।",
"PowerPoint to PDF": "PowerPoint থেকে PDF", "Turn a .pptx presentation into a PDF.": ".pptx প্রেজেন্টেশনকে PDF করুন।",
"PDF to text": "PDF থেকে লেখা", "Pull all the text out of a PDF into a .txt file.": "PDF-এর সব লেখা বের করে .txt ফাইলে নিন।",
"HTML to PDF": "HTML থেকে PDF", "Turn an HTML file or pasted content into a PDF.": "HTML ফাইল বা পেস্ট করা লেখাকে PDF করুন।",
"ZIP files": "ZIP ফাইল", "Make a ZIP from many files, or open a ZIP.": "অনেক ফাইল এক ZIP-এ ভরুন, বা ZIP খুলুন।",
"Resize image to KB": "ছবি KB-তে ছোট করুন", "Make a photo exactly 20 KB, 50 KB, 100 KB or any size.": "ছবিকে ঠিক ২০, ৫০, ১০০ KB বা যেকোনো সাইজে আনুন।",
"Signature maker": "সিগনেচার মেকার", "Draw or type a signature and save it as a transparent PNG.": "সাইন আঁকুন বা টাইপ করুন, স্বচ্ছ PNG হিসেবে সেভ করুন।",
"Photo enhancer": "ছবি উন্নত করুন", "Brighten, sharpen and fix the colours of a photo.": "ছবি উজ্জ্বল, ঝকঝকে আর রং ঠিক করুন।",
"Meme maker": "মিম মেকার", "Make a meme with top and bottom text or a caption.": "উপরে-নিচে লেখা বা ক্যাপশন দিয়ে মিম বানান।",
"Prayer times": "নামাজের সময়", "Today's salah times for your city, with a countdown.": "আপনার শহরের আজকের নামাজের সময়, কাউন্টডাউনসহ।",
"End of service (gratuity)": "চাকরি শেষের টাকা (গ্র্যাচুইটি)", "Saudi and UAE end-of-service benefit for your years of work.": "সৌদি ও আমিরাতে চাকরির বছর অনুযায়ী এন্ড-অফ-সার্ভিস হিসাব।",
"Currency converter": "মুদ্রা রূপান্তর", "SAR, BDT, AED, USD and more at today's rates.": "আজকের রেটে রিয়াল, টাকা, দিরহাম, ডলার ইত্যাদি।",
"BMI calculator": "BMI ক্যালকুলেটর", "Body mass index and the healthy weight for your height.": "BMI আর আপনার উচ্চতার জন্য সুস্থ ওজন।",
"Date calculator": "তারিখ ক্যালকুলেটর", "Days between two dates, or add days to a date.": "দুই তারিখের মাঝে কত দিন, বা তারিখে দিন যোগ।",
# shared UI
"Choose a PDF first": "আগে একটা PDF বাছুন", "Working…": "কাজ চলছে…", "Loading…": "লোড হচ্ছে…", "Saving…": "সেভ হচ্ছে…",
"This PDF could not be opened. If it has a password, unlock it first.": "এই PDF খোলা গেল না। পাসওয়ার্ড থাকলে আগে আনলক করুন।",
"1. Choose a PDF": "১. একটা PDF বাছুন", "2. Options": "২. অপশন", "Quality": "মান", "Format": "ফরম্যাট", "Pages": "পাতা",
# sign pdf
"1. Make your signature": "১. আপনার সাইন তৈরি করুন", "2. Place it": "২. বসান", "Draw": "আঁকুন", "Type": "টাইপ", "Upload": "আপলোড", "Clear": "মুছুন",
"Your name": "আপনার নাম", "A photo of your signature on white paper. The white background is removed for you.": "সাদা কাগজে করা সাইনের ছবি দিন। সাদা অংশ নিজে থেকেই সরে যাবে।",
"Tap on a page to put your signature there. Drag to move, use the red dot to resize.": "যেখানে সাইন চান সেই পাতায় চাপুন। টেনে সরান, লাল বিন্দু টেনে ছোট-বড় করুন।",
"📅 Add today's date": "📅 আজকের তারিখ দিন", "🔤 Add text (name, initials)": "🔤 লেখা যোগ (নাম, আদ্যক্ষর)", "✓ Sign & save PDF": "✓ সাইন করে PDF সেভ",
"Choose a PDF above to see its pages here.": "উপরে PDF বাছলে পাতাগুলো এখানে দেখাবে।", "Tap a page to place your signature.": "সাইন বসাতে পাতায় চাপুন।",
"Make your signature first (draw, type or upload).": "আগে সাইন তৈরি করুন (আঁকুন, টাইপ বা আপলোড)।", "Tap a page to place your signature first.": "আগে পাতায় চেপে সাইন বসান।",
"Text to add (for example your name or initials):": "কী লিখবেন (যেমন নাম বা আদ্যক্ষর):", "Could not save the PDF:": "PDF সেভ করা গেল না:",
# compare
"Original (old) PDF": "আগের (পুরোনো) PDF", "New (changed) PDF": "নতুন (বদলানো) PDF", "Show only the changed lines": "শুধু বদলানো লাইন দেখান",
"Ignore extra spaces": "বাড়তি স্পেস বাদ দিন", "Ignore capital letters": "বড়-ছোট হাতের অক্ষর বাদ দিন", "⇆ Compare PDFs": "⇆ PDF তুলনা করুন",
"Choose both PDF files first.": "আগে দুটো PDF-ই বাছুন।", "Reading both files…": "দুটো ফাইল পড়া হচ্ছে…", "removed": "বাদ", "added": "যোগ", "changed": "বদলানো", "same": "একই",
"No differences found. The text of both PDFs is the same.": "কোনো পার্থক্য নেই। দুই PDF-এর লেখা একই।",
"No text was found. These look like scanned PDFs; run them through OCR first.": "কোনো লেখা পাওয়া যায়নি। এগুলো স্ক্যান করা PDF মনে হচ্ছে; আগে OCR করুন।",
# flatten
"2. How to flatten": "২. কীভাবে ফ্ল্যাটেন করবেন", "Lock form fields": "ফর্মের ঘর লক", "Flatten everything": "সবকিছু ফ্ল্যাটেন",
"Filled-in boxes, ticks and dropdowns become normal page content. Text stays sharp and searchable.": "পূরণ করা ঘর, টিক আর ড্রপডাউন সাধারণ পাতার অংশ হয়ে যায়। লেখা ঝকঝকে ও খোঁজা যায়।",
"Every page is turned into a single picture: comments, stamps, highlights and forms included. Nothing can be edited after this.": "প্রতিটা পাতা একটা ছবি হয়ে যায়: কমেন্ট, স্ট্যাম্প, হাইলাইট আর ফর্মসহ। এরপর আর কিছু বদলানো যায় না।",
"▤ Flatten PDF": "▤ PDF ফ্ল্যাটেন করুন", "This PDF has no form fields. Flatten everything into pictures instead?": "এই PDF-এ কোনো ফর্মের ঘর নেই। এর বদলে সবকিছু ছবিতে ফ্ল্যাটেন করবেন?",
# png / gray
"Resolution": "রেজোলিউশন", "Transparent background (PNG)": "স্বচ্ছ ব্যাকগ্রাউন্ড (PNG)", "🖼 Convert to images": "🖼 ছবিতে রূপান্তর", "images ready": "টি ছবি তৈরি",
"No pages match that range.": "এই সীমায় কোনো পাতা নেই।", "Look": "ধরন", "Grayscale": "ধূসর", "Black & white (crisp text)": "সাদাকালো (স্পষ্ট লেখা)", "◐ Make it grayscale": "◐ সাদাকালো করুন",
# ppt
"1. Choose a PowerPoint file (.pptx)": "১. PowerPoint ফাইল (.pptx) বাছুন", "Add slide numbers": "স্লাইড নম্বর দিন", "▶ Convert to PDF": "▶ PDF করুন", "Slide": "স্লাইড",
"Choose a PowerPoint file first.": "আগে একটা PowerPoint ফাইল বাছুন।",
"This is the old .ppt format. Open it in PowerPoint or Google Slides and save it as .pptx first.": "এটা পুরোনো .ppt ফরম্যাট। PowerPoint বা Google Slides-এ খুলে আগে .pptx হিসেবে সেভ করুন।",
# text / html / zip
"Mark where each page starts": "প্রতিটা পাতা কোথায় শুরু দেখান", "Join broken lines into paragraphs": "ভাঙা লাইন জোড়া দিয়ে অনুচ্ছেদ করুন", "📝 Extract text": "📝 লেখা বের করুন",
"⬇ Save .txt": "⬇ .txt সেভ", "📋 Copy all": "📋 সব কপি", "words": "শব্দ", "pages": "পাতা",
"Upload .html file": ".html ফাইল দিন", "Paste HTML or text": "HTML বা লেখা পেস্ট করুন", "Page size": "পাতার সাইজ", "Margins": "মার্জিন", "⬇ Save as PDF": "⬇ PDF হিসেবে সেভ",
"The preview appears here.": "প্রিভিউ এখানে দেখাবে।", "Add an HTML file or paste some content first.": "আগে HTML ফাইল দিন বা কিছু লেখা পেস্ট করুন।",
"Make a ZIP": "ZIP বানান", "Open a ZIP": "ZIP খুলুন", "Put many files into one ZIP, so you can send them as a single attachment.": "অনেক ফাইল এক ZIP-এ ভরুন, যাতে একটা অ্যাটাচমেন্ট হিসেবে পাঠানো যায়।",
"See what's inside a ZIP and save the files you need. Works on phones too.": "ZIP-এর ভেতরে কী আছে দেখুন, দরকারি ফাইল সেভ করুন। ফোনেও চলে।",
"🗜 Create ZIP": "🗜 ZIP তৈরি করুন", "⬇ Save all files": "⬇ সব ফাইল সেভ", "files inside": "টি ফাইল আছে", "Choose some files first.": "আগে কিছু ফাইল বাছুন।",
# kb
"1. Choose a photo": "১. একটা ছবি বাছুন", "2. Target size": "২. কাঙ্ক্ষিত সাইজ", "Or type it (KB)": "অথবা লিখুন (KB)", "Width (px, optional)": "প্রস্থ (px, ঐচ্ছিক)",
"Height (px, optional)": "উচ্চতা (px, ঐচ্ছিক)", "⇲ Make it this size": "⇲ এই সাইজ করুন", "Before": "আগে", "After": "পরে", "Choose a photo first": "আগে একটা ছবি বাছুন",
"Many forms ask for a photo under a size, for example 50 KB, or exactly 300 × 300 pixels. Fill in the width and height only if the form asks for exact pixels.": "অনেক ফর্মে নির্দিষ্ট সাইজের ছবি চায়, যেমন ৫০ KB-এর কম বা ঠিক ৩০০ × ৩০০ পিক্সেল। ফর্মে নির্দিষ্ট পিক্সেল চাইলে তবেই প্রস্থ-উচ্চতা দিন।",
# signature maker
"✍ Draw": "✍ আঁকুন", "Aa Type": "Aa টাইপ", "📷 From photo": "📷 ছবি থেকে", "Pen": "কলম", "Thin": "চিকন", "Medium": "মাঝারি", "Bold": "মোটা", "↶ Undo": "↶ আগের অবস্থা",
"Type your full name": "আপনার পুরো নাম লিখুন", "Clean-up strength": "পরিষ্কারের মাত্রা", "Ink colour": "কালির রং", "Your signature": "আপনার সাইন",
"Draw, type or upload your signature above.": "উপরে সাইন আঁকুন, টাইপ করুন বা ছবি দিন।", "⬇ Download PNG (transparent)": "⬇ PNG ডাউনলোড (স্বচ্ছ)", "⬇ JPG (white background)": "⬇ JPG (সাদা ব্যাকগ্রাউন্ড)",
"→ Use it to sign a PDF": "→ এটা দিয়ে PDF সাইন করুন", "Make your signature first.": "আগে সাইন তৈরি করুন।",
"Sign on plain white paper with a dark pen, take a clear photo, and choose it here. The paper is removed and only the ink is kept.": "সাদা কাগজে গাঢ় কলমে সাইন করে পরিষ্কার ছবি তুলে এখানে দিন। কাগজ সরে যাবে, শুধু কালি থাকবে।",
# enhancer
"✨ Auto enhance": "✨ অটো উন্নত করুন", "📄 Document": "📄 ডকুমেন্ট", "🌈 Vivid": "🌈 উজ্জ্বল রং", "☀ Warm": "☀ উষ্ণ", "◐ B & W": "◐ সাদাকালো", "Adjust": "ঠিক করুন",
"Brightness": "উজ্জ্বলতা", "Contrast": "কনট্রাস্ট", "Colour": "রং", "Warmth": "উষ্ণতা", "Shadows": "ছায়া", "Sharpness": "ধার", "Vignette": "ভিনিয়েট", "↺ Reset": "↺ আগের মতো",
"Save as": "সেভ করুন", "⬇ Save photo": "⬇ ছবি সেভ", "👁 Hold to see original": "👁 চেপে ধরে আসলটা দেখুন",
# meme
"or start with a plain background": "অথবা সাদামাটা ব্যাকগ্রাউন্ড দিয়ে শুরু করুন", "Use colour": "রং ব্যবহার", "Style": "ধরন", "Classic (text on photo)": "ক্লাসিক (ছবির উপর লেখা)",
"Caption bar on top": "উপরে ক্যাপশন বার", "Top text": "উপরের লেখা", "Bottom text": "নিচের লেখা", "Caption": "ক্যাপশন", "Size": "সাইজ", "CAPITALS": "বড় হাতের", "⬇ Save meme": "⬇ মিম সেভ",
# gratuity
"🇸🇦 Saudi Arabia": "🇸🇦 সৌদি আরব", "🇦🇪 UAE": "🇦🇪 আমিরাত", "First day of work": "কাজের প্রথম দিন", "Last day of work": "কাজের শেষ দিন", "Last monthly wage": "শেষ মাসিক বেতন",
"Basic + housing + other fixed allowances": "মূল বেতন + বাসা ভাতা + অন্যান্য নির্দিষ্ট ভাতা", "Basic salary only, as in your contract": "শুধু মূল বেতন, চুক্তি অনুযায়ী",
"Currency": "মুদ্রা", "Unpaid leave days": "বিনা বেতনের ছুটির দিন", "Days of unpaid absence during the job, if any": "চাকরির সময় বিনা বেতনের অনুপস্থিতি, যদি থাকে",
"How did the job end?": "চাকরি কীভাবে শেষ হলো?", "Contract ended or employer ended it": "চুক্তি শেষ বা মালিক শেষ করেছে", "I resigned": "আমি রিজাইন দিয়েছি",
"Left for a reason the law protects (e.g. Article 81, force majeure)": "আইনসম্মত কারণে চলে এসেছি (যেমন ধারা ৮১, অনিবার্য কারণ)",
"End-of-service benefit": "এন্ড-অফ-সার্ভিস পাওনা", "Time served": "চাকরির মেয়াদ", "years": "বছর", "months": "মাস", "days": "দিন", "Fill in the dates and the wage.": "তারিখ আর বেতন লিখুন।",
"First 5 years × half a month": "প্রথম ৫ বছর × অর্ধেক মাস", "After 5 years × one month": "৫ বছরের পর × এক মাস", "Full award": "পুরো পাওনা", "Resignation share": "রিজাইনে প্রাপ্য অংশ",
"Under 2 years: no award on resignation": "২ বছরের কম: রিজাইনে কিছু পাবেন না", "2 to 5 years: one third": "২ থেকে ৫ বছর: এক-তৃতীয়াংশ", "5 to 10 years: two thirds": "৫ থেকে ১০ বছর: দুই-তৃতীয়াংশ",
"10 years or more: full award": "১০ বছর বা বেশি: পুরো পাওনা", "Daily basic wage (÷30)": "দৈনিক মূল বেতন (÷৩০)", "First 5 years × 21 days": "প্রথম ৫ বছর × ২১ দিন", "After 5 years × 30 days": "৫ বছরের পর × ৩০ দিন",
"Less than one year of service": "এক বছরের কম চাকরি", "No gratuity": "গ্র্যাচুইটি নেই", "Capped at 2 years' wage": "সর্বোচ্চ ২ বছরের বেতন",
# currency
"Amount": "পরিমাণ", "From": "থেকে", "To": "তে", "in other currencies": "অন্যান্য মুদ্রায়", "Mid-market rates updated": "মধ্য-বাজার রেট আপডেট",
"Banks and exchange shops add their own margin, so the amount you receive will be a little lower.": "ব্যাংক ও এক্সচেঞ্জ নিজেদের লাভ যোগ করে, তাই হাতে একটু কম পাবেন।",
"Saudi riyal": "সৌদি রিয়াল", "Bangladeshi taka": "বাংলাদেশি টাকা", "UAE dirham": "আমিরাতি দিরহাম", "US dollar": "মার্কিন ডলার", "Euro": "ইউরো", "British pound": "ব্রিটিশ পাউন্ড",
"Indian rupee": "ভারতীয় রুপি", "Pakistani rupee": "পাকিস্তানি রুপি", "Qatari riyal": "কাতারি রিয়াল", "Kuwaiti dinar": "কুয়েতি দিনার", "Omani rial": "ওমানি রিয়াল", "Bahraini dinar": "বাহরাইনি দিনার",
"Malaysian ringgit": "মালয়েশিয়ান রিংগিত",
# bmi
"Height (cm)": "উচ্চতা (সেমি)", "Weight (kg)": "ওজন (কেজি)", "Height (ft, in)": "উচ্চতা (ফুট, ইঞ্চি)", "Weight (lb)": "ওজন (পাউন্ড)", "Age": "বয়স", "Scale": "মাপকাঠি",
"WHO (international)": "WHO (আন্তর্জাতিক)", "WHO Asian (South Asia, Gulf, East Asia)": "WHO এশীয় (দক্ষিণ এশিয়া, উপসাগর, পূর্ব এশিয়া)", "Underweight": "কম ওজন", "Healthy weight": "সুস্থ ওজন",
"Overweight": "বাড়তি ওজন", "Obesity class I": "স্থূলতা ১ম ধাপ", "Obesity class II": "স্থূলতা ২য় ধাপ", "Obesity class III": "স্থূলতা ৩য় ধাপ", "Healthy weight for your height": "আপনার উচ্চতায় সুস্থ ওজন",
# date
"Days between dates": "দুই তারিখের মাঝে দিন", "Add or subtract days": "দিন যোগ বা বিয়োগ", "Start date": "শুরুর তারিখ", "End date": "শেষ তারিখ", "Weekend (for working days)": "সাপ্তাহিক ছুটি (কর্মদিবসের জন্য)",
"Count the end date too": "শেষ তারিখও গুনুন", "Add / subtract": "যোগ / বিয়োগ", "Add (+)": "যোগ (+)", "Subtract (−)": "বিয়োগ (−)", "Years": "বছর", "Months": "মাস", "Weeks": "সপ্তাহ", "Days": "দিন",
"Total days": "মোট দিন", "Years, months, days": "বছর, মাস, দিন", "Working days": "কর্মদিবস", "Weekend days": "ছুটির দিন", "Hours": "ঘণ্টা", "Months (approx.)": "মাস (প্রায়)",
"Result date": "ফলাফলের তারিখ", "Date (DD/MM/YYYY)": "তারিখ (দিন/মাস/বছর)", "Days from start": "শুরু থেকে দিন", "weeks": "সপ্তাহ",
"Count working days only (skip Friday + Saturday)": "শুধু কর্মদিবস গুনুন (শুক্র + শনি বাদ)",
# prayer
"City": "শহর", "Date": "তারিখ", "Method": "পদ্ধতি", "Asr": "আসর", "📍 Use my location": "📍 আমার লোকেশন", "Next prayer": "পরের নামাজ", "Next 7 days": "পরের ৭ দিন",
"Fajr": "ফজর", "Sunrise": "সূর্যোদয়", "Dhuhr": "জোহর", "Maghrib": "মাগরিব", "Isha": "এশা", "My location": "আমার লোকেশন", "Shafi, Maliki, Hanbali": "শাফেয়ি, মালেকি, হাম্বলি", "Hanafi": "হানাফি",
"Finding your location…": "লোকেশন খোঁজা হচ্ছে…", "Location permission was not given. Pick your city instead.": "লোকেশনের অনুমতি দেওয়া হয়নি। শহর বেছে নিন।",
"Your local mosque may differ by a few minutes.": "আপনার এলাকার মসজিদের সময় কয়েক মিনিট আলাদা হতে পারে।", "Times are calculated for": "সময় হিসাব করা হয়েছে",
"Umm al-Qura sets Isha 90 minutes after Maghrib; in Ramadan many mosques in Saudi Arabia use 120 minutes. ": "উম্মুল কুরা পদ্ধতিতে এশা মাগরিবের ৯০ মিনিট পর; রমজানে সৌদির অনেক মসজিদে ১২০ মিনিট। ",
"Riyadh": "রিয়াদ", "Jeddah": "জেদ্দা", "Makkah": "মক্কা", "Madinah": "মদিনা", "Dammam": "দাম্মাম", "Dhaka": "ঢাকা", "Chattogram": "চট্টগ্রাম", "Sylhet": "সিলেট", "Feni": "ফেনী",
"Noakhali": "নোয়াখালী", "Cumilla": "কুমিল্লা", "Khulna": "খুলনা", "Rajshahi": "রাজশাহী", "Barishal": "বরিশাল", "Rangpur": "রংপুর", "Mymensingh": "ময়মনসিংহ", "Dubai": "দুবাই",
}
p = sys.argv[1] + "/lang.js"; t = open(p, encoding="utf-8").read()
start = t.index("var BN = {"); end = t.index("\n};", start)
body = t[start:end]
add = "".join(f"\n{json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}," for k, v in BN.items() if f'"{k}":' not in body)
# make sure the last existing entry ends with a comma
prev = t[:end].rstrip()
if not prev.endswith(","): t = prev + "," + t[end:] ; end = t.index("\n};", start)
t = t[:end] + add.rstrip(",") + t[end:]
open(p, "w", encoding="utf-8").write(t)
print("added", add.count("\n"))
