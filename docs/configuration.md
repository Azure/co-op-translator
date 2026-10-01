# Configuration

Co-op Translator requires one language model provider. Image translation additionally requires Azure AI Vision.

Configuration is read from environment variables. For local projects, place them in a `.env` file at the project root.

For Azure resource setup, see [Azure AI Setup](azure-ai-setup.md).

## Local runtime setup

Use a virtual environment before running the CLI locally. Co-op Translator supports Python 3.11 through 3.14.

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
3. Anthropic

If no provider is configured, `translate`, `evaluate`, `migrate-links`, and `run_translation` fail during configuration checks. `co-op-review` and `run_review` are deterministic maintenance checks and do not require provider credentials.

## Model client backend

Azure OpenAI and OpenAI use Semantic Kernel by default. Anthropic uses the [Microsoft Agent Framework Anthropic integration](https://github.com/microsoft/agent-framework/tree/main/python/packages/anthropic) automatically. To select Agent Framework explicitly, set:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="agent-framework"
```

Supported values are `semantic-kernel` and `agent-framework`. Anthropic requires `agent-framework`; explicitly selecting `semantic-kernel` with Anthropic fails with a configuration error. Invalid values fail during provider-backed translator initialization instead of silently falling back.

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
OPENAI_ORG_ID="..."          # optional
OPENAI_BASE_URL="..."        # optional
```

`OPENAI_CHAT_MODEL_ID` is required because the translator needs an explicit chat model for API calls.

## Anthropic Claude

Use Anthropic when calling the Claude API directly. Create an [Anthropic API key](https://platform.claude.com/docs/en/get-started) and choose a supported [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
ANTHROPIC_BASE_URL="..."      # optional; omit for the Anthropic API
```

`ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` are required. You do not need to set `CO_OP_TRANSLATOR_MODEL_CLIENT`; Anthropic selects Agent Framework automatically.

## Azure AI Vision

Image translation requires Azure AI Vision so the tool can extract text from images before the configured language model translates it. Anthropic can translate the extracted text just like Azure OpenAI or OpenAI.

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

OpenAI and Anthropic support the same suffix convention. Keep every variable in a credential set on the same suffix, including optional values such as `OPENAI_BASE_URL_1` or `ANTHROPIC_BASE_URL_1`.

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Translates Markdown only. |
| `translate -nb` | Yes | No | Translates notebooks only. |
| `translate -img` | Yes | Yes | Translates images only. |
| `translate` with no type flags | Yes | Yes | Default mode includes Markdown, notebooks, and images. |
| `evaluate` | Yes | No | Uses LLM evaluation unless `--fast` is selected. |
| `migrate-links` | Yes | No | Performs link migration, but still runs shared configuration checks. |
| `co-op-review` | No | No | Runs deterministic translation structure, freshness, Markdown, notebook, and local link checks. |
| `run_translation(markdown=True)` | Yes | No | Programmatic Markdown translation. |
| `run_translation(images=True)` | Yes | Yes | Programmatic image translation. |
| `run_review(...)` | No | No | Programmatic deterministic review. |

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
