# Konfigurasjon

Co-op Translator krever en språkmodell-leverandør. Bildetranslasjon krever i tillegg Azure AI Vision.

Konfigurasjonen leses fra miljøvariabler. For lokale prosjekter, legg dem i en `.env`-fil i prosjektets rotmappe.

For oppsett av Azure-ressurser, se [Azure AI Setup](azure-ai-setup.md).

## Lokal runtime-oppsett

Bruk et virtuelt miljø før du kjører CLI lokalt. Co-op Translator støtter Python 3.11 til 3.14.

For vanlig bruk av CLI, installer den publiserte pakken i et virtuelt miljø:

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

### Repository-utvikling

For utvikling av depotet, installer avhengigheter fra prosjektets rot i stedet:

```bash
poetry install
poetry run translate --help
```

Etter at CLI er tilgjengelig, konfigurer en språkmodell-leverandør i `.env`.

## Leverandørvalg

Verktøyet oppdager automatisk leverandører i denne rekkefølgen:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Oversettelse krever leverandørlegitimasjon, unntatt for forhåndsvisninger som `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, og `run_review` er deterministiske vedlikeholdsoperasjoner og krever ikke leverandørlegitimasjon.

## Modellklient-backend

Fra og med Co-op Translator 0.22.0 bruker Azure OpenAI, OpenAI og Anthropic Microsoft Agent Framework som standard. Ingen backend-innstilling kreves for vanlig bruk.

Semantic Kernel er fortsatt midlertidig tilgjengelig for kompatibilitet. For å velge det eksplisitt, sett:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Bruk av Semantic Kernel utløser en utfasingsadvarsel. Planen er å flytte Semantic Kernel til en valgfri avhengighet i 0.23.0 og fjerne integrasjonen i 0.24.0, underlagt kompatibilitetsresultater og brukertilbakemeldinger. Anthropic krever `agent-framework`; det å velge `semantic-kernel` eksplisitt med Anthropic feiler med en konfigurasjonsfeil. Ugyldige verdier feiler under initialiseringen av leverandørstøttet oversetter i stedet for å falle tilbake stille. Følg utrullingen og rapporter blokkeringer i [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Bruk Azure OpenAI når modellen din er distribuert i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Tilkoblingskontrollen bruker endepunkt, API-nøkkel, API-versjon og distribusjonsnavn før oversettelsen starter.

## OpenAI

Bruk OpenAI når du kaller OpenAI API direkte.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` kreves fordi oversetteren trenger en eksplisitt chat-modell for API-kall.

La `OPENAI_ORG_ID` og `OPENAI_BASE_URL` stå udefinerte for standardoppsettet. Legg til et organisasjons-ID bare hvis kontoen din trenger det, eller en base-URL bare når du bruker et tilpasset endepunkt. Ikke kopier plassholderverdier for valgfrie innstillinger.

## Anthropic Claude

Bruk Anthropic når du kaller Claude API direkte. Opprett en [Anthropic API-nøkkel](https://platform.claude.com/docs/en/get-started) og velg en støttet [Claude modell-ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` og `ANTHROPIC_MODEL` er påkrevd. Du trenger ikke å sette `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework er standard backend.

La `ANTHROPIC_BASE_URL` stå udefinert for Anthropic API. Sett den kun ved bruk av et tilpasset endepunkt.

`ANTHROPIC_MAX_TOKENS` har standardverdien `8192`, som gir plass til token-tette skriftsystemer som Meitei Mayek. Senk den hvis modellen din eller Anthropic-kompatibelt endepunkt begrenser output under det.

## Azure AI Vision

Bildetranslasjon krever Azure AI Vision slik at verktøyet kan trekke ut tekst fra bilder før den konfigurerte språkmodellen oversetter den. Anthropic kan oversette den uttrukne teksten på samme måte som Azure OpenAI eller OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Hvis bildetranslasjon er valgt med `-img`, `images=True`, eller uten filter for innholdstype, validerer verktøyet Vision-konfigurasjonen før oversettelsen starter.

## Flere legitimasjonssett

Konfigurasjonslaget støtter flere legitimasjonssett ved å legge samme indeks som suffiks på variablene:

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

Hvert sett må være komplett. Helsekontrollen velger et fungerende sett før oversettelsen fortsetter.

OpenAI og Anthropic støtter samme suffiks-konvensjon. Hold alle variabler i et legitimasjonssett på samme suffiks, inkludert valgfrie verdier som `OPENAI_BASE_URL_1` eller `ANTHROPIC_BASE_URL_1`.

## Krav for kommandoer

| Kommando eller API | Krever LLM | Krever Vision | Notater |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nei | Oversetter kun Markdown. |
| `translate -nb` | Ja | Nei | Oversetter kun notatbøker. |
| `translate -img` | Ja | Ja | Oversetter kun bilder. |
| `translate` uten typeflagg | Ja | Ja | Standardmodus inkluderer Markdown, notatbøker og bilder. |
| `evaluate` | Ja | Nei | Bruker LLM-evaluering med mindre `--fast` er valgt. |
| `migrate-links` | Nei | Nei | Utfører lokal lenkemigrering uten leverandørkall. |
| `co-op-review` | Nei | Nei | Kjører deterministiske kontroller for oversettelsesstruktur, ferskhet, Markdown, notatbøker og lokale lenker. |
| `run_translation(markdown=True)` | Ja | Nei | Programmatisk Markdown-oversettelse. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk bildetranslasjon. |
| `run_review(...)` | Nei | Nei | Programmatisk deterministisk gjennomgang. |

## Utdata-kataloger

Standard utdata for tekstoversettelse:

```text
translations/<language-code>/<source-relative-path>
```

Standardutdata for oversatte bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API-en kan overstyre disse katalogene med `translations_dir` og `image_dir`.