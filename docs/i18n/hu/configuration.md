# Konfiguráció

Co-op Translator requires one language model provider. Image translation additionally requires Azure AI Vision.

Configuration is read from environment variables. For local projects, place them in a `.env` file at the project root.

For Azure resource setup, see [Azure AI beállítása](azure-ai-setup.md).

## Helyi futtatási környezet beállítása

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

## Szolgáltató kiválasztása

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
OPENAI_ORG_ID="..."          # opcionális
OPENAI_BASE_URL="..."        # opcionális
```

`OPENAI_CHAT_MODEL_ID` is required because the translator needs an explicit chat model for API calls.

## Azure AI Vision

Image translation requires Azure AI Vision so the tool can extract text from images before translating it.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

If image translation is selected with `-img`, `images=True`, or no content-type filter, the tool validates Vision configuration before translation starts.

## Több hitelesítő készlet

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

## Parancsok követelményei

| Parancs vagy API | LLM szükséges | Vision szükséges | Megjegyzések |
| --- | --- | --- | --- |
| `translate -md` | Igen | Nem | Csak Markdown-t fordít. |
| `translate -nb` | Igen | Nem | Csak notebookokat fordít. |
| `translate -img` | Igen | Igen | Csak képeket fordít. |
| `translate` típusjelzők nélkül | Igen | Igen | Az alapértelmezett mód tartalmazza a Markdown-t, a notebookokat és a képeket. |
| `evaluate` | Igen | Nem | LLM-értékelést használ, hacsak nem a `--fast` van kiválasztva. |
| `migrate-links` | Igen | Nem | Linkáttelepítést hajt végre, de továbbra is lefuttatja a megosztott konfigurációs ellenőrzéseket. |
| `co-op-review` | Nem | Nem | Futtat determinisztikus fordítási szerkezet-, frissesség-, Markdown-, notebook- és helyi link ellenőrzéseket. |
| `run_translation(markdown=True)` | Igen | Nem | Programozott Markdown fordítás. |
| `run_translation(images=True)` | Igen | Igen | Programozott képfordítás. |
| `run_review(...)` | Nem | Nem | Programozott determinisztikus ellenőrzés. |

## Kimeneti könyvtárak

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

The Python API can override these directories with `translations_dir` and `image_dir`.