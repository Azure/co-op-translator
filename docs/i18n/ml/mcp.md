# MCP സർവർ

Co-op Translator ഏജന്റുകൾക്കും എഡിറ്റർമാർക്കും MCP-ഓപ്പം പ്രവർത്തിക്കാവുന്ന ക്ലയന്റുകൾക്കും വേണ്ടി ഒരു Model Context Protocol സർവർ ഉൾക്കൊള്ളിക്കുന്നു.

ഡീഫോൾട്ട് ലോക്കൽ സെറ്റ്‌‌അപ്പിനായി, ഉപയോക്താക്കൾ ഹസ്തപരമായി വേർതിരിച്ചൊരു സർവർ പ്രവർത്തിപ്പിക്കണമെന്നില്ല. അവർ അവരുടെ MCP ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുകയും, ക്ലയന്റ് Co-op Translator ടൂളുകൾ ആവശ്യമായപ്പോൾ `stdio` വഴി സ്വയം `co-op-translator-mcp` ആരംഭിക്കുകയും ചെയ്യുന്നു.

CLI, Python API, MCP എന്നിവയിൽ നിന്ന് തിരഞ്ഞെടുക്കാൻ നോക്കുന്നുവെങ്കിൽ, [നിങ്ങളുടെ വർക്ക്‌ഫ്ലോ തിരഞ്ഞെടുക്കുക](workflows.md) എന്നത് ആരംഭിക്കാൻ ഉത്തമമാണ്.

ഏജന്റ് അല്ലെങ്കിൽ എഡിറ്റർ Co-op Translator നെ നേരിട്ട് വിളിക്കേണ്ടതുള്ളപ്പോൾ MCP ഉപയോഗിക്കുക:

| ഉപയോക്താവിന്റെ ലക്ഷ്യം | MCP ടൂളുകൾ |
| --- | --- |
| ഒരു Markdown ഡോക്യുമെന്റ്, നോട്ട്‌ബുക്ക് അല്ലെങ്കിൽ ചിത്രം വിവർത്തനം ചെയ്യുക | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ഹോസ്റ്റ് ഏജന്റ് മോഡൽ ഉപയോഗിച്ച് Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ഉള്ളടക്കം വിവർത്തനം ചെയ്യുക | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ഔട്ട്പുട്ട് പാത തിരഞ്ഞെടുക്കുമ്പോൾ വിവർത്തനം ചെയ്ത Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ലിങ്കുകൾ പുനഃലേഖനം ചെയ്യുക | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI പോലെയുള്ള രീതിയിൽ മുഴുവൻ റിപ്പോസിറ്ററി വിവർത്തനവും നടത്തുക | `run_translation`, `translate_project` |
| LLM ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ വിവർത്തനം ചെയ്ത ഔട്ട്പുട്ട് റിവ്യൂ ചെയ്യുക | `run_review` |
| കാര്യക്ഷമതകളും പരിസ്ഥിതി സ്ഥിതിവിവരങ്ങളും പരിശോധിക്കുക | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP സർവർ [Python API](api.md) ലെ രേഖപ്പെടുത്തിയതേയും പേരിലുള്ള പൊതു Python API-യേയും കവർ ചെയ്യുന്നു. Provider-backed ടൂളുകൾ CLI-യും Python API-യും ഉപയോഗിക്കുന്നതേ മാത്രമുള്ള കോൺഫിഗർ ചെയ്ത പ്രൊവൈഡറുകളേയാണ് ഉപയോഗിക്കുന്നത്. ഏജന്റ്-സഹായിത ടൂളുകൾ MCP ഹോസ്റ്റ് ഏജന്റിന് വിവർത്തനം ചെയ്യാൻ ചങ്കുകൾ തയ്യാറാക്കുകയും, തുടർന്ന് Co-op Translator ഉപയോഗിച്ച് അന്തിമ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് പുനഃരൂപീകരിക്കുകയും ചെയ്യുന്നു.

## ഘട്ടം 1: Co-op Translator ഇൻസ്റ്റാൾ ചെയ്ത് കോൺഫിഗർ ചെയ്യുക

നിങ്ങളുടെ MCP ക്ലയന്റ് ഉപയോഗിക്കുന്ന Python പരിസ്ഥിതിയിൽ Co-op Translator ഇൻസ്റ്റാൾ ചെയ്യുക:

```bash
pip install co-op-translator
```

ഈ റിപോസിറ്ററിയിൽ നിന്നുള്ള ലോക്കൽ ഡെവലപ്പ്മെന്റിനായി, പാക്കേജ് എഡിറ്റബിൾ മോഡിൽ ഇൻസ്റ്റാൾ ചെയ്യുക:

```bash
pip install -e .
```

നിങ്ങളുടെ MCP ക്ലയന്റ് ഉപയോഗിക്കാവുന്ന വിവർത്തന മോഡ് തിരഞ്ഞെടുക്കുക:

| മോഡ് | ഇതിനു ഉപയോഗിക്കുക | ക്രെഡൻഷ്യലുകൾ |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, അല്ലെങ്കിൽ `run_translation` വിളിക്കുമ്പോൾ. | Markdown & നോട്ട്‌ബുക്ക് വിവർത്തനത്തിന് Azure OpenAI അല്ലെങ്കിൽ OpenAI വേണം. ചിത്രം വിവർത്തനത്തിന് Azure AI Vision കൂടി വേണം. |
| Agent-assisted | MCP ഹോസ്റ്റ് ഏജന്റ് `start_markdown_agent_translation` അല്ലെങ്കിൽ `start_notebook_agent_translation` റിട്ടേൺ ചെയ്യുന്ന ചങ്കുകൾ വിവർത്തനം ചെയ്യും. | Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ചങ്കുകൾക്ക് Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ആവശ്യമില്ല. ചിത്ര വിവർത്തനം ഇപ്പോഴും ഏജന്റ്-സഹായിത മോഡിൽ ഉൾപ്പെടുന്നില്ല. |

Codex അല്ലെങ്കിൽ Claude Code പോലുള്ള ഒരു ഏജന്റിനുള്ളിൽ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് വിവർത്തനത്തോടെ ആരംഭിക്കുന്നുണ്ടെങ്കിൽ, ഏജന്റ്-സഹായിത മോഡിൽ ആരംഭിക്കുക. Co-op Translator സ്വയം നിങ്ങളുടെ കോൺഫിഗർ ചെയ്ത പ്രൊവൈഡറുകളെ വിളിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നപ്പോൾ, ചിത്രങ്ങൾ വിവർത്തനം ചെയ്യുമ്പോൾ, അല്ലെങ്കിൽ CLI പോലെയുള്ള റിപ്പോസിറ്ററി-തത്വത്തിലുള്ള വിവർത്തനം നടത്തുമ്പോൾ provider-backed മോഡ് ഉപയോഗിക്കുക.

Provider-backed വർക്ക്‌ഫ്ലോകൾക്കായിച്ചേ ക്രെഡൻഷ്യലുകൾ കോൺഫിഗർ ചെയ്യുക:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed ചിത്രം വിവർത്തനത്തിന് മേൽതെരുവിൽ തന്നെയുള്ളതും ആവശ്യമാണ്:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ഏജന്റ്-സഹായിത മോഡ് നിലവിൽ Markdown ۽ നോട്ട്‌ബുക്ക് Markdown സെല്ലുകൾ വരെ മാത്രം കവർ ചെയ്യുന്നു. ചിത്രം വിവർത്തനം ഇപ്പോഴും provider-backed image പൈപ്പ്‌ലൈൻ ഉപയോഗിക്കുന്നു, OCRക്കും ലേയൗട്ട്-അവബോധമുള്ള റെൻഡറിംഗിനും Azure AI Vision ആവശ്യമാണ്.

## ഘട്ടം 2: നിങ്ങളുടെ MCP ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുക

സാധാരണ ലോക്കൽ `stdio` സെറ്റ്‌അപ്പിനായി, MCP ക്ലയന്റ് കോൺഫിഗറേഷനിൽ Co-op Translator ചേർക്കുക. ക്ലയന്റ് പ്രക്രിയ സ്വയം ആരംഭിക്കുകയും നിർത്തുകയും ചെയ്യും.

ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജ് കോൺഫിഗറേഷൻ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows-ൽ സോഴ്സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS അല്ലെങ്കിൽ Linux-യിൽ സോഴ്സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP ക്ലയന്റ് കോൺഫിഗർ മാറ്റിയശേഷം, ക്ലയന്റ് പുതിയ സർവർ കണ്ടെത്താൻ റസ്റ്റാർട്ട് അല്ലെങ്കിൽ റീലോഡ് ചെയ്യുക.

## ഘട്ടം 3: ക്ലയന്റിൽ സർവർ സ്ഥിരീകരിക്കുക

ലഭ്യമായ ടൂളുകൾ പട്ടികപ്പെടുത്തിയെടുക്കാൻ MCP ക്ലയന്റോട് പറയുക, അല്ലെങ്കിൽ ആദ്യം ഒരു റീഡ്-ഓൺലി ഹെൽപ്പർ കോൾ ചെയ്യുക:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ഉപയോഗപ്രദമായ ആദ്യ പരിശോധനകൾ:

| ടൂൾ | എന്താണ് പരിശോധിക്കേണ്ടത് |
| --- | --- |
| `get_api_overview` | സർവർ എത്താവുന്നതാണോ എന്നു സ്ഥിരീകരിക്കുകയും ലഭ്യമായ വർക്ക്‌ഫ്ലോകൾ കാണിക്കുകയും ചെയ്യുന്നു. |
| `list_supported_languages` | പാക്കേജുചെയ്ത ഭാഷാ ഡാറ്റ ലോഡ് ചെയ്യാൻ കഴിയുന്നുണ്ടോ എന്ന് സ്ഥിരീകരിക്കുന്നു. |
| `get_configuration_status` | രഹസ്യ മൂല്യങ്ങൾ പുറത്തെടുക്കാതെ LLM & Vision പ്രൊവൈഡറുകളുടെ ലഭ്യത സ്ഥിരീകരിക്കുന്നു. |

## ഘട്ടം 4: ഒരു വർക്ക്‌ഫ്ലോ തിരഞ്ഞെടുക്കുക

### വ്യക്തിഗത ഫയലുകൾ അല്ലെങ്കിൽ ഡോക്യുമെന്റുകൾ വിവർത്തനം ചെയ്യുക

MCP ക്ലയന്റിന് ഡോക്യുമെന്റ് ഉള്ളടക്കമോ ചിത്രം പാതയോ ഇതിനകം ഉണ്ട് എന്നായുളള പക്ഷം Co-op Translator കോൺഫിഗർ ചെയ്ത പ്രൊവൈഡറുകളെ വിളിക്കേണ്ടത് എന്നാവുന്നതിനാൽ provider-backed ഉള്ളടക്ക ടൂളുകൾ ഉപയോഗിക്കുക.

Markdown కోసం:

1. `document`, `language_code`, ആവശ്യമെങ്കിൽ `source_path` കൊടുത്തുകൊണ്ട് `translate_markdown_content` കോൾ ചെയ്യുക.
2. വിവർത്തനം ചെയ്ത ഫലത്തെ Co-op Translator ഔട്ട്പുട്ട് ലേയൗട്ടിലേക്ക് എഴുതാൻ നിങ്ങൾ പദ്ധതിയിടുകയാണെങ്കിൽ `rewrite_markdown_paths` കോൾ ചെയ്യുക.
3. ക്ലയന്റ് അന്തിമ `content` എഴുതുകയോ തിരിച്ചുനൽകുകയോ ചെയ്യട്ടെ.

നോട്ട്‌ബുക്ക്‌സിനായി:

1. നോട്ട്‌ബുക്ക് JSON-ഉം `language_code`ഉം ഒప്ഷനായി കൊടുത്ത് `translate_notebook_content` കോൾ ചെയ്യുക.
2. ലക്ഷ്യപാതയ്‌ക്കായി വിവർത്തനം ചെയ്ത നോട്ട്‌ബുക്ക് ലിങ്കുകൾ ക്രമബദ്ധമാക്കേണ്ടതുണ്ടെങ്കിൽ `rewrite_notebook_paths` കോൾ ചെയ്യുക.
3. അന്തിമ നോട്ട്‌ബുക്ക് JSON എഴുതുകയോ തിരിച്ചുനൽകുകയോ ചെയ്യുക.

ചിത്രങ്ങൾക്കായി:

1. `image_path`, `language_code`, അതോടൊപ്പം ഓപ്ഷണൽ `root_dir` അല്ലെങ്കിൽ `fast_mode` கொടുക്കിയാണ് `translate_image_content` കോൾ ചെയ്യുക.
2. റിട്ടേൺ ചെയ്‌ത `data_base64`യും `mime_type`ഉം വായിക്കുക.
3. `output_path` നൽകിയാൽ, വിവർത്തനം ചെയ്ത ചിത്രം ആ പാതയിലും സേവ് ചെയ്യും.

ഉള്ളടക്ക ടൂളുകൾ പ്രോജക്ട് കണ്ടെത്തൽ, മെടാഡേറ്റാ അപ്‌ഡേറ്റുകൾ, ഡിസ്ക്ലെയിമറുകൾ, അല്ലെങ്കിൽ സ്വയംപാത പുനഃലേഖനം എന്നിവ നടത്തി കൊളയില്ല. Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ ഹോസ്റ്റ് ഏജന്റ് Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ചങ്കുകൾ വിവർത്തനം ചെയ്യണമെന്ന് നിങ്ങൾ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, താഴെയുള്ള ഏജന്റ്-സഹായിത വർക്ക്‌ഫ്ലോ ഉപയോഗിക്കുക.

### ഹോസ്റ്റ് ഏജന്റ് മോഡൽ ഉപയോഗിച്ച് വിവർത്തനം ചെയ്യുക

Co-op Translatorക്ക് Azure OpenAI അല്ലെങ്കിൽ OpenAI കോൺഫിഗർ ചെയ്യുന്നത് ഒഴിവാക്കാൻ, ഹോസ്റ്റ് ഏജന്റ് (ഒരു കോഡിംഗ് അസിസ്റ്റന്റ് പോലുള്ള) തയാറാക്കുന്ന വിവർത്തന ടെക്സ്റ്റ് ഉപയോഗിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുമ്പോൾ ഏജന്റ്-സഹായിത ടൂളുകൾ ഉപയോഗിക്കുക.

ചാറ്റ്-അഡ്ഭുത MCP ക്ലയന്റിൽ, സാധാരണയായി നിങ്ങൾ ടൂൾ JSON സ്വമേധയാ എഴുതേണ്ടതില്ല. ഏജന്റ്-സഹായിത വർക്ക്‌ഫ്ലോ ഉപയോഗിക്കാൻ ഏജന്റിന് പറയുക:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

നോട്ട്‌ബുക്കുകൾക്കായി സമാന പാറ്റേൺ ഉപയോഗിക്കുക:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

നിങ്ങളുടെ MCP ക്ലയന്റ് സെർച്ചർവ് പ്രോംപ്റ്റുകൾ പിന്തുണച്ചാൽ, അതേ വർക്ക്‌ഫ്ലോ നിർദേശങ്ങൾ ലോഡ് ചെയ്യാൻ `agent_assisted_markdown_translation_prompt` ഉപയോഗിക്കുക.

Markdown വേണ്ടി:

1. `document`, `language_code`, ആവശ്യമായെങ്കിൽ `source_path` കൊടുക്കുക `start_markdown_agent_translation` കോൾ ചെയ്യുക.
2. ഓരോ റിട്ടേൺ ചെയ്തത് ചങ്കും ഹോസ്റ്റ് ഏജന്റിൽ chunk `prompt` പിന്തുടർന്ന് വിവർത്തനം ചെയ്യുക.
3. യഥാർത്ഥ `job` ഒപ്പം `chunk_id`യും `translated_text`ഉം ഉപയോഗിച്ച് വിവർത്തനം ചെയ്ത ചങ്കുകൾക്കൊപ്പം `finish_markdown_agent_translation` കോൾ ചെയ്യുക.
4. ഉള്ളടക്കം വിവർത്തനം ചെയ്ത ലക്ഷ്യപാതയിൽ എഴുതilecek ആണെങ്കിൽ `rewrite_markdown_paths` കോൾ ചെയ്യുക.

നോട്ട്‌ബുക്കുകൾക്കായി:

1. നോട്ട്‌ബുക്ക് JSON കൂടി `language_code` കൊടുത്ത് `start_notebook_agent_translation` കോൾ ചെയ്യുക.
2. ഓരോ റിട്ടേൺ ചെയ്ത ചങ്കും ഹോസ്റ്റ് ഏജന്റിൽ വിവർത്തനം ചെയ്യുക.
3. യഥാർത്ഥ `job` ഒപ്പം വിവർത്തനം ചെയ്ത ചങ്കുകൾ ഉപയോഗിച്ച് `finish_notebook_agent_translation` കോൾ ചെയ്യുക.
4. വിവർത്തനം ചെയ്ത നോട്ട്‌ബുക്ക് ലിങ്കുകൾക്കായി ടാർഗറ്റ്-പാത്ത് ക്രമീകരണം ആവശ്യമായെങ്കിൽ `rewrite_notebook_paths` കോൾ ചെയ്യുക.

ഏജന്റ്-സഹായിത ടൂളുകൾ Co-op Translator-ൽ നിന്നു Azure OpenAI അല്ലെങ്കിൽ OpenAI കോൾ ചെയ്യുകയില്ല. റിട്ടേൺ ചെയ്യുന്ന ചങ്കുകൾ വിവർത്തനം ചെയ്യേണ്ടത് ഹോസ്റ്റ് ഏജന്റിന്റെ ഉത്തരവാദിത്വമാണ്. Co-op Translator Markdown ചങ്ക് വിഭജനം, പ്ലേസ്‌ഹോൾഡർ സംരക്ഷണം, ഫ്രോണ്ട്മാറ്റർ പുനഃസംരചന, നോട്ട്‌ബുക്ക് സെൽ മാറ്റം, കൂടാതെ വിവർത്തനാനന്തര സാധാരണവത്കരണം എന്നിവ കൈകാര്യം ചെയ്യുന്നു.

### ഒരു മുഴുവൻ റിപ്പോസിറ്ററി വിവർത്തനം ചെയ്യുക

ഉപയോക്താവ് Co-op Translator-നെ CLI പോലെ പ്രവർത്തിപ്പിക്കാൻ ആഗ്രഹിക്കുന്നപ്പോൾ `run_translation` ഉപയോഗിക്കുക.

റിപ്പോസിറ്ററി വിവർത്തനം നിശ്ചിതമായി `dry_run=true` ആകുന്നു, അതോടെ ഏജന്റ് ഫയൽ മാറ്റങ്ങൾക്ക് മുൻപ് പരിമിതിയുടെ പരിശോധന ചെയ്യാൻ കഴിയും:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

എഴുത്തുകൾ അനുവദിക്കണമെങ്കിൽ, കോളർ യുൾക്ക് `dry_run=false`യും `confirm_write=true`യും ഇരുവും സജ്ജമാക്കണം:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` `run_translation`ക്കായ് സമവാക്യമായ ഒരു കമ്പാറ്റിബിലിറ്റി അലയാസായി പുറത്ത് വയ്ക്കപ്പെട്ടിട്ടുണ്ട്.

### വിവർത്തനം ചെയ്ത ഔട്ട്പുട്ട് റിവ്യൂ ചെയ്യുക

LLM അല്ലെങ്കിൽ Vision ക്രെഡൻഷ്യലുകൾ ആവശ്യമില്ലാത്ത നിശ്ചിതപരിശോധനകൾക്കായി `run_review` ഉപയോഗിക്കുക:

!!! note "Beta"
    MCP ബീറ്റാ `run_review` API-യെ പുറത്ത് വയ്ക്കുന്നു. ഇത് റീഡ്-ഓൺലി റിവ്യൂ വർക്ക്‌ഫ്ലോകൾക്കായി സുരക്ഷിതമാണ്, പക്ഷേ റിവ്യൂ ചെക്കുകളും പ്രശ്ന സ്‌കീമകളും മാറ്റങ്ങൾക്കുള്ള സാധ്യത ഉണ്ടാവാം.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ഫലം പിടിച്ചെടുത്ത ടെക്സ്റ്റ് ഔട്ട്പുട്ടും ലഭ്യമായപ്പോൾ ഘടനാപരമായ റിവ്യൂ സംക്ഷേപവും ഉൾക്കൊള്ളുന്നതാണ്.

## മാനുവൽ സർവർ റൺസ്

മാനുവൽ റൺസുകൾ പ്രധാനമായും ഡീബഗ്ഗിംഗിനും അല്ലെങ്കിൽ ദീർഘകാലം പ്രവർത്തിക്കുന്ന സർവറുകളെ പോലെ പ്രവർത്തിക്കുന്ന ട്രാൻസ്പോർട്ടുകൾക്കുമായി ആണ്.

ഡീഫോൾട്ട് stdio 서버 ഡീബഗു ചെയ്യുക:

```bash
co-op-translator-mcp
```

സോഴ്സ് ചെക്ക്ഔട്ടിൽ നിന്നു റൺ ചെയ്യുക:

```bash
python -m co_op_translator.mcp.server
```

ദീർഘകാലം ജീവിക്കുന്ന HTTP അല്ലെങ്കിൽ SSE സർവർ ഓടിക്കുക:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ലൊക്കൽ എഡിറ്റർ/ഏജന്റ് സംയോജനങ്ങൾക്ക്, ഘട്ടം 2-ൽ ക്ലയന്റ്-മാനേജുചെയ്യുന്ന `stdio` കോൺഫിഗറേഷനാണ് മുൻഗണന.

## ഉപകരണങ്ങൾ

| ടൂൾ | ഉദ്ദേശ്യം | ഫയലുകൾ എഴുതുന്നുവോ |
| --- | --- | --- |
| `translate_markdown_content` | ഒരു Markdown സ്ട്രിംഗ് വിവർത്തനം ചെയ്യുക. | ഇല്ല |
| `translate_notebook_content` | നോട്ട്‌ബുക്ക് JSON-ിലുള്ള Markdown സെല്ലുകൾ വിവർത്തനം ചെയ്യുക. | ഇല്ല |
| `translate_image_content` | ഒരു εικόണത്തിൽ ഉള്ള ടെക്സ്റ്റ് വിവർത്തനം ചെയ്ത് base64 ഇമേജ് ഡാറ്റ പ്രത്യാഘാതം നൽകുക. | ഓപ്ഷണൽ, `output_path` നൽകിയപ്പോഴാണ് മാത്രം |
| `start_markdown_agent_translation` | Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്യാൻ Markdown ചങ്കുകൾ തയ്യാറാക്കുക. | ഇല്ല |
| `finish_markdown_agent_translation` | ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്ത ചങ്കുകൾ സഅഞ്ചൽ ചെയ്ത് Markdown പുനഃരൂപീകരിക്കുക. | ഇല്ല |
| `start_notebook_agent_translation` | ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്യാൻ നോട്ട്‌ബുക്ക് Markdown-സെൽ ചങ്കുകൾ തയ്യാറാക്കുക. | ഇല്ല |
| `finish_notebook_agent_translation` | ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്ത ചങ്കുകൾ ഉപയോഗിച്ച് നോട്ട്‌ബുക്ക് JSON പുനഃസംരചിക്കുക. | ഇല്ല |
| `rewrite_markdown_paths` | വിവർത്തനം ചെയ്ത ലക്ഷ്യത്തിനായി Markdown ബോഡിും ഫ്രോണ്ട്മാറ്ററും ഉള്ള പാതകൾ പുനഃലേഖനം ചെയ്യുക. | ഇല്ല |
| `rewrite_notebook_paths` | നോട്ട്‌ബുക്ക് Markdown സെല്ലുകൾക്കുള്ളിൽ പാതകൾ പുനഃലേഖനം ചെയ്യുക. | ഇല്ല |
| `run_translation` | CLI പോലെ പ്രോജക്റ്റ്-തല വിവർത്തനം നടത്തുക. | അതെ, `dry_run=false`യും `confirm_write=true`ഉം ആയാൽ ഫയലുകൾ എഴുതുന്നു |
| `translate_project` | `run_translation` നുള്ള കമ്പാറ്റിബിലിറ്റി അലയാസ്. | അതെ, `dry_run=false`യും `confirm_write=true`ഉം ആയാൽ ഫയലുകൾ എഴുതുന്നു |
| `run_review` | നിശ്ചിതപരിശോധനകൾ റൺ ചെയ്യുക. | ഇല്ല |
| `get_configuration_status` | രഹസ്യങ്ങൾ പുറത്തെടുക്കാതെ കോൺഫിഗർ ചെയ്ത LLM & Vision പ്രൊവൈഡറുകൾ റിപ്പോർട്ട് ചെയ്യുക. | ഇല്ല |
| `list_supported_languages` | പിന്തുണയ്‌ക്കുന്ന ലക്ഷ്യ ഭാഷാ കോഡുകളുടെ പട്ടിക നൽകുക. | ഇല്ല |
| `get_api_overview` | ലഭ്യമായ MCP വർക്ക്‌ഫ്ലോകളും ടൂളുകളും വിവരണപ്പെടുത്തുക. | ഇല്ല |

## റിസോഴ്‌സുകൾ

| റിസോഴ്‌സ് URI | ഉദ്ദേശ്യം |
| --- | --- |
| `co-op://api` | വർക്ക്‌ഫ്ലോകളുടെയും ടൂളുകളുടെയും JSON അവലോകനം. |
| `co-op://supported-languages` | പിന്തുണയ്‌ക്കുന്ന ഭാഷാ കോഡുകളുടെ JSON പട്ടിക. |
| `co-op://configuration` | രഹസ്യങ്ങൾ പുറത്തെടുക്കാതെയുള്ള പ്രൊവൈഡർ ലഭ്യതാ സംഗ്രഹം JSON ആയി. |

## പ്രോംപ്റ്റുകൾ

| പ്രോംപ്റ്റ് | ഉദ്ദേശ്യം |
| --- | --- |
| `translate_markdown_document_prompt` | ഉള്ളടക്ക വിവർത്തനത്തിനും ആവശ്യമായെങ്കിൽ പാത പുനഃലേഖനത്തിനും MCP ക്ലയന്റ് ഗൈഡുചെയ്യുക. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ ഹോസ്റ്റ്-ഏജന്റ് Markdown വിവർത്തനത്തിന് MCP ക്ലയന്റ് ഗൈഡ് ചെയ്യുക. |
| `translate_repository_prompt` | ആദ്യം dry-run ആക്കിവച്ച് റിപ്പോസിറ്ററി വിവർത്തനത്തിനുള്ള MCP ക്ലയന്റ് ഗൈഡ് ചെയ്യുക. |

## കോപ്പി-പേസ്റ്റ് ഉദാഹരണങ്ങൾ

Markdown ഉള്ളടക്കം വിവർത്തനം ചെയ്യുക:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

വിവർത്തനം ചെയ്ത Markdown ലിങ്കുകൾ പുനഃലേഖനം ചെയ്യുക:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

ഹോസ്റ്റ് ഏജന്റ് മോഡൽ ഉപയോഗിച്ച് Markdown വിവർത്തനം ചെയ്യുക:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

ഹോസ്റ്റ് ഏജന്റ് മടങ്ങിയുമെത്തിച്ച ഓരോ ചങ്കും വിവർത്തനം ചെയ്തശേഷം, `start_markdown_agent_translation` കോൾ ചെയ്തത് റിട്ടേൺ ചെയ്ത പൂര്‍ണ്ണ `job` ഒബ്ജക്‌ടിനൊപ്പം ജോബ് പൂർത്തിയാക്കുക:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

റിപ്പോസിറ്ററി വിവർത്തനത്തിന്റെ പ്രിവ്യൂ കാണുക:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## പ്രശ്നപരിഹാരം

| പ്രശ്നം | എന്ത് ശ്രമിക്കണം |
| --- | --- |
| MCP ക്ലയന്റ് `co-op-translator-mcp` കണ്ടെത്തുന്നില്ല. | അണിയാത്ത പ്ലിൻത്ത് absolute Python executable പാതയും `["-m", "co_op_translator.mcp.server"]` സോഴ്സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ ഉപയോഗിക്കുക. |
| സർവർ ലിസ്റ്റ് ചെയ്യപ്പെട്ടിട്ടുണ്ട്, പക്ഷേ വിവർത്തനം പരാജയപ്പെടുന്നു. | `get_configuration_status` കോൾ ചെയ്ത് ഒരു LLM പ്രൊവൈഡർ ലഭ്യമാണ് എന്ന് സ്ഥിരീകരിക്കുക. |
| Azure OpenAI/OpenAI കീകൾ ഇല്ലാതെ Markdown അല്ലെങ്കിൽ നോട്‌ബുക്ക് വിവർത്തനം വേണമെന്ന് ആവശ്യമാണ്. | ഹോസ്റ്റ് ഏജന്റ് ചങ്കുകൾ വിവർത്തനം ചെയ്യാൻ `start_markdown_agent_translation` / `finish_markdown_agent_translation` അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് സമാനങ്ങൾ ഉപയോഗിക്കുക. |
| ചിത്രം വിവർത്തനം പരാജയപ്പെടുന്നു. | Azure AI Vision വ്യത്യാസങ്ങൾ സജ്ജമാക്കിയിട്ടുണ്ടോ എന്ന് സ്ഥിരീകരിച്ച് `get_configuration_status` കോൾ ചെയ്യുക. |
| റിപ്പോസിറ്ററി വിവർത്തനം ഫയലുകൾ എഴുതി ഭാഗ്യമില്ല. | ക്ലയന്റ് വ്യക്തമായി അംഗീകാരം നൽകിയതിന് ശേഷമേ `dry_run=false`യും `confirm_write=true`യും സജ്ജമാക്കുകയുള്ളൂ. |
| ക്ലയന്റ് കോൺഫിഗിൽ മാറ്റങ്ങൾ പ്രത്യക്ഷപ്പെടുന്നില്ല. | MCP ക്ലയന്റ് റസ്റ്റാർട്ട് അല്ലെങ്കിൽ റീലോഡ് ചെയ്യുക. |

## സുരക്ഷാ കുറിപ്പുകൾ

- MCP ടൂൾ കോൾകൾ ഹോസ്റ്റ് ആപ്ലിക്കേഷന്റെ മോഡൽ നിയന്ത്രണത്തിലുള്ളവയാണ്, അതിനാൽ റിപ്പോസിറ്ററി വിവർത്തനം എന്ന നിലയിൽ ഡീഫോൾട്ട് ആയി dry-run ആണ്.
- മുഴുവൻ റിപ്പോസിറ്ററി വിവർത്തനം നിരവധി ഫയലുകൾ സൃഷ്ടിക്കാനും അപ്ഡേറ്റ് ചെയ്യാനും നീക്കം ചെയ്യാനുമിടയായേക്കാം. `confirm_write=true` സജ്ജമാക്കുന്നതിന് മുമ്പ് വ്യക്തമായ ഉപയോക്തൃ അംഗീകാരം ആവശ്യപ്പെടുക.
- കോൺഫിഗറേഷൻ സ്റ്റാറ്റസ് ടൂൾ എപ്പോഴും API കീകൾ, എൻഡ്പോയിന്റുകൾ അല്ലെങ്കിൽ മറ്റ് രഹസ്യ മൂല്യങ്ങൾ_RETURNS_ ചെയ്യില്ല.
- ചിത്രം വിവർത്തനം base64 ഇമേജ് ഡാറ്റ മടกลับ നൽകും. വലുതായ ഇമേജുകൾ വലിയ ടൂൾ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കാവുന്നു.
- ഏജന്റ്-സഹായിത ടൂളുകൾ സോഴ്സ് ചങ്കുകളും പ്രോംപ്റ്റുകളും MCP ഹോസ്റ്റിന് റിട്ടേൺ ചെയ്യുന്നു. ഉപയോക്താവ് ആ ഹോസ്റ്റ് ഏജന്റ് മോഡലിനോട് അയയ്ക്കാൻ സുഖമുള്ള ഉള്ളടക്കത്തിൽ മാത്രമേ ഇവ ഉപയോഗിക്കാവൂ.