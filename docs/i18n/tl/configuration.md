# Konfigurasyon

Nangangailangan ang Co-op Translator ng isang language model provider. Para sa pagsasalin ng mga imahe, kailangan din ang Azure AI Vision.

Binabasa ang konfigurasyon mula sa mga environment variable. Para sa mga lokal na proyekto, ilagay ang mga ito sa isang `.env` na file sa root ng proyekto.

Para sa pagsasaayos ng Azure resource, tingnan ang [Azure AI Setup](azure-ai-setup.md).

## Lokal na pagsasaayos ng runtime

Gumamit ng virtual environment bago patakbuhin ang CLI nang lokal. Sinusuportahan ng Co-op Translator ang Python 3.11 hanggang 3.14.

Para sa karaniwang paggamit ng CLI, i-install ang inilathalang package sa loob ng virtual environment:

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

### Pag-develop ng repository

Para sa pag-develop ng repository, i-install ang mga dependency mula sa root ng proyekto sa halip:

```bash
poetry install
poetry run translate --help
```

Kapag magagamit na ang CLI, i-configure ang isang language model provider sa `.env`.

## Pagpili ng provider

Awtomatikong dini-detect ng tool ang mga provider sa sumusunod na pagkakasunod-sunod:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Nangangailangan ng credentials ng provider ang pagsasalin, maliban sa mga preview tulad ng `translate -l "ko" -md --dry-run`. Ang `migrate-links`, `co-op-review`, at `run_review` ay deterministic na maintenance operations at hindi nangangailangan ng provider credentials.

## Backend ng model client

Simula sa Co-op Translator 0.22.0, gumagamit ang Azure OpenAI, OpenAI, at Anthropic ng Microsoft Agent Framework bilang default. Hindi kailangan ng backend setting para sa karaniwang paggamit.

Panandaliang magagamit pa rin ang Semantic Kernel para sa compatibility. Upang piliin ito nang tahasan, itakda:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Ang paggamit ng Semantic Kernel ay maglalabas ng deprecation warning. Nakalahad sa plano na ilipat ng package ang Semantic Kernel bilang optional dependency sa 0.23.0 at alisin ang integrasyon sa 0.24.0, depende sa mga resulta ng compatibility at feedback ng mga gumagamit. Nangangailangan ang Anthropic ng `agent-framework`; ang tahasang pagpili ng `semantic-kernel` kasama ang Anthropic ay magkakamali na may configuration error. Ang mga invalid na halaga ay mabibigo sa panahon ng provider-backed translator initialization sa halip na tahimik na mag-fallback. Sundan ang rollout at i-report ang mga blocker sa [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Gamitin ang Azure OpenAI kapag naka-deploy ang iyong modelo sa Azure AI Foundry o Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Gumagamit ang connectivity check ng endpoint, API key, API version, at deployment name bago magsimula ang pagsasalin.

## OpenAI

Gamitin ang OpenAI kapag direktang tumatawag sa OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ay kinakailangan dahil kailangan ng translator ng isang tahasang chat model para sa mga API call.

Iwanan ang `OPENAI_ORG_ID` at `OPENAI_BASE_URL` na hindi naka-set para sa default na setup. Magdagdag ng organization ID lamang kung kailangan ng iyong account, o base URL lamang kapag gumagamit ng custom endpoint. Huwag kopyahin ang mga placeholder na halaga para sa mga opsyonal na setting.

## Anthropic Claude

Gamitin ang Anthropic kapag direktang tumatawag sa Claude API. Gumawa ng isang [Anthropic API key](https://platform.claude.com/docs/en/get-started) at pumili ng suportadong [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` at `ANTHROPIC_MODEL` ay kinakailangan. Hindi mo kailangang itakda ang `CO_OP_TRANSLATOR_MODEL_CLIENT`; ang Agent Framework ang default na backend.

Iwanang hindi naka-set ang `ANTHROPIC_BASE_URL` para sa Anthropic API. Itakda ito lamang kapag gumagamit ng custom endpoint.

`ANTHROPIC_MAX_TOKENS` ay naka-default sa `8192`, na nag-iiwan ng puwang para sa mga script na maraming token tulad ng Meitei Mayek. Bawasan ito kung nililimitahan ng iyong modelo o Anthropic-compatible endpoint ang output sa mas mababa dito.

## Azure AI Vision

Nangangailangan ang pagsasalin ng imahe ng Azure AI Vision upang makuha ng tool ang teksto mula sa mga imahe bago ito isalin ng naka-configure na language model. Maaari ring isalin ng Anthropic ang nakuha na teksto katulad ng Azure OpenAI o OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Kung napili ang pagsasalin ng imahe gamit ang `-img`, `images=True`, o walang content-type filter, sinusuri ng tool ang Vision configuration bago magsimula ang pagsasalin.

## Maramihang set ng kredensyal

Sinusuportahan ng configuration layer ang maramihang set ng kredensyal sa pamamagitan ng pagsasuffix ng mga variable gamit ang parehong index:

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

Sinusuportahan ng OpenAI at Anthropic ang parehong suffix convention. Panatilihin ang bawat variable sa isang credential set na may parehong suffix, kabilang ang mga opsyonal na halaga tulad ng `OPENAI_BASE_URL_1` o `ANTHROPIC_BASE_URL_1`.

## Mga kinakailangan ng command

| Command o API | Kailangan ng LLM | Kailangan ng Vision | Mga Tala |
| --- | --- | --- | --- |
| `translate -md` | Oo | Hindi | Isinasalin ang Markdown lamang. |
| `translate -nb` | Oo | Hindi | Isinasalin ang mga notebook lamang. |
| `translate -img` | Oo | Oo | Isinasalin ang mga imahe lamang. |
| `translate` with no type flags | Oo | Oo | Kasama sa default na mode ang Markdown, notebooks, at mga imahe. |
| `evaluate` | Oo | Hindi | Gumagamit ng LLM evaluation maliban kung pinili ang `--fast`. |
| `migrate-links` | Hindi | Hindi | Gumagawa ng lokal na migration ng link nang walang pagtawag sa provider. |
| `co-op-review` | Hindi | Hindi | Pinapatakbo ang deterministang tseke ng istruktura ng pagsasalin, freshness, Markdown, notebook, at lokal na link. |
| `run_translation(markdown=True)` | Oo | Hindi | Programatikong pagsasalin ng Markdown. |
| `run_translation(images=True)` | Oo | Oo | Programatikong pagsasalin ng mga imahe. |
| `run_review(...)` | Hindi | Hindi | Programatikong deterministang review. |

## Mga output na direktoryo

Default na output ng pagsasalin ng teksto:

```text
translations/<language-code>/<source-relative-path>
```

Default na output para sa mga isinaling imahe:

```text
translated_images/<language-code>/<source-relative-path>
```

Maaaring i-override ng Python API ang mga direktoryong ito gamit ang `translations_dir` at `image_dir`.