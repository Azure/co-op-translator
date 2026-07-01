# CLI റഫറൻസ്

Co-op Translator ഈ കമാൻഡ്-ലൈൻ എൻട്രി പോയിന്റുകൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നു:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links`, και `co-op-review` കമാൻഡുകൾ `co_op_translator.__main__` വഴി ഡിസ്പാച്ച് ചെയ്യപ്പെടുന്നു, ഇത് വിളിച്ച സ്ക്രിപ്റ്റ് പേരിന്റെ അടിസ്ഥാനത്തിൽ കമാൻഡ് ഇംപ്ലിമെന്റേഷൻ തെരഞ്ഞെടുത്ത് 실행 ചെയ്യും. MCP സർവർ `co_op_translator.mcp.server` നേരിട്ട് ഉപയോഗിക്കുന്നു.

CLI, Python API, ഉം MCP ഉം തമ്മിൽ തിരഞ്ഞെടുക്കുന്നതിൽ നിങ്ങൾ തീരുമാനമെടുക്കുകയാണെങ്കിൽ, [നിങ്ങളുടെ വർക്‌ഫ്ലോ തിരഞ്ഞെടുക്കുക](workflows.md) എന്നതിലേയ്ക്ക് ആരംഭിക്കുക.

## ആദ്യമായി CLI ഉപയോഗിക്കുന്നവരുടേത്

ടെർമിനലിൽനിന്ന് Co-op Translator ഉപയോഗിക്കുന്നവരോ തുടങ്ങുക:

1. [Configuration](configuration.md) ൽ വിശദീകരിച്ചിട്ടുള്ളതുപോലെ ഒരു LLM_PROVIDER കോൺഫിഗർ ചെയ്യുക.
2. നിങ്ങൾ വിവർത്തനം ചെയ്യാൻ ആഗ്രഹിക്കുന്ന ഉള്ളടക്ക തരം തിരഞ്ഞെടുക്കുക.
3. ആദ്യം ഫോകസഡ് കമാൻഡ് ஓന്ന് നടത്തുക, ഉദാഹരണത്തിന് Markdown-മാത്രം വിവർത്തനം.
4. വലിയ റപ്പോസിറ്ററി മാറ്റങ്ങൾക്ക് മുമ്പ് `--dry-run` ഉപയോഗിക്കുക.
5. ഘടനയും പുതുതലയും പരിശോധിക്കാൻ വിവർത്തനത്തിനുശേഷം `co-op-review` ഉപയോഗിക്കുക.

| ലക്ഷ്യം | ആരംഭിക്കാൻ കമാൻഡ് |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | CLI കമാൻഡുകൾ നേരിട്ട് പതിയ്ക്കുന്നതിനായി [MCP Server](mcp.md) കോൺഫിഗർ ചെയ്യുക. |

## translate

Markdown ഫയലുകൾ, നോട്ട്‌ബുക്കുകൾ, ഇമേജ് ടെക്സ്റ്റ് ഒന്നോ അതിൽ കൂടുതൽ ലക്ഷ്യംഭാഷകളിലേക്കോ വിവർത്തനം ചെയ്യുക.

```bash
translate -l "ko ja fr"
```

### സാധാരണ ഉദാഹരണങ്ങൾ

Markdown മാത്രം വിവർത്തനം ചെയ്യുക:

```bash
translate -l "de" -md
```

നോട്ട്‌ബുക്കുകൾ മാത്രം വിവർത്തനം ചെയ്യുക:

```bash
translate -l "zh-CN" -nb
```

Markdown and images కలిసి വിവർത്തനം ചെയ്യുക:

```bash
translate -l "pt-BR" -md -img
```

ഉളളതിരിച്ചെടുത്ത വിവർത്തനങ്ങൾ ഇല്ലാതാക്കി വീണ്ടും സൃഷ്‌ടിച്ച് നിലവിലുള്ള വിവർത്തനങ്ങൾ അപ്ഡേറ്റ് ചെയ്യുക:

```bash
translate -l "ko" -u
```

ഇന്ററാക്ടീവ് പ്രോംപ്റ്റുകൾ ഇല്ലാതെ 실행 ചെയ്യുക:

```bash
translate -l "ko ja" -md -y
```

ലോഗുകൾ സേവ് ചെയ്യുക:

```bash
translate -l "ko" -s
```

### ഓപ്ഷനുകൾ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | No | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | No | Enable debug logging in the console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Auto-confirm prompts, useful in CI. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration and translation estimates without writing files. |

ഓരോ തരം ഫ്ലാഗും നൽകാത്ത പക്ഷം, `translate` Markdown, നോട്ട്‌ബുക്ക്‌കൾ, ഇമേജുകൾ എല്ലാം പ്രോസസ്സ് ചെയ്യും. ഇമേജ് വിവർത്തനം Azure AI Vision കോൺഫിഗറേഷൻ ആവശ്യമാണ്.

## evaluate

ഒരു ഭാഷയ്ക്ക് വിവർത്തനമായ Markdown-ന്റെ ഗുണനിലവ് വിലയിരുത്തുക.

!!! warning "Experimental"
    `evaluate` പരീക്ഷണാത്മകമാണ്. ഇത് റൂൾ-ആധാരിതവും LLM-ആധാരിതവുമായ ഗുണനിലവാരം സംശോധനകൾ ഉപയോഗിക്കാൻ കഴിയും, വിലയിരുത്തൽ ഫലങ്ങൾ വിവർത്തന മെറ്റാഡാറ്റയിലേക്ക് എഴുതുന്നു, അതിന്റെ സ്കോറിംഗ് മോഡൽയും മെറ്റാഡാറ്റ പെരുമാറലും മാറാവുന്നതാണ്.

```bash
evaluate -l "ko"
```

### സാധാരണ ഉദാഹരണങ്ങൾ

കഠിനമായ കുറഞ്ഞ-ആത്മവിശ്വാസ പരിധി ഉപയോഗിക്കുക:

```bash
evaluate -l "es" -c 0.8
```

റൂൾ-ആധാരിത പരിശോധനകൾ മാത്രം നടത്തുക:

```bash
evaluate -l "fr" -f
```

LLM-ആധാരിത പരിശോധനകൾ മാത്രം നടത്തുക:

```bash
evaluate -l "ja" -D
```

### ഓപ്ഷനുകൾ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

డിഫോൾട്ടായി, `evaluate` റൂൾ-ആധാരിതവും LLM-ആധാരിതവും രണ്ടു രീതികളും ഉപയോഗിക്കുന്നു. ഫലങ്ങൾ വിവർത്തന മെറ്റാഡാറ്റയിലേക്ക് എഴുതപ്പെടുകയും കൺസോളിൽ സംഗ്രഹിക്കപ്പെടുകയും ചെയ്യുന്നു.

## co-op-review

API ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ детർമിനിസ്റ്റിക് വിവർത്തന പരിപാലന പരിശോധനകൾ ഓടിക്കുക.

!!! note "Beta"
    `co-op-review` ബീറ്റാ ഘട്ടത്തിലുള്ള ഒരു ഡീറ്റർമിനിസ്‌റ്റിക് റിവ്യൂ കമാൻഡാണ്. ഇത് മോഡൽ പ്രൊവൈഡർമാരെ വിളിക്കില്ല, ഫയലുകൾ എഴുത്തില്ല, എന്നാല്‍ അതിന്റെ ചെക്കുകളും പ്രശ്നങ്ങളുടെയും ഔട്ട്‌പുട്ട് സ്കീമയും മാറാം.

```bash
co-op-review -l "ko"
```

### സാധാരണ ഉദാഹരണങ്ങൾ

നിലവിലെ ഡയറക്ടറിയിൽ നിന്ന് കൊറിയൻ և ജപ്പാനീസ് വിവർത്തനങ്ങൾ റിവ്യൂ ചെയ്യുക:

```bash
co-op-review -l "ko ja"
```

നിർദ്ദിഷ്ട പ്രോജക്ട് റൂട്ടിനെ റിവ്യൂ ചെയ്യുക:

```bash
co-op-review -l "fr" -r ./my-course
```

ബേസ് റഫിന്‍െതിരെ മാറ്റപ്പെട്ട സോഴ്സ് ഫയലുകൾ മാത്രം റിവ്യൂ ചെയ്യുക:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI സംഗ്രഹങ്ങൾക്കായി GitHub-ഫ്ലേവർഡ് Markdown ഔട്ട്പുട്ട് പ്രിന്റ് ചെയ്യുക:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### ഓപ്ഷനുകൾ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` നിലവിൽ കാണപ്പെടാത്ത വിവർത്തന ഫയലുകൾ, ഉണ്ടാക്കാത്തതോ പഴയതായ വിവർത്തന മെറ്റാഡാറ്റ, Markdown frontmatter-ഉം കോഡ് ഫെൻസ് സംരക്ഷണം, അസാധുവായ വിവർത്തന നോട്ട്‌ബുക്ക് JSON, ലോക്കൽ Markdown അല്ലെങ്കിൽ ഇമേജ് ലിങ്ക് ലക്ഷ്യങ്ങളുടെ കുറവ് എന്നിവ പരിശോധിക്കുന്നു. കുറവായ ലിങ്കുകൾ ഡീഫോൾട്ടായി മുന്നറിയിപ്പുകളാണ്; ഘടനാത്മകവും പുതുതല പ്രശ്നങ്ങളും കമാൻഡ് പരാജയപ്പെടുന്ന കാരണങ്ങളാണ്.

## co-op-translator-mcp

ഏജന്റുകൾക്കായി, എഡിറ്റർമാർക്കായി, MCP-സ്കോപ്പിലുള്ള ക്ലയന്റുകൾക്കായി Co-op Translator MCP സർവർ ഓടിക്കുക.

```bash
co-op-translator-mcp
```

ഡീഫോൾട്ട് ട്രാൻസ്പോർട്ട് `stdio` ആണ്. ക്ലയന്റ് കോൺഫിഗറേഷൻ, ടൂൾസ്, റിസോഴ്‌സുകൾ, സുരക്ഷാ കുറിപ്പുകൾ എന്നിവയ്ക്ക് [MCP Server](mcp.md) മാർഗനിർദ്ദേശം കാണുക.

### ഓപ്ഷനുകൾ

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

വിവർത്തനമാക്കിയ Markdown ഫയലുകൾ വീണ്ടും പ്രോസസ്സ് ചെയ്ത് നോട്ട്ബുക്ക് ലിങ്കുകൾ ലഭ്യമായാൽ വിവർത്തന നോട്ട്‌ബുക്കുകളിലേക്ക് പോയിന്റ് ചെയ്യുന്നതായി അപ്ഡേറ്റ് ചെയ്യുക.

```bash
migrate-links -l "ko ja"
```

### സാധാരണ ഉദാഹരണങ്ങൾ

ലിങ്ക് അപ്‌ഡേറ്റുകൾ മുന്നോട്ടുള്ക്ക് കാണുക:

```bash
migrate-links -l "ko" --dry-run
```

Confirm ഇല്ലാതെ എല്ലാ സപ്പോർട്ടഡ് ഭാഷകളും പ്രോസസ്സ് ചെയ്യുക:

```bash
migrate-links -l "all" -y
```

വിവർത്തന നോട്ട്‌ബുക്കുകൾ മാത്രമേ ഉണ്ടായിരിക്കുമ്പോഴേ ലിങ്കുകൾ പുനഃലേഖനം ചെയ്യൂ:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### ഓപ്ഷനുകൾ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | No | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Auto-confirm prompts when processing all languages. |

## Environment

എല്ലാ കമാൻഡുകളും ഒരു കോൺഫിഗർ ചെയ്ത LLM പ്രൊവൈഡർ ഒന്നിനെ ആവശ്യപ്പെടുന്നു:

```bash
# ആസ്യൂർ ഓപൺഎഐ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# അതവാ ഓപൺഎഐ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

ഇമേജ് വിവർത്തനത്തിന് കൂടാതെ Azure AI Vision ആവശ്യമാണ്:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## ഔട്ട്പുട്ട് ലേയൗട്ട്

ടെക്സ്റ്റ് വിവർത്തനങ്ങൾ താഴെ എഴുതപ്പെടുന്നു:

```text
translations/<language-code>/<original-path>
```

വിവർത്തനമായ ഇമേജ് ഔട്ട്പുട്ട് താഴെ എഴുതപ്പെടുന്നു:

```text
translated_images/<language-code>/<original-path>
```

ഉദാഹരണത്തിന്, `README.md` และ `docs/setup.md` കൊറിയൻ ഭാഷയിലേക്കു വിവർത്തനം ചെയ്യുമ്പോൾ ഉളള ഫയൽ നിർമ്മാണം:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## കോപി-പേസ്റ്റ് CLI ഉദാഹരണങ്ങൾ

Markdown മൂന്ന് ഭാഷകളിലേക്കു വിവർത്തനം ചെയ്യുക:

```bash
translate -l "ko ja fr" -md
```

നോട്ട്‌ബുക്കുകൾ മാത്രം വിവർത്തനം ചെയ്യുക:

```bash
translate -l "zh-CN" -nb
```

ഇമേജുകൾ മാത്രം വിവർത്തനം ചെയ്യുക:

```bash
translate -l "pt-BR" -img
```

Markdown വിവർത്തനം ഫയലുകൾ എഴുതാതെ മുപ്പറാക്കൽ കാണുക:

```bash
translate -l "de es" -md --dry-run
```

കുറഞ്ഞ-ആത്മവിശ്വാസമുള്ള Markdown വിവർത്തനങ്ങൾ റിപ്പെയ്ർ ചെയ്യുക:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI സൗഹൃദ Markdown വിവർത്തനം നടത്തുക:

```bash
translate -l "ko ja" -md -y -s
```

വിവർത്തന ഔട്ട്പുട്ട് റിവ്യൂ ചെയ്യുക:

```bash
co-op-review -l "ko ja"
```

ലിങ്ക് മൈഗ്രേഷൻ മുൻകൂർ കാണുക:

```bash
migrate-links -l "ko" --dry-run
```