# ക്രമീകരണം

Co-op Translatorക്ക് ഒരു ഭാഷാ മോഡൽ പ്രൊവൈഡർ ആവശ്യം ഉണ്ട്. ചിത്രം വിവർത്തനത്തിന് അധികമായി Azure AI Vision ആവശ്യമാണ്.

ക്രമീകരണങ്ങൾ പരിസ്ഥിതി വ്യരിയബിളുകളിൽ നിന്ന് വായിക്കുന്നു. ലോക്കൽ പ്രോജക്റ്റുകൾക്കുവേണ്ടി, അവ പ്രോജക്റ്റ് റൂട്ടിൽ 있는 `.env` ഫയലിൽ ഇടുക.

Azure ресурс സജ്ജീകരണങ്ങൾക്ക്, [Azure AI ക്രമീകരണം](azure-ai-setup.md) കാണുക.

## ലൊക്കൽ റൺടൈം ക്രമീകരണം

ലോകലായി CLI പ്രവർത്തിപ്പിക്കുന്നതിന് മുമ്പ് ഒരു virtual environment ഉപയോഗിക്കുക. Co-op Translator Python 3.11 മുതൽ 3.14 വരെ പിന്തുണയ്ക്കുന്നു.

സാധാരണ CLI ഉപയോഗത്തിനായി, പ്രസിദ്ധീകരിച്ച പാക്കേജ് ഒരു virtual environment-ഇൽ ഇൻസ്റ്റാൾ ചെയ്യുക:

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

### റിപോസിറ്ററി വികസനം

റിപോസിറ്ററി വികസനത്തിനായി, പ്രോജക്ട് റൂട്ടിൽ നിന്നാണ് ഡിപ്പെൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യേണ്ടത്:

```bash
poetry install
poetry run translate --help
```

CLI ലഭ്യമായ ശേഷം, `.env` ഫയലിൽ ഒരു ഭാഷാ മോഡൽ പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യുക.

## പ്രൊവൈഡർ തിരഞ്ഞെടുപ്പ്

ടൂൾ ഈ ക്രമത്തിൽ പ്രൊവൈഡറുകൾ സ്വയം കണ്ടെത്തും:

1. Azure OpenAI
2. OpenAI
3. Anthropic

വിവർത്തനത്തിന് പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ആവശ്യമുണ്ട്, എന്നാൽ `translate -l "ko" -md --dry-run` പോലുള്ള മുൻവീക്ഷണങ്ങൾക്ക് ബാധകമല്ല. `migrate-links`, `co-op-review`, மற்றும் `run_review` നിർണ്ണായക പരിപാലന പ്രവർത്തനങ്ങളാണ്; അവയ്ക്ക് പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ不要.

## മോഡൽ ക്ലയന്റ് ബാക്ക്എൻഡ്

Co-op Translator 0.22.0 മുതൽ Azure OpenAI, OpenAI, Anthropic എന്നിവ ഡീഫോൾട്ട് ആയി Microsoft Agent Framework ഉപയോഗിക്കുന്നു. സാധാരണ ഉപയോഗത്തിന് ബാക്ക്എൻഡ് സജ്ജീകരണം ആവശ്യമാണ് എന്നില്ല.

പൊരുത്തത്തിനായി Semantic Kernel താൽക്കാലികമായി ലഭ്യമാണ്. അതിനെ വ്യക്തമായി തിരഞ്ഞെടുക്കാൻ, സജ്ജീകരിക്കുക:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel ഉപയോഗിക്കുന്നത് ഡിപ്രീക്കേഷൻ മുന്നറിയിപ്പ് ഉൽപാദിപ്പിക്കും. പാക്കേജ് Semantic Kernel-നെ 0.23.0-ൽ ഐച്ഛിക ഡീപെൻഡൻസിയായി മാറ്റാൻ പദ്ധതിയിടുന്നുണ്ട്, കൂടാതെ 0.24.0-ൽ ഇന്റഗ്രേഷൻ നീക്കംചെയ്യാൻ ഉദ്ദേശിക്കുന്നതാണ്, പൊരുത്ത പരിശോധന ഫലങ്ങളുടെ വിപണിയും ഉപഭോക്തൃ ഫീഡ്ബാക്കും ആശ്രയിച്ചാണ് ഇത്. Anthropic-യ്ക്ക് `agent-framework` ആവശ്യമാണ്; Anthropic-നൊപ്പം വ്യക്തമായി `semantic-kernel` തിരഞ്ഞെടുക്കാൻ ശ്രമിച്ചാൽ കോൺഫിഗറേഷൻ പിശകോടെ പരാജയമാകും. അസാധുവായ മൂല്യങ്ങൾ ശബ്ദരഹിതമായി fallback ചെയ്യാനുള്ള പകരം provider-backed translator initialization സമയത്ത് പരാജയപ്പെടും. റോളൗട്ട് പിന്തുടരുകയും തടസ്സങ്ങൾ [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) ൽ റിപ്പോർട്ട് ചെയ്യുക.

## Azure OpenAI

നിങ്ങളുടെ മോഡൽ Azure AI Foundry അല്ലെങ്കിൽ Azure OpenAI Service-ൽ ഡിപ്ലോയുചെയ്തിട്ടുണ്ടെങ്കിൽ Azure OpenAI ഉപയോഗിക്കുക.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

വിവർത്തനം ആരംഭിക്കുന്നതിന് മുന്‍പ് കണക്ടിവിറ്റി ചെക്ക് endpoint, API key, API version, deployment name എന്നിവ ഉപയോഗിച്ച് നടത്തും.

## OpenAI

OpenAI API നേരിട്ട് വിളിക്കുമ്പോൾ OpenAI ഉപയോഗിക്കുക.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ആവശ്യമാണ് കാരണം ട്രാൻസ്ലേറ്റർ API കോൾസ് സമ്പാദിപ്പിക്കാൻ വ്യക്തമായ ഒരു ചാറ്റ് മോഡൽ ആവശ്യപ്പെടുന്നു.

ഡീഫോൾട്ട് സെറ്റപ്പിനായി `OPENAI_ORG_ID` மற்றும் `OPENAI_BASE_URL` unset ആയി bırakൂ. നിങ്ങളുടെ അക്കൗണ്ടിന് ഓർഗനൈസേഷൻ ID ആവശ്യമായെങ്കിൽ മാത്രം ചേർക്കുക, അല്ലെങ്കിൽ കസ്റ്റം എൻഡ്പോയിന്റ് ഉപയോഗിക്കുമ്പോഴേ base URL സജ്ജീകരിക്കുക. ഐച്ഛിക സജ്ജീകരണങ്ങൾക്ക് placeholder മൂല്യങ്ങൾ കോപ്പി ചെയ്യരുത്.

## Anthropic Claude

Claude API നേരിട്ട് വിളിക്കുമ്പോൾ Anthropic ഉപയോഗിക്കുക. [Anthropic API key](https://platform.claude.com/docs/en/get-started) ഉണ്ടാക്കിയെടുക്കുക, കൂടാതെ പിന്തുണയുള്ള [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) തിരഞ്ഞെടുക്കുക.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY`നും `ANTHROPIC_MODEL`നും ആവശ്യമുണ്ട്. `CO_OP_TRANSLATOR_MODEL_CLIENT` സജ്ജീകരിക്കേണ്ടതില്ല; ഡീഫോൾട്ട് ബാക്ക്എൻഡ് ആയി Agent Framework ആണ്.

Anthropic API-ക്കായി `ANTHROPIC_BASE_URL` unset ആയിരിക്കണം. കസ്റ്റം എൻड്പോയിന്റ് ഉപയോഗിക്കുമ്പോഴേ അത് സജ്ജീകരിക്കുക.

`ANTHROPIC_MAX_TOKENS` ന്റെ ഡീഫോൾട്ട് മൂല്യം `8192` ആണ്, ഇത് Meitei Mayek പോലുള്ള ടോക്കൺ ധാരാളമായ സ്ക്രിപ്റ്റുകൾക്കായി സ്ഥലം bırakൂ. നിങ്ങളുടെ മോഡൽ അല്ലെങ്കിൽ Anthropic-അനുകൂല എൻഡ്പോയിന്റ് ഔട്ട്‌പുട്ട് അതിന് താഴെയേ മടക്കുകയാണെങ്കിൽ ഇതിന്റെ മൂല്യം കുറഞ്ഞു സജ്ജീകരിക്കുക.

## Azure AI Vision

ചിത്രം വിവർത്തനത്തിനായി Azure AI Vision ആവശ്യമാണ്, കാരണം ടൂൾ നേരത്തെ കോൺഫിഗർ ചെയ്‌ത ഭാഷാ മോഡൽ വിവർത്തനം തുടങ്ങാനായി ഇമേജുകളിൽ നിന്നുള്ള ടെക്സ്റ്റ് എക്സ്ട്രാക്ട് ചെയ്യേണ്ടതുണ്ട്. Anthropic നിർത്ഥമായും Azure OpenAI അല്ലെങ്കിൽ OpenAI പോലെയേ എക്സ്ട്രാക്ട് ചെയ്ത ടെക്സ്റ്റ് വിവർത്തനം ചെയ്യാൻ കഴിയും.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True` ഉപയോഗിച്ചോ, അല്ലെങ്കിൽ content-type ഫിൽട്ടർ ഇല്ലാതെയോ ഇമേജ് വിവർത്തനം തിരഞ്ഞെടുക്കപ്പെട്ടാൽ, ടൂൾ വിവർത്തനം ആരംഭിക്കുന്നതിന് മുന്‍പ് Vision കോൺഫിഗറേഷൻ സാധുത പരിശോധിക്കും.

## ഒന്നിലധികം ക്രെഡൻഷ്യൽ സെറ്റുകൾ

കോൺഫിഗറേഷൻ ലെയർ ഒരേ ഇൻഡക്സുള്ള സഫിക്സ് ചേർക്കുന്നതിലൂടെ ഒന്നിലധികം ക്രെഡൻഷ്യൽ സെറ്റുകൾ പിന്തുണയ്ക്കുന്നു:

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

ഓരോ സെറ്റും പൂര്‍ണമായിരിക്കണം. ഹെൽത്ത് ചെക്ക് വിവർത്തനം തുടരുന്നതിന് മുമ്പ് പ്രവർത്തനക്ഷമമായ ഒരു സെറ്റ് തിരഞ്ഞെടുക്കും.

OpenAIയും Anthropicയും അതേ സഫിക്സ് സങ്കേതം പിന്തുടരുന്നു. ഒരു ക്രെഡൻഷ്യൽ സെറ്റിലെ എല്ലാ വ്യരിയബിളുകളും ഒരേ സഫിക്സിൽ रखें, `OPENAI_BASE_URL_1` അല്ലെങ്കിൽ `ANTHROPIC_BASE_URL_1` പോലുള്ള ഐച്ഛിക മൂല്യങ്ങളും ഉൾപ്പെടെ.

## കമാൻഡ് ആവശ്യകതകൾ

| കമാൻഡ് അല്ലെങ്കിൽ API | LLM ആവശ്യമാണ് | Vision ആവശ്യമാണ് | കുറിപ്പുകൾ |
| --- | --- | --- | --- |
| `translate -md` | അയഥെ | ഇല്ല | Markdown മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate -nb` | അയഥെ | ഇല്ല | നോട്ട്ബുക്കുകൾ മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate -img` | അയഥെ | അയഥെ | ചിത്രങ്ങൾ മാത്രം വിവർത്തനം ചെയ്യുന്നു. |
| `translate` with no type flags | അയഥെ | അയഥെ | ഡീഫോൾട്ട് മോഡ് Markdown, നോട്ട്ബുക്കുകൾ, ചിത്രങ്ങൾ എന്നിവ ഉൾക്കൊള്ളുന്നു. |
| `evaluate` | അയഥെ | ഇല്ല | `--fast` തിരഞ്ഞെടുക്കണമെങ്കിൽ ഒഴിച്ച് LLM മൂല്യനിർണയം ഉപയോഗിക്കും. |
| `migrate-links` | ഇല്ല | ഇല്ല | പ്രൊവൈഡർ കോളുകൾ ഇല്ലാതെ ലോക്കൽ ലിങ്ക് മാറ്റം നിർവഹിക്കുന്നു. |
| `co-op-review` | ഇല്ല | ഇല്ല | നിശ്ചിതമായ വിവർത്തന ഘടന, താജ്യത, Markdown, നോട്ട്ബുക്ക്, ലോക്കൽ ലിങ്ക് പരിശോധനകൾ നടത്തുന്നു. |
| `run_translation(markdown=True)` | അയഥെ | ഇല്ല | പ്രോഗ്രാമാറ്റിക് Markdown വിവർത്തനം. |
| `run_translation(images=True)` | അയഥെ | അയഥെ | പ്രോഗ്രാമാറ്റിക് ഇമേജ് വിവർത്തനം. |
| `run_review(...)` | ഇല്ല | ഇല്ല | പ്രോഗ്രാമാറ്റിക് നിർണ്ണായക റിവ്യൂ. |

## ഔട്ട്‌പുട്ട് ഡയറക്ടറികൾ

ഡീഫോൾട്ട് ടെക്സ്റ്റ് വിവർത്തന ഔട്ട്‌പുട്ട്:

```text
translations/<language-code>/<source-relative-path>
```

ഡീഫോൾട്ട് വിവർത്തനചെയ്ത ഇമേജ് ഔട്ട്‌പുട്ട്:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ഈ ഡയറക്ടറികൾ `translations_dir` և `image_dir` ഉപയോഗിച്ച് ഓവർറൈഡ് തീർക്കാൻ കഴിയും.