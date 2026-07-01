# को-ऑप ट्रांसलेटर

_अपने शैक्षिक GitHub सामग्री के अनुवादों को कई भाषाओं में आसानी से स्वचालित और बनाए रखें जब आपका प्रोजेक्ट विकसित होता है._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python पैकेज](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![लाइसेंस: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![डाउनलोड](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![डाउनलोड](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![कंटेनर: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![कोड स्टाइल: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub इश्यूज़](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs का स्वागत है](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**यहाँ से शुरू करें:** [अपना वर्कफ़्लो चुनें](https://azure.github.io/co-op-translator/workflows/) | [कॉन्फ़िगरेशन](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 बहु-भाषा समर्थन

#### [Co-op Translator](https://github.com/Azure/co-op-translator) द्वारा समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गारियाई](../bg/README.md) | [बर्मीज़ (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh-CN/README.md) | [चीनी (पारंपरिक, हांगकांग)](../zh-HK/README.md) | [चीनी (पारंपरिक, मकाऊ)](../zh-MO/README.md) | [चीनी (पारंपरिक, ताइवान)](../zh-TW/README.md) | [क्रोएशियाई](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाई](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](./README.md) | [हंगेरियाई](../hu/README.md) | [इंडोनेशियाई](../id/README.md) | [इतालवी](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड़](../kn/README.md) | [खमेर](../km/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियाई](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नाइजीरियाई पिजिन](../pcm/README.md) | [नॉर्वेजियाई](../no/README.md) | [फ़ारसी (Farsi)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राज़ील)](../pt-BR/README.md) | [पुर्तगाली (पुर्तगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियाई](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियाई](../sl/README.md) | [स्पैनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टैगालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)

> **लोकल क्लोन पसंद करते हैं?**
>
> यह रिपॉजिटरी 50+ भाषाई अनुवाद शामिल करती है जिससे डाउनलोड साइज काफी बढ़ जाता है। बिना अनुवादों के क्लोन करने के लिए sparse checkout का उपयोग करें:
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
> यह आपको कोर्स पूरा करने के लिए आवश्यक सब कुछ देता है और डाउनलोड बहुत तेज़ होता है।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub स्टार्स](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![GitHub Codespaces में खोलें](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** आपकी शैक्षिक GitHub सामग्री को कई भाषाओं में सहजता से स्थानीयकृत करने में मदद करता है।  
जब आप अपने Markdown फाइलें, इमेज, या नोटबुक अपडेट करते हैं, तो अनुवाद स्वचालित रूप से सिंक में रहते हैं, जिससे आपकी सामग्री दुनिया भर के शिक्षार्थियों के लिए सटीक और अप टू डेट बनी रहती है।

इसे रिपॉजिटरी अनुवाद के लिए CLI से, ऑटोमेशन के लिए Python API से, या एजेंट और एडिटर वर्कफ़्लो के लिए MCP सर्वर के माध्यम से उपयोग करें।

अनुवादित सामग्री कैसे व्यवस्थित है इसका उदाहरण:

![उदाहरण](../../imgs/translation-ex.png)

## क्यों Co-op Translator?

एक फ़ाइल का अनुवाद करना आसान है। पूरा डॉक्स रिपॉजिटरी अनुवादित, लिंक्ड, और अप टू डेट रखना ही मुश्किल काम है।

| समस्या | Co-op Translator कैसे मदद करता है |
| --- | --- |
| Long docs are not one prompt | बड़े Markdown फ़ाइलों को चंक्स में विभाजित किया जाता है, इसलिए एक लंबा README एक कमजोर मॉडल प्रतिक्रिया पर निर्भर नहीं रहता। यदि कोई चंक फेल होता है, तो Co-op Translator केवल असफल भाग को फिर से चंंक और रिट्राई कर सकता है। |
| Incomplete translations should not be marked current | एक अधूरा अनुवाद कभी भी अद्यतित के रूप में सील नहीं किया जाना चाहिए। Co-op Translator सेव करने से पहले अनुवाद की अखंडता की जांच करता है और संरचनात्मक रूप से अधूरे मौजूदा अनुवादों का पता लगा सकता है। |
| Links should match the translated repo structure | मैनुअल अनुवाद अक्सर सापेक्ष लिंक्स को स्रोत ट्री की ओर छोड़ देते हैं। Co-op Translator Markdown, नोटबुक, इमेज, और README लिंक्स को `translations/<lang>/...` संरचना से मेल खाने के लिए पुनर्लेखन करता है। |
| Translation should work across an entire repo | Co-op Translator README फाइलें, डॉक्स, नोटबुक, और इमेज टेक्स्ट को एक रिपोजिटरी वर्कफ़्लो के हिस्से के रूप में हैंडल करता है, बजाय फाइलों को एक-एक करके अनुवाद करने के। |
| Maintaining translations matters more than creating them once | स्रोत हैश और अनुवाद मेटाडेटा Co-op Translator को पुरानी फाइलें खोजने, बिना बदलाव वाली फाइलों को स्किप करने, और स्रोत रिपॉ के विकसित होने पर अनुवादित सामग्री को सिंक्रनाइज़ रखने में मदद करते हैं। |

## अनुवाद की स्थिति कैसे प्रबंधित की जाती है

Co-op Translator अनुवादित सामग्री को **संस्करणीकृत सॉफ़्टवेयर आर्टिफैक्ट्स**,  
के रूप में प्रबंधित करता है, न कि स्थैतिक फ़ाइलों के रूप में।

यह उपकरण भाषा-स्कोप्ड मेटाडेटा का उपयोग करके अनुवादित Markdown, इमेज, और नोटबुक की स्थिति को ट्रैक करता है।

यह डिज़ाइन Co-op Translator को सक्षम बनाता है कि वह:

- विश्वसनीय रूप से पुराने अनुवाद का पता लगाए
- Markdown, इमेज, और नोटबुक को सुसंगत रूप से हैंडल करे
- बड़े, तेज़ी से बदलते, बहु-भाषा रिपोजिटरीज़ पर सुरक्षित रूप से स्केल करे

अनुवादों को प्रबंधित आर्टिफैक्ट के रूप में मॉडल करके, अनुवाद वर्कफ़्लोज़ आधुनिक सॉफ़्टवेयर निर्भरता और आर्टिफैक्ट प्रबंधन प्रथाओं के साथ स्वाभाविक रूप से संरेखित होते हैं।

→ [अनुवाद की स्थिति कैसे प्रबंधित की जाती है](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### संबंधित गहन अध्ययन

- [AI अनुवाद में टूटे हुए Markdown की मरम्मत: एक प्रोडक्शन पाइपलाइन को मजबूत बनाना](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## आरंभ करें

Co-op Translator को CLI, Python API, या MCP सर्वर से उपयोग किया जा सकता है। यदि आप स्थानीय अनुवाद, ऑटोमेशन, CI, और एजेंट/एडिटर एकीकरण के बीच चयन कर रहे हैं तो वर्कफ़्लो गाइड से शुरू करें।

- [अपना वर्कफ़्लो चुनें](../../docs/workflows.md)
- [प्रमाण-पत्र कॉन्फ़िगर करें](../../docs/configuration.md)
- [CLI से अनुवाद करें](../../docs/cli.md)
- [Python API के साथ स्वचालित करें](../../docs/api.md)
- [MCP सर्वर से कनेक्ट करें](../../docs/mcp.md)
- [GitHub Actions में चलाएँ](../../docs/github-actions.md)

कॉन्फ़िगरेशन के बाद न्यूनतम CLI उदाहरण:

```bash
python -m venv .venv
# विंडोज़
.venv\Scripts\activate
# मैकओएस/लिनक्स
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

बड़े रिपॉजिटरीज़ पर पहली बार रन करने के लिए, अनुवादित फ़ाइलें लिखने से पहले `--dry-run` का उपयोग करें। सामग्री प्रकार फ्लैग, लॉग, समीक्षा, और लिंक माइग्रेशन के लिए [CLI संदर्भ](../../docs/cli.md) देखें।

Bash/Zsh के साथ कंटेनर त्वरित रन:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell के साथ कंटेनर त्वरित रन:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## विशेषताएँ

- Markdown, नोटबुक और इमेज के लिए स्वचालित अनुवाद
- स्रोत परिवर्तनों के साथ अनुवादों को समन्वित रखता है
- स्थानीय रूप से (CLI) या CI (GitHub Actions) में काम करता है
- MCP के माध्यम से Markdown, नोटबुक, इमेज, समीक्षा और प्रोजेक्ट अनुवाद उपकरण उपलब्ध कराता है
- प्रदाता-समर्थित अनुवाद के लिए Azure OpenAI या OpenAI का उपयोग करता है
- MCP को एजेंट्स को Co-op Translator LLM क्रेडेंशियल्स के बिना Markdown और नोटबुक चंक्स का अनुवाद करवाने की अनुमति देता है
- इमेज टेक्स्ट एक्सट्रैक्शन और अनुवाद के लिए Azure AI Vision का उपयोग करता है
- नियतात्मक (deterministic) जांचों के साथ अनुवाद की संरचना और ताज़गी की समीक्षा करता है
- Markdown फॉर्मेटिंग और संरचना को संरक्षित रखता है

## दस्तावेज़

- [डॉक्यूमेंटेशन साइट](https://azure.github.io/co-op-translator/)
- [अपना वर्कफ़्लो चुनें](../../docs/workflows.md)
- [कॉन्फ़िगरेशन](../../docs/configuration.md)
- [Azure AI सेटअप](../../docs/azure-ai-setup.md)
- [CLI संदर्भ](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP सर्वर](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README भाषाओं टेम्पलेट](../../docs/readme-languages-template.md)
- [समर्थित भाषाएँ](../../docs/supported-languages.md)
- [योगदान](../../CONTRIBUTING.md)
- [समस्या निवारण](../../docs/troubleshooting.md)

### Microsoft-विशेष मार्गदर्शिका
> [!NOTE]
> केवल Microsoft “For Beginners” रिपॉजिटरी के मेंटेनरों के लिए।

- [“अन्य कोर्स” सूची को अपडेट करना (केवल MS Beginners रिपॉजिटरीज़ के लिए)](../../docs/microsoft-beginners.md)

## हमारा समर्थन करें और वैश्विक सीखने को बढ़ावा दें

वैश्विक स्तर पर शैक्षिक सामग्री साझा करने के तरीके में क्रांति लाने में हमारे साथ जुड़ें! GitHub पर [Co-op Translator](https://github.com/azure/co-op-translator) को ⭐ दें और सीखने और प्रौद्योगिकी में भाषा बाधाओं को तोड़ने के हमारे मिशन का समर्थन करें। आपकी रुचि और योगदान एक महत्वपूर्ण प्रभाव डालते हैं! कोड योगदान और फीचर सुझाव हमेशा स्वागत योग्य हैं।

### अपनी भाषा में Microsoft शैक्षिक सामग्री का अन्वेषण करें
- [LangChain4j-शुरुआती के लिए](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD शुरुआती के लिए](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI शुरुआती के लिए](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) शुरुआती के लिए](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents शुरुआती के लिए](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI .NET के साथ शुरुआती के लिए](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI शुरुआती के लिए](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI Java के साथ शुरुआती के लिए](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML शुरुआती के लिए](https://aka.ms/ml-beginners)
- [Data Science शुरुआती के लिए](https://aka.ms/datascience-beginners)
- [AI शुरुआती के लिए](https://aka.ms/ai-beginners)
- [Cybersecurity शुरुआती के लिए](https://github.com/microsoft/Security-101)
- [Web Dev शुरुआती के लिए](https://aka.ms/webdev-beginners)
- [IoT शुरुआती के लिए](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## वीडियो प्रस्तुतियाँ

👉 नीचे की छवि पर क्लिक करके YouTube पर देखें।

- **Open at Microsoft**: Co-op Translator का उपयोग कैसे करें, इस पर एक संक्षिप्त 18 मिनट का परिचय और त्वरित मार्गदर्शिका।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

यह परियोजना योगदान और सुझावों का स्वागत करती है। Azure Co-op Translator में योगदान करने में रुचि रखते हैं? कृपया यह देखें: हमारी [CONTRIBUTING.md](../../CONTRIBUTING.md) जिसमें बताया गया है कि आप Co-op Translator को और अधिक सुलभ बनाने में कैसे मदद कर सकते हैं।

## योगदानकर्ता

[![co-op-translator योगदानकर्ता](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

इस परियोजना ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) को अपनाया है।
अधिक जानकारी के लिए देखें [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) या किसी अतिरिक्त प्रश्न या टिप्पणी के लिए [opencode@microsoft.com](mailto:opencode@microsoft.com) से संपर्क करें।

## जिम्मेदार एआई

Microsoft हमारे ग्राहकों को हमारे एआई उत्पादों का जिम्मेदाराना उपयोग करने में मदद करने, हमारे अनुभव साझा करने, और Transparency Notes और Impact Assessments जैसे उपकरणों के माध्यम से भरोसेमंद साझेदारी बनाने के लिए प्रतिबद्ध है। इन संसाधनों में से कई [https://aka.ms/RAI](https://aka.ms/RAI) पर पाए जा सकते हैं।
Microsoft का जिम्मेदार एआई के प्रति दृष्टिकोण हमारे एआई सिद्धांतों—निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशन, पारदर्शिता, और जवाबदेही—पर आधारित है।

वृहद पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल — जैसे इस नमूने में उपयोग किए गए मॉडल — संभावित रूप से ऐसा व्यवहार कर सकते हैं जो अनुचित, अविश्वसनीय, या आपत्तिजनक हो सकता है, और परिणामस्वरूप हानि कर सकता है। कृपया जोखिमों और सीमाओं के बारे में सूचित होने के लिए [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।

इन जोखिमों को कम करने के लिए सुझाया गया तरीका यह है कि अपने आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल करें जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो आवेदन और सेवाओं में हानिकारक उपयोगकर्ता-जनित और एआई-जनित सामग्री का पता लगा सकता है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। हमारे पास एक इंटरैक्टिव Content Safety Studio भी है जो आपको विभिन्न तरीकों में हानिकारक सामग्री का पता लगाने के लिए उदाहरण कोड देखने, एक्सप्लोर करने और आज़माने की अनुमति देता है। निम्न [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा को अनुरोध भेजने के लिए मार्गदर्शन करता है।

एक और पहलू जिसे ध्यान में रखना चाहिए वह है समग्र एप्लिकेशन प्रदर्शन। बहु-मॉडल और बहु-मॉडल्स एप्लिकेशन के साथ, हम प्रदर्शन को उस रूप में मानते हैं जैसा कि आप और आपके उपयोगकर्ता अपेक्षा करते हैं, जिसमें हानिकारक आउटपुट न उत्पन्न होना भी शामिल है। अपने समग्र एप्लिकेशन के प्रदर्शन का मूल्यांकन करना महत्वपूर्ण है, और इसके लिए आप [generation quality और risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग कर सकते हैं।

आप अपने विकास वातावरण में अपने एआई एप्लिकेशन का मूल्यांकन [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके कर सकते हैं। चाहे आपके पास एक परीक्षण डेटासेट हो या कोई लक्ष्य, आपकी जनरेटिव एआई एप्लिकेशन की जनरेशन को बिल्ट-इन एवैल्युएटर्स या आपकी पसंद के कस्टम एवैल्युएटर्स के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए prompt flow sdk के साथ आरंभ करने हेतु आप [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का पालन कर सकते हैं। एक बार जब आप एक मूल्यांकन रन निष्पादित कर लेते हैं, तो आप [Azure AI Studio में परिणामों को विज़ुअलाइज़ कर सकते हैं](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्क

इस परियोजना में परियोजनाओं, उत्पादों, या सेवाओं के ट्रेडमार्क या लोगो हो सकते हैं। Microsoft ट्रेडमार्क या लोगो का अधिकृत उपयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) के अधीन और उसके अनुसार होना चाहिए।
Microsoft ट्रेडमार्क या लोगो का इस परियोजना के परिवर्तित संस्करणों में उपयोग भ्रम पैदा नहीं करना चाहिए और न ही Microsoft के प्रायोजन का आभास कराना चाहिए।
किसी तृतीय पक्ष के ट्रेडमार्क या लोगो का कोई भी उपयोग उन तृतीय पक्ष की नीतियों के अधीन है।

## सहायता प्राप्त करें

यदि आप अटक जाते हैं या एआई ऐप्स बनाने के बारे में कोई प्रश्न है, तो जुड़ें:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि आपके पास उत्पाद से संबंधित प्रतिक्रिया है या निर्माण के दौरान त्रुटियाँ आ रही हैं तो जाएँ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)