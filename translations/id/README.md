<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:48:35+00:00",
  "source_file": "README.md",
  "language_code": "id"
}
-->
# Co-op Translator

_Mudah mengotomatiskan terjemahan konten edukasi GitHub Anda ke berbagai bahasa untuk menjangkau audiens global._

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
[Arab](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Cina (Sederhana)](../zh/README.md) | [Cina (Tradisional, Hong Kong)](../hk/README.md) | [Cina (Tradisional, Macau)](../mo/README.md) | [Cina (Tradisional, Taiwan)](../tw/README.md) | [Kroasia](../hr/README.md) | [Ceko](../cs/README.md) | [Denmark](../da/README.md) | [Belanda](../nl/README.md) | [Estonia](../et/README.md) | [Finlandia](../fi/README.md) | [Prancis](../fr/README.md) | [Jerman](../de/README.md) | [Yunani](../el/README.md) | [Ibrani](../he/README.md) | [Hindi](../hi/README.md) | [Hungaria](../hu/README.md) | [Indonesia](./README.md) | [Italia](../it/README.md) | [Jepang](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Lituania](../lt/README.md) | [Melayu](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin Nigeria](../pcm/README.md) | [Norwegia](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Polandia](../pl/README.md) | [Portugis (Brasil)](../br/README.md) | [Portugis (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumania](../ro/README.md) | [Rusia](../ru/README.md) | [Serbia (Sirilik)](../sr/README.md) | [Slovakia](../sk/README.md) | [Slovenia](../sl/README.md) | [Spanyol](../es/README.md) | [Swahili](../sw/README.md) | [Swedia](../sv/README.md) | [Tagalog (Filipina)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ikhtisar

**Co-op Translator** membantu Anda melokalisasi konten edukasi GitHub ke berbagai bahasa dengan mudah.  
Saat Anda memperbarui file Markdown, gambar, atau notebook, terjemahan akan otomatis tersinkronisasi, memastikan konten Anda tetap akurat dan terbaru untuk para pembelajar di seluruh dunia.

Contoh bagaimana konten terjemahan diatur:

![Contoh](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.id.png)

## Memulai dengan cepat

```bash
# Buat dan aktifkan lingkungan virtual (disarankan)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instal paket
pip install co-op-translator
# Terjemahkan
translate -l "ko ja fr" -md
```
  
Docker:

```bash
# Tarik gambar publik dari GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Jalankan dengan folder saat ini dipasang dan .env disediakan (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```
  
## Pengaturan minimal

1. Buat file `.env` menggunakan template: [.env.template](../../.env.template)  
2. Konfigurasikan satu penyedia LLM (Azure OpenAI atau OpenAI)  
3. (Opsional) Untuk terjemahan gambar (`-img`), konfigurasikan Azure AI Vision  
4. (Disarankan) Bersihkan terjemahan sebelumnya untuk menghindari konflik (misal: `translations/`)  
5. (Disarankan) Tambahkan bagian terjemahan ke README Anda menggunakan [template bahasa README](./getting_started/README_languages_template.md)  
6. Lihat: [Menyiapkan Azure AI](./getting_started/set-up-azure-ai.md)

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
  
Flag lainnya: [Referensi perintah](./getting_started/command-reference.md)

## Fitur

- Terjemahan otomatis untuk Markdown, notebook, dan gambar  
- Menjaga terjemahan tetap sinkron dengan perubahan sumber  
- Bisa dijalankan secara lokal (CLI) atau di CI (GitHub Actions)  
- Menggunakan Azure OpenAI atau OpenAI; opsional Azure AI Vision untuk gambar  
- Mempertahankan format dan struktur Markdown

## Dokumentasi

- [Panduan baris perintah](./getting_started/command-line-guide/command-line-guide.md)  
- [Panduan GitHub Actions (Repositori publik & rahasia standar)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Panduan GitHub Actions (Repositori organisasi Microsoft & pengaturan tingkat organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Template bahasa README](./getting_started/README_languages_template.md)  
- [Bahasa yang didukung](./getting_started/supported-languages.md)  
- [Kontribusi](./CONTRIBUTING.md)  
- [Pemecahan masalah](./getting_started/troubleshooting.md)

### Panduan khusus Microsoft
> [!NOTE]  
> Untuk pemelihara repositori “For Beginners” Microsoft saja.

- [Memperbarui daftar “kursus lain” (hanya untuk repositori MS Beginners)](./getting_started/update-other-courses.md)

## Dukung kami dan dorong pembelajaran global

Bergabunglah bersama kami dalam merevolusi cara konten edukasi dibagikan secara global! Berikan ⭐ pada [Co-op Translator](https://github.com/azure/co-op-translator) di GitHub dan dukung misi kami untuk menghilangkan hambatan bahasa dalam pembelajaran dan teknologi. Minat dan kontribusi Anda sangat berarti! Kontribusi kode dan saran fitur selalu kami sambut.

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

## Presentasi video

👉 Klik gambar di bawah untuk menonton di YouTube.

- **Open at Microsoft**: Perkenalan singkat 18 menit dan panduan cepat cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.id.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Kontribusi

Proyek ini menyambut kontribusi dan saran. Tertarik berkontribusi pada Azure Co-op Translator? Silakan lihat [CONTRIBUTING.md](./CONTRIBUTING.md) untuk panduan bagaimana Anda bisa membantu membuat Co-op Translator lebih mudah diakses.

## Kontributor

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kode Etik

Proyek ini mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Untuk informasi lebih lanjut lihat [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/) atau  
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## AI yang Bertanggung Jawab

Microsoft berkomitmen membantu pelanggan menggunakan produk AI kami secara bertanggung jawab, berbagi pembelajaran, dan membangun kemitraan berbasis kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber daya ini dapat ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).  
Pendekatan Microsoft terhadap AI yang bertanggung jawab didasarkan pada prinsip AI kami yaitu keadilan, keandalan dan keselamatan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model bahasa alami, gambar, dan suara berskala besar - seperti yang digunakan dalam contoh ini - berpotensi berperilaku tidak adil, tidak dapat diandalkan, atau menyinggung, yang dapat menyebabkan kerugian. Silakan lihat [catatan transparansi layanan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk informasi tentang risiko dan keterbatasan.
Pendekatan yang direkomendasikan untuk mengurangi risiko ini adalah dengan menyertakan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen yang mampu mendeteksi konten berbahaya yang dibuat oleh pengguna maupun AI dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi yang berbahaya. Kami juga memiliki Content Safety Studio interaktif yang memungkinkan Anda melihat, menjelajahi, dan mencoba contoh kode untuk mendeteksi konten berbahaya di berbagai modalitas. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) akan memandu Anda dalam membuat permintaan ke layanan ini.

Aspek lain yang perlu diperhatikan adalah kinerja keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami mengartikan kinerja sebagai sistem yang berjalan sesuai dengan harapan Anda dan pengguna, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai kinerja aplikasi Anda secara keseluruhan menggunakan [metrik kualitas generasi serta risiko dan keamanan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan menggunakan dataset uji atau target tertentu, hasil generasi aplikasi AI generatif Anda diukur secara kuantitatif dengan evaluator bawaan atau evaluator kustom pilihan Anda. Untuk memulai menggunakan prompt flow SDK dalam mengevaluasi sistem Anda, Anda dapat mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah menjalankan evaluasi, Anda dapat [memvisualisasikan hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Merek Dagang

Proyek ini mungkin berisi merek dagang atau logo untuk proyek, produk, atau layanan. Penggunaan merek dagang atau logo Microsoft yang sah harus mematuhi dan mengikuti [Pedoman Merek Dagang & Merek Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Penggunaan merek dagang atau logo Microsoft dalam versi modifikasi dari proyek ini tidak boleh menimbulkan kebingungan atau menyiratkan dukungan dari Microsoft.  
Setiap penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika Anda mengalami kesulitan atau memiliki pertanyaan tentang membangun aplikasi AI, bergabunglah dengan:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika Anda memiliki masukan produk atau menemukan kesalahan saat membangun, kunjungi:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->