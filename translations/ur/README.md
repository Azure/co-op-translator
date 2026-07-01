‏# کو-اوپ ٹرانسلیٹر

_اپنے تعلیمی GitHub مواد کا ترجمہ مختلف زبانوں میں آسانی سے خودکار اور برقرار رکھیں جب آپ کا پروجیکٹ ترقی کرتا ہے._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

**یہاں شروع کریں:** [اپنا ورک فلو منتخب کریں](https://azure.github.io/co-op-translator/workflows/) | [ترتیبات](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP سرور](https://azure.github.io/co-op-translator/mcp/)

### 🌐 متعدد زبانوں کی حمایت

#### [Co-op Translator](https://github.com/Azure/co-op-translator) کی طرف سے سپورٹ کردہ

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (سادہ)](../zh-CN/README.md) | [چینی (روایتی، ہانگ کانگ)](../zh-HK/README.md) | [چینی (روایتی، میکو)](../zh-MO/README.md) | [چینی (روایتی، تائیوان)](../zh-TW/README.md) | [کروشین](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [ایسٹونین](../et/README.md) | [فنِش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگیرین](../hu/README.md) | [انڈونیشیائی](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کنڑا](../kn/README.md) | [خمیر](../km/README.md) | [کوریائی](../ko/README.md) | [لتھوانیائی](../lt/README.md) | [ملائی](../ms/README.md) | [ملیالم](../ml/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [نائجیریائی پیجین](../pcm/README.md) | [ناروِجی](../no/README.md) | [فارسی (Farsi)](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../pt-BR/README.md) | [پرتگالی (پرتگال)](../pt-PT/README.md) | [پنجابی (گُرمُخی)](../pa/README.md) | [رومانوی](../ro/README.md) | [روسی](../ru/README.md) | [سربیائی (سِریلیک)](../sr/README.md) | [سلوواک](../sk/README.md) | [سلووینیائی](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹاگالوگ (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تیلگو](../te/README.md) | [تھائی](../th/README.md) | [ترکِی](../tr/README.md) | [یوکرائینی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)

> **کیا آپ مقامی طور پر کلون کرنا پسند کریں گے؟**
>
> اس ریپوزیٹری میں 50+ زبانوں کے تراجم شامل ہیں جو ڈاؤن لوڈ سائز میں نمایاں اضافہ کرتے ہیں۔ تراجم کے بغیر کلون کرنے کے لیے، sparse checkout استعمال کریں:
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
> یہ آپ کو کورس مکمل کرنے کے لیے درکار تمام چیزیں بہت تیز ڈاؤن لوڈ کے ساتھ فراہم کرتا ہے۔
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## جائزہ

**Co-op Translator** آپ کے تعلیمی GitHub مواد کو متعدد زبانوں میں بغیر کسی کوشش کے مقامی بنانے میں مدد دیتا ہے۔
جب آپ اپنی Markdown فائلز، تصاویر، یا نوٹ بکس کو اپ ڈیٹ کرتے ہیں، تراجم خود بخود ہم آہنگ رہتے ہیں، اس بات کو یقینی بناتے ہوئے کہ آپ کا مواد دنیا بھر کے سیکھنے والوں کے لیے درست اور تازہ رہے۔

آپ اسے رپوزیٹری کے ترجمے کے لیے CLI سے، خودکار عمل کے لیے Python API سے، یا ایجنٹ/ایڈیٹر ورک فلو کے لیے MCP سرور کے ذریعے استعمال کر سکتے ہیں۔

یہاں دکھایا گیا ہے کہ ترجمہ شدہ مواد کیسے منظم ہوتا ہے:

![Example](../../imgs/translation-ex.png)

## کیوں Co-op Translator؟

ایک فائل کا ترجمہ آسان ہے۔ پورے ڈاکیومنٹیشن ریپوزیٹری کو
ترجمہ شدہ، مربوط، اور تازہ ترین رکھنا وہ مشکل کام ہے۔

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | بڑی Markdown فائلوں کو حصوں میں تقسیم کیا جاتا ہے، لہٰذا ایک طویل README ایک نازک ماڈل ردِعمل پر منحصر نہیں رہتا۔ اگر کسی حصے میں ناکامی ہو، تو Co-op Translator صرف خراب حصے کو دوبارہ کوشش اور دوبارہ تقسیم کر سکتا ہے۔ |
| Incomplete translations should not be marked current | ایک نامکمل ترجمہ کو کبھی بھی جدید قرار نہیں دیا جانا چاہیے۔ Co-op Translator محفوظ کرنے سے پہلے ترجمے کی سالمیت کو چیک کرتا ہے اور ساختی طور پر نامکمل موجودہ تراجم کا پتہ لگا سکتا ہے۔ |
| Links should match the translated repo structure | دستی تراجم اکثر نسبتی لنکس کو سورس درخت کی طرف اشارہ کرنے کے لیے چھوڑ دیتے ہیں۔ Co-op Translator Markdown، نوٹ بک، تصویر، اور README لنکس کو `translations/<lang>/...` ساخت کے مطابق دوبارہ لکھتا ہے۔ |
| Translation should work across an entire repo | Co-op Translator README فائلیں، دستاویزات، نوٹ بکس، اور تصویر کے متن کو ایک رپوزیٹری ورک فلو کے حصے کے طور پر سنبھالتا ہے، بجائے اس کے کہ فائلوں کو ایک ایک کر کے ترجمہ کرے۔ |
| Maintaining translations matters more than creating them once | سورس ہیشز اور ترجمہ میٹا ڈیٹا Co-op Translator کو پرانی فائلیں تلاش کرنے، غیر تبدیل شدہ فائلوں کو چھوڑنے، اور سورس ریپو کے ارتقاء کے ساتھ ترجمہ شدہ مواد کو ہم آہنگ رکھنے دیتے ہیں۔ |

## ترجمے کی حالت کا انتظام کیسے کیا جاتا ہے

Co-op Translator ترجمہ شدہ مواد کو بطور **ورژن شدہ سافٹ ویئر آرٹیفیکٹس** سنبھالتا ہے،  
نہ کہ بطور جامد فائلیں۔

یہ ٹول ترجمہ شدہ Markdown، تصاویر، اور نوٹ بکس کی حالت کو
استعمال کرتا ہے **زبان محدد میٹا ڈیٹا**۔

یہ ڈیزائن Co-op Translator کو اجازت دیتا ہے کہ وہ:

- پرانے ترجموں کا قابلِ اعتماد طریقے سے پتہ لگائے
- Markdown، تصاویر، اور نوٹ بکس کو مستقل طور پر برتاؤ کرے
- بڑے، تیزی سے حرکت کرنے والے، کثیر اللسانی ریپوزیٹریز میں محفوظ طریقے سے پیمانے پر کام کرے

ترجموں کو منظم آرٹیفیکٹس کے طور پر ماڈل کر کے،
ترجمہ کے ورک فلو جدید سافٹ ویئر انحصار اور آرٹیفیکٹ مینجمنٹ طریقوں کے ساتھ فطری طور پر ہم آہنگ ہو جاتے ہیں۔

→ [ترجمے کی حالت کا انتظام کیسے کیا جاتا ہے](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### متعلقہ تفصیلی مضامین

- [AI ترجمہ میں ٹوٹے ہوئے Markdown کی اصلاح: پروڈکشن پائپ لائن کو مضبوط کرنا](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## شروعات کریں

Co-op Translator کو CLI، Python API، یا MCP سرور سے استعمال کیا جا سکتا ہے۔ اگر آپ مقامی ترجمہ، خودکاری، CI، اور ایجنٹ/ایڈیٹر انضمام کے درمیان انتخاب کر رہے ہیں تو ورک فلو گائیڈ سے شروع کریں۔

- [اپنا ورک فلو منتخب کریں](../../docs/workflows.md)
- [اسناد ترتیب دیں](../../docs/configuration.md)
- [CLI سے ترجمہ کریں](../../docs/cli.md)
- [Python API کے ساتھ خودکاری کریں](../../docs/api.md)
- [MCP سرور کے ساتھ کنیکٹ کریں](../../docs/mcp.md)
- [GitHub Actions میں چلائیں](../../docs/github-actions.md)

تشکیل کے بعد کم از کم CLI مثال:

```bash
python -m venv .venv
# ونڈوز
.venv\Scripts\activate
# میک او ایس/لینکس
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

بڑے ریپوزیٹریز پر پہلی بار چلانے کے لیے، ترجمہ شدہ فائلیں لکھنے سے پہلے `--dry-run` استعمال کریں۔ مواد کی قسم کے فلیگز، لوگز، جائزہ، اور لنک مائگریشن کے بارے میں دیکھیں [CLI Reference](../../docs/cli.md)۔

کنٹینر فوری چلانے کے لیے Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

کنٹینر فوری چلانے کے لیے PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## خصوصیات

- Markdown، نوٹ بکس، اور تصاویر کے لیے خودکار ترجمہ
- تراجم کو ماخذ کی تبدیلیوں کے ساتھ ہم آہنگ رکھتا ہے
- مقامی (CLI) یا CI (GitHub Actions) میں کام کرتا ہے
- MCP کے ذریعے Markdown، نوٹ بکس، تصویر، جائزہ، اور پروجیکٹ ترجمہ کے آلات فراہم کرتا ہے
- مزود کے تعاون یافتہ ترجمے کے لیے Azure OpenAI یا OpenAI استعمال کرتا ہے
- MCP کو اجازت دیتا ہے کہ وہ ایجنٹس کو Co-op Translator LLM اسناد کے بغیر Markdown اور نوٹ بکس کے حصوں کا ترجمہ کرنے کی میزبانی کرے
- تصویر کے متن نکالنے اور ترجمہ کے لیے Azure AI Vision استعمال کرتا ہے
- تراجم کے ڈھانچے اور تازگی کا معائنہ قطعی چیکس کے ساتھ کرتا ہے
- Markdown کی ساخت اور فارمیٹنگ کو برقرار رکھتا ہے

## دستاویزات

- [دستاویزی سائٹ](https://azure.github.io/co-op-translator/)
- [اپنا ورک فلو منتخب کریں](../../docs/workflows.md)
- [ترتیبات](../../docs/configuration.md)
- [Azure AI ترتیب](../../docs/azure-ai-setup.md)
- [CLI حوالہ](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP سرور](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README زبانوں کا ٹیمپلیٹ](../../docs/readme-languages-template.md)
- [معاونت یافتہ زبانیں](../../docs/supported-languages.md)
- [شراکت](../../CONTRIBUTING.md)
- [مسائل حل کرنا](../../docs/troubleshooting.md)

### مائیکروسافٹ مخصوص رہنمائی
> [!NOTE]
> صرف Microsoft کے “For Beginners” ریپوزیٹریز کے مینٹینرز کے لیے۔

- [“دیگر کورسس” فہرست کو اپ ڈیٹ کرنا (صرف MS Beginners ریپوزیٹریز کے لیے)](../../docs/microsoft-beginners.md)

## ہماری مدد کریں اور عالمی تعلیم کو فروغ دیں

ہمارے ساتھ شامل ہوں کہ تعلیمی مواد کو دنیا بھر میں شیئر کرنے کے طریقوں میں انقلاب لایا جائے! [Co-op Translator](https://github.com/azure/co-op-translator) کو GitHub پر ⭐ دیں اور سیکھنے اور ٹیکنالوجی میں زبان کی رکاوٹوں کو ختم کرنے کے ہمارے مشن کی حمایت کریں۔ آپ کی دلچسپی اور شراکتیں نمایاں اثر ڈالتی ہیں! کوڈ میں شراکت اور فیچر تجویزات ہمیشہ خوش آئند ہیں۔

### اپنی زبان میں مائیکروسافٹ تعلیمی مواد تلاش کریں
- [LangChain4j برائے مبتدی](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD برائے مبتدی](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI برائے مبتدی](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) برائے مبتدی](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents برائے مبتدی](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI برائے مبتدیان (.NET استعمال کرتے ہوئے)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI برائے مبتدی](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI برائے مبتدی (Java استعمال کرتے ہوئے)](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML برائے مبتدی](https://aka.ms/ml-beginners)
- [Data Science برائے مبتدی](https://aka.ms/datascience-beginners)
- [AI برائے مبتدی](https://aka.ms/ai-beginners)
- [سائبر سیکیورٹی برائے مبتدی](https://github.com/microsoft/Security-101)
- [Web Dev برائے مبتدی](https://aka.ms/webdev-beginners)
- [IoT برائے مبتدی](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ویڈیو پریزنٹیشنز

👉 یوٹیوب پر دیکھنے کے لیے نیچے والی تصویر پر کلک کریں۔

- **Open at Microsoft**: Co-op Translator کو استعمال کرنے کا ایک مختصر 18 منٹ کا تعارف اور فوری رہنمائی۔

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## شراکت

یہ پراجیکٹ شراکتوں اور تجاویز کا خیرمقدم کرتا ہے۔ Azure Co-op Translator میں حصہ لینے میں دلچسپی رکھتے ہیں؟ براہِ کرم ہمارے [CONTRIBUTING.md](../../CONTRIBUTING.md) کو دیکھیں تاکہ آپ جان سکیں کہ آپ Co-op Translator کو مزید قابلِ رسائی بنانے میں کس طرح مدد کر سکتے ہیں۔

## شریک کنندگان

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ضابطۂ اخلاق

اس پراجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) کو اپنایا ہے۔
مزید معلومات کے لیے [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) دیکھیں یا
کوئی اضافی سوالات یا تبصرے ہوں تو [opencode@microsoft.com](mailto:opencode@microsoft.com) سے رابطہ کریں۔

## ذمہ دار مصنوعی ذہانت

Microsoft اپنے صارفین کی مدد کے لیے پرعزم ہے کہ وہ ہمارے AI مصنوعات کو ذمہ داری کے ساتھ استعمال کریں، اپنے تجربات شیئر کریں، اور Transparency Notes اور Impact Assessments جیسے اوزاروں کے ذریعے اعتماد پر مبنی شراکت داری قائم کریں۔ ان وسائل میں سے بہت سے [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔
Microsoft کا ذمہ دار AI کا نقطۂ نظر ہماری انصاف، قابلِ اعتماد اور حفاظت، رازداری اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی کے AI اصولوں پر مبنی ہے۔

اس مثال میں استعمال ہونے والے بڑے پیمانے پر قدرتی زبان، تصویر، اور تقریر ماڈلز ممکنہ طور پر ایسے رویے اختیار کر سکتے ہیں جو غیر منصفانہ، غیر قابلِ اعتماد، یا توہین آمیز ہوں، جس کے نتیجے میں نقصان ہو سکتا ہے۔ خطرات اور حدود کے بارے میں آگاہ رہنے کے لیے براہِ کرم [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ملاحظہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ اپنی فن تعمیر میں ایک حفاظتی نظام شامل کریں جو مضر رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلیکیشنز اور سروسز میں صارف کے بنائے ہوئے اور AI کے بنائے ہوئے مضر مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں ایسی ٹیکسٹ اور تصویر کی APIs شامل ہیں جو مضر مواد کا پتہ لگانے کی اجازت دیتی ہیں۔ ہمارے پاس ایک interactive Content Safety Studio بھی ہے جو آپ کو مختلف طریقوں میں مضر مواد کا پتہ لگانے کے لیے نمونے کوڈ دیکھنے، دریافت کرنے اور آزمانے کی اجازت دیتا ہے۔ درج ذیل [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس تک درخواستیں بھیجنے کے عمل میں رہنمائی فراہم کرتی ہے۔

ایک اور پہلو جسے مدنظر رکھنا ضروری ہے وہ مجموعی ایپلیکیشن کارکردگی ہے۔ کثیر ماڈیول اور کثیر ماڈلز والی ایپلیکیشنز کے ساتھ، کارکردگی سے مراد یہ ہے کہ سسٹم آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، بشمول مضر آؤٹ پٹس پیدا نہ کرنا۔ اپنے مجموعی ایپلیکیشن کی کارکردگی کا اندازہ لگانا اہم ہے، جس کے لیے [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) استعمال کیے جا سکتے ہیں۔

آپ اپنے ترقیاتی ماحول میں اپنے AI ایپلیکیشن کا جائزہ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے لے سکتے ہیں۔ چاہے آپ کے پاس ایک ٹیسٹ ڈیٹا سیٹ ہو یا کوئی ہدف، آپ کی generative AI ایپلیکیشن کی جنریشنز کو بلٹ اِن یا اپنی مرضی کے مطابق ایویلیویٹرز کے ساتھ مقداری طور پر ناپا جاتا ہے۔ اپنے سسٹم کے جائزے کے لیے prompt flow sdk کے ساتھ شروع کرنے کے لیے آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) کی پیروی کر سکتے ہیں۔ ایک بار جب آپ کسی evaluation run کو execute کر لیتے ہیں، تو آپ [Azure AI Studio میں نتائج کو visualize کر سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ٹریڈ مارکس

اس پراجیکٹ میں پروجیکٹس، مصنوعات، یا سروسز کے ٹریڈ مارکس یا لوگوز شامل ہو سکتے ہیں۔ Microsoft کے ٹریڈ مارکس یا لوگوز کا مستند استعمال [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) کے تحت ہونا چاہیے اور ان کی پیروی کرنی چاہیے۔
Microsoft کے ٹریڈ مارکس یا لوگوز کا اس پراجیکٹ کے تبدیل شدہ ورژنز میں استعمال الجھن پیدا نہیں کرے اور Microsoft کی معاونت کا تاثر نہیں دینا چاہیے۔
تیسری پارٹی کے کسی بھی ٹریڈ مارک یا لوگو کے استعمال پر متعلقہ تیسری پارٹی کی پالیسیاں لاگو ہوتی ہیں۔

## مدد حاصل کریں

اگر آپ کہیں پھنس جائیں یا AI ایپس بنانے کے بارے میں کوئی سوال ہو تو شامل ہوں:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر آپ کے پاس پروڈکٹ فیڈبیک ہے یا تعمیر کے دوران کوئی غلطیاں آئیں تو یہاں ملاحظہ کریں:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)