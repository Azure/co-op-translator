# கட்டமைப்பு

Co-op Translatorக்கு ஒரு மொழி மாடல் வழங்குனர் ஒன்றே தேவையாகும். பட மொழிபெயர்ப்பிற்கு கூடுதலாக Azure AI Vision தேவை.

கட்டமைப்பை சுற்றுச்சூழல் மாறில்களிலிருந்து வாசிக்கப்படுகிறது. உள்ளூரில் உள்ள திட்டங்களுக்கு, அவற்றை திட்டத்தின் ரூட்டில் உள்ள `.env` கோப்பில் வைக்கவும்.

Azure வள அமைப்பிற்கான விபரங்களுக்கு, [Azure AI அமைப்பு](azure-ai-setup.md) பார்க்கவும்.

## உள்ளூர் இயக்க சூழல் அமைப்பு

CLI-யை உள்ளூரில் இயக்குவதற்கு முன் ஒரு மெய்நிகர் சூழலை (virtual environment) பயன்படுத்துங்கள். Co-op Translator Python 3.10 முதல் 3.12 வரை ஆதரிக்கிறது.

சாதாரண CLI பயன்பாட்டிற்கு, வெளியிடப்பட்ட package-ஐ ஒரு மெய்நிகர் சூழலில் நிறுவுங்கள்:

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

களஞ்சிய மேம்பாட்டுக்காக, பதிலாக திட்டத்தின் ரூட்டிலிருந்து சார்புகளை நிறுவவும்:

```bash
poetry install
poetry run translate --help
```

CLI கிடைக்கும் பிறகு, `.env` இல் ஒரு மொழி மாடல் வழங்குனரை அமைக்கவும்.

## வழங்குனர் தேர்வு

கருவி பின்வரும் வரிசையில் வழங்குனர்களை தானாக கண்டுபிடிக்கிறது:

1. Azure OpenAI
2. OpenAI

இரண்டிலும் எந்தவொரு வழங்குனரும் கட்டமைக்கப்படவில்லை என்றால், `translate`, `evaluate`, `migrate-links`, மற்றும் `run_translation` கட்டமைப்பு சரிபார்ப்புகள் செய்யும்போது தோல்வியடையும். `co-op-review` மற்றும் `run_review` நிர்ணயமான பராமரிப்பு சரிபார்ப்புகள் ஆகும் மற்றும் வழங்குனர் அங்கீகாரங்களைப் பெற தேவையில்லை.

## Azure OpenAI

உங்கள் மாடல் Azure AI Foundry அல்லது Azure OpenAI Service இல் தொடங்கப்பட்டிருக்கும் போது Azure OpenAI பயன்படுத்தவும்.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

தொடர்பு சோதனை மொழிபெயர்ப்பு துவங்குவதற்கு முன் endpoint, API key, API version மற்றும் deployment name ஆகியவற்றைப் பயன்படுத்துகிறது.

## OpenAI

OpenAI API-வை நேரடியாக அழைக்கும் போது OpenAI-ஐ பயன்படுத்தவும்.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # விருப்பமான
OPENAI_BASE_URL="..."        # விருப்பமான
```

`OPENAI_CHAT_MODEL_ID` தேவையாகும், ஏனெனில் மொழிபெயர்ப்பகரம் API அழைப்புகளுக்கான தெளிவான chat மாடலைக் கோரியுள்ளது.

## Azure AI Vision

பட மொழிபெயர்ப்பு Azure AI Vision-ஐ தேவைப்படுத்துகிறது, அதனால் கருவி படங்களில் உள்ள உரையை பின்பு மொழிபெயர்க்கும் முன் எடுக்கும்.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True` அல்லது எந்த content-type வடிகட்டியும் இல்லாமல் பட மொழிபெயர்ப்பு தேர்ந்தெடுக்கப்பட்டால், மொழிபெயர்ப்பு துவங்குவதற்கு முன் கருவி Vision கட்டமைப்பை சரிபார்க்கிறது.

## பல சான்றிதழ் தொகுதிகள்

கட்டமைப்பு அடுக்குத் தொகுப்பு ஒரே காட்டியை (index) கொண்ட மாறில்களை அடைப்பு செய்து பல சான்றிதழ் தொகுதிகளை ஆதரிக்கிறது:

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

ஒவ்வொரு தொகுதியும் முழுமையாக இருக்க வேண்டும். ஆரோக்கியச் சோதனை (health check) மொழிபெயர்ப்பு தொடரும் முன் செயல்படும் தொகுதியை தேர்வு செய்கிறது.

## கட்டளை தேவைகள்

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | ஆம் | இல்லை | Markdown-ஐ மட்டும் மொழிபெயர்க்கிறது. |
| `translate -nb` | ஆம் | இல்லை | notebooks-ஐ மட்டும் மொழிபெயர்க்கிறது. |
| `translate -img` | ஆம் | ஆம் | படங்களை மட்டும் மொழிபெயர்க்கிறது. |
| `translate` with no type flags | ஆம் | ஆம் | இயல்புநிலை முறையில் Markdown, notebooks மற்றும் படங்கள் அனைத்தும் உள்ளடக்கப்படும். |
| `evaluate` | ஆம் | இல்லை | `--fast` தேர்ந்தெடுக்கப்படாமலிருந்தால் LLM மதிப்பீட்டை பயன்படுத்துகிறது. |
| `migrate-links` | ஆம் | இல்லை | இணைப்பு இடமாற்றத்தைச் செய்கிறது, ஆனால் இன்னும் பகிரப்பட்ட கட்டமைப்பு சரிபார்ப்புகளை இயக்குகிறது. |
| `co-op-review` | இல்லை | இல்லை | நிர்ணயமான மொழிபெயர்ப்பு அமைப்பு, تاز்மை (freshness), Markdown, notebook மற்றும் உள்ளூர் இணைப்பு சரிபார்ப்புகளை இயக்குகிறது. |
| `run_translation(markdown=True)` | ஆம் | இல்லை | நிரலாக்க மொழியில் Markdown மொழிபெயர்ப்பு. |
| `run_translation(images=True)` | ஆம் | ஆம் | நிரலாக்க மொழியில் பட மொழிபெயர்ப்பு. |
| `run_review(...)` | இல்லை | இல்லை | நிரலாக்க மொழியில் நிர்ணயமான மதிப்பாய்வு. |

## வெளியீட்டு அடைவரிசைகள்

இயல்பான உரை மொழிபெயர்ப்பு வெளியீடு:

```text
translations/<language-code>/<source-relative-path>
```

இயல்பான மொழிபெயர்க்கப்பட்ட பட வெளியீடு:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API `translations_dir` மற்றும் `image_dir` என்பன மூலம் இவைகளை மாற்றிக்கொள்ளலாம்.