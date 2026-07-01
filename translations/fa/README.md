# Co-op Translator

_به‌سادگی ترجمه‌ها را برای محتوای آموزشی GitHub خود در چندین زبان به‌صورت خودکار مدیریت کنید، همزمان با پیشرفت پروژه._

![پایتون 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**شروع کنید:** [روند کاری خود را انتخاب کنید](https://azure.github.io/co-op-translator/workflows/) | [پیکربندی](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [API پایتون](https://azure.github.io/co-op-translator/api/) | [سرور MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی‌شده توسط [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاری](../bg/README.md) | [برمه‌ای (میانمار)](../my/README.md) | [چینی (ساده‌شده)](../zh-CN/README.md) | [چینی (سنتی، هنگ‌کنگ)](../zh-HK/README.md) | [چینی (سنتی، ماکائو)](../zh-MO/README.md) | [چینی (سنتی، تایوان)](../zh-TW/README.md) | [کرواتی](../hr/README.md) | [چکی](../cs/README.md) | [دانمارکی](../da/README.md) | [هلندی](../nl/README.md) | [استونیایی](../et/README.md) | [فنلاندی](../fi/README.md) | [فرانسوی](../fr/README.md) | [آلمانی](../de/README.md) | [یونانی](../el/README.md) | [عبری](../he/README.md) | [هندی](../hi/README.md) | [مجاری](../hu/README.md) | [اندونزیایی](../id/README.md) | [ایتالیایی](../it/README.md) | [ژاپنی](../ja/README.md) | [کانادا](../kn/README.md) | [خمری](../km/README.md) | [کره‌ای](../ko/README.md) | [لیتوانیایی](../lt/README.md) | [مالایی](../ms/README.md) | [مالایالام](../ml/README.md) | [مراتی](../mr/README.md) | [نپالی](../ne/README.md) | [پیجین نیجریه‌ای](../pcm/README.md) | [نروژی](../no/README.md) | [فارسی (Farsi)](./README.md) | [لهستانی](../pl/README.md) | [پرتغالی (برزیل)](../pt-BR/README.md) | [پرتغالی (پرتغال)](../pt-PT/README.md) | [پنجابی (گورموکی)](../pa/README.md) | [رومانیایی](../ro/README.md) | [روسی](../ru/README.md) | [صربی (سیریلیک)](../sr/README.md) | [اسلواکیایی](../sk/README.md) | [اسلوونیایی](../sl/README.md) | [اسپانیایی](../es/README.md) | [سواحیلی](../sw/README.md) | [سوئدی](../sv/README.md) | [تاگالوگ (فیلیپینی)](../tl/README.md) | [تامیلی](../ta/README.md) | [تلوگو](../te/README.md) | [تایلندی](../th/README.md) | [ترکی](../tr/README.md) | [اوکراینی](../uk/README.md) | [اردو](../ur/README.md) | [ویتنامی](../vi/README.md)

> **ترجیح می‌دهید به‌صورت محلی کلون کنید؟**
>
> این مخزن شامل ترجمه‌های بیش از 50 زبان است که حجم دانلود را به‌طور قابل‌توجهی افزایش می‌دهد. برای کلون کردن بدون ترجمه‌ها، از sparse checkout استفاده کنید:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> این به شما همهٔ چیزهای لازم برای تکمیل دوره را با دانلود بسیار سریع‌تر می‌دهد.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## مرور کلی

**Co-op Translator** به شما کمک می‌کند محتوای آموزشی GitHub خود را به‌سادگی به چندین زبان بومی‌سازی کنید.
وقتی فایل‌های Markdown، تصاویر یا دفترچه‌ها (notebooks) خود را به‌روزرسانی می‌کنید، ترجمه‌ها به‌طور خودکار همگام باقی می‌مانند و اطمینان می‌دهند محتوای شما برای یادگیرندگان سراسر جهان دقیق و به‌روز است.

از آن می‌توانید از طریق CLI برای ترجمهٔ مخزن، از API پایتون برای خودکارسازی، یا از طریق سرور MCP برای جریان‌های کاری عامل‌ها و ویرایشگرها استفاده کنید.

نمونه‌ای از نحوهٔ سازمان‌دهی محتوای ترجمه‌شده:

![نمونه](../../imgs/translation-ex.png)

## چرا Co-op Translator؟

ترجمهٔ یک فایل آسان است. نگه داشتن کل یک مخزن مستندات
ترجمه‌شده، متصل و به‌روز کار دشواری است.

| مشکل | Co-op Translator چگونه کمک می‌کند |
| --- | --- |
| مستندات طولانی محدود به یک پرامپت نیستند | فایل‌های بزرگ Markdown به قطعات تقسیم می‌شوند، بنابراین یک README طولانی به یک پاسخ آسیب‌پذیر از مدل وابسته نیست. اگر یک قطعه ناموفق شود، Co-op Translator می‌تواند فقط قسمت ناموفق را دوباره تلاش کند و دوباره تقسیم‌بندی کند. |
| ترجمه‌های ناقص نباید به‌عنوان جاری علامت‌گذاری شوند | یک ترجمهٔ ناقص هرگز نباید به‌عنوان به‌روز مهر شود. Co-op Translator قبل از ذخیره یکپارچگی ترجمه را بررسی می‌کند و می‌تواند ترجمه‌های موجود که از نظر ساختاری ناقص‌اند را تشخیص دهد. |
| پیوندها باید با ساختار مخزن ترجمه‌شده مطابقت داشته باشند | ترجمه‌های دستی اغلب لینک‌های نسبی را به درخت منبع نشان می‌دهند. Co-op Translator لینک‌های Markdown، دفترچه، تصویر و README را بازنویسی می‌کند تا با ساختار `translations/<lang>/...` مطابقت داشته باشند. |
| ترجمه باید در سراسر یک مخزن کار کند | Co-op Translator فایل‌های README، مستندات، دفترچه‌ها و متن تصاویر را به‌عنوان بخشی از یک جریان کاری مخزن واحد مدیریت می‌کند، به‌جای اینکه فایل‌ها را یکی‌یکی ترجمه کند. |
| حفظ ترجمه‌ها مهم‌تر از ایجاد یک‌بارهٔ آن‌ها است | هش‌های منبع و متادیتای ترجمه به Co-op Translator اجازه می‌دهند فایل‌های قدیمی را پیدا کند، فایل‌های تغییریافته را رد کند و محتوای ترجمه‌شده را همگام نگه دارد در حالی که مخزن منبع تکامل می‌یابد. |

## نحوه مدیریت وضعیت ترجمه

Co-op Translator محتوای ترجمه‌شده را به‌عنوان **آرتیفکت‌های نرم‌افزاری نسخه‌بندی‌شده** مدیریت می‌کند،  
نه به‌عنوان فایل‌های ایستا.

این ابزار وضعیت Markdown، تصاویر و دفترچه‌های ترجمه‌شده را با استفاده از **متادیتای محدوده‌زبان** ردیابی می‌کند.

این طراحی به Co-op Translator اجازه می‌دهد که:

- تشخیص قابل‌اطمینان ترجمه‌های قدیمی
- رفتار یکسان با Markdown، تصاویر و دفترچه‌ها
- مقیاس‌پذیری ایمن در مخازن بزرگ، پرسرعت و چندزبانه

با مدل‌سازی ترجمه‌ها به‌عنوان آرتیفکت‌های مدیریت‌شده،
جریان‌های کاری ترجمه به‌طور طبیعی با روش‌های
مدیریت وابستگی‌ها و آرتیفکت‌های مدرن هم‌راستا می‌شوند.

→ [نحوه مدیریت وضعیت ترجمه](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### مطالعات عمیق مرتبط

- [اصلاح مارک‌داون شکسته در ترجمهٔ هوش مصنوعی: تقویت یک خط لولهٔ تولید](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## شروع کنید

Co-op Translator را می‌توان از CLI، API پایتون، یا سرور MCP استفاده کرد. اگر بین ترجمهٔ محلی، خودکارسازی، CI، و ادغام عامل/ویرایشگر در حال انتخاب هستید، با راهنمای روند کاری شروع کنید.

- [روند کاری خود را انتخاب کنید](../../docs/workflows.md)
- [پیکربندی اعتبارنامه‌ها](../../docs/configuration.md)
- [ترجمه از طریق CLI](../../docs/cli.md)
- [خودکارسازی با API پایتون](../../docs/api.md)
- [اتصال به سرور MCP](../../docs/mcp.md)
- [اجرای در GitHub Actions](../../docs/github-actions.md)

مثال حداقلی CLI پس از پیکربندی:

```bash
python -m venv .venv
# ویندوز
.venv\Scripts\activate
# مک‌اواس/لینوکس
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

برای اجراهای اولیه در مخازن بزرگ، قبل از نوشتن فایل‌های ترجمه‌شده از `--dry-run` استفاده کنید. برای پرچم‌های نوع محتوا، لاگ‌ها، بازبینی و مهاجرت لینک‌ها به [مرجع CLI](../../docs/cli.md) مراجعه کنید.

اجرای سریع کانتینر با Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

اجرای سریع کانتینر با PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## ویژگی‌ها

- ترجمهٔ خودکار برای Markdown، دفترچه‌ها و تصاویر
- نگه‌داشتن ترجمه‌ها همگام با تغییرات منبع
- کارکرد محلی (CLI) یا در CI (GitHub Actions)
- ارائهٔ ابزارهای ترجمهٔ Markdown، دفترچه، تصویر، بازبینی و پروژه از طریق MCP
- استفاده از Azure OpenAI یا OpenAI برای ترجمه با پشتیبانی ارائه‌دهنده
- اجازه می‌دهد MCP میزبان عامل‌ها باشد تا قطعات Markdown و دفترچه را بدون اعتبارنامهٔ LLM مترجم Co-op ترجمه کنند
- استفاده از Azure AI Vision برای استخراج متن از تصویر و ترجمه
- بازبینی ساختار ترجمه و تازگی آن با بررسی‌های قطعی
- حفظ قالب‌بندی و ساختار Markdown

## مستندات

- [سایت مستندات](https://azure.github.io/co-op-translator/)
- [روند کاری خود را انتخاب کنید](../../docs/workflows.md)
- [پیکربندی](../../docs/configuration.md)
- [تنظیم Azure AI](../../docs/azure-ai-setup.md)
- [مرجع CLI](../../docs/cli.md)
- [API پایتون](../../docs/api.md)
- [سرور MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [قالب README زبان‌ها](../../docs/readme-languages-template.md)
- [زبان‌های پشتیبانی‌شده](../../docs/supported-languages.md)
- [مشارکت](../../CONTRIBUTING.md)
- [عیب‌یابی](../../docs/troubleshooting.md)

### راهنمای مخصوص مایکروسافت
> [!NOTE]
> فقط برای نگهدارندگان مخازن Microsoft “For Beginners”.

- [به‌روزرسانی فهرست “دوره‌های دیگر” (فقط برای مخازن MS Beginners)](../../docs/microsoft-beginners.md)

## از ما حمایت کنید و یادگیری جهانی را ترویج دهید

به ما در انقلاب نحوهٔ به‌اشتراک‌گذاری محتوای آموزشی در سطح جهانی بپیوندید! به [Co-op Translator](https://github.com/azure/co-op-translator) در GitHub ستاره ⭐ بدهید و از مأموریت ما برای از بین بردن موانع زبانی در یادگیری و فناوری حمایت کنید. علاقه و مشارکت‌های شما تأثیر قابل‌توجهی دارد! مشارکت‌های کد و پیشنهادهای ویژگی همیشه خوش‌آمد گفته می‌شوند.

### محتوای آموزشی مایکروسافت را به زبان خود بررسی کنید
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ارائه‌های ویدئویی

👉 برای تماشا در YouTube روی تصویر زیر کلیک کنید.

- **Open at Microsoft**: معرفی کوتاه ۱۸ دقیقه‌ای و راهنمای سریع درباره نحوه استفاده از Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## مشارکت

این پروژه از مشارکت‌ها و پیشنهادها استقبال می‌کند. علاقه‌مند به مشارکت در Azure Co-op Translator هستید؟ لطفاً برای راهنمایی درباره نحوه کمک به قابل‌دسترس‌تر کردن Co-op Translator به [CONTRIBUTING.md](../../CONTRIBUTING.md) مراجعه کنید.

## مشارکت‌کنندگان

[![مشارکت‌کنندگان co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## آیین‌نامه رفتاری

این پروژه [آیین‌نامه رفتار منبع باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/) را پذیرفته است.
برای اطلاعات بیشتر به [پرسش‌های متداول آیین‌نامه رفتار](https://opensource.microsoft.com/codeofconduct/faq/) مراجعه کنید یا در صورت سوالات یا نظرات اضافی با [opencode@microsoft.com](mailto:opencode@microsoft.com) تماس بگیرید.

## هوش مصنوعی مسئولانه

مایکروسافت متعهد است به کمک به مشتریان برای استفاده مسئولانه از محصولات هوش مصنوعی‌مان، به اشتراک‌گذاری آموخته‌هایمان و ساخت مشارکت‌های مبتنی بر اعتماد از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی‌های اثر. بسیاری از این منابع را می‌توانید در [https://aka.ms/RAI](https://aka.ms/RAI) بیابید.
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول هوش مصنوعی ما مبتنی است: عدالت، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، شمول‌پذیری، شفافیت و پاسخ‌گویی.

مدل‌های زبان، تصویر و گفتار در مقیاس بزرگ — مانند نمونه‌هایی که در این پروژه استفاده شده‌اند — ممکن است رفتارهایی نامنصفانه، غیرقابل‌اطمینان یا توهین‌آمیز داشته باشند که می‌تواند آسیب‌رسان باشد. لطفاً برای اطلاع از خطرات و محدودیت‌ها به [یادداشت شفافیت سرویس Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) مراجعه کنید.

رویکرد توصیه‌شده برای کاهش این خطرات، گنجاندن یک سیستم ایمنی در معماری شما است که قادر به شناسایی و جلوگیری از رفتارهای مضر باشد. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) لایه‌ای مستقل از حفاظت فراهم می‌کند که توانایی تشخیص محتوای مضر تولیدشده توسط کاربر و تولیدشده توسط هوش مصنوعی را در برنامه‌ها و خدمات داراست. Azure AI Content Safety شامل APIهای متن و تصویر است که به شما امکان می‌دهد محتوای مضر را شناسایی کنید. ما همچنین یک Content Safety Studio تعاملی داریم که به شما اجازه می‌دهد نمونه‌های کد را برای تشخیص محتوای مضر در مودالیتی‌های مختلف مشاهده، کاوش و آزمایش کنید. مستندات [شروع سریع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) زیر شما را در ارسال درخواست‌ها به سرویس راهنمایی می‌کند.

جنبه دیگری که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندمودالی و چندمدلی، عملکرد به معنای این است که سیستم همان‌طور که شما و کاربران‌تان انتظار دارید عمل کند، از جمله عدم تولید خروجی‌های مضر. ارزیابی عملکرد کل برنامه با استفاده از [معیارهای کیفیت تولید و معیارهای ریسک و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) اهمیت دارد.

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه با استفاده از [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با داشتن یک مجموعه داده آزمایشی یا یک هدف، تولیدات برنامه تولیدی هوش مصنوعی شما به‌صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی موردنظر شما سنجیده می‌شوند. برای شروع کار با prompt flow sdk جهت ارزیابی سیستم‌تان، می‌توانید راهنمای [شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) را دنبال کنید. پس از اجرای یک دور ارزیابی، می‌توانید [نتایج را در Azure AI Studio مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت تابع و باید مطابق با
[راهنمای علائم تجاری و برند مایکروسافت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) باشد.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید باعث سردرگمی یا القای حمایت مایکروسافت شود.
هرگونه استفاده از علائم تجاری یا لوگوهای اشخاص ثالث تابع سیاست‌های آن اشخاص ثالث است.

## دریافت کمک

اگر گیر کردید یا سوالی درباره ساخت برنامه‌های هوش مصنوعی دارید، بپیوندید:

[![دیسکورد Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر در هنگام توسعه بازخورد محصول یا خطاهایی داشتید، به بازدید کنید:

[![انجمن توسعه‌دهندگان Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)