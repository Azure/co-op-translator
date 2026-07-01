# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![កញ្ចប់ Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![អាជ្ញាប័ណ្ណ: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![ការទាញយក](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![ការទាញយក](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![កុងតឺន័រ: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![រចនាប័ទ្ម​កូដ: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![អ្នករួមចំណែក GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![បញ្ហា GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-Requests GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![ស្វាគមន៍ PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**ចាប់ផ្ដើមនៅទីនេះ:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [ម៉ាស៊ីនបម្រើ MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](./README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> ឃ្លាំងនេះមានការបកប្រែលើស 50 ភាសា ដែលធ្វើឲ្យទំហំទាញយកធំឡើងយ៉ាងទូលំទូលាយ។ ដើម្បី clone ដោយមិនទាញយកឯកសារបកប្រែ សូមប្រើ sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> វានឹងផ្ដល់អ្វីដែលអ្នកត្រូវការទាំងអស់ដើម្បីបញ្ចប់វគ្គសិក្សា ដោយមានការទាញយកដែលលឿនជាងមុន។

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![អ្នកតាមដាន GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![ផ្កាយ GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![បើកក្នុង GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ទិដ្ឋភាពទូទៅ

**Co-op Translator** ជួយអ្នកក្នុងការរួមបម្លែងមាតិកាអប់រំលើ GitHub ទៅជាភាសាជាច្រើនបានយ៉ាងងាយស្រួល។ ជាមួយពេលដែលអ្នកធ្វើបច្ចុប្បន្នភាពឯកសារ Markdown, រូបភាព ឬ notebook ការបកប្រែទាំងឡាយនឹងត្រូវសមកាលភាពដោយស្វ័យប្រវត្តិ ដែលធានាថាមាតិការបស់អ្នកនៅតែត្រឹមត្រូវ និងបច្ចុប្បន្នសម្រាប់អ្នកសិក្សាទូទាំងពិភពលោក។

ប្រើវាចេញពី CLI សម្រាប់ការបកប្រែឃ្លាំង, ពី Python API សម្រាប់ស្វ័យករណ៍, ឬតាមរយៈម៉ាស៊ីនបម្រើ MCP សម្រាប់លំហូរអ្នកប្រើប្រាស់-agent និងកែសម្រួល។

Example of how translated content is organized:

![ឧទាហរណ៍](../../imgs/translation-ex.png)

## ហេតុអ្វី Co-op Translator?

Translating one file is easy. Keeping an entire documentation repository
translated, linked, and up to date is the hard part.

| បញ្ហា | របៀប Co-op Translator ជួយ |
| --- | --- |
| Long docs are not one prompt | ឯកសារ Markdown វែងៗ ត្រូវបានបំបែកចេញជាផ្នែកតូចៗ ដូច្នេះ README វែងមួយមិនពឹងផ្អែកលើចម្លើយពីម៉ូឌែលតែមួយដែលងាយខូចទុកទេ។ ប្រសិនបើផ្នែកណាមួយបរាជ័យ Co-op Translator អាចព្យាយាមម្តងទៀត ហើយបំបែកឡើងវិញសម្រាប់ផ្នែកដែលបរាជ័យតែកន្លែងនោះ។ |
| Incomplete translations should not be marked current | ការបកប្រែដែលត្រូវកាត់ខ្លី មិនគួរត្រូវបានគិតថា​ត្រឹមត្រូវ​បច្ចុប្បន្ន។ Co-op Translator ពិនិត្យភាពទាំងមូលនៃការបកប្រែមុនពេលរក្សាទុក ហើយអាចរកឃើញការបកប្រែដែលខ្វះដោយរចនាសម្ព័ន្ធបាន។ |
| Links should match the translated repo structure | ការបកប្រែដោយដៃជាញិញជាមានន័យថា link ដែលជាអ نسب(Relative) គួរត្រូវតែបង្ហាញត្រឡប់ទៅដើមឈើដើម។ Co-op Translator សរសេរឡើងវិញ Markdown, notebook, រូបភាព និង README links ដើម្បីផ្គូរផ្គងទៅនឹងរចនាសម្ព័ន្ធ `translations/<lang>/...`។ |
| Translation should work across an entire repo | Co-op Translator គ្រប់គ្រង README files, docs, notebooks និងអត្ថបទក្នុងរូបភាពដោយជាទម្រង់លំហូរបស់ឃ្លាំងមួយទៀងទាត់ មិនមែនបកប្រែកឯកសារមួយៗ។ |
| Maintaining translations matters more than creating them once | Hashs ของ source និង metadata នៃការបកប្រែនាំឲ្យ Co-op Translator រកឃើញឯកសារចាស់ៗ, កាត់កើតឯកសារដែលមិនប្រែប្រួល, និងរក្សាការសមកាលភាពនៃការបកប្រែពេលដែលឃ្លាំងដើមមានការផ្លាស់ប្ដូរ។ |

## របៀបគ្រប់គ្រងស្ថានភាពការបកប្រែ

Co-op Translator គ្រប់គ្រងមាតិកាបកប្រែជាប្រភេទ "អាត៊ីហ្វ៉ាក់សូហ្វ្ថវែរ" ដែលមានកំណែ (versioned software artifacts),  
មិនមែនជាឯកសារស្ថិតស្ថេរទេ។

ឧបករណ៍នេះតាមដានស្ថានភាពនៃ Markdown, រូបភាព និង notebooks ដែលបានបកប្រែ
ដោយប្រើ metadata ដែលពាក់ព័ន្ធតាមភាសា។

ការរចនានេះអនុញ្ញាតឲ Co-op Translator អាច:

- រកឃើញការបកប្រែចាស់ៗដោយទុកចិត្ត
- ដំណើរការ Markdown, រូបភាព និង notebooks ឲ្យក្លាយជា​ទៀងទាត់
- លានសមត្ថភាពឲ្យសមរម្យនៅក្នុងឃ្លាំងធំដែលផ្លាសចលនាដោយលឿន និងមានភាសាច្រើន

ដោយមើលការបកប្រែជា អាត៊ីហ្វ៉ាក់ដែលគ្រប់គ្រង,
លំហូរការបកប្រែឆ្គាំឆ្គងជាមួយនឹងអនុប្បទាប современной
វិធានការគ្រប់គ្រងអាសយដ្ឋាន និងអាត៊ីហ្វ៉ាក់នៃសូហ្វ ថូវែរ។

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Related deep dives

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## ចាប់ផ្ដើម

Co-op Translator អាចប្រើបានពី CLI, Python API, ឬម៉ាស៊ីនបម្រើ MCP។ ចាប់ផ្ដើមជាមួយមគ្គុទេសក៍ workflow ប្រសិនបើអ្នកកំពុងជ្រើសរើសរវាងការបកប្រែក្នុងកុំព្យូទ័រមូលដ្ឋាន, ស្វ័យករ, CI, និងការរួមបញ្ចូលរវាង agent/editor។

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Minimal CLI example after configuration:

```bash
python -m venv .venv
# វីនដូ
.venv\Scripts\activate
# ម៉ាក់អូអេស/លីនុច
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

For first runs on large repositories, use `--dry-run` before writing translated files. See the [CLI Reference](../../docs/cli.md) for content type flags, logs, review, and link migration.

Container quick run with Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Container quick run with PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## មុខលក្ខណៈ

- បកប្រែស្វ័យប្រវត្តិសម្រាប់ Markdown, notebooks, និងរូបភាព
- រក្សាការសមកាលភាពការបកប្រែជាមួយការផ្លាស់ប្តូរក្នុងប្រភព
- ប្រើបាននៅក្នុងកុំព្យូទ័រមូលដ្ឋាន (CLI) ឬក្នុង CI (GitHub Actions)
- បង្ហាញឧបករណ៍បកប្រែ Markdown, notebook, រូបភាព, ការត្រួតពិនិត្យ និងគម្រោង តាមរយៈ MCP
- ប្រើ Azure OpenAI ឬ OpenAI សម្រាប់អ្នកផ្គត់ផ្គង់ (provider)-supported translation
- អនុញ្ញាតឲ MCP ជាអ្នកផ្តល់ទីតាំងឲ្យ agents បកប្រែកchunks Markdown និង notebook ដោយមិនចាំបាច់មានគណនី LLM របស់ Co-op Translator
- ប្រើ Azure AI Vision សម្រាប់ដកអត្ថបទពីរូបភាព និងបកប្រែ
- ត្រួតពិនិត្យរចនាសម្ព័ន្ធនិងភាពទាន់សម័យនៃការបកប្រែជាមួយតេស្តដែលកំណត់ច្បាស់
- រក្សាទ្រង់ទ្រាយ និងរចនាសម្ព័ន្ធ Markdown

## ឯកសារ

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> សម្រាប់អ្នកថែទាំរបស់ឃ្លាំង Microsoft “For Beginners” តែប៉ុណ្ណោះ។

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## គាំទ្រយើង និងសម្របតាមការសិក្សាថ្មីทั่วលោក

ចូលរួមជាមួយយើងក្នុងការបំលែងរបៀបដែលមាតិកាហត្ថាបណ្តុះបណ្តាលត្រូវចែកចាយជាច្រើនជាសកល! ផ្ដល់⭐ ទៅ [Co-op Translator](https://github.com/azure/co-op-translator) លើ GitHub និងគាំទ្រយុទ្ធសាស្ត្ររបស់យើងក្នុងការបំបែកឧបសគ្គភាសាក្នុងការសិក្សា និងបច្ចេកវិទ្យា។ ការចាប់អារម្មណ៍ និងការរួមចំណែករបស់អ្នកមានអត្ថិភាពយ៉ាងខ្លាំង! ការរួមចំណែកកូដ និងការផ្តល់យោបល់លើមុខងារ សូមស្វាគមន៍អស់។

### ស្វែងយល់មាតិកាអប់រំ Microsoft ជាភាសារបស់អ្នក
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ការបង្ហាញវីដេអូ

👉 ចុចរូបភាពខាងក្រោមដើម្បីមើលលើ YouTube។

- **Open នៅ Microsoft**: ការណែនាំខ្លីប្រមាណ 18 នាទី និងមគ្គុទេសក៍លឿនអំពីវិធីប្រើ Co-op Translator។

  [![Open នៅ Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## រួមចំណែក

គម្រោងនេះស្វាគមន៍ការរួមចំណែក និងយោបល់។ ចាប់អារម្មណ៍ក្នុងការរួមចំណែកទៅ Azure Co-op Translator ទេ? សូមមើល [CONTRIBUTING.md](../../CONTRIBUTING.md) សម្រាប់កាន់តែលម្អិតអំពីរបៀបដែលអ្នកអាចជួយធ្វើឱ្យ Co-op Translator មានភាពងាយចូលប្រើកាន់តែច្រើន។

## អ្នករួមចំណែក

[![អ្នករួមចំណែក co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## កូដអាកប្បកិរិយា

គម្រោងនេះបានទទួលយក [កូដអាកប្បកិរិយាសម្រាប់ប្រភពបើករបស់ Microsoft](https://opensource.microsoft.com/codeofconduct/)។ សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [សំណួរញឹកញាប់អំពីកូដអាកប្បកិរិយា](https://opensource.microsoft.com/codeofconduct/faq/) ឬ ទំនាក់ទំនង [opencode@microsoft.com](mailto:opencode@microsoft.com) ប្រសិនបើមានសំណួរ ឬ មតិយោបល់បន្ថែម។

## AI ធ្វើការ​ខាងទទួលខុសត្រូវ

Microsoft មានក្តីសន្យាផ្តល់ជំនួយដល់អតិថិជនដើម្បីប្រើផលិតផល AI របស់យើងយ៉ាងមានការទទួលខុសត្រូវ, ចែករំលែកบทសិក្សា, និងសាងសង់ភាពជាដៃគូផ្អែកលើទំនុកចិត្ត តាមឧបករណ៍ដូចជា Transparency Notes និង Impact Assessments។ ធនធានជាច្រើនអាចស្វែងរកបាននៅ [https://aka.ms/RAI](https://aka.ms/RAI)។

យុទ្ធសាស្ត្ររបស់ Microsoft ចំពោះ AI ដែលមានការទទួលខុសត្រូវស្ថិតលើគោលការណ៍ AI របស់យើង ដូចជា ភាពយុតិធម៌, ការជឿទុកចិត្ត និងសុវត្ថិភាព, សម្ងាត់និងសន្តិសុខ, ភាពរួមបញ្ចូល, ភាពថ្លា, និងការទទួលខុសត្រូវ។

ម៉ូឌែលធំនៃភាសា, រូបភាព និងសំឡេង — ដូចជាThose used in this sample — អាចមានឥរិយាបថដែលអាចមិនយុតិធម៌, មិនអាចទុកចិត្តបាន, ឬអាចជួបប្រទៈចំពោះអត្ថន័យផ្ទាល់ខ្លួន ដោយបណ្ដាលឲ្យមានគ្រោះថ្នាក់។ សូមយោងទៅកាន់ [សេចក្តីសម្គាល់ភាពថ្លាពីសេវា Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ដើម្បីទទួលបានព័ត៌មានអំពីហានិភ័យ និងគួចចំនុចកំណត់។

វិធីសាស្ត្រដែលផ្ដល់អនុសាសន៍ក្នុងការត្រួតពិនិត្យហានិភ័យទាំងនេះ គឺការរួមបញ្ចូលប្រព័ន្ធសុវត្ថិភាពនៅក្នុងស្ថាបត្យកម្មរបស់អ្នក ដែលអាចស្គាល់ និងទប់ស្កាត់ឥរិយាបថមិនល្អបាន។ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ផ្តល់ជានិរន្តរភាពការការពារ ដោយអាចស្គាល់មាតិកាដែលបង្កហានិភ័យដែលបានបង្កើតដោយអ្នកប្រើ និងដោយ AI នៅក្នុងកម្មវិធី និងសេវាកម្ម។ Azure AI Content Safety រួមមាន API សម្រាប់អត្ថបទ និងរូបភាព ដែលអនុញ្ញាតឲ្យអ្នកស្គាល់មាតិកាដែលមានហានិភ័យ។ យើងក៏មាន Content Safety Studio អន្តរកម្ម ដែលអាចឲ្យអ្នកមើល, ស្វែងចែក និងសាកល្បងកូដឧទាហរណ៍សម្រាប់ស្គាល់មាតិកាដែលបង្កហានិភ័យនៅក្នុងរបៀបផ្សេងៗគ្នា។ កុងតឺនដែលមើលឃើញក្នុង [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ខាងក្រោម នាំបង្ហាញអ្នកតាមដានវិធីធ្វើសំណើទៅសេវា។

មុខម្ហូបមួយទៀតដែលគួរឲ្យយកចិត្តទុកដាក់ គឺកម្រិតសមត្ថភាពរួមបញ្ចូលនៃកម្មវិធី។ ជាមួយកម្មវិធីដែលមានមុខងារច្រើន-ចំហៀង និងម៉ូឌែលជាច្រើន យើងចាត់ទុកថា សមត្ថភាពបង្ហាញថារូបបែបនេះសមនឹងការរំពឹងទុករបស់អ្នកនិងអ្នកប្រើ រួមទាំងការមិនបង្កើតផលិតផលមានគ្រោះថ្នាក់។ វាសំខាន់ក្នុងការវាយតម្លៃសមត្ថភាពរបស់កម្មវិធីរួមសរុបដោយប្រើ [គុណភាពការបង្កើត និង ម៉ែត្រហានិភ័យនិងសុវត្ថិភាព](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)។

អ្នកអាចវាយតម្លៃកម្មវិធី AI របស់អ្នកនៅក្នុងបរិយាកាសអភិវឌ្ឍន៍ដោយប្រើ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html)។ ប្រសិនបើមានទិន្នន័យសាកល្បង ឬ គោលដៅណាណាមួយ ការបង្កើតរបស់កម្មវិធី generative AI របស់អ្នក នឹងត្រូវបានវាស់វែងជាបរិមាណដោយឧបករណ៍វាស់វែងដែលមានរួចឬឧបករណ៍វាស់វែងឯកជនដែលអ្នកជ្រើស។ ដើម្បីចាប់ផ្តើមប្រើ prompt flow sdk សម្រាប់វាយតម្លៃប្រព័ន្ធរបស់អ្នក អ្នកអាចអាន [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)។ បន្ទាប់ពីអ្នកអនុវត្តការប្រតិបត្តិការវាយតម្លៃ អ្នកអាច [បង្ហាញទិន្នផលនៅក្នុង Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)។

## សញ្ញាពាណិជ្ជកម្ម

គម្រោងនេះអាចមានសញ្ញាពាណិជ្ជកម្ម ឬឡូហ្គោសម្រាប់គម្រោង, ផលិតផល, ឬសេវាកម្ម المختلفة។ ការប្រើប្រាស់សញ្ញាពាណិជ្ជកម្ម ឬឡូហ្គោរបស់ Microsoft ត្រូវសម្របខ្លួន និងត្រូវតាម [សេចក្ដីណែនាំសញ្ញាពាណិជ្ជកម្ម និងម៉ាករបស់ Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)។ ការប្រើប្រាស់សញ្ញា ឬឡូហ្គោរបស់ Microsoft ក្នុងកំណែដែលបានកែប្រែក្នុងគម្រោងនេះ មិនគួរបង្កឲ្យមានច្របូកច្របល់ ឬពន្យល់ថា Microsoft ជាអ្នកឧបត្ថម្ភ។ ការប្រើប្រាស់សញ្ញាពាណិជ្ជកម្ម ឬឡូហ្គោរបស់ភាគីទីបី ត្រូវសម្របទៅតាមគោលការណ៍នៃភាគីទីបីនោះៗ។

## ការទទួលជំនួយ

ប្រសិនបើអ្នកជាប់ព្រួយ ឬមានសំណួរអំពីការសាងសង់កម្មវិធី AI សូមចូលរួម៖

[![Discord របស់ Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

បើអ្នកមានមតិយោបល់ពីផលិតផល ឬកំហុសពេលកំពុងសាងសង់ សូមទៅកាន់៖

[![វេទិកាអភិវឌ្ឍន៍ Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)