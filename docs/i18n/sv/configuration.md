# Konfiguration

Co-op Translator kräver en språkmodellleverantör. Bildöversättning kräver dessutom Azure AI Vision.

Konfiguration läses från miljövariabler. För lokala projekt, placera dem i en `.env`-fil i projektets rot.

För Azure-resurser, se [Azure AI-inställning](azure-ai-setup.md).

## Lokal körmiljö

Använd en virtuell miljö innan du kör CLI lokalt. Co-op Translator stöder Python 3.10 till 3.12.

För normal CLI-användning, installera det publicerade paketet i en virtuell miljö:

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

För utveckling av repositoryt, installera beroenden från projektets rot istället:

```bash
poetry install
poetry run translate --help
```

Efter att CLI är tillgänglig, konfigurera en språkmodellleverantör i `.env`.

## Val av leverantör

Verktyget autodetekterar leverantörer i följande ordning:

1. Azure OpenAI
2. OpenAI

Om ingen av leverantörerna är konfigurerad misslyckas `translate`, `evaluate`, `migrate-links`, och `run_translation` under konfigurationskontroller. `co-op-review` och `run_review` är deterministiska underhållskontroller och kräver inga autentiseringsuppgifter.

## Azure OpenAI

Använd Azure OpenAI när din modell är distribuerad i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Hälsokontrollen använder slutpunkt, API-nyckel, API-version och driftsättningsnamn innan översättningen påbörjas.

## OpenAI

Använd OpenAI när du anropar OpenAI API direkt.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # valfritt
OPENAI_BASE_URL="..."        # valfritt
```

`OPENAI_CHAT_MODEL_ID` krävs eftersom översättaren behöver en explicit chatmodell för API-anrop.

## Azure AI Vision

Bildöversättning kräver Azure AI Vision så verktyget kan extrahera text från bilder innan den översätts.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Om bildöversättning väljs med `-img`, `images=True`, eller inget content-type-filter, validerar verktyget Vision-konfigurationen innan översättningen startar.

## Flera uppsättningar med autentiseringsuppgifter

Konfigurationslagret stöder flera uppsättningar med autentiseringsuppgifter genom att lägga till samma index som suffix på variablerna:

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

Varje uppsättning måste vara komplett. Hälsokontrollen väljer en fungerande uppsättning innan översättningen fortsätter.

## Krav per kommando

| Kommando eller API | LLM krävs | Vision krävs | Anteckningar |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nej | Översätter endast Markdown. |
| `translate -nb` | Ja | Nej | Översätter endast notebooks. |
| `translate -img` | Ja | Ja | Översätter endast bilder. |
| `translate` with no type flags | Ja | Ja | Standardläge inkluderar Markdown, notebooks och bilder. |
| `evaluate` | Ja | Nej | Använder LLM-utvärdering om inte `--fast` är valt. |
| `migrate-links` | Ja | Nej | Utför länk-migrering, men kör fortfarande delade konfigurationskontroller. |
| `co-op-review` | Nej | Nej | Kör deterministiska kontroller för översättningsstruktur, aktualitet, Markdown, notebook och lokala länkar. |
| `run_translation(markdown=True)` | Ja | Nej | Programmatisk Markdown-översättning. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk bildöversättning. |
| `run_review(...)` | Nej | Nej | Programmatisk deterministisk granskning. |

## Output directories

Standardutdata för textöversättning:

```text
translations/<language-code>/<source-relative-path>
```

Standardutdata för översatta bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API:t kan åsidosätta dessa kataloger med `translations_dir` och `image_dir`.