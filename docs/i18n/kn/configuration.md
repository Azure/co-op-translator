# ಸಂರಚನೆ

Co-op Translatorಗೆ ಒಂದು ಭಾಷಾ ಮಾದರಿ ಪ್ರೊವೈಡರ್ ಬೇಕಾಗಿದೆ. ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ ಜೊತೆಗೂಡಿಸಲಾಗಿ Azure AI Vision ಸಹ ಅಗತ್ಯವಿರುತ್ತದೆ.

ಸಂರಚನೆ ವಾತಾವರಣ ಮೌಲ್ಯಗಳಿಂದ ಓದಲಾಗುತ್ತದೆ. ಸ್ಥಳೀಯ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಗಾಗಿ, ಅವುಗಳನ್ನು ಪ್ರಾಜೆಕ್ಟ್ ಮೂಲದಲ್ಲಿ `.env` ಫೈಲ್‌ನಲ್ಲಿ ಇರಿಸಿ.

Azure ಸಂಪನ್ಮೂಲಗಳ ಸಂರಚನೆಗಾಗಿ, [Azure AI ಸೆಟಪ್](azure-ai-setup.md) ಅನ್ನು ನೋಡಿ.

## ಸ್ಥಳೀಯ ರನ್‌ಟೈಮ್ ಸೆಟ್‌ಅಪ್

ಸ್ಥಳೀಯವಾಗಿ CLI ರನ್ ಮಾಡುವ ಮೊದಲು ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಬಳಸಿ. Co-op Translator Python 3.10 ರಿಂದ 3.12 ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

ಸಾಮಾನ್ಯ CLI ಬಳಕೆಗೆ, ಪ್ರಕಟಿತ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವರ್ಚುವಲ್ ಪರಿಸರದಲ್ಲಿನೊಳಗೆ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

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

CLI ಲಭ್ಯವಾದ ನಂತರ, `.env` ನಲ್ಲಿ ಒಂದು ಭಾಷಾ ಮಾದರಿ ಪ್ರೊವೈಡರ್ ಅನ್ನು ಸಂರಚಿಸಿ.

## ಪ್ರೊವೈಡರ್ ಆಯ್ಕೆ

ಟೂಲ್ನು ಈ ಕ್ರಮದಲ್ಲಿ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಸ್ವಯಂ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ:

1. Azure OpenAI
2. OpenAI

ಎರಡೂ ಪ್ರೊವೈಡರ್‌ಗಳೂ ಸಂರಚಿಸಲ್ಪಟ್ಟಿಲ್ಲದಿದ್ದರೆ, `translate`, `evaluate`, `migrate-links`, ಮತ್ತು `run_translation` ಸಂರಚನೆ ಪರಿಶೀಲನೆಗಳ ವೇಳೆ ವಿಫಲವಾಗುತ್ತವೆ. `co-op-review` ಮತ್ತು `run_review` ನಿರ್ಧಾರಾತ್ಮಕ ನಿರ್ವಹಣಾ ಪರಿಶೀಲನೆಗಳಾಗಿದ್ದು, ಪ್ರೊವೈಡರ್ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ.

## Azure OpenAI

ನಿಮ್ಮ ಮಾದರಿ Azure AI Foundry ಅಥವಾ Azure OpenAI Service ನಲ್ಲಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಲಾಗಿದ್ದರೆ Azure OpenAI ಅನ್ನು ಬಳಸಿ.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ದೂರಸಂಪರ್ಕ ಪರಿಶೀಲನೆ ಅನುವಾದ ಪ್ರಾರಂಭವಾಗುವ ಮೊದಲು ಎಂಡ್ಪಾಯಿಂಟ್, API ಕೀ, API ಆವೃತ್ತಿ ಮತ್ತು ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ ಹೆಸರನ್ನು ಬಳಸುತ್ತದೆ.

## OpenAI

OpenAI API ಅನ್ನು ನೇರವಾಗಿ ಕರೆಮಾಡುವಾಗ OpenAI ಅನ್ನು ಬಳಸಿ.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ಐಚ್ಛಿಕ
OPENAI_BASE_URL="..."        # ಐಚ್ಛಿಕ
```

`OPENAI_CHAT_MODEL_ID` ಅವಶ್ಯಕವಾಗಿದೆ ಏಕೆಂದರೆ ಅನುವಾದಕಕ್ಕೆ API ಕರೆಗೆ ಸ್ಪಷ್ಟವಾದ ಚಾಟ್ ಮಾದರಿ ಬೇಕಾಗಿರುತ್ತದೆ.

## Azure AI Vision

ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ Azure AI Vision ಅಗತ್ಯವಾಗುತ್ತದೆ, ಏಕೆಂದರೆ ಟೂಲ್ ಅನುವಾದ ಮಾಡುವ ಮೊದಲು ಚಿತ್ರಗಳಿಂದ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ಚಿತ್ರ ಅನುವಾದವನ್ನು `-img`, `images=True`, ಅಥವಾ content-type ಫಿಲ್ಟರ್ ಇಲ್ಲದೆ ಆಯ್ಕೆ ಮಾಡಿದ್ದರೆ, ಟೂಲ್ಗೆ ಅನುವಾದ ಪ್ರಾರಂಭವಾಗುವ ಮೊದಲು Vision ಸಂರಚನೆಯನ್ನು ಮಾನ್ಯಗೊಳಿಸುತ್ತದೆ.

## ಬಹು ಪ್ರಮಾಣಪತ್ರ ಸೆಟ್‌ಗಳು

ಸಂರಚನಾ ಪದರವು ಒಂದೇ ಸೂಚ್ಯಂಕವನ್ನು ಚರಗಳ ಹೆಸರಿನ ಕೊನೆಯಲ್ಲಿ ಸೇರಿಸುವ ಮೂಲಕ ಬಹು ಪ್ರಮಾಣಪತ್ರ ಸೆಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ:

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

ಪ್ರತಿ ಸೆಟ್ ಪೂರ្នកೃತವಾಗಿರಬೇಕು. ಅನುವಾದ ಮುಂದುವರಿಯುವ ಮೊದಲು ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ (health check) ಒಂದು ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಸೆಟ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತದೆ.

## ಕಮಾಂಡ್ ಅವಶ್ಯಕತೆಗಳು

| ಕಮಾಂಡ್ ಅಥವಾ API | LLM ಅಗತ್ಯವಿದೆ | Vision ಅಗತ್ಯವಿದೆ | ಟಿಪ್ಪಣಿಗಳು |
| --- | --- | --- | --- |
| `translate -md` | ಹೌದು | ಇಲ್ಲ | Markdown ಮಾತ್ರ ಅನುವಾದ ಮಾಡುತ್ತದೆ. |
| `translate -nb` | ಹೌದು | ಇಲ್ಲ | ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಮಾತ್ರ ಅನುವಾದ ಮಾಡುತ್ತದೆ. |
| `translate -img` | ಹೌದು | ಹೌದು | ಚಿತ್ರಗಳನ್ನು ಮಾತ್ರ ಅನುವಾದ ಮಾಡುತ್ತದೆ. |
| `translate` with no type flags | ಹೌದು | ಹೌದು | ಡೀಫಾಲ್ಟ್ ಮೋಡ್‌ನಲ್ಲಿ Markdown, ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳು ಸೇರಿವೆ. |
| `evaluate` | ಹೌದು | ಇಲ್ಲ | `--fast` ಆಯ್ಕೆಮಾಡದವರೆಗೆ LLM ಮೌಲ್ಯಮಾಪನವನ್ನು ಬಳಸುತ್ತದೆ. |
| `migrate-links` | ಹೌದು | ಇಲ್ಲ | ಲಿಂಕ್ ಮೈಸಗ್ರೇಷನ್ ನಿರ್ವಹಿಸುತ್ತದೆ, ಆದರೆ ಹಂಚಿಕೊಂಡ ಸಂರಚನೆ ಪರಿಶೀಲನೆಗಳನ್ನು ಇನ್ನೂ ನಡೆಸುತ್ತದೆ. |
| `co-op-review` | ಇಲ್ಲ | ಇಲ್ಲ | ನಿರ್ಧಾರಾತ್ಮಕ ಅನುವಾದ ರಚನೆ, ತಾಜಾತನ, Markdown, ನೋಟ್ಬುಕ್ ಮತ್ತು ಸ್ಥಳೀಯ ಲಿಂಕ್ ಪರಿಶೀಲನೆಗಳನ್ನು ನಡೆಸುತ್ತದೆ. |
| `run_translation(markdown=True)` | ಹೌದು | ಇಲ್ಲ | ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕ್ Markdown ಅನುವಾದ. |
| `run_translation(images=True)` | ಹೌದು | ಹೌದು | ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕ್ ಚಿತ್ರ ಅನುವಾದ. |
| `run_review(...)` | ಇಲ್ಲ | ಇಲ್ಲ | ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕ್ ನಿರ್ಧಾರಾತ್ಮಕ ವಿಮರ್ಶೆ. |

## ಔಟ್‌ಪುಟ್ ಡೈರೆಕ್ಟರಿಗಳು

ಡೀಫಾಲ್ಟ್ ಪಠ್ಯ ಅನುವಾದ ಔಟ್‌ಪುಟ್:

```text
translations/<language-code>/<source-relative-path>
```

ಡೀಫಾಲ್ಟ್ ಅನುವಾದಿತ ಚಿತ್ರ ಔಟ್‌ಪುಟ್:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ಈ ಡೈರೆಕ್ಟರಿಗಳನ್ನು `translations_dir` ಮತ್ತು `image_dir` ಬಳಸಿ ಓವರ್‌ರೈಡ್ ಮಾಡಬಹುದು.