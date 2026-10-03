# ಕಾನ್ಫಿಗರೇಶನ್

Co-op Translator ಗೆ ಒಂದು ಭಾಷಾ ಮಾದರಿ ಪೂರೈಕೆದಾರ ಅಗತ್ಯವಿದೆ. ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಹೆಚ್ಚುವриди ಆಗಿ Azure AI Vision ಅಗತ್ಯವಿದೆ.

ಕಾನ್ಫಿಗರೇಶನ್ ಅನ್ನು ವಾತಾವರಣ ಚರಗಳಿಂದ ಓದಲಾಗುತ್ತದೆ. ಸ್ಥಳೀಯ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಗೆ, ಅದನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಲ್ಲಿ `.env` ಫೈಲ್‌ನಲ್ಲಿ ಇರಿಸಿ.

Azure ಸಂಪನ್ಮೂಲ ಸೆಟಪ್‌ಗಾಗಿ, [Azure AI ಸೆಟಪ್](azure-ai-setup.md) ಅನ್ನು ನೋಡಿ.

## ಸ್ಥಳೀಯ ರನ್‌ಟೈಮ್ ಸೆಟ್‌ಅಪ್

CLI ಅನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಓಡಿಸುವ ಮೊದಲು ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಬಳಸಿ. Co-op Translator ಪೈಥಾನ್ 3.11 ಇಂದ 3.14 ರವರೆಗೆ ಬೆಂಬಲಿಸುತ್ತದೆ.

ಸಾಮಾನ್ಯ CLI ಬಳಕೆಗೆ, ಪ್ರಕಟಿತ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಒಳಗೆ ಸ್ಥಾಪಿಸಿ:

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

### ರೆಪೊಸಿಟರಿ ಅಭಿವೃದ್ಧಿ

ರೆಪೊಸಿಟರಿ ಅಭಿವೃದ್ಧಿಗಾಗಿ, ಪ್ರಾಜೆಕ್ಟ್ ರೂಟ್‌ನಿಂದ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:

```bash
poetry install
poetry run translate --help
```

CLI ಲಭ್ಯವಾದ ನಂತರ, `.env` ಫೈಲ್‌ನಲ್ಲಿ ಒಂದು ಭಾಷಾ ಮಾದರಿ ಪೂರೈಕೆದಾರವನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ.

## ಪೂರೈಕೆದಾರ ಆಯ್ಕೆ

ಟೂಲ್ ಈ ಕ್ರಮದಲ್ಲಿ ಪೂರೈಕೆದಾರರನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ:

1. Azure OpenAI
2. OpenAI
3. Anthropic

ಅನುವಾದಕ್ಕೆ ಪೂರೈಕೆದಾರರ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳು ಅಗತ್ಯವಿದೆ, `translate -l "ko" -md --dry-run` ಮುಂತಾದ ಪೂರ್ವದೃಶ್ಯಗಳನ್ನು ಹೊರತಾಗಿ. `migrate-links`, `co-op-review`, ಮತ್ತು `run_review` ನಿರ್ಧಾರಾತ್ಮಕ ನಿರ್ವಹಣಾ ಕಾರ್ಯಗಳಾಗಿದ್ದು, ಅವುಗಳಿಗೆ ಪೂರೈಕೆದಾರರ ಕ್ರೆಡೆನ್ಷಿಯಲ್ ಅಗತ್ಯವಿಲ್ಲ.

## ಮಾದರಿ ಕ್ಲೈಂಟ್ ಬ್ಯಾಕೆಂಡ್

Co-op Translator 0.22.0 ರಿಂದ, Azure OpenAI, OpenAI, ಮತ್ತು Anthropic ಡೀಫಾಲ್ಟ್ ಆಗಿ Microsoft Agent Framework ಅನ್ನು ಬಳಸುತ್ತವೆ. ಸಾಮಾನ್ಯ ಬಳಕೆಗೆ ಯಾವುದೇ ಬ್ಯಾಕೆಂಡ್ ಸೆಟ್ಟಿಂಗ್ ಅಗತ್ಯವಿಲ್ಲ.

Semantic Kernel ತಾಳಮೇಳಕ್ಕಾಗಿ ತಾತ್ಕಾಲಿಕವಾಗಿ ಲಭ್ಯವಿದೆ. ಅದನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಆಯ್ಕೆಮಾಡಲು, ಸೆಟ್ ಮಾಡಿ:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel ಬಳಸಿದಾಗ ಒಂದು ಅಪ್ರಚಲಿತತೆ (deprecation) ಎಚ್ಚರಿಕೆ ನೀಡಲಾಗುತ್ತದೆ. ಪ್ಯಾಕೇಜ್ 0.23.0 ರಲ್ಲಿ Semantic Kernel ಅನ್ನು ಐಚ್ಛಿಕ ಅವಲಂಬನೆಯಾಗಿ moved ಮಾಡಲು ಮತ್ತು 0.24.0 ರಲ್ಲಿ ಈ ಏಕೀಕರಣವನ್ನು ತೆಗೆದುಹಾಕಲು ಯೋಜಿಸಲಾಗಿದೆ, ಇದು ಹೊಂದಾಣಿಕೆ ಫಲಿತಾಂಶಗಳು ಮತ್ತು ಬಳಕೆದಾರರ ಪ್ರತಿಕ್ರಿಯೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ. Anthropic ಗೆ `agent-framework` ಅಗತ್ಯವಿದೆ; Anthropic ಜೊತೆಗೆ ಸ್ಪಷ್ಟವಾಗಿ `semantic-kernel` ಅನ್ನು ಆಯ್ಕೆಮಾಡಿದರೆ ಅದು ಕಾನ್ಫಿಗರೇಶನ್ ದೋಷದಿಂದ ವಿಫಲವಾಗುತ್ತದೆ. ಅಮಾನ್ಯ ಮೌಲ್ಯಗಳು ಮೌನವಾಗಿ ಪರ್ಯಾಯಕ್ಕೆ ಹೋಗುವ ಬದಲಿಗೆ ಪೂರೈಕೆದಾರ-ಆಧಾರಿತ ಅನುವಾದಕದ ಪ್ರಾರಂಭಣೆಯ ವೇಳೆ ವಿಫಲವಾಗುತ್ತವೆ. ರೋಲೌಟ್ ಅನ್ನು ಅನುಸರಿಸಿ ಮತ್ತು ಅಡ್ಡಿಪಡೆಗಳನ್ನು [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) ನಲ್ಲಿ ವರದಿ ಮಾಡಿ.

## Azure OpenAI

ನಿಮ್ಮ ಮಾದರಿ Azure AI Foundry ಅಥವಾ Azure OpenAI Service ನಲ್ಲಿ ನಿಯೋಜಿತವಾಗಿದ್ದಾಗ Azure OpenAI ಅನ್ನು ಬಳಸಿರಿ.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ಕನಕ್ಟಿವಿಟಿ ಪರಿಶೀಲನೆ ಅನುವಾದ ಆರಂಭವಾಗುವ ಮೊದಲು ಎಂಡ್‌ಪುಯಿಂಟ್, API ಕೀ, API ಆವೃತ್ತಿ, ಮತ್ತು ನಿಯೋಜನೆ ಹೆಸರನ್ನು ಬಳಸಿ ಪರಿಶೀಲಿಸುತ್ತದೆ.

## OpenAI

OpenAI API ಅನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡುವಾಗ OpenAI ಅನ್ನು ಬಳಸಿ.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ಅಗತ್ಯವಿದೆ ಏಕೆಂದರೆ ಅನುವಾದಕಕ್ಕೆ API ಕರೆಗೆ ಸ್ಪಷ್ಟವಾದ ಚಾಟ್ ಮಾದರಿ ಬೇಕು.

ಡೀಫಾಲ್ಟ್ ಸೆಟ್‌ಅಪ್‌ಗಾಗಿ `OPENAI_ORG_ID` ಮತ್ತು `OPENAI_BASE_URL` ಅನ್ನು ಅನ್ಸೆಟ್ ಮಾಡಿ. ನಿಮ್ಮ ಖಾತೆಗೆ ಒಂದು.organization ID ಬೇಕಾದರೆ ಮಾತ್ರ ಅದನ್ನು ಸೇರಿಸಿ, ಅಥವಾ ಕಸ್ಟಮ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಬಳಸುತ್ತಿರುವಾಗ ಮಾತ್ರ base URL ಸೇರಿಸಿ. ಐಚ್ಛಿಕ ಸೆಟ್ಟಿಂಗ್ಸ್‌ಗಳಿಗೆ ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಮೌಲ್ಯಗಳನ್ನು ನಕಲಿಸಬೇಡಿ.

## Anthropic Claude

Claude API ಅನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡುವಾಗ Anthropic ಅನ್ನು ಬಳಸಿ. [Anthropic API ಕೀ](https://platform.claude.com/docs/en/get-started) ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಬೆಂಬಲಿತ [Claude ಮಾದರಿ ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ಮತ್ತು `ANTHROPIC_MODEL` ಅಗತ್ಯವಿದೆ. `CO_OP_TRANSLATOR_MODEL_CLIENT` ಅನ್ನು ಸೆಟ್ ಮಾಡುವ ಅಗತ್ಯವಿಲ್ಲ; Agent Framework ಡೀಫಾಲ್ಟ್ ಬ್ಯಾಕೆಂಡ್ ಆಗಿದೆ.

Anthropic API ನಿರಗೆ `ANTHROPIC_BASE_URL` ಅನ್ನು ಅಸೇಟ್‌ನಲ್ಲಿರಿಸಿ. ಕಸ್ಟಮ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಬಳಸುತ್ತಿರುವಾಗ ಮಾತ್ರ ಅದನ್ನು ಸೆಟ್ ಮಾಡಿ.

`ANTHROPIC_MAX_TOKENS` ಡೀಫಾಲ್ಟ್ `8192` ಆಗಿದೆ, ಇದು Meitei Mayek ಮುಂತಾದ ಟೋಕನ್-ಸಂಘಟಿತ ಲಿಪಿಗಳಿಗೆ ಜಾಗವನ್ನು ಬಿಡುತ್ತದೆ. ನಿಮ್ಮ ಮಾದರಿ ಅಥವಾ Anthropic-ಸಮ್ಮತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಆಗಲೇ ಅದರಿಗಿಂತ ಕಡಿಮೆ ಔಟ್ಪುಟ್‌ನ್ನು ಮಿತಿಗೊಳಿಸುತ್ತಿದ್ದರೆ ಇದನ್ನು ಕಡಿಮೆ ಮಾಡಿ.

## Azure AI Vision

ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ Azure AI Vision ಅಗತ್ಯವಿದೆ, ಏಕೆಂದರೆ ಟೂಲ್ಗೆ ಚಿತ್ರಗಳಿಂದ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆಯಲು ಇದು ಅಗತ್ಯವಾಗುತ್ತದೆ ಮತ್ತು ನಂತರ ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಭಾಷಾ ಮಾದರಿ ಅದನ್ನು ಅನುವಾದಿಸುತ್ತದೆ. Anthropic ಕೂಡ ಹೊರತೆಗೆಯಲಾದ ಪಠ್ಯವನ್ನು Azure OpenAI ಅಥವಾ OpenAI ಹಾಗೆಯೇ ಅನುವಾದಿಸಬಹುದು.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True`, ಅಥವಾ ಯಾವುದೇ content-type ಫಿಲ್ಟರ್ ಇಲ್ಲದಿದ್ದರೆ ಚಿತ್ರ ಅನುವಾದ ಆಯ್ಕೆಮಾಡಿದಾಗ, ಟೂಲ್ ಅನುವಾದ ಆರಂಭವಾಗುವ ಮೊದಲು Vision ಸಂರಚನೆಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.

## ಬಹು ಪ್ರಮಾಣೀಕರಣ ಸೆಟ್‌ಗಳು

ಕಾನ್ಫಿಗರೇಷನ್ ಲೇಯರ್ ಒಂದೇ ಸೂಚ್ಯಂಕದೊಂದಿಗೆ ಚರಗಳಿಗೆ ಸೂಫಿಕ್ಸ್ ಸೇರಿಸುವ ಮೂಲಕ ಬಹು ಕ್ರೆಡೆನ್ಷಿಯಲ್ ಸೆಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ:

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

ಪ್ರತಿ ಸೆಟ್ ಪೂರ್ಣವಾಗಿರಬೇಕು. ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಅನುವಾದ ಮುಂದುವರಿಯುವ ಮೊದಲು ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಸೆಟ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತದೆ.

OpenAI ಮತ್ತು Anthropic ಒಂದೇ ಸಫಿಕ್ಸ್ ಸಂಪ್ರದಾಯವನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ. `OPENAI_BASE_URL_1` ಅಥವಾ `ANTHROPIC_BASE_URL_1` ಮುಂತಾದ ಐಚ್ಛಿಕ ಮೌಲ್ಯಗಳನ್ನು ಒಳಗೊಂಡಂತೆ, ಕ್ರೆಡೆನ್ಷಿಯಲ್ ಸೆಟ್‌ನ ಪ್ರತಿಯೊಂದು ಚರವನ್ನು ಒಂದೇ ಸಫಿಕ್ಸ್‌ನಲ್ಲಿ ಇಡಿರಿ.

## ಆಜ್ಞೆ ಅವಶ್ಯಕತೆಗಳು

| Command ಅಥವಾ API | LLM ಅಗತ್ಯವಿದೆ | Vision ಅಗತ್ಯವಿದೆ | ಟಿಪ್ಪಣಿಗಳು |
| --- | --- | --- | --- |
| `translate -md` | ಹೌದು | ಇಲ್ಲ | Markdown ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ. |
| `translate -nb` | ಹೌದು | ಇಲ್ಲ | ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ. |
| `translate -img` | ಹೌದು | ಹೌದು | ಚಿತ್ರಗಳನ್ನು ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ. |
| `translate` with no type flags | ಹೌದು | ಹೌದು | ಡೀಫಾಲ್ಟ್ ಮೋಡ್‌ನಲ್ಲಿ Markdown, ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳು ಸೇರಿವೆ. |
| `evaluate` | ಹೌದು | ಇಲ್ಲ | `--fast` ಆಯ್ಕೆಮಾಡದಿದ್ದರೆ LLM ಮೌಲ್ಯಮಾಪನವನ್ನು ಬಳಸುತ್ತದೆ. |
| `migrate-links` | ಇಲ್ಲ | ಇಲ್ಲ | ಪೂರೈಕೆದಾರ ಕರೆದಿಲ್ಲದೆ ಸ್ಥಳೀಯ ಲಿಂಕ್‌ಗಳನ್ನು ಸ್ಥಳಾಂತರಿಸುತ್ತದೆ. |
| `co-op-review` | ಇಲ್ಲ | ಇಲ್ಲ | ನಿರ್ಧಾರಾತ್ಮಕ ಅನುವಾದ ರಚನೆ, ತಾಜಾತನ, Markdown, ನೋಟ್ಬುಕ್ ಮತ್ತು ಸ್ಥಳೀಯ ಲಿಂಕ್ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |
| `run_translation(markdown=True)` | ಹೌದು | ಇಲ್ಲ | ಪ್ರೋಗ್ರಾಮಾತ್ಮಕ Markdown ಅನುವಾದ. |
| `run_translation(images=True)` | ಹೌದು | ಹೌದು | ಪ್ರೋಗ್ರಾಮಾತ್ಮಕ ಚಿತ್ರ ಅನುವಾದ. |
| `run_review(...)` | ಇಲ್ಲ | ಇಲ್ಲ | ಪ್ರೋಗ್ರಾಮಾತ್ಮಕ ನಿರ್ಧಾರಾತ್ಮಕ ಪರಿಶೀಲನೆ. |

## ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಗಳು

ಡೀಫಾಲ್ಟ್ ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್:

```text
translations/<language-code>/<source-relative-path>
```

ಡೀಫಾಲ್ಟ್ ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ಈ ಡೈರೆಕ್ಟರಿಗಳನ್ನು `translations_dir` ಮತ್ತು `image_dir` ಮೂಲಕ ಓವರ್‌ರೈಡ್ (override) ಮಾಡಬಹುದು.