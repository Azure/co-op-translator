# Konfigurasyon

Ang Co-op Translator ay nangangailangan ng isang provider ng language model. Ang pagsasalin ng imahe ay nangangailangan din ng Azure AI Vision.

Kinukuha ang konfigurasyon mula sa environment variables. Para sa mga lokal na proyekto, ilagay ang mga ito sa isang `.env` file sa root ng proyekto.

Para sa pagsasaayos ng Azure resource, tingnan ang [Pag-setup ng Azure AI](azure-ai-setup.md).

## Lokal na pagsasaayos ng runtime

Gumamit ng virtual environment bago patakbuhin ang CLI nang lokal. Sinusuportahan ng Co-op Translator ang Python 3.10 hanggang 3.12.

Para sa normal na paggamit ng CLI, i-install ang published package sa loob ng isang virtual environment:

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

Para sa development ng repository, i-install ang mga dependency mula sa project root sa halip:

```bash
poetry install
poetry run translate --help
```

Pagkatapos magamit ang CLI, i-configure ang isang language model provider sa `.env`.

## Pagpili ng provider

Awtomatikong nade-detect ng tool ang mga provider sa sumusunod na pagkakasunod:

1. Azure OpenAI
2. OpenAI

Kung wala sa mga provider ang naka-konfigura, magfa-fail ang `translate`, `evaluate`, `migrate-links`, at `run_translation` sa mga configuration check. Ang `co-op-review` at `run_review` ay mga deterministikong maintenance check at hindi nangangailangan ng provider credentials.

## Azure OpenAI

Gamitin ang Azure OpenAI kapag naka-deploy ang iyong modelo sa Azure AI Foundry o Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Sinusuri ng connectivity check ang endpoint, API key, API version, at deployment name bago magsimula ang pagsasalin.

## OpenAI

Gamitin ang OpenAI kapag direktang tumatawag sa OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opsyonal
OPENAI_BASE_URL="..."        # opsyonal
```

Kinakailangan ang `OPENAI_CHAT_MODEL_ID` dahil kailangan ng translator ng isang tahasang chat model para sa mga API call.

## Azure AI Vision

Ang pagsasalin ng imahe ay nangangailangan ng Azure AI Vision upang makahugot ang tool ng teksto mula sa mga imahe bago ito isalin.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Kung napili ang pagsasalin ng imahe gamit ang `-img`, `images=True`, o walang content-type filter, binavalida ng tool ang Vision configuration bago magsimula ang pagsasalin.

## Maramihang credential set

Sinusuportahan ng configuration layer ang maraming credential set sa pamamagitan ng pagdadagdag ng suffix na pareho ang index sa mga variable:

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

Dapat kumpleto ang bawat set. Pinipili ng health check ang gumaganang set bago magpatuloy ang pagsasalin.

## Mga kinakailangan ng command

| Command o API | Kailangan ang LLM | Kailangan ang Vision | Mga tala |
| --- | --- | --- | --- |
| `translate -md` | Oo | Hindi | Isinasalin lamang ang Markdown. |
| `translate -nb` | Oo | Hindi | Isinasalin lamang ang mga notebook. |
| `translate -img` | Oo | Oo | Isinasalin lamang ang mga imahe. |
| `translate` with no type flags | Oo | Oo | Ang default mode ay kasama ang Markdown, mga notebook, at mga imahe. |
| `evaluate` | Oo | Hindi | Gumagamit ng LLM evaluation maliban kung napili ang `--fast`. |
| `migrate-links` | Oo | Hindi | Nagsasagawa ng link migration, ngunit pinapatakbo pa rin ang mga shared configuration check. |
| `co-op-review` | Hindi | Hindi | Nagpapatakbo ng deterministikong tsek sa istruktura ng pagsasalin, kasariwaan, Markdown, notebook, at mga lokal na link. |
| `run_translation(markdown=True)` | Oo | Hindi | Programatikong pagsasalin ng Markdown. |
| `run_translation(images=True)` | Oo | Oo | Programatikong pagsasalin ng imahe. |
| `run_review(...)` | Hindi | Hindi | Programatikong deterministikong review. |

## Mga direktoryo ng output

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Maaaring i-override ng Python API ang mga direktoryong ito gamit ang `translations_dir` at `image_dir`.