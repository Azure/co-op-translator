# कॉन्फिगरेशन

Co-op Translator ला एका भाषा मॉडेल प्रदात्याची आवश्यकता आहे. प्रतिमा अनुवादासाठी अतिरिक्तपणे Azure AI Vision आवश्यक आहे.

कॉनफिगरेशन पर्यावरण चलांमधून वाचले जाते. स्थानिक प्रकल्पांसाठी, प्रकल्पाच्या मूळ निर्देशिकेत `.env` फाइलमध्ये ते ठेवा.

For Azure resource setup, see [Azure AI सेटअप](azure-ai-setup.md).

## स्थानिक रनटाइम सेटअप

CLI स्थानिकपणे चालवण्यापूर्वी वर्चुअल एन्व्हायर्नमेंट वापरा. Co-op Translator Python 3.10 ते 3.12 पर्यंत समर्थन करतो.

सामान्य CLI वापरासाठी, प्रकाशित पॅकेज वर्चुअल एन्व्हायर्नमेंटच्या आत इन्स्टॉल करा:

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

रिपॉझिटरी विकसित करण्यासाठी, प्रकल्पाच्या मूळ निर्देशिकेतून अवलंबित्वे इन्स्टॉल करा:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध झाल्यानंतर, `.env` मध्ये एक भाषा मॉडेल प्रदाता कॉन्फिगर करा.

## प्रदाता निवड

टूल खालील क्रमाने प्रदाते ऑटो-डिटेक्ट करते:

1. Azure OpenAI
2. OpenAI

जर कोणताही प्रदाता कॉन्फिगर नसेल, तर `translate`, `evaluate`, `migrate-links`, आणि `run_translation` कॉन्फिगरेशन तपासणी दरम्यान अयशस्वी होतात. `co-op-review` आणि `run_review` निश्चित-किर्यता देखभाल तपासण्या आहेत आणि त्यांना प्रदाता प्रमाणपत्रांची आवश्यकता नाही.

## Azure OpenAI

जेव्हा आपले मॉडेल Azure AI Foundry किंवा Azure OpenAI Service मध्ये डिप्लॉय केलेले असेल तेव्हा Azure OpenAI वापरा.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

कनेक्टिव्हिटी तपासणी अनुवाद सुरू होण्याआधी endpoint, API key, API version, आणि deployment name वापरते.

## OpenAI

OpenAI API ला थेट कॉल करताना OpenAI वापरा.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ऐच्छिक
OPENAI_BASE_URL="..."        # ऐच्छिक
```

`OPENAI_CHAT_MODEL_ID` आवश्यक आहे कारण ट्रान्सलेटरला API कॉलसाठी स्पष्ट chat मॉडेल लागते.

## Azure AI Vision

प्रतिमा अनुवादासाठी Azure AI Vision आवश्यक आहे जेणेकरून टूल प्रतिमांमधून मजकूर एक्सट्रॅक्ट करू शकेल आणि नंतर अनुवाद करू शकेल.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

जर प्रतिमा अनुवाद `-img`, `images=True`, किंवा कोणताही content-type फिल्टर न देता निवडले गेले, तर टूल अनुवाद सुरू होण्यापूर्वी Vision कॉन्फिगरेशनची वैधता (validate) करते.

## अनेक क्रेडेन्शियल सेट्स

कॉन्फिगरेशन लेयर एकाच इंडेक्ससह चल (variables) सुफिक्स करून अनेक क्रेडेन्शियल सेट्सना समर्थन करते:

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

प्रत्येक सेट पूर्ण असणे आवश्यक आहे. हेल्थ चेक अनुवाद सुरू होण्यापूर्वी काम करणारा सेट निवडतो.

## कमांड आवश्यकता

| Command or API | LLM आवश्यक | Vision आवश्यक | नोट्स |
| --- | --- | --- | --- |
| `translate -md` | होय | नाही | फक्त Markdown अनुवाद करते. |
| `translate -nb` | होय | नाही | फक्त नोटबुक अनुवाद करते. |
| `translate -img` | होय | होय | फक्त प्रतिमा अनुवादित करतो. |
| `translate` with no type flags | होय | होय | डिफॉल्ट मोडमध्ये Markdown, नोटबुक, आणि प्रतिमा समाविष्ट असतात. |
| `evaluate` | होय | नाही | `--fast` निवडलं नसेल तर LLM मूल्यमापन वापरतो. |
| `migrate-links` | होय | नाही | लिंक माईग्रेशन करतो, परंतु तरीही सामायिक कॉन्फिगरेशन तपासण्या चालवतो. |
| `co-op-review` | नाही | नाही | निश्चित अनुवाद संरचना, नवीनता, Markdown, नोटबुक, आणि स्थानिक लिंक तपासण्या चलवते. |
| `run_translation(markdown=True)` | होय | नाही | प्रोग्रामॅटिक Markdown अनुवाद. |
| `run_translation(images=True)` | होय | होय | प्रोग्रामॅटिक प्रतिमा अनुवाद. |
| `run_review(...)` | नाही | नाही | प्रोग्रामॅटिक निश्चित समीक्षा. |

## आउटपुट निर्देशिका

डिफॉल्ट मजकूर अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफॉल्ट अनुवादित प्रतिमा आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API हे निर्देशिका `translations_dir` आणि `image_dir` ने ओव्हरराइड करू शकतो.