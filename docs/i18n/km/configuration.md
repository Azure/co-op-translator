# ការកំណត់

Co-op Translator ត្រូវការអ្នកផ្គត់ផ្គង់ម៉ូដែលភាសា មួយ។ ការបកប្រែរូបភាពត្រូវការផងដែរ Azure AI Vision។

ការកំណត់ត្រូវបានអានពី environment variables។ សម្រាប់ប្រព័ន្ធ​ផLocal, ដាក់ពួកវាក្នុងឯកសារ `.env` នៅឬតាម root នៃគម្រោង។

សម្រាប់ការរៀបចំធនធាន Azure, មើល [Azure AI Setup](azure-ai-setup.md)។

## ការកំណត់​សម្រាប់​រត់​នៅ​ម៉ាស៊ីន​ផ្ទាល់

ប្រើ virtual environment មុនពេលរត់ CLI នៅលើកុំព្យូទ័រផ្ទាល់។ Co-op Translator គាំទ្រ Python 3.10 រហូតដល់ 3.12 ។

សម្រាប់ការប្រើប្រាស់ CLI ទូទៅ, តំឡើង package ដែលបានបោះពុម្ពផ្សាយនៅក្នុង virtual environment៖

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

សម្រាប់ការអភិវឌ្ឍក្នុង repository, តំឡើងការពឹងផ្អែកពី root នៃគម្រោងជាផ្ទាល់៖

```bash
poetry install
poetry run translate --help
```

បន្ទាប់ពី CLI អាចប្រើបាន សូមកំណត់អ្នកផ្គត់ផ្គង់ម៉ូដែលភាសា​មួយ ក្នុង `.env` ។

## ការជ្រើសរើសអ្នកផ្គត់ផ្គង់

ឧបករណ៍នេះស្វ័យប្រវត្តិកំណត់អ្នកផ្គត់ផ្គង់ក្នុងលំដាប់នេះ៖

1. Azure OpenAI
2. OpenAI

ប្រសិនបើគ្មានអ្នកផ្គត់ផ្គង់ណាមួយត្រូវបានកំណត់, `translate`, `evaluate`, `migrate-links`, និង `run_translation` នឹងបរាជ័យក្នុងពេលធ្វើតេស្តការកំណត់។ `co-op-review` និង `run_review` គឺជាការត្រួតពិនិត្យថែទាំអាចកំណត់បាន ហើយមិនត្រូវការតំណក្រដាសអ្នកផ្គត់ផ្គង់ទេ។

## Azure OpenAI

ប្រើ Azure OpenAI នៅពេលម៉ូដែលរបស់អ្នកត្រូវបានដាក់ពង្រីកនៅក្នុង Azure AI Foundry ឬ Azure OpenAI Service។

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ការត្រួតពិនិត្យការតភ្ជាប់ប្រើ endpoint, API key, API version, និង deployment name មុនការចាប់ផ្តើមការបកប្រែ។

## OpenAI

ប្រើ OpenAI នៅពេលហៅ OpenAI API ត្រង់ៗ។

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ជាជម្រើស
OPENAI_BASE_URL="..."        # ជាជម្រើស
```

`OPENAI_CHAT_MODEL_ID` ត្រូវការ ព្រោះ translator ត្រូវការម៉ូដែល chat បញ្ជាក់សម្រាប់ការហៅ API ។

## Azure AI Vision

ការបកប្រែរូបភាពត្រូវការការកំណត់ Azure AI Vision ដើម្បីឲ្យឧបករណ៍អាចយកអក្សរចេញពីរូបភាពមុនពេលបកប្រែវា។ 

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ប្រសិនបើការបកប្រែរូបភាពត្រូវបានជ្រើសជាមួយ `-img`, `images=True`, ឬគ្មាន content-type filter, ឧបករណ៍នឹងផ្ទៀងផ្ទាត់ការកំណត់ Vision មុនពេលចាប់ផ្តើមការបកប្រែ។

## សំណុំគ្រប់គ្រងអត្តសញ្ញាណច្រើន

ស្រទាប់ការកំណត់គាំទ្រការកំណត់សំណុំគ្រប់គ្រងសញ្ញាច្រើន ដោយបញ្ចប់ឈ្មោះអថេរជាមួយលេខទីពីប្រភេទដដែល៖

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

រាល់សំណុំត្រូវតែមានគ្រប់។ ការត្រួតពិនិត្យសុខភាពនឹងជ្រើសសំណុំដែលដំណើរការបានមួយ មុនពេលការបកប្រែបន្ត។

## តម្រូវការកម្មង់

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | ចាំបាច់ | មិនចាំបាច់ | បកប្រែ Markdown តែប៉ុណ្ណោះ។ |
| `translate -nb` | ចាំបាច់ | មិនចាំបាច់ | បកប្រែ notebooks តែប៉ុណ្ណោះ។ |
| `translate -img` | ចាំបាច់ | ចាំបាច់ | បកប្រែរូបភាពតែប៉ុណ្ណោះ។ |
| `translate` with no type flags | ចាំបាច់ | ចាំបាច់ | របៀបលំនាំដើម​រួមមាន Markdown, notebooks, និង រូបភាព។ |
| `evaluate` | ចាំបាច់ | មិនចាំបាច់ | ប្រើការវាយតម្លៃដោយ LLM លុះត្រាតែបានជ្រើស `--fast`។ |
| `migrate-links` | ចាំបាច់ | មិនចាំបាច់ | អនុវត្តការផ្លាស់ទីតំណ (link migration), ប៉ុន្តែ​នៅតែដោយរត់ការត្រួតពិនិត្យការកំណត់រួម។ |
| `co-op-review` | មិនចាំបាច់ | មិនចាំបាច់ | រត់ការត្រួតពិនិត្យ deterministic សម្រាប់​រចនាសម្ព័ន្ធ​បកប្រែ, ភាពទាន់សម័យ, Markdown, notebook, និង តំណក្នុងស្រុក។ |
| `run_translation(markdown=True)` | ចាំបាច់ | មិនចាំបាច់ | ការបកប្រែ Markdown ដោយកម្មវិធី។ |
| `run_translation(images=True)` | ចាំបាច់ | ចាំបាច់ | ការបកប្រែរូបភាពដោយកម្មវិធី។ |
| `run_review(...)` | មិនចាំបាច់ | មិនចាំបាច់ | ការត្រួតពិនិត្យ deterministic ដោយកម្មវិធី។ |

## ថតផ្លូវចេញ

ថតលទ្ធផលលំនាំដើមសម្រាប់អត្ថបទដែលបានបកប្រែ:

```text
translations/<language-code>/<source-relative-path>
```

ថតលទ្ធផលលំនាំដើមសម្រាប់រូបភាពដែលបានបកប្រែ:

```text
translated_images/<language-code>/<source-relative-path>
```

API Python អាចប្តូរថតទាំងនេះបានដោយប្រើ `translations_dir` និង `image_dir`។