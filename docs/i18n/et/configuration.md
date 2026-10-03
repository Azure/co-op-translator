# Konfiguratsioon

Co-op Translator nõuab ühte keelemudeli pakkujat. Pildi tõlkimine nõuab lisaks Azure AI Visioni.

Konfiguratsioon loetakse keskkonnamuutujatest. Kohalike projektide puhul paigutage need projekti juurkausta faili `.env`.

Azure ressursi seadistamiseks vaadake [Azure AI seadistamine](azure-ai-setup.md).

## Kohaliku käituskeskkonna seadistamine

Enne CLI lokaalsel käivitamist kasutage virtuaalset keskkonda. Co-op Translator toetab Python 3.11 kuni 3.14.

Tavapärase CLI kasutuse jaoks installige avaldatud pakett virtuaalsesse keskkonda:

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

### Hoidla arendus

Hoidla arendamiseks installige sõltuvused projekti juurkataloogist:

```bash
poetry install
poetry run translate --help
```

Pärast CLI kättesaadavaks muutumist seadistage üks keelemudeli pakkuja faili `.env`.

## Pakkuja valik

Tööriist tuvastab pakkujad automaatselt selles järjekorras:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Tõlkimiseks on vaja pakkuja mandaate, välja arvatud eelvaated nagu `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` ja `run_review` on deterministlikud hooldusoperatsioonid ega vaja pakkuja mandaate.

## Mudeli kliendi taustsüsteem

Alates Co-op Translator versioonist 0.22.0 kasutavad Azure OpenAI, OpenAI ja Anthropic vaikimisi Microsoft Agent Frameworki. Tavapäraseks kasutamiseks pole backend-seadistust vaja.

Semantic Kernel jääb ajutiselt ühilduvuse huvides kättesaadavaks. Selle selgesõnaliseks valimiseks määrake:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kerneli kasutamisel kuvatakse deprecatsioonihoiatus. Plaanis on teha Semantic Kernelist valikuline sõltuvus versioonis 0.23.0 ja eemaldada integratsioon versioonis 0.24.0, sõltuvalt ühilduvuse tulemustest ja kasutajate tagasisidest. Anthropic nõuab `agent-framework`i; `semantic-kernel`i otsene valimine Anthropicuga ebaõnnestub konfiguratsiooniveaga. Kehtetud väärtused nurjuvad pakkujatoega tõlkija käivitamisel ning ei lange vaikides tagasi. Jälgige rakendamist ja teatage takistustest [GitHubi issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Kasutage Azure OpenAI-d, kui teie mudel on juurutatud Azure AI Foundrysse või Azure OpenAI teenusesse.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ühenduse kontroll kasutab enne tõlkimise alustamist lõpp-punkti, API võtit, API versiooni ja juurutuse nime.

## OpenAI

Kasutage OpenAI-d, kui kutsute OpenAI API-d otse.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` on nõutud, kuna tõlkija vajab API-kõnede jaoks selgesõnalist vestlusmudelit.

Jätke `OPENAI_ORG_ID` ja `OPENAI_BASE_URL` vaikekonfiguratsiooni jaoks määramata. Lisage organisatsiooni ID ainult siis, kui teie konto seda vajab, või baas-URL ainult kohandatud lõpp-punkti kasutamisel. Ärge kopeerige kohatäitja väärtusi valikuliste seadete jaoks.

## Anthropic Claude

Kasutage Anthropicut, kui kutsute Claude API-d otse. Looge [Anthropic API-võti](https://platform.claude.com/docs/en/get-started) ja valige toetatud [Claude mudeli ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ja `ANTHROPIC_MODEL` on nõutud. Te ei pea seadistama `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework on vaikimisi taustsüsteem.

Jätke `ANTHROPIC_BASE_URL` Anthropic API puhul määramata. Määrake see ainult kohandatud lõpp-punkti kasutamisel.

`ANTHROPIC_MAX_TOKENS` vaikimisi väärtus on `8192`, mis jätab ruumi tokenite-rikkale skriptile nagu Meitei Mayek. Alandage seda, kui teie mudel või Anthropic-ühilduv lõpp-punkt seab väljundile madalamad piirid.

## Azure AI Vision

Pildi tõlkimiseks on vaja Azure AI Visioni, et tööriist saaks piltidelt teksti ekstraheerida enne, kui konfigureeritud keelemudel selle tõlgib. Anthropic saab ekstraheeritud teksti tõlkida samamoodi nagu Azure OpenAI või OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Kui pildi tõlkimine valitakse `-img`, `images=True` või ilma sisu tüübi filtrita, siis tööriist valideerib Visioni konfiguratsiooni enne tõlkimise alustamist.

## Mitme mandaadikomplekti tugi

Konfiguratsioonikiht toetab mitut mandaadikomplekti, lisades muutujatele sama indeksi sufiksina:

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

Iga komplekt peab olema täielik. Tervisekontroll valib töötava komplekti enne tõlkimise jätkamist.

OpenAI ja Anthropic toetavad sama sufiksikonventsiooni. Hoidke iga mandaadikomplekti kõik muutujad samal sufiksil, kaasa arvatud valikulised väärtused nagu `OPENAI_BASE_URL_1` või `ANTHROPIC_BASE_URL_1`.

## Käskude nõuded

| Käsk või API | LLM nõutud | Vision nõutud | Märkused |
| --- | --- | --- | --- |
| `translate -md` | Jah | Ei | Tõlgib ainult Markdowni. |
| `translate -nb` | Jah | Ei | Tõlgib ainult notebooke. |
| `translate -img` | Jah | Jah | Tõlgib ainult pilte. |
| `translate` ilma tüübi lipikuteta | Jah | Jah | Vaikerežiim hõlmab Markdowni, notebooke ja pilte. |
| `evaluate` | Jah | Ei | Kasutab LLM-i hindamist, välja arvatud kui on valitud `--fast`. |
| `migrate-links` | Ei | Ei | Teostab kohaliku linkide migratsiooni ilma pakkujakõnedeta. |
| `co-op-review` | Ei | Ei | Käivitab deterministlikud tõlke struktuuri, värskuse, Markdowni, notebookide ja kohalike linkide kontrollid. |
| `run_translation(markdown=True)` | Jah | Ei | Programmaatiline Markdowni tõlkimine. |
| `run_translation(images=True)` | Jah | Jah | Programmaatiline piltide tõlkimine. |
| `run_review(...)` | Ei | Ei | Programmaatiline deterministlik ülevaatus. |

## Väljundkataloogid

Vaikimisi tekstitõlke väljund:

```text
translations/<language-code>/<source-relative-path>
```

Vaikimisi tõlgitud piltide väljund:

```text
translated_images/<language-code>/<source-relative-path>
```

Pythoni API saab neid katalooge üle kirjutada parameetritega `translations_dir` ja `image_dir`.