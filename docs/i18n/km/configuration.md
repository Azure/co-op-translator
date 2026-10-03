# ការកំណត់

Co-op Translator ត្រូវការ​អ្នកផ្គត់ផ្គងម៉ូឌែលភាសា​មួយ។ ការប្រែរូបភាពបន្ថែមទៀតត្រូវការព្រឹត្តការណ៍ Azure AI Vision។

ការកំណត់ត្រូវបានអានពីអថេរសម្រាប់បរិបទ (environment variables)។ សម្រាប់គម្រោងក្នុងស្រុក សូមដាក់ពួកវានៅក្នុងឯកសារ `.env` នៅឫសគម្រោង។

សម្រាប់ការតំឡើងធនធាន Azure សូមមើល [ការតំឡើង Azure AI](azure-ai-setup.md)។

## ការកំណត់ runtime ក្នុងកុំព្យូទ័រមូលដ្ឋាន

ប្រើបរិយាកាសមេរោគ (virtual environment) មុនពេលរត់ CLI នៅក្នុងស្រុក។ Co-op Translator គាំទ្រ Python 3.11 ដល់ 3.14។

សម្រាប់ការប្រើ CLI ទូទៅ សូមដំឡើងកញ្ចប់ដែលបានបោះពុម្ពនៅក្នុង virtual environment៖

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

### ការអភិវឌ្ឍន៍ Repository

សម្រាប់ការអភិវឌ្ឍន៍ repository សូមដំឡើងការពឹងផ្អែកពីឫសគម្រោងជំនួស៖

```bash
poetry install
poetry run translate --help
```

បន្ទាប់ពី CLI មានស្រាប់ សូមកំណត់អ្នកផ្គត់ផ្គង់ម៉ូឌែលភាសាមួយក្នុង `.env` ។

## ការជ្រើសរើសអ្នកផ្គត់ផ្គង់

ឧបករណ៍នេះស្វ័យប្រវត្តិរកអ្នកផ្គត់ផ្គង់នៅក្នុងលំដាប់ដូចខាងក្រោម៖

1. Azure OpenAI
2. OpenAI
3. Anthropic

ការប្រែប្រើត្រូវការបញ្ជាក់អត្តសញ្ញាណអ្នកផ្គត់ផ្គង់ លើកលែងតែក្នុងការមើលជាមុនដូចជា `translate -l "ko" -md --dry-run`។ `migrate-links`, `co-op-review`, និង `run_review` ជាដំណើរការថែទាំវត្ថុដដែលដែលមានលទ្ធភាពកំណត់ និងមិនត្រូវការការបញ្ជាក់អត្តសញ្ញាណអ្នកផ្គត់ផ្គង់។

## Backend របស់ client ម៉ូឌែល

ចាប់ពី Co-op Translator 0.22.0, Azure OpenAI, OpenAI, និង Anthropic ប្រើ Microsoft Agent Framework ជារៀងរហូត។ មិនចាំបាច់កំណត់ backend សម្រាប់ការប្រើប្រាស់ទូទៅ។

Semantic Kernel នៅតែអាចប្រើបានជាបណ្តោះអាសន្នសម្រាប់សមភាព។ ដើម្បីជ្រើសរើសវាដោយច្បាស់ សូមកំណត់៖

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

ការប្រើ Semantic Kernel នឹងបញ្ចេញការព្រមានថាកំពុងត្រូវបានលុបចេញ។ ផ្នែកកញ្ចប់នេះគ្រោងនឹងផ្លាស់ Semantic Kernel ទៅជាការពឹងផ្អែកជាជម្រើសក្នុង 0.23.0 ហើយយកការរួមបញ្ចូលចេញក្នុង 0.24.0 បើយោងទៅលលទ្ធផលសមភាព និងមតិព័ត៌មានពីអ្នកប្រើ។ Anthropic ត្រូវការនិង `agent-framework`; ការជ្រើស `semantic-kernel` ជាច្បាស់ជាមួយ Anthropic នឹងបរាជ័យដោយកំហុសកំណត់ការរៀបចំ។ តម្លៃមិនត្រឹមត្រូវនឹងបរាជ័យនៅពេលចាប់ផ្តើមកម្មវិធីប្រែដែលស្ដាប់ពីអ្នកផ្គត់ផ្គង់ មិនមែនស្ងាត់សត្រូវត្រឡប់ក្រោយទេ។ អានវិភាគការបញ្ចេញ និងរាយការណ៍បញ្ហានៅ [បញ្ហា GitHub #543](https://github.com/Azure/co-op-translator/issues/543)។

## Azure OpenAI

ប្រើ Azure OpenAI នៅពេលម៉ូឌែលរបស់អ្នកបានដាក់បញ្ជូននៅក្នុង Azure AI Foundry ឬ Azure OpenAI Service។

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ការត្រួតពិនិត្យការតភ្ជាប់ប្រើ endpoint, API key, API version និងឈ្មោះ deployment មុនពេលការប្រែចាប់ផ្តើម។

## OpenAI

ប្រើ OpenAI នៅពេលហៅ OpenAI API ដោយផ្ទាល់។

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ត្រូវការព្រោះTranslator ត្រូវការម៉ូឌែលជឿនជាក់លាក់សម្រាប់ការហៅ API។

ទុក `OPENAI_ORG_ID` និង `OPENAI_BASE_URL` ឲ្យស្អុយសម្រាប់ការកំណត់លំនាំដើម។ បញ្ចូល ID អង្គការម្នាក់តែប៉ុណ្ណោះ ប្រសិនបើគណនីរបស់អ្នកត្រូវការ ឬបញ្ចូល base URL តែពេលប្រើ endpoint ផ្ទាល់ខ្លួន។ កុំចម្លងតម្លៃគំរូសម្រាប់ការកំណត់ជាជម្រើស។

## Anthropic Claude

ប្រើ Anthropic នៅពេលហៅ Claude API ដោយផ្ទាល់។ បង្កើត [Anthropic API key](https://platform.claude.com/docs/en/get-started) ហើយជ្រើស [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ដែលគាំទ្រ។

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` និង `ANTHROPIC_MODEL` ត្រូវការជាអច្ឆរិយភាព។ អ្នកមិនត្រូវការ​កំណត់ `CO_OP_TRANSLATOR_MODEL_CLIENT` ទេ; Agent Framework គឺជា backend លំនាំដើម។

ទុក `ANTHROPIC_BASE_URL` ឲ្យស្អុយសម្រាប់ Anthropic API។ កំណត់វា​តែពេលប្រើ endpoint ផ្ទាល់ខ្លួន។

`ANTHROPIC_MAX_TOKENS` ស្តង់ដារត្រូវជា `8192`, ដែលអនុញ្ញាតកន្លែងសម្រាប់ស្ត្រីបម្រើ token ច្រើនដូចជា Meitei Mayek។ កាត់បន្ថយវាបើម៉ូឌែលរបស់អ្នកឬ endpoint ដែលសាងសមភាពជាមួយ Anthropic កំណត់លទ្ធផលចេញក្រោមតម្លៃនោះ។

## Azure AI Vision

ការប្រែរូបភាពត្រូវការប្រើ Azure AI Vision ដើម្បីឲ្យឧបករណ៍អាចដកអត្ថបទពីរូបភាពមុនពេលម៉ូឌែលភាសាដែលបានកំណត់ធ្វើការបកប្រែ។ Anthropic អាចបកប្រែអត្ថបទដែលដកចេញដូចដដែលដូច Azure OpenAI ឬ OpenAI។

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ប្រសិនបើបានជ្រើសការប្រែរូបភាពជាមួយ `-img`, `images=True`, ឬគ្មានចម្រៀងប្រភេទខ្លឹមសារ (content-type) ផ្សេងទៀត ឧបករណ៍នឹងផ្ទៀងផ្ទាត់ការកំណត់ Vision មុនការប្រែចាប់ផ្តើម។

## សំណុំអត្តសញ្ញាណច្រើន

ស្រទាប់កំណត់ចំណាំគាំទ្រសំណុំអត្តសញ្ញាណច្រើនដោយបន្ថែមស្រេចលើអថេរជាមួយលេខដូចគ្នា៖

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

សំណុំទាំងអស់ត្រូវតែសរុបល្អឥតខ្ចោះ។ ការត្រួតពិនិត្យសុខភាពនឹងជ្រើសសំណុំពេលដែលធ្វើការ មុនពេលការប្រែបន្ត។

OpenAI និង Anthropic គាំទ្រពិធីសាស្ត្រស្រេចដូចគ្នា។ តម្រូវឲ្យរក្សាទុករាល់អថេរនៅក្នុងសំណុំអត្តសញ្ញាណនៅលើស្រេចដូចគ្នា រួមទាំងតម្លៃជាជម្រើសដូចជា `OPENAI_BASE_URL_1` ឬ `ANTHROPIC_BASE_URL_1`។

## តម្រូវការកម្មវិធីបញ្ជា

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | បាទ | ទេ | ប្រែ Markdown ប៉ុណ្ណោះ។ |
| `translate -nb` | បាទ | ទេ | ប្រែ notebook ប៉ុណ្ណោះ។ |
| `translate -img` | បាទ | បាទ | ប្រែរូបភាពប៉ុណ្ណោះ។ |
| `translate` with no type flags | បាទ | បាទ | ម៉ូដលំនាំដើមរួមមាន Markdown, notebook, និងរូបភាព។ |
| `evaluate` | បាទ | ទេ | ប្រើការវាយតម្លៃដោយ LLM លុះត្រាតែបានជ្រើស `--fast`។ |
| `migrate-links` | ទេ | ទេ | ធ្វើការផ្លាស់ទីតំណក្នុងស្រុកដោយមិនហៅអ្នកផ្គត់ផ្គង់។ |
| `co-op-review` | ទេ | ទេ | រត់ការត្រួតពិនិត្យរចនាសម្ព័ន្ធការប្រែដែលកំណត់, ភាពទាន់សម័យ, Markdown, notebook, និងការត្រួតពិនិត្យតំណក្នុងស្រុក។ |
| `run_translation(markdown=True)` | បាទ | ទេ | ការប្រែ Markdown តាមកម្មវិធី។ |
| `run_translation(images=True)` | បាទ | បាទ | ការប្រែរូបភាពតាមកម្មវិធី។ |
| `run_review(...)` | ទេ | ទេ | ការត្រួតពិនិត្យដែល deterministic តាមកម្មវិធី។ |

## តំណរលទ្ធផលចេញ

លទ្ធផលចេញសម្រាប់ការប្រែអត្ថបទលំនាំដើម៖

```text
translations/<language-code>/<source-relative-path>
```

លទ្ធផលរូបភាពដែលបានបកប្រែលំនាំដើម៖

```text
translated_images/<language-code>/<source-relative-path>
```

Python API អាចលើកលែងថតទាំងនេះដោយ `translations_dir` និង `image_dir`។