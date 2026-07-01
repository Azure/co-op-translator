# Co-op Translator

_قم بأتمتة وصيانة الترجمات لمحتوى GitHub التعليمي عبر لغات متعددة بسهولة بينما يتطور مشروعك._

![بايثون 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![حزمة بايثون](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![الرخصة: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![التنزيلات](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![التنزيلات](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![حاوية: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![نمط الشيفرة: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![المساهمون على GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![قضايا GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![طلبات السحب على GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![طلبات السحب مرحب بها](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**ابدأ من هنا:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 دعم متعدد اللغات

#### مدعوم بواسطة [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[العربية](./README.md) | [البنغالية](../bn/README.md) | [البلغارية](../bg/README.md) | [البورمية (ميانمار)](../my/README.md) | [الصينية (مبسطة)](../zh-CN/README.md) | [الصينية (تقليدية، هونغ كونغ)](../zh-HK/README.md) | [الصينية (تقليدية، ماكاو)](../zh-MO/README.md) | [الصينية (تقليدية، تايوان)](../zh-TW/README.md) | [الكرواتية](../hr/README.md) | [التشيكية](../cs/README.md) | [الدانمركية](../da/README.md) | [الهولندية](../nl/README.md) | [الإستونية](../et/README.md) | [الفنلندية](../fi/README.md) | [الفرنسية](../fr/README.md) | [الألمانية](../de/README.md) | [اليونانية](../el/README.md) | [العبرية](../he/README.md) | [الهندية](../hi/README.md) | [الهنغارية](../hu/README.md) | [الإندونيسية](../id/README.md) | [الإيطالية](../it/README.md) | [اليابانية](../ja/README.md) | [الكانادية](../kn/README.md) | [الخميرية](../km/README.md) | [الكورية](../ko/README.md) | [اللتوانية](../lt/README.md) | [الماليزية](../ms/README.md) | [المالايالامية](../ml/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [البيجين النيجيري](../pcm/README.md) | [النرويجية](../no/README.md) | [الفارسية (فارسي)](../fa/README.md) | [البولندية](../pl/README.md) | [البرتغالية (البرازيل)](../pt-BR/README.md) | [البرتغالية (البرتغال)](../pt-PT/README.md) | [البنجابية (غورموخي)](../pa/README.md) | [الرومانية](../ro/README.md) | [الروسية](../ru/README.md) | [الصربية (السيريلية)](../sr/README.md) | [السلوفاكية](../sk/README.md) | [السلوفينية](../sl/README.md) | [الإسبانية](../es/README.md) | [السواحلية](../sw/README.md) | [السويدية](../sv/README.md) | [التاغالوغية (الفلبينية)](../tl/README.md) | [التاميلية](../ta/README.md) | [التيلوجو](../te/README.md) | [اللغة التايلاندية](../th/README.md) | [التركية](../tr/README.md) | [الأوكرانية](../uk/README.md) | [الأردية](../ur/README.md) | [الفيتنامية](../vi/README.md)

> **تفضل الاستنساخ محليًا؟**
>
> هذا المستودع يتضمن ترجمات لأكثر من 50 لغة مما يزيد بشكل كبير من حجم التنزيل. للاستنساخ بدون الترجمات، استخدم السحب الانتقائي (sparse checkout):
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
> هذا يمنحك كل ما تحتاجه لإكمال الدورة مع تنزيل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![المتابعون على GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![التفرعات على GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![النجوم على GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![ديسكورد Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![افتح في GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## نظرة عامة

**Co-op Translator** يساعدك على تعريب محتوى GitHub التعليمي الخاص بك إلى لغات متعددة بسهولة.
عندما تقوم بتحديث ملفات Markdown أو الصور أو دفاتر الملاحظات، تظل الترجمات متزامنة تلقائيًا، مما يضمن بقاء المحتوى دقيقًا ومحدثًا للمتعلمين حول العالم.

استخدمه من سطر الأوامر لترجمة المستودع، أو من واجهة برمجة بايثون للأتمتة، أو عبر خادم MCP لتدفقات عمل الوكلاء والمحررين.

مثال على كيفية تنظيم المحتوى المترجم:

![مثال](../../imgs/translation-ex.png)

## لماذا Co-op Translator؟

ترجمة ملف واحد سهلة. الحفاظ على مستودع وثائق كامل
مترجمًا، ومربوطًا، ومحدثًا هو الجزء الصعب.

| المشكلة | كيف يساعد Co-op Translator |
| --- | --- |
| المستندات الطويلة ليست مطالبة واحدة | يتم تقسيم ملفات Markdown الكبيرة إلى أجزاء، لذا لا يعتمد ملف README طويل على استجابة نموذج واحدة هشة. إذا فشل جزء، يمكن لـ Co-op Translator إعادة المحاولة وإعادة تقسيم الجزء الفاشل فقط. |
| يجب ألا تُعتبر الترجمات غير المكتملة حالية | يجب ألا تُغلق ترجمة مقتظة على أنها محدثة. يتحقق Co-op Translator من سلامة الترجمة قبل الحفظ ويمكنه اكتشاف الترجمات الحالية الناقصة بنيويًا. |
| يجب أن تتطابق الروابط مع هيكل المستودع المترجم | غالبًا ما تترك الترجمات اليدوية الروابط النسبية تشير مرة أخرى إلى شجرة المصدر. يقوم Co-op Translator بإعادة كتابة روابط Markdown ودفاتر الملاحظات والصور وREADME لتطابق هيكل `translations/<lang>/...`. |
| يجب أن تعمل الترجمة عبر المستودع بأكمله | يتعامل Co-op Translator مع ملفات README، والوثائق، ودفاتر الملاحظات، ونصوص الصور كجزء من سير عمل مستودع واحد، بدلًا من ترجمة الملفات واحدًا تلو الآخر. |
| الحفاظ على الترجمات أهم من إنشائها مرة واحدة | تتيح هاشات المصدر وبيانات تعريف الترجمة لـ Co-op Translator العثور على الملفات القديمة، وتخطي الملفات غير المتغيرة، والحفاظ على تزامن المحتوى المترجم مع تطور المستودع المصدر. |

## كيف يُدار حالة الترجمة

يتعامل Co-op Translator مع المحتوى المترجم كـ "مخزنات برمجية مُصنفة بالإصدارات"،  
وليس كملفات ثابتة.

يتتبع الأداة حالة Markdown المترجم، والصور، ودفاتر الملاحظات
باستخدام بيانات تعريف نطاق اللغة.

يتيح هذا التصميم لـ Co-op Translator أن:

- يكتشف الترجمات القديمة بشكل موثوق
- يعامل Markdown والصور ودفاتر الملاحظات بشكل متسق
- يتوسع بأمان عبر مستودعات متعددة اللغات كبيرة وسريعة الحركة

من خلال نمذجة الترجمات كآثار مُدارة،
تتوافق سير عمل الترجمة طبيعيًا مع ممارسات
إدارة اعتماديات وقطع برمجية حديثة.

→ [كيفية إدارة حالة الترجمة](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### مقالات متعمقة ذات صلة

- [إصلاح Markdown المعطوب في الترجمة بواسطة الذكاء الاصطناعي: تقوية خط أنابيب الإنتاج](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## ابدأ

يمكن استخدام Co-op Translator من سطر الأوامر، أو واجهة بايثون، أو خادم MCP. ابدأ بدليل سير العمل إذا كنت تختار بين الترجمة المحلية، أو الأتمتة، أو CI، أو تكامل الوكيل/المحرر.

- [اختر سير عملك](../../docs/workflows.md)
- [تهيئة بيانات الاعتماد](../../docs/configuration.md)
- [الترجمة من سطر الأوامر](../../docs/cli.md)
- [الأتمتة عبر واجهة بايثون](../../docs/api.md)
- [الاتصال بخادم MCP](../../docs/mcp.md)
- [التشغيل في GitHub Actions](../../docs/github-actions.md)

مثال CLI بسيط بعد التهيئة:

```bash
python -m venv .venv
# ويندوز
.venv\Scripts\activate
# ماك أو إس/لينكس
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

للمرات الأولى على مستودعات كبيرة، استخدم `--dry-run` قبل كتابة الملفات المترجمة. راجع [مرجع CLI](../../docs/cli.md) لعلمات نوع المحتوى، والسجلات، والمراجعة، وترحيل الروابط.

تشغيل سريع للحاوية عبر Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

تشغيل سريع للحاوية عبر PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## الميزات

- ترجمة آلية للـ Markdown، ودفاتر الملاحظات، والصور
- يحافظ على تزامن الترجمات مع تغييرات المصدر
- يعمل محليًا (CLI) أو في CI (GitHub Actions)
- يوفّر أدوات ترجمة للـ Markdown، ودفاتر الملاحظات، والصور، والمراجعة، والمشروع عبر MCP
- يستخدم Azure OpenAI أو OpenAI للترجمة المدعومة من مزود
- يتيح لـ MCP استضافة وكلاء لترجمة أجزاء Markdown ودفاتر الملاحظات بدون بيانات اعتماد LLM لـ Co-op Translator
- يستخدم Azure AI Vision لاستخراج نص الصورة وترجمته
- يراجع بنية الترجمة وحداثتها عبر فحوص حتمية
- يحافظ على تنسيق وبنية Markdown

## الوثائق

- [موقع الوثائق](https://azure.github.io/co-op-translator/)
- [اختر سير عملك](../../docs/workflows.md)
- [الإعداد](../../docs/configuration.md)
- [إعداد Azure AI](../../docs/azure-ai-setup.md)
- [مرجع CLI](../../docs/cli.md)
- [واجهة بايثون البرمجية](../../docs/api.md)
- [خادم MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [قالب لغات README](../../docs/readme-languages-template.md)
- [اللغات المدعومة](../../docs/supported-languages.md)
- [المساهمة](../../CONTRIBUTING.md)
- [استكشاف الأخطاء وإصلاحها](../../docs/troubleshooting.md)

### دليل مخصص لمايكروسوفت
> [!NOTE]
> لمؤسسي ومستوديعات "للمبتدئين" التابعة لمايكروسوفت فقط.

- [تحديث قائمة "الدورات الأخرى" (لمستودعات MS Beginners فقط)](../../docs/microsoft-beginners.md)

## ادعمنا وادعم التعلم العالمي

انضم إلينا في تحويل طريقة مشاركة المحتوى التعليمي عالميًا! امنح [Co-op Translator](https://github.com/azure/co-op-translator) نجمة ⭐ على GitHub وادعم مهمتنا في إزالة حواجز اللغة في التعلم والتكنولوجيا. اهتمامك ومساهماتك يحدثان تأثيرًا كبيرًا! مساهمات الشيفرة واقتراحات الميزات مرحب بها دائمًا.

### استكشف محتوى مايكروسوفت التعليمي بلغتك
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

## عروض فيديو

👉 انقر الصورة أدناه للمشاهدة على YouTube.

- **Open at Microsoft**: مقدمة موجزة مدتها 18 دقيقة ودليل سريع حول كيفية استخدام Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## المساهمة

يرحب هذا المشروع بالمساهمات والاقتراحات. هل ترغب في المساهمة في Azure Co-op Translator؟ يرجى الاطلاع على [CONTRIBUTING.md](../../CONTRIBUTING.md) للاطلاع على الإرشادات حول كيفية المساعدة في جعل Co-op Translator أكثر سهولة في الاستخدام.

## المساهمون

[![مساهمو co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## مدونة السلوك

اعتمد هذا المشروع على [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
لمزيد من المعلومات راجع [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) أو
تواصل مع [opencode@microsoft.com](mailto:opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## الذكاء الاصطناعي المسؤول

تلتزم Microsoft بمساعدة عملائنا على استخدام منتجاتنا المدعومة بالذكاء الاصطناعي بمسؤولية، ومشاركة ما تعلمناه، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات الأثر. يمكن العثور على العديد من هذه الموارد على [https://aka.ms/RAI](https://aka.ms/RAI).
نهج Microsoft تجاه الذكاء الاصطناعي المسؤول يستند إلى مبادئنا المتعلقة بالعدالة والموثوقية والسلامة والخصوصية والأمن والشمولية والشفافية والمساءلة.

يمكن للنماذج واسعة النطاق للغة والصورة والصوت - مثل تلك المستخدمة في هذا المثال - أن تتصرف بطرق قد تكون غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضرارًا. يرجى الرجوع إلى [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) للاطلاع على المخاطر والقيود.

النهج الموصى به للتخفيف من هذه المخاطر هو تضمين نظام أمان في البنية المعمارية يمكنه اكتشاف ومنع السلوك الضار. يوفر [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة مستقلة من الحماية، قادرة على اكتشاف المحتوى الضار الذي ينشئه المستخدم أو المحتوى الناتج عن الذكاء الاصطناعي في التطبيقات والخدمات. يتضمن Azure AI Content Safety واجهات برمجة تطبيقات للنص والصورة تتيح لك اكتشاف المواد الضارة. لدينا أيضًا Content Safety Studio التفاعلي الذي يتيح لك عرض وتجربة أمثلة التعليمات البرمجية لاكتشاف المحتوى الضار عبر وسائط مختلفة. يوجهك مستند البدء السريع التالي [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) خلال كيفية إجراء الطلبات إلى الخدمة.

جانب آخر يجب أخذه في الحسبان هو أداء التطبيق ككل. مع التطبيقات متعددة الوسائط والمتعددة النماذج، نعني بالأداء أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم توليد مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). سواء كان لديك مجموعة بيانات اختبار أو هدف معين، يتم قياس مخرجات تطبيق الذكاء الاصطناعي التوليدي كميًا باستخدام المقيمين المدمجين أو مقيمين مخصصين من اختيارك. للبدء باستخدام prompt flow sdk لتقييم نظامك، يمكنك متابعة [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل تقييم، يمكنك [عرض النتائج في Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشروعات أو منتجات أو خدمات. يخضع الاستخدام المصرح به لعلامات Microsoft التجارية أو شعاراتها ويجب أن يتبع
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
استخدام علامات Microsoft التجارية أو شعاراتها في نسخ معدلة من هذا المشروع يجب ألا يسبب ارتباكًا أو يوحي برعاية من Microsoft.
أي استخدام لعلامات تجارية أو شعارات طرف ثالث يخضع لسياسات تلك الأطراف الثالثة.

## الحصول على المساعدة

إذا واجهت صعوبة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

إذا كان لديك ملاحظات عن المنتج أو واجهت أخطاء أثناء البناء زر:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)