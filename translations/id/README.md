# Co-op Translator

_Mudah mengotomatiskan dan memelihara terjemahan untuk konten edukasi GitHub Anda ke berbagai bahasa seiring proyek Anda berkembang._

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

**Mulai di sini:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Dukungan Multi-Bahasa

#### Didukung oleh [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](./README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Lebih Suka Meng-Cloning Secara Lokal?**
>
> Repositori ini mencakup lebih dari 50 terjemahan bahasa yang secara signifikan menambah ukuran unduhan. Untuk meng-clone tanpa terjemahan, gunakan sparse checkout:
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
> Ini memberi Anda semua yang diperlukan untuk menyelesaikan kursus dengan unduhan yang jauh lebih cepat.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ikhtisar

**Co-op Translator** membantu Anda melokalkan konten edukasi GitHub Anda ke berbagai bahasa dengan mudah.
Saat Anda memperbarui file Markdown, gambar, atau notebook, terjemahan akan tetap tersinkronisasi secara otomatis, memastikan konten Anda tetap akurat dan mutakhir bagi pelajar di seluruh dunia.

Gunakan dari CLI untuk menerjemahkan repositori, dari Python API untuk otomatisasi, atau melalui server MCP untuk alur kerja agen dan editor.

Contoh bagaimana konten terjemahan diatur:

![Example](../../imgs/translation-ex.png)

## Mengapa Co-op Translator?

Menerjemahkan satu file itu mudah. Menjaga seluruh repositori dokumentasi
yang sudah diterjemahkan, terhubung, dan mutakhir adalah bagian yang sulit.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | File Markdown besar dibagi menjadi potongan-potongan, sehingga README panjang tidak bergantung pada satu respons model yang rapuh. Jika sebuah potongan gagal, Co-op Translator dapat mencoba lagi dan hanya memproses ulang bagian yang gagal. |
| Incomplete translations should not be marked current | Terjemahan yang terpotong tidak boleh ditandai sebagai mutakhir. Co-op Translator memeriksa integritas terjemahan sebelum menyimpan dan dapat mendeteksi terjemahan yang secara struktural tidak lengkap. |
| Links should match the translated repo structure | Terjemahan manual sering meninggalkan tautan relatif yang mengarah kembali ke pohon sumber. Co-op Translator menulis ulang tautan Markdown, notebook, gambar, dan README agar sesuai dengan struktur `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator menangani file README, docs, notebook, dan teks gambar sebagai bagian dari satu alur kerja repositori, alih-alih menerjemahkan file satu per satu. |
| Maintaining translations matters more than creating them once | Hash sumber dan metadata terjemahan memungkinkan Co-op Translator menemukan file yang usang, melewati file yang tidak berubah, dan menjaga konten terjemahan tetap sinkron saat repositori sumber berkembang. |

## Bagaimana status terjemahan dikelola

Co-op Translator mengelola konten terjemahan sebagai **artefak perangkat lunak yang diberi versi**,  
bukan sebagai file statis.

Alat ini melacak status Markdown, gambar, dan notebook yang diterjemahkan
menggunakan **metadata yang dibatasi per bahasa**.

Desain ini memungkinkan Co-op Translator untuk:

- Mendeteksi terjemahan yang usang dengan andal
- Memperlakukan Markdown, gambar, dan notebook secara konsisten
- Berskala dengan aman di seluruh repositori multi-bahasa yang besar dan bergerak cepat

Dengan memodelkan terjemahan sebagai artefak yang dikelola,
alur kerja terjemahan selaras secara alami dengan praktik
manajemen ketergantungan dan artefak perangkat lunak modern.

→ [Bagaimana status terjemahan dikelola](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Ulasan mendalam terkait

- [Memperbaiki Markdown Rusak dalam Terjemahan AI: Memperkuat Pipeline Produksi](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Memulai

Co-op Translator dapat digunakan dari CLI, Python API, atau server MCP. Mulailah dengan panduan alur kerja jika Anda memilih di antara terjemahan lokal, otomatisasi, CI, dan integrasi agen/editor.

- [Pilih alur kerja Anda](../../docs/workflows.md)
- [Konfigurasikan kredensial](../../docs/configuration.md)
- [Terjemahkan dari CLI](../../docs/cli.md)
- [Otomatisasi dengan Python API](../../docs/api.md)
- [Hubungkan dengan Server MCP](../../docs/mcp.md)
- [Jalankan di GitHub Actions](../../docs/github-actions.md)

Contoh CLI minimal setelah konfigurasi:

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

Untuk jalankan pertama pada repositori besar, gunakan `--dry-run` sebelum menulis file terjemahan. Lihat [CLI Reference](../../docs/cli.md) untuk flag tipe konten, log, peninjauan, dan migrasi tautan.

Jalankan cepat container dengan Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Jalankan cepat container dengan PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Fitur

- Terjemahan otomatis untuk Markdown, notebook, dan gambar
- Menjaga terjemahan sinkron dengan perubahan sumber
- Bekerja secara lokal (CLI) atau di CI (GitHub Actions)
- Mengekspos alat terjemahan untuk Markdown, notebook, gambar, peninjauan, dan proyek melalui MCP
- Menggunakan Azure OpenAI atau OpenAI untuk penyedia terjemahan
- Memungkinkan MCP menjadi host agen untuk menerjemahkan potongan Markdown dan notebook tanpa kredensial LLM Co-op Translator
- Menggunakan Azure AI Vision untuk ekstraksi teks gambar dan terjemahan
- Meninjau struktur dan kesegaran terjemahan dengan pemeriksaan deterministik
- Mempertahankan format dan struktur Markdown

## Dokumentasi

- [Situs dokumentasi](https://azure.github.io/co-op-translator/)
- [Pilih alur kerja Anda](../../docs/workflows.md)
- [Konfigurasi](../../docs/configuration.md)
- [Pengaturan Azure AI](../../docs/azure-ai-setup.md)
- [Referensi CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [Server MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Template README bahasa](../../docs/readme-languages-template.md)
- [Bahasa yang didukung](../../docs/supported-languages.md)
- [Kontribusi](../../CONTRIBUTING.md)
- [Pemecahan masalah](../../docs/troubleshooting.md)

### Panduan khusus Microsoft
> [!NOTE]
> Untuk pemelihara repositori Microsoft “For Beginners” saja.

- [Memperbarui daftar “other courses” (hanya untuk repositori MS Beginners)](../../docs/microsoft-beginners.md)

## Dukung kami dan dukung pembelajaran global

Bergabunglah bersama kami dalam merevolusi cara konten edukasi dibagikan secara global! Berikan [Co-op Translator](https://github.com/azure/co-op-translator) sebuah ⭐ di GitHub dan dukung misi kami untuk menghapus hambatan bahasa dalam pembelajaran dan teknologi. Minat dan kontribusi Anda memberikan dampak besar! Kontribusi kode dan saran fitur selalu disambut.

### Jelajahi konten edukasi Microsoft dalam bahasa Anda
- [LangChain4j untuk Pemula](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD untuk Pemula](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI untuk Pemula](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) untuk Pemula](https://github.com/microsoft/mcp-for-beginners)
- [Agen AI untuk Pemula](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI untuk Pemula menggunakan .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI untuk Pemula](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI untuk Pemula menggunakan Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML untuk Pemula](https://aka.ms/ml-beginners)
- [Data Science untuk Pemula](https://aka.ms/datascience-beginners)
- [AI untuk Pemula](https://aka.ms/ai-beginners)
- [Keamanan Siber untuk Pemula](https://github.com/microsoft/Security-101)
- [Pengembangan Web untuk Pemula](https://aka.ms/webdev-beginners)
- [IoT untuk Pemula](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Presentasi video

👉 Klik gambar di bawah untuk menonton di YouTube.

- **Open di Microsoft**: Sebuah pengantar singkat 18 menit dan panduan cepat tentang cara menggunakan Co-op Translator.

  [![Open di Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Berkontribusi

Proyek ini menerima kontribusi dan saran. Tertarik berkontribusi pada Azure Co-op Translator? Silakan lihat [CONTRIBUTING.md](../../CONTRIBUTING.md) untuk pedoman tentang bagaimana Anda dapat membantu membuat Co-op Translator lebih mudah diakses.

## Kontributor

[![kontributor co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kode Perilaku

Proyek ini telah mengadopsi [Kode Perilaku Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/).
Untuk informasi lebih lanjut lihat [FAQ Kode Perilaku](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## AI yang Bertanggung Jawab

Microsoft berkomitmen untuk membantu pelanggan kami menggunakan produk AI secara bertanggung jawab, berbagi pembelajaran kami, dan membangun kemitraan yang didasarkan pada kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber daya ini dapat ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI yang bertanggung jawab didasarkan pada prinsip AI kami yaitu keadilan, keandalan dan keselamatan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model skala besar untuk bahasa alami, gambar, dan ucapan - seperti yang digunakan dalam contoh ini - berpotensi berperilaku dengan cara yang tidak adil, tidak dapat diandalkan, atau menyinggung, yang pada gilirannya dapat menyebabkan dampak buruk. Harap lihat [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk mengetahui risiko dan keterbatasan.

Pendekatan yang disarankan untuk mengurangi risiko ini adalah dengan menyertakan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen, mampu mendeteksi konten yang dihasilkan pengguna dan AI yang berbahaya dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi yang berbahaya. Kami juga memiliki Content Safety Studio interaktif yang memungkinkan Anda melihat, mengeksplorasi, dan mencoba contoh kode untuk mendeteksi konten berbahaya di berbagai modalitas. [Dokumentasi quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) memandu Anda melalui pembuatan permintaan ke layanan tersebut.

Aspek lain yang perlu diperhatikan adalah kinerja keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami menganggap kinerja berarti bahwa sistem bekerja sebagaimana Anda dan pengguna Anda harapkan, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai kinerja aplikasi keseluruhan Anda menggunakan [metrik kualitas generasi serta risiko dan keselamatan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan dataset uji atau target tertentu, keluaran dari aplikasi generatif AI Anda diukur secara kuantitatif dengan evaluator bawaan atau evaluator kustom pilihan Anda. Untuk memulai dengan prompt flow sdk untuk mengevaluasi sistem Anda, Anda dapat mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah Anda menjalankan evaluasi, Anda dapat [memvisualisasikan hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Merek Dagang

Proyek ini mungkin berisi merek dagang atau logo untuk proyek, produk, atau layanan. Penggunaan merek dagang atau logo Microsoft yang sah tunduk pada dan harus mengikuti
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Penggunaan merek dagang atau logo Microsoft dalam versi proyek yang dimodifikasi tidak boleh menimbulkan kebingungan atau menyiratkan sponsor oleh Microsoft.
Setiap penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika Anda mengalami kebuntuan atau memiliki pertanyaan tentang membangun aplikasi AI, bergabunglah:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika Anda memiliki masukan produk atau menemukan kesalahan saat membangun, kunjungi:

[![Forum Pengembang Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)