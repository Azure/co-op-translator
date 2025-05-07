<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbc19abb46abfba90855f2b7bd01767",
  "translation_date": "2025-05-06T17:29:04+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
![Logo](../../../../../../imgs/logo.png)

# Co-op Translator: शैक्षिक दस्तावेज़ीकरण का अनुवाद आसानी से स्वचालित करें

_अपने दस्तावेज़ों का अनुवाद कई भाषाओं में आसानी से स्वचालित करें और वैश्विक दर्शकों तक पहुँचें।_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Co-op Translator द्वारा समर्थित भाषाएँ

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](./README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)


[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **शक्तिशाली ऑटोमेशन**: अब GitHub Actions समर्थन के साथ! जब भी आपके रिपॉजिटरी में बदलाव होते हैं, तो आपकी डाक्यूमेंटेशन स्वचालित रूप से अनुवादित हो जाती है, जिससे सब कुछ बिना किसी झंझट के अपडेट रहता है। [और जानें](../..)।

## समर्थित मॉडल और सेवाएँ

| प्रकार                  | नाम                           |
|-----------------------|--------------------------------|
| भाषा मॉडल             | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| कंप्यूटर विज़न        | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> यदि कोई कंप्यूटर विज़न सेवा उपलब्ध नहीं है, तो co-op translator [Markdown-only mode](./getting_started/markdown-only-mode.md) में स्विच हो जाएगा।

## अवलोकन: अपने शैक्षिक सामग्री अनुवाद को सरल बनाएं

भाषाई बाधाएं विश्वभर के शिक्षार्थियों और डेवलपर्स के लिए मूल्यवान शैक्षिक संसाधनों और तकनीकी ज्ञान तक पहुँच को काफी सीमित कर देती हैं। इससे भागीदारी कम होती है और वैश्विक नवाचार तथा सीखने की गति धीमी पड़ जाती है।

**Co-op Translator** Microsoft की अपनी बड़े पैमाने की शैक्षिक श्रृंखला (जैसे "For Beginners" गाइड्स) के लिए गैर-प्रभावी मैनुअल अनुवाद प्रक्रिया को सुधारने की जरूरत से उत्पन्न हुआ। यह एक आसान, शक्तिशाली उपकरण बन गया है जो सभी के लिए ये बाधाएं तोड़ता है। CLI और GitHub Actions के माध्यम से उच्च गुणवत्ता वाली स्वचालित अनुवाद प्रदान करके, Co-op Translator शिक्षकों, छात्रों, शोधकर्ताओं और डेवलपर्स को बिना भाषा की बाधाओं के ज्ञान साझा करने और प्राप्त करने का अवसर देता है।

देखें कि Co-op Translator कैसे अनुवादित शैक्षिक सामग्री को व्यवस्थित करता है:

![उदाहरण](../../../../../../imgs/translation-ex.png)

Markdown फाइलें और छवि में मौजूद टेक्स्ट स्वचालित रूप से अनुवादित होकर भाषा-विशिष्ट फोल्डरों में व्यवस्थित हो जाते हैं।

**आज ही Co-op Translator के साथ अपनी शैक्षिक सामग्री को वैश्विक पहुँच प्रदान करें!**

## Microsoft के लर्निंग संसाधनों के लिए वैश्विक पहुँच का समर्थन

Co-op Translator प्रमुख Microsoft शैक्षिक पहलों के लिए भाषा की दूरी को कम करने में मदद करता है, उन रिपॉजिटरीज़ के लिए अनुवाद प्रक्रिया को स्वचालित करता है जो वैश्विक डेवलपर समुदाय को सेवा देती हैं। वर्तमान में Co-op Translator का उपयोग करने वाले उदाहरण हैं:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## मुख्य विशेषताएँ

- **स्वचालित अनुवाद**: बिना किसी मेहनत के कई भाषाओं में टेक्स्ट का अनुवाद करें।
- **GitHub Actions एकीकरण**: अपने CI/CD पाइपलाइन का हिस्सा बनाकर अनुवाद को स्वचालित करें।
- **Markdown संरक्षित रखें**: अनुवाद के दौरान Markdown सिंटैक्स को सही बनाए रखें।
- **छवि टेक्स्ट अनुवाद**: छवियों में मौजूद टेक्स्ट को निकालकर अनुवादित करें।
- **उन्नत LLM तकनीक**: उच्च गुणवत्ता वाले अनुवाद के लिए अत्याधुनिक भाषा मॉडल का उपयोग करें।
- **आसान एकीकरण**: अपने मौजूदा प्रोजेक्ट सेटअप के साथ सहज रूप से एकीकृत करें।
- **स्थानीयकरण सरल बनाएं**: अपने प्रोजेक्ट को अंतरराष्ट्रीय बाजारों के लिए स्थानीयकृत करने की प्रक्रिया को आसान बनाएं।

## यह कैसे काम करता है

![आर्किटेक्चर](../../../../../../imgs/architecture_241019.png)

Co-op Translator आपके प्रोजेक्ट फोल्डर से Markdown फाइलें और छवियां लेकर निम्नलिखित प्रक्रिया करता है:

1. **टेक्स्ट निकालना**: Markdown फाइलों से टेक्स्ट निकालता है और यदि कॉन्फ़िगर किया गया हो (जैसे Azure Computer Vision के साथ), तो छवियों में मौजूद टेक्स्ट भी निकालता है।
1. **AI अनुवाद**: निकाले गए टेक्स्ट को कॉन्फ़िगर किए गए LLM (Azure OpenAI, OpenAI आदि) को अनुवाद के लिए भेजता है।
1. **परिणाम सहेजना**: अनुवादित Markdown फाइलें और छवियां (अनुवादित टेक्स्ट के साथ) भाषा-विशिष्ट फोल्डरों में सहेजता है, मूल फॉर्मेटिंग को बनाए रखते हुए।

## आरंभ कैसे करें

CLI के साथ जल्दी शुरू करें या GitHub Actions के साथ पूर्ण स्वचालन सेटअप करें।

### त्वरित शुरुआत: कमांड लाइन

कमांड लाइन का उपयोग करके तेजी से शुरू करने के लिए:

1. पैकेज इंस्टॉल करें:
    ```bash
    pip install co-op-translator
    ```
2. क्रेडेंशियल्स कॉन्फ़िगर करें:
  - `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` फ्लैग बनाएं:
    ```bash
    translate -l "ko ja fr"
    ```
    *(अपने रिपॉजिटरी में `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows` को बदलें। स्थानीय इंस्टॉलेशन की आवश्यकता नहीं।
- गाइड्स:
  - [GitHub Actions Guide (Public Repositories & Standard Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md) - अधिकांश सार्वजनिक या व्यक्तिगत रिपॉजिटरी के लिए जो स्टैंडर्ड रिपॉजिटरी सीक्रेट्स पर निर्भर हैं।
  - [GitHub Actions Guide (Microsoft Organization Repos & Org-Level Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md) - यदि आप Microsoft GitHub संगठन के अंदर काम कर रहे हैं या संगठन-स्तर के सीक्रेट्स या रनर्स का उपयोग करना चाहते हैं, तो इस गाइड का उपयोग करें।

> [!NOTE]
> जबकि यह ट्यूटोरियल Azure संसाधनों पर केंद्रित है, आप [supported models and services](../..) सूची से किसी भी समर्थित भाषा मॉडल का उपयोग कर सकते हैं।

### समस्या निवारण और सुझाव

- [Troubleshooting Guide](./getting_started/troubleshooting.md)

### अतिरिक्त संसाधन

- [Command Reference](./getting_started/command-reference.md): उपलब्ध सभी कमांड और विकल्पों का विस्तृत मार्गदर्शन।
- [Multi-language Support Setup](./getting_started/multi-language-support.md): README में अनुवादित संस्करणों के लिंक के लिए तालिका कैसे जोड़ें।
- [Supported Languages](./getting_started/supported-languages.md): समर्थित भाषाओं की सूची और नई भाषाएँ जोड़ने के निर्देश।
- [Markdown-Only Mode](./getting_started/markdown-only-mode.md): केवल टेक्स्ट का अनुवाद कैसे करें, बिना छवि अनुवाद के।

## वीडियो प्रस्तुतियाँ

Co-op Translator के बारे में अधिक जानें हमारी प्रस्तुतियों के माध्यम से _(नीचे दिए गए चित्र पर क्लिक करके YouTube पर देखें)_:

- **Open at Microsoft**: Co-op Translator का संक्षिप्त 18 मिनट का परिचय और त्वरित मार्गदर्शिका।

  [![Open at Microsoft](../../../../../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: एक घंटे का विस्तृत चरण-दर-चरण मार्गदर्शन जिसमें Co-op Translator क्या है, टूल कैसे सेटअप करें, प्रभावी ढंग से उपयोग करें, और इसके कार्यों का लाइव डेमो शामिल है।

  [![Microsoft Reactor](../../../../../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## हमारा समर्थन करें और वैश्विक शिक्षा को बढ़ावा दें

शैक्षिक सामग्री को वैश्विक स्तर पर साझा करने के तरीके में क्रांति लाने में हमारा साथ दें! [Co-op Translator](https://github.com/azure/co-op-translator) को GitHub पर ⭐ दें और सीखने तथा तकनीक में भाषा की बाधाओं को दूर करने के हमारे मिशन का समर्थन करें। आपकी रुचि और योगदान महत्वपूर्ण प्रभाव डालते हैं! कोड योगदान और फीचर सुझाव हमेशा स्वागत योग्य हैं।

## योगदान

यह प्रोजेक्ट योगदान और सुझावों का स्वागत करता है। Azure Co-op Translator में योगदान करना चाहते हैं? कृपया हमारे [CONTRIBUTING.md](./CONTRIBUTING.md) को देखें ताकि आप जान सकें कि कैसे Co-op Translator को और अधिक सुलभ बनाया जा सकता है।

## योगदानकर्ता

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

इस प्रोजेक्ट ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) को अपनाया है।
अधिक जानकारी के लिए देखें [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) या
किसी भी अतिरिक्त प्रश्न या टिप्पणी के लिए [opencode@microsoft.com](mailto:opencode@microsoft.com) से संपर्क करें।

## जिम्मेदार AI

Microsoft अपने ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद करने, अपने अनुभव साझा करने, और ट्रांसपेरेंसी नोट्स और इम्पैक्ट असेसमेंट जैसे उपकरणों के माध्यम से भरोसेमंद साझेदारी बनाने के लिए प्रतिबद्ध है। इन संसाधनों का अधिकांश हिस्सा [https://aka.ms/RAI](https://aka.ms/RAI) पर उपलब्ध है।
Microsoft का जिम्मेदार AI दृष्टिकोण हमारे AI सिद्धांतों पर आधारित है, जिनमें निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशिता, पारदर्शिता, और जवाबदेही शामिल हैं।

बड़े पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल - जैसे इस उदाहरण में उपयोग किए गए - संभावित रूप से ऐसे व्यवहार कर सकते हैं जो अनुचित, अविश्वसनीय, या आपत्तिजनक हो सकते हैं, जिससे नुकसान हो सकता है। कृपया जोखिम और सीमाओं के बारे में सूचित होने के लिए [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।
जोखिमों को कम करने के लिए सुझाया गया तरीका यह है कि आपकी आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल की जाए जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो एप्लिकेशन और सेवाओं में उपयोगकर्ता-जनित और AI-जनित हानिकारक सामग्री का पता लगाने में सक्षम है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। हमारे पास एक इंटरैक्टिव Content Safety Studio भी है जो आपको विभिन्न प्रकार की हानिकारक सामग्री का पता लगाने के लिए नमूना कोड को देखने, एक्सप्लोर करने और आजमाने की सुविधा देता है। निम्नलिखित [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा के लिए अनुरोध करने के चरणों में मार्गदर्शन करता है।

एक और पहलू जिसे ध्यान में रखना चाहिए वह है समग्र एप्लिकेशन प्रदर्शन। मल्टी-मोडल और मल्टी-मॉडल एप्लिकेशन के साथ, हम प्रदर्शन का मतलब लेते हैं कि सिस्टम आपके और आपके उपयोगकर्ताओं की अपेक्षाओं के अनुसार काम करता है, जिसमें हानिकारक आउटपुट न उत्पन्न करना भी शामिल है। आपके समग्र एप्लिकेशन के प्रदर्शन का मूल्यांकन करना महत्वपूर्ण है, इसके लिए आप [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग कर सकते हैं।

आप अपने विकास वातावरण में अपने AI एप्लिकेशन का मूल्यांकन [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके कर सकते हैं। चाहे आपके पास परीक्षण डेटा सेट हो या कोई लक्ष्य, आपकी जनरेटिव AI एप्लिकेशन की जनरेशन को बिल्ट-इन या कस्टम मूल्यांकनकर्ताओं के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए prompt flow sdk के साथ शुरुआत करने के लिए, आप [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का अनुसरण कर सकते हैं। एक बार जब आप मूल्यांकन रन निष्पादित कर लेते हैं, तो आप [Azure AI Studio में परिणामों का विज़ुअलाइज़ेशन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) कर सकते हैं।

## Trademarks

यह प्रोजेक्ट प्रोजेक्ट्स, उत्पादों, या सेवाओं के ट्रेडमार्क या लोगो शामिल कर सकता है। Microsoft के ट्रेडमार्क या लोगो का अधिकृत उपयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) के अनुसार होना चाहिए। इस प्रोजेक्ट के संशोधित संस्करणों में Microsoft के ट्रेडमार्क या लोगो के उपयोग से भ्रम नहीं होना चाहिए और न ही इससे Microsoft के प्रायोजन का आभास होना चाहिए। किसी तीसरे पक्ष के ट्रेडमार्क या लोगो का उपयोग उन तीसरे पक्ष की नीतियों के अधीन होता है।

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।