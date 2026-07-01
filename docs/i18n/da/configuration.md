# Konfiguration

Co-op Translator kræver en sprogmodeludbyder. Billedoversættelse kræver derudover Azure AI Vision.

Konfiguration læses fra miljøvariabler. For lokale projekter, placer dem i en `.env`-fil i projektets rodmappe.

For opsætning af Azure-ressourcer, se [Azure AI-opsætning](azure-ai-setup.md).

## Lokal runtime-opsætning

Brug et virtuelt miljø, før du kører CLI lokalt. Co-op Translator understøtter Python 3.10 til 3.12.

For normal CLI-brug, installer den publicerede pakke i et virtuelt miljø:

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

For udvikling af projektet, installer afhængigheder fra projektets rod i stedet:

```bash
poetry install
poetry run translate --help
```

Efter CLI'en er tilgængelig, konfigurer en sprogmodeludbyder i `.env`.

## Valg af udbyder

Værktøjet registrerer automatisk udbydere i denne rækkefølge:

1. Azure OpenAI
2. OpenAI

Hvis ingen af udbyderne er konfigureret, fejler `translate`, `evaluate`, `migrate-links` og `run_translation` under konfigurationskontroller. `co-op-review` og `run_review` er deterministiske vedligeholdelsestjek og kræver ikke udbyder-legitimationsoplysninger.

## Azure OpenAI

Brug Azure OpenAI, når din model er implementeret i Azure AI Foundry eller Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Forbindelsestjekket bruger endepunkt, API-nøgle, API-version og deploymentsnavn, før oversættelsen begynder.

## OpenAI

Brug OpenAI, når du kalder OpenAI API'en direkte.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # valgfri
OPENAI_BASE_URL="..."        # valgfri
```

`OPENAI_CHAT_MODEL_ID` er påkrævet, fordi oversætteren har brug for en eksplicit chatmodel til API-opkald.

## Azure AI Vision

Billedoversættelse kræver Azure AI Vision, så værktøjet kan udtrække tekst fra billeder, før den oversættes.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Hvis billedoversættelse er valgt med `-img`, `images=True` eller uden indholdstypefilter, validerer værktøjet Vision-konfigurationen, før oversættelsen starter.

## Flere sæt legitimationsoplysninger

Konfigurationslaget understøtter flere legitimationssæt ved at føje det samme indeks som suffiks til variablerne:

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

## Krav til kommandoer

| Kommando eller API | LLM påkrævet | Vision påkrævet | Bemærkninger |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nej | Oversætter kun Markdown. |
| `translate -nb` | Ja | Nej | Oversætter kun notebooks. |
| `translate -img` | Ja | Ja | Oversætter kun billeder. |
| `translate` uden typeflag | Ja | Ja | Standardtilstand inkluderer Markdown, notebooks og billeder. |
| `evaluate` | Ja | Nej | Bruger LLM-evaluering medmindre `--fast` er valgt. |
| `migrate-links` | Ja | Nej | Udfører linkmigrering, men kører stadig de delte konfigurationskontroller. |
| `co-op-review` | Nej | Nej | Kører deterministiske tjek af oversættelsesstruktur, friskhed, Markdown, notebooks og lokale links. |
| `run_translation(markdown=True)` | Ja | Nej | Programmatisk Markdown-oversættelse. |
| `run_translation(images=True)` | Ja | Ja | Programmatisk billedoversættelse. |
| `run_review(...)` | Nej | Nej | Programmatisk deterministisk gennemgang. |

## Output-mapper

Standard output for tekstoversættelse:

```text
translations/<language-code>/<source-relative-path>
```

Standard output for oversatte billeder:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API'en kan overskrive disse mapper med `translations_dir` og `image_dir`.