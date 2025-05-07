<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbc19abb46abfba90855f2b7bd01767",
  "translation_date": "2025-05-06T17:31:31+00:00",
  "source_file": "README.md",
  "language_code": "id"
}
-->
![Logo](../../../../../../imgs/logo.png)

# Co-op Translator: Otomatiskan Terjemahan Dokumentasi Pendidikan dengan Mudah

_Mudah mengotomatisasi terjemahan dokumentasi Anda ke berbagai bahasa untuk menjangkau audiens global._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Dukungan Bahasa Didukung oleh Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](./README.md) | [Vietnamese](../vi/README.md)


[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **Otomasi yang Kuat**: Sekarang dengan dukungan GitHub Actions! Terjemahkan dokumentasi Anda secara otomatis saat ada perubahan di repositori, menjaga semuanya tetap terbaru dengan mudah. [Pelajari lebih lanjut](../..).

## Model dan Layanan yang Didukung

| Tipe                  | Nama                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Jika layanan computer vision tidak tersedia, co-op translator akan beralih ke [Markdown-only mode](./getting_started/markdown-only-mode.md).

## Ikhtisar: Permudah Terjemahan Konten Pendidikan Anda

Hambatan bahasa sangat menghalangi akses ke sumber daya pendidikan yang berharga dan pengetahuan teknis bagi pelajar dan pengembang di seluruh dunia. Hal ini membatasi partisipasi dan memperlambat laju inovasi serta pembelajaran global.

**Co-op Translator** lahir dari kebutuhan untuk mengatasi proses terjemahan manual yang tidak efisien untuk seri pendidikan skala besar milik Microsoft (seperti panduan "For Beginners"). Alat ini berkembang menjadi sebuah tool yang mudah digunakan dan kuat, dirancang untuk menghilangkan hambatan tersebut bagi semua orang. Dengan menyediakan terjemahan otomatis berkualitas tinggi melalui CLI dan GitHub Actions, Co-op Translator memberdayakan pendidik, pelajar, peneliti, dan pengembang di seluruh dunia untuk berbagi dan mengakses pengetahuan tanpa batasan bahasa.

Lihat bagaimana Co-op Translator mengatur konten pendidikan yang sudah diterjemahkan:

![Contoh](../../../../../../imgs/translation-ex.png)

File Markdown dan teks gambar diterjemahkan secara otomatis dan diorganisasi dengan rapi ke dalam folder berdasarkan bahasa.

**Buka akses global ke konten pendidikan Anda dengan Co-op Translator hari ini!**

## Mendukung Akses Global untuk Sumber Belajar Microsoft

Co-op Translator membantu menjembatani kesenjangan bahasa untuk inisiatif pendidikan utama Microsoft, mengotomatiskan proses terjemahan untuk repositori yang melayani komunitas pengembang global. Contoh yang saat ini menggunakan Co-op Translator antara lain:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Fitur Utama

- **Terjemahan Otomatis**: Terjemahkan teks ke berbagai bahasa dengan mudah.
- **Integrasi GitHub Actions**: Otomatiskan terjemahan sebagai bagian dari pipeline CI/CD Anda.
- **Preservasi Markdown**: Pertahankan sintaks Markdown yang benar selama terjemahan.
- **Terjemahan Teks Gambar**: Ekstrak dan terjemahkan teks dalam gambar.
- **Teknologi LLM Canggih**: Gunakan model bahasa mutakhir untuk terjemahan berkualitas tinggi.
- **Integrasi Mudah**: Terhubung dengan lancar ke pengaturan proyek Anda yang sudah ada.
- **Permudah Lokalisasi**: Sederhanakan proses lokalisasi proyek Anda untuk pasar internasional.

## Cara Kerja

![Arsitektur](../../../../../../imgs/architecture_241019.png)

Co-op Translator mengambil file Markdown dan gambar dari folder proyek Anda dan memprosesnya sebagai berikut:

1. **Ekstraksi Teks**: Mengambil teks dari file Markdown dan, jika dikonfigurasi (misalnya dengan Azure Computer Vision), teks yang ada di dalam gambar.
1. **Terjemahan AI**: Mengirimkan teks yang diambil ke LLM yang dikonfigurasi (Azure OpenAI, OpenAI, dll.) untuk diterjemahkan.
1. **Menyimpan Hasil**: Menyimpan file Markdown dan gambar yang sudah diterjemahkan ke folder berdasarkan bahasa, sambil mempertahankan format asli.

## Memulai

Mulai dengan cepat menggunakan CLI atau atur otomatisasi penuh dengan GitHub Actions.

### Mulai Cepat: Command Line

Untuk memulai dengan cepat menggunakan command line:

1. Instal paket:
    ```bash
    pip install co-op-translator
    ```
2. Konfigurasikan Kredensial:
  - Buat file `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` flag:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Ganti `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) di repositori Anda. Tidak perlu instalasi lokal.
- Panduan:
  - [GitHub Actions Guide (Public Repositories & Standard Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Gunakan ini untuk sebagian besar repositori publik atau pribadi yang mengandalkan secrets standar repositori.
  - [GitHub Actions Guide (Microsoft Organization Repos & Org-Level Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Gunakan panduan ini jika Anda bekerja dalam organisasi GitHub Microsoft atau perlu memanfaatkan secrets atau runner tingkat organisasi.

> [!NOTE]
> Meskipun tutorial ini fokus pada sumber daya Azure, Anda dapat menggunakan model bahasa apa pun yang didukung dari daftar [supported models and services](../..).

### Pemecahan Masalah dan Tips

- [Panduan Pemecahan Masalah](./getting_started/troubleshooting.md)

### Sumber Tambahan

- [Referensi Perintah](./getting_started/command-reference.md): Panduan lengkap untuk semua perintah dan opsi yang tersedia.
- [Pengaturan Dukungan Multi-bahasa](./getting_started/multi-language-support.md): Cara menambahkan tabel yang menautkan ke versi terjemahan di README Anda.
- [Bahasa yang Didukung](./getting_started/supported-languages.md): Periksa daftar bahasa yang didukung dan petunjuk untuk menambah bahasa baru.
- [Mode Markdown-Only](./getting_started/markdown-only-mode.md): Cara menerjemahkan teks saja, tanpa terjemahan gambar.

## Presentasi Video

Pelajari lebih lanjut tentang Co-op Translator melalui presentasi kami _(Klik gambar di bawah untuk menonton di YouTube.)_:

- **Open at Microsoft**: Perkenalan singkat 18 menit dan panduan cepat tentang cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../../../../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Panduan rinci satu jam langkah demi langkah yang mencakup segala hal mulai dari memahami apa itu Co-op Translator, pengaturan alat, penggunaannya secara efektif, hingga demo langsung yang menunjukkan kemampuannya.

  [![Microsoft Reactor](../../../../../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Dukung Kami dan Dorong Pembelajaran Global

Bergabunglah dengan kami dalam merevolusi cara konten pendidikan dibagikan secara global! Berikan [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ di GitHub dan dukung misi kami untuk menghapus hambatan bahasa dalam pembelajaran dan teknologi. Ketertarikan dan kontribusi Anda sangat berarti! Kontribusi kode dan saran fitur selalu diterima.


## Kontribusi

Proyek ini menyambut kontribusi dan saran. Tertarik berkontribusi ke Azure Co-op Translator? Silakan lihat [CONTRIBUTING.md](./CONTRIBUTING.md) untuk panduan tentang bagaimana Anda dapat membantu membuat Co-op Translator lebih mudah diakses.

## Kontributor

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kode Etik

Proyek ini telah mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk informasi lebih lanjut lihat [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## AI yang Bertanggung Jawab

Microsoft berkomitmen membantu pelanggan menggunakan produk AI kami secara bertanggung jawab, berbagi pembelajaran, dan membangun kemitraan berbasis kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber daya ini dapat ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI yang bertanggung jawab didasarkan pada prinsip AI kami yaitu keadilan, keandalan dan keselamatan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model bahasa, gambar, dan suara berskala besar - seperti yang digunakan dalam contoh ini - berpotensi berperilaku tidak adil, tidak dapat diandalkan, atau menyinggung, yang pada gilirannya dapat menyebabkan kerugian. Harap lihat [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk informasi tentang risiko dan keterbatasan.
Pendekatan yang disarankan untuk mengurangi risiko ini adalah dengan memasukkan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen, mampu mendeteksi konten yang berbahaya yang dibuat oleh pengguna maupun AI dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi yang berbahaya. Kami juga memiliki Content Safety Studio interaktif yang memungkinkan Anda melihat, menjelajahi, dan mencoba contoh kode untuk mendeteksi konten berbahaya di berbagai modalitas. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) akan memandu Anda dalam membuat permintaan ke layanan tersebut.

Aspek lain yang perlu diperhatikan adalah performa keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami mengartikan performa sebagai sistem yang berjalan sesuai dengan harapan Anda dan pengguna, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai performa aplikasi Anda secara keseluruhan menggunakan [metrik kualitas generasi serta risiko dan keamanan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan menggunakan dataset uji atau target tertentu, generasi aplikasi AI generatif Anda diukur secara kuantitatif dengan evaluator bawaan atau evaluator kustom pilihan Anda. Untuk memulai dengan prompt flow sdk dalam mengevaluasi sistem Anda, Anda dapat mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah Anda menjalankan evaluasi, Anda dapat [memvisualisasikan hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Proyek ini mungkin mengandung merek dagang atau logo untuk proyek, produk, atau layanan. Penggunaan merek dagang atau logo Microsoft yang sah harus mematuhi dan mengikuti [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Penggunaan merek dagang atau logo Microsoft dalam versi modifikasi dari proyek ini tidak boleh menimbulkan kebingungan atau menyiratkan dukungan dari Microsoft. Setiap penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah dan otoritatif. Untuk informasi yang sangat penting, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.