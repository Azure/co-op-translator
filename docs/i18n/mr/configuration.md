# कॉन्फिगरेशन

Co-op Translator ला एका भाषा मॉडेल प्रदात्याची आवश्यकता असते. चित्र अनुवादासाठी अतिरिक्तपणे Azure AI Vision आवश्यक आहे.

कॉन्फिगरेशन पर्यावरण चलांमधून वाचले जाते. स्थानिक प्रकल्पांसाठी, प्रकल्पाच्या रूटमध्ये `.env` फाईलमध्ये ठेवा.

Azure संसाधन सेटअपसाठी, पहा [Azure AI सेटअप](azure-ai-setup.md).

## स्थानिक रनटाइम सेटअप

CLI स्थानिकपणे चालवण्यापूर्वी आभासी वातावरण वापरा. Co-op Translator Python 3.11 ते 3.14 पर्यंत समर्थित आहे.

सामान्य CLI वापरासाठी, प्रकाशित पॅकेज आभासी वातावरणाच्या आत इन्स्टॉल करा:

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

### रिपॉझिटरी विकास

रिपॉझिटरी विकासासाठी, प्रकल्पाच्या रूटमधून अवलंबने इन्स्टॉल करा:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध झाल्यानंतर, `.env` मध्ये एक भाषा मॉडेल प्रदाता कॉन्फिगर करा.

## प्रदाता निवड

हे टूल खालील क्रमाने प्रदाते स्वयंचलितपणे ओळखते:

1. Azure OpenAI
2. OpenAI
3. Anthropic

अनुवादासाठी प्रदाता credentials आवश्यक असतात, परंतु `translate -l "ko" -md --dry-run"` सारख्या पूर्वदृश्यांसाठी हे लागू होत नाही. `migrate-links`, `co-op-review`, आणि `run_review` हे निर्धारपूर्वक देखभाल ऑपरेशन्स आहेत आणि त्यांना प्रदाता credentials ची आवश्यकता नसते.

## मॉडेल क्लायंट बॅकएंड

Co-op Translator 0.22.0 पासून, Azure OpenAI, OpenAI, आणि Anthropic डिफॉल्टने Microsoft Agent Framework वापरतात. सामान्य वापरासाठी कोणतीही बॅकएंड सेटिंग आवश्यक नाही.

सुसंगततेसाठी Semantic Kernel तात्पुरते उपलब्ध राहते. ते स्पष्टपणे निवडण्यासाठी, सेट करा:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel वापरल्यास deprecation इशारा देण्यात येतो. पॅकेजमध्ये Semantic Kernel ला 0.23.0 मध्ये ऐच्छिक अवलंबनात हलवण्याचे आणि 0.24.0 मध्ये एकत्रीकरण काढून टाकण्याचे नियोजन आहे, हे सुसंगतता निकाल आणि वापरकर्त्यांच्या अभिप्रायावर अवलंबून आहे. Anthropic ला `agent-framework` ची गरज आहे; Anthropic सह स्पष्टपणे `semantic-kernel` निवडल्यास कॉन्फिगरेशन त्रुटी येते. अवैध मूल्ये गुप्तपणे फॉलबॅक न करता प्रदाता-समर्थित ट्रान्सलेटरच्या प्रारंभिकरणादरम्यान अयशस्वी होतात. रोलआउटचे अनुसरण करा आणि अडथळे [GitHub इशュー #543](https://github.com/Azure/co-op-translator/issues/543) मध्ये नोंदवा.

## Azure OpenAI

आपले मॉडेल Azure AI Foundry किंवा Azure OpenAI Service मध्ये डिप्लॉय केले असल्यास Azure OpenAI वापरा.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

कनेक्टिव्हिटी तपासणी अनुवाद सुरू होण्यापूर्वी endpoint, API key, API version आणि deployment name वापरते.

## OpenAI

OpenAI API ला थेट कॉल करताना OpenAI वापरा.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` आवश्यक आहे कारण ट्रांसलेटरला API कॉलसाठी स्पष्ट chat मॉडेलची आवश्यकता असते.

डिफॉल्ट सेटअपने `OPENAI_ORG_ID` आणि `OPENAI_BASE_URL` अनसेट ठेवा. फक्त आपल्या खात्याला आवश्यकता असल्यास organization ID जोडा, किंवा कस्टम endpoint वापरत असलात तरच base URL जोडा. ऐच्छिक सेटिंग्ससाठी placeholder मूल्ये कॉपी करू नका.

## Anthropic Claude

Claude API ला थेट कॉल करताना Anthropic वापरा. एक [Anthropic API की](https://platform.claude.com/docs/en/get-started) तयार करा आणि एक समर्थित [Claude मॉडेल ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) निवडा.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` आणि `ANTHROPIC_MODEL` आवश्यक आहेत. `CO_OP_TRANSLATOR_MODEL_CLIENT` सेट करण्याची आवश्यकता नाही; Agent Framework डिफॉल्ट बॅकएंड आहे.

Anthropic API साठी `ANTHROPIC_BASE_URL` अनसेट ठेवा. फक्त कस्टम endpoint वापरत असल्यासच ते सेट करा.

`ANTHROPIC_MAX_TOKENS` चे डिफॉल्ट `8192` आहे, जे Meitei Mayek सारख्या टोकन-घन स्क्रिप्टसाठी जागा ठेवते. जर आपल्या मॉडेलने किंवा Anthropic-संगत endpoint ने आउटपुट यापेक्षा कमी मर्यादा घातली असेल तर ते कमी करा.

## Azure AI Vision

चित्र अनुवादासाठी Azure AI Vision आवश्यक आहे जेणेकरून टूल कॉन्फिगर केलेल्या भाषा मॉडेलने अनुवाद करण्यापूर्वी प्रतिमांमधून मजकूर काढू शकेल. Anthropic देखील Azure OpenAI किंवा OpenAI प्रमाणे काढलेल्या मजकुराचा अनुवाद करू शकते.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

जर `-img`, `images=True` किंवा कोणताही content-type फिल्टर न वापरता image translation निवडले गेले असेल, तर टूल अनुवाद सुरू होण्यापूर्वी Vision कॉन्फिगरेशनची पडताळणी करते.

## अनेक क्रेडेन्शियल संच

कॉन्फिगरेशन स्तर समान अनुक्रमांकाने चलांना suffix देऊन अनेक क्रेडेन्शियल संचांचे समर्थन करते:

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

प्रत्येक संच पूर्ण असावा. अनुवाद सुरू होण्यापूर्वी हेल्थ चेक एक कार्यरत संच निवडते.

OpenAI आणि Anthropic एकाच suffix पद्धतीला समर्थन देतात. एका क्रेडेन्शियल संचातील प्रत्येक चल एकाच suffix वर ठेवा, ज्यात `OPENAI_BASE_URL_1` किंवा `ANTHROPIC_BASE_URL_1` सारखी ऐच्छिक मूल्येही समाविष्ट आहेत.

## कमांड आवश्यकता

| Command किंवा API | LLM आवश्यक | Vision आवश्यक | नोट्स |
| --- | --- | --- | --- |
| `translate -md` | होय | नाही | फक्त Markdown अनुवादित करते. |
| `translate -nb` | होय | नाही | फक्त नोटबुक्स अनुवादित करते. |
| `translate -img` | होय | होय | फक्त प्रतिमा अनुवादित करते. |
| `translate` with no type flags | होय | होय | डीफॉल्ट मोडमध्ये Markdown, नोटबुक्स, आणि प्रतिमा समाविष्ट असतात. |
| `evaluate` | होय | नाही | `--fast` निवडले नसेल तर LLM मूल्यांकन वापरते. |
| `migrate-links` | नाही | नाही | प्रदाता कॉलशिवाय स्थानिक लिंक माइग्रेशन करते. |
| `co-op-review` | नाही | नाही | निर्धारपूर्वक अनुवाद रचना, ताजेपणा, Markdown, नोटबुक, आणि स्थानिक लिंक तपासणी चालवते. |
| `run_translation(markdown=True)` | होय | नाही | प्रोग्रामॅटिक Markdown अनुवाद. |
| `run_translation(images=True)` | होय | होय | प्रोग्रामॅटिक प्रतिमा अनुवाद. |
| `run_review(...)` | नाही | नाही | प्रोग्रामॅटिक निर्धारपूर्वक पुनरावलोकन. |

## आउटपुट निर्देशिका

डिफॉल्ट मजकूर अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफॉल्ट अनुवादित प्रतिमा आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API हे निर्देशिका `translations_dir` आणि `image_dir` ने ओव्हरराईड करू शकते.