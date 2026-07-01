# Configuration

Co-op Translator inahitaji mtoaji mmoja wa modeli ya lugha. Tafsiri ya picha kwa ziada inahitaji Azure AI Vision.

Usanidi unasomwa kutoka kwa vigezo vya mazingira. Kwa miradi ya ndani, weka ndani ya faili `.env` katika mizizi ya mradi.

Kwa usanidi wa rasilimali za Azure, angalia [Usanidi wa Azure AI](azure-ai-setup.md).

## Local runtime setup

Tumia mazingira pepe kabla ya kuendesha CLI kwa ndani. Co-op Translator inasaidia Python 3.10 hadi 3.12.

Kwa matumizi ya kawaida ya CLI, weka kifurushi kilichochapishwa ndani ya mazingira pepe:

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

Kwa ukuzaji wa hazina, weka utegemezi kutoka kwenye mizizi ya mradi badala yake:

```bash
poetry install
poetry run translate --help
```

Baada ya CLI kupatikana, sanidi mtoaji mmoja wa modeli ya lugha katika `.env`.

## Provider selection

Chombo hugitambua watoaji moja kwa moja kwa mpangilio huu:

1. Azure OpenAI
2. OpenAI

Kama hakuna mtoa huduma aliyesanidiwa, `translate`, `evaluate`, `migrate-links`, na `run_translation` zitashindwa wakati wa ukaguzi wa usanidi. `co-op-review` na `run_review` ni ukaguzi wa matengenezo unaotabirika na hazihitaji nyaraka za mtoa huduma.

## Azure OpenAI

Tumia Azure OpenAI wakati modeli yako imewekwa katika Azure AI Foundry au Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ukaguzi wa muunganisho unatumia endpoint, API key, API version, na deployment name kabla ya kuanza kwa tafsiri.

## OpenAI

Tumia OpenAI unapoitisha OpenAI API moja kwa moja.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # hiari
OPENAI_BASE_URL="..."        # hiari
```

`OPENAI_CHAT_MODEL_ID` inahitajika kwa sababu mtafsiri anahitaji modeli maalum ya mazungumzo kwa wito za API.

## Azure AI Vision

Tafsiri ya picha inahitaji Azure AI Vision ili chombo kiweze kutoa maandishi kutoka kwa picha kabla ya kuyatafsiri.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ikiwa tafsiri ya picha imechaguliwa kwa `-img`, `images=True`, au hakuna kichujio cha content-type, chombo kinathibitisha usanidi wa Vision kabla ya kuanza kwa tafsiri.

## Multiple credential sets

Tabaka la usanidi linaunga mkono seti nyingi za nyaraka kwa kuongeza nambari ya mwisho kwa vigezo vyenye kiashiria sawa:

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

Kila seti lazima iwe kamili. Ukaguzi wa afya huchagua seti inayofanya kazi kabla ya kuendelea na tafsiri.

## Command requirements

| Amri au API | Inahitaji LLM | Inahitaji Vision | Maelezo |
| --- | --- | --- | --- |
| `translate -md` | Ndio | Hapana | Inatafsiri Markdown tu. |
| `translate -nb` | Ndio | Hapana | Inatafsiri notibuki tu. |
| `translate -img` | Ndio | Ndio | Inatafsiri picha tu. |
| `translate` with no type flags | Ndio | Ndio | Hali ya chaguo-msingi inajumuisha Markdown, notebooks, na picha. |
| `evaluate` | Ndio | Hapana | Inatumia tathmini ya LLM isipokuwa `--fast` ikichaguliwa. |
| `migrate-links` | Ndio | Hapana | Hufanya uhamishaji wa viungo, lakini bado hufanya ukaguzi wa usanidi ulioshirikiwa. |
| `co-op-review` | Hapana | Hapana | Inafanya ukaguzi wa muundo wa tafsiri unaotabirika, upya, Markdown, notebook, na ukaguzi wa viungo vya ndani. |
| `run_translation(markdown=True)` | Ndio | Hapana | Tafsiri ya Markdown kwa programu. |
| `run_translation(images=True)` | Ndio | Ndio | Tafsiri ya picha kwa programu. |
| `run_review(...)` | Hapana | Hapana | Mapitio unaotabirika wa programu. |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

API ya Python inaweza kubadilisha folda hizi kwa kutumia `translations_dir` na `image_dir`.