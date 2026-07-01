# ម៉ាស៊ីនបម្រើ MCP

Co-op Translator មានម៉ាស៊ីនបម្រើ Model Context Protocol សម្រាប់ភ្នាក់ងារ អ្នកកែសម្រួល និងអ្នកប្រើប្រាស់ដែលគាំទ្រ MCP ។

សម្រាប់ការកំណត់ค่า​រកទីតាំង​ឈានមូលដ្ឋាន (local) ពេញនិយម អ្នកប្រើមិនចាំបាច់រត់ម៉ាស៊ីនបម្រើបាក់​ទូដដោយដៃឡើយ។ ពួកគេកំណត់តម្លៃអតិថិជន MCP របស់ពួកគេ ហើយអតិថិជននោះនឹងចាប់ផ្តើម `co-op-translator-mcp` ដោយស្វ័យប្រវត្តិលើ `stdio` នៅពេលវាត្រូវការឧបករណ៍ Co-op Translator ។

បើអ្នកកំពុងសម្រេចចិត្តរវាង CLI, Python API, និង MCP សូមចាប់ផ្ដើមជាមួយ [Choose Your Workflow](workflows.md) ។

ប្រើ MCP នៅពេលភ្នាក់ងារ ឬអ្នកកែសម្រួល គួរតែនៅតែហៅ Co-op Translator ដោយផ្ទាល់៖

| គោលដៅអ្នកប្រើ | ឧបករណ៍ MCP |
| --- | --- |
| បកប្រែឯកសារ Markdown មួយ ឬ notebook ឬ រូបភាព | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| បកប្រែខ្លឹមសារ Markdown ឬ notebook ជាមួយម៉ូដែលភ្ញៀវ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| កែសម្រួលភ្ជាប់ Markdown ឬ notebook បន្ទាប់ពីជ្រើសទីតាំងផ្លូវចេញ | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| បកប្រែ repository ទាំងមូល ដូចជា CLI | `run_translation`, `translate_project` |
| ពិនិត្យលទ្ធផលបកប្រែក្នុងគ្មានសមាជិក LLM | `run_review` |
| ពិនិត្យមើលសមត្ថភាព និងស្ថានភាពបរិបទ | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

ម៉ាស៊ីន​បម្រើ MCP បញ្ចอบ API សាធារណៈ Python ដដែលដែលបានរាយនៅ [Python API](api.md) ។ ឧបករណ៍ដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ប្រើអ្នកផ្គត់ផ្គង់ដែលបានកំណត់ដូចជា CLI និង Python API ។ ឧបករណ៍ជួយដោយភ្នាក់ងារ (Agent-assisted) រៀបចំចំណែកសម្រាប់ភ្ញៀវម៉ាស៊ីនបម្រើ MCP ដើម្បីបកប្រែ បន្ទាប់មកប្រើ Co-op Translator ដើម្បីសង់ឡើងវិញ Markdown ឬ notebook ចុងក្រោយ។

## ជំហ៊ាន 1: តំឡើង និងកំណត់ค่า Co-op Translator

តំឡើង Co-op Translator នៅក្នុងបរិយាកាស Python ដែលអតិថិជន MCP របស់អ្នកនឹងប្រើ៖

```bash
pip install co-op-translator
```

សម្រាប់ការអភិវឌ្ឍនៅលើដែនកំណត់ពី repository នេះ តំឡើង package ក្នុងម៉ូដដែលអាចកែបាន (editable mode)៖

```bash
pip install -e .
```

ជ្រើសម៉ូដបកប្រែដែលអតិថិជន MCP របស់អ្នកនឹងប្រើ៖

| Mode | ប្រើសម្រាប់ | ទិន្នន័យសមាធី (Credentials) |
| --- | --- | --- |
| Provider-backed | Co-op Translator ហៅ `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ឬ `run_translation`។ | ការបកប្រែ Markdown និង notebook ត្រូវការកូនស្រី Azure OpenAI ឬ OpenAI។ ការបកប្រែរូបភាពក៏ត្រូវការក៏ Azure AI Vision។ |
| Agent-assisted | ភ្ញៀវម៉ាស៊ីនបម្រើ MCP បកប្រែចំណែកដែលបានត្រឡប់ពី `start_markdown_agent_translation` ឬ `start_notebook_agent_translation`។ | មិនចាំបាច់មានសមាជិក Co-op Translator LLM សម្រាប់ចំណែក Markdown ឬ notebook។ មូដ agent-assisted មិនទាន់គ្របដណ្តប់ការបកប្រែរូបភាពទេ។ |

បើអ្នកចាប់ផ្តើមជាមួយការបកប្រែ Markdown ឬ notebook ក្នុងភ្នាក់ងារដូចជា Codex ឬ Claude Code សូមចាប់ផ្តើមជាមួយម៉ូដ agent-assisted ។ ប្រើ provider-backed បើអ្នកចង់ឲ្យ Co-op Translator ហៅអ្នកផ្គត់ផ្គង់ដែលបានកំណត់ផ្ទាល់ ឬពេលអ្នកកំពុងបកប្រែរូបភាព ឬពេលអ្នកកំពុងរត់ការបកប្រែកម្រិត repository ដូចជា CLI ។

កំណត់សម្រាប់ភ្ជាប់អ្នកផ្គត់ផ្គង់តែសម្រាប់កម្មវិធីដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ (provider-backed)៖

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ការបកប្រែរូបភាពដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ត្រូវការបន្ថែម៖

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ម៉ូដ agent-assisted ពាក់ព័ន្ធបច្ចុប្បន្នគ្របដណ្តប់ Markdown និងកោសិកា Markdown ក្នុង notebook។ ការបកប្រែរូបភាពនៅតែប្រើបំពង់រូបភាពដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ ហើយត្រូវការកូនស្រី Azure AI Vision សម្រាប់ OCR និង ការបង្ហាញដែលយល់ពីលំដាប់ទំហំ (layout-aware) ។

## ជំហ៊ាន 2: កំណត់តម្លៃអតិថិជន MCP របស់អ្នក

សម្រាប់ការកំណត់ `stdio` ទូទៅនៅក្នុងเครื่องកុំព្យូទ័រផ្ទាល់ (local) បន្ថែម Co-op Translator ទៅក្នុងការកំណត់តម្លៃអតិថិជន MCP របស់អ្នក។ អតិថិជននឹងចាប់ផ្តើម និងបញ្ឈប់ដំណើរការ ដោយស្វ័យប្រវត្តិក្នុងករណីនេះ។

កំណត់តម្លៃ package ដែលបានតំឡើង:

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

កំណត់តម្លៃពី source checkout លើ Windows:

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

កំណត់តម្លៃពី source checkout លើ macOS ឬ Linux:

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

បន្ទាប់ពីផ្លាស់ប្តូរការកំណត់អតិថិជន MCP សូមបញ្ចុះ ឬផ្ទុកឡើងវិញអតិថិជន ដើម្បីវាមានឱកាសស្វែងរកម៉ាស៊ីនបម្រើថ្មី។

## ជំហ៊ាន 3: បញ្ជាក់ម៉ាស៊ីនបម្រើក្នុងអតិថិជន

ស្នើអតិថិជន MCP ដើម្បីបញ្ជីឧបករណ៍ដែលមាន សូម្បីតែហៅមួយក្នុងចំណោមកម្មវិធីជំនួយសម្រាប់អានគត់៖

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ការត្រួតពិនិត្យដំបូងដែលមានប្រយោជន៍៖

| ឧបករណ៍ | ត្រូវត្រួតពិនិត្យអ្វី |
| --- | --- |
| `get_api_overview` | បញ្ជាក់ថាម៉ាស៊ីនបម្រើអាចទំនាក់ទំនងបាន និងបង្ហាញ workflow ដែលមាន។ |
| `list_supported_languages` | បញ្ជាក់ថា ទិន្នន័យភាសាបញ្ចូលអាចផ្ទុកបាន។ |
| `get_configuration_status` | បញ្ជាក់ពីភាពជាប់រួមរបស់អ្នកផ្គត់ផ្គង់ LLM និង Vision ដោយមិនបង្ហាញតម្លៃសម្ងាត់។ |

## ជំហ៊ាន 4: ជ្រើស workflow

### បកប្រែឯកសារឬឯកសារឯកតាច្រើនៗ

ប្រើឧបករណ៍ដែលពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ (provider-backed content tools) នៅពេលអតិថិជន MCP មានខ្លឹមសារឯកសារឬផ្លូវរូបភាព និងចង់ឲ្យ Co-op Translator ហៅអ្នកផ្គត់ផ្គង់ដែលបានកំណត់។

សម្រាប់ Markdown:

1. ហៅ `translate_markdown_content` ជាមួយ `document`, `language_code`, និងជម្រើស `source_path` ។
2. ប្រសិនបើលទ្ធផលបានបកប្រែត្រូវបានសរសេរចូលទ្រង់ទ្រាយចេញ Co-op Translator សូមហៅ `rewrite_markdown_paths` ។
3. អនុញ្ញាតឲ្យអតិថិជនសរសេរ ឬត្រឡប់ `content` ចុងក្រោយ។

សម្រាប់ notebooks:

1. ហៅ `translate_notebook_content` ជាមួយ JSON នៃ notebook និង `language_code` ។
2. ហៅ `rewrite_notebook_paths` ប្រសិនបើភ្ជាប់ក្នុង notebook ដែលបានបកប្រែត្រូវត្រូវបានកែសម្រួលសម្រាប់ផ្លូវគោលដៅ។
3. សរសេរ ឬត្រឡប់ JSON នៃ notebook ចុងក្រោយ។

សម្រាប់រូបភាព:

1. ហៅ `translate_image_content` ជាមួយ `image_path`, `language_code`, និងជម្រើស `root_dir` ឬ `fast_mode` ។
2. អាន `data_base64` និង `mime_type` ដែលត្រូវបានត្រឡប់មកវិញ។
3. ប្រសិនបើបានផ្តល់ `output_path` រូបភាពដែលបានបកប្រែក៏ត្រូវបានរក្សាទុកនៅផ្លូវនោះផងដែរ។

ឧបករណ៍ខ្លឹមសារ (content tools) មិនអនុវត្តការស្វែងរក project, បច្ចប្បន្នភាព metadata, សេចក្តីប្រកាសបក្សព័ន្ធ, ឬការកែសម្រួលផ្លូវដោយស្វ័យប្រវត្តិទេ។ ប្រសិនបើអ្នកចង់ឲ្យភ្ញៀវម៉ាស៊ីនបម្រើបកប្រែចំណែក Markdown ឬ notebook ដោយគ្មានសមាជិក Co-op Translator LLM បញ្ចូល សូមប្រើ workflow agent-assisted ខាងក្រោម។

### បកប្រែជាមួយម៉ូដែលភ្ញៀវ (Host Agent Model)

ប្រើឧបករណ៍ agent-assisted នៅពេលអ្នកចង់ឲ្យភ្ញៀវម៉ាស៊ីនបម្រើ MCP ផ្ទាល់ ដូចជា ជំនួយការកូដ កំណត់អក្សរ ដែលផលិតអត្ថបទបានបកប្រែជំនួសការកំណត់ Azure OpenAI ឬ OpenAI សម្រាប់ Co-op Translator ។

នៅក្នុងអតិថិជន MCP ប្រភេទ chat-based ទូទៅ អ្នកមិនចាំបាច់សរសេរ JSON ដៃសម្រាប់ឧបករណ៍ទេ។ សូមស្នើឲ្យភ្ញៀវប្រើ workflow agent-assisted៖

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

សម្រាប់ notebooks ប្រើទម្រង់ដូចគ្នា៖

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ប្រសិនបើអតិថិជន MCP របស់អ្នកគាំទ្រ server prompts សូមប្រើ `agent_assisted_markdown_translation_prompt` ដើម្បីឲ្យអតិថិជនផ្ទុកសេចក្តីណែនាំ workflow ដូចគ្នា។

សម្រាប់ Markdown:

1. ហៅ `start_markdown_agent_translation` ជាមួយ `document`, `language_code`, និងជម្រើស `source_path` ។
2. បកប្រែចំណែកដែលត្រូវបានត្រឡប់មកក្នុងភ្ញៀវម៉ាស៊ីនបម្រើដោយអនុវត្ត `prompt` របស់ចំណែកនីមួយៗ។
3. ហៅ `finish_markdown_agent_translation` ជាមួយ `job` ដើម និងចំណែកដែលបានបកប្រែក្នុងការ​ប្រើ `chunk_id` និង `translated_text` ។
4. ប្រសិនបើខ្លឹមសារត្រូវបានសរសេរចូលផ្លូវគោលដៅដែលបានបកប្រែ សូមហៅ `rewrite_markdown_paths` ។

សម្រាប់ notebooks:

1. ហៅ `start_notebook_agent_translation` ជាមួយ JSON នៃ notebook និង `language_code` ។
2. បកប្រែចំណែកនីមួយៗក្នុងភ្ញៀវម៉ាស៊ីនបម្រើ។
3. ហៅ `finish_notebook_agent_translation` ជាមួយ `job` ដើម និងចំណែកដែលបានបកប្រែ។
4. ហៅ `rewrite_notebook_paths` ប្រសិនបើភ្ជាប់ក្នុង notebook ត្រូវការកែសម្រួលសម្រាប់ផ្លូវគោលដៅ។

ឧបករណ៍ agent-assisted មិនហៅ Azure OpenAI ឬ OpenAI ពី Co-op Translator ទេ។ ភ្ញៀវម៉ាស៊ីនបម្រើមានកាតព្វកិច្ចក្នុងការបកប្រែចំណែកដែលត្រូវបានត្រឡប់។ Co-op Translator ប្រគល់ការចែកចាយ Markdown, រក្សាទុកកន្លែងទំនេរ (placeholders), សង់ឡើងវិញ frontmatter, ជំនួសកោសិកា notebook, និងធ្វើ normalization បន្ទាប់បកប្រែ។

### បកប្រែ Repository ទាំងមូល

ប្រើ `run_translation` នៅពេលអ្នកចង់ឲ្យ Co-op Translator ប្រព្រឹត្តទៅដូចជា CLI `translate` ។

ការបកប្រែ repository នឹងកំណត់តម្លៃលំនាំដើមជា `dry_run=true` ដូច្នេះភ្ញៀវអាចពិនិត្យដែនកំណត់មុនការផ្លាស់ប្តូរ​ឯកសារ៖

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

ដើម្បីអនុញ្ញាតឲ្យសរសេរ និយោជកត្រូវតែដាក់ទាំង `dry_run=false` និង `confirm_write=true` ៖

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ត្រូវបានបង្ហាញជាឈ្មោះជំនួសសមត្ថភាពសម្រាប់ `run_translation` ។

### ពិនិត្យលទ្ធផលដែលបានបកប្រែ

ប្រើ `run_review` សម្រាប់ការត្រួតពិនិត្យដែលកំណត់ទិសដៅ ដែលមិនទាមទារសមាជិក LLM ឬ Vision ៖

!!! note "Beta"
    MCP បង្ហាញ API ជាកម្រិតប៊ីតា `run_review` ។ វាសុវត្ថិសម្រាប់ workflow ពិនិត្យអានតែប៉ុណ្ណោះ ប៉ុន្តែការត្រួតពិនិត្យ និង schema កំហុសអាចបន្តផ្លាស់ប្តូរបាន។

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

លទ្ធផលរួមមានលទ្ធផលអក្សរដែលចាប់បាន និងសេចក្តីសង្ខេបការពិនិត្យដែលមានរចនាសម្ព័ន្ធនៅពេលមាន។

## រត់ម៉ាស៊ីនបម្រើដោយដៃ (Manual Server Runs)

ការរត់ដោយដៃភាគច្រើនសម្រាប់ដោះស្រាយបញ្ហា ឬសម្រាប់ការដឹកជញ្ជូនដែលប្រព្រឹត្តដូចម៉ាស៊ីនបម្រើដំណើររយៈប្រវែងវែង។

ដោះស្រាយបញ្ហាម៉ាស៊ីនបម្រើ stdio លំនាំដើម៖

```bash
co-op-translator-mcp
```

រត់ពី source checkout៖

```bash
python -m co_op_translator.mcp.server
```

រត់ម៉ាស៊ីនបម្រើ HTTP ឬ SSE អាយុកាលវែង៖

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

សម្រាប់ការរួមបញ្ចូលជាមួយកម្មវិធីកែសម្រួល និងភ្នាក់ងារក្នុងដែនកំណត់ (local) សូមពេញចិត្តជាមួយការកំណត់ `stdio` ដែលគ្រប់គ្រងដោយអតិថិជន ក្នុងជំហ៊ាន 2 ។

## ឧបករណ៍

| ឧបករណ៍ | គោលបំណង | សរសេរឯកសារ |
| --- | --- | --- |
| `translate_markdown_content` | បកប្រែអក្សារ Markdown មួយ។ | ទេ |
| `translate_notebook_content` | បកប្រែកោសិកា Markdown ក្នុង JSON នៃ notebook។ | ទេ |
| `translate_image_content` | បកប្រែអត្ថបទក្នុងរូបភាពមួយ និងត្រឡប់ទិន្នន័យរូបភាពជា base64។ | ជម្រើស, មានតែពេល `output_path` ត្រូវបានផ្តល់ |
| `start_markdown_agent_translation` | ត្រៀមចំណែក Markdown សម្រាប់ភ្ញៀវម៉ាស៊ីនបម្រើបកប្រែដោយគ្មានសមាជិក Co-op Translator LLM។ | ទេ |
| `finish_markdown_agent_translation` | ស្ដារឡើងវិញ Markdown ពីចំណែកដែលភ្ញៀវម៉ាស៊ីនបម្រើបានបកប្រែ។ | ទេ |
| `start_notebook_agent_translation` | ត្រៀមចំណែកកោសិកា Markdown ក្នុង notebook សម្រាប់ភ្ញៀវម៉ាស៊ីនបម្រើបកប្រែ។ | ទេ |
| `finish_notebook_agent_translation` | ស្ដារឡើងវិញ JSON នៃ notebook ពីចំណែកដែលភ្ញៀវម៉ាស៊ីនបម្រើបានបកប្រែរ។ | ទេ |
| `rewrite_markdown_paths` | កែសម្រួលផ្លូវក្នុងខ្លឹមសារ Markdown និង frontmatter សម្រាប់គោលដៅដែលបានបកប្រែ។ | ទេ |
| `rewrite_notebook_paths` | កែសម្រួលផ្លូវក្នុងកោសិកា Markdown របស់ notebook។ | ទេ |
| `run_translation` | រត់ការបកប្រែកម្រិត project ដូចជា CLI។ | មាន នៅពេល `dry_run=false` និង `confirm_write=true` |
| `translate_project` | ឈ្មោះជំនួសសមរម្យសម្រាប់ `run_translation`។ | មាន នៅពេល `dry_run=false` និង `confirm_write=true` |
| `run_review` | រត់ការត្រួតពិនិត្យដែលកំណត់ទិសដៅ។ | ទេ |
| `get_configuration_status` | រាយការណ៍អ្នកផ្គត់ផ្គង់ LLM និង Vision ដែលបានកំណត់ ដោយមិនបង្ហាញសម្ងាត់។ | ទេ |
| `list_supported_languages` | បញ្ជីកូដភាសាគោលដៅដែលគាំទ្រ។ | ទេ |
| `get_api_overview` | ពិពណ៌នាអំពី workflow និងឧបករណ៍ MCP ដែលមាន។ | ទេ |

## ធនធាន

| Resource URI | គោលបំណង |
| --- | --- |
| `co-op://api` | សេចក្តីសង្ខេប JSON នៃ workflow និងឧបករណ៍។ |
| `co-op://supported-languages` | បញ្ជី JSON នៃកូដភាសាដែលគាំទ្រ។ |
| `co-op://configuration` | សេចក្តីសង្ខេបភាពមានស្រាប់របស់អ្នកផ្គត់ផ្គង់ ដោយមិនមានសម្ងាត់។ |

## សេចក្តីណែនាំ (Prompts)

| Prompt | គោលបំណង |
| --- | --- |
| `translate_markdown_document_prompt` | មគ្គុទេសក៍សម្រាប់អតិថិជន MCP តាមរយៈការបកប្រែខ្លឹមសារ និងជម្រើសកែផ្លូវ។ |
| `agent_assisted_markdown_translation_prompt` | មគ្គុទេសក៍សម្រាប់អតិថិជន MCP តាមរយៈការបកប្រែ Markdown ដោយភ្ញៀវម៉ាស៊ីនបម្រើ ដោយគ្មានសមាជិក LLM នៃ Co-op Translator។ |
| `translate_repository_prompt` | មគ្គុទេសក៍សម្រាប់អតិថិជន MCP តាមរយៈការបកប្រែ repository ដែលអនុវត្ត dry-run មុន។ |

## ឧទាហរណ៍ចម្លង-បិទបិទ (Copy-Paste Examples)

បកប្រែខ្លឹមសារ Markdown៖

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

កែសម្រួលភ្ជាប់ Markdown ដែលបានបកប្រែ៖

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

បកប្រែ Markdown ជាមួយម៉ូដែលភ្ញៀវ៖

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

បន្ទាប់ពីភ្ញៀវម៉ាស៊ីនបម្រើបកប្រែចំណែកដែលបានត្រឡប់មក ត្រូវបញ្ចប់ការងារ ដោយប្រើ `job` ពេញលេញ ដែលត្រូវបានត្រឡប់ពី `start_markdown_agent_translation` ៖

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ទស្សនាមុនការបកប្រែ repository៖

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

## ដោះស្រាយបញ្ហា (Troubleshooting)

| បញ្ហា | ត្រូវព្យាយាមអ្វី |
| --- | --- |
| អតិថិជន MCP មិនអាចរកឃើញ `co-op-translator-mcp` បាន។ | ប្រើ path លម្អិតនៃ Python executable និង `["-m", "co_op_translator.mcp.server"]` ក្នុងកំណត់តម្លៃ source checkout។ |
| ម៉ាស៊ីនបម្រើត្រូវបានរាយប៉ុណ្ណោះ តែការបកប្រែបរាជ័យ។ | ហៅ `get_configuration_status` និងបញ្ជាក់ថាអ្នកផ្គត់ផ្គង់ LLM មានស្រាប់។ |
| អ្នកចង់បានការបកប្រែ Markdown ឬ notebook ដោយគ្មានកូនស្រី Azure OpenAI/OpenAI ។ | ប្រើ `start_markdown_agent_translation` / `finish_markdown_agent_translation` ឬប្រភេទ notebook ឲ្យភ្ញៀវម៉ាស៊ីនបម្រើបកប្រែចំណែក។ |
| ការបកប្រែរូបភាពបរាជ័យ។ | បញ្ជាក់ថาตัวแปร Azure AI Vision ត្រូវបានកំណត់ ហើយហៅ `get_configuration_status` ។ |
| ការបកប្រែ repository មិនបានសរសេរឯកសារ។ | ដាក់ `dry_run=false` និង `confirm_write=true` បន្ទាប់ពីមានការយល់ព្រមច្បាស់ពីអ្នកប្រើ។ |
| ការផ្លាស់ប្តូរទៅកាន់កំណត់តម្លៃអតិថិជនមិនបង្ហាញ។ | ចាប់ផ្តើមឡើងវិញ ឬផ្ទុកឡើងវិញអតិថិជន MCP ។

## សេចក្តីអនុវត្តសុវត្ថិភាព (Safety Notes)

- ការ ហៅឧបករណ៍ MCP ត្រូវបានគ្រប់គ្រងដោយម៉ូដែល (model-controlled) ដោយកម្មវិធីម្ចាស់ (host application), ដូច្នេះការបកប្រែ repository ត្រូវបានកំណត់ជា dry-run ដោយលំនាំ។
- ការបកប្រែ repository ពេញលេញ អាចបង្កើត បច្ចុប្បន្នភាព ឬលុបឯកសារច្រើន។ សូមទាមទារការយល់ព្រមកំណត់ច្បាស់ពីអ្នកប្រើ មុនពេលដាក់ `confirm_write=true` ។
- ឧបករណ៍ស្ថានភាពកំណត់ (configuration status) មិនដែលត្រឡប់សោ API, endpoints, ឬតម្លៃសម្ងាត់ផ្សេងទៀតឡា។ 
- ការបកប្រែរូបភាព ត្រឡប់ទិន្នន័យរូបភាពជា base64។ រូបភាពធំនឹងបង្កើតចម្លើយឧបករណ៍ដែលធំ។ 
- ឧបករណ៍ agent-assisted ត្រឡប់ចំណែកដើម និង prompt ទៅភ្ញៀវម៉ាស៊ីនបម្រើ MCP។ ប្រើវិធីនេះតែនៅពេលខ្លឹមសារដែលអ្នកប្រើមានមនសិទ្ធិស្នាក់នៅក្នុងការផ្ញើទៅម៉ូដែលភ្ញៀវនោះ។