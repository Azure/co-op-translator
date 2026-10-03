# MCP സെർവർ

Co-op Translator-ൽ ഏജന്റുകൾക്കും എഡിറ്റർമാർക്കും MCP-അനുസരിച്ചുള്ള ക്ലയന്റുകൾക്കും വേണ്ടി ഒരു Model Context Protocol സർവർ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്.

ഡിഫോൾട്ട് ലോക്കൽ സെറ്റപ്പിനായി, ഉപയോക്താക്കൾ പ്രത്യേക സെർവർ കൈക്കൈയിൽ chạy ചെയ്യാറില്ല. അവർ അവരുടെ MCP ക്ലയന്റ് ക്രമീകരിക്കും, ക്ലയന്റ് Co-op Translator ഉപകരണങ്ങൾ ആവശ്യമുള്ളപ്പോൾ `stdio` വഴി സ്വയം `co-op-translator-mcp` ആരംഭിക്കും.

CLI, Python API, MCP എന്നിവയിൽ തിരഞ്ഞെടുക്കുന്നതിനായി, ആദ്യം [Choose Your Workflow](workflows.md) കാണുക.

ഏജന്റ് അല്ലെങ്കിൽ എഡിറ്റർ Co-op Translator-നെ നേരിട്ട് വിളിക്കേണ്ട സാഹചര്യത്തിൽ MCP ഉപയോഗിക്കുക:

| ഉപയോക്തൃ ലക്ഷ്യം | MCP ഉപകരണങ്ങൾ |
| --- | --- |
| ഒരു Markdown ഡോക്യുമെന്റ്, നോട്ട്‌ബുക്ക്, അല്ലെങ്കിൽ ചിത്രം വിവർത്തനം ചെയ്യുക | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ഹോസ്റ്റ് ഏജന്റ് മോഡലിനോട് ചേർന്ന് Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ഉള്ളടക്കം വിവർത്തനം ചെയ്യുക | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ഔട്ട്‌പുട്ട് പാത തിരഞ്ഞെടുക്കുന്നതിന് ശേഷം വിവർത്തനം ചെയ്ത Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ലിങ്കുകൾ വീണ്ടും എഴുതുക | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI പോലെ മുഴുവൻ റീപോസിറ്ററിയെ വിവർത്തനം ചെയ്യുക | `run_translation`, `translate_project` |
| LLM ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ വിവർത്തനം ചെയ്ത ഔട്ട്‌പുട്ട് റിവ്യൂ ചെയ്യുക | `run_review` |
| ശേഷികൾക്കും പരിസ്ഥിതി നിലക്കും പരിശോധിക്കുക | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP സർവർ [Python API](api.md) ൽ രേഖപ്പെടുത്തിയതേ പൊതു Python API തത്ത്വങ്ങൾ ഉപയോഗിക്കുന്നു. Provider-backed ടൂളുകൾ CLI-യും Python API-യും ക്രമീകരിച്ചിട്ടുള്ളതേ പ്രൊവൈഡർമാരെ ഉപയോഗിക്കുന്നു. Agent-assisted ടൂളുകൾ MCP ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്യാൻ chunks തയ്യാറാക്കി, പിന്നെ Co-op Translator ഉപയോഗിച്ച് അവസാന Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് പുനഃനിർമിക്കുന്നു.

## ഘട്ടം 1: Co-op Translator ഇൻസ്റ്റാൾ ചെയ്ത് ക്രമീകരിക്കുക

നിങ്ങളുടെ MCP ക്ലയന്റ് ഉപയോഗിക്കുന്ന Python പരിസ്ഥിതിയിൽ Co-op Translator ഇൻസ്റ്റാൾ ചെയ്യുക:

```bash
pip install co-op-translator
```

ഈ റീപോസിറ്ററിയിൽ നിന്നുള്ള ലോക്കൽ ഡെവലപ്പ്മെന്റിനായി, പാക്കേജ് എഡിറ്റബിൾ മോഡിൽ ഇൻസ്റ്റാൾ ചെയ്യുക:

```bash
pip install -e .
```

നിങ്ങളുടെ MCP ക്ലയന്റ് ഉപയോഗിക്കുന്ന വിവർത്തന മോഡ് തിരഞ്ഞെടുക്കുക:

| മോഡ് | ഇതിന് ഉപയോഗിക്കുക | ക്രെഡൻഷ്യലുകൾ |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, അല്ലെങ്കിൽ `run_translation` കോളുകൾ നടത്തുന്നു. | വിവർത്തനത്തിന് Azure OpenAI, OpenAI, അല്ലെങ്കിൽ Anthropic ആവശ്യമാണ്. ഇമേജ് വിവർത്തനത്തിന് Azure AI Vision കൂടി ആവശ്യമാണ്. |
| Agent-assisted | MCP ഹോസ്റ്റ് ഏജന്റ് `start_markdown_agent_translation` അല്ലെങ്കിൽ `start_notebook_agent_translation` വഴി ലഭിക്കുന്ന chunks വിവർത്തനം ചെയ്യുന്നു. | Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് chunks-നായി Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ആവശ്യമില്ല. ഇമേജ് വിവർത്തനം ഇതുവരെ agent-assisted മോഡിൽ ഉൾപ്പെടുന്നില്ല. |

Codex അല്ലെങ്കിൽ Claude Code പോലുള്ള ഏജന്റിനുള്ളിൽ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് വിവർത്തനത്തോടെ തുടങ്ങുകയാണെങ്കിൽ agent-assisted മോഡ് ഉപയോഗിച്ച് തുടങ്ങുക. Co-op Translator നുള്ള പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യണമെന്ന് ആവശ്യമുള്ളപ്പോൾ, ചിത്രങ്ങൾ വിവർത്തനം ചെയ്യുമ്പോൾ, അല്ലെങ്കിൽ CLI പോലെയുള്ള റീപ്പോ-ലെവൽ വിവർത്തനം നടത്തുമ്പോൾ provider-backed മോഡ് ഉപയോഗിക്കുക.

Provider-backed ജോലി-പ്രവാഹങ്ങൾക്ക് ഒരെണ്ണം പ്രൊവൈഡർ ക്രമീകരിക്കുക:

```bash
# അസ്യൂർ ഓപ്പൺഎഐ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# അതവാ ഓപ്പൺഎഐ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# അതവാ ആൻത്രോപ്പിക്
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed ഇമേജ് വിവർത്തനത്തിന് കൂടാതെ ആവശ്യമായത്:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted മോഡ് നിലവിൽ Markdown და നോട്ട്‌ബുക്ക് Markdown സെൽുകൾ മാത്രമേ ഉൾക്കൊള്ളൂ. ഇമേജ് വിവർത്തനം ഇപ്പോഴും provider-backed ഇമേജ് പൈപ്ലൈനത്തിനാണ്, OCRക്കും ലേയൗട്ട്-അവേരായ റെൻഡറിംഗിനും Azure AI Vision ആവശ്യമാണ്.

## ഘട്ടം 2: നിങ്ങളുടെ MCP ക്ലയന്റ് ക്രമീകരിക്കുക

സാധാരണ ലോക്കൽ `stdio` സെറ്റപ്പിനായി, Co-op Translator-നെ നിങ്ങളുടെ MCP ക്ലയന്റ് കോൺഫിഗറേഷനിൽ ചേർക്കുക. ക്ലയന്റ് പ്രക്രിയ സ്വയം ആരംഭിക്കുകയും നിര്‍ത്തുകയും ചെയ്യും.

ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജിന്റെ കോൺഫിഗറേഷൻ:

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

Windows-ൽ സോഴ്‌സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ:

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

macOS അല്ലെങ്കിൽ Linux-ൽ സോഴ്‌സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ:

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

MCP ക്ലയന്റ് കോൺഫിഗറേഷൻ മാറ്റിയ 뒤, പുതിയ സർവർ കണ്ടെത്താൻ ക്ലയന്റ് റസ്റ്റാർട്ട് അല്ലെങ്കിൽ റീലോഡ് ചെയ്യുക.

## ഘട്ടം 3: ക്ലയന്റിൽ സർവർ സ്ഥിരീകരിക്കുക

ലഭ്യമായ ടൂളുകളുടെ പട്ടിക കാണിക്കാൻ MCP ക്ലയന്റോട് അഭ്യർത്ഥിക്കൂ, അല്ലെങ്കിൽ ആദ്യം ഒരു റീഡ്-ഓൺലി ഹെൽപ്പർ വിളിച്ച് പരിശോധിക്കുക:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ആദ്യമായി പരിശോധിക്കാൻ ഉപകാരപ്രദമായ കാര്യങ്ങൾ:

| ടൂൾ | എന്ത് പരിശോധിക്കണം |
| --- | --- |
| `get_api_overview` | സർവർ ലഭ്യമാണെന്ന് സ്ഥിരീകരിക്കുകയും ലഭ്യമായ വർക്ക്‌ഫ്ലോകൾ കാണിക്കുകയും ചെയ്യുക. |
| `list_supported_languages` | പാക്കേജിലുള്ള ഭാഷാ ഡാറ്റ ലോഡ് ചെയ്യാൻ കഴിയുന്നുവെന്ന് സ്ഥിരീകരിക്കുക. |
| `get_configuration_status` | രഹസ്യ മൂല്യങ്ങൾ പുറത്തുവിടാതെ LLM மற்றும் Vision പ്രൊവൈഡറുകളുടെ ലഭ്യത സ്ഥിരീകരിക്കുക. |

## ഘട്ടം 4: ഒരു Workflow തിരഞ്ഞെടുക്കുക

### വ്യക്തിഗത ഫയലുകൾ അല്ലെങ്കിൽ ഡോക്യുമെന്റുകൾ വിവർത്തനം ചെയ്യുക

MCP ക്ലയന്റിന് ഡോക്യുമെന്റ് ഉള്ളടക്കം അല്ലെങ്കിൽ ഇമേജ് പാതയേ ഇതിനകം ഉണ്ടെങ്കിൽ, Co-op Translator-ന് ക്രമീകരിച്ച പ്രൊവൈഡറുമാർ വിളിക്കണമെന്നും ആഗ്രഹിക്കുമ്പോൾ provider-backed content tools ഉപയോഗിക്കുക.

Markdown-ക്കായി:

1. `document`, `language_code`, ഐച്ഛികമായി `source_path` എന്നിവ നൽകി `translate_markdown_content` കോൾ ചെയ്യുക.
2. വിവർത്തന ഫലവും Co-op Translator ഔട്ട്‌പുട്ട് ലേയൗട്ടിലേക്ക് എഴുതുകയാണെങ്കിൽ `rewrite_markdown_paths` കോൾ ചെയ്യുക.
3. ക്ലയന്റ് അന്തിമ `content` എഴുതുകയോ തിരിച്ചുകൊടുക്കുകയോ ചെയ്യട്ടെ.

നോട്ട്‌ബുക്കുകൾക്കായി:

1. നോട്ട്‌ബുക്ക് JSON-യും `language_code`-ഉം നൽകി `translate_notebook_content` കോൾ ചെയ്യുക.
2. വിവർത്തനം ചെയ്ത നോട്ട്‌ബുക്ക് ലിങ്കുകൾ ദിശാന്വേഷിക്കുന്നതിനു ടാർഗറ്റ് പാതയ്ക്ക് അനുസൃതമാക്കേണ്ടതുണ്ടെങ്കിൽ `rewrite_notebook_paths` കോൾ ചെയ്യുക.
3. അന്തിമ നോട്ട്‌ബുക്ക് JSON എഴുതുകയോ തിരികെയാക്കുകയോ ചെയ്യുക.

ചിത്രങ്ങൾക്കായി:

1. `image_path`, `language_code`, ഐച്ഛികമായി `root_dir` അല്ലെങ്കിൽ `fast_mode` നൽകി `translate_image_content` കോൾ ചെയ്യുക.
2. മടങ്ങിച്ചെത്തുന്ന `data_base64`യും `mime_type`യും വായിക്കുക.
3. `output_path` നൽകിയിട്ടുണ്ടെങ്കിൽ വിവർത്തനചെയ്ത ചിത്രം ആ പാതയിലും സേവ് ചെയ്യപ്പെടും.

ഈ content ടൂളുകൾ പ്രോജക്‌ട് ഡിസ്ഫവറി, മെറ്റാഡേറ്റ അപ്ഡേറ്റുകൾ, ഡിസ്‌ക്ലെയിമറുകൾ, അല്ലെങ്കിൽ സ്വയം പാത പുനഃരചയനം നടത്താറില്ല. ഹോസ്റ്റ് ഏജന്റ് Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് chunks വിവർത്തനം ചെയ്യാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നെങ്കിൽ താഴെ കൊടുത്തിരിക്കുന്ന agent-assisted workflow ഉപയോഗിക്കുക.

### ഹോസ്റ്റ് ഏജന്റ് മോഡലുമായി വിവർത്തനം ചെയ്യുക

MCP ഹോസ്റ്റ് ഏജന്റ് (ഏറ്റവും സാധാരണ കോഡിംഗ് അസിസ്റ്റന്റ് പോലുള്ള) ആണ് വിവർത്തനം ചെയ്ത ടെക്സ്റ്റ് നിർമ്മിക്കുന്നത് എന്ന് നിങ്ങൾ ആഗ്രഹിക്കുന്നപ്പോൾ, Co-op Translator ന് വേണ്ടി LLM പ്രൊവൈഡർ ക്രമീകരിക്കാതെ agent-assisted ടൂളുകൾ ഉപയോഗിക്കുക.

ചാറ്റ്-ഓറിയന്റഡ് MCP ക്ലയന്റിൽ സാധാരണയായി ടൂൾ JSON നിങ്ങൾ തന്നെ എഴുതേണ്ടതില്ല. ഏജന്റിനോട് agent-assisted workflow ഉപയോഗിക്കാൻ പറയുക:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

നോട്ട്‌ബുക്കുകൾക്കായി, അതേ രീതിയാണ് ഉപയോഗിക്കുക:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

നിങ്ങളുടെ MCP ക്ലയന്റ് സെർവർ പ്രോംപ്റ്റുകൾ പിന്തുണയ്ക്കുകയാണെങ്കിൽ, ക്ലയന്റ് തത്തോടെ അതേ വർക്ക്‌ഫ്ലോ നിർദേശങ്ങൾ ലോഡ് ചെയ്യാൻ `agent_assisted_markdown_translation_prompt` ഉപയോഗിക്കുക.

Markdown-ക്കായി:

1. `document`, `language_code`, ഐച്ഛികമായി `source_path` നൽകി `start_markdown_agent_translation` കോൾ ചെയ്യുക.
2. മടങ്ങിയെത്തിയ ഓരോ chunk-ഉം chunk-യുടെ `prompt` പിന്തുടർന്ന് ഹോസ്റ്റ് ഏജന്റിൽ വിവർത്തനം ചെയ്യുക.
3. ഒറിജിനൽ `job`-ഉം `chunk_id`യും `translated_text`യും ഉപയോഗിച്ചുകൊണ്ട് വിവർത്തനം ചെയ്ത chunks സഹിതം `finish_markdown_agent_translation` കോൾ ചെയ്യുക.
4. ഉള്ളടക്കം വിവർത്തിച്ച ലക്ഷ്യ പാത്തിൽ എഴുതുന്നതിനായാൽ ആയാൽ `rewrite_markdown_paths` കോൾ ചെയ്യുക.

നോട്ട്‌ബുക്കുകൾക്കായി:

1. നോട്ട്‌ബുക്ക് JSON-നും `language_code`-ഉം നൽകി `start_notebook_agent_translation` കോൾ ചെയ്യുക.
2. മടങ്ങിയെത്തിയ ഓരോ chunk-ഉം ഹോസ്റ്റ് ഏജന്റിൽ വിവർത്തനം ചെയ്യുക.
3. ഒറിജിനൽ `job`-ഉം വിവർത്തന ചങ്കുകളും ഉപയോഗിച്ച് `finish_notebook_agent_translation` കോൾ ചെയ്യുക.
4. വിവർത്തിച്ച നോട്ട്‌ബുക്ക് ലിങ്കുകൾക്ക് ടാർഗറ്റ്-പാത്ത് ക്രമമാക്കേണ്ടതുണ്ടെങ്കിൽ `rewrite_notebook_paths` കോൾ ചെയ്യുക.

Agent-assisted ടൂളുകൾ Co-op Translator-ലേക്കുനിന്ന് ക്രമീകരിച്ച LLM പ്രൊവൈഡറിനെ വിളിക്കുന്നില്ല. മടങ്ങിയെത്തിയ chunks വിവർത്തനം ചെയ്യുന്നത് ഹോസ്റ്റ് ഏജന്റിന്റെ ഉത്തരവാദിത്വത്തിലാണ്. Co-op Translator Markdown ചങ്കിംഗ്, പ്ലേസ്ഹോൾഡർ സംരക്ഷണം, frontmatter പുനർനിർമാണം, നോട്ട്‌ബുക്ക് സെൽ മാറ്റം, പോസ്റ്റ്-ട്രാൻസ്ലേഷൻ നോർമലൈസ് ചെയ്യൽ എന്നിവ കൈകാര്യം ചെയ്യുന്നു.

### ഒരു മുഴുവൻ റീപോസിറ്ററി വിവർത്തനം ചെയ്യുക

ഉപയോക്താവ് Co-op Translator-ൻറെ CLI പോലെയൊരുക്കാൻ ആഗ്രഹിക്കുന്ന പക്ഷം `run_translation` ഉപയോഗിക്കുക.

റീപോസിറ്ററി വിവർത്തനം ഡിഫൗൾട്ടായി `dry_run=true` ആക്കിയാണ് നടത്തുന്നത്, ώστε ഏജന്റ് ഫയൽ മാറ്റങ്ങൾക്കുമുമ്പ് പരിധി പരിശോധിക്കാൻ കഴിയും:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` ഫലത്തിൽ പതിപ്പുചെയ്ത `events` അരേ ഉൾക്കൊള്ളിക്കുന്നു.
`co-op.translation.event.v1` പ്രോഗ്രസ് ഇവന്റുകൾ അടങ്ങിയിരിക്കും. MCP ക്ലയന്റുകൾ കോൻസോൾ ടെക്സ്റ്റ് പാഴ്സ് ചെയ്യുന്നതിന്റെ പകരം താഴെപ്പറയുന്ന ഫീൽഡുകൾ ഉപയോഗിക്കണം
ഉദാഹരണത്തിന് `type`, `stage_key`, `completed`, `total`, `current_path` എന്നിവ.
ക്യാപ്ചർ ചെയ്ത കൺസോൾ ടെക്സ്റ്റ് പാഴ്സിങ് ചെയ്യാൻ പകരം ഇവയിലെ ഫീൽഡുകൾ ഉപയോഗിക്കുക. ആ ഇവന്റുകൾ NDJSON ഫയലിലേക്ക് എഴുതണമെങ്കിൽ `json_events_path` പാസ്സ് ചെയ്യുക.
NDJSON ഫയലിലേക്ക്.

എഴുതലുകള് അനുവദിക്കുവാൻ caller-ന് `dry_run=false`യും `confirm_write=true`യും രണ്ടും സജ്ജമാക്കണം:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project`-നെ `run_translation`-നുള്ള അനുയോജ്യമായ ആലിയസായി നൽകുന്നു.

### വിവർത്തനം ചെയ്ത ഔട്ട്‌പുട്ട് റിവ്യൂ ചെയ്യുക

LLM അല്ലെങ്കിൽ Vision ക്രെഡൻഷ്യലുകൾ ആവശ്യമില്ലാത്ത നിർണ്ണായക പരിശോധനകൾക്കായി `run_review` ഉപയോഗിക്കുക:

!!! note "Beta"
    MCP ബിേറ്റ പതിപ്പിന്റെ `run_review` API തുറന്ന് തരുന്നു. ഇത് റീഡ്-ഓൺലി റിവ്യൂ വർക്ക്‌ഫ്ലോകുകൾക്കായി സുരക്ഷിതമാണ്, പക്ഷേ റിവ്യൂ പരിശോധനകളും ഇഷ്യൂ സ്‌കീമുകളും വളരാൻസാധ്യത ഉണ്ട്.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ഫലത്തിൽ ക്യാപ്ചർ ചെയ്ത ടെക്സ്റ്റ് ഔട്ട്‌പുട്ടും ലഭ്യമായപ്പോൾ ഘടനാപരമായ റിവ്യൂ സംഗ്രഹവും ഉൾക്കൊള്ളും.

## മാനുവൽ സെർവർ റൺസ്

മാനുവൽ റൺസ് പ്രധാനമായും ഡീബഗിംഗിനോ ദീർഘകാലം ജോലിയിലിരിക്കുന്ന സെർവർ പോലെയുള്ള ട്രാൻസ്പോർട്ടുകൾക്കായോ ആണ്.

ഡീബഗിന് ഡിഫോൾട്ട് `stdio` സർവർ:

```bash
co-op-translator-mcp
```

സോഴ്‌സ് ചെക്ക്ഔട്ട്-ൽ നിന്നു പ്രവർത്തിപ്പിക്കുക:

```bash
python -m co_op_translator.mcp.server
```

ദീർഘകാലപരമായി നിലനിൽക്കുന്ന HTTP അല്ലെങ്കിൽ SSE സർവർ റൺ ചെയ്യുക:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ലോക്കൽ എഡിറ്റർ மற்றும் ഏജന്റ് ഇന്റഗ്രേഷനുകൾക്കായി, ഘട്ടം 2-ലുള്ള ക്ലയന്റ്-മാനേജ്ഡ് `stdio` കോൺഫിഗറേഷൻ പ്രഥമ പരിഗണന ആക്കുക.

## ടൂളുകൾ

| ടൂൾ | ഉപയോഗം | ഫയലുകൾ എഴുതുന്നു |
| --- | --- | --- |
| `translate_markdown_content` | ഒരു Markdown സ്ട്രിംഗ് വിവർത്തനം ചെയ്യുക. | ഇല്ല |
| `translate_notebook_content` | നോട്ട്‌ബുക്ക് JSON-ിലെ Markdown സെലുകൾ വിവർത്തനം ചെയ്യുക. | ഇല്ല |
| `translate_image_content` | ഒരു ചിത്രത്തിലെ ടെക്സ്റ്റ് വിവർത്തനം ചെയ്ത് base64 ഇമേജ് ഡാറ്റ തിരികെ നൽകുക. | ഐച്ഛികം, `output_path` നൽകിയപ്പോൾ മാത്രം |
| `start_markdown_agent_translation` | Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്യാൻ Markdown chunks തയ്യാറാക്കുക. | ഇല്ല |
| `finish_markdown_agent_translation` | ഹോസ്റ്റ്-എജന്റ് വിവർത്തന ചങ്കുകളിൽ നിന്ന് Markdown പുനഃനിർമിക്കുക. | ഇല്ല |
| `start_notebook_agent_translation` | ഹോസ്റ്റ് ഏജന്റ് വിവർത്തനം ചെയ്യാൻ നോട്ട്‌ബുക്ക് Markdown-സെൽ ചങ്കുകൾ തയ്യാറാക്കുക. | ഇല്ല |
| `finish_notebook_agent_translation` | ഹോസ്റ്റ്-എജന്റ് വിവർത്തന ചങ്കുകൾ ഉപയോഗിച്ച് നോട്ട്‌ബുക്ക് JSON പുനഃനിർമിക്കുക. | ഇല്ല |
| `rewrite_markdown_paths` | വിവർത്തിച്ച ലക്ഷ്യത്തിനായുള്ള Markdown ബോഡി һәм frontmatter പാത്തുകൾ പുനഃരചയിക്കുക. | ഇല്ല |
| `rewrite_notebook_paths` | നോട്ട്‌ബുക്ക് Markdown സെലുകൾക്കുള്ളതിലുള്ള പാത്തുകൾ പുനഃരചയിക്കുക. | ഇല്ല |
| `run_translation` | CLI പോലെയുള്ള പ്രോജക്‌ട്-ലെവൽ വിവർത്തനം നടത്തുക. | ഉണ്ടോ, `dry_run=false`യും `confirm_write=true`യും ആയപ്പോൾ |
| `translate_project` | `run_translation`-നുള്ള കംപാറ്റിബിലിറ്റി ആലിയസ്. | ഉണ്ടോ, `dry_run=false`യും `confirm_write=true`യും ആയപ്പോൾ |
| `run_review` | നിർണ്ണായക റിവ്യൂ പരിശോധനകൾ നടത്തുക. | ഇല്ല |
| `get_configuration_status` | രഹസ്യങ്ങൾ പുറത്താക്കാതെ ക്രമീകരിച്ച LLM మరియు Vision പ്രൊവൈഡറുകൾ റിപ്പോർട്ട് ചെയ്യുക. | ഇല്ല |
| `list_supported_languages` | പിന്തുണയുള്ള ലക്ഷ്യ ഭാഷാ കോഡുകൾ ലിസ്റ്റ് ചെയ്യുക. | ഇല്ല |
| `get_api_overview` | ലഭ്യമായ MCP വർക്ക്‌ഫ്ലോകളും ടൂളുകളും വിവരണം നൽകുക. | ഇല്ല |

## റിസോഴ്‌സുകൾ

| റിസോഴ്‌സ് URI | ഉപയോഗം |
| --- | --- |
| `co-op://api` | വർക്ക്‌ഫ്ലോകളുടെയും ടൂളുകളുടെയും JSON അവലോകനം. |
| `co-op://supported-languages` | പിന്തുണയുള്ള ഭാഷാ കോഡുകളുടെ JSON ലിസ്റ്റ്. |
| `co-op://configuration` | രഹസ്യങ്ങൾ ഇല്ലാതെ പ്രൊവൈഡർ ലഭ്യതയുടെ JSON സംഗ്രഹം. |

## പ്രോംപ്റ്റുകൾ

| പ്രോംപ്റ്റ് | ഉപയോഗം |
| --- | --- |
| `translate_markdown_document_prompt` | content വിവർത്തനവും ഐച്ഛികമായി പാത പുനഃരചയനവുമുള്ള MCP ക്ലയന്റിനെ മാർഗ്‌ദർശിപ്പിക്കുക. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ ഹോസ്റ്റ്-ഏജന്റ് Markdown വിവർത്തനത്തിനു MCP ക്ലയന്റിനെ മാർഗ്‌ദർശിപ്പിക്കുക. |
| `translate_repository_prompt` | ആദ്യം dry-run നടത്തുന്ന റീപോസിറ്ററി വിവർത്തനത്തിലേക്കുള്ള MCP ക്ലയന്റിനെ മാർഗ്‌ദർശിപ്പിക്കുക. |

## കോപി-പേസ്റ്റ് ഉദാഹരണങ്ങൾ

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

വിവർത്തിച്ചത് Markdown ലിങ്കുകൾ പുനഃരചയിക്കുക:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

ഹോസ്റ്റ് ഏജന്റ് മടങ്ങിയെത്തിച്ച ഓരോ chunk-ഉം വിവർത്തനം ചെയ്തത് കഴിഞ്ഞ്, `start_markdown_agent_translation` മടങ്ങിച്ചുതരുന്ന മുഴുവൻ `job` ഒബ്ജക്റ്റുമായി ജോബ് ഉപസംഹരിക്കൂ:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

റീപോസിറ്ററി വിവർത്തനം മുൻ‌കൂട്ടി കാണുക:

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

| പ്രശ്നം | പരീക്ഷിക്കേണ്ടത് |
| --- | --- |
| MCP ക്ലയന്റ് `co-op-translator-mcp` കണ്ടെത്താൻ കഴിയുന്നില്ല. | ആബ്സല്യൂട്ട് Python എക്സിക്യൂട്ടബിൾ പാത്ത് ഉപയോഗിക്കുക, మరియు `["-m", "co_op_translator.mcp.server"]` സോഴ്‌സ് ചെക്ക്ഔട്ട് കോൺഫിഗറേഷൻ ഉപയോഗിക്കുക. |
| സെർവർ ലിസ്റ്റിൽ കാണിച്ചാലും വിവർത്തനം പരാജയപ്പെടുന്നു. | `get_configuration_status` കോൾ ചെയ്ത് ഒരു LLM പ്രൊവൈഡർ ലഭ്യമാണെന്ന് സ്ഥിരീകരിക്കുക. |
| പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് വിവർത്തനം വേണം. | ഹോസ്റ്റ് ഏജന്റ് chunks വിവർത്തനം ചെയ്യാൻ `start_markdown_agent_translation` / `finish_markdown_agent_translation` ഉപയോഗിക്കുക അതോ നോട്ട്‌ബുക്ക് സഹപ്രവർത്തി ടൂളുകൾ ഉപയോഗിക്കുക. |
| ഇമേജ് വിവർത്തനം പരാജയപ്പെടുന്നു. | Azure AI Vision ചാരങ്ങൾ ക്രമീകരിച്ചിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക ಮತ್ತು `get_configuration_status` കോൾ ചെയ്യുക. |
| റീപോസിറ്ററി വിവർത്തനം ഫയലുകൾ എഴുതുന്നില്ല. | ഉപയോക്താവിന്റെ വ്യക്തമായ അംഗീകാരം ലഭിക്കാത്തവരെ `dry_run=false`യും `confirm_write=true`യും സജ്ജമാക്കരുത്. |
| ക്ലയന്റ് കോൺഫിഗിൽ മാറ്റങ്ങൾ പ്രത്യക്ഷപ്പെടുന്നില്ല. | MCP ക്ലയന്റ് റസ്റ്റാർട്ട് അല്ലെങ്കിൽ റീലോഡ് ചെയ്യുക. |

## സുരക്ഷാ കുറിപ്പുകൾ

- MCP ടൂൾ കോളുകൾ ഹോസ്റ്റ് അപ്ലിക്കേഷനാൽ മോഡൽ-നിയന്ത്രിതമാണ്, അതിനാൽ റീപോസിറ്ററി വിവർത്തനം ഡിഫോൾട്ടായി dry-run ആണ്.
- മുഴുവൻ റീപോസിറ്ററി വിവർത്തനം നിരവധി ഫയലുകൾ സൃഷ്ടിക്കാനും അപ്‌ഡേറ്റ് ചെയ്യാനും നീക്കം ചെയ്യാനും ഇടയാക്കാം. `confirm_write=true` സജ്ജമാക്കുന്നതിന് മുമ്പ് ഉപയോക്താവിന്റെ വ്യക്തമായ അംഗീകാരം ആവശ്യമുണ്ട്.
- കോൺഫിഗറേഷൻ സ്റ്റാറ്റസ് ടൂൾ എപ്പോഴും API കീകൾ, എന്റ്പോയിന്റുകൾ അല്ലെങ്കിൽ മറ്റ് രഹസ്യ മൂല്യങ്ങൾ തിരിച്ചുനൽകാറില്ല.
- ഇമേജ് വിവർത്തനം base64 ഇമേജ് ഡാറ്റ തിരികെ നൽകും. വലിയ ചിത്രങ്ങൾ വലിയ ടൂൾ റസ്പോൺസുകൾ സൃഷ്ടിക്കാൻ ഇടയാക്കാം.
- Agent-assisted ടൂളുകൾ സോഴ്‌സ് chunks-നും പ്രോംപ്റ്റുകൾക്കും MCP ഹോസ്റ്റിന് മടങ്ങി നൽകുന്നു. ആ ഹോസ്റ്റ് ഏജന്റ് മോഡലിലേക്ക് അയക്കാൻ ഉപയോക്താവ് സുഖമുളള ഉള്ളടക്കത്തിനേ മാത്രം അവ ഉപയോഗിക്കുക.