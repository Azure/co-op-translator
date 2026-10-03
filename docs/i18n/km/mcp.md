# ម៉ាស៊ីនមេ MCP

Co-op Translator រួមមានម៉ាស៊ីនមេ Model Context Protocol សម្រាប់ភ្នាក់ងារ អេឌីទ័រ និងកម្មវិធីអតិថិជនដែលគាំទ្រ MCP។

សម្រាប់ការកំណត់លំនាំដើមនៅក្នុងបរិយាកាស local អ្នកប្រើមិនចាំបាច់រត់ម៉ាស៊ីនមេបំបែកដោយដៃទេ។ ពួកគេកំណត់រចនាសម្ព័ន្ធកម្មវិធីអតិថិជន MCP ហើយអតិថិជននោះនឹងចាប់ផ្ដើម `co-op-translator-mcp` ដោយស្វ័យប្រវត្តិតាម `stdio` នៅពេលដែលវាត្រូវការឧបករណ៍ Co-op Translator។

បើអ្នកកំពុងជ្រើសរើសរវាង CLI, Python API, និង MCP សូមចាប់ផ្ដើមជាមួយ [ជ្រើសរើសដំណើរការងារ](workflows.md)។

ប្រើ MCP នៅពេលដែលភ្នាក់ងារ ឬកម្មវិធីកែសម្រួល គួរត្រូវហៅ Co-op Translator ដោយផ្ទាល់៖

| គោលដៅ​អ្នក​ប្រើ | ឧបករណ៍ MCP |
| --- | --- |
| បកប្រែឯកសារ Markdown, notebook ឬរូបភាពមួយ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| បកប្រែមាតិកា Markdown ឬ notebook ជាមួយម៉ូដែលភ្នាក់ងារ (host agent model) | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| សរសេរឡើងវិញតំណភ្ជាប់នៃ Markdown ឬ notebook បន្ទាប់ពីជ្រើសផ្លូវចេញ | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| បកប្រែគម្រោងទាំងមូលដូចជា CLI | `run_translation`, `translate_project` |
| ពិនិត្យលទ្ធផលដែលបានបកប្រែដោយគ្មានសញ្ញាប័ត្រ LLM | `run_review` |
| ពិនិត្យសមត្ថភាព និងស្ថានភាពបរិយាកាស | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

ម៉ាស៊ីនមេ MCP ប្រមូល API សាធារណៈ Python ដូចគ្នាដែលបានតំណើរការនៅក្នុង [Python API](api.md)។ ឧបករណ៍ដែលផ្អែកលើអ្នកផ្តល់ប្រើអ្នកផ្តល់ដែលបានកំណត់រចនាសម្ព័ន្ធដូចគ្នាជាមួយ CLI និង Python API។ ឧបករណ៍ជំនួយដោយភ្នាក់ងារ រៀបចំគ្រាប់សម្រាប់ភ្នាក់ងារម្ចាស់ MCP ឲ្យបកប្រែ បន្ទាប់មកប្រើ Co-op Translator ដើម្បីស្តារឡើងវិញ Markdown ឬ notebook ចុងក្រោយ។

## ជំហានទី 1: ធ្វើការ​ដំឡើង និងកំណត់រចនាសម្ព័ន្ធ Co-op Translator

ដំឡើង Co-op Translator នៅក្នុងបរិយាកាស Python ដែលកម្មវិធីអតិថិជន MCP របស់អ្នកនឹងប្រើ៖

```bash
pip install co-op-translator
```

សម្រាប់ការអភិវឌ្ឍក្នុងស្រុកពី repository នេះ សូមដំឡើង package ក្នុងរបៀប editable៖

```bash
pip install -e .
```

ជ្រើសរើសរបៀបបកប្រែដែលកម្មវិធីអតិថិជន MCP របស់អ្នកនឹងប្រើ៖

| របៀប | ប្រើសម្រាប់ | សញ្ញាប័ត្រ |
| --- | --- | --- |
| Provider-backed | Co-op Translator នឹងហៅ `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ឬ `run_translation`។ | ការបកប្រែត្រូវការអ្នកផ្តល់ Azure OpenAI, OpenAI, ឬ Anthropic។ ការបកប្រែរូបភាពក៏ត្រូវការ Azure AI Vision ផងដែរ។ |
| Agent-assisted | ភ្នាក់ងារម្ចាស់ MCP បកប្រែគ្រាប់ដែលត្រឡប់មកពី `start_markdown_agent_translation` ឬ `start_notebook_agent_translation`។ | មិនត្រូវការសញ្ញាប័ត្រ provider LLM របស់ Co-op Translator សម្រាប់គ្រាប់ Markdown ឬ notebook។ ការបកប្រែរូបភាពមិនទាន់គ្របដណ្តប់ដោយម៉ូដជំនួយដោយភ្នាក់ងារ។ |

ប្រសិនបើអ្នកចាប់ផ្ដើមជាមួយការបកប្រែ Markdown ឬ notebook ក្នុងភ្នាក់ងារ ដូចជា Codex ឬ Claude Code សូមចាប់ផ្ដើមដោយម៉ូដជំនួយដោយភ្នាក់ងារ។ ប្រើម៉ូដដែលផ្អែកលើអ្នកផ្តល់ នៅពេលដែលអ្នកចង់ឲ្យ Co-op Translator សរសេរហៅអ្នកផ្តល់ដែលបានកំណត់ដោយខ្លួនឯង, នៅពេលដែលអ្នកកំពុងបកប្រែរូបភាព, ឬនៅពេលដែលអ្នកកំពុងរត់ការបកប្រែកម្រិតគម្រោងដូចជា CLI។

កំណត់អ្នកផ្តល់មួយសម្រាប់ workflow ដែលផ្អែកលើអ្នកផ្តល់៖

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ឬ OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# ឬ Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

ការបកប្រែរូបភាពដែលផ្អែកលើអ្នកផ្តល់ត្រូវការបន្ថែម៖

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ម៉ូដជំនួយដោយភ្នាក់ងារ បច្ចុប្បន្នកំពុងគ្របដណ្តប់លើ Markdown និងកោសិកា Markdown ក្នុងកំណត់ត្រា (notebook). ការបកប្រែរូបភាពនៅតែប្រើបណ្តាញដំណើរការរូបភាពដែលគាំទ្រដោយអ្នកផ្គត់ផ្គង់ និងទាមទារ Azure AI Vision សម្រាប់ OCR និងការរៀបចំតាមរចនាសម្ព័ន្ធ (layout-aware rendering).

## ជំហានទី 2: កំណត់រចនាសម្ព័ន្ធកម្មវិធីអតិថិជន MCP របស់អ្នក

សម្រាប់ការកំណត់ `stdio` ស្តង់ដារផ្ទាល់, បន្ថែម Co-op Translator ទៅក្នុងកំណត់រចនាសម្ព័ន្ធកម្មវិធីអតិថិជន MCP។ អតិថិជននឹងចាប់ផ្ដើម និងផ្អាកដំណើរការនោះដោយស្វ័យប្រវត្តិ។

Installed package configuration:

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

Source checkout configuration on Windows:

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

កំណត់​រចនាសម្ព័ន្ធសម្រាប់ source checkout នៅលើ macOS ឬ Linux:

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

បន្ទាប់ពីផ្លាស់ប្តូរកំណត់រចនាសម្ព័ន្ធកម្មវិធីអតិថិជន MCP សូមចាប់ផ្ដើមឡើងវិញ ឬផ្ទុកឡើងវិញអតិថិជន ដើម្បីឲ្យវាអាចស្វែងរកម៉ាស៊ីនមេថ្មី។

## ជំហានទី 3: បញ្ជាក់ម៉ាស៊ីនមេក្នុងកម្មវិធីអតិថិជន

សូមឲ្យកម្មវិធីអតិថិជន MCP បញ្ជីឧបករណ៍ដែលមាន ឬហៅមួយក្នុងចំណោមឧបករណ៍ជំនួយអានតែបានមុន៖

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ការត្រួតពិនិត្យដំបូងដែលមានប្រយោជន៍៖

| ឧបករណ៍ | ត្រូវពិនិត្យអ្វី |
| --- | --- |
| `get_api_overview` | បញ្ជាក់ថាម៉ាស៊ីនមេអាចទំនាក់ទំនងបាន និងបង្ហាញដំណើរការងារដែលមាន។ |
| `list_supported_languages` | បញ្ជាក់ថាដុំទិន្នន័យភាសាដែលបានរួមបញ្ចូលអាចត្រូវបានផ្ទុក។ |
| `get_configuration_status` | បញ្ជាក់ពីភាពមានស្រាប់នៃអ្នកផ្តល់ LLM និង Vision ដោយមិនបង្ហាញតម្លៃសម្ងាត់។ |

## ជំហានទី 4: ជ្រើសរើសដំណើរការងារ

### បកប្រែឯកសារ ឬឯកសារផ្ទាល់ខ្លួន

ប្រើឧបករណ៍មាតិកាដែលផ្អែកលើអ្នកផ្តល់ នៅពេលដែលកម្មវិធីអតិថិជន MCP មានមាតិកាឯកសារ ឬផ្លូវរូបភាពរួចហើយ ហើយ Co-op Translator គួរតែហៅអ្នកផ្តល់ដែលបានកំណត់។

សម្រាប់ Markdown:

1. ហៅ `translate_markdown_content` ជាមួយ `document`, `language_code`, និងជាជម្រើស `source_path`។
2. ប្រសិនបើលទ្ធផលបានបកប្រែត្រូវបានសរសេរចូលក្នុងលំនាំចេញរបស់ Co-op Translator សូមហៅ `rewrite_markdown_paths`។
3. អោយអតិថិជនសរសេរ ឬបញ្ជូនត្រឡប់ `content` ចុងក្រោយ។

សម្រាប់ notebooks:

1. ហៅ `translate_notebook_content` ជាមួយ JSON នៃ notebook និង `language_code`។
2. ហៅ `rewrite_notebook_paths` ប្រសិនបើតំណនៃ notebook ដែលបានបកប្រែ ត្រូវបានកែសម្រួលសម្រាប់ផ្លូវគោលដៅ។
3. សរសេរ ឬបញ្ជូនត្រឡប់ JSON ចុងក្រោយនៃ notebook។

សម្រាប់រូបភាព:

1. ហៅ `translate_image_content` ជាមួយ `image_path`, `language_code`, និងជាជម្រើស `root_dir` ឬ `fast_mode`។
2. អាន `data_base64` និង `mime_type` ដែលត្រឡប់មក។
3. ប្រសិនបើផ្គត់ផ្គង់ `output_path` រូបភាពដែលបានបកប្រែក៏នឹងត្រូវរក្សាទុកទៅផ្លូវនោះផងដែរ។

ឧបករណ៍មាតិការនេះមិនអនុវត្តការស្វែងរកគម្រោង ការអាប់ដេតមេតាដាតា ការបដិសេធ ឬការសរសេរផ្លូវជាស្វ័យប្រវត្តិ ទេ។ ប្រសិនបើអ្នកចង់ឲ្យភ្នាក់ងារម្ចាស់ផ្ទះបកប្រែគ្រាប់ Markdown ឬ notebook ដោយគ្មានសញ្ញាប័ត្រ provider LLM របស់ Co-op Translator សូមប្រើដំណើរការជំនួយដោយភ្នាក់ងារខាងក្រោម។

### បកប្រែជាមួយម៉ូដែលភ្នាក់ងារម្ចាស់ផ្ទះ

ប្រើឧបករណ៍ជំនួយដោយភ្នាក់ងារ នៅពេលដែលអ្នកចង់ឲ្យភ្នាក់ងារម្ចាស់ MCP ដូចជាជំនួយក្នុងការសរសេរកូដ បង្កើតអត្ថបទដែលបានបកប្រែ ជំនួសការកំណត់អ្នកផ្តល់ LLM សម្រាប់ Co-op Translator។

នៅក្នុងកម្មវិធីអតិថិជន MCP ដែលមានមូលដ្ឋានជាជជែក អ្នកជាទូទៅមិនចាំបាច់សរសេរ JSON ឧបករណ៍ដោយខ្លួនឯងទេ។ សុំឲ្យភ្នាក់ងារ ប្រើដំណើរការជំនួយដោយភ្នាក់ងារ៖

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

សម្រាប់ notebooks ប្រើលំនាំដូចគ្នា៖

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ប្រសិនបើកម្មវិធីអតិថិជន MCP របស់អ្នកគាំទ្រសារ server prompts សូមប្រើ `agent_assisted_markdown_translation_prompt` ដើម្បីឲ្យអតិថិជនផ្ទុកសេចក្តីណែនាំដំណើរការដូចគ្នា។

សម្រាប់ Markdown:

1. ហៅ `start_markdown_agent_translation` ជាមួយ `document`, `language_code`, និងជាជម្រើស `source_path`។
2. បកប្រែគ្រាប់នីមួយៗដែលត្រឡប់មកក្នុងភ្នាក់ងារម្ចាស់ដោយតាម `prompt` របស់គ្រាប់។
3. ហៅ `finish_markdown_agent_translation` ជាមួយ `job` ដើម និងគ្រាប់ដែលបានបកប្រែ ដោយប្រើ `chunk_id` និង `translated_text`។
4. ប្រសិនបើមាតិកានឹងត្រូវបានសរសេរទៅផ្លូវគោលដៅដែលបានបកប្រែ សូមហៅ `rewrite_markdown_paths`។

សម្រាប់ notebooks:

1. ហៅ `start_notebook_agent_translation` ជាមួយ JSON នៃ notebook និង `language_code`។
2. បកប្រែគ្រាប់នីមួយៗដែលត្រឡប់មកក្នុងភ្នាក់ងារម្ចាស់។
3. ហៅ `finish_notebook_agent_translation` ជាមួយ `job` ដើម និងចំណែកដែលបានបកប្រែ។
4. ហៅ `rewrite_notebook_paths` ប្រសិនបើតំណក្នុង notebook ដែលបានបកប្រែ ត្រូវការកែផ្លូវគោលដៅ។

ឧបករណ៍ជំនួយដោយភ្នាក់ងារមិនហៅអ្នកផ្តល់ LLM ដែលបានកំណត់ពី Co-op Translator ទេ។ ភ្នាក់ងារអាហ្វត (host agent) មានសារៈសំខាន់ក្នុងការបកប្រែចំណែកដែលបានត្រឡប់មកវិញ។ Co-op Translator ទទួលខុសត្រូវក្នុងការបែងចែក Markdown ជាចំណែក, រក្សាទុកចំណុចដាក់ជំនួស, ស្ដារឡើងវិញ frontmatter, ជំនួសកោសិកា notebook និងធ្វើឲ្យធម្មតាផ្សេងៗបន្ទាប់ពីបកប្រែ។

### បកប្រែ Repository ទាំងមូល

ប្រើ `run_translation` នៅពេលដែលអ្នកប្រើចង់ឱ្យ Co-op Translator ប្រតិបត្តិដូច CLI `translate`។

ការបកប្រែ Repository មានតម្លៃដើមជា `dry_run=true` ដើម្បីឱ្យភ្នាក់ងារអាចពិនិត្យដែនកំណត់មុនពេលកែប្រែឯកសារ៖

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

លទ្ធផល `run_translation` រួមមានអារេ `events` ដែលមាន
`co-op.translation.event.v1` នៃព្រឹត្តិការណ៍បង្ហាញស្ថានភាព។ អតិថិជន MCP គួរប្រើវាលដូចជា
`type`, `stage_key`, `completed`, `total`, និង `current_path` ជំនួស
ការវិភាគអត្ថបទកុងសុលដែលបានចាប់យក។ ផ្ដល់ `json_events_path` ដើម្បីសរសេរព្រឹត្តិការណ៍ទាំងនោះ
ទៅក្នុងឯកសារ NDJSON។

ដើម្បីអនុញ្ញាតការសរសេរ អ្នកហៅត្រូវកំណត់ទាំង `dry_run=false` និង `confirm_write=true`៖

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ត្រូវបានផ្ដល់ជាឈ្មោះសមភាពសម្រាប់ `run_translation`។

### ពិនិត្យលទ្ធផលដែលបានបកប្រែ

ប្រើ `run_review` សម្រាប់ការត្រួតពិនិត្យដែលមានលទ្ធផលកំណត់ត្រា ហើយមិនទាមទារអត្តសញ្ញាណ LLM ឬ Vision ទេ៖

!!! note "ប៊ីតា"
    MCP បង្ហាញ API `run_review` ជាស៊េរីប៊ីតា។ វាសុវត្ថិសម្រាប់ដំណើរការត្រួតពិនិត្យការអានតែប៉ុណ្ណោះ ប៉ុន្តែការត្រួតពិនិត្យ និងស្គីមបញ្ហាអាចមានការផ្លាស់ប្តូរ។

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

លទ្ធផលរួមមានអត្ថបទដែលបានចាប់យក និងសេចក្តីសង្ខេបការពិនិត្យដែលមានរចនាសម្ព័ន្ធ នៅពេលមាន។

## ការរត់ម៉ាស៊ីនមេដោយដៃ

ការរត់ដោយដៃភាគច្រើនសម្រាប់ដោះស្រាយបញ្ហា ឬសម្រាប់ transports ដែលដំណើរការដូចម៉ាស៊ីនមេរយៈពេលយូរ។

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

រត់ម៉ាស៊ីនមេ HTTP ឬ SSE រយៈពេលយូរ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

សម្រាប់ការរួមបញ្ចូលជាមួយកម្មវិធីកែសម្រួលក្នុងកន្លែង និងភ្នាក់ងារ ជ្រើសប្រើការកំណត់ `stdio` ដែលគ្រប់គ្រងដោយ client ក្នុងជំហានទី 2។

## Tools

| ឧបករណ៍ | គោលបំណង | សរសេរឯកសារ |
| --- | --- | --- |
| `translate_markdown_content` | បកប្រែខ្សែអក្សារ Markdown។ | ទេ |
| `translate_notebook_content` | បកប្រែកោសិកា Markdown ក្នុង JSON នៃ notebook។ | ទេ |
| `translate_image_content` | បកប្រែអត្ថបទក្នុងរូបភាពមួយ និងប្រគល់ទិន្នន័យរូបភាព base64។ | ជាជម្រើស, តែត្រឹមពេលតែម្តងដែលបានផ្ដល់ `output_path` |
| `start_markdown_agent_translation` | រៀបចំចំណែក Markdown សម្រាប់ភ្នាក់ងារ (host agent) ដើម្បីបកប្រែដោយគ្មានអាជ្ញាប័ណ្ណ LLM របស់ Co-op Translator។ | ទេ |
| `finish_markdown_agent_translation` | ស្ដារឡើងវិញ Markdown ពីចំណែកដែលភ្នាក់ងារ (host agent) បានបកប្រែ។ | ទេ |
| `start_notebook_agent_translation` | រៀបចំចំណែកកោសិកា Markdown នៃ notebook សម្រាប់ភ្នាក់ងារ (host agent) បកប្រែ। | ទេ |
| `finish_notebook_agent_translation` | ស្ដារឡើងវិញ JSON នៃ notebook ពីចំណែកដែលភ្នាក់ងារ (host agent) បានបកប្រែ។ | ទេ |
| `rewrite_markdown_paths` | ប្តូរវិញផ្លូវនៅក្នុងខ្លឹមសាររ៉េ Markdown និង frontmatter សម្រាប់គោលដៅដែលបានបកប្រែ។ | ទេ |
| `rewrite_notebook_paths` | ប្តូរវិញផ្លូវនៅក្នុងកោសិកា Markdown របស់ notebook។ | ទេ |
| `run_translation` | ដំណើរការបកប្រែកម្រិតគម្រោង ដូច CLI។ | បាទ បើ `dry_run=false` និង `confirm_write=true` |
| `translate_project` | ឈ្មោះសមភាពសម្រាប់ `run_translation`។ | បាទ បើ `dry_run=false` និង `confirm_write=true` |
| `run_review` | អនុវត្តត្រួតពិនិត្យដែលកំណត់លទ្ធផល។ | ទេ |
| `get_configuration_status` | រាយការណ៍អ្នកផ្តល់ LLM និង Vision ដែលបានកំណត់ ដោយមិនបង្ហាញអំពីសម្ងាត់។ | ទេ |
| `list_supported_languages` | បង្ហាញបញ្ជីកូដភាសាគោលដៅដែលគាំទ្រ។ | ទេ |
| `get_api_overview` | ពណ៌នា workflows និងឧបករណ៍ MCP ដែលមានស្រាប់។ | ទេ |

## Resources

| Resource URI | គោលបំណង |
| --- | --- |
| `co-op://api` | ទិដ្ឋភាពទូទៅ JSON នៃ workflows និងឧបករណ៍។ |
| `co-op://supported-languages` | បញ្ជី JSON នៃកូដភាសាដែលគាំទ្រ។ |
| `co-op://configuration` | សេចក្តីសង្ខេប JSON នៃភាពអាចប្រើបានរបស់អ្នកផ្តល់ដោយមិនបង្ហាញសម្ងាត់។ |

## Prompts

| Prompt | គោលបំណង |
| --- | --- |
| `translate_markdown_document_prompt` | ជួយណែនាំអតិថិជន MCP តាមដានការបកប្រែខ្លឹមសារ និងជម្រើសកែផ្លូវ។ |
| `agent_assisted_markdown_translation_prompt` | ជួយណែនាំអតិថិជន MCP តាមដានការបកប្រែ Markdown ដោយភ្នាក់ងារ (host agent) ដោយគ្មានអាជ្ញាប័ណ្ណ LLM នៃ Co-op Translator។ |
| `translate_repository_prompt` | ផ្ដល់ការណែនាំដល់អតិថិជន MCP សម្រាប់ការបកប្រែ Repository ដែលចាប់ផ្តើមដោយ dry-run ជាមុន។ |

## ឧទាហរណ៍សម្រាប់ចម្លង និង ភ្ជាប់

បកប្រែខ្លឹមសារ Markdown:

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

ប្តូរតំណ Markdown ដែលបានបកប្រែ:

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

បកប្រែ Markdown ជាមួយម៉ូឌែលភ្នាក់ងារ (host agent):

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

បន្ទាប់ពីភ្នាក់ងារ (host agent) បកប្រែចំណែកនីមួយៗដែលបានត្រឡប់មកវិញ សូមបញ្ចប់ការងារ ដោយប្រើអង្គភាព `job` ពេញលេញ ដែលបានត្រឡប់ពី `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

មើលមុននូវការបកប្រែ Repository:

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

## Troubleshooting

| បញ្ហា | តើត្រូវព្យាយាមអ្វី |
| --- | --- |
| អតិថិជន MCP មិនអាចរកឃើញ `co-op-translator-mcp` ទេ។ | ប្រើផ្លូវ Python អនុវត្តដោយពេញលេញ និងកំណត់ source checkout `["-m", "co_op_translator.mcp.server"]`។ |
| ម៉ាស៊ីនមេត្រូវបានបញ្ជីប៉ុន្តែការបកប្រែបរាជ័យ។ | ហៅ `get_configuration_status` និងបញ្ជាក់ថាអ្នកផ្តល់ LLM មានស្រាប់។ |
| អ្នកចង់បកប្រែ Markdown ឬ notebook ដោយគ្មានអាជ្ញាប័ណ្ណអ្នកផ្តល់។ | ប្រើ `start_markdown_agent_translation` / `finish_markdown_agent_translation` ឬសមរាប់សម្រាប់ notebook ដូច្នេះភ្នាក់ងារ (host agent) នឹងបកប្រែចំណែក។ |
| ការបកប្រែរូបភាពបរាជ័យ។ | ប្រាកដថាតម្លៃអថេរ Azure AI Vision ត្រូវបានកំណត់ ហើយហៅ `get_configuration_status`។ |
| ការបកប្រែ Repository មិនសរសេរឯកសារ។ | កំណត់ `dry_run=false` និង `confirm_write=true` តែបន្ទាប់ពីបានទទួលការយល់ព្រមពីអ្នកប្រើយ៉ាងច្បាស់។ |
| ការផ្លាស់ប្តូរនៅក្នុងការកំណត់ client មិនបង្ហាញ។ | ចាប់ផ្តើមឡើងវិញ ឬផ្ទុកឡើងវិញអតិថិជន MCP។ |

## កំណត់ចំណាំសុវត្ថិភាព

- ការហៅឧបករណ៍ MCP ត្រូវបានគ្រប់គ្រងដោយម៉ូឌែលនៃកម្មវិធីម៉ាស៊ីម (host application), ដូច្នេះការបកប្រែ Repository គឺជា dry-run លំនាំដើម។
- ការបកប្រែ Repository ពេញលេញអាចបង្កើត, កែប្រែ, ឬលុបឯកសារច្រើន។ ត្រូវទាមទារការយល់ព្រមយ៉ាងច្បាស់ពីអ្នកប្រើ មុនពេលកំណត់ `confirm_write=true`។
- ឧបករណ៍ស្ថានភាពកំណត់មិនដែលត្រឡប់កូនសោ API, endpoints, ឬតម្លៃសម្ងាត់ផ្សេងៗ។
- ការបកប្រែរូបភាពបញ្ជូនទិន្នន័យរូបភាពជា base64។ រូបភាពធំៗអាចបង្កើតចម្លើយឧបករណ៍ដែលមានទំហំធំ។
- ឧបករណ៍ជំនួយដោយភ្នាក់ងារត្រឡប់ចំណែកប្រភព និង prompts ទៅកាន់ម៉ាស៊ីនផ្ដល់ MCP (host)。 ជ្រើសប្រើពួកវាប៉ុណ្ណោះសម្រាប់ខ្លីមសារ​ដែលអ្នកប្រើមានក្ដីពេញចិត្តក្នុងការផ្ញើទៅម៉ូឌែលភ្នាក់ងារ host នោះ។