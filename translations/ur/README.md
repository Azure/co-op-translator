<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:23:06+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# کو-آپ ٹرانسلیٹر

_اپنے تعلیمی GitHub مواد کو خودکار طریقے سے کئی زبانوں میں ترجمہ کریں اور عالمی سطح پر زیادہ لوگوں تک پہنچیں۔_

### 🌐 کثیر لسانی سپورٹ

#### [کو-آپ ٹرانسلیٹر](https://github.com/Azure/Co-op-Translator) کی طرف سے سپورٹ کردہ

[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (آسان)](../zh/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، مکاؤ)](../mo/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [کروشین](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [ایسٹونین](../et/README.md) | [فنش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگیرین](../hu/README.md) | [انڈونیشین](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کوریائی](../ko/README.md) | [لتھوانیائی](../lt/README.md) | [ملائی](../ms/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [نارویجن](../no/README.md) | [فارسی](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../br/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [رومینین](../ro/README.md) | [روسی](../ru/README.md) | [سربین (سیریلک)](../sr/README.md) | [سلوواک](../sk/README.md) | [سلووینین](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحیلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹیگالوگ (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تھائی](../th/README.md) | [ترکش](../tr/README.md) | [یوکرینیائی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)

## جائزہ

**کو-آپ ٹرانسلیٹر** آپ کو اپنے تعلیمی GitHub مواد کو تیزی سے کئی زبانوں میں ترجمہ کرنے کی سہولت دیتا ہے، تاکہ آپ آسانی سے عالمی سطح پر لوگوں تک پہنچ سکیں۔ جب آپ اپنے مارک ڈاؤن فائلز، تصاویر یا جیوپیٹر نوٹ بکس کو اپ ڈیٹ کرتے ہیں، تو ترجمے خود بخود ہم آہنگ ہو جاتے ہیں تاکہ آپ کا تعلیمی GitHub مواد بین الاقوامی صارفین کے لیے ہمیشہ تازہ اور متعلقہ رہے۔

دیکھیں کو-آپ ٹرانسلیٹر کس طرح ترجمہ شدہ تعلیمی GitHub مواد کو منظم کرتا ہے:

![مثال](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ur.png)

## فوری آغاز

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

ڈوکر:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## کم سے کم سیٹ اپ

- `.env` فائل بنائیں، ٹیمپلیٹ استعمال کریں: [.env.template](../../.env.template)
- ایک LLM فراہم کنندہ کنفیگر کریں (Azure OpenAI یا OpenAI)
- اگر تصویر کا ترجمہ کرنا ہے (`-img`)، تو Azure AI Vision بھی سیٹ کریں
- سفارش: اگر آپ کے پاس پہلے سے کسی اور ٹول سے ترجمے موجود ہیں، تو انہیں پہلے صاف کر لیں تاکہ تضاد نہ ہو (مثلاً: `translations/`)
- سفارش: اپنے README میں ترجمہ جات کا سیکشن شامل کریں، [README زبانوں کا ٹیمپلیٹ](./README_languages_template.md) استعمال کریں
- مزید دیکھیں: [Azure AI سیٹ اپ کریں](./getting_started/set-up-azure-ai.md)

## استعمال

تمام سپورٹڈ اقسام کا ترجمہ کریں:

```bash
translate -l "ko ja"
```

صرف مارک ڈاؤن:

```bash
translate -l "de" -md
```

مارک ڈاؤن + تصاویر:

```bash
translate -l "pt" -md -img
```

صرف نوٹ بکس:

```bash
translate -l "zh" -nb
```

مزید فلیگز: [کمانڈ ریفرنس](./getting_started/command-reference.md)

## خصوصیات

- مارک ڈاؤن، نوٹ بکس اور تصاویر کے لیے خودکار ترجمہ
- ترجمہ جات کو ماخذ میں تبدیلی کے ساتھ ہم آہنگ رکھتا ہے
- مقامی طور پر (CLI) یا CI (GitHub Actions) میں کام کرتا ہے
- Azure OpenAI یا OpenAI استعمال کرتا ہے؛ تصاویر کے لیے اختیاری Azure AI Vision
- مارک ڈاؤن کی فارمیٹنگ اور ساخت برقرار رکھتا ہے

## دستاویزات

- [کمانڈ لائن گائیڈ](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions گائیڈ (پبلک ریپوزٹریز اور اسٹینڈرڈ سیکرٹس)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions گائیڈ (Microsoft آرگنائزیشن ریپوزٹریز اور آرگنائزیشن لیول سیٹ اپ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [سپورٹڈ زبانیں](./getting_started/supported-languages.md)
- [مسائل کا حل](./getting_started/troubleshooting.md)

## ہمارا ساتھ دیں اور عالمی تعلیم کو فروغ دیں

ہمارے ساتھ مل کر تعلیمی مواد کو عالمی سطح پر شیئر کرنے کے طریقے میں انقلاب لائیں! [کو-آپ ٹرانسلیٹر](https://github.com/azure/co-op-translator) کو GitHub پر ⭐ دیں اور ہماری اس مشن میں ساتھ دیں کہ تعلیم اور ٹیکنالوجی میں زبان کی رکاوٹیں دور کی جائیں۔ آپ کی دلچسپی اور تعاون سے بڑا فرق پڑتا ہے! کوڈ میں بہتری اور فیچر کی تجاویز ہمیشہ خوش آمدید ہیں۔

### اپنی زبان میں Microsoft کا تعلیمی مواد دریافت کریں

- [AZD فار بیگنرز](https://github.com/microsoft/AZD-for-beginners)
- [ایج AI فار بیگنرز](https://github.com/microsoft/edgeai-for-beginners)
- [ماڈل کانٹیکسٹ پروٹوکول (MCP) فار بیگنرز](https://github.com/microsoft/mcp-for-beginners)
- [AI ایجنٹس فار بیگنرز](https://github.com/microsoft/ai-agents-for-beginners)
- [جنریٹو AI فار بیگنرز (.NET کے ساتھ)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [جنریٹو AI فار بیگنرز](https://github.com/microsoft/generative-ai-for-beginners)
- [جنریٹو AI فار بیگنرز (جاوا کے ساتھ)](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML فار بیگنرز](https://aka.ms/ml-beginners)
- [ڈیٹا سائنس فار بیگنرز](https://aka.ms/datascience-beginners)
- [AI فار بیگنرز](https://aka.ms/ai-beginners)
- [سائبرسیکیورٹی فار بیگنرز](https://github.com/microsoft/Security-101)
- [ویب ڈیولپمنٹ فار بیگنرز](https://aka.ms/webdev-beginners)
- [IoT فار بیگنرز](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ویڈیو پریزنٹیشنز

کو-آپ ٹرانسلیٹر کے بارے میں مزید جانیں ہماری پریزنٹیشنز کے ذریعے _(نیچے دی گئی تصویر پر کلک کریں اور یوٹیوب پر دیکھیں)_:

- **Open at Microsoft**: 18 منٹ کی مختصر تعارف اور کو-آپ ٹرانسلیٹر استعمال کرنے کا فوری گائیڈ۔

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ur.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## تعاون

یہ پروجیکٹ تعاون اور تجاویز کا خیرمقدم کرتا ہے۔ Azure کو-آپ ٹرانسلیٹر میں دلچسپی ہے؟ براہ کرم ہمارے [CONTRIBUTING.md](./CONTRIBUTING.md) دیکھیں کہ آپ کس طرح کو-آپ ٹرانسلیٹر کو مزید قابل رسائی بنانے میں مدد کر سکتے ہیں۔

## معاونین

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ضابطہ اخلاق

اس پروجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) کو اپنایا ہے۔
مزید معلومات کے لیے [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) دیکھیں یا
[opencode@microsoft.com](mailto:opencode@microsoft.com) پر رابطہ کریں اگر آپ کے پاس مزید سوالات یا تبصرے ہوں۔

## ذمہ دار AI

Microsoft اپنے صارفین کو AI مصنوعات ذمہ داری سے استعمال کرنے میں مدد دینے، اپنے تجربات شیئر کرنے اور اعتماد پر مبنی شراکت داری بنانے کے لیے پرعزم ہے، جیسے ٹولز: Transparency Notes اور Impact Assessments۔ ان میں سے کئی وسائل یہاں دستیاب ہیں: [https://aka.ms/RAI](https://aka.ms/RAI)۔
Microsoft کا ذمہ دار AI کا طریقہ کار ہمارے AI اصولوں پر مبنی ہے: انصاف، قابل اعتماد اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت اور جوابدہی۔

بڑے پیمانے پر قدرتی زبان، تصویر اور آواز کے ماڈلز - جیسے اس نمونے میں استعمال ہونے والے - بعض اوقات غیر منصفانہ، غیر قابل اعتماد یا ناگوار رویہ اختیار کر سکتے ہیں، جس سے نقصان ہو سکتا ہے۔ براہ کرم [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) پڑھیں تاکہ آپ کو خطرات اور حدود کا علم ہو۔

ان خطرات کو کم کرنے کے لیے سفارش کی جاتی ہے کہ آپ اپنی آرکیٹیکچر میں ایک حفاظتی نظام شامل کریں جو نقصان دہ رویے کو شناخت اور روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو صارف یا AI کے بنائے گئے نقصان دہ مواد کو ایپلیکیشنز اور سروسز میں شناخت کر سکتا ہے۔ Azure AI Content Safety میں ٹیکسٹ اور امیج APIs شامل ہیں جو نقصان دہ مواد کی شناخت میں مدد دیتے ہیں۔ ہمارے پاس ایک انٹرایکٹو Content Safety Studio بھی ہے، جس میں آپ مختلف اقسام کے نقصان دہ مواد کی شناخت کے لیے نمونہ کوڈ آزما سکتے ہیں۔ یہ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس پر درخواست بھیجنے کا طریقہ بتاتا ہے۔

ایک اور پہلو جسے مدنظر رکھنا ضروری ہے وہ مجموعی ایپلیکیشن کی کارکردگی ہے۔ جب آپ ملٹی موڈل اور ملٹی ماڈلز ایپلیکیشنز بناتے ہیں، تو کارکردگی سے مراد یہ ہے کہ سسٹم ویسا ہی کام کرے جیسا آپ اور آپ کے صارفین توقع کرتے ہیں، اور اس میں نقصان دہ نتائج پیدا نہ ہوں۔ اپنی مجموعی ایپلیکیشن کی کارکردگی کو جانچنا ضروری ہے، جس کے لیے آپ [جنریشن کوالٹی اور رسک و سیفٹی میٹرکس](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) استعمال کر سکتے ہیں۔

آپ اپنی AI ایپلیکیشن کو ڈیولپمنٹ ماحول میں [پرومپٹ فلو SDK](https://microsoft.github.io/promptflow/index.html) کے ذریعے جانچ سکتے ہیں۔ چاہے آپ کے پاس ٹیسٹ ڈیٹا سیٹ ہو یا کوئی ہدف، آپ کی جنریٹو AI ایپلیکیشن کی جنریشنز کو بلٹ ان ایویلیوئیٹرز یا آپ کی پسند کے کسٹم ایویلیوئیٹرز کے ذریعے مقداری طور پر ناپا جاتا ہے۔ اگر آپ پرومپٹ فلو SDK کے ساتھ اپنے سسٹم کی جانچ شروع کرنا چاہتے ہیں تو [کوئیک اسٹارٹ گائیڈ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کریں۔ جب آپ ایویلیوئیشن رن مکمل کر لیتے ہیں، تو آپ [نتائج کو Azure AI Studio میں دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈ مارکس

اس پروجیکٹ میں کسی پروجیکٹ، پروڈکٹ یا سروس کے ٹریڈ مارکس یا لوگوز شامل ہو سکتے ہیں۔ مائیکروسافٹ کے ٹریڈ مارکس یا لوگوز کے مجاز استعمال کے لیے ضروری ہے کہ آپ [مائیکروسافٹ کی ٹریڈ مارک اور برانڈ گائیڈ لائنز](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) پر عمل کریں۔
اس پروجیکٹ کے ترمیم شدہ ورژن میں مائیکروسافٹ کے ٹریڈ مارکس یا لوگوز کا استعمال ایسا نہ ہو کہ صارفین کو کنفیوژن ہو یا مائیکروسافٹ کی اسپانسرشپ کا تاثر ملے۔
کسی بھی تھرڈ پارٹی کے ٹریڈ مارکس یا لوگوز کا استعمال ان کی اپنی پالیسیز کے مطابق ہوگا۔

## مدد حاصل کریں

اگر آپ کو کہیں مشکل پیش آئے یا AI ایپس بنانے کے بارے میں کوئی سوال ہو، تو شامل ہوں:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

اگر آپ کو پروڈکٹ کے بارے میں فیڈبیک دینا ہو یا ایپ بنانے کے دوران کوئی غلطی آئے تو یہاں جائیں:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**اعلانِ دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی اصل زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔