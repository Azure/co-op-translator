<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:46:06+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# কো-অপ ট্রান্সলেটর

_সহজেই আপনার শিক্ষামূলক GitHub কনটেন্টকে একাধিক ভাষায় অনুবাদ করুন এবং বিশ্বব্যাপী দর্শকদের কাছে পৌঁছান।_

### 🌐 একাধিক ভাষার সমর্থন

#### [কো-অপ ট্রান্সলেটর](https://github.com/Azure/Co-op-Translator) দ্বারা সমর্থিত

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বর্মী (মিয়ানমার)](../my/README.md) | [চাইনিজ (সরলীকৃত)](../zh/README.md) | [চাইনিজ (প্রথাগত, হংকং)](../hk/README.md) | [চাইনিজ (প্রথাগত, ম্যাকাও)](../mo/README.md) | [চাইনিজ (প্রথাগত, তাইওয়ান)](../tw/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রিক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পার্সিয়ান)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../br/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পাঞ্জাবি (গুরুমুখী)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [ইউক্রেনীয়](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামিজ](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## সংক্ষিপ্ত পরিচিতি

**কো-অপ ট্রান্সলেটর** আপনাকে দ্রুত আপনার শিক্ষামূলক GitHub কনটেন্টকে একাধিক ভাষায় অনুবাদ করতে সাহায্য করে, যাতে আপনি সহজেই বিশ্বব্যাপী দর্শকদের কাছে পৌঁছাতে পারেন। আপনি যখন আপনার Markdown ফাইল, ছবি বা Jupyter নোটবুক আপডেট করেন, তখন অনুবাদগুলো স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ হয়, যাতে আপনার শিক্ষামূলক GitHub কনটেন্ট আন্তর্জাতিক ব্যবহারকারীদের জন্য সবসময় আপডেটেড ও প্রাসঙ্গিক থাকে।

দেখুন কো-অপ ট্রান্সলেটর কীভাবে অনুবাদকৃত শিক্ষামূলক GitHub কনটেন্ট সংগঠিত করে:

![উদাহরণ](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.bn.png)

## দ্রুত শুরু করুন

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

ডকার:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ন্যূনতম সেটআপ

- [.env.template](../../.env.template) টেমপ্লেট ব্যবহার করে একটি `.env` তৈরি করুন
- একটি LLM প্রদানকারী কনফিগার করুন (Azure OpenAI অথবা OpenAI)
- ছবি অনুবাদের জন্য (`-img`), Azure AI Vision-ও সেট করুন
- সুপারিশ: যদি আপনার কাছে অন্য টুলে তৈরি করা অনুবাদ থাকে, তাহলে প্রথমে সেগুলো পরিষ্কার করুন যাতে দ্বন্দ্ব না হয় (যেমন: `translations/`)।
- সুপারিশ: আপনার README-তে [README languages template](./README_languages_template.md) ব্যবহার করে একটি অনুবাদ বিভাগ যোগ করুন
- দেখুন: [Azure AI সেটআপ করুন](./getting_started/set-up-azure-ai.md)

## ব্যবহারবিধি

সমস্ত সমর্থিত টাইপ অনুবাদ করুন:

```bash
translate -l "ko ja"
```

শুধুমাত্র Markdown:

```bash
translate -l "de" -md
```

Markdown + ছবি:

```bash
translate -l "pt" -md -img
```

শুধুমাত্র নোটবুক:

```bash
translate -l "zh" -nb
```

আরও ফ্ল্যাগ: [কমান্ড রেফারেন্স](./getting_started/command-reference.md)

## বৈশিষ্ট্য

- Markdown, নোটবুক ও ছবির জন্য স্বয়ংক্রিয় অনুবাদ
- সোর্স পরিবর্তনের সাথে অনুবাদ সিঙ্ক রাখে
- লোকাল (CLI) বা CI (GitHub Actions)-এ কাজ করে
- Azure OpenAI বা OpenAI ব্যবহার করে; ছবির জন্য ঐচ্ছিক Azure AI Vision
- Markdown ফরম্যাটিং ও গঠন অক্ষুণ্ণ রাখে

## ডকুমেন্টেশন

- [কমান্ড-লাইন গাইড](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions গাইড (পাবলিক রিপোজিটরি ও স্ট্যান্ডার্ড সিক্রেটস)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions গাইড (Microsoft অর্গানাইজেশন রিপোজিটরি ও অর্গ-লেভেল সেটআপ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [সমর্থিত ভাষাসমূহ](./getting_started/supported-languages.md)
- [সমস্যা সমাধান](./getting_started/troubleshooting.md)

## আমাদের সমর্থন করুন এবং বিশ্বব্যাপী শেখার প্রসার করুন

বিশ্বব্যাপী শিক্ষামূলক কনটেন্ট ভাগাভাগির ধারা বদলাতে আমাদের সঙ্গে যোগ দিন! [কো-অপ ট্রান্সলেটর](https://github.com/azure/co-op-translator)-এ একটি ⭐ দিন এবং শেখা ও প্রযুক্তিতে ভাষার বাধা ভাঙার আমাদের মিশনকে সমর্থন করুন। আপনার আগ্রহ ও অবদান গুরুত্বপূর্ণ! কোড কন্ট্রিবিউশন ও ফিচার সাজেশন সবসময় স্বাগত।

### আপনার ভাষায় Microsoft-এর শিক্ষামূলক কনটেন্ট এক্সপ্লোর করুন

- [AZD ফর বিগিনারস](https://github.com/microsoft/AZD-for-beginners)
- [এজ এআই ফর বিগিনারস](https://github.com/microsoft/edgeai-for-beginners)
- [মডেল কনটেক্সট প্রোটোকল (MCP) ফর বিগিনারস](https://github.com/microsoft/mcp-for-beginners)
- [এআই এজেন্টস ফর বিগিনারস](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [এমএল ফর বিগিনারস](https://aka.ms/ml-beginners)
- [ডেটা সায়েন্স ফর বিগিনারস](https://aka.ms/datascience-beginners)
- [এআই ফর বিগিনারস](https://aka.ms/ai-beginners)
- [সাইবারসিকিউরিটি ফর বিগিনারস](https://github.com/microsoft/Security-101)
- [ওয়েব ডেভ ফর বিগিনারস](https://aka.ms/webdev-beginners)
- [আইওটি ফর বিগিনারস](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ভিডিও উপস্থাপনা

কো-অপ ট্রান্সলেটর সম্পর্কে আরও জানুন আমাদের উপস্থাপনার মাধ্যমে _(নিচের ছবিতে ক্লিক করে YouTube-এ দেখুন)_:

- **Open at Microsoft**: কো-অপ ট্রান্সলেটর ব্যবহারের সংক্ষিপ্ত ১৮ মিনিটের পরিচিতি ও দ্রুত গাইড।

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.bn.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## কন্ট্রিবিউশন

এই প্রকল্পে অবদান ও পরামর্শ স্বাগত। Azure Co-op Translator-এ অবদান রাখতে আগ্রহী? অনুগ্রহ করে [CONTRIBUTING.md](./CONTRIBUTING.md) দেখুন, কীভাবে কো-অপ ট্রান্সলেটরকে আরও সহজলভ্য করতে সাহায্য করতে পারেন।

## কন্ট্রিবিউটরস

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## আচরণবিধি

এই প্রকল্পে [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করা হয়েছে।
আরও তথ্যের জন্য দেখুন [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা
[opencode@microsoft.com](mailto:opencode@microsoft.com)-এ যোগাযোগ করুন যদি অতিরিক্ত প্রশ্ন বা মন্তব্য থাকে।

## দায়িত্বশীল এআই

Microsoft আমাদের গ্রাহকদের দায়িত্বশীলভাবে আমাদের AI পণ্য ব্যবহারে সহায়তা করতে, আমাদের শেখা শেয়ার করতে এবং Transparency Notes ও Impact Assessments-এর মতো টুলের মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তুলতে প্রতিশ্রুতিবদ্ধ। এই সংক্রান্ত অনেক রিসোর্স পাওয়া যাবে [https://aka.ms/RAI](https://aka.ms/RAI) ঠিকানায়।
Microsoft-এর দায়িত্বশীল AI-এর পদ্ধতি আমাদের AI নীতিমালার উপর ভিত্তি করে: ন্যায্যতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতা।

বৃহৎ-স্কেলের প্রাকৃতিক ভাষা, ছবি ও স্পিচ মডেল—যেমন এই নমুনায় ব্যবহৃত—সম্ভাব্যভাবে অন্যায্য, অবিশ্বস্ত বা আপত্তিকর আচরণ করতে পারে, যা ক্ষতির কারণ হতে পারে। অনুগ্রহ করে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পড়ে ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে জানুন।

এই ঝুঁকি কমানোর জন্য সুপারিশকৃত পদ্ধতি হলো আপনার আর্কিটেকচারে একটি নিরাপত্তা ব্যবস্থা রাখা, যা ক্ষতিকর আচরণ শনাক্ত ও প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর দেয়, যা অ্যাপ্লিকেশন ও সার্ভিসে ক্ষতিকর ব্যবহারকারী-উৎপাদিত ও AI-উৎপাদিত কনটেন্ট শনাক্ত করতে পারে। Azure AI Content Safety-তে টেক্সট ও ইমেজ API রয়েছে, যা ক্ষতিকর উপাদান শনাক্ত করতে দেয়। আমাদের একটি ইন্টারেক্টিভ Content Safety Studio-ও আছে, যেখানে আপনি বিভিন্ন মোডালিটিতে ক্ষতিকর কনটেন্ট শনাক্ত করার নমুনা কোড দেখতে, এক্সপ্লোর করতে ও চেষ্টা করতে পারেন। নিম্নোক্ত [কুইকস্টার্ট ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসে অনুরোধ পাঠানোর গাইড দেবে।

আরেকটি গুরুত্বপূর্ণ বিষয় হলো পুরো অ্যাপ্লিকেশনের পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনের ক্ষেত্রে, পারফরম্যান্স বলতে বোঝায় যে সিস্টেমটি আপনি এবং আপনার ব্যবহারকারীদের প্রত্যাশা অনুযায়ী কাজ করছে কিনা, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার পুরো অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা জরুরি, [জেনারেশন কোয়ালিটি এবং রিস্ক ও সেফটি মেট্রিক্স](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে।

আপনি আপনার ডেভেলপমেন্ট এনভায়রনমেন্টে [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা টার্গেট দেওয়া হলে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের আউটপুটগুলো বিল্ট-ইন ইভ্যালুয়েটর বা আপনার পছন্দের কাস্টম ইভ্যালুয়েটর দিয়ে পরিমাপ করা হয়। আপনার সিস্টেম মূল্যায়নের জন্য prompt flow sdk দিয়ে শুরু করতে চাইলে [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি ইভ্যালুয়েশন রান সম্পন্ন করলে, [Azure AI Studio-তে ফলাফল ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্ক

এই প্রকল্পে বিভিন্ন প্রকল্প, পণ্য, বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহারের অনুমোদিত নিয়ম [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।
এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহার করলে যেন বিভ্রান্তি না হয় বা Microsoft-এর স্পনসরশিপ বোঝায় না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহারের ক্ষেত্রে তাদের নিজস্ব নীতিমালা অনুসরণ করতে হবে।

## সাহায্য পাওয়ার উপায়

আপনি যদি কোনো সমস্যায় পড়েন বা AI অ্যাপ তৈরি নিয়ে কোনো প্রশ্ন থাকে, তাহলে যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

আপনার যদি কোনো পণ্যের ফিডব্যাক থাকে বা অ্যাপ তৈরি করতে গিয়ে কোনো ত্রুটি পান, তাহলে দেখুন:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।