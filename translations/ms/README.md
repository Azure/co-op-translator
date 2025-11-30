<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:52:24+00:00",
  "source_file": "README.md",
  "language_code": "ms"
}
-->
# Penterjemah Kerjasama

_Mudah mengautomasikan terjemahan kandungan pendidikan GitHub anda ke dalam pelbagai bahasa untuk mencapai audiens global._

[![Pakej Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Lesen: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Muat Turun](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Muat Turun](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Kontena: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Gaya kod: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Penyumbang GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Isu GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Permintaan tarik GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Dialu-alukan](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Sokongan Pelbagai Bahasa

#### Disokong oleh [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Bahasa Burma (Myanmar)](../my/README.md) | [Cina (Ringkas)](../zh/README.md) | [Cina (Tradisional, Hong Kong)](../hk/README.md) | [Cina (Tradisional, Macau)](../mo/README.md) | [Cina (Tradisional, Taiwan)](../tw/README.md) | [Kroasia](../hr/README.md) | [Czech](../cs/README.md) | [Denmark](../da/README.md) | [Belanda](../nl/README.md) | [Estonia](../et/README.md) | [Finland](../fi/README.md) | [Perancis](../fr/README.md) | [Jerman](../de/README.md) | [Greek](../el/README.md) | [Ibrani](../he/README.md) | [Hindi](../hi/README.md) | [Hungary](../hu/README.md) | [Indonesia](../id/README.md) | [Itali](../it/README.md) | [Jepun](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Lithuania](../lt/README.md) | [Melayu](./README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin Nigeria](../pcm/README.md) | [Norway](../no/README.md) | [Parsi (Farsi)](../fa/README.md) | [Poland](../pl/README.md) | [Portugis (Brazil)](../br/README.md) | [Portugis (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Rusia](../ru/README.md) | [Serbia (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenia](../sl/README.md) | [Sepanyol](../es/README.md) | [Swahili](../sw/README.md) | [Sweden](../sv/README.md) | [Tagalog (Filipina)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turki](../tr/README.md) | [Ukraine](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Pengikut GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Bintang GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Buka dalam GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Gambaran Keseluruhan

**Co-op Translator** membantu anda melokalkan kandungan pendidikan GitHub anda ke dalam pelbagai bahasa dengan mudah.
Apabila anda mengemas kini fail Markdown, imej, atau buku nota anda, terjemahan akan diselaraskan secara automatik, memastikan kandungan anda sentiasa tepat dan terkini untuk pelajar di seluruh dunia.

Contoh bagaimana kandungan terjemahan disusun:

![Contoh](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ms.png)

## Mula dengan cepat

```bash
# Cipta dan aktifkan persekitaran maya (disyorkan)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Pasang pakej
pip install co-op-translator
# Terjemah
translate -l "ko ja fr" -md
```

Docker:

```bash
# Tarik imej awam dari GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Jalankan dengan folder semasa dipasang dan .env disediakan (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Persediaan minimum

1. Buat fail `.env` menggunakan templat: [.env.template](../../.env.template)
2. Konfigurasikan satu penyedia LLM (Azure OpenAI atau OpenAI)
3. (Pilihan) Untuk terjemahan imej (`-img`), konfigurasikan Azure AI Vision
4. (Disyorkan) Bersihkan sebarang terjemahan terdahulu untuk mengelakkan konflik (contoh: `translations/`)
5. (Disyorkan) Tambah bahagian terjemahan ke README anda menggunakan [templat bahasa README](./getting_started/README_languages_template.md)
6. Lihat: [Sediakan Azure AI](./getting_started/set-up-azure-ai.md)

## Cara penggunaan

Terjemah semua jenis yang disokong:

```bash
translate -l "ko ja"
```

Hanya Markdown:

```bash
translate -l "de" -md
```

Markdown + imej:

```bash
translate -l "pt" -md -img
```

Hanya buku nota:

```bash
translate -l "zh" -nb
```

Lebih banyak bendera: [Rujukan arahan](./getting_started/command-reference.md)

## Ciri-ciri

- Terjemahan automatik untuk Markdown, buku nota, dan imej
- Menyelaraskan terjemahan dengan perubahan sumber
- Berfungsi secara tempatan (CLI) atau dalam CI (GitHub Actions)
- Menggunakan Azure OpenAI atau OpenAI; pilihan Azure AI Vision untuk imej
- Mengekalkan format dan struktur Markdown

## Dokumentasi

- [Panduan baris arahan](./getting_started/command-line-guide/command-line-guide.md)
- [Panduan GitHub Actions (Repositori awam & rahsia standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Panduan GitHub Actions (Repositori organisasi Microsoft & persediaan peringkat organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Templat bahasa README](./getting_started/README_languages_template.md)
- [Bahasa yang disokong](./getting_started/supported-languages.md)
- [Menyumbang](./CONTRIBUTING.md)
- [Penyelesaian masalah](./getting_started/troubleshooting.md)

### Panduan khusus Microsoft
> [!NOTE]
> Untuk penyelenggara repositori “Untuk Pemula” Microsoft sahaja.

- [Mengemas kini senarai “kursus lain” (untuk repositori MS Pemula sahaja)](./getting_started/update-other-courses.md)

## Sokong kami dan galakkan pembelajaran global

Sertai kami dalam merevolusikan cara kandungan pendidikan dikongsi secara global! Berikan [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ di GitHub dan sokong misi kami untuk meruntuhkan halangan bahasa dalam pembelajaran dan teknologi. Minat dan sumbangan anda memberi impak besar! Sumbangan kod dan cadangan ciri sentiasa dialu-alukan.

### Terokai kandungan pendidikan Microsoft dalam bahasa anda

- [AZD untuk Pemula](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI untuk Pemula](https://github.com/microsoft/edgeai-for-beginners)
- [Protokol Konteks Model (MCP) Untuk Pemula](https://github.com/microsoft/mcp-for-beginners)
- [Ejen AI untuk Pemula](https://github.com/microsoft/ai-agents-for-beginners)
- [AI Generatif untuk Pemula menggunakan .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [AI Generatif untuk Pemula](https://github.com/microsoft/generative-ai-for-beginners)
- [AI Generatif untuk Pemula menggunakan Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML untuk Pemula](https://aka.ms/ml-beginners)
- [Sains Data untuk Pemula](https://aka.ms/datascience-beginners)
- [AI untuk Pemula](https://aka.ms/ai-beginners)
- [Keselamatan Siber untuk Pemula](https://github.com/microsoft/Security-101)
- [Pembangunan Web untuk Pemula](https://aka.ms/webdev-beginners)
- [IoT untuk Pemula](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Persembahan video

👉 Klik imej di bawah untuk menonton di YouTube.

- **Open at Microsoft**: Pengenalan ringkas selama 18 minit dan panduan cepat cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ms.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Berminat untuk menyumbang kepada Azure Co-op Translator? Sila lihat [CONTRIBUTING.md](./CONTRIBUTING.md) kami untuk panduan bagaimana anda boleh membantu menjadikan Co-op Translator lebih mudah diakses.

## Penyumbang

[![penyumbang co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod Etika

Projek ini telah mengamalkan [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut, lihat [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## AI Bertanggungjawab

Microsoft komited untuk membantu pelanggan kami menggunakan produk AI kami secara bertanggungjawab, berkongsi pembelajaran kami, dan membina perkongsian berasaskan kepercayaan melalui alat seperti Nota Ketelusan dan Penilaian Impak. Banyak sumber ini boleh didapati di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI bertanggungjawab berasaskan prinsip AI kami iaitu keadilan, kebolehpercayaan dan keselamatan, privasi dan keselamatan, keterangkuman, ketelusan, dan akauntabiliti.

Model bahasa semula jadi, imej, dan ucapan berskala besar - seperti yang digunakan dalam contoh ini - berpotensi berkelakuan secara tidak adil, tidak boleh dipercayai, atau menyinggung, yang boleh menyebabkan kemudaratan. Sila rujuk [Nota Ketelusan perkhidmatan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk maklumat tentang risiko dan had.
Pendekatan yang disyorkan untuk mengurangkan risiko ini adalah dengan memasukkan sistem keselamatan dalam seni bina anda yang dapat mengesan dan menghalang tingkah laku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan bebas, yang mampu mengesan kandungan berbahaya yang dihasilkan oleh pengguna dan AI dalam aplikasi dan perkhidmatan. Azure AI Content Safety merangkumi API teks dan imej yang membolehkan anda mengesan bahan yang berbahaya. Kami juga mempunyai Content Safety Studio interaktif yang membolehkan anda melihat, meneroka dan mencuba kod contoh untuk mengesan kandungan berbahaya merentasi pelbagai modaliti. Dokumentasi [quickstart berikut](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) membimbing anda melalui cara membuat permintaan kepada perkhidmatan tersebut.

Satu lagi aspek yang perlu diambil kira adalah prestasi keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami menganggap prestasi bermaksud sistem berfungsi seperti yang anda dan pengguna anda jangkakan, termasuk tidak menghasilkan output yang berbahaya. Adalah penting untuk menilai prestasi keseluruhan aplikasi anda menggunakan [kualiti generasi dan metrik risiko serta keselamatan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda boleh menilai aplikasi AI anda dalam persekitaran pembangunan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dengan dataset ujian atau sasaran, generasi aplikasi AI generatif anda diukur secara kuantitatif dengan penilai terbina dalam atau penilai tersuai pilihan anda. Untuk memulakan dengan prompt flow sdk bagi menilai sistem anda, anda boleh mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah anda menjalankan penilaian, anda boleh [memvisualisasikan keputusan dalam Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tanda Dagangan

Projek ini mungkin mengandungi tanda dagangan atau logo untuk projek, produk, atau perkhidmatan. Penggunaan tanda dagangan atau logo Microsoft yang dibenarkan tertakluk kepada dan mesti mengikuti [Garis Panduan Tanda Dagangan & Jenama Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Penggunaan tanda dagangan atau logo Microsoft dalam versi projek yang diubah suai tidak boleh menyebabkan kekeliruan atau memberi gambaran bahawa Microsoft menaja. Sebarang penggunaan tanda dagangan atau logo pihak ketiga tertakluk kepada polisi pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika anda menghadapi kesukaran atau mempunyai sebarang soalan mengenai pembinaan aplikasi AI, sertai:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika anda mempunyai maklum balas produk atau menemui ralat semasa membina, lawati:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->