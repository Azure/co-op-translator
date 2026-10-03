# Mipangilio

Co-op Translator inahitaji msambazaji mmoja wa modeli ya lugha. Kutafsiri picha pia kunahitaji Azure AI Vision.

Mipangilio husomwa kutoka kwa vigezo vya mazingira. Kwa miradi ya ndani, waiweke katika faili `.env` kwenye mzizi wa mradi.

Kwa usanidi wa rasilimali za Azure, angalia [Azure AI Setup](azure-ai-setup.md).

## Usanidi wa wakati wa kukimbia kwa ndani

Tumia mazingira pepe kabla ya kuendesha CLI kwa ndani. Co-op Translator inaunga mkono Python 3.11 hadi 3.14.

Kwa matumizi ya kawaida ya CLI, weka kifurushi kilichochapishwa ndani ya mazingira pepe:

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

### Maendeleo ya hazina

Kwa maendeleo ya hazina, badala yake weka utegemezi kutoka kwa mzizi wa mradi:

```bash
poetry install
poetry run translate --help
```

Baada ya CLI kupatikana, sanidi msambazaji mmoja wa modeli ya lugha katika `.env`.

## Uchaguzi wa msambazaji

Chombo kinatambua wasambazaji kiotomatiki kwa mpangilio huu:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Tafsiri inahitaji cheti za msambazaji, isipokuwa kwa mapitio kama `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, na `run_review` ni shughuli za matengenezo zinazoamuliwa na hazihitaji cheti za msambazaji.

## Sehemu ya nyuma ya mteja wa modeli

Kuanzia Co-op Translator 0.22.0, Azure OpenAI, OpenAI, na Anthropic zinatumia Microsoft Agent Framework kwa chaguo-msingi. Hakuna usanidi wa backend unaohitajika kwa matumizi ya kawaida.

Semantic Kernel bado inapatikana kwa muda kwa ajili ya ulinganishaji. Ili kuichagua waziwazi, weka:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Kutumia Semantic Kernel kunatoa onyo la kuachwa. Kifurushi kinapangwa kuhamisha Semantic Kernel kuwa utegemezi wa hiari katika 0.23.0 na kuondoa muunganisho katika 0.24.0, kulingana na matokeo ya ulinganifu na maoni ya watumiaji. Anthropic inahitaji `agent-framework`; kuchagua waziwazi `semantic-kernel` na Anthropic husababisha kosa la usanidi. Thamani zisizo halali zitashindwa wakati wa uanzishaji wa mtafsiri unaotegemea msambazaji badala ya kushuka kimya. Fuata utangazaji na ripoti vikwazo katika [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Tumia Azure OpenAI wakati modeli yako imewekwa katika Azure AI Foundry au Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ukaguzi wa muunganisho unatumia endpoint, API key, API version, na deployment name kabla ya kutafsiri kuanza.

## OpenAI

Tumia OpenAI unapopiga API ya OpenAI moja kwa moja.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` inahitajika kwa sababu mtafsiri anahitaji modeli maalum ya mazungumzo kwa wito za API.

Acha `OPENAI_ORG_ID` na `OPENAI_BASE_URL` zisiwe zimewekwa kwa usanidi wa chaguo-msingi. Ongeza kitambulisho cha shirika tu ikiwa akaunti yako inahitaji, au base URL tu unapokitumia endpoint maalum. Usinakili thamani za kielelezo kwa mipangilio ya hiari.

## Anthropic Claude

Tumia Anthropic unapopiga API ya Claude moja kwa moja. Tengeneza [funguo la API la Anthropic](https://platform.claude.com/docs/en/get-started) na chagua [Kitambulisho cha modeli ya Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) inayotumika.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` na `ANTHROPIC_MODEL` zinahitajika. Huna haja ya kuweka `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework ni backend ya chaguo-msingi.

Acha `ANTHROPIC_BASE_URL` isiyowekwa kwa API ya Anthropic. Iweke tu unapotumia endpoint maalum.

`ANTHROPIC_MAX_TOKENS` kwa kawaida ni `8192`, ambayo inatoa nafasi kwa maandishi yenye wingi wa token kama Meitei Mayek. Punguza ikiwa modeli yako au endpoint inayolingana na Anthropic inapunguza matokeo chini ya hapo.

## Azure AI Vision

Kutafsiri picha kunahitaji Azure AI Vision ili chombo kiweze kutoa maandishi kutoka kwa picha kabla modeli ya lugha iliyosanidiwa kuziatafsiri. Anthropic inaweza kutafsiri maandishi yaliyotolewa kama vile Azure OpenAI au OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ikiwa kutafsiri picha kumechaguliwa kwa `-img`, `images=True`, au bila kichujio cha aina ya maudhui, chombo kinathibitisha usanidi wa Vision kabla ya kutafsiri kuanza.

## Seti nyingi za vyeti

Tabaka la usanidi linaunga mkono seti nyingi za vyeti kwa kuongeza nambari ya mwisho (suffix) kwa vigezo vyenye index sawa:

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

Kila seti lazima iwe kamili. Ukaguzi wa afya huchagua seti inayofanya kazi kabla ya kutafsiri kuendelea.

OpenAI na Anthropic zinaunga mkono desturi ile ile ya suffix. Weka kila kigezo katika seti ya vyeti kwenye suffix ile ile, ikiwa ni pamoja na thamani za hiari kama `OPENAI_BASE_URL_1` au `ANTHROPIC_BASE_URL_1`.

## Mahitaji ya amri

| Amri au API | LLM inahitajika | Vision inahitajika | Maelezo |
| --- | --- | --- | --- |
| `translate -md` | Ndiyo | Hapana | Inatafsiri Markdown tu. |
| `translate -nb` | Ndiyo | Hapana | Inatafsiri daftari tu. |
| `translate -img` | Ndiyo | Ndiyo | Inatafsiri picha tu. |
| `translate` bila vigezo vya aina | Ndiyo | Ndiyo | Hali ya chaguo-msingi inajumuisha Markdown, notebooks, na picha. |
| `evaluate` | Ndiyo | Hapana | Inatumia tathmini ya LLM isipokuwa `--fast` imechaguliwa. |
| `migrate-links` | Hapana | Hapana | Inafanya uhamishaji wa viungo vya ndani bila wito kwa wasambazaji. |
| `co-op-review` | Hapana | Hapana | Inaendesha ukaguzi wa muundo wa tafsiri unaoamuliwa, upya wa maudhui (freshness), Markdown, daftari, na ukaguzi wa viungo vya ndani. |
| `run_translation(markdown=True)` | Ndiyo | Hapana | Kutafsiri Markdown kwa programu. |
| `run_translation(images=True)` | Ndiyo | Ndiyo | Kutafsiri picha kwa programu. |
| `run_review(...)` | Hapana | Hapana | Ukaguzi unaoamuliwa kwa programu. |

## Saraka za pato

Pato la tafsiri ya maandishi (chaguo-msingi):

```text
translations/<language-code>/<source-relative-path>
```

Pato la picha zilizotafsiriwa (chaguo-msingi):

```text
translated_images/<language-code>/<source-relative-path>
```

API ya Python inaweza kubadilisha saraka hizi kwa `translations_dir` na `image_dir`.