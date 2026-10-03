# கட்டமைப்பு

Co-op Translator-க்கு ஒரு மொழி மாடல் வழங்குநர் தேவையாகும். படப் மொழிபெயர்ப்புக்கு கூடுதல், Azure AI Vision தேவை.

கட்டமைப்பு சூழல் மாறில்களிலிருந்து படிக்கப்படுகிறது. உள்ளூர் திட்டங்களுக்கு, அவற்றை `.env` கோப்பில் திட்டத்தின் ரூட்டில் வைக்கவும்.

Azure வள அமைப்பிற்காக, [Azure AI அமைப்பு](azure-ai-setup.md) ஐப் பார்க்கவும்.

## உள்ளூர் ரன்டைம் அமைப்பு

CLI-ஐ உள்ளூராக இயக்குவதற்கு முன் ஒரு மெய்நிகர் சூழலைப் பயன்படுத்தவும். Co-op Translator Python 3.11 முதல் 3.14 வரை ஆதரிக்கிறது.

சாதாரண CLI பயன்பாட்டிற்கு, வெளியிடப்பட்ட பேக்கேஜை மெய்நிகர் சூழலுக்குள் நிறுவவும்:

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

### Repository மேம்பாடு

Repository மேம்பாட்டிற்காக, பதிலாக திட்டத்தின் ரூட்டிலிருந்து இணைக்கூறுகளை நிறுவவும்:

```bash
poetry install
poetry run translate --help
```

CLI கிடைக்கும்போது, `.env`ல் ஒரு மொழி மாதிரி வழங்குநரை கட்டமைக்கவும்.

## வழங்குநர் தேர்வு

கருவி கீழ்க்காணும் வரிசையில் வழங்குநர்களை தானாக கண்டறிகிறது:

1. Azure OpenAI
2. OpenAI
3. Anthropic

மொழிபெயர்ப்பிற்கு வழங்குநர் சான்றுகள் (credentials) தேவை, உதாரணமாக முன்னோட்டங்களுக்கு `translate -l "ko" -md --dry-run` போன்றவற்றைத் தவிர. `migrate-links`, `co-op-review`, மற்றும் `run_review` தீர்மானமான பராமரிப்பு செயல்கள் என்பதால் அவை வழங்குநர் சான்றுகளை தேடாது.

## மாடல் கிளையன்ட் பின்னணி

Co-op Translator 0.22.0 முதல், Azure OpenAI, OpenAI மற்றும் Anthropic இயல்பாக Microsoft Agent Framework-ஐப் பயன்படுத்துகின்றன. சாதாரண பயன்பாட்டிற்கு பின்னணி அமைப்பை அமைக்க தேவையில்லை.

பொருந்துதலுக்கு Semantic Kernel தற்காலிகமாக கிடைக்கிறது. அதை தெளிவாகத் தேர்ந்தெடுக்க, இதை அமைக்கவும்:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel பயன்படுத்துவதால் ஒரு deprecation எச்சரிக்கை வெளியிடப்படுகிறது. தொகுப்பு Semantic Kernel-ஐ விருப்ப பொறுப்பாக (optional dependency) 0.23.0-ல் மாற்றவும் மற்றும் 0.24.0-இல் ஒருங்கிணைப்பை நீக்க திட்டமிடப்பட்டுள்ளது, இது பொருந்துதலின் முடிவுகள் மற்றும் பயனர் பின்னூட்டத்தின் அடிப்படையில் இருக்கும். Anthropic-க்கு `agent-framework` தேவை; Anthropic உடன் தெளிவாக `semantic-kernel`-ஐ தேர்ந்தெடுப்பது கட்டமைப்பு பிழையால் தோல்வியடையும். தவறான மதிப்புகள் மௌனமாக fallback ஆகாமல் பதிலாக வழங்குநர் ஆதரவு மொழிபெயர்ப்பாளர் ஒருங்கிணைப்பு ஆரம்பத்தில் தோல்வியடையும். வெளியீட்டை பின்தொடரவும் மற்றும் தடைகளை [GitHub பிரச்சினை #543](https://github.com/Azure/co-op-translator/issues/543) இல் பதிவு செய்யவும்.

## Azure OpenAI

உங்கள் மாடல் Azure AI Foundry அல்லது Azure OpenAI Service-இல் பதிக்கப்பட்டிருந்தால் Azure OpenAI-யைப் பயன்படுத்தவும்.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

இணைப்பு சோதனை மொழிபெயர்ப்பு தொடங்குவதற்கு முன் endpoint, API key, API version மற்றும் deployment name ஆகியவற்றைப் பயன்படுத்துகிறது.

## OpenAI

OpenAI API-ஐ நேரடியாக அழைக்கும் போது OpenAI-யைப் பயன்படுத்தவும்.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` தேவைப்படுகின்றது, ஏனெனில் மொழிபெயர்ப்பாளருக்கு API அழைப்புகளுக்கான ஒரு தெளிவான chat மாதிரி அவசியம்.

`OPENAI_ORG_ID` மற்றும் `OPENAI_BASE_URL`-ஐ இயல்புநிலைக்காக அமைக்காமல் வைக்கவும். உங்கள் கணக்கு ஒரு அமைப்புப் ID-ஐ தேவைப்படுத்தினால் மட்டுமே அமைப்புப் ID ஐச் சேர்க்கவும், அல்லது தனிப்பயன் endpoint பயன்படுத்தும்போது மட்டுமே base URL ஐச் சேர்க்கவும். விருப்பமான அமைப்புகளுக்கான placeholder மதிப்புகளை நகலெடுக்காதீர்கள்.

## Anthropic Claude

Claude API-ஐ நேரடியாக அழைக்கும் போது Anthropic-ஐப் பயன்படுத்தவும். ஒரு [Anthropic API விசை](https://platform.claude.com/docs/en/get-started) உருவாக்கவும் மற்றும் ஆதரிக்கப்படும் [Claude மாதிரி ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ஒன்றை தேர்ந்தெடுக்கவும்.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` மற்றும் `ANTHROPIC_MODEL` அவசியம். `CO_OP_TRANSLATOR_MODEL_CLIENT` ஐ அமைக்க தேவையில்லை; Agent Framework இயல்புநிலை பின்னணியாகும்.

`ANTHROPIC_BASE_URL` ஐ Anthropic API-க்காக அமைக்காமல் வைக்கவும். தனிப்பயன் endpoint பயன்படுத்துமானால் மட்டுமே அதை அமைக்கவும்.

`ANTHROPIC_MAX_TOKENS` தனது இயல்புநிலை மதிப்பாக `8192` ஆகும், இது Meitei Mayek போன்ற token அடர்த்தியான எழுத்துருக்களுக்கு இடம் விடுகிறது. உங்கள் மாடல் அல்லது Anthropic-உருப்படியான endpoint வெளியீட்டை அதற்கு கீழ் கட்டுப்படுத்தினால் இதைக் குறைக்கவும்.

## Azure AI Vision

பட மொழிபெயர்ப்புக்கு Azure AI Vision தேவை, ஏனெனில் கருவி படங்களில் இருந்து உரையை பிரித்து அதை நந்தியமிடும் மொழி மாடல் மொழிபெயர்க்கும் முன் எடுத்துக் கொள்ள இது அவசியம். Anthropic பிரிக்கப்பட்ட உரையை Azure OpenAI அல்லது OpenAI போலவே மொழிபெயர்க்க முடியும்.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

பட மொழிபெயர்ப்பு `-img`, `images=True` அல்லது எந்த content-type வடிகட்டலும் இல்லாமல் தேர்ந்தெடுக்கப்பட்டால், கருவி மொழிபெயர்ப்பு தொடங்குவதற்கு முன் Vision அமைப்பைச் சரிபார்க்கும்.

## பல சான்றிதழ் செட்டுகள்

கட்டமைப்பு அடுக்கு, மாறில்களுக்கு ஒரே குறியீடான suffix சேர்த்து பல சான்றிதழ் செட்டுகளை ஆதரிக்கிறது:

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

ஒவ்வொரு செட்டும் முழுமையானதாக இருக்க வேண்டும். ஹெல்த் சோதனை மொழிபெயர்ப்பு தொடங்குவதற்கு முன் ஒரு செயல்படும் செட்டை தேர்வு செய்யும்.

OpenAI மற்றும் Anthropic ஒரே suffix நடைமுறையை ஆதரிக்கின்றன. ஒரு சான்றிதழ் செட்டில் உள்ள ஒவ்வொரு மாறியையும் அதே suffix-இல் வைத்திருங்கள், இதில் `OPENAI_BASE_URL_1` அல்லது `ANTHROPIC_BASE_URL_1` போன்ற விருப்பமான மதிப்புகளும் அடங்கும்.

## கட்டளை தேவைகள்

| கட்டளை அல்லது API | LLM தேவை | Vision தேவை | குறிப்புகள் |
| --- | --- | --- | --- |
| `translate -md` | ஆம் | இல்லை | Markdown மட்டுமே மொழிபெயர்க்கிறது. |
| `translate -nb` | ஆம் | இல்லை | நோட்புக் கோப்புகளை மட்டும் மொழிபெயர்க்கிறது. |
| `translate -img` | ஆம் | ஆம் | படங்களை மட்டும் மொழிபெயர்க்கும். |
| `translate` with no type flags | ஆம் | ஆம் | இயல்புநிலை முறையில் Markdown, நோட்புக் கோப்புகள் மற்றும் படங்கள் அடங்கும். |
| `evaluate` | ஆம் | இல்லை | `--fast` தேர்ந்தெடுக்கப்படாவிட்டால் LLM மதிப்பீட்டை பயன்படுத்தும். |
| `migrate-links` | இல்லை | இல்லை | வழங்குநர் அழைப்புகள் இல்லாமல் உள்ளூர் இணைப்பு இடமாற்றத்தை நிகழ்த்துகிறது. |
| `co-op-review` | இல்லை | இல்லை | தீர்மானமான மொழிபெயர்ப்பு கட்டமைப்பு, புதுமைத்தன்மை, Markdown, நோட்புக் மற்றும் உள்ளூர் இணைப்பு சோதனைகளை இயக்கும். |
| `run_translation(markdown=True)` | ஆம் | இல்லை | நிரல்பூர்வ Markdown மொழிபெயர்ப்பு. |
| `run_translation(images=True)` | ஆம் | ஆம் | நிரல்பூர்வ பட மொழிபெயர்ப்பு. |
| `run_review(...)` | இல்லை | இல்லை | நிரல்பூர்வ தீர்மானமான பரிசீலனை. |

## வெளியீட்டு அடைவுகள்

இயல்புநிலை உரை மொழிபெயர்ப்பு வெளியீடு:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API இவை கோப்புறைகளை `translations_dir` மற்றும் `image_dir` மூலம் மீறலாம்.
