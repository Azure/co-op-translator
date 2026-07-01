# Konfiguratsioon

Co-op Translator nõuab üht keelemudeli pakkujat. Piltide tõlkimiseks on lisaks vaja Azure AI Visioni.

Konfiguratsioon loetakse keskkonnamuutujatest. Kohalike projektide puhul paiguta need projekti juurkausta faili `.env`.

Azure'i ressursside seadistamiseks vaata [Azure AI seadistus](azure-ai-setup.md).

## Kohaliku käituskeskkonna seadistus

Use a virtual environment before running the CLI locally. Co-op Translator supports Python 3.10 through 3.12.

For normal CLI usage, install the published package inside a virtual environment:

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

For repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

After the CLI is available, configure one language model provider in `.env`.

## Provider selection

The tool auto-detects providers in this order:

1. Azure OpenAI
2. OpenAI

If neither provider is configured, `translate`, `evaluate`, `migrate-links`, and `run_translation` fail during configuration checks. `co-op-review` and `run_review` are deterministic maintenance checks and do not require provider credentials.

## Azure OpenAI

Use Azure OpenAI when your model is deployed in Azure AI Foundry or Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

The connectivity check uses the endpoint, API key, API version, and deployment name before translation begins.

## OpenAI

Use OpenAI when calling the OpenAI API directly.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # valikuline
OPENAI_BASE_URL="..."        # valikuline
```

`OPENAI_CHAT_MODEL_ID` is required because the translator needs an explicit chat model for API calls.

## Azure AI Vision

Image translation requires Azure AI Vision so the tool can extract text from images before translating it.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

If image translation is selected with `-img`, `images=True`, or no content-type filter, the tool validates Vision configuration before translation starts.

## Multiple credential sets

The configuration layer supports multiple credential sets by suffixing variables with the same index:

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

Each set must be complete. The health check selects a working set before translation proceeds.

## Command requirements

| Käsk või API | LLM nõutud | Vision nõutud | Märkused |
| --- | --- | --- | --- |
| `translate -md` | Jah | Ei | Tõlgib ainult Markdowni. |
| `translate -nb` | Jah | Ei | Tõlgib ainult märkmikke. |
| `translate -img` | Jah | Jah | Tõlgib ainult pilte. |
| `translate` with no type flags | Jah | Jah | Vaikimisi režiim hõlmab Markdowni, märkmikke ja pilte. |
| `evaluate` | Jah | Ei | Kasutab LLM-i hindamist, välja arvatud kui on valitud `--fast`. |
| `migrate-links` | Jah | Ei | Teostab linkide migreerimise, kuid käivitab endiselt ühised konfiguratsioonikontrollid. |
| `co-op-review` | Ei | Ei | Käivitab deterministlikud tõlke struktuuri, värskuse, Markdowni, märkmike ja kohalike linkide kontrollid. |
| `run_translation(markdown=True)` | Jah | Ei | Programmaatiline Markdowni tõlkimine. |
| `run_translation(images=True)` | Jah | Jah | Programmaatiline piltide tõlkimine. |
| `run_review(...)` | Ei | Ei | Programmaatiline deterministlik ülevaatus. |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

The Python API can override these directories with `translations_dir` and `image_dir`.