<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:43:03+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
# को-ऑप ट्रांसलेटर

_अपने शैक्षिक GitHub कंटेंट का अनुवाद कई भाषाओं में आसानी से ऑटोमेट करें और वैश्विक दर्शकों तक पहुँचें।_

### 🌐 बहुभाषी समर्थन

#### समर्थित भाषाएँ [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारा

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियाई](../bg/README.md) | [बर्मी (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (पारंपरिक, हांगकांग)](../hk/README.md) | [चीनी (पारंपरिक, मकाऊ)](../mo/README.md) | [चीनी (पारंपरिक, ताइवान)](../tw/README.md) | [क्रोएशियाई](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाई](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](./README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियाई](../id/README.md) | [इतालवी](../it/README.md) | [जापानी](../ja/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियाई](../lt/README.md) | [मलय](../ms/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राजील)](../br/README.md) | [पुर्तगाली (पुर्तगाल)](../pt/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियाई](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियाई](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टैगालोग (फिलिपीनो)](../tl/README.md) | [तमिल](../ta/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## अवलोकन

**Co-op Translator** आपको अपने शैक्षिक GitHub कंटेंट को कई भाषाओं में जल्दी से अनुवाद करने की सुविधा देता है, जिससे आप आसानी से वैश्विक दर्शकों तक पहुँच सकते हैं। जब आप अपने Markdown फाइल, इमेज या Jupyter नोटबुक अपडेट करते हैं, तो अनुवाद अपने आप सिंक्रनाइज़ हो जाते हैं ताकि आपका शैक्षिक GitHub कंटेंट अंतरराष्ट्रीय उपयोगकर्ताओं के लिए हमेशा ताज़ा और प्रासंगिक बना रहे।

देखें Co-op Translator किस तरह अनुवादित शैक्षिक GitHub कंटेंट को व्यवस्थित करता है:

![उदाहरण](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hi.png)

## त्वरित शुरुआत

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

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## न्यूनतम सेटअप

- एक `.env` बनाएं, टेम्पलेट का उपयोग करें: [.env.template](../../.env.template)
- एक LLM प्रदाता कॉन्फ़िगर करें (Azure OpenAI या OpenAI)
- इमेज अनुवाद (`-img`) के लिए, Azure AI Vision भी सेट करें
- अनुशंसित: यदि आपके पास अन्य टूल्स द्वारा बनाए गए अनुवाद हैं, तो पहले उन्हें साफ़ कर लें ताकि कोई टकराव न हो (जैसे: `translations/`)
- अनुशंसित: अपने README में अनुवाद अनुभाग जोड़ें, [README भाषाएँ टेम्पलेट](./README_languages_template.md) का उपयोग करें
- देखें: [Azure AI सेटअप करें](./getting_started/set-up-azure-ai.md)

## उपयोग

सभी समर्थित प्रकारों का अनुवाद करें:

```bash
translate -l "ko ja"
```

केवल Markdown:

```bash
translate -l "de" -md
```

Markdown + इमेज:

```bash
translate -l "pt" -md -img
```

केवल नोटबुक:

```bash
translate -l "zh" -nb
```

अधिक फ्लैग्स: [कमांड संदर्भ](./getting_started/command-reference.md)

## विशेषताएँ

- Markdown, नोटबुक और इमेज के लिए ऑटोमेटेड अनुवाद
- स्रोत में बदलाव के साथ अनुवाद सिंक्रनाइज़ रहते हैं
- लोकली (CLI) या CI (GitHub Actions) में काम करता है
- Azure OpenAI या OpenAI का उपयोग करता है; इमेज के लिए वैकल्पिक Azure AI Vision
- Markdown फॉर्मेटिंग और संरचना को बनाए रखता है

## दस्तावेज़

- [कमांड-लाइन गाइड](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions गाइड (पब्लिक रिपॉजिटरी और स्टैंडर्ड सीक्रेट्स)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions गाइड (Microsoft संगठन रिपॉजिटरी और संगठन स्तर सेटअप)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [समर्थित भाषाएँ](./getting_started/supported-languages.md)
- [समस्या निवारण](./getting_started/troubleshooting.md)

## हमारा समर्थन करें और वैश्विक शिक्षा को बढ़ावा दें

हमारे साथ मिलकर शैक्षिक कंटेंट को वैश्विक स्तर पर साझा करने के तरीके में क्रांति लाएँ! [Co-op Translator](https://github.com/azure/co-op-translator) को GitHub पर ⭐ दें और सीखने व तकनीक में भाषा की बाधाओं को दूर करने के हमारे मिशन का समर्थन करें। आपकी रुचि और योगदान बड़ा असर डालते हैं! कोड योगदान और फीचर सुझाव हमेशा स्वागत योग्य हैं।

### अपनी भाषा में Microsoft शैक्षिक कंटेंट देखें

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

## वीडियो प्रस्तुतियाँ

Co-op Translator के बारे में अधिक जानें हमारे प्रस्तुतियों के माध्यम से _(नीचे दी गई इमेज पर क्लिक करें और YouTube पर देखें)_:

- **Open at Microsoft**: Co-op Translator का 18 मिनट का संक्षिप्त परिचय और त्वरित गाइड।

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

इस प्रोजेक्ट में योगदान और सुझावों का स्वागत है। Azure Co-op Translator में योगदान देने में रुचि है? कृपया हमारे [CONTRIBUTING.md](./CONTRIBUTING.md) देखें, जिसमें बताया गया है कि आप Co-op Translator को और अधिक सुलभ बनाने में कैसे मदद कर सकते हैं।

## योगदानकर्ता

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

इस प्रोजेक्ट ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) को अपनाया है।
अधिक जानकारी के लिए [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) देखें या
[opencode@microsoft.com](mailto:opencode@microsoft.com) पर अतिरिक्त सवाल या टिप्पणियाँ भेजें।

## जिम्मेदार AI

Microsoft अपने ग्राहकों को AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद करने के लिए प्रतिबद्ध है, अपने अनुभव साझा करता है, और पारदर्शिता नोट्स व इम्पैक्ट असेसमेंट जैसे टूल्स के माध्यम से विश्वास-आधारित साझेदारी बनाता है। इन संसाधनों में से कई [https://aka.ms/RAI](https://aka.ms/RAI) पर उपलब्ध हैं।
Microsoft की जिम्मेदार AI की नीति हमारे AI सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशिता, पारदर्शिता, और जवाबदेही।

बड़े पैमाने के प्राकृतिक भाषा, इमेज और स्पीच मॉडल - जैसे कि इस सैंपल में उपयोग किए गए - कभी-कभी अनुचित, अविश्वसनीय या आपत्तिजनक व्यवहार कर सकते हैं, जिससे नुकसान हो सकता है। कृपया [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पढ़ें ताकि आप जोखिमों और सीमाओं के बारे में जान सकें।

इन जोखिमों को कम करने के लिए अनुशंसित तरीका है कि आप अपनी आर्किटेक्चर में एक सुरक्षा सिस्टम शामिल करें, जो हानिकारक व्यवहार का पता लगा सके और रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो आपके एप्लिकेशन और सेवाओं में उपयोगकर्ता-जनित और AI-जनित हानिकारक कंटेंट का पता लगा सकता है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं, जो हानिकारक सामग्री का पता लगाने में मदद करते हैं। हमारे पास एक इंटरैक्टिव Content Safety Studio भी है, जिसमें आप विभिन्न प्रकार की हानिकारक सामग्री का पता लगाने के लिए सैंपल कोड देख सकते हैं, एक्सप्लोर कर सकते हैं और आज़मा सकते हैं। निम्नलिखित [त्वरित शुरुआत दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा के लिए अनुरोध करने की प्रक्रिया बताता है।

एक और महत्वपूर्ण पहलू है आपके एप्लिकेशन की समग्र प्रदर्शन। मल्टी-मोडल और मल्टी-मॉडल एप्लिकेशन में, प्रदर्शन का मतलब है कि सिस्टम वैसा ही काम करता है जैसा आप और आपके उपयोगकर्ता उम्मीद करते हैं, जिसमें हानिकारक आउटपुट न बनाना भी शामिल है। अपने एप्लिकेशन की समग्र प्रदर्शन का मूल्यांकन करना जरूरी है, जिसमें आप [generation quality और risk और safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग कर सकते हैं।

आप अपने डेवलपमेंट एनवायरनमेंट में [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके अपने AI एप्लिकेशन का मूल्यांकन कर सकते हैं। चाहे आपके पास टेस्ट डेटा सेट हो या कोई टारगेट, आपके जनरेटिव AI एप्लिकेशन के आउटपुट को बिल्ट-इन या कस्टम इवैल्यूएटर्स के साथ क्वांटिटेटिव रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए prompt flow sdk से शुरुआत करने के लिए आप [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) देख सकते हैं। एक बार जब आप इवैल्यूएशन रन करते हैं, तो आप [Azure AI Studio में परिणाम देख सकते हैं](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्क

इस प्रोजेक्ट में किसी प्रोजेक्ट, उत्पाद या सेवा के ट्रेडमार्क या लोगो हो सकते हैं। Microsoft के ट्रेडमार्क या लोगो का अधिकृत उपयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) के अनुसार होना चाहिए।
इस प्रोजेक्ट के संशोधित संस्करणों में Microsoft के ट्रेडमार्क या लोगो का उपयोग भ्रम पैदा नहीं करना चाहिए या Microsoft की स्पॉन्सरशिप का संकेत नहीं देना चाहिए।
किसी भी थर्ड-पार्टी ट्रेडमार्क या लोगो का उपयोग उन थर्ड-पार्टी की नीतियों के अधीन है।

## सहायता प्राप्त करें

अगर आप कहीं अटक जाएं या AI ऐप्स बनाने को लेकर कोई सवाल हो, तो जुड़ें:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

अगर आपको प्रोडक्ट फीडबैक देना हो या ऐप बनाते समय कोई त्रुटि मिले, तो जाएं:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।