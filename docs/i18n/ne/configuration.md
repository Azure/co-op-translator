# कन्फिगरेसन

Co-op Translator लाई एउटा भाषा मोडेल प्रदायक आवश्यक छ। छवि अनुवादका लागि अतिरिक्त रूपमा Azure AI Vision आवश्यक हुन्छ।

कन्फिगरेसन वातावरण चरहरूबाट पढिन्छ। स्थानीय परियोजनाहरूको लागि, तिनीहरूलाई परियोजना रुटमा `.env` फाइलमा राख्नुहोस्।

Azure स्रोत सेटअपका लागि हेर्नुहोस् [Azure AI सेटअप](azure-ai-setup.md).

## स्थानीय रनटाइम सेटअप

स्थानीय रूपमा CLI चलाउनुअघि भर्चुअल वातावरण प्रयोग गर्नुहोस्। Co-op Translator ले Python 3.10 देखि 3.12 सम्म समर्थन गर्छ।

सामान्य CLI प्रयोगका लागि, प्रकाशित प्याकेजलाई भर्चुअल वातावरण भित्र इन्स्टल गर्नुहोस्:

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

रिपोजिटरी विकासका लागि, परियोजना रुटबाट निर्भरताहरू इन्स्टल गर्नुहोस्:

```bash
poetry install
poetry run translate --help
```

CLI उपलब्ध भएपछि, एउटै भाषा मोडेल प्रदायक `.env` मा कन्फिगर गर्नुहोस्।

## प्रदायक चयन

उपकरणले निम्न क्रममा प्रदायकहरू अटो-डिटेक्ट गर्छ:

1. Azure OpenAI
2. OpenAI

यदि कुनै पनि प्रदायक कन्फिगर गरिएको छैन भने, `translate`, `evaluate`, `migrate-links`, र `run_translation` कन्फिगरेसन जाँचहरूको क्रममा असफल हुन्छन्। `co-op-review` र `run_review` निर्धारक मर्मत जाँचहरू हुन् र यीले प्रदायक क्रेडेन्शियलहरू आवश्यक पर्दैन।

## Azure OpenAI

तपाईंको मोडेल Azure AI Foundry वा Azure OpenAI Service मा डिप्लोइ गरिएको अवस्थामा Azure OpenAI प्रयोग गर्नुहोस्।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

कनेक्टिभिटी जाँचले अनुवाद सुरु हुनुअघि एन्डपोइन्ट, API कुञ्जी, API संस्करण, र डिप्लोयमेन्ट नाम प्रयोग गर्छ।

## OpenAI

OpenAI API सिधा कल गर्दा OpenAI प्रयोग गर्नुहोस्।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # वैकल्पिक
OPENAI_BASE_URL="..."        # वैकल्पिक
```

`OPENAI_CHAT_MODEL_ID` आवश्यक छ किनभने अनुवादकलाई API कलहरूको लागि स्पष्ट च्याट मोडेल चाहिन्छ।

## Azure AI Vision

छवि अनुवादको लागि Azure AI Vision आवश्यक छ ताकि उपकरणले अनुवाद गर्नु अघि छविहरूबाट पाठ निकाल्न सकोस्।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

यदि छवि अनुवाद `-img`, `images=True`, वा कुनै content-type फिल्टर नहुँदा चयन गरिएको छ भने, उपकरणले अनुवाद सुरु हुनु अघि Vision कन्फिगरेसनलाई मान्य गर्छ।

## बहु क्रेडेन्शियल सेटहरू

कन्फिगरेसन लेयरले भेरिएबलहरूमा उस्तै सूचकांक (index) थपेर धेरै क्रेडेन्शियल सेटहरू समर्थन गर्छ:

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

प्रत्येक सेट पूर्ण हुनैपर्छ। स्वास्थ्य जाँचले अनुवाद अघि काम गर्ने सेट चयन गर्छ।

## कमाण्ड आवश्यकताहरू

| कमाण्ड वा API | LLM आवश्यक | Vision आवश्यक | नोटहरू |
| --- | --- | --- | --- |
| `translate -md` | हो | होइन | Markdown मात्र अनुवाद गर्छ। |
| `translate -nb` | हो | होइन | नोटबुक मात्र अनुवाद गर्छ। |
| `translate -img` | हो | हो | छविहरू मात्र अनुवाद गर्छ। |
| `translate` with no type flags | हो | हो | पूर्वनिर्धारित मोडमा Markdown, नोटबुकहरू, र छविहरू समावेश हुन्छ। |
| `evaluate` | हो | होइन | जबसम्म `--fast` चयन गरिएको छैन तबसम्म LLM मूल्याङ्कन प्रयोग गर्छ। |
| `migrate-links` | हो | होइन | लिंक माइग्रेसन गर्छ, तर अझै साझा कन्फिगरेसन जाँचहरू चलाउँछ। |
| `co-op-review` | होइन | होइन | निर्धारक अनुवाद संरचना, ताजगी, Markdown, नोटबुक, र स्थानीय लिङ्क जाँचहरू चलाउँछ। |
| `run_translation(markdown=True)` | हो | होइन | प्रोग्रामेटिक Markdown अनुवाद। |
| `run_translation(images=True)` | हो | हो | प्रोग्रामेटिक छवि अनुवाद। |
| `run_review(...)` | होइन | होइन | प्रोग्रामेटिक निर्धारक समीक्षा। |

## आउटपुट डाइरेक्टरीहरू

डिफल्ट पाठ अनुवाद आउटपुट:

```text
translations/<language-code>/<source-relative-path>
```

डिफल्ट अनुवादित छवि आउटपुट:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ले यी डाइरेक्टरीहरूलाई `translations_dir` र `image_dir` द्वारा ओभरराइड गर्न सक्छ।