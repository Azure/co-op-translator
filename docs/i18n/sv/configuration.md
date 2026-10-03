# Konfiguration

Co-op Translator kräver en språkmodellsleverantör. Bildöversättning kräver dessutom Azure AI Vision.

Konfigurationen läses från miljövariabler. För lokala projekt, placera dem i en `.env`-fil i projektets rot.

För att konfigurera Azure-resurser, se [Azure AI-inställning](azure-ai-setup.md).

## Lokal runtime-inställning

Använd en virtuell miljö innan du kör CLI lokalt. Co-op Translator stödjer Python 3.11 till 3.14.

För normal CLI-användning, installera det publicerade paketet i en virtuell miljö:

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

### Repository-utveckling

För repository-utveckling, installera beroenden från projektets rot istället:

```bash
poetry install
poetry run translate --help
```

När CLI:t är tillgängligt, konfigurera en språkmodellsleverantör i `.env`.

## Val av leverantör

Verktyget upptäcker leverantörer automatiskt i följande ordning:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Översättning kräver autentiseringsuppgifter för leverantören, utom för förhandsgranskningar som `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, och `run_review` är deterministiska underhållsoperationer och kräver inte leverantörsuppgifter.

## Modellklient-backend

Från och med Co-op Translator 0.22.0 använder Azure OpenAI, OpenAI och Anthropic Microsoft Agent Framework som standard. Ingen backend-inställning krävs för normalt bruk.

Semantic Kernel finns kvar tillfälligt för kompatibilitet. För att välja det uttryckligen, ange:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Användning av Semantic Kernel ger en varning om föråldring. Paketet planeras att göra Semantic Kernel till ett valfritt beroende i 0.23.0 och att ta bort integrationen i 0.24.0, beroende på kompatibilitetsresultat och användarfeedback. Anthropic kräver `agent-framework`; att uttryckligen välja `semantic-kernel` med Anthropic misslyckas med ett konfigurationsfel. Ogiltiga värden misslyckas under initialiseringen av leverantörsbackad översättare istället för att tyst falla tillbaka. Följ utrullningen och rapportera blockerare i [GitHub-ärende #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Använd Azure OpenAI när din modell är distribuerad i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Anslutningskontrollen använder endpunkt, API-nyckel, API-version och distributionsnamn innan översättningen börjar.

## OpenAI

Använd OpenAI när du anropar OpenAI:s API direkt.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` krävs eftersom översättaren behöver en explicit chattmodell för API-anrop.

Lämna `OPENAI_ORG_ID` och `OPENAI_BASE_URL` oinställda för standardkonfigurationen. Lägg till en organisations-ID endast om ditt konto behöver en, eller en bas-URL endast när du använder en anpassad slutpunkt. Kopiera inte platshållarvärden för valfria inställningar.

## Anthropic Claude

Använd Anthropic när du anropar Claude API direkt. Skapa en [Anthropic API-nyckel](https://platform.claude.com/docs/en/get-started) och välj ett stödjat [Claude-modell-ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` och `ANTHROPIC_MODEL` krävs. Du behöver inte ange `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework är standardbackend.

Lämna `ANTHROPIC_BASE_URL` oinställd för Anthropic API. Ange den endast när du använder en anpassad slutpunkt.

`ANTHROPIC_MAX_TOKENS` är som standard `8192`, vilket lämnar utrymme för tokentäta skript som Meitei Mayek. Sänk det om din modell eller Anthropic-kompatibla slutpunkt begränsar utdata till mindre än så.

## Azure AI Vision

Bildöversättning kräver Azure AI Vision så att verktyget kan extrahera text från bilder innan den konfigurerade språkmodellen översätter den. Anthropic kan översätta den extraherade texten på samma sätt som Azure OpenAI eller OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Om bildöversättning väljs med `-img`, `images=True` eller utan innehållstypsfilter, validerar verktyget Vision-konfigurationen innan översättningen börjar.

## Flera uppsättningar autentiseringsuppgifter

Konfigurationslagret stöder flera uppsättningar autentiseringsuppgifter genom att lägga till samma index som suffix på variabler:

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

Varje uppsättning måste vara komplett. Hälsokontrollen väljer en fungerande uppsättning innan översättning fortsätter.

OpenAI och Anthropic stödjer samma suffixkonvention. Håll varje variabel i en autentiseringsuppsättning på samma suffix, inklusive valfria värden som `OPENAI_BASE_URL_1` eller `ANTHROPIC_BASE_URL_1`.

## Kommandokrav

| Kommando eller API | LLM krävs | Vision krävs | Anteckningar |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nej | Översätter endast Markdown. |
| `translate -nb` | Ja | Nej | Översätter endast notebooks. |
| `translate -img` | Ja | Ja | Översätter endast bilder. |
| `translate` utan typflaggor | Ja | Ja | Standardläge inkluderar Markdown, notebooks och bilder. |
| `evaluate` | Ja | Nej | Använder LLM-utvärdering om inte `--fast` är valt. |
| `migrate-links` | Nej | Nej | Utför lokal länkmigrering utan leverantörsanrop. |
| `co-op-review` | Nej | Nej | Kör deterministiska kontroller av översättningsstruktur, färskhet, Markdown, notebook och lokala länkar. |
| `run_translation(markdown=True)` | Ja | Nej | Programmatisk Markdown-översättning. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk bildöversättning. |
| `run_review(...)` | Nej | Nej | Programmatisk deterministisk granskning. |

## Utdata-kataloger

Standardutdata för textöversättning:

```text
translations/<language-code>/<source-relative-path>
```

Standardutdata för översatta bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API:t kan åsidosätta dessa kataloger med `translations_dir` och `image_dir`.