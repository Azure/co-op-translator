# ឯកសារយោង CLI

Co-op Translator តម្លើងចំណុចចូលតាមបញ្ជាទាំងនេះ:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

ពាក្យបញ្ជា `translate`, `evaluate`, `migrate-links`, និង `co-op-review` ត្រូវបានផ្ញើតាម `co_op_translator.__main__` ដែលជ្រើសរើសការអនុវត្តន៍ពាក្យបញ្ជាដោយផ្អែកលើឈ្មោះស្គ្រីបដែលបានហៅ។ MCP server ប្រើ `co_op_translator.mcp.server` ដោយផ្ទាល់។

ប្រសិនបើអ្នកកំពុងជ្រើសរវាង CLI, Python API, និង MCP ចាប់ផ្តើមជាមួយ [ជ្រើសរើសលំហូរការងារ](workflows.md)។

## លទ្ធផលក្នុង​កុងសូល

ត_terminal អន្តរកម្ម​នឹងប្រើទ្រង់ទ្រាយ Rich សម្រាប់ក្បាលពាក្យបញ្ជា ការបង្ហាញដំណើរការ និងសង្ខេប។ សម្រាប់ CI និងលទ្ធផលមិនអន្តរកម្ម វានឹងធ្លាក់ត្រឡប់ទៅជាអក្សរសាមញ្ញដោយស្វ័យប្រវត្តិ។

កំណត់ `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` ដើម្បីបង្ខំជាលទ្ធផលសាមញ្ញ ឬ `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` ដើម្បីបង្ខំប្រើ Rich។ កំណត់ `CO_OP_TRANSLATOR_NO_PROGRESS=1` ដើម្បីរក្សាសង្ខេប ខណៈដែលបិទបាំងរបារបង្ហាញដំណើរការផ្ទាល់។

ប្រើ `translate --json-events progress.ndjson` នៅពេលប្រព័ន្ធផ្សេងទៀតត្រូវការព័ត៌មានដំណើរការដែលអានបានដោយម៉ាស៊ីន។ CLI នឹងបន្តបង្ហាញលទ្ធផលសម្រាប់មនុស្ស ខណៈដែលឯកសារ NDJSON នឹងទទួលព្រឹត្តិការណ៍ចម្លងជាបណ្ដើរ `co-op.translation.event.v1` ដែលមានវាលដែលបានស្ថេរដូចជា `type`, `stage_key`, `completed`, `total`, និង `current_path`។





## លំហូរដំបូងសម្រាប់ CLI

ចាប់ផ្តើមនៅទីនេះ ប្រសិនបើអ្នកកំពុងប្រើ Co-op Translator ពី terminal:

1. กำหนดអ្នកផ្គត់ផ្គង់ LLM ដូចបានពិពណ៌នានៅ [ការកំណត់](configuration.md)។
2. ជ្រើសប្រភេទមាតិកាដែលអ្នកចង់បកប្រែ។
3. ដំណើរការបញ្ជាផ្តោតមុន ដូចជា បកប្រែ Markdown តែប៉ុណ្ណោះ។
4. ប្រើ `--dry-run` មុនការផ្លាស់ប្តូរធំៗក្នុង repository។
5. ប្រើ `co-op-review` បន្ទាប់ពីការបកប្រែ ដើម្បីពិនិត្យរចនាសម្ព័ន្ធ និងភាពទាន់សម័យ។

| គោលដៅ | ពាក្យបញ្ជាដើម្បីចាប់ផ្តើម |
| --- | --- |
| បកប្រែឯកសារ Markdown | `translate -l "ko" -md` |
| បកប្រែ notebooks | `translate -l "ko" -nb` |
| បកប្រែអត្ថបទក្នុងរូបភាព | `translate -l "ko" -img` |
| មើលមុនដោយមិនសរសេរឯកសារ | `translate -l "ko" -md --dry-run` |
| ពិនិត្យការបកប្រែដែលមាន | `co-op-review -l "ko"` |
| ធ្វើបច្ចុប្បន្នភាពតំណភ្ជាប់ notebook និង Markdown | `migrate-links -l "ko" --dry-run` |
| បើកមុខងារទៅកាន់អតិថិជន MCP | កំណត់ [MCP Server](mcp.md) ជំនួសការរត់ពាក្យបញ្ជា CLI ដោយផ្ទាល់។ |

## translate

បកប្រែឯកសារ Markdown, notebooks, និងអត្ថបទក្នុងរូបភាព ទៅជាភាសាគោលដៅមួយឬច្រើន។

```bash
translate -l "ko ja fr"
```

### ឧទាហរណ៍ទូទៅ

បកប្រែ Markdown តែប៉ុណ្ណោះ:

```bash
translate -l "de" -md
```

បកប្រែ notebooks តែប៉ុណ្ណោះ:

```bash
translate -l "zh-CN" -nb
```

បកប្រែ Markdown និងរូបភាព:

```bash
translate -l "pt-BR" -md -img
```

ធ្វើបច្ចុប្បន្នភាពការបកប្រែដែលមាន ដោយលុបចោលហើយបង្កើតឡើងវិញ:

```bash
translate -l "ko" -u
```

ដំណើរការដោយគ្មានការស្នើសុំអន្តរកម្ម:

```bash
translate -l "ko ja" -md -y
```

រក្សាកំណត់ហេតុ:

```bash
translate -l "ko" -s
```

សរសេព្រឹត្តិការណ៍ដំណើរការដែលបានរៀបចំ:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### ជម្រើស

| ជម្រើស | ត្រូវការ | ពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | កូដភាសាដាក់បំបែក​ដោយចន្លោះ, ឧទាហរណ៍ `"es fr de"`, ឬ `"all"`. |
| `-r`, `--root-dir` | No | ឫសគម្រោង។ ដើមមានតម្លៃជាថតបច្ចុប្បន្ន។ |
| `-u`, `--update` | No | លុបការបកប្រែដែលមានសម្រាប់ភាសាត្រូវបានជ្រើស និងបង្កើតឡើងវិញ។ |
| `-img`, `--images` | No | បកប្រែឯកសាររូបភាពតែប៉ុណ្ណោះ។ |
| `-md`, `--markdown` | No | បកប្រែឯកសារ Markdown តែប៉ុណ្ណោះ។ |
| `-nb`, `--notebook` | No | បកប្រែកំណត់ត្រា Jupyter (notebook) តែប៉ុណ្ណោះ។ |
| `-d`, `--debug` | No | បើកកំណត់ហេតុ debug នៅក្នុង console។ |
| `-s`, `--save-logs` | No | រក្សាកំណត់ហេតុនៅកម្រិត DEBUG ទៅក្នុង `<root-dir>/logs/`។ |
| `--json-events` | No | សរសេព្រឹត្តិការណ៍ដំណើរការបកប្រែដែលអាចអានបានដោយម៉ាស៊ីនជារាង NDJSON។ |
| `-x`, `--fix` | No | បកប្រែឡើងវិញឯកសារ Markdown ដែលមានទំនុកចិត្តទាប ដោយផ្អែកលើលទ្ធផលវាយតម្លៃមុន។ |
| `-c`, `--min-confidence` | No | គ្រោងទំនុកចិត្តសម្រាប់ `--fix`។ ដើមមានតម្លៃជា `0.7`។ |
| `--add-disclaimer`, `--no-disclaimer` | No | បន្ថែម ឬ បដិសេធ ពាក្យពន្យល់ពីការបកប្រែដោយម៉ាស៊ីន។ តម្លៃលំនាំដើមនៅ CLI គឺបើក។ |
| `-f`, `--fast` | No | ម៉ូដរហ័សសម្រាប់រូបភាព ដែលបានព្រហ្មទោស (deprecated)។ |
| `-y`, `--yes` | No | បញ្ជាក់ដោយស្វ័យប្រវត្តិ សមរម្យសម្រាប់ CI។ |
| `--repo-url` | No | URL របស់ repository ដែលប្រើនៅក្នុង README languages table sparse-checkout advisory។ |
| `--migrate-language-folders` | No | ផ្លាស់ប្តូរឈ្មោះថត alias ចាស់ៗ ដូចជា `cn` ឬ `tw` ទៅឈ្មោះថត BCP 47 ដែលត្រឹមត្រូវ។ |
| `--dry-run` | No | មើលជាមុនការផ្លាស់ប្តូរថតភាសា និងការប៉ាន់ស្មានការបកប្រែ ដោយមិនបានសរសេរ​ឯកសារ។ |

ប្រសិនបើមិនមានផ្លាហ្គោប្រភេទ (`type flag`) ផ្ដល់ `translate` នឹងដំណើរការពាក្យបញ្ជារ Markdown, notebooks, និងរូបភាព។ ការបកប្រែរូបភាពត្រូវការ ការកំណត់ Azure AI Vision។

## evaluate

វាយតម្លៃគុណភាពនៃការបកប្រែ Markdown សម្រាប់ភាសាមួយ។

!!! warning "កំពុងសាកល្បង"
    `evaluate` គឺកំពុងសាកល្បង។ វាអាចប្រើការត្រួតពិនិត្យគុណភាពដែលផ្អែកលើច្បាប់ និងលើ LLM, សរសេរវិលលទ្ធផលការវាយតម្លៃចូលទៅក្នុងមេតាដាតាការបកប្រែ, ហើយម៉ូឌែលពិន្ទុ និងអាកប្បកិរិយារបស់មេតាដាតា អាចផ្លាស់ប្តូរ។

```bash
evaluate -l "ko"
```

### ឧទាហរណ៍ទូទៅ

ប្រើសន្ទស្សន៍ទំនុកចិត្តទាបដែលតឹងរឹងជាងមុន:

```bash
evaluate -l "es" -c 0.8
```

រត់តែការត្រួតពិនិត្យដោយច្បាប់ (rule-based) តែម្តង:

```bash
evaluate -l "fr" -f
```

រត់តែការត្រួតពិនិត្យដោយ LLM តែម្តង:

```bash
evaluate -l "ja" -D
```

### ជម្រើស

| ជម្រើស | ត្រូវការ | ពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | កូដភាសាពីតែមួយសម្រាប់វាយតម្លៃ។ កូដឈ្មោះដាក់ជាជំនួសនឹងត្រូវបានធ្វើឲ្យមានទ្រង់ទ្រាយស្តង់ដារ។ |
| `-r`, `--root-dir` | No | ឫសគម្រោង។ ដើមមានតម្លៃជា​ថត​បច្ចុប្បន្ន។ |
| `-c`, `--min-confidence` | No | គ្រោងដែលប្រើពេលបង្ហាញបកប្រែដែលមានទំនុកចិត្តទាប។ ដើមមានតម្លៃជា `0.7`។ |
| `-d`, `--debug` | No | បើកកំណត់ហេតុខាង debug។ |
| `-s`, `--save-logs` | No | រក្សាកំណត់ហេតុនៅកម្រិត DEBUG ទៅក្នុង `<root-dir>/logs/`។ |
| `-f`, `--fast` | No | វាយតម្លៃត្រឹមតែដោយច្បាប់ (rule-based) ។ |
| `-D`, `--deep` | No | វាយតម្លៃត្រឹមតែដោយ LLM ។ |

ដើមម៉ឺន `evaluate` ប្រើទាំងវីធីវាយតម្លៃដោយច្បាប់ និងដោយ LLM។ លទ្ធផលត្រូវបានសន្សំពីក្នុង metadata នៃកាពកប្រែ និងសង្ខេបក្នុងកុងសូល។

## co-op-review

រត់ការត្រួតពិនិត្យថែទាំការបកប្រែមានលទ្ធភាពកំណត់ ដោយមិនត្រូវការសញ្ញាប័ត្រ API។

!!! note "បេតា"
    `co-op-review` គឺជាបញ្ជាពិនិត្យក្នុងស្ថានភាពបេតា ដែលមានលទ្ធផលកំណត់។ វាមិនហៅអ្នកផ្តល់ម៉ូឌែល ឬសរសេរឯកសារ ទេ ប៉ុន្តែការត្រួតពិនិត្យរបស់វា និងស្កីម៉ាសម្រាប់លទ្ធផលបញ្ហា អាចអភិវឌ្ឍបាន។

```bash
co-op-review -l "ko"
```

### ឧទាហរណ៍ទូទៅ

ពិនិត្យការបកប្រែភាសាកូរ៉េ និងជប៉ុន ពីថតបច្ចុប្បន្ន:

```bash
co-op-review -l "ko ja"
```

ពិនិត្យឫសគម្រោងជាក់លាក់:

```bash
co-op-review -l "fr" -r ./my-course
```

ពិនិត្យតែ README បន្ទាប់ពីការបកប្រែ README ប៉ុណ្ណោះ:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` មិនយកឯកសារផ្សេងៗ និង README តំណរតំណែមខាងក្នុង។ វាខូចបរាជ័យ ប្រសិនបើឯកសារ `README.md` នៅឫសមិនមាន។ ជាមួយនឹង `--changed-from` វាពិនិត្យតែ README ទៅតាមករណីដែលឯកសារ​ដើមនោះបានផ្លាស់ប្តូរ។ ការបកប្រែ README តែប៉ុណ្ណោះ នឹងប៉ាមួយឯកសារ README ដើមមិនផ្លាស់ប្តូរ រួមទាំងសញ្ញាផ្នែកចែករំលែកណាមួយ។




ពិនិត្យតែឯកសារដើមដែលបានផ្លាស់ប្តូរទៅប្រឆាំងនឹងយោងមូលដ្ឋាន:

```bash
co-op-review -l "ko" --changed-from origin/main
```

បោះពុម្ពលទ្ធផល Markdown រចនាបទ GitHub សម្រាប់សង្ខេប CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### ជម្រើស

| ជម្រើស | ត្រូវការ | ពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-code` | No | កូដភាសាដើម្បីពិនិត្យ។ អាចផ្ដល់ច្រើនដង ឬជាតម្លៃដាច់ដោយចន្លោះ។ ដើមមានតម្លៃជា រាប់ទាំងភាសាបកប្រែទាំងអស់ដែលត្រូវបានរកឃើញ។ |
| `-r`, `--root-dir` | No | ឫសគម្រោង។ ដើមមានតម្លៃជា​ថត​បច្ចុប្បន្ន។ |
| `--changed-from` | No | Git ref ដែលប្រើដើម្បីកំណត់ការពិនិត្យទៅតែឯកសារដើមដែលបានផ្លាស់ប្តូរ។ |
| `--readme-only` | No | ពិនិត្យតែការបកប្រែ `README.md` នៅឫសប៉ុណ្ណោះ។ |
| `--format` | No | ទ្រង់ទ្រាយលទ្ធផល៖ `text` ឬ `github`។ ដើមមានតម្លៃជា `text`។ |

`co-op-review` ត្រួតពិនិត្យឥឡូវនេះ សម្រាប់ឯកសារបកប្រែដែលខ្វះ metadata បកប្រែដែលខ្វះឬចាស់ៗ, ភាពសាធារណៈ (frontmatter) និងភាពត្រឹមត្រូវនៃកូដក្បាល, JSON នៃ notebook បកប្រែដែលមិនត្រឹមត្រូវ, និងគោលដៅតំណភ្ជាប់ Markdown ឬ រូបភាពក្នុងស្រុកដែលខ្វះ។ តំណភ្ជាប់ដែលខ្វះគឺជាការព្រមានដោយលំនាំដើម; បញ្ហាផ្នែករចនាសម្ព័ន្ធ និងភាពទាន់សម័យនឹងធ្វើឲ្យពាក្យបញ្ជាខូចបរាជ័យ។

## co-op-translator-mcp

រត់ម៉ាស៊ីនមេ Co-op Translator MCP សម្រាប់ agents, editors និងអតិថិជនដែលឆាប់បាន MCP-compatible។

```bash
co-op-translator-mcp
```

ឡានដឹកជញ្ជូនលំនាំដើមគឺ `stdio`។ មើលគណៈកម្មាធិការណ៍ [MCP Server](mcp.md) សម្រាប់ការកំណត់អតិថិជន ការឧបករណ៍ សัพតាភាព និងកំណត់សុវត្ថិភាព។

### ជម្រើស

| ជម្រើស | ត្រូវការ | ពណ៌នា |
| --- | --- | --- |
| `--transport` | No | ការដឹកជញ្ជូន MCP៖ `stdio`, `streamable-http`, ឬ `sse`។ ដើមមានតម្លៃជា `stdio`។ |

## migrate-links

ពង្រីកឯកសារ Markdown ដែលបានបកប្រែឡើងវិញ និងធ្វើបច្ចុប្បន្នភាពតំណភ្ជាប់ notebook ដើម្បីឲ្យពួកវាសម្ងាត់ទៅកាន់ notebook បកប្រេប្រសិនមាន។

```bash
migrate-links -l "ko ja"
```

### ឧទាហរណ៍ទូទៅ

មើលមុនការអាប់ដេតតំណភ្ជាប់:

```bash
migrate-links -l "ko" --dry-run
```

ដំណើរការជា​ភាសាទាំងអស់ដែលគាំទ្រ ដោយគ្មានការបញ្ជាក់:

```bash
migrate-links -l "all" -y
```

កែសម្រួលតំណភ្ជាប់តែពេលមាន notebook បកប្រែស្រាប់ប៉ុណ្ណោះ:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### ជម្រើស

| ជម្រើស | ត្រូវការ | ពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | កូដភាសាដាក់បំបែកដោយចន្លោះ ឬ `"all"`។ |
| `-r`, `--root-dir` | No | ឫសគម្រោង។ ដើមមានតម្លៃជា​ថត​បច្ចុប្បន្ន។ |
| `--image-dir` | No | ថតរូបភាពដែលបានបកប្រែនេះទ относительно លើឫស។ ដើមមានតម្លៃជា `translated_images`។ |
| `--dry-run` | No | បង្ហាញឯកសារដែលនឹងផ្លាស់ប្តូរដោយមិនសរសេរកំណែចេញ។ |
| `--fallback-to-original`, `--no-fallback-to-original` | No | ប្រើតំណ notebook ដើមនៅពេល notebook បកប្រែអវត្តមាន។ បើកដោយលំនាំដើម។ |
| `-d`, `--debug` | No | បើកកំណត់ហេតុ debug។ |
| `-s`, `--save-logs` | No | រក្សាកំណត់ហេតុនៅកម្រិត DEBUG ទៅក្នុង `<root-dir>/logs/`។ |
| `-y`, `--yes` | No | បញ្ជាក់ដោយស្វ័យប្រវត្តិពេលដំណើរការភាសាទាំងអស់។ |

## Environment

នៅពេលពាក្យបញ្ជាតម្រូវឲ្យមានសក្ដានុពលផ្តល់សេវាកម្ម ជ្រើសរើសកំណត់មួយចំនួនពីកុងហ្វីកនេះ។ `translate --dry-run` និង `co-op-review` មិនត្រូវការសក្ដានុពលផ្តល់សេវាកម្ម។

```bash
# អាស៊ែរ OpenAI
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

ការបកប្រែរូបភាព ត្រូវការបន្ថែម Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## រចនាសម្បទាលទ្ធផល

ការបកប្រែអក្សរត្រូវបានសរសេរទុកនៅក្រោម៖

```text
translations/<language-code>/<original-path>
```

លទ្ធផលរូបភាពដែលបានបកប្រែ ត្រូវបានសរសេរទុកនៅក្រោម៖

```text
translated_images/<language-code>/<original-path>
```

ឧទាហរណ៍ បកប្រែ `README.md` និង `docs/setup.md` ទៅជាស اللغة Korean នឹងបង្កើត៖

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## ឧទាហរណ៍ CLI សម្រាប់ចម្លង និងដាក់

បកប្រែ Markdown ទៅជាភាសាបី:

```bash
translate -l "ko ja fr" -md
```

បកប្រែ notebooks តែប៉ុណ្ណោះ:

```bash
translate -l "zh-CN" -nb
```

បកប្រែរូបភាពតែប៉ុណ្ណោះ:

```bash
translate -l "pt-BR" -img
```

មើលមុនការបកប្រែ Markdown ដោយមិនសរសេរឯកសារ:

```bash
translate -l "de es" -md --dry-run
```

ជួសជុលការបកប្រែ Markdown ដែលមានទំនុកចិត្តទាប:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

ដំណើរការបកប្រែ Markdown ដែលសមរម្យសម្រាប់ CI:

```bash
translate -l "ko ja" -md -y -s
```

ពិនិត្យលទ្ធផលដែលបានបកប្រែ:

```bash
co-op-review -l "ko ja"
```

មើលមុនការផ្លាស់ទីតំណភ្ជាប់:

```bash
migrate-links -l "ko" --dry-run
```