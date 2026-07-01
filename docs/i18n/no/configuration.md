# Konfigurasjon

Co-op Translator krever en språkmodell-leverandør. Bildeoversettelse krever i tillegg Azure AI Vision.

Konfigurasjonen leses fra miljøvariabler. For lokale prosjekter, plasser dem i en `.env`-fil i prosjektets rotmappe.

For oppsett av Azure-ressurser, se [Azure AI-oppsett](azure-ai-setup.md).

## Lokal runtime-oppsett

Bruk et virtuelt miljø før du kjører CLI lokalt. Co-op Translator støtter Python 3.10 til 3.12.

For vanlig bruk av CLI, installer den publiserte pakken inne i et virtuelt miljø:

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

For utvikling av repositoryet, installer avhengigheter fra prosjektets rot i stedet:

```bash
poetry install
poetry run translate --help
```

Etter at CLI er tilgjengelig, konfigurer en språkmodell-leverandør i `.env`.

## Valg av leverandør

Verktøyet oppdager automatisk leverandører i denne rekkefølgen:

1. Azure OpenAI
2. OpenAI

Hvis ingen av leverandørene er konfigurert, vil `translate`, `evaluate`, `migrate-links` og `run_translation` feile under konfigurasjonskontroller. `co-op-review` og `run_review` er deterministiske vedlikeholdssjekker og krever ikke leverandør-legitimasjon.

## Azure OpenAI

Bruk Azure OpenAI når modellen din er distribuert i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Tilkoblingssjekken bruker endepunktet, API-nøkkelen, API-versjonen og distribusjonsnavnet før oversettelsen starter.

## OpenAI

Bruk OpenAI når du kaller OpenAI API direkte.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # valgfri
OPENAI_BASE_URL="..."        # valgfri
```

`OPENAI_CHAT_MODEL_ID` er påkrevd fordi oversetteren trenger en eksplisitt chatmodell for API-kall.

## Azure AI Vision

Bildeoversettelse krever Azure AI Vision slik at verktøyet kan hente ut tekst fra bilder før teksten oversettes.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Hvis bildeoversettelse er valgt med `-img`, `images=True`, eller hvis det ikke er noe innholdstypefilter, validerer verktøyet Vision-konfigurasjonen før oversettelsen starter.

## Flere legitimasjonssett

Konfigurasjonslaget støtter flere sett med legitimasjon ved å legge samme indeks som suffiks til variablene:

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

## Kommandokrav

| Kommando eller API | LLM nødvendig | Vision nødvendig | Notater |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nei | Oversetter bare Markdown. |
| `translate -nb` | Ja | Nei | Oversetter bare notatbøker. |
| `translate -img` | Ja | Ja | Oversetter bare bilder. |
| `translate` with no type flags | Ja | Ja | Standardmodus inkluderer Markdown, notatbøker og bilder. |
| `evaluate` | Ja | Nei | Bruker LLM-evaluering med mindre `--fast` er valgt. |
| `migrate-links` | Ja | Nei | Utfører lenkemigrering, men kjører fortsatt delte konfigurasjonskontroller. |
| `co-op-review` | Nei | Nei | Kjører deterministiske sjekker for oversettelsesstruktur, ferskhet, Markdown, notatbok og lokale lenker. |
| `run_translation(markdown=True)` | Ja | Nei | Programmatisk Markdown-oversettelse. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk bildeoversettelse. |
| `run_review(...)` | Nei | Nei | Programmatisk deterministisk gjennomgang. |

## Utdata-kataloger

Standard utdata for tekstoversettelse:

```text
translations/<language-code>/<source-relative-path>
```

Standard utdata for oversatte bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-APIen kan overstyre disse katalogene med `translations_dir` og `image_dir`.