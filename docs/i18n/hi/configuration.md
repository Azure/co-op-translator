# कॉन्फ़िगरेशन

Co-op Translator को एक भाषा मॉडल प्रदाता की आवश्यकता होती है। छवि अनुवाद के लिए अतिरिक्त रूप से Azure AI Vision की आवश्यकता होती है।

कॉन्फ़िगरेशन वातावरण चर से पढ़ी जाती है। लोकल प्रोजेक्ट्स के लिए, उन्हें प्रोजेक्ट रूट पर `.env` फ़ाइल में रखें।

Azure संसाधन सेटअप के लिए, देखें [Azure AI Setup](azure-ai-setup.md).

## लोकल रनटाइम सेटअप

CLI को स्थानीय रूप से चलाने से पहले एक वर्चुअल एनवायरनमेंट का उपयोग करें। Co-op Translator Python 3.10 से 3.12 तक का समर्थन करता है।

सामान्य CLI उपयोग के लिए, वर्चुअल एनवायरनमेंट के अंदर प्रकाशित पैकेज इंस्टॉल करें:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

रिपॉज़िटरी डेवलपमेंट के लिए, इसके बजाय प्रोजेक्ट रूट से डिपेंडेंसीज़ इंस्टॉल करें:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध होने के बाद, `.env` में एक भाषा मॉडल प्रदाता कॉन्फ़िगर करें।

## प्रदाता चयन

टूल इन प्रदाताओं का ऑटो-डिटेक्शन इस क्रम में करता है:

1. Azure OpenAI
2. OpenAI

यदि किसी भी प्रदाता को कॉन्फ़िगर नहीं किया गया है, तो `translate`, `evaluate`, `migrate-links`, और `run_translation` कॉन्फ़िगरेशन जाँचों के दौरान विफल हो जाते हैं। `co-op-review` और `run_review` निर्धारक रखरखाव जाँचें हैं और उन्हें प्रदाता क्रेडेंशियल्स की आवश्यकता नहीं होती है।

## Azure OpenAI

जब आपका मॉडल Azure AI Foundry या Azure OpenAI Service में डिप्लॉय किया गया हो तो Azure OpenAI का उपयोग करें।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

कननेक्टिविटी चेक ट्रांसलेशन शुरू होने से पहले endpoint, API key, API version, और deployment name का उपयोग करता है।

## OpenAI

जब आप OpenAI API को सीधे कॉल कर रहे हों तो OpenAI का उपयोग करें।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # वैकल्पिक
OPENAI_BASE_URL="..."        # वैकल्पिक
```

`OPENAI_CHAT_MODEL_ID` आवश्यक है क्योंकि अनुवादक को API कॉल्स के लिए एक स्पष्ट चैट मॉडल की आवश्यकता होती है।

## Azure AI Vision

इमेज अनुवाद के लिए Azure AI Vision आवश्यक है ताकि टूल अनुवाद करने से पहले छवियों से टेक्स्ट निकाल सके।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

यदि इमेज अनुवाद `-img`, `images=True`, या कोई content-type फ़िल्टर न होने के साथ चुना गया है, तो टूल ट्रांसलेशन शुरू होने से पहले Vision कॉन्फ़िगरेशन को मान्य करता है।

## एकाधिक क्रेडेंशियल सेट

कॉन्फ़िगरेशन लेयर एक ही इंडेक्स के साथ वैरिएबल्स को सुफिक्स करके एकाधिक क्रेडेंशियल सेट्स का समर्थन करती है:

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

प्रत्येक सेट पूर्ण होना चाहिए। हेल्थ चेक ट्रांसलेशन आगे बढ़ने से पहले एक कार्यशील सेट का चयन करता है।

## कमांड आवश्यकताएँ

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | हाँ | नहीं | केवल Markdown का अनुवाद करता है। |
| `translate -nb` | हाँ | नहीं | केवल नोटबुक्स का अनुवाद करता है। |
| `translate -img` | हाँ | हाँ | केवल छवियों का अनुवाद करता है। |
| `translate` with no type flags | हाँ | हाँ | डिफ़ॉल्ट मोड में Markdown, नोटबुक्स, और छवियाँ शामिल हैं। |
| `evaluate` | हाँ | नहीं | LLM मूल्यांकन का उपयोग करता है जब तक कि `--fast` नहीं चुना गया हो। |
| `migrate-links` | हाँ | नहीं | लिंक माइग्रेशन करता है, लेकिन अभी भी साझा कॉन्फ़िगरेशन जाँचें चलाता है। |
| `co-op-review` | नहीं | नहीं | निर्धारक ट्रांसलेशन संरचना, ताज़गी, Markdown, नोटबुक, और लोकल लिंक जाँचें चलाता है। |
| `run_translation(markdown=True)` | हाँ | नहीं | प्रोग्रामेटिक Markdown अनुवाद। |
| `run_translation(images=True)` | हाँ | हाँ | प्रोग्रामेटिक इमेज अनुवाद। |
| `run_review(...)` | नहीं | नहीं | प्रोग्रामेटिक निर्धारक समीक्षा। |

## आउटपुट निर्देशिकाएँ

डिफ़ॉल्ट टेक्स्ट अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफ़ॉल्ट अनुवादित इमेज आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API `translations_dir` और `image_dir` के साथ इन निर्देशिकाओं को ओवरराइड कर सकता है।