# Konfiguration

Co-op Translator kræver én sprogmodeludbyder. Billedoversættelse kræver desuden Azure AI Vision.

Konfiguration læses fra miljøvariabler. For lokale projekter, placer dem i en `.env`-fil i projektets rodmappe.

For opsætning af Azure-ressourcer, se [Azure AI-opsætning](azure-ai-setup.md).

## Lokal runtime-opsætning

Brug et virtuelt miljø, før du kører CLI'en lokalt. Co-op Translator understøtter Python 3.11 til 3.14.

For normal CLI-brug, installer den publicerede pakke i et virtuelt miljø:

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

### Repository-udvikling

For udvikling af repositoryet, installer afhængigheder fra projektets rod i stedet:

```bash
poetry install
poetry run translate --help
```

Når CLI'en er tilgængelig, konfigurer én sprogmodeludbyder i `.env`.

## Valg af udbyder

Værktøjet registrerer automatisk udbydere i denne rækkefølge:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Oversættelse kræver udbyderlegitimationsoplysninger, undtagen for forhåndsvisninger som `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, og `run_review` er deterministiske vedligeholdelsesoperationer og kræver ikke udbyderlegitimationsoplysninger.

## Modelklient-backend

Fra og med Co-op Translator 0.22.0 bruger Azure OpenAI, OpenAI og Anthropic Microsoft Agent Framework som standard. Der kræves ingen backend-indstilling til normal brug.

Semantic Kernel er midlertidigt stadig tilgængelig af hensyn til kompatibilitet. For at vælge det eksplicit, angiv:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Brug af Semantic Kernel udløser en deprecationsadvarsel. Pakken planlægger at flytte Semantic Kernel til en valgfri afhængighed i 0.23.0 og fjerne integrationen i 0.24.0, afhængigt af kompatibilitetsresultater og brugertilbagemeldinger. Anthropic kræver `agent-framework`; eksplicit valg af `semantic-kernel` med Anthropic mislykkes med en konfigurationsfejl. Ugyldige værdier fejler under initialiseringen af oversætteren med udbyder i stedet for at falde tilbage stiltiende. Følg udrulningen og rapporter blokeringer i [GitHub-issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Brug Azure OpenAI, når din model er udrullet i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Forbindelsestjekket bruger endpoint, API-nøgle, API-version og deploymentsnavn, før oversættelsen begynder.

## OpenAI

Brug OpenAI, når du kalder OpenAI-API'et direkte.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` er påkrævet, fordi oversætteren har brug for en eksplicit chatmodel til API-kald.

Lad `OPENAI_ORG_ID` og `OPENAI_BASE_URL` stå udefineret for standardopsætningen. Tilføj kun en organisations-id, hvis din konto kræver det, eller en base-URL kun når du bruger et brugerdefineret endpoint. Kopier ikke pladsholderværdier for valgfrie indstillinger.

## Anthropic Claude

Brug Anthropic, når du kalder Claude-API'et direkte. Opret en [Anthropic API-nøgle](https://platform.claude.com/docs/en/get-started) og vælg en understøttet [Claude-model-ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` og `ANTHROPIC_MODEL` er påkrævede. Du behøver ikke at sætte `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework er standardbackend.

Lad `ANTHROPIC_BASE_URL` stå udefineret for Anthropic-API'en. Sæt den kun, når du bruger et brugerdefineret endpoint.

`ANTHROPIC_MAX_TOKENS` har standardværdien `8192`, hvilket giver plads til token-tætte skriftsystemer som Meitei Mayek. Sænk den, hvis din model eller Anthropic-kompatible endpoint begrænser outputtet under det.

## Azure AI Vision

Billedoversættelse kræver Azure AI Vision, så værktøjet kan udtrække tekst fra billeder, før den konfigurerede sprogmodel oversætter den. Anthropic kan oversætte den udtrukne tekst på samme måde som Azure OpenAI eller OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Hvis billedoversættelse vælges med `-img`, `images=True` eller uden content-type-filter, validerer værktøjet Vision-konfigurationen, før oversættelsen starter.

## Flere legitimationssæt

Konfigurationslaget understøtter flere legitimationssæt ved at tilføje suffikser til variablerne med samme indeks:

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

Hvert sæt skal være komplet. Sundhedstjekket vælger et fungerende sæt, før oversættelsen fortsætter.

OpenAI og Anthropic understøtter samme suffiks-konvention. Hold alle variabler i et legitimationssæt på samme suffiks, inklusive valgfrie værdier som `OPENAI_BASE_URL_1` eller `ANTHROPIC_BASE_URL_1`.

## Krav til kommandoer

| Kommando eller API | Kræver LLM | Kræver Vision | Noter |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nej | Oversætter kun Markdown. |
| `translate -nb` | Ja | Nej | Oversætter kun notebooks. |
| `translate -img` | Ja | Ja | Oversætter kun billeder. |
| `translate` uden type-flags | Ja | Ja | Standardtilstand inkluderer Markdown, notebooks og billeder. |
| `evaluate` | Ja | Nej | Bruger LLM-evaluering medmindre `--fast` vælges. |
| `migrate-links` | Nej | Nej | Udfører lokal link-migrering uden opkald til udbyder. |
| `co-op-review` | Nej | Nej | Kører deterministiske tjek af oversættelsesstruktur, friskhed, Markdown, notebook og lokale links. |
| `run_translation(markdown=True)` | Ja | Nej | Programmatisk Markdown-oversættelse. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk billedoversættelse. |
| `run_review(...)` | Nej | Nej | Programmatisk deterministisk gennemgang. |

## Output-mapper

Standarduddata for tekstoversættelse:

```text
translations/<language-code>/<source-relative-path>
```

Standarduddata for oversatte billeder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API'en kan tilsidesætte disse mapper med `translations_dir` og `image_dir`.