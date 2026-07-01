# Konfigureshon

Co-op Translator need one language model provider. For image translation, e still need Azure AI Vision.

Configuration dey read from environment variables. For local projects, put dem for `.env` file for the project root.

If you wan set up Azure resource, check [Azure AI Setup](azure-ai-setup.md).

## Local runtime setup

Make you use a virtual environment before you run the CLI locally. Co-op Translator support Python 3.10 through 3.12.

For normal CLI use, install the published package inside a virtual environment:

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

If you dey develop the repository, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

After the CLI don dey available, configure one language model provider in `.env`.

## Provider selection

The tool go auto-detect providers for this order:

1. Azure OpenAI
2. OpenAI

If neither provider configured, `translate`, `evaluate`, `migrate-links`, and `run_translation` go fail during configuration checks. `co-op-review` and `run_review` na deterministic maintenance checks and no need provider credentials.

## Azure OpenAI

Use Azure OpenAI if your model dey deployed for Azure AI Foundry or Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

The connectivity check dey use the endpoint, API key, API version, and deployment name before translation begins.

## OpenAI

Use OpenAI if you dey call the OpenAI API directly.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # na your choice
OPENAI_BASE_URL="..."        # na your choice
```

`OPENAI_CHAT_MODEL_ID` dey required because the translator need an explicit chat model for API calls.

## Azure AI Vision

Image translation need Azure AI Vision so the tool fit extract text from images before e translate am.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

If image translation is selected with `-img`, `images=True`, or no content-type filter, the tool validates Vision configuration before translation starts.

## Multiple credential sets

The configuration layer fit support multiple credential sets by suffixing variables with the same index:

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

Every set gats complete. The health check go select a working set before translation proceeds.

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | E dey translate Markdown only. |
| `translate -nb` | Yes | No | E dey translate notebooks only. |
| `translate -img` | Yes | Yes | E dey translate images only. |
| `translate` with no type flags | Yes | Yes | Default mode include Markdown, notebooks, and images. |
| `evaluate` | Yes | No | E go use LLM evaluation unless `--fast` is selected. |
| `migrate-links` | Yes | No | E go perform link migration, but e still go run shared configuration checks. |
| `co-op-review` | No | No | E dey run deterministic translation structure, freshness, Markdown, notebook, and local link checks. |
| `run_translation(markdown=True)` | Yes | No | Na programmatic Markdown translation. |
| `run_translation(images=True)` | Yes | Yes | Na programmatic image translation. |
| `run_review(...)` | No | No | Na programmatic deterministic review. |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

The Python API fit override these directories with `translations_dir` and `image_dir`.