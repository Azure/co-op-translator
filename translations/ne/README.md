# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

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

**यहाँबाट सुरु गर्नुहोस्:** [आफ्नो वर्कफ्लो छान्नुहोस्](https://azure.github.io/co-op-translator/workflows/) | [कन्फिगरेसन](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 बहुभाषी समर्थन

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियाली](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh-CN/README.md) | [चीनी (परम्परागत, हङकङ)](../zh-HK/README.md) | [चीनी (परम्परागत, मकाउ)](../zh-MO/README.md) | [चीनी (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएशियाली](../hr/README.md) | [चेख](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाली](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रान्सेली](../fr/README.md) | [जर्मन](../de/README.md) | [यूनानी](../el/README.md) | [हिब्रू](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इन्डोनेशियाली](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड](../kn/README.md) | [खमेर](../km/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियाली](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजेरीयन पिजिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [पर्शियन (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगाली (ब्राजिल)](../pt-BR/README.md) | [पोर्तुगाली (पोर्चुगल)](../pt-PT/README.md) | [पञ्जाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाली (साइरिलिक)](../sr/README.md) | [स्लोभाक](../sk/README.md) | [स्लोभेनियाली](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [ट्यागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाइ](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [भियतनामी](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**
>
> यस रिपोजिटरीमा 50+ भाषा अनुवादहरू समावेश छन् जसले डाउनलोड साइज उल्लेखनीय रूपमा बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
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
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै कुरा बढी छिटो डाउनलोडको साथ दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## सारांश

**Co-op Translator** ले तपाईंलाई सजिलैसँग तपाईंको शैक्षिक GitHub सामग्रीलाई बहुभाषामा स्थानीयकरण गर्न मद्दत गर्छ।
जब तपाईंले आफ्नो Markdown फाइलहरू, तस्बिरहरू, वा नोटबुकहरू अपडेट गर्नुहुन्छ, अनुवादहरू स्वचालित रूपमा समक्रमित रहन्छन्, जसले विश्वभरका सिक्नेहरूका लागि तपाईंको सामग्री सही र अद्यावधिक रहन सुनिश्चित गर्छ।

यस लाई रिपोजिटरी अनुवादका लागि CLI बाट, स्वचालनका लागि Python API बाट, वा एजेन्ट र सम्पादनकर्ता वर्कफ्लोका लागि MCP सर्भर मार्फत प्रयोग गर्न सकिन्छ।

अनुवादित सामग्री कसरी व्यवस्थित गरिएको छ भन्ने उदाहरण:

![उदाहरण](../../imgs/translation-ex.png)

## किन Co-op Translator?

एक फाइल अनुवाद गर्नु सजिलो छ। पूरा डकुमेन्टेसन रिपोजिटरीलाई
अनुवादित, लिंक गरिएको, र अद्यावधिक राख्नु नै कठिन भाग हो।

| समस्या | Co-op Translator कसरी मद्दत गर्छ |
| --- | --- |
| Long docs are not one prompt | लामो Markdown फाइलहरू टुक्रा गरेर विभाजन गरिन्छ, ताकि एउटा लामो README एक नाजुक मोडेल प्रतिक्रियामा निर्भर नहोस्। यदि कुनै chunk असफल भयो भने, Co-op Translator केवल असफल भागलाई पुनः प्रयास र पुनः-चंक गर्न सक्छ। |
| Incomplete translations should not be marked current | अधूरा अनुवादलाई कहिल्यै अद्यावधिक मान्न बन्द गर्नुहोस्। Co-op Translator ले बचत गर्नु अघि अनुवादको अखण्डता जाँच्छ र संरचनात्मक रूपमा अधूरा भएका पहिलेका अनुवादहरू पत्ता लगाउन सक्छ। |
| Links should match the translated repo structure | म्यानुअल अनुवादहरूले प्रायः सापेक्ष लिंकहरू स्रोत ट्रीतर्फ फर्किन्छन्। Co-op Translator ले Markdown, नोटबुक, तस्बिर, र README लिंकहरू `translations/<lang>/...` संरचनासँग मेल खाने गरी पुनर्लेखन गर्छ। |
| Translation should work across an entire repo | Co-op Translator ले README फाइलहरू, डकुमेन्टेसन, नोटबुकहरू, र तस्बिरको पाठलाई एउटा रिपोजिटरी वर्कफ्लोको हिस्सा रूपमा ह्यान्डल गर्छ, एक-एक गरी फाइलहरु अनुवाद गर्ने सट्टा। |
| Maintaining translations matters more than creating them once | स्रोत ह्यास र अनुवाद मेटा डाटा ले Co-op Translator लाई पुराना फाइलहरू पत्ता लगाउन, नबदलिएको फाइलहरू स्किप गर्न, र स्रोत रिपोजिटरी विकास हुँदा अनुवादित सामग्री समक्रमित राख्न मद्दत गर्छ। |

## अनुवाद अवस्था कसरी व्यवस्थापन गरिन्छ

Co-op Translator ले अनुवादित सामग्रीलाई **versioned software artifacts** को रूपमा व्यवस्थापन गर्छ,  
स्टेटिक फाइलहरू जस्तो होइन।

यो टुलले अनुवाद गरिएको Markdown, तस्बिरहरू, र नोटबुकहरूको अवस्था
**language-scoped metadata** प्रयोग गरेर ट्र्याक गर्छ।

यस डिजाइनले Co-op Translator लाई अनुमति दिन्छ:

- भरपर्दो रूपमा पुराना अनुवादहरू पत्ता लगाउन
- Markdown, तस्बिरहरू, र नोटबुकहरूलाई सुसंगत रूपमा व्यवहार गर्न
- ठूलो, छिटो-गतिमा चल्ने, बहुभाषी रिपोजिटरीहरूमा सुरक्षित रूपमा स्केल गर्न

अनुवादहरूलाई व्यवस्थापन गरिएका आर्टिफ्याक्टका रूपमा मोडल गर्दा,
अनुवाद वर्कफ्लोहरू आधुनिक सफ्टवेयर निर्भरता र आर्टिफ्याक्ट व्यवस्थापन अभ्यासहरूसँग स्वाभाविक रूपमा मेल खान्छन्।

→ [अनुवाद अवस्था कसरी व्यवस्थापन गरिन्छ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### सम्बन्धित विस्तृत लेखहरू

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## सुरु गर्नुहोस्

Co-op Translator लाई CLI, Python API, वा MCP सर्भरबाट प्रयोग गर्न सकिन्छ। यदि तपाईं स्थानीय अनुवाद, स्वचालन, CI, र एजेन्ट/सम्पादक एकीकरणको बीच रोज्ने सोचमा हुनुहुन्छ भने वर्कफ्लो मार्गदर्शिका बाट सुरु गर्नुहोस्।

- [आफ्नो वर्कफ्लो छान्नुहोस्](../../docs/workflows.md)
- [क्रेडेन्सियल कन्फिगर गर्नुहोस्](../../docs/configuration.md)
- [CLI बाट अनुवाद गर्नुहोस्](../../docs/cli.md)
- [Python API सँग स्वचालन गर्नुहोस्](../../docs/api.md)
- [MCP सर्भरसँग जडान गर्नुहोस्](../../docs/mcp.md)
- [GitHub Actions मा चलाउनुहोस्](../../docs/github-actions.md)

कन्फिगरेसन पछि न्यूनतम CLI उदाहरण:

```bash
python -m venv .venv
# विन्डोज
.venv\Scripts\activate
# म्याकओएस/लिनक्स
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

ठूला रिपोजिटरीहरूमा पहिलो दौडहरूका लागि, अनुवादित फाइलहरू लेख्नु अघि `--dry-run` प्रयोग गर्नुहोस्। समग्री प्रकार झण्डा, लगहरू, समीक्षा, र लिंक माइग्रेशनका लागि [CLI Reference](../../docs/cli.md) हेर्नुहोस्।

Bash/Zsh सहित कन्टेनर छिटो चलाउने:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell सहित कन्टेनर छिटो चलाउने:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## विशेषताहरू

- Markdown, नोटबुकहरू, र तस्बिरहरूको लागि स्वचालित अनुवाद
- स्रोत परिवर्तनहरूसँग अनुवादहरू समक्रमित राख्छ
- स्थानीय (CLI) वा CI (GitHub Actions) मा काम गर्छ
- MCP मार्फत Markdown, नोटबुक, तस्बिर, समीक्षा, र प्रोजेक्ट अनुवाद उपकरणहरू एक्स्पोज गर्छ
- Azure OpenAI वा OpenAI प्रयोग गरेर प्रदायक समर्थन गरिएको अनुवाद
- MCP लाई एजेन्टहरूलाई Co-op Translator LLM क्रेडेन्सियल बिना Markdown र नोटबुक chunk हरू अनुवाद गर्न होस्ट गर्न अनुमति दिन्छ
- तस्बिरको पाठ निकाल्न र अनुवाद गर्न Azure AI Vision प्रयोग गर्छ
- निर्धारक जाँचहरूसँग अनुवाद संरचना र ताजगी समीक्षा गर्छ
- Markdown फर्म्याटिङ र संरचना संरक्षित राख्छ

## कागजात

- [डकुमेन्टेसन साइट](https://azure.github.io/co-op-translator/)
- [आफ्नो वर्कफ्लो छान्नुहोस्](../../docs/workflows.md)
- [कन्फिगरेसन](../../docs/configuration.md)
- [Azure AI सेटअप](../../docs/azure-ai-setup.md)
- [CLI सन्दर्भ](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README भाषाहरू टेम्पलेट](../../docs/readme-languages-template.md)
- [समर्थित भाषाहरू](../../docs/supported-languages.md)
- [योगदान कसरी गर्ने](../../CONTRIBUTING.md)
- [समस्या समाधान](../../docs/troubleshooting.md)

### Microsoft-विशेष मार्गदर्शन
> [!NOTE]
> केवल Microsoft “For Beginners” रिपोजिटरीहरूको मेन्टेनेरहरूको लागि।

- [“other courses” सूची अपडेट गर्नु (केवल MS Beginners रिपोजिटरीहरूको लागि)](../../docs/microsoft-beginners.md)

## हामीलाई समर्थन गर्नुहोस् र विश्वव्यापी सिकाइ प्रवर्द्धन गर्नुहोस्

शैक्षिक सामग्रीलाई विश्वव्यापी रूपमा कसरी साझा गरिन्छ भन्ने क्रान्तिमा हामीसँग सामेल हुनुहोस्! GitHub मा [Co-op Translator](https://github.com/azure/co-op-translator) लाई ⭐ दिनुहोस् र सिकाइ र प्रविधिमा भाषा अवरोधहरू तोड्ने हाम्रो मिशनलाई समर्थन गर्नुहोस्। तपाईंको चासो र योगदानले महत्वपूर्ण प्रभाव पार्छ! कोड योगदान र सुविधाको सुझावहरू सधैं स्वागतयोग्य छन्।

### आफ्नो भाषामा Microsoft शैक्षिक सामग्री अन्वेषण गर्नुहोस्
- [LangChain4j-शुरुआतीहरूका लागि](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD सुरुआतीहरूको लागि](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI सुरुआतीहरूको लागि](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) सुरुआतीहरूको लागि](https://github.com/microsoft/mcp-for-beginners)
- [AI एजेन्टहरू सुरुआतीहरूको लागि](https://github.com/microsoft/ai-agents-for-beginners)
- [.NET प्रयोग गरेर Generative AI सुरुआतीहरूको लागि](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI सुरुआतीहरूको लागि](https://github.com/microsoft/generative-ai-for-beginners)
- [Java प्रयोग गरेर Generative AI सुरुआतीहरूको लागि](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML सुरुआतीहरूको लागि](https://aka.ms/ml-beginners)
- [Data Science सुरुआतीहरूको लागि](https://aka.ms/datascience-beginners)
- [AI सुरुआतीहरूको लागि](https://aka.ms/ai-beginners)
- [Cybersecurity सुरुआतीहरूको लागि](https://github.com/microsoft/Security-101)
- [Web Dev सुरुआतीहरूको लागि](https://aka.ms/webdev-beginners)
- [IoT सुरुआतीहरूको लागि](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## भिडियो प्रस्तुतीकरणहरू

👉 तलको तस्वीरमा क्लिक गरेर YouTube मा हेर्नुहोस्।

- **Open at Microsoft**: Co-op Translator कसरी प्रयोग गर्ने बारे संक्षेपमा १८ मिनेटको परिचय र छिटो मार्गदर्शन।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

यो परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्छ। Azure Co-op Translator मा योगदान गर्न इच्छुक हुनुहुन्छ? कृपया Co-op Translator लाई थप पहुँचयोग्य बनाउन तपाईंले कसरी मद्दत गर्न सक्नुहुने बारे दिशानिर्देशहरूको लागि हाम्रो [CONTRIBUTING.md](../../CONTRIBUTING.md) हेर्नुहोस्।

## योगदानकर्ताहरू

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचारसंहिता

यो परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ। अधिक जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा थप प्रश्न वा टिप्पणीहरूका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## जिम्मेवार AI

Microsoft ले हाम्रा ग्राहकहरूलाई हाम्रा AI उत्पादनहरू जिम्मेवार तरिकाले प्रयोग गर्न मद्दत गर्न, हाम्रा सिकाइहरू साझा गर्न, र Transparency Notes तथा Impact Assessments जस्ता उपकरणहरू मार्फत विश्वासमा आधारित साझेदारीहरू बनाउने प्रतिबद्धता लिएको छ। यी मध्ये धेरै स्रोतहरू [https://aka.ms/RAI](https://aka.ms/RAI) मा फेला पार्न सकिन्छ।  
Microsoft को जिम्मेवार AI दृष्टिकोण हाम्रो AI सिद्धान्तहरू—न्याय, भरपर्दो र सुरक्षा, गोपनियत्व र सुरक्षा, समावेशिता, पारदर्शिता, र जवाफदेहिता—मा आधारित छ।

यो नमुनामा प्रयोग गरिएका जस्ता ठूलो-स्तरका प्राकृतिक भाषा, इमेज, र स्पीच मोडेलहरूले कहिलेकाहीं असमान, अविश्वसनीय, वा आपत्तिजनक तरिकाले व्यवहार गर्न सक्छन् जसले हानि पुर्‍याउन सक्छ। जोखिम र सीमाहरूबारे जानकारीका लागि कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) सल्लाह गर्नुहोस्।

यी जोखिमहरू कम गर्न सुझाव गरिएको तरिका भनेको तपाईंको आर्किटेक्चरमा यस्तो सुरक्षा प्रणाली समावेश गर्नु हो जसले हानिकारक व्यवहार पत्ता लगाउन र रोकिन सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ले स्वतन्त्र सुरक्षा तह प्रदान गर्छ, जसले एप्लिकेशन र सेवाहरूमा प्रयोगकर्ताद्वारा सिर्जित र AI-द्वारा सिर्जित हानिकारक सामग्री पत्ता लगाउन सक्षम छ। Azure AI Content Safety मा पाठ र छवि API हरू समावेश छन् जसले तपाईंलाई हानिकारक सामग्री पत्ता लगाउन अनुमति दिन्छ। हामीसँग एक अन्तरक्रियात्मक Content Safety Studio पनि छ जसले विभिन्न मोड्यालिटीहरूमा हानिकारक सामग्री पत्ता लगाउन नमूना कोड हेर्न, अन्वेषण गर्न र प्रयास गर्न अनुमति दिन्छ। निम्न [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ले तपाईंलाई सेवामा अनुरोधहरू गर्ने तरिका मार्गदर्शन गर्छ।

ध्यानमा राख्नुपर्ने अर्को पक्ष भनेको समग्र अनुप्रयोग प्रदर्शन हो। बहु-मोडालिटी र बहु-मोडेल एप्लिकेसनहरूमा, हामी प्रदर्शनलाई त्यसरी बुझ्छौं कि प्रणाली तपाईं र तपाईंका प्रयोगकर्ताले अपेक्षा गरेको अनुसार काम गरोस्, जसमा हानिकारक नतिजाहरू उत्पन्न नगर्नु पनि समावेश छ। तपाईंको समग्र अनुप्रयोगको प्रदर्शन [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गरेर मूल्याङ्कन गर्नु महत्त्वपूर्ण छ।

तपाईंले आफ्नो विकास वातावरणमा [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरेर AI अनुप्रयोग मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिइएपछि, तपाईंको जनरेटिव AI अनुप्रयोगका उत्पादनहरू built-in मूल्याङ्ककहरू वा तपाईंको रोजाइका कस्टम मूल्याङ्ककहरूले परिमाणात्मक रूपमा मापन गरिन्छ। तपाईंको प्रणाली मूल्याङ्कन गर्न prompt flow SDK बाट सुरु गर्न, तपाईं [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) पालना गर्न सक्नुहुन्छ। एक पटक मूल्याङ्कन रन पूरा गरेपछि, तपाईं परिणामहरू [Azure AI Studio मा दृश्याङ्कन गर्न](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) सक्नुहुन्छ।

## ट्रेडमार्कहरू

यो परियोजनाले परियोजना, उत्पादन, वा सेवाहरूका ट्रेडमार्क वा लोगोहरू समावेश गर्न सक्छ। Microsoft ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) को अधीन हुनेछ र तिनीहरूको पालन गर्नैपर्छ। यस परियोजनाका परिमार्जित संस्करणहरूमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम सिर्जना नगर्नु वा Microsoft प्रायोजन संकेत नगर्नु पर्नेछ। तेस्रो-पक्षका ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग ती तेस्रो-पक्षका नीतिहरूको अधीन हुनेछ।

## मद्दत लिनुहोस्

यदि तपाईं अड्किनुभयो वा AI एपहरू निर्माण गर्ने बारे कुनै प्रश्न छ भने, सहभागी हुनुहोस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि तपाईंलाई उत्पादन सम्बन्धी प्रतिक्रिया वा निर्माण गर्ने क्रममा त्रुटिहरू आइरहेका छन् भने, यहाँ जानुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)