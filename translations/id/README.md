<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:37:17+00:00",
  "source_file": "README.md",
  "language_code": "id"
}
-->
# Co-op Translator

_Otomatisasi penerjemahan konten edukasi GitHub Anda ke berbagai bahasa dengan mudah untuk menjangkau audiens global._

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

### 🌐 Dukungan Multi-Bahasa

#### Didukung oleh [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](./README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ringkasan

**Co-op Translator** memudahkan Anda menerjemahkan konten edukasi GitHub ke berbagai bahasa dengan cepat, sehingga Anda bisa menjangkau audiens global tanpa repot. Setiap kali Anda memperbarui file Markdown, gambar, atau notebook Jupyter, hasil terjemahan akan otomatis disinkronkan agar konten edukasi Anda tetap segar dan relevan untuk pengguna internasional.

Lihat bagaimana Co-op Translator mengatur konten edukasi GitHub yang sudah diterjemahkan:

![Contoh](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.id.png)

## Mulai Cepat

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Pengaturan Minimal

- Buat file `.env` menggunakan template: [.env.template](../../.env.template)
- Konfigurasikan satu penyedia LLM (Azure OpenAI atau OpenAI)
- Untuk terjemahan gambar (`-img`), aktifkan juga Azure AI Vision
- Rekomendasi: Jika Anda punya hasil terjemahan dari alat lain, bersihkan dulu agar tidak terjadi konflik (misal: `translations/`).
- Rekomendasi: Tambahkan bagian terjemahan ke README Anda menggunakan [template bahasa README](./README_languages_template.md)
- Lihat: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Penggunaan

Terjemahkan semua tipe yang didukung:

```bash
translate -l "ko ja"
```

Hanya Markdown:

```bash
translate -l "de" -md
```

Markdown + gambar:

```bash
translate -l "pt" -md -img
```

Hanya notebook:

```bash
translate -l "zh" -nb
```

Opsi lainnya: [Referensi perintah](./getting_started/command-reference.md)

## Fitur

- Terjemahan otomatis untuk Markdown, notebook, dan gambar
- Menjaga hasil terjemahan tetap sinkron dengan perubahan sumber
- Bisa dijalankan lokal (CLI) atau di CI (GitHub Actions)
- Menggunakan Azure OpenAI atau OpenAI; Azure AI Vision opsional untuk gambar
- Format dan struktur Markdown tetap terjaga

## Dokumentasi

- [Panduan command-line](./getting_started/command-line-guide/command-line-guide.md)
- [Panduan GitHub Actions (Repositori publik & secrets standar)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Panduan GitHub Actions (Repositori organisasi Microsoft & setup level organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Bahasa yang didukung](./getting_started/supported-languages.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

## Dukung Kami dan Majukan Pembelajaran Global

Bergabunglah bersama kami untuk merevolusi cara berbagi konten edukasi secara global! Berikan ⭐ untuk [Co-op Translator](https://github.com/azure/co-op-translator) di GitHub dan dukung misi kami untuk menghapus hambatan bahasa dalam pembelajaran dan teknologi. Minat dan kontribusi Anda sangat berarti! Kontribusi kode dan saran fitur selalu terbuka.

### Jelajahi konten edukasi Microsoft dalam bahasa Anda

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

## Presentasi Video

Pelajari lebih lanjut tentang Co-op Translator melalui presentasi kami _(Klik gambar di bawah untuk menonton di YouTube.)_:

- **Open at Microsoft**: Pengantar singkat selama 18 menit dan panduan cepat menggunakan Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.id.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Kontribusi

Proyek ini terbuka untuk kontribusi dan saran. Tertarik berkontribusi ke Azure Co-op Translator? Silakan lihat [CONTRIBUTING.md](./CONTRIBUTING.md) untuk panduan cara membantu agar Co-op Translator makin mudah diakses.

## Kontributor

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kode Etik

Proyek ini mengikuti [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk info lebih lanjut, lihat [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## AI yang Bertanggung Jawab

Microsoft berkomitmen membantu pelanggan menggunakan produk AI kami secara bertanggung jawab, membagikan pembelajaran kami, dan membangun kemitraan berbasis kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber daya ini bisa ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI yang bertanggung jawab didasarkan pada prinsip AI kami: keadilan, keandalan dan keamanan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model bahasa, gambar, dan suara berskala besar—seperti yang digunakan dalam contoh ini—bisa saja berperilaku tidak adil, tidak dapat diandalkan, atau menyinggung, sehingga berpotensi menimbulkan dampak negatif. Silakan baca [catatan transparansi layanan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk memahami risiko dan keterbatasannya.

Cara yang disarankan untuk mengurangi risiko ini adalah dengan menambahkan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen, mampu mendeteksi konten berbahaya yang dibuat pengguna maupun AI dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi berbahaya. Kami juga menyediakan Content Safety Studio interaktif untuk melihat, mengeksplorasi, dan mencoba kode contoh mendeteksi konten berbahaya di berbagai jenis data. [Dokumentasi quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) akan memandu Anda membuat permintaan ke layanan tersebut.
Aspek lain yang perlu diperhatikan adalah performa aplikasi secara keseluruhan. Pada aplikasi multi-modal dan multi-model, performa berarti sistem berjalan sesuai harapan Anda dan pengguna, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai performa aplikasi Anda secara keseluruhan menggunakan [metrik kualitas generasi serta risiko dan keamanan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan memberikan dataset uji atau target, hasil generasi aplikasi AI generatif Anda akan diukur secara kuantitatif menggunakan evaluator bawaan atau evaluator kustom pilihan Anda. Untuk memulai menggunakan prompt flow sdk dalam mengevaluasi sistem Anda, Anda dapat mengikuti [panduan cepat](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah Anda menjalankan evaluasi, Anda dapat [memvisualisasikan hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Merek Dagang

Proyek ini mungkin memuat merek dagang atau logo untuk proyek, produk, atau layanan tertentu. Penggunaan merek dagang atau logo Microsoft yang sah harus mengikuti [Panduan Merek Dagang & Merek Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Penggunaan merek dagang atau logo Microsoft pada versi modifikasi dari proyek ini tidak boleh menimbulkan kebingungan atau mengesankan adanya sponsor dari Microsoft. Setiap penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika Anda mengalami kesulitan atau memiliki pertanyaan tentang membangun aplikasi AI, bergabunglah di:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jika Anda memiliki masukan produk atau menemukan kesalahan saat membangun, kunjungi:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer (Penafian)**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang paling otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul akibat penggunaan terjemahan ini.