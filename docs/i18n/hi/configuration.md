# कॉन्फ़िगरेशन

Co-op Translator को एक भाषा मॉडल प्रदाता की आवश्यकता होती है। छवि अनुवाद के लिए अतिरिक्त रूप से Azure AI Vision की आवश्यकता होती है।

कॉन्फ़िगरेशन पर्यावरण चर से पढ़ा जाता है। स्थानीय प्रोजेक्ट्स के लिए, इन्हें प्रोजेक्ट रूट में `.env` फ़ाइल में रखें।

Azure संसाधन सेटअप के लिए, देखें [Azure AI सेटअप](azure-ai-setup.md).

## स्थानीय रनटाइम सेटअप

CLI को स्थानीय रूप से चलाने से पहले वर्चुअल एनवायरनमेंट का उपयोग करें। Co-op Translator Python 3.11 से 3.14 तक का समर्थन करता है।

सामान्य CLI उपयोग के लिए, वर्चुअल एनवायरनमेंट के अंदर प्रकाशित पैकेज इंस्टॉल करें:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### रिपॉज़िटरी विकास

रिपॉज़िटरी विकास के लिए, इसके बजाय प्रोजेक्ट रूट से निर्भरताएँ इंस्टॉल करें:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध होने के बाद, `.env` में एक भाषा मॉडल प्रदाता को कॉन्फ़िगर करें।

## प्रदाता चयन

यह टूल प्रदाताओं का निम्नलिखित क्रम में स्वतः पहचान करता है:

1. Azure OpenAI
2. OpenAI
3. Anthropic

अनुवाद के लिए प्रदाता प्रमाण-पत्रों की आवश्यकता होती है, उन प्रीव्यूज़ को छोड़कर जैसे `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, और `run_review` निर्धारित रखरखाव संचालन हैं और इन्हें प्रदाता प्रमाण-पत्रों की आवश्यकता नहीं होती।

## मॉडल क्लाइंट बैकएंड

Co-op Translator 0.22.0 से शुरू होकर, Azure OpenAI, OpenAI, और Anthropic डिफ़ॉल्ट रूप से Microsoft Agent Framework का उपयोग करते हैं। सामान्य उपयोग के लिए किसी बैकएंड सेटिंग की आवश्यकता नहीं है।

संगतता के लिए Semantic Kernel अस्थायी रूप से उपलब्ध रहता है। इसे स्पष्ट रूप से चुनने के लिए, सेट करें:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel का उपयोग करने पर डिप्रीकेशन चेतावनी जारी होती है। पैकेज में योजना है कि Semantic Kernel को 0.23.0 में वैकल्पिक निर्भरता के रूप में स्थानांतरित किया जाए और 0.24.0 में इस एकीकरण को हटाया जाए, बशर्ते संगतता परिणामों और उपयोगकर्ता फीडबैक के आधार पर। Anthropic के लिए `agent-framework` आवश्यक है; Anthropic के साथ स्पष्ट रूप से `semantic-kernel` चुनने पर कॉन्फ़िगरेशन त्रुटि होती है। अमान्य मान प्रदाता-समर्थित ट्रांसलेटर इनिशियलाइज़ेशन के दौरान असफल होते हैं बजाय कि शांतिपूर्वक फॉल बैक करने के। रोलआउट का पालन करें और बाधाओं की रिपोर्ट करें [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

जब आपका मॉडल Azure AI Foundry या Azure OpenAI Service में तैनात हो तो Azure OpenAI का उपयोग करें।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

कनेक्टिविटी जांच अनुवाद शुरू होने से पहले endpoint, API key, API version, और deployment name का उपयोग करती है।

## OpenAI

जब आप सीधे OpenAI API को कॉल कर रहे हों तो OpenAI का उपयोग करें।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` आवश्यक है क्योंकि ट्रांसलेटर को API कॉल्स के लिए एक स्पष्ट चैट मॉडल की आवश्यकता होती है।

`OPENAI_ORG_ID` और `OPENAI_BASE_URL` को डिफ़ॉल्ट सेटअप के लिए अनसेट ही रखें। संगठन ID तभी जोड़ें जब आपके खाते को इसकी आवश्यकता हो, या base URL तभी जब कस्टम endpoint उपयोग कर रहे हों। वैकल्पिक सेटिंग्स के लिए प्लेसहोल्डर मान कॉपी न करें।

## Anthropic Claude

जब आप सीधे Claude API को कॉल कर रहे हों तो Anthropic का उपयोग करें। एक [Anthropic API कुंजी](https://platform.claude.com/docs/en/get-started) बनाएं और एक समर्थित [Claude मॉडल ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) चुनें।

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` और `ANTHROPIC_MODEL` आवश्यक हैं। आपको `CO_OP_TRANSLATOR_MODEL_CLIENT` सेट करने की आवश्यकता नहीं है; Agent Framework डिफ़ॉल्ट बैकएंड है।

`ANTHROPIC_BASE_URL` को Anthropic API के लिए अनसेट ही रखें। केवल कस्टम endpoint उपयोग करते समय ही इसे सेट करें।

`ANTHROPIC_MAX_TOKENS` का डिफ़ॉल्ट मान `8192` है, जो Meitei Mayek जैसे टोकन-घने स्क्रिप्ट्स के लिए स्थान छोड़ता है। यदि आपका मॉडल या Anthropic-संगत endpoint आउटपुट को इससे कम सीमित करता है तो इसे घटाएँ।

## Azure AI Vision

छवि अनुवाद के लिए Azure AI Vision आवश्यक है ताकि टूल छवियों से टेक्स्ट निकाल सके और फिर कॉन्फ़िगर किया गया भाषा मॉडल उसे अनुवाद कर सके। Anthropic भी निकाले गए टेक्स्ट का अनुवाद Azure OpenAI या OpenAI की तरह कर सकता है।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

यदि छवि अनुवाद `-img`, `images=True`, या बिना content-type फ़िल्टर के चयनित है, तो टूल अनुवाद शुरू होने से पहले Vision कॉन्फ़िगरेशन को मान्य करता है।

## एकाधिक क्रेडेंशियल सेट

कॉन्फ़िगरेशन लेयर वेरिएबल्स के अंत में समान सूचकांक जोड़कर एकाधिक क्रेडेंशियल सेट का समर्थन करता है:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

प्रत्येक सेट पूर्ण होना चाहिए। स्वास्थ्य जांच अनुवाद आगे बढ़ने से पहले एक काम करने वाला सेट चुनती है।

OpenAI और Anthropic वही suffix कन्वेंशन समर्थन करते हैं। क्रेडेंशियल सेट में हर वेरिएबल को उसी suffix पर रखें, जिसमें वैकल्पिक मान जैसे `OPENAI_BASE_URL_1` या `ANTHROPIC_BASE_URL_1` शामिल हैं।

## कमांड आवश्यकताएँ

| कमांड या API | LLM आवश्यक | Vision आवश्यक | नोट्स |
| --- | --- | --- | --- |
| `translate -md` | हाँ | नहीं | केवल Markdown का अनुवाद करता है। |
| `translate -nb` | हाँ | नहीं | केवल नोटबुक्स का अनुवाद करता है। |
| `translate -img` | हाँ | हाँ | केवल छवियों का अनुवाद करता है। |
| `translate` with no type flags | हाँ | हाँ | डिफ़ॉल्ट मोड में Markdown, नोटबुक्स, और छवियाँ शामिल हैं। |
| `evaluate` | हाँ | नहीं | `--fast` चुना गया न होने पर LLM मूल्यांकन का उपयोग करता है। |
| `migrate-links` | नहीं | नहीं | प्रदाता कॉल के बिना स्थानीय लिंक माइग्रेशन करता है। |
| `co-op-review` | नहीं | नहीं | निर्धारित अनुवाद संरचना, ताज़गी, Markdown, नोटबुक, और स्थानीय लिंक जांच चलाता है। |
| `run_translation(markdown=True)` | हाँ | नहीं | प्रोग्रामैटिक Markdown अनुवाद। |
| `run_translation(images=True)` | हाँ | हाँ | प्रोग्रामैटिक छवि अनुवाद। |
| `run_review(...)` | नहीं | नहीं | प्रोग्रामैटिक निर्धारित समीक्षा। |

## आउटपुट डायरेक्टरीज़

डिफ़ॉल्ट टेक्स्ट अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफ़ॉल्ट अनुवादित छवि आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API इन निर्देशिकाओं को `translations_dir` और `image_dir` के साथ ओवरराइड कर सकता है।