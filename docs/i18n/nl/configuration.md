# Configuratie

Co-op Translator vereist één provider voor taalmodellen. Beeldvertaling vereist daarnaast Azure AI Vision.

Configuratie wordt gelezen uit omgevingsvariabelen. Voor lokale projecten, plaats ze in een `.env` bestand in de projectroot.

Voor Azure resource setup, zie [Azure AI Setup](azure-ai-setup.md).

## Lokale runtime-configuratie

Gebruik een virtuele omgeving voordat je de CLI lokaal uitvoert. Co-op Translator ondersteunt Python 3.10 tot en met 3.12.

Voor normaal CLI-gebruik, installeer het gepubliceerde pakket binnen een virtuele omgeving:

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

Voor repository-ontwikkeling, installeer in plaats daarvan afhankelijkheden vanuit de projectroot:

```bash
poetry install
poetry run translate --help
```

Nadat de CLI beschikbaar is, configureer je één provider voor taalmodellen in `.env`.

## Providerselectie

Het hulpmiddel detecteert automatisch providers in deze volgorde:

1. Azure OpenAI
2. OpenAI

Als geen van beide providers is geconfigureerd, falen `translate`, `evaluate`, `migrate-links`, en `run_translation` tijdens de configuratiecontroles. `co-op-review` en `run_review` zijn deterministische onderhoudscontroles en vereisen geen providerreferenties.

## Azure OpenAI

Gebruik Azure OpenAI wanneer je model is gedeployed in Azure AI Foundry of Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

De connectiviteitscontrole gebruikt het eindpunt, de API-sleutel, API-versie en de deploymentnaam voordat de vertaling begint.

## OpenAI

Gebruik OpenAI wanneer je rechtstreeks de OpenAI API aanroept.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # optioneel
OPENAI_BASE_URL="..."        # optioneel
```

`OPENAI_CHAT_MODEL_ID` is vereist omdat de vertaler een expliciet chatmodel nodig heeft voor API-aanroepen.

## Azure AI Vision

Beeldvertaling vereist Azure AI Vision zodat het hulpmiddel tekst uit afbeeldingen kan extraheren voordat het die vertaalt.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Als beeldvertaling is geselecteerd met `-img`, `images=True`, of geen content-type filter, valideert het hulpmiddel de Vision-configuratie voordat de vertaling begint.

## Meerdere sets met referenties

De configuratielaag ondersteunt meerdere sets met referenties door variabelen van hetzelfde achtervoegsel (index) te voorzien:

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

## Vereisten per commando

| Commando of API | LLM vereist | Vision vereist | Opmerkingen |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nee | Vertaalt alleen Markdown. |
| `translate -nb` | Ja | Nee | Vertaalt alleen notebooks. |
| `translate -img` | Ja | Ja | Vertaalt alleen afbeeldingen. |
| `translate` with no type flags | Ja | Ja | De standaardmodus omvat Markdown, notebooks en afbeeldingen. |
| `evaluate` | Ja | Nee | Gebruikt LLM-evaluatie tenzij `--fast` is geselecteerd. |
| `migrate-links` | Ja | Nee | Voert linkmigratie uit, maar voert nog steeds gedeelde configuratiecontroles uit. |
| `co-op-review` | Nee | Nee | Voert deterministische controles uit op vertaalkader, actualiteit, Markdown, notebooks en lokale links. |
| `run_translation(markdown=True)` | Ja | Nee | Programmatische Markdown-vertaling. |
| `run_translation(images=True)` | Ja | Ja | Programmatische beeldvertaling. |
| `run_review(...)` | Nee | Nee | Programmatische deterministische controle. |

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