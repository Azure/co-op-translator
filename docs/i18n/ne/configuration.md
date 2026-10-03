# कन्फिगरेसन

Co-op Translator लाई एउटा भाषा मोडेल प्रदायक चाहिन्छ। तस्बिर अनुवादका लागि थप रूपमा Azure AI Vision आवश्यक हुन्छ।

कन्फिगरेसन वातावरण परिवर्तनशीलहरूबाट पढिन्छ। स्थानीय प्रोजेक्टहरूको लागि, तिनीहरूलाई प्रोजेक्ट रुटमा `.env` फाइलमा राख्नुहोस्।

Azure स्रोत सेटअपका लागि, हेर्नुहोस् [Azure AI सेटअप](azure-ai-setup.md).

## स्थानीय रनटाइम सेटअप

CLI स्थानीय रूपमा चलाउनु अघि भर्चुअल वातावरण प्रयोग गर्नुहोस्। Co-op Translator ले Python 3.11 देखि 3.14 सम्म समर्थन गर्छ।

सामान्य CLI प्रयोगका लागि, प्रकाशित प्याकेजलाई भर्चुअल वातावरण भित्र इन्स्टल गर्नुहोस्:

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

### रिपोजिटरी विकास

रिपोजिटरी विकासका लागि, यसको सट्टा प्रोजेक्ट रुटबाट निर्भरताहरू इन्स्टल गर्नुहोस्:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध भएपछि, `.env` मा एउटा भाषा मोडेल प्रदायक कन्फिगर गर्नुहोस्।

## प्रदायक चयन

उपकरणले निम्न क्रममा प्रदायकहरू स्वचालित रूपमा पत्ता लगाउँछ:

1. Azure OpenAI
2. OpenAI
3. Anthropic

अनुवादका लागि प्रदायक प्रमाण-पत्रहरू आवश्यक हुन्छन्, यद्यपि पूर्वावलोकनहरू जस्तै `translate -l "ko" -md --dry-run` को लागि आवश्यक पर्दैन। `migrate-links`, `co-op-review`, र `run_review` निर्धारक मर्मत कार्यहरू हुन् र तिनीहरूलाई प्रदायक प्रमाण-पत्रहरू आवश्यक पर्दैन।

## मोडेल क्लाइन्ट ब्याकएन्ड

Co-op Translator 0.22.0 देखि सुरू गरी, Azure OpenAI, OpenAI, र Anthropic ले डिफल्ट रूपमा Microsoft Agent Framework प्रयोग गर्छन्। सामान्य प्रयोगका लागि कुनै ब्याकएन्ड सेटिङ आवश्यक पर्दैन।

अनुकूलताका लागि Semantic Kernel अस्थायी रूपमा उपलब्ध छ। यसलाई स्पष्ट रूपमा चयन गर्न, सेट गर्नुहोस्:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel प्रयोग गर्दा अवमूल्यन चेतावनी देखािन्छ। प्याकेजले Semantic Kernel लाई 0.23.0 मा वैकल्पिक निर्भरता बनाउने र 0.24.0 मा एकीकरण हटाउने योजना राखेको छ, जुन अनुकूलता नतिजाहरू र प्रयोगकर्ता प्रतिक्रियामा निर्भर रहनेछ। Anthropic लाई `agent-framework` चाहिन्छ; Anthropic सँग `semantic-kernel` लाई स्पष्ट रूपमा चयन गर्दा कन्फिगरेसन त्रुटि हुन्छ। अवैध मानहरू provider-backed translator को इनिसियलाइजेसनको क्रममा असफल हुन्छन्, स्वतः fallback हुनका सट्टा। रोलआउटलाई ट्र्याक गर्नुहोस् र अवरोधहरू रिपोर्ट गर्नुहोस् [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

जब तपाइँको मोडेल Azure AI Foundry वा Azure OpenAI Service मा डिप्लोय गरिएको छ तब Azure OpenAI प्रयोग गर्नुहोस्।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

अनुवाद सुरु हुनु अघि कनेक्टिविटी जाँचले endpoint, API key, API version, र deployment name प्रयोग गर्छ।

## OpenAI

OpenAI API सिधै कल गर्दा OpenAI प्रयोग गर्नुहोस्।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` आवश्यक छ किनभने अनुवादकर्ताले API कलहरूको लागि स्पष्ट chat मोडेल चाहिन्छ।

डिफल्ट सेटअपका लागि `OPENAI_ORG_ID` र `OPENAI_BASE_URL` लाई अनसेट राख्नुहोस्। तपाईंको अकाउन्टले आवश्यक परे मात्र संगठन ID थप्नुहोस्, वा कस्टम endpoint प्रयोग गर्दा मात्र base URL सेट गर्नुहोस्। वैकल्पिक सेटिङहरूका लागि placeholder मानहरू नकल नगर्नुहोस्।

## Anthropic Claude

Claude API सिधै कल गर्दा Anthropic प्रयोग गर्नुहोस्। एउटा [Anthropic API कुञ्जी](https://platform.claude.com/docs/en/get-started) बनाउनुहोस् र समर्थन गरिने [Claude मोडेल ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) छान्नुहोस्।

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` र `ANTHROPIC_MODEL` आवश्यक छन्। तपाईंलाई `CO_OP_TRANSLATOR_MODEL_CLIENT` सेट गर्न जरुरी छैन; Agent Framework डिफल्ट ब्याकएन्ड हो।

Anthropic API का लागि `ANTHROPIC_BASE_URL` अनसेट राख्नुहोस्। केवल कस्टम endpoint प्रयोग गर्दा मात्र यसलाई सेट गर्नुहोस्।

`ANTHROPIC_MAX_TOKENS` को डिफल्ट `8192` हो, जसले Meitei Mayek जस्ता token-घना स्क्रिप्टहरूका लागि स्थान छोड्छ। यदि तपाईंको मोडेल वा Anthropic-संग मिल्ने endpoint ले सो भन्दा कम आउटपुट सीमित गर्छ भने यसलाई घटाउनुहोस्।

## Azure AI Vision

तस्बिर अनुवादको लागि Azure AI Vision आवश्यक हुन्छ ताकि टुलले छविबाट टेक्स्ट निकाल्न सकोस् र सो टेक्स्ट कन्फिगर गरिएको भाषा मोडेलले अनुवाद गर्न सकोस्। Anthropic ले पनि निकालिएको टेक्स्टलाई Azure OpenAI वा OpenAI जस्तै अनुवाद गर्न सक्छ।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

यदि `-img`, `images=True`, वा कुनै content-type फिल्टर नभएको अवस्थामा तस्बिर अनुवाद चयन गरिएको छ भने, टुलले अनुवाद सुरु हुनुअघि Vision कन्फिगरेसनलाई मान्य बनाउँछ।

## बहु क्रेडेन्सियल सेटहरू

कन्फिगरेसन लेयरले एउटै इन्डेक्समा suffix गरेर बहु क्रेडेन्सियल सेटहरू समर्थन गर्छ:

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

प्रत्येक सेट पूरा हुनैपर्छ। स्वास्थ्य जाँचले अनुवाद अघि काम गर्ने सेट चयन गर्दछ।

OpenAI र Anthropic ले समान suffix सम्मेलन समर्थन गर्छन्। क्रेडेन्सियल सेटभित्र प्रत्येक भेरिएबललाई एउटै suffix मा राख्नुहोस्, `OPENAI_BASE_URL_1` वा `ANTHROPIC_BASE_URL_1` जस्ता वैकल्पिक मानहरू सहित।

## कमाण्ड आवश्यकताहरू

| Command वा API | LLM आवश्यक | Vision आवश्यक | नोट्स |
| --- | --- | --- | --- |
| `translate -md` | हो | होइन | केवल Markdown अनुवाद गर्छ। |
| `translate -nb` | हो | होइन | केवल नोटबुकहरू अनुवाद गर्छ। |
| `translate -img` | हो | हो | केवल तस्बिरहरू अनुवाद गर्छ। |
| `translate` with no type flags | हो | हो | डिफल्ट मोडमा Markdown, नोटबुकहरू, र तस्बिरहरू समावेश छन्। |
| `evaluate` | हो | होइन | यदि `--fast` चयन गरिएको छैन भने LLM मूल्याङ्कन प्रयोग गर्छ। |
| `migrate-links` | होइन | होइन | प्रदायक कलहरू बिना स्थानीय लिंक माइग्रेशन गर्छ। |
| `co-op-review` | होइन | होइन | अनुवादको संरचना, ताजापन, Markdown, नोटबुक, र स्थानीय लिंक जाँचहरू निर्धारक रूपमा चलाउँछ। |
| `run_translation(markdown=True)` | हो | होइन | प्रोग्रामिक Markdown अनुवाद। |
| `run_translation(images=True)` | हो | हो | प्रोग्रामिक तस्बिर अनुवाद। |
| `run_review(...)` | होइन | होइन | प्रोग्रामिक निर्धारक समीक्षा। |

## आउटपुट डाइरेक्टरीहरू

डिफल्ट टेक्स्ट अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफल्ट अनुवादित तस्बिर आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ले यी डाइरेक्टरीहरूलाई `translations_dir` र `image_dir` प्रयोग गरेर ओभरराइड गर्न सक्छ।