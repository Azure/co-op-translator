# Konfigureshon

Co-op Translator dey require one language model provider. For image translation, e still require Azure AI Vision.

Configuration dey read from environment variables. For local projects, put dem inside a `.env` file for di project root.

If you wan set up Azure resources, see [Azure AI Setup](azure-ai-setup.md).

## Local runtime setup

Make you use a virtual environment before you run the CLI locally. Co-op Translator dey support Python 3.11 through 3.14.

For normal CLI use, install the published package inside a virtual environment:

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

### Repository development

If you dey do repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

After the CLI don become available, configure one language model provider inside `.env`.

## Provider selection

The tool go auto-detect providers for this order:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Translation need provider credentials, except for previews such as `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, and `run_review` na deterministic maintenance operations and dem no need provider credentials.

## Model client backend

Starting with Co-op Translator 0.22.0, Azure OpenAI, OpenAI, and Anthropic dey use Microsoft Agent Framework by default. No backend setting dey required for normal use.

Semantic Kernel still dey available temporarily for compatibility. If you wan select am explicitly, set:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

If you use Semantic Kernel e go show deprecation warning. The package get plan to move Semantic Kernel to an optional dependency in 0.23.0 and remove the integration in 0.24.0, depending on compatibility results and user feedback. Anthropic dey require `agent-framework`; explicitly selecting `semantic-kernel` with Anthropic go fail with a configuration error. Invalid values go fail during provider-backed translator initialization instead of silently falling back. Follow the rollout and report blockers in [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Use Azure OpenAI when your model dey deployed in Azure AI Foundry or Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

The connectivity check dey use the endpoint, API key, API version, and deployment name before translation begins.

## OpenAI

Use OpenAI when you dey call the OpenAI API directly.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` is required because the translator need an explicit chat model for API calls.

Leave `OPENAI_ORG_ID` and `OPENAI_BASE_URL` unset for the default setup. Add an organization ID only if your account needs one, or a base URL only when using a custom endpoint. No copy placeholder values for optional settings.

## Anthropic Claude

Use Anthropic when you dey call the Claude API directly. Create an [Anthropic API key](https://platform.claude.com/docs/en/get-started) and choose a supported [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` dey required. You no need set `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework na the default backend.

Leave `ANTHROPIC_BASE_URL` unset for the Anthropic API. Set it only when using a custom endpoint.

`ANTHROPIC_MAX_TOKENS` defaults to `8192`, which leave room for token-dense scripts such as Meitei Mayek. Lower am if your model or Anthropic-compatible endpoint caps output below that.

## Azure AI Vision

Image translation dey require Azure AI Vision so the tool fit extract text from images before the configured language model translate am. Anthropic fit translate the extracted text just like Azure OpenAI or OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

If image translation dey selected with `-img`, `images=True`, or no content-type filter, the tool go validate Vision configuration before translation starts.

## Multiple credential sets

The configuration layer support multiple credential sets by suffixing variables with the same index:

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

Every set gats be complete. The health check go select a working set before translation proceed.

OpenAI and Anthropic support the same suffix convention. Keep every variable in a credential set on the same suffix, including optional values such as `OPENAI_BASE_URL_1` or `ANTHROPIC_BASE_URL_1`.

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Na only Markdown e translate. |
| `translate -nb` | Yes | No | Na only notebooks e translate. |
| `translate -img` | Yes | Yes | Na only images e translate. |
| `translate` with no type flags | Yes | Yes | Default mode include Markdown, notebooks, and images. |
| `evaluate` | Yes | No | E dey use LLM evaluation unless `--fast` dey selected. |
| `migrate-links` | No | No | E go perform local link migration without provider calls. |
| `co-op-review` | No | No | E go run deterministic checks for translation structure, freshness, Markdown, notebook, and local link checks. |
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

The Python API fit override these directories with `translations_dir` and `image_dir`.