# CLI តំណរឯកសារ

Co-op Translator តстанавлиș នូវចំណុចចុះចូលបញ្ចូលតាមបន្ទាត់បញ្ជានេះ:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

ពាក្យបញ្ជា `translate`, `evaluate`, `migrate-links`, និង `co-op-review` ត្រូវបានដឹកនាំតាម `co_op_translator.__main__` ដែលជ្រើសរើសការអនុវត្តន៍ពាក្យបញ្ជាតាមឈ្មោះស្គ្រីបដែលបានហៅ។ ម៉ាស៊ីនមេ MCP ប្រើ `co_op_translator.mcp.server` ដោយផ្ទាល់។

បើអ្នកកំពុងសម្រេចចិត្តរវាង CLI, Python API, និង MCP សូមចាប់ផ្តើមនៅ [Choose Your Workflow](workflows.md)។

## ដំណើរការ CLI លើកដំបូង

ចាប់ផ្តើមនៅទីនេះ ប្រសិនបើអ្នកកំពុងប្រើ Co-op Translator ពី terminal:

1. កំណត់អ្នកផ្គត់ផ្គង់ LLM ដូចបានពិពណ៌នា​នៅ [Configuration](configuration.md)។
2. ជ្រើសប្រភេទមាតិកាដែលអ្នកចង់បកប្រែ។
3. ប្រតិបត្តិពាក្យបញ្ជាជាក់លាក់ជាមុន ដូចជា ការបកប្រែ Markdown ប៉ុណ្ណោះ។
4. ប្រើ `--dry-run` មុនការប្រែប្រួលRepository លំនឹងច្រើន។
5. ប្រើ `co-op-review` បន្ទាប់ពីការបកប្រែ ដើម្បីពិនិត្យរចនាសម្ព័ន្ធ និងភាពទាន់សម័យ។

| គោលដៅ | ពាក្យបញ្ជាដើម្បីចាប់ផ្តើម |
| --- | --- |
| បកប្រែឯកសារ Markdown | `translate -l "ko" -md` |
| បកប្រែសៀវភៅកំណត់ត្រា (notebooks) | `translate -l "ko" -nb` |
| បកប្រែអត្ថបទរូបភាព | `translate -l "ko" -img` |
| មើលជាមុនដោយមិនសរសេរឯកសារ | `translate -l "ko" -md --dry-run` |
| ពិនិត្យបកប្រែដែលមានស្រាប់ | `co-op-review -l "ko"` |
| ធ្វើបច្ចុប្បន្នភាពតំណភ្ជាប់ notebook និង Markdown | `migrate-links -l "ko" --dry-run` |
| បង្ហាញឧបករណ៍ទៅឱ្យគ klient MCP | កំណត់តម្លៃ [MCP Server](mcp.md) ជំនួសការរត់ពាក្យបញ្ជា CLI ដោយផ្ទាល់។ |

## translate

បកប្រែឯកសារ Markdown, សៀវភៅកំណត់ត្រា (notebooks), និងអត្ថបទរូបភាពទៅជาทាសាគោលដែលចង់បានមួយឬច្រើន។

```bash
translate -l "ko ja fr"
```

### ឧទាហរណ៍ទូទៅ

បកប្រែ Markdown តែប៉ុណ្ណោះ:

```bash
translate -l "de" -md
```

បកប្រែសៀវភៅកំណត់ត្រាតែប៉ុណ្ណោះ:

```bash
translate -l "zh-CN" -nb
```

បកប្រែ Markdown និងរូបភាព:

```bash
translate -l "pt-BR" -md -img
```

ធ្វើបច្ចុប្បន្នភាពការបកប្រែដែលមានស្រាប់ដោយលុបហើយបង្កើតឡើងវិញ:

```bash
translate -l "ko" -u
```

រត់ដោយមិនមានបញ្ហាសំណួរបញ្ចេញអ្នកប្រើ:

```bash
translate -l "ko ja" -md -y
```

រក្សាទុកកំណត់ហេតុ:

```bash
translate -l "ko" -s
```

### ជម្រើស

| ជម្រើស | ត្រូវការឫទេ | ការពិពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-codes` | បាទ/ចាស | កូដភាសាដាក់ចន្លោះដោយចន្លោះ ព្រមទាំង `"es fr de"` ឬ `"all"`។ |
| `-r`, `--root-dir` | ទេ | រុំឫតគម្រោង។ លំនាំដើមទៅថា ថតបច្ចុប្បន្ន។ |
| `-u`, `--update` | ទេ | លុបការបកប្រែនៅមានស្រាប់សម្រាប់ភាសាជ្រើសរើស ហើយបង្កើតឡើងវិញ។ |
| `-img`, `--images` | ទេ | បកប្រែឯកសាររូបភាពតែប៉ុណ្ណោះ។ |
| `-md`, `--markdown` | ទេ | បកប្រែឯកសារ Markdown តែប៉ុណ្ណោះ។ |
| `-nb`, `--notebook` | ទេ | បកប្រែឯកសារ Jupyter notebook តែប៉ុណ្ណោះ។ |
| `-d`, `--debug` | ទេ | បើកកំណត់ហេតុខុសត្រូវ debug នៅក្នុង console។ |
| `-s`, `--save-logs` | ទេ | រក្សាកំណត់ហេតុខុសត្រូវ DEBUG នៅក្នុង `<root-dir>/logs/`។ |
| `-x`, `--fix` | ទេ | បកប្រែឡើងវិញឯកសារ Markdown ដែលទទួលការវាយតម្លៃទំនុកចិត្តទាប dựa trên លទ្ធផលវាយតម្លៃមុន។ |
| `-c`, `--min-confidence` | ទេ | សម្ព័ន្ធទំនុកចិត្តសម្រាប់ `--fix`។ លំនាំដើមជា `0.7`។ |
| `--add-disclaimer`, `--no-disclaimer` | ទេ | បន្ថែមឬលុបការជូនដំណឹងអំពីការបកប្រែដោយម៉ាស៊ីន។ លំនាំដើមបើកក្នុង CLI។ |
| `-f`, `--fast` | ទេ | ម៉ូដរហ័សសម្រាប់រូបភាព ដែលបានច្រានចោល។ |
| `-y`, `--yes` | ទេ | បញ្ជាក់ដោយស្វ័យប្រវត្តិ សមស្របសម្រាប់ CI។ |
| `--repo-url` | ទេ | URL របស់repository ដែលប្រើនៅក្នុងការបំភ្លឺស្ពាស "README languages table" sparse-checkout។ |
| `--migrate-language-folders` | ទេ | ឈ្មោះថតរបស់អាលីយ៉ាស់ចាស់ៗ ដូចជា `cn` ឬ `tw` ទៅឈ្មោះត្រិះ BCP 47 ធម្មតា។ |
| `--dry-run` | ទេ | មើលមុនការផ្លាស់ប្តូរថតភាសា និងការប៉ាន់ស្មានការបកប្រែដោយមិនសរសេរឯកសារ។ |

បើមិនមានបន្ទាត់ប្រភេទ (type flag) ត្រូវបានផ្តល់ `translate` នឹងដំណើរការ Markdown, សៀវភៅកំណត់ត្រា និងរូបភាព។ ការបកប្រែរូបភាពត្រូវការកំណត់ Azure AI Vision។ 

## evaluate

វាយតម្លៃគុណភាពការបកប្រែ Markdown សម្រាប់ភាសាមួយ។

!!! warning "បឋមភាព"
    `evaluate` គឺ experimental។ វាអាចប្រើការត្រួតពិនិត្យដោយច្បាប់ និងដោយ LLM, សរសេរលទ្ធផលវាយតម្លៃចូលទៅក្នុងមេតាដាតាអំពីការបកប្រែ, ហើយម៉ូដែលស្កូរនិងសេចក្តីអនុវត្តមេតាដាតាអាចផ្លាស់ប្តូរ។ 

```bash
evaluate -l "ko"
```

### ឧទាហរណ៍ទូទៅ

ប្រើកម្រិតទាបទំនុកចិត្តទាន់តឹងជាងមុន:

```bash
evaluate -l "es" -c 0.8
```

រត់តែការត្រួតពិនិត្យដោយច្បាប់តែប៉ុណ្ណោះ:

```bash
evaluate -l "fr" -f
```

រត់តែការត្រួតពិនិត្យដោយ LLM តែប៉ុណ្ណោះ:

```bash
evaluate -l "ja" -D
```

### ជម្រើស

| ជម្រើស | ត្រូវការឫទេ | ការពិពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-code` | បាទ/ចាស | កូដភាសាចម្បងសម្រាប់វាយតម្លៃ។ កូដអាលីយ៉ាស់ត្រូវបានធ្វើឲ្យស្ដង់ដារ។ |
| `-r`, `--root-dir` | ទេ | រុំឫតគម្រោង។ លំនាំដើមទៅថា ថតបច្ចុប្បន្ន។ |
| `-c`, `--min-confidence` | ទេ | គោលកំណត់ដែលប្រើពេលបញ្ជីការបកប្រែទំនុកចិត្តទាប។ លំនាំដើមជា `0.7`។ |
| `-d`, `--debug` | ទេ | បើកកំណត់ហេតុខុសត្រូវ debug។ |
| `-s`, `--save-logs` | ទេ | រក្សាកំណត់ហេតុខុសត្រូវ DEBUG នៅក្នុង `<root-dir>/logs/`។ |
| `-f`, `--fast` | ទេ | តែការវាយតម្លៃដោយច្បាប់។ |
| `-D`, `--deep` | ទេ | តែការវាយតម្លៃដោយ LLM។ |

លំនាំដើម `evaluate` ប្រើទាំងការវាយតម្លៃដោយច្បាប់ និងដោយ LLM។ លទ្ធផលត្រូវបានសរសេរចូលក្នុងមេតាដាតាអំពីការបកប្រែ និងសង្ខេបនៅក្នុង console។

## co-op-review

រត់ការត្រួតពិនិត្យថែទាំការបកប្រែដោយមិនទាមទារអាជ្ញាប័ណ្ណ API។

!!! note "បីតា"
    `co-op-review` គឺជាពាក្យបញ្ជាពិសេសវែប៉ា (beta) សម្រាប់ការពិនិត្យអចិន្ត្រៃយ៍។ វាមិនហៅអ្នកផ្គត់ផ្គង់ម៉ូឌែល ឬសរសេរឯកសារ ទេ ប៉ុន្តែនីតិវិធីត្រួតពិនិត្យ និងស្កេមាផលិតកម្មបញ្ហាអាចផ្លាស់ប្តូរ។

```bash
co-op-review -l "ko"
```

### ឧទាហរណ៍ទូទៅ

ពិនិត្យការបកប្រែភាសាកូរ៉េ និងជប៉ុន ពីថតបច្ចុប្បន្ន:

```bash
co-op-review -l "ko ja"
```

ពិនិត្យ root គម្រោងជាក់លាក់មួយ:

```bash
co-op-review -l "fr" -r ./my-course
```

ពិនិត្យតែឯកសារប្រភពដែលបានផ្លាស់ប្តូរទល់នឹង base ref មួយ:

```bash
co-op-review -l "ko" --changed-from origin/main
```

បោះពុម្ពលទ្ធផលជា Markdown រចនាបទ GitHub សម្រាប់សង្ខេប CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### ជម្រើស

| ជម្រើស | ត្រូវការឫទេ | ការពិពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-code` | ទេ | កូដភាសាសម្រាប់ពិនិត្យ។ អាចផ្តល់ច្រើនដង ឬជាតួអក្សរដាក់ចន្លោះ។ លំនាំដើមទៅលើភាសាបកប្រែទាំងអស់ដែលរកឃើញ។ |
| `-r`, `--root-dir` | ទេ | រុំឫតគម្រោង។ លំនាំដើមទៅថា ថតបច្ចុប្បន្ន។ |
| `--changed-from` | ទេ | ក ref Git ប្រើដើម្បីកំណត់ការពិនិត្យតែឯកសារប្រភពដែលបានផ្លាស់ប្តូរ។ |
| `--format` | ទេ | ទ្រង់ទ្រាយលទ្ធផល៖ `text` ឬ `github`។ លំនាំដើមជា `text`។ |

`co-op-review` សព្វថ្ងៃពិនិត្យរកឯកសារបកប្រែបាត់, មេតាដាតាអំពីការបកប្រែដែលបាត់ឬចាស់, សន្មថ frontmatter និង ខុំភីសោនោរបស់កូដ (code fence) នៅក្នុង Markdown, JSON notebook បកប្រែដែលមិនត្រឹមត្រូវ, និងគោលដៅតំណភ្ជាប់ Markdown ឬរូបភាពក្នុងសាធារណៈដែលបាត់។ តំណដែលបាត់គឺជាការព្រមានលំនាំដើម; បញ្ហាផ្នែករចនាសម្ព័ន្ធ និងភាពទាន់សម័យនឹងធ្វើឲ្យពាក្យបញ្ជាត្រូវបរាជ័យ។

## co-op-translator-mcp

រត់ម៉ាស៊ីនមេ Co-op Translator MCP សម្រាប់ភ្នាក់ងារ, អ្នកកែសម្រួល, និងកliet MCP-compatible។

```bash
co-op-translator-mcp
```

ការដឹកជញ្ជូនលំនាំដើមគឺ `stdio`។ មើលមេរៀន [MCP Server](mcp.md) សម្រាប់ការកំណត់កliet, ឧបករណ៍, ទ្រព្យសម្បត្តិ, និងកំណត់សុវត្ថិភាព។

### ជម្រើស

| ជម្រើស | ត្រូវការឫទេ | ការពិពណ៌នា |
| --- | --- | --- |
| `--transport` | ទេ | MCP transport: `stdio`, `streamable-http`, ឬ `sse`។ លំនាំដើមជា `stdio`។ |

## migrate-links

ដំណើរការឡើងវិញឯកសារ Markdown ដែលបានបកប្រែ និងធ្វើឲ្យតំណនៅក្នុង notebook ជាអ្នកបញ្ចូនទៅ notebook ដែលបានបកប្រែពេលមាន។

```bash
migrate-links -l "ko ja"
```

### ឧទាហរណ៍ទូទៅ

មើលជាមុនការផ្លាស់ប្តូរតំណ៖

```bash
migrate-links -l "ko" --dry-run
```

ដំណើរការភាសាអនុគ្រោះទាំងអស់ដោយគ្មានការបញ្ជាក់៖

```bash
migrate-links -l "all" -y
```

កែតែបញ្ជូលតំណម្ដងទេពេលមាន notebook បកប្រែ:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### ជម្រើស

| ជម្រើស | ត្រូវការឫទេ | ការពិពណ៌នា |
| --- | --- | --- |
| `-l`, `--language-codes` | បាទ/ចាស | កូដភាសាដាក់ចន្លោះ ជាជម្រើស ឬ `"all"`។ |
| `-r`, `--root-dir` | ទេ | រុំឫតគម្រោង។ លំនាំដើមទៅថា ថតបច្ចុប្បន្ន។ |
| `--image-dir` | ទេ | ថតរូបភាពដែលបានបកប្រែ יחסית root។ លំនាំដើមជា `translated_images`។ |
| `--dry-run` | ទេ | បង្ហាញឯកសារដែលនឹងផ្លាស់ប្តូរដោយមិនសរសេរអាប់ដេត។ |
| `--fallback-to-original`, `--no-fallback-to-original` | ទេ | ប្រើតំណ notebook ដើមពេល notebook បកប្រែមិនមាន។ បើកដោយលំនាំដើម។ |
| `-d`, `--debug` | ទេ | បើកកំណត់ហេតុខុសត្រូវ debug។ |
| `-s`, `--save-logs` | ទេ | រក្សាកំណត់ហេតុខុសត្រូវ DEBUG នៅក្នុង `<root-dir>/logs/`។ |
| `-y`, `--yes` | ទេ | បញ្ជាក់ដោយស្វ័យប្រវត្តិពេលដំណើរការភាសាទាំងអស់។ |

## បរិយាកាស

ពាក្យបញ្ជារទាំងអស់ត្រូវការអ្នកផ្គត់ផ្គង់ LLM មួយបានកំណត់:

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
```

ការបកប្រែរូបភាពត្រូវការបន្ថែម Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## រចនាសម្ព័ន្ធលទ្ធផល

ការបកប្រែអត្ថបទត្រូវបានសរសេរទៅក្រោម៖

```text
translations/<language-code>/<original-path>
```

លទ្ធផលរូបភាពដែលបកប្រែត្រូវបានសរសេរទៅក្រោម៖

```text
translated_images/<language-code>/<original-path>
```

ឧទាហរណ៍ បកប្រែ `README.md` និង `docs/setup.md` ទៅជาทាសាកូរ៉េ ផលិតជា:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## ឧទាហរណ៍ CLI សម្រាប់ចម្លង-បិទជាថ្មី

បកប្រែ Markdown ទៅជារបៀបបីភាសា:

```bash
translate -l "ko ja fr" -md
```

បកប្រែសៀវភៅកំណត់ត្រាតែប៉ុណ្ណោះ:

```bash
translate -l "zh-CN" -nb
```

បកប្រែរូបភាពតែប៉ុណ្ណោះ:

```bash
translate -l "pt-BR" -img
```

មើលជាមុនការបកប្រែ Markdown ដោយមិនសរសេរ​ឯកសារ:

```bash
translate -l "de es" -md --dry-run
```

ជួសជុលការបកប្រែ Markdown ដែលទទួលទំនុកចិត្តទាប:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

រត់ការបកប្រែ Markdown សមរម្យសម្រាប់ CI:

```bash
translate -l "ko ja" -md -y -s
```

ពិនិត្យលទ្ធផលដែលបានបកប្រែ:

```bash
co-op-review -l "ko ja"
```

មើលជាមុនការផ្លាស់ប្តូរតំណ:

```bash
migrate-links -l "ko" --dry-run
```