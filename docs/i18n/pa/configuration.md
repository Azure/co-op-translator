# ਸੰਰਚਨਾ

Co-op Translator ਨੂੰ ਇਕ ਭਾਸ਼ਾ ਮਾਡਲ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਚਿੱਤਰਾਂ ਦੇ ਅਨੁਵਾਦ ਲਈ ਵਾਧੂ ਤੌਰ 'ਤੇ Azure AI Vision ਲਾਜ਼ਮੀ ਹੈ।

ਸੰਰਚਨਾ ਵਾਤਾਵਰਨੀ ਵਰਿਆਬਲਾਂ (environment variables) ਤੋਂ ਪੜ੍ਹੀ ਜਾਂਦੀ ਹੈ। ਲੋਕਲ ਪ੍ਰੋਜੈਕਟਾਂ ਲਈ, ਉਨ੍ਹਾਂ ਨੂੰ ਪ੍ਰੋਜੈਕਟ ਰੂਟ 'ਤੇ ਇੱਕ `.env` ਫਾਇਲ ਵਿੱਚ ਰੱਖੋ।

Azure ਸਰੋਤ ਸੈੱਟਅਪ ਲਈ ਵੇਖੋ [Azure AI Setup](azure-ai-setup.md).

## ਲੋਕਲ ਰਨਟਾਇਮ ਸੈਟਅਪ

CLI ਨੂੰ ਲੋਕਲੀ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਵਰਤੋ। Co-op Translator Python 3.11 ਤੋਂ 3.14 ਤੱਕ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ।

ਆਮ CLI ਵਰਤੋਂ ਲਈ, ਪ੍ਰਕਾਸ਼ਿਤ ਪੈਕੇਜ ਨੂੰ ਇੱਕ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਦੇ ਅੰਦਰ ਇਨਸਟਾਲ ਕਰੋ:

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

### ਰਿਪੋਜ਼ਿਟਰੀ ਵਿਕਾਸ

ਰਿਪੋਜ਼ਿਟਰੀ ਵਿਕਾਸ ਲਈ, ਇਸ ਦੀ ਥਾਂ ਪ੍ਰੋਜੈਕਟ ਰੂਟ ਤੋਂ ਨਿਰਭਰਤਾਵਾਂ ਇਨਸਟਾਲ ਕਰੋ:

```bash
poetry install
poetry run translate --help
```

CLI ਉਪਲੱਬਧ ਹੋਣ ਦੇ ਬਾਅਦ, `.env` ਵਿੱਚ ਇੱਕ ਭਾਸ਼ਾ ਮਾਡਲ ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰੋ।

## ਪ੍ਰਦਾਤਾ ਚੋਣ

ਟੂਲ ਪ੍ਰਦਾਤਾਵਾਂ ਨੂੰ ਇਸ ਕ੍ਰਮ ਵਿੱਚ ਆਟੋ-ਡਿਟੈਕਟ ਕਰਦਾ ਹੈ:

1. Azure OpenAI
2. OpenAI
3. Anthropic

ਅਨੁਵਾਦ ਲਈ ਪ੍ਰਦਾਤਾ ਕ੍ਰੈਡੈਂਸ਼ਲ ਲਾਜ਼ਮੀ ਹਨ, ਐਸੇ previews ਛੱਡ ਕੇ ਜਿਵੇਂ `translate -l "ko" -md --dry-run`। `migrate-links`, `co-op-review`, ਅਤੇ `run_review` ਡਿਟਰਮਿਨਿਸਟਿਕ ਮੇਨਟੇਨੈਂਸ ਐਪਰੇਸ਼ਨ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਪ੍ਰਦਾਤਾ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

## ਮਾਡਲ ਕਲਾਇਂਟ ਬੈਕਐਂਡ

Co-op Translator 0.22.0 ਤੋਂ ਸ਼ੁਰੂ ਹੋ ਕੇ, Azure OpenAI, OpenAI, ਅਤੇ Anthropic ਡਿਫੌਲਟ ਤੌਰ 'ਤੇ Microsoft Agent Framework ਵਰਤਦੇ ਹਨ। ਆਮ ਵਰਤੋਂ ਲਈ ਕਿਸੇ ਬੈਕਐਂਡ ਸੈਟਿੰਗ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।

Semantic Kernel ਸਮਰਥਨ ਲਈ ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਉਪਲੱਬਧ ਰਹਿੰਦਾ ਹੈ। ਇਸਨੂੰ ਖਾਸ ਤੌਰ 'ਤੇ ਚੁਣਨ ਲਈ, ਸੈੱਟ ਕਰੋ:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel ਵਰਤਣ 'ਤੇ ਡਿਪ੍ਰੀਕੇਸ਼ਨ ਚੇਤਾਵਨੀ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ। ਯੋਜਨਾ ਇਹ ਹੈ ਕਿ ਪੈਕੇਜ Semantic Kernel ਨੂੰ 0.23.0 ਵਿੱਚ ਇੱਕ ਵਿਕਲਪਿਕ ਨਿਰਭਰਤਾ ਵਜੋਂ ਭੁਜਾਏਗਾ ਅਤੇ 0.24.0 ਵਿੱਚ ਇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਹਟਾ ਦੇਵੇਗਾ, ਜੋ ਕਿ ਸਮਰਥਤਾ ਨਤੀਜਿਆਂ ਅਤੇ ਯੂਜ਼ਰ ਫੀਡਬੈਕ 'ਤੇ ਨਿਰਭਰ ਹੋਵੇਗਾ। Anthropic ਨੂੰ `agent-framework` ਦੀ ਲੋੜ ਹੈ; Anthropic ਦੇ ਨਾਲ ਖਾਸ ਤੌਰ 'ਤੇ `semantic-kernel` ਚੁਣਨ 'ਤੇ ਸੰਰਚਨਾ ਤਰੁੱਟੀ ਆ ਜਾਂਦੀ ਹੈ। ਗ਼ਲਤ ਮੁੱਲ(provider-backed translator initialization ਦੌਰਾਨ) ਸਾਇਲੈਂਟ fallback ਕਰਨ ਦੀ ਬਜਾਏ ਫੇਲ ਹੋ ਜਾਂਦੇ ਹਨ। ਰੋਲਆਉਟ ਦੀ ਪਾਲਣਾ ਕਰੋ ਅਤੇ ਰੁਕਾਵਟਾਂ ਦੀ ਰਿਪੋਰਟ [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) 'ਚ ਕਰੋ।

## Azure OpenAI

ਜਦੋਂ ਤੁਹਾਡਾ ਮਾਡਲ Azure AI Foundry ਜਾਂ Azure OpenAI Service ਵਿੱਚ ਡਿਪਲੋਏ ਕੀਤਾ ਗਿਆ ਹੋਵੇ ਤਾਂ Azure OpenAI ਵਰਤੋ।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ਕਨੈਕਟਿਵਿਟੀ ਚੈੱਕ ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ endpoint, API key, API version, ਅਤੇ deployment name ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।

## OpenAI

ਜਦੋਂ OpenAI API ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕੀਤਾ ਜਾਵੇ ਤਾਂ OpenAI ਵਰਤੋ।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ਲਾਜ਼ਮੀ ਹੈ ਕਿਉਂਕਿ ਅਨੁਵਾਦਕ ਨੂੰ API ਕਾਲਾਂ ਲਈ ਇੱਕ ਸਪਸ਼ਟ chat model ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

ਡਿਫੌਲਟ ਸੈਟਅਪ ਲਈ `OPENAI_ORG_ID` ਅਤੇ `OPENAI_BASE_URL` ਨੂੰ ਅਨਸੈਟ ਛੱਡੋ। ਇੱਕ organization ID ਕੇਵਲ ਉਸ ਵੇਲੇ ਸ਼ਾਮਲ ਕਰੋ ਜੇ ਤੁਹਾਡੇ ਖਾਤੇ ਨੂੰ ਲੋੜ ਹੋਵੇ, ਜਾਂ base URL ਕੇਵਲ ਉਸ ਵੇਲੇ ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਕਸਟਮ endpoint ਵਰਤ ਰਹੇ ਹੋ। ਵਿਕਲਪਿਕ ਸੈਟਿੰਗਾਂ ਲਈ placeholder ਮੁੱਲ ਨਕਲ ਨਾ ਕਰੋ।

## Anthropic Claude

ਜਦੋਂ Claude API ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕੀਤਾ ਜਾਵੇ ਤਾਂ Anthropic ਵਰਤੋ। ਇੱਕ [Anthropic API key](https://platform.claude.com/docs/en/get-started) ਬਣਾਓ ਅਤੇ ਇੱਕ ਸਹਿਰਿਤ [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ਚੁਣੋ।

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ਅਤੇ `ANTHROPIC_MODEL` ਲਾਜ਼ਮੀ ਹਨ। ਤੁਹਾਨੂੰ `CO_OP_TRANSLATOR_MODEL_CLIENT` ਸੈੱਟ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ; Agent Framework ਡਿਫੌਲਟ ਬੈਕਐਂਡ ਹੈ।

Anthropic API ਲਈ `ANTHROPIC_BASE_URL` ਨੂੰ ਅਨਸੈਟ ਛੱਡੋ। ਸਿਰਫ਼ ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਕਸਟਮ endpoint ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ ਹੀ ਇਹ ਸੈੱਟ ਕਰੋ।

`ANTHROPIC_MAX_TOKENS` ਦੀ ਡੀਫੌਲਟ ਵੈਲਯੂ `8192` ਹੈ, ਜੋ Meitei Mayek ਵਰਗੀਆਂ ਟੋਕਨ-ਘਣੀਆਂ ਸਕ੍ਰਿਪਟਾਂ ਲਈ ਕਮਰਾ ਛੱਡਦੀ ਹੈ। ਜੇ ਤੁਹਾਡਾ ਮਾਡਲ ਜਾਂ Anthropic-ਸੰਗਤ endpoint ਇਸ ਤੋਂ ਘੱਟ ਆਉਟਪੁਟ ਸੀਮਾ ਰੱਖਦਾ ਹੈ ਤਾਂ ਇਸ ਨੂੰ ਘਟਾਓ।

## Azure AI Vision

ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ Azure AI Vision ਲਾਜ਼ਮੀ ਹੈ ਤਾਂ ਕਿ ਟੂਲ ਸੰਰਚਿਤ ਭਾਸ਼ਾ ਮਾਡਲ ਦੇ ਅਨੁਵਾਦ ਤੋਂ ਪਹਿਲਾਂ ਚਿੱਤਰਾਂ ਵਿੱਚੋਂ ਟੈਕਸਟ ਨਿਕਾਲ ਸਕੇ। Anthropic ਨਿਕਾਲੇ ਗਏ ਟੈਕਸਟ ਦਾ ਅਨੁਵਾਦ Azure OpenAI ਜਾਂ OpenAI ਦੀ ਤਰ੍ਹਾਂ ਕਰ ਸਕਦਾ ਹੈ।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ਜੇ ਚਿੱਤਰ ਅਨੁਵਾਦ `-img`, `images=True`, ਜਾਂ ਕੋਈ content-type filter ਨਾ ਦਿੱਤਾ ਹੋਵੇ ਨਾਲ ਚੁਣਿਆ ਗਿਆ ਹੈ, ਤਦ ਟੂਲ ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ Vision ਸੰਰਚਨਾ ਦੀ ਵੈਧਤਾ ਜਾਂਚਦਾ ਹੈ।

## ਬਹੁਤ ਸਾਰੇ ਕ੍ਰੈਡੈਂਸ਼ਲ ਸੈੱਟ

ਸੰਰਚਨਾ ਲੇਅਰ ਇੱਕੋ ਇੰਡੈਕਸ ਨਾਲ ਵੈਰੀਏਬਲਾਂ 'ਤੇ ਸਫਿਕਸ ਲਗਾ ਕੇ ਕਈ ਕ੍ਰੈਡੈਂਸ਼ਲ ਸੈੱਟਾਂ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੀ ਹੈ:

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

ਹਰ ਸੈੱਟ ਪੂਰਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਹੈਲਥ ਚੈਕ ਅਨੁਵਾਦ ਅੱਗੇ ਵੱਧਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਕੰਮ ਕਰ ਰਹਾ ਸੈੱਟ ਚੁਣਦਾ ਹੈ।

OpenAI ਅਤੇ Anthropic ਇੱਕੋ suffix ਚਲਨ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਨ। ਇੱਕ ਕ੍ਰੈਡੈਂਸ਼ਲ ਸੈੱਟ ਵਿਚ ਹਰ ਵੇਰੀਏਬਲ ਨੂੰ ਇੱਕੋ suffix 'ਤੇ ਰੱਖੋ, ਜਿਸ ਵਿੱਚ ਵਿਕਲਪਿਕ ਮੁੱਲ ਜਿਵੇਂ `OPENAI_BASE_URL_1` ਜਾਂ `ANTHROPIC_BASE_URL_1` ਵੀ ਸ਼ਾਮਲ ਹਨ।

## ਕਮਾਂਡ ਦੀਆਂ ਲੋੜਾਂ

| ਕਮਾਂਡ ਜਾਂ API | LLM ਲਾਜ਼ਮੀ | Vision ਲਾਜ਼ਮੀ | ਟਿੱਪਣੀਆਂ |
| --- | --- | --- | --- |
| `translate -md` | ਹਾਂ | ਨਹੀਂ | ਸਿਰਫ਼ Markdown ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। |
| `translate -nb` | ਹਾਂ | ਨਹੀਂ | ਸਿਰਫ਼ notebooks ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। |
| `translate -img` | ਹਾਂ | ਹਾਂ | ਸਿਰਫ਼ ਚਿੱਤਰਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। |
| `translate` with no type flags | ਹਾਂ | ਹਾਂ | ਡੀਫੌਲਟ ਮੋਡ ਵਿੱਚ Markdown, notebooks, ਅਤੇ images ਸ਼ਾਮਲ ਹਨ। |
| `evaluate` | ਹਾਂ | ਨਹੀਂ | ਜੇ `--fast` ਨਹੀਂ ਚੁਣਿਆ ਗਿਆ, ਤਾਂ LLM ਮੁਲਾਂਕਣ ਵਰਤਦਾ ਹੈ। |
| `migrate-links` | ਨਹੀਂ | ਨਹੀਂ | ਪ੍ਰਦਾਤਾ ਕਾਲਾਂ ਦੇ ਬਿਨਾਂ ਲੋਕਲ ਲਿੰਕ ਮਾਈਗ੍ਰੇਸ਼ਨ ਕਰਦਾ ਹੈ। |
| `co-op-review` | ਨਹੀਂ | ਨਹੀਂ | ਡਿਟਰਮਿਨਿਸਟਿਕ ਅਨੁਵਾਦ ਸੰਰਚਨਾ, ਤਾਜ਼ਗੀ, Markdown, notebook, ਅਤੇ ਲੋਕਲ ਲਿੰਕ ਚੈਕ ਚਲਾਉਂਦਾ ਹੈ। |
| `run_translation(markdown=True)` | ਹਾਂ | ਨਹੀਂ | ਪ੍ਰੋਗ੍ਰਾਮੈਟਿਕ Markdown ਅਨੁਵਾਦ। |
| `run_translation(images=True)` | ਹਾਂ | ਹਾਂ | ਪ੍ਰੋਗ੍ਰਾਮੈਟਿਕ ਚਿੱਤਰ ਅਨੁਵਾਦ। |
| `run_review(...)` | ਨਹੀਂ | ਨਹੀਂ | ਪ੍ਰੋਗ੍ਰਾਮੈਟਿਕ ਡਿਟਰਮਿਨਿਸਟਿਕ ਰੀਵਿਊ। |

## ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀਆਂ

ਡਿਫੌਲਟ ਟੈਕਸਟ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ:

```text
translations/<language-code>/<source-relative-path>
```

ਡਿਫੌਲਟ ਅਨੁਵਾਦ ਕੀਤਾ ਚਿੱਤਰ ਆਉਟਪੁੱਟ:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ਇਨ੍ਹਾਂ ਡਾਇਰੈਕਟਰੀਜ਼ ਨੂੰ `translations_dir` ਅਤੇ `image_dir` ਨਾਲ ਓਵਰਰਾਈਡ ਕਰ ਸਕਦਾ ਹੈ।