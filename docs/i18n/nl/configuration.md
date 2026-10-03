# Configuratie

Co-op Translator vereist één taalmodelprovider. Voor beeldvertaling is daarnaast Azure AI Vision vereist.

Configuration wordt gelezen uit omgevingsvariabelen. Voor lokale projecten plaats je ze in een `.env` bestand in de projectroot.

Voor het instellen van Azure-resources, zie [Azure AI-configuratie](azure-ai-setup.md).

## Lokale runtime-instelling

Gebruik een virtuele omgeving voordat je de CLI lokaal uitvoert. Co-op Translator ondersteunt Python 3.11 tot en met 3.14.

Voor gewoon CLI-gebruik, installeer het gepubliceerde pakket binnen een virtuele omgeving:

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

### Repository-ontwikkeling

Voor ontwikkeling van de repository, installeer in plaats daarvan de afhankelijkheden vanuit de projectroot:

```bash
poetry install
poetry run translate --help
```

Nadat de CLI beschikbaar is, configureer je één taalmodelprovider in `.env`.

## Providerselectie

Het hulpmiddel detecteert providers automatisch in de volgende volgorde:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Vertaling vereist provider-referenties, behalve voor previews zoals `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, en `run_review` zijn deterministische onderhoudsoperaties en vereisen geen provider-referenties.

## Modelclient-backend

Vanaf Co-op Translator 0.22.0 gebruiken Azure OpenAI, OpenAI en Anthropic standaard Microsoft Agent Framework. Er is geen backend-instelling nodig voor normaal gebruik.

Semantic Kernel blijft tijdelijk beschikbaar voor compatibiliteit. Om het expliciet te selecteren, stel in:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Het gebruik van Semantic Kernel geeft een verouderingswaarschuwing. Het pakket is van plan om Semantic Kernel in 0.23.0 naar een optionele afhankelijkheid te verplaatsen en de integratie in 0.24.0 te verwijderen, afhankelijk van compatibiliteitsresultaten en gebruikersfeedback. Anthropic vereist `agent-framework`; het expliciet selecteren van `semantic-kernel` met Anthropic faalt met een configuratiefout. Ongeldige waarden resulteren in fouten tijdens de initialisatie van de provider-ondersteunde vertaler in plaats van stilletjes terug te vallen. Volg de uitrol en rapporteer blokkades in [GitHub-issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Gebruik Azure OpenAI wanneer je model is uitgerold in Azure AI Foundry of Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

De verbindingscontrole gebruikt de endpoint, API-sleutel, API-versie en deploymentnaam voordat de vertaling begint.

## OpenAI

Gebruik OpenAI wanneer je direct de OpenAI-API aanroept.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` is vereist omdat de vertaler een expliciet chatmodel nodig heeft voor API-aanroepen.

Laat `OPENAI_ORG_ID` en `OPENAI_BASE_URL` leeg in de standaardconfiguratie. Voeg een organisatie-ID alleen toe als je account er een nodig heeft, of een base URL alleen bij gebruik van een aangepast endpoint. Kopieer geen voorbeeldwaarden voor optionele instellingen.

## Anthropic Claude

Gebruik Anthropic wanneer je direct de Claude-API aanroept. Maak een [Anthropic API-sleutel](https://platform.claude.com/docs/en/get-started) en kies een ondersteunde [Claude-model-ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` en `ANTHROPIC_MODEL` zijn vereist. Je hoeft `CO_OP_TRANSLATOR_MODEL_CLIENT` niet in te stellen; Agent Framework is de standaardbackend.

Laat `ANTHROPIC_BASE_URL` leeg voor de Anthropic-API. Stel het alleen in bij gebruik van een aangepast endpoint.

`ANTHROPIC_MAX_TOKENS` heeft als standaard `8192`, wat ruimte laat voor token-rijke scripts zoals Meitei Mayek. Verlaag het als je model of een Anthropic-compatibel endpoint uitvoer daaronder limiteert.

## Azure AI Vision

Beeldvertaling vereist Azure AI Vision zodat het hulpmiddel tekst uit afbeeldingen kan extraheren voordat het geconfigureerde taalmodel het vertaalt. Anthropic kan de geëxtraheerde tekst vertalen net als Azure OpenAI of OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Als beeldvertaling is geselecteerd met `-img`, `images=True`, of geen content-typefilter, valideert het hulpmiddel de Vision-configuratie voordat de vertaling start.

## Meerdere referentiesets

De configuratielaag ondersteunt meerdere referentiesets door variabelen te voorzien van hetzelfde indexachtervoegsel:

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

Elke set moet compleet zijn. De gezondheidscontrole selecteert een werkende set voordat de vertaling doorgaat.

OpenAI en Anthropic ondersteunen dezelfde suffixconventie. Houd elke variabele in een referentieset op hetzelfde achtervoegsel, inclusief optionele waarden zoals `OPENAI_BASE_URL_1` of `ANTHROPIC_BASE_URL_1`.

## Vereisten voor commando's

| Commando of API | LLM vereist | Vision vereist | Opmerkingen |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nee | Vertaalt alleen Markdown. |
| `translate -nb` | Ja | Nee | Vertaalt alleen notebooks. |
| `translate -img` | Ja | Ja | Vertaalt alleen afbeeldingen. |
| `translate` with no type flags | Ja | Ja | Standaardmodus bevat Markdown, notebooks en afbeeldingen. |
| `evaluate` | Ja | Nee | Gebruikt LLM-evaluatie tenzij `--fast` is geselecteerd. |
| `migrate-links` | Nee | Nee | Voert lokale linkmigratie uit zonder provider-aanroepen. |
| `co-op-review` | Nee | Nee | Voert deterministische controles uit voor vertaalstructuur, actualiteit, Markdown, notebook en lokale links. |
| `run_translation(markdown=True)` | Ja | Nee | Programmeerbare Markdown-vertaling. |
| `run_translation(images=True)` | Ja | Ja | Programmeerbare beeldvertaling. |
| `run_review(...)` | Nee | Nee | Programmeerbare deterministische review. |

## Uitvoermappen

Standaard uitvoer voor tekstvertaling:

```text
translations/<language-code>/<source-relative-path>
```

Standaard uitvoer voor vertaalde afbeeldingen:

```text
translated_images/<language-code>/<source-relative-path>
```

De Python-API kan deze mappen overschrijven met `translations_dir` en `image_dir`.