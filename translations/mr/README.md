# Co-op Translator

_आपल्या शैक्षणिक GitHub सामग्रीचे विविध भाषांमध्ये सहजपणे स्वयंचलित अनुवाद आणि देखभाल करा जसे आपल्या प्रकल्पात बदल होत असतात._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python पॅकेज](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![परवाना: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![डाउनलोड्स](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![डाउनलोड्स](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![कंटेनर: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![कोड शैली: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub समस्या](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs स्वागत](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**इथे सुरू करा:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 बहुभाषीय समर्थन

#### [Co-op Translator](https://github.com/Azure/co-op-translator) कडून समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परंपरागत, हाँगकाँग)](../zh-HK/README.md) | [चिनी (परंपरागत, मकाऊ)](../zh-MO/README.md) | [चिनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [इस्टोनियन](../et/README.md) | [फिन्निश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [खमेर](../km/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मल्याळम](../ml/README.md) | [मराठी](./README.md) | [नेपाळी](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (Farsi)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../pt-BR/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [तागालॉग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [तुर्किश](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिकरित्या क्लोन करायचे का?**
>
> हा रेपॉझिटरी 50+ भाषांतील अनुवाद समाविष्ट करतो ज्यामुळे डाउनलोड आकार मोठा होतो. अनुवादांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> यामुळे आपल्याला कोर्स पूर्ण करण्यासाठी आवश्यक असलेले सर्व घटक जलद डाउनलोडसह मिळतात.

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub स्टार्स](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![GitHub Codespaces मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** आपल्याला आपली शैक्षणिक GitHub सामग्री अनेक भाषांमध्ये स्थानिकीकरण करण्यात मदत करते, तेही सहजपणे.
जेव्हा आपण आपल्या Markdown फाइल्स, प्रतिमा किंवा नोटबुक अद्यतनित करता, तेव्हांना अनुवाद आपोआप समक्रमित राहतात, ज्यामुळे आपल्या सामग्रीचे अचूकपणा आणि नवीनतेचा ध्यास जागतिक विद्यार्थींसाठी राखला जातो.

CLI मधून रेपॉझिटरी अनुवादासाठी, Python API मधून ऑटोमेशनसाठी, किंवा एजंट व संपादक वर्कफ्लो साठी MCP सर्व्हरद्वारे वापरा.

अनुवादित सामग्री कशी आयोजित केलेली आहे याचे उदाहरण:

![उदाहरण](../../imgs/translation-ex.png)

## Co-op Translator का?

एका फाइलचा अनुवाद करणे सोपे आहे. एक संपूर्ण दस्तऐवज रेपॉझिटरी
अनुवादित, दुव्यांसह आणि अद्ययावत ठेवणे हे आव्हानात्मक आहे.

| समस्या | Co-op Translator कसे मदत करते |
| --- | --- |
| Long docs are not one prompt | मोठ्या Markdown फाइल्सना छोटे भागांमध्ये विभाजित केले जाते, त्यामुळे एक मोठा README एका नाजूक मॉडेल प्रतिसादावर अवलंबून राहत नाही. जर एखादा भाग अयशस्वी झाला, तर Co-op Translator फक्त अयशस्वी भाग पुन्हा प्रयत्न करू किंवा पुन्हा-चंक करू शकतो. |
| Incomplete translations should not be marked current | एक अर्धवट अनुवाद कधीही अद्ययावत म्हणून ठप्प केला जाऊ नये. Co-op Translator जतन करण्यापूर्वी अनुवादाची अखंडता तपासतो आणि संरचनात्मकदृष्ट्या अपूर्ण विद्यमान अनुवाद शोधू शकतो. |
| Links should match the translated repo structure | मॅन्युअल अनुवाद अनेकदा सापेक्ष दुवे मूळ झाडाकडे परत निर्देश करतात. Co-op Translator Markdown, नोटबुक, प्रतिमा आणि README दुव्यांना `translations/<lang>/...` संरचनेशी जुळवून पुन्हा लिहितो. |
| Translation should work across an entire repo | Co-op Translator README फाइल्स, docs, नोटबुक आणि प्रतिमा मजकूर या सर्वांना एका रेपॉझिटरी वर्कफ्लोचा भाग म्हणून हाताळतो, फाइल्स एक-एक करून अनुवाद करण्याऐवजी. |
| Maintaining translations matters more than creating them once | स्रोत हॅश आणि अनुवाद मेटाडेटा Co-op Translator ला जुन्या फाइल्स शोधण्यास, न बदललेल्या फाइल्स वगळण्यास, आणि स्रोत रेपॉझिटरी बदलत असताना अनुवादित सामग्री समक्रमित ठेवण्यास मदत करतात. |

## अनुवाद स्थिती कशी व्यवस्थापित केली जाते

Co-op Translator अनुवादित सामग्रीचे व्यवस्थापन "आवृत्तीबद्ध सॉफ्टवेअर आर्टिफॅक्ट" म्हणून करते,  
स्थिर फाइल्स म्हणून नाही.

हे टूल भाषा-स्कोप केलेल्या मेटाडेटाचा वापर करून Markdown, प्रतिमा आणि नोटबुक्सच्या अनुवादित स्थितीचा मागोवा ठेवते.

या डिझाइनमुळे Co-op Translator ला सक्षम होते:

- जुन्या अनुवादांची अचूक ओळख पटवणे
- Markdown, प्रतिमा, आणि नोटबुक्स यांना सुसंगतपणे हाताळणे
- मोठ्या, वेगवान बदलांमुळे होणाऱ्या मल्टि-लँग रेपॉझिटरीजमध्ये सुरक्षितपणे स्केल करणे

अनुवादांना व्यवस्थापित आर्टिफॅक्ट म्हणून मॉडेल करून,
अनुवाद वर्कफ्लो आधुनिक सॉफ्टवेअर निर्भरता आणि आर्टिफॅक्ट व्यवस्थापन पद्धतींशी नैसर्गिकरित्या संरेखित होतात.

→ [अनुवाद स्थिती कशी व्यवस्थापित केली जाते](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### संबंधित सखोल लेख

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## सुरू करा

Co-op Translator CLI, Python API, किंवा MCP सर्व्हरद्वारे वापरता येऊ शकतो. स्थानिक अनुवाद, ऑटोमेशन, CI आणि एजंट/एडिटर इंटिग्रेशनमधून कोणता वर्कफ्लो निवडायचा हे ठरवताना वर्कफ्लो मार्गदर्शिका वापरा.

- [आपला वर्कफ्लो निवडा](../../docs/workflows.md)
- [क्रेडेन्शियल कॉन्फिगर करा](../../docs/configuration.md)
- [CLI कडून अनुवाद करा](../../docs/cli.md)
- [Python API सह ऑटोमेट करा](../../docs/api.md)
- [MCP सर्व्हरशी कनेक्ट करा](../../docs/mcp.md)
- [GitHub Actions मध्ये चालवा](../../docs/github-actions.md)

कॉन्फिगरेशननंतरचा किमान CLI उदाहरण:

```bash
python -m venv .venv
# विंडोज
.venv\Scripts\activate
# मॅकओएस/लिनक्स
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

मोठ्या रेपॉझिटरीजवर प्रथम चालवताना, अनुवादित फाइल्स लिहिण्यापूर्वी `--dry-run` वापरा. कंटेंट प्रकार फ्लॅग, लॉग, पुनरावलोकन, आणि लिंक मायग्रेशनसाठी पाहा [CLI Reference](../../docs/cli.md).

Bash/Zsh सह कंटेनर जलद चालवा:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell सह कंटेनर जलद चालवा:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## वैशिष्ट्ये

- Markdown, नोटबुक, आणि प्रतिमांसाठी स्वयंचलित अनुवाद
- स्रोत बदलांसह अनुवाद समक्रमित ठेवतो
- स्थानिकरित्या (CLI) किंवा CI मध्ये (GitHub Actions) काम करते
- MCP मधून Markdown, नोटबुक, प्रतिमा, पुनरावलोकन, आणि प्रोजेक्ट अनुवाद साधने उपलब्ध करते
- प्रदात्या-समर्थित अनुवादासाठी Azure OpenAI किंवा OpenAI चा वापर करते
- MCP एजंटना Co-op Translator LLM क्रेडेन्शियलशिवाय Markdown आणि नोटबुक चंक्स अनुवादित करण्याची परवानगी देते
- प्रतिमा मजकूर बाहेर काढण्यासाठी आणि अनुवादासाठी Azure AI Vision चा वापर करते
- अनुवाद संरचना आणि ताजेपणा ठराविक तपासण्‍यांसह पुनरावलोकन करते
- Markdown स्वरूपन आणि संरचना जपते

## दस्तऐवज

- [Documentation site](https://azure.github.io/co-op-translator/)
- [आपला वर्कफ्लो निवडा](../../docs/workflows.md)
- [कॉन्फिगरेशन](../../docs/configuration.md)
- [Azure AI सेटअप](../../docs/azure-ai-setup.md)
- [CLI संदर्भ](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP सर्व्हर](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README भाषांचे साचे](../../docs/readme-languages-template.md)
- [समर्थित भाषा](../../docs/supported-languages.md)
- [योगदान कसे करावे](../../CONTRIBUTING.md)
- [समस्यांचे निराकरण](../../docs/troubleshooting.md)

### Microsoft-विशिष्ट मार्गदर्शक
> [!NOTE]
> For maintainers of the Microsoft “For Beginners” repositories only.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## आम्हाला समर्थन द्या आणि जागतिक शिक्षणाला प्रोत्साहन द्या

शैक्षणिक सामग्री जागतिक पातळीवर कशी सामायिक केली जाते यामध्ये आमच्यासोबत क्रांती घडवा! [Co-op Translator](https://github.com/azure/co-op-translator) ला GitHub वर एक ★ द्या आणि शिक्षण व तंत्रज्ञानातील भाषा अडथळे तोडण्याच्या आमच्या ध्येयाला समर्थन करा. आपली आवड आणि योगदान मोठा परिणाम करतात! कोड योगदान आणि वैशिष्ट्य सूचना नेहमी स्वागतार्ह आहेत.

### आपल्या भाषेत Microsoft शैक्षणिक सामग्री एक्सप्लोर करा
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

## व्हिडिओ सादरीकरणे

👉 YouTube वर पाहण्यासाठी खालील प्रतिमेवर क्लिक करा.

- **Open at Microsoft**: Co-op Translator कसा वापरायचा याबद्दलचे संक्षिप्त 18-मिनिटांचे परिचय आणि जलद मार्गदर्शक.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

हा प्रकल्प योगदान आणि सूचना स्वागत करतो. Azure Co-op Translator मध्ये योगदान देण्यात रस आहे का? Co-op Translator अधिक प्रवेशयोग्य करण्यासाठी आपण कशी मदत करू शकता याबद्दल मार्गदर्शकासाठी कृपया आमचे [CONTRIBUTING.md](../../CONTRIBUTING.md) पहा.

## योगदानकर्ते

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## वर्तनसंहिता

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारली आहे.
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा
इतर प्रश्न किंवा टिप्पण्यांसाठी [opencode@microsoft.com](mailto:opencode@microsoft.com) यांच्याशी संपर्क साधा.

## जबाबदार AI

Microsoft आपल्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यात, आमचे अनुभव सामायिक करण्यात आणि Transparency Notes आणि Impact Assessments सारख्या साधनांद्वारे विश्वास-आधारित भागीदार्या निर्माण करण्यात वचनबद्ध आहे. या संसाधनांपैकी बरेच [https://aka.ms/RAI](https://aka.ms/RAI) येथे आढळतील.
Microsoft चे जबाबदार AI साठीचे मार्गदर्शन न्याय्यते, विश्वसनीयता आणि सुरक्षा, गोपनीयता आणि सुरक्षितता, समावेशिता, पारदर्शकता आणि जबाबदारी या AI तत्त्वांवर आधारित आहे.

या नमुना मध्ये वापरल्या जाणाऱ्या मोठ्या-स्तरावरील नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल्स कधीकधी अन्यायकारक, अविश्वसनीय किंवा अपमानजनक वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. जोखीम आणि मर्यादांविषयी माहिती मिळवण्यासाठी कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या जोखमींचा मुकाबला करण्यासाठी शिफारसीत दृष्टिकोन म्हणजे आपल्या आर्किटेक्चरमध्ये असा सुरक्षा प्रणाली समाविष्ट करणे जी हानिकारक वर्तन शोधू आणि प्रतिबंधित करू शकेल. वापरकर्त्याद्वारे निर्मित आणि AI-द्वारे निर्मित हानिकारक सामग्री शोधण्यासाठी स्वतंत्र संरक्षणाची सतत थर म्हणून [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) उपलब्ध आहे. Azure AI Content Safety मध्ये असे टेक्स्ट आणि प्रतिमा APIs आहेत जे हानिकारक सामग्रीचा शोध घेऊ शकतात. आम्हाकडे एक परस्परसंवादी Content Safety Studio देखील आहे जे विविध मोडॅलिटीजमध्ये हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्याची, शोधण्याची आणि प्रयत्न करण्याची परवानगी देते. खालील [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपल्याला सेवेला विनंत्या कशा कराव्यात हे मार्गदर्शन करेल.

धरून घ्या की आणखी एक विचार करण्यासारखा भाग म्हणजे संपूर्ण अनुप्रयोगाची कार्यक्षमता आहे. बहु-मॉडॅल आणि बहु-मॉडेल अनुप्रयोगांसह, कार्यक्षमता म्हणजे प्रणाली आपण आणि आपल्या वापरकर्त्यांनी जसे अपेक्षित केले आहे तसे कार्य करणे, ज्यात हानिकारक आउटपुट तयार न करणे ही गोष्टही समाविष्ट आहे. आपल्या संपूर्ण अनुप्रयोगाची कार्यक्षमता [generation quality आणि risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून मोजणे महत्वाचे आहे.

आपण आपल्या विकास वातावरणात [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) वापरून आपल्या AI अनुप्रयोगाचे मूल्यांकन करू शकता. टेस्ट डेटासेट किंवा लक्ष्य दिल्यास, आपले जनरेटिव्ह AI अनुप्रयोग निर्मिती अंतर्गत मूल्यांकनकर्ते किंवा आपल्या पसंतीचे कस्टम मूल्यांकनकर्ते वापरून मात्रात्मकदृष्ट्या मापन करण्यात येतात. आपल्या प्रणालीचे मुल्यमापन करण्यासाठी prompt flow sdk वापरून सुरू करण्यासाठी आपण [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरू शकता. एकदा आपण मूल्यांकन रन चालवताच, आपण [Azure AI Studio मध्ये निकालांचे दृश्य화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) करू शकता.

## ट्रेडमार्क

या प्रकल्पात प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft ट्रेडमार्क किंवा लोगोच्या अधिकृत वापरासाठी [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) चे पालन करणे आवश्यक आहे.
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगो वापरल्यास गोंधळ निर्माण होऊ नये किंवा Microsoft च्या अधिकृत समर्थनाचा अर्थ लागू नये.
तृतीय-पक्ष ट्रेडमार्क किंवा लोगोच्या कोणत्याही वापरासाठी त्या तृतीय-पक्षाच्या धोरणांचे पालन करणे आवश्यक आहे.

## मदत मिळवा

जर आपण अडकले असाल किंवा AI अनुप्रयोग तयार करण्याबाबत काही प्रश्न असतील तर सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

उत्पादनाबद्दल अभिप्राय किंवा बांधणीदरम्यान त्रुटी असल्यास भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)