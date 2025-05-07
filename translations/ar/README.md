<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:57:00+00:00",
  "source_file": "README.md",
  "language_code": "ar"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: أتمتة ترجمة الوثائق التعليمية بسهولة

_قم بأتمتة ترجمة وثائقك إلى عدة لغات بسهولة للوصول إلى جمهور عالمي._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### دعم اللغات مدعوم بواسطة Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](./README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **أتمتة قوية**: الآن مع دعم GitHub Actions! قم بترجمة توثيقك تلقائيًا عند إجراء تغييرات على مستودعك، مما يحافظ على تحديث كل شيء بسهولة. [تعرف على المزيد](../..).

## النماذج والخدمات المدعومة

| النوع                  | الاسم                           |
|-----------------------|--------------------------------|
| نموذج اللغة           | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| الرؤية الحاسوبية       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> إذا لم تتوفر خدمة الرؤية الحاسوبية، فسيقوم co-op translator بالتبديل إلى [وضع Markdown فقط](./getting_started/markdown-only-mode.md).

## نظرة عامة: تبسيط ترجمة المحتوى التعليمي الخاص بك

تشكل حواجز اللغة عقبة كبيرة أمام الوصول إلى الموارد التعليمية القيمة والمعرفة التقنية للمتعلمين والمطورين حول العالم. هذا يحد من المشاركة ويبطئ وتيرة الابتكار والتعلم العالمي.

وُلد **Co-op Translator** من الحاجة إلى معالجة عملية الترجمة اليدوية غير الفعالة لسلسلة تعليمية واسعة النطاق من Microsoft (مثل أدلة "للمبتدئين"). تطور ليصبح أداة قوية وسهلة الاستخدام تهدف إلى إزالة هذه الحواجز للجميع. من خلال توفير ترجمات آلية عالية الجودة عبر CLI وGitHub Actions، يمكّن Co-op Translator المعلمين والطلاب والباحثين والمطورين حول العالم من مشاركة والوصول إلى المعرفة دون قيود لغوية.

شاهد كيف ينظم Co-op Translator المحتوى التعليمي المترجم:

![مثال](../../imgs/translation-ex.png)

يتم ترجمة ملفات Markdown ونصوص الصور تلقائيًا وتنظيمها بعناية في مجلدات مخصصة لكل لغة.

**افتح الوصول العالمي لمحتواك التعليمي مع Co-op Translator اليوم!**

## دعم الوصول العالمي لموارد التعلم في Microsoft

يساعد Co-op Translator في سد فجوة اللغة للمبادرات التعليمية الرئيسية في Microsoft، مؤتمتًا عملية الترجمة للمستودعات التي تخدم مجتمع المطورين العالمي. تشمل الأمثلة التي تستخدم Co-op Translator حاليًا:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## الميزات الرئيسية

- **ترجمات آلية**: ترجم النصوص إلى لغات متعددة بسهولة.
- **تكامل مع GitHub Actions**: أتمتة الترجمات كجزء من خط CI/CD الخاص بك.
- **الحفاظ على Markdown**: الحفاظ على صياغة Markdown الصحيحة أثناء الترجمة.
- **ترجمة نص الصور**: استخراج وترجمة النصوص داخل الصور.
- **تقنية LLM المتقدمة**: استخدام نماذج اللغة المتطورة لترجمات عالية الجودة.
- **تكامل سهل**: دمج سلس مع إعداد مشروعك الحالي.
- **تبسيط التعريب**: تبسيط عملية تعريب مشروعك للأسواق الدولية.

## كيف يعمل

![الهيكلية](../../imgs/architecture_241019.png)

يأخذ Co-op Translator ملفات Markdown والصور من مجلد مشروعك ويعالجها كما يلي:

1. **استخراج النص**: استخراج النص من ملفات Markdown، وإذا تم الإعداد (مثلًا باستخدام Azure Computer Vision)، النص الموجود داخل الصور.
1. **الترجمة بالذكاء الاصطناعي**: إرسال النص المستخرج إلى نموذج اللغة المهيأ (Azure OpenAI، OpenAI، إلخ) للترجمة.
1. **حفظ النتائج**: حفظ ملفات Markdown المترجمة والصور (مع النصوص المترجمة) في مجلدات خاصة بكل لغة، مع الحفاظ على التنسيق الأصلي.

## البدء

ابدأ بسرعة باستخدام CLI أو قم بإعداد الأتمتة الكاملة عبر GitHub Actions.

### بداية سريعة: سطر الأوامر

للبدء السريع باستخدام سطر الأوامر:

1. قم بتثبيت الحزمة:
    ```bash
    pip install co-op-translator
    ```
2. إعداد بيانات الاعتماد:
  - أنشئ ملف `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` بعلم:
    ```bash
    translate -l "ko ja fr"
    ```
    *(استبدل `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) في مستودعك. لا حاجة للتثبيت المحلي.
- الأدلة:
  - [دليل GitHub Actions (المستودعات العامة والأسرار القياسية)](./getting_started/github-actions-guide/github-actions-guide-public.md) - استخدم هذا لمعظم المستودعات العامة أو الشخصية التي تعتمد على أسرار المستودع القياسية.
  - [دليل GitHub Actions (مستودعات منظمة Microsoft وإعدادات على مستوى المنظمة)](./getting_started/github-actions-guide/github-actions-guide-org.md) - استخدم هذا الدليل إذا كنت تعمل ضمن منظمة Microsoft على GitHub أو تحتاج إلى استخدام أسرار أو مشغلات على مستوى المنظمة.

> [!NOTE]
> على الرغم من أن هذا الدليل يركز على موارد Azure، يمكنك استخدام أي نموذج لغة مدعوم من قائمة [النماذج والخدمات المدعومة](../..).

### استكشاف الأخطاء والنصائح

- [دليل استكشاف الأخطاء](./getting_started/troubleshooting.md)

### موارد إضافية

- [مرجع الأوامر](./getting_started/command-reference.md): دليل مفصل لجميع الأوامر والخيارات المتاحة.
- [إعداد دعم متعدد اللغات](./getting_started/multi-language-support.md): كيفية إضافة جدول يربط بالإصدارات المترجمة في ملف README الخاص بك.
- [اللغات المدعومة](./getting_started/supported-languages.md): تحقق من قائمة اللغات المدعومة وتعليمات إضافة لغات جديدة.
- [وضع Markdown فقط](./getting_started/markdown-only-mode.md): كيفية ترجمة النص فقط، دون ترجمة الصور.

## العروض التقديمية بالفيديو

تعرف أكثر على Co-op Translator من خلال عروضنا التقديمية _(انقر على الصورة أدناه للمشاهدة على YouTube)_:

- **Open at Microsoft**: مقدمة مختصرة لمدة 18 دقيقة ودليل سريع حول كيفية استخدام Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: دليل تفصيلي لمدة ساعة خطوة بخطوة يغطي كل شيء من فهم ما هو Co-op Translator، إعداد الأداة، استخدامها بفعالية، إلى عرض حي يوضح قدراتها في العمل.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## دعمنا وتعزيز التعلم العالمي

انضم إلينا في ثورة مشاركة المحتوى التعليمي عالميًا! امنح [Co-op Translator](https://github.com/azure/co-op-translator) نجمة ⭐ على GitHub وادعم مهمتنا في إزالة حواجز اللغة في التعلم والتكنولوجيا. اهتمامك ومساهماتك تحدث فرقًا كبيرًا! مساهمات الكود واقتراحات الميزات مرحب بها دائمًا.

## المساهمة

يرحب هذا المشروع بالمساهمات والاقتراحات. هل ترغب في المساهمة في Azure Co-op Translator؟ يرجى الاطلاع على [CONTRIBUTING.md](./CONTRIBUTING.md) للإرشادات حول كيفية المساعدة في جعل Co-op Translator أكثر سهولة في الوصول.

## المساهمون

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## مدونة السلوك

اعتمد هذا المشروع [مدونة السلوك مفتوحة المصدر من Microsoft](https://opensource.microsoft.com/codeofconduct/).
لمزيد من المعلومات، راجع [الأسئلة الشائعة حول مدونة السلوك](https://opensource.microsoft.com/codeofconduct/faq/) أو اتصل بـ [opencode@microsoft.com](mailto:opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## الذكاء الاصطناعي المسؤول

تلتزم Microsoft بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي بمسؤولية، ومشاركة تجاربنا، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات الأثر. يمكن العثور على العديد من هذه الموارد في [https://aka.ms/RAI](https://aka.ms/RAI).
تستند مقاربة Microsoft للذكاء الاصطناعي المسؤول إلى مبادئ الذكاء الاصطناعي الخاصة بنا والتي تشمل العدالة، والموثوقية والسلامة، والخصوصية والأمان، والشمولية، والشفافية، والمساءلة.

يمكن أن تتصرف نماذج اللغة الطبيعية، والصورة، والكلام واسعة النطاق - مثل تلك المستخدمة في هذا المثال - بطرق قد تكون غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضرارًا. يرجى الاطلاع على [ملاحظة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) للاطلاع على المخاطر والقيود.
النهج الموصى به للتخفيف من هذه المخاطر هو تضمين نظام أمان في البنية الخاصة بك يمكنه اكتشاف ومنع السلوك الضار. يوفر [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي يتم إنشاؤه بواسطة المستخدم أو الذكاء الاصطناعي في التطبيقات والخدمات. يتضمن Azure AI Content Safety واجهات برمجة تطبيقات للنصوص والصور تتيح لك اكتشاف المواد الضارة. لدينا أيضًا استوديو Content Safety تفاعلي يسمح لك بمشاهدة واستكشاف وتجربة أمثلة على الشيفرة لاكتشاف المحتوى الضار عبر مختلف الوسائط. يوجهك [وثائق البدء السريع التالية](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) خلال كيفية إرسال الطلبات إلى الخدمة.

جانب آخر يجب أخذه في الاعتبار هو أداء التطبيق العام. مع التطبيقات متعددة الوسائط والنماذج، نعتبر الأداء بمعنى أن النظام يعمل كما تتوقع أنت والمستخدمون، بما في ذلك عدم توليد مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [مقاييس جودة التوليد والمخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). بناءً على مجموعة بيانات اختبار أو هدف معين، يتم قياس نتائج تطبيق الذكاء الاصطناعي التوليدي الخاص بك كميًا باستخدام مقيمين مدمجين أو مقيمين مخصصين من اختيارك. للبدء باستخدام prompt flow sdk لتقييم النظام الخاص بك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ عملية التقييم، يمكنك [عرض النتائج في Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. يخضع الاستخدام المصرح به لعلامات Microsoft التجارية أو شعاراتها ويجب أن يتبع
[إرشادات العلامات التجارية والهوية الخاصة بـ Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
يجب ألا يسبب استخدام علامات Microsoft التجارية أو شعاراتها في نسخ معدلة من هذا المشروع أي لبس أو يوحي برعاية Microsoft.
أي استخدام لعلامات تجارية أو شعارات لأطراف ثالثة يخضع لسياسات تلك الأطراف.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة الاحترافية التي يقوم بها بشر. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.