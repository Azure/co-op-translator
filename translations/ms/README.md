# Co-op Translator

_Mudahkan automasi dan penyelenggaraan terjemahan untuk kandungan pendidikan GitHub anda merentasi pelbagai bahasa seiring projek anda berkembang._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Mula di sini:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Disokong oleh [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](./README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
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
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Gambaran keseluruhan

**Co-op Translator** membantu anda menempatkan kandungan pendidikan GitHub anda ke dalam pelbagai bahasa dengan mudah.
Apabila anda mengemas kini fail Markdown, imej, atau notebook, terjemahan akan kekal diselaraskan secara automatik, memastikan kandungan anda tepat dan dikemas kini untuk pelajar di seluruh dunia.

Gunakan dari CLI untuk terjemahan repositori, dari API Python untuk automasi, atau melalui pelayan MCP untuk aliran kerja ejen dan editor.

Contoh bagaimana kandungan yang diterjemahkan disusun:

![Contoh](../../imgs/translation-ex.png)

## Mengapa Co-op Translator?

Menterjemah satu fail adalah mudah. Menjaga keseluruhan repositori dokumentasi
diterjemah, dipautkan, dan dikemas kini adalah bahagian yang sukar.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Large Markdown files are split into chunks, so a long README does not depend on one fragile model response. If a chunk fails, Co-op Translator can retry and re-chunk only the failed part. |
| Incomplete translations should not be marked current | A truncated translation should never be sealed as up to date. Co-op Translator checks translation integrity before saving and can detect structurally incomplete existing translations. |
| Links should match the translated repo structure | Manual translations often leave relative links pointing back to the source tree. Co-op Translator rewrites Markdown, notebook, image, and README links to match the `translations/<lang>/...` structure. |
| Translation should work across an entire repo | Co-op Translator handles README files, docs, notebooks, and image text as part of one repository workflow, instead of translating files one by one. |
| Maintaining translations matters more than creating them once | Source hashes and translation metadata let Co-op Translator find outdated files, skip unchanged files, and keep translated content synchronized as the source repo evolves. |

## Bagaimana keadaan terjemahan diuruskan

Co-op Translator menguruskan kandungan yang diterjemah sebagai **artefak perisian berpenversi**,  
bukan sebagai fail statik.

Alat ini menjejaki keadaan Markdown, imej, dan notebook yang diterjemah
menggunakan **metadata berlingkup bahasa**.

Reka bentuk ini membolehkan Co-op Translator untuk:

- Mengesan terjemahan yang ketinggalan dengan boleh dipercayai
- Melayan Markdown, imej, dan notebook secara konsisten
- Skalakan dengan selamat merentasi repositori besar, pantas, dan berbilang bahasa

Dengan memodelkan terjemahan sebagai artefak yang diuruskan,
aliran kerja terjemahan selaras secara semula jadi dengan amalan
pengurusan pergantungan dan artefak perisian moden.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Related deep dives

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Mula

Co-op Translator boleh digunakan dari CLI, API Python, atau pelayan MCP. Mulakan dengan panduan aliran kerja jika anda memilih antara terjemahan tempatan, automasi, CI, dan integrasi ejen/editor.

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Contoh CLI minimum selepas konfigurasi:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Untuk kali pertama pada repositori besar, gunakan `--dry-run` sebelum menulis fail yang diterjemah. Lihat [CLI Reference](../../docs/cli.md) untuk bendera jenis kandungan, log, semakan, dan migrasi pautan.

Jalan pantas bekas dengan Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Jalan pantas bekas dengan PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Ciri-ciri

- Terjemahan automatik untuk Markdown, notebook, dan imej
- Menjaga terjemahan selari dengan perubahan sumber
- Berfungsi secara tempatan (CLI) atau dalam CI (GitHub Actions)
- Mendedahkan alat terjemahan Markdown, notebook, imej, semakan, dan projek melalui MCP
- Menggunakan Azure OpenAI atau OpenAI sebagai penyedia terjemahan
- Membolehkan MCP hos ejen menterjemah bahagian Markdown dan notebook tanpa kelayakan LLM Co-op Translator
- Menggunakan Azure AI Vision untuk pengektrakan teks imej dan terjemahan
- Menyemak struktur terjemahan dan kesegaran dengan pemeriksaan deterministik
- Menjaga format dan struktur Markdown

## Dokumentasi

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
> Untuk penyelenggara repositori Microsoft “For Beginners” sahaja.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## Sokong kami dan galakkan pembelajaran global

Sertai kami dalam merevolusikan cara kandungan pendidikan dikongsi di seluruh dunia! Beri [Co-op Translator](https://github.com/azure/co-op-translator) sebuah ⭐ di GitHub dan sokong misi kami untuk meruntuhkan halangan bahasa dalam pembelajaran dan teknologi. Minat dan sumbangan anda memberikan impak yang besar! Sumbangan kod dan cadangan ciri sentiasa dialu-alukan.

### Terokai kandungan pendidikan Microsoft dalam bahasa anda
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

## Pembentangan video

👉 Klik imej di bawah untuk menonton di YouTube.

- **Open at Microsoft**: Pengenalan ringkas 18-minit dan panduan pantas tentang cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Berminat untuk menyumbang kepada Azure Co-op Translator? Sila lihat our [CONTRIBUTING.md](../../CONTRIBUTING.md) untuk garis panduan tentang bagaimana anda boleh membantu menjadikan Co-op Translator lebih mudah diakses.

## Penyumbang

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod Etika

Projek ini telah mengamalkan the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut lihat the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## AI Bertanggungjawab

Microsoft komited untuk membantu pelanggan kami menggunakan produk AI kami secara bertanggungjawab, berkongsi pembelajaran kami, dan membina perkongsian berasaskan kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber ini boleh didapati di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI yang bertanggungjawab berpandukan prinsip AI kami iaitu keadilan, kebolehpercayaan dan keselamatan, privasi dan keselamatan, keterangkuman, ketelusan, dan akauntabiliti.

Model berskala besar untuk bahasa, imej, dan ucapan - seperti yang digunakan dalam contoh ini - berpotensi berkelakuan dengan cara yang tidak adil, tidak boleh dipercayai, atau menyinggung, yang seterusnya boleh menyebabkan kemudaratan. Sila rujuk the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk dimaklumkan tentang risiko dan batasan.

Pendekatan yang disyorkan untuk mengurangkan risiko ini adalah untuk memasukkan sistem keselamatan dalam seni bina anda yang boleh mengesan dan menghalang tingkah laku yang membahayakan. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan yang berdikari, yang dapat mengesan kandungan yang membahayakan yang dijana oleh pengguna dan AI dalam aplikasi dan perkhidmatan. Azure AI Content Safety merangkumi API teks dan imej yang membolehkan anda mengesan bahan yang membahayakan. Kami juga mempunyai Content Safety Studio interaktif yang membolehkan anda melihat, meneroka dan mencuba kod contoh untuk mengesan kandungan yang membahayakan merentasi pelbagai modaliti. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) membimbing anda melalui cara membuat permintaan kepada perkhidmatan.

Satu lagi aspek yang perlu diambil kira ialah prestasi keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami menganggap prestasi bermaksud sistem berfungsi seperti yang anda dan pengguna anda jangkakan, termasuk tidak menjana output yang membahayakan. Adalah penting untuk menilai prestasi keseluruhan aplikasi anda menggunakan [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda boleh menilai aplikasi AI anda dalam persekitaran pembangunan anda menggunakan the [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan sama ada set data ujian atau sasaran, hasil generatif aplikasi AI anda dinilai secara kuantitatif dengan penilai terbina dalam atau penilai tersuai pilihan anda. Untuk bermula dengan prompt flow sdk untuk menilai sistem anda, anda boleh mengikuti the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah anda menjalankan penilaian, anda boleh [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tanda dagangan

Projek ini mungkin mengandungi tanda dagangan atau logo untuk projek, produk, atau perkhidmatan. Penggunaan tanda dagangan atau logo Microsoft yang dibenarkan tertakluk kepada dan mesti mematuhi
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Penggunaan tanda dagangan atau logo Microsoft dalam versi projek yang diubah suai tidak boleh menyebabkan kekeliruan atau memberi implikasi penajaan Microsoft.
Sebarang penggunaan tanda dagangan atau logo pihak ketiga tertakluk kepada polisi pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika anda tersekat atau mempunyai sebarang pertanyaan mengenai membina aplikasi AI, sertai:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika anda mempunyai maklum balas produk atau ralat semasa membina lawati:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)