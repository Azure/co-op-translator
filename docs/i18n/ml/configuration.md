# ക്രമീകരണം

Co-op Translator-ന് ഒരു ഭാഷാ മോഡൽ പ്രൊവൈഡർ ആവശ്യമാണ്. ചിത്ര വിവർത്തനത്തിനായി കൂടാതെ Azure AI Vision ആവശ്യമാണ്.

ക്രമീകരണം പരിസ്ഥിതി വ്യത്യസ്ഥികളിൽ നിന്ന് വായിച്ചെടുക്കും. പ്രാദേശിക പ്രോജക്ടുകൾക്കായി, അവ പ്രോജക്ട് റൂട്ടിലുള്ള `.env` ഫയലിൽ വെക്കുക.

For Azure resource setup, see [Azure AI ക്രമീകരണം](azure-ai-setup.md).

## പ്രാദേശിക റൺടൈം ക്രമീകരണം

CLI പ്രാദേശികമായി ഓടിക്കുന്നതിന് മുമ്പ് ഒരു വിർച്വൽ എൻവയോൺമെന്റ് ഉപയോഗിക്കുക. Co-op Translator Python 3.10 മുതൽ 3.12 വരെ പിന്തുണയ്ക്കുന്നു.

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

CLI ലഭിച്ചശേഷം, `.env`-ൽ ഒരു ഭാഷാ മോഡൽ പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യുക.

## പ്രൊവൈഡർ തിരഞ്ഞെടുപ്പ്

ഉപകരണം ഈ ക്രമത്തിൽ പ്രൊവൈഡറുകൾ ഓട്ടോ-ഡീറ്റക്ട് ചെയ്യുന്നു:

1. Azure OpenAI
2. OpenAI

ഏതെങ്കിലും പ്രൊവൈഡറും കോൺഫിഗർ ചെയ്തിട്ടില്ലെങ്കിൽ, `translate`, `evaluate`, `migrate-links`, and `run_translation` കോൺഫിഗറേഷൻ പരിശോദ്ധനകളിൽ പരാജയപ്പെടും. `co-op-review` and `run_review` നിശ്ചിതമായ മെയിന്റനൻസ് പരിശോധനകളാണ് ಮತ್ತು പ്രൊവൈഡർ ക്രെഡൻഷ്യൽസ് ആവശ്യപ്പെടുന്നില്ല.

## Azure OpenAI

നിങ്ങളുടെ മോഡൽ Azure AI Foundry-യിലോ Azure OpenAI Service-ലോ ഡിപ്ലോയ്ചെയ്തിരിക്കുന്നവയെങ്കിൽ Azure OpenAI ഉപയോഗിക്കുക.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

കണക്ടിവിറ്റി ചെക്ക് ട്രാൻസ്ലേഷൻ തുടങ്ങുന്നതിന് മുമ്പ് endpoint, API key, API version, deployment name എന്നിവ ഉപയോഗിക്കുന്നു.

## OpenAI

OpenAI API നേരിട്ട് വിളിക്കുമ്പോൾ OpenAI ഉപയോഗിക്കുക.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ഐച്ഛിക
OPENAI_BASE_URL="..."        # ഐച്ഛിക
```

`OPENAI_CHAT_MODEL_ID` ആവശ്യമാണ് കാരണം ട്രാൻസ്ലേറ്റർക്ക് API വിളികളിലേക്ക് ഒരു വ്യക്തമായ ചാറ്റ് മോഡൽ ആവശ്യമുണ്ട്.

## Azure AI Vision

ചിത്ര വിവർത്തനത്തിന് Azure AI Vision ആവശ്യമാണ്, ടൂൾ ചിത്രങ്ങളിൽ നിന്ന് ടെക്സ്റ്റ് പുറത്തെടുക്കാൻ അത് ഉപയോഗിക്കുന്നു.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True`, അല്ലെങ്കിൽ content-type ഫിൽറ്റർ ഇല്ലെങ്കിൽ ചിത്ര വിവർത്തനം തിരഞ്ഞെടുത്തതായി ഉണ്ടെങ്കിൽ, ടൂൾ വിവർത്തനം ആരംഭിക്കുന്നതിന് മുമ്പ് Vision കോൺഫിഗറേഷൻ പരിശോധിക്കും.

## പല ക്രെഡൻഷ്യൽ സെറ്റുകളും

കോൺഫിഗറേഷൻ ലെയർ ഒരേ ഇൻഡക്സ് ഉപയോഗിച്ച് വേരിയബിളുകൾക്ക് സഫിക്‌സുകൾ ചേർക്കുന്നതിനാൽ பல ക്രെഡൻഷ്യൽ സെറ്റുകൾ പിന്തുണയ്ക്കുന്നു:

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

ഓരോ സെറ്റും സമ്പൂർണ്ണം ആകിരിക്കണം. നല്ല പ്രവര്‍ത്തനക്ഷമമായ സെറ്റ് സംവൃദ്ധി പുറത്തെടുക്കുന്നതിന് ഹെൽത്ത് ചെക്ക് തിരഞ്ഞെടുക്കും മുമ്പ് വിവർത്തനം തുടരും.

## കമാൻഡ് ആവശ്യങ്ങൾ

| കമാൻഡ് അല്ലെങ്കിൽ API | LLM ആവശ്യമാണ് | Vision ആവശ്യമാണ് | കുറിപ്പുകൾ |
| --- | --- | --- | --- |
| `translate -md` | അതെ | ഇല്ല | Markdown മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate -nb` | അതെ | ഇല്ല | നോട്ട്‌ബുക്കുകൾ മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate -img` | അതെ | അതെ | ചിത്രങ്ങൾ മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate` with no type flags | അതെ | അതെ | ഡീഫോൾട്ട് മോഡിൽ Markdown, നോട്ട്‌ബുക്കുകൾ, ചിത്രങ്ങൾ എന്നിവ ഉൾക്കൊള്ളുന്നു. |
| `evaluate` | അതെ | ഇല്ല | `--fast` തിരഞ്ഞെടുക്കപ്പെട്ടില്ലെങ്കിൽ LLM മൂല്യനിർണയം ഉപയോഗിക്കുന്നു. |
| `migrate-links` | അതെ | ഇല്ല | ലിങ്ക് മൈഗ്രേഷൻ നടന്ന്, പക്ഷേ പങ്കിട്ട കോൺഫിഗറേഷൻ പരിശോധനകളും ഇപ്പോഴും ഓടുന്നു. |
| `co-op-review` | ഇല്ല | ഇല്ല | നിശ്ചിത ഫലമുള്ള തർജ്ജമാ ഘടന, പുതുതല പരിശോധന, Markdown, നോട്ട്‌ബുക്ക്, പ്രാദേശിക ലിങ്ക് പരിശോധനകൾ ഓടിക്കുന്നു. |
| `run_translation(markdown=True)` | അതെ | ഇല്ല | പ്രോഗ്രാമാറ്റിക് Markdown വിവർത്തനം. |
| `run_translation(images=True)` | അതെ | അതെ | പ്രോഗ്രാമാറ്റിക് ചിത്ര വിവർത്തനം. |
| `run_review(...)` | ഇല്ല | ഇല്ല | പ്രോഗ്രാമാറ്റിക് നിശ്ചിത ഫലമുള്ള റിവ്യൂ. |

## ഔട്ട്പുട്ട് ഡയറക്ടറികൾ

ഡീഫോൾട്ട് ടെക്സ്റ്റ് വിവർത്തന ഔട്ട്‌പുട്ട്:

```text
translations/<language-code>/<source-relative-path>
```

ഡീഫോൾട്ട് വിവർത്തനം ചെയ്ത ചിത്രം ഔട്ട്‌പുട്ട്:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ഈ ഡയറക്ടറികളെ `translations_dir` and `image_dir` ഉപയോഗിച്ച് ഓവർറൈഡ് ചെയ്യാം.