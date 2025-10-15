<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:39:43+00:00",
  "source_file": "README.md",
  "language_code": "ms"
}
-->
# Co-op Translator

_Automatikkan terjemahan kandungan pendidikan GitHub anda ke pelbagai bahasa dengan mudah untuk menjangkau audiens global._

### 🌐 Sokongan Pelbagai Bahasa

#### Disokong oleh [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Cina (Ringkas)](../zh/README.md) | [Cina (Tradisional, Hong Kong)](../hk/README.md) | [Cina (Tradisional, Macau)](../mo/README.md) | [Cina (Tradisional, Taiwan)](../tw/README.md) | [Croatia](../hr/README.md) | [Czech](../cs/README.md) | [Denmark](../da/README.md) | [Belanda](../nl/README.md) | [Estonia](../et/README.md) | [Finland](../fi/README.md) | [Perancis](../fr/README.md) | [Jerman](../de/README.md) | [Greek](../el/README.md) | [Ibrani](../he/README.md) | [Hindi](../hi/README.md) | [Hungary](../hu/README.md) | [Indonesia](../id/README.md) | [Itali](../it/README.md) | [Jepun](../ja/README.md) | [Korea](../ko/README.md) | [Lithuania](../lt/README.md) | [Melayu](./README.md) | [Marathi](../mr/README.md) | [Nepal](../ne/README.md) | [Norway](../no/README.md) | [Parsi (Farsi)](../fa/README.md) | [Poland](../pl/README.md) | [Portugis (Brazil)](../br/README.md) | [Portugis (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Rusia](../ru/README.md) | [Serbia (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenia](../sl/README.md) | [Sepanyol](../es/README.md) | [Swahili](../sw/README.md) | [Sweden](../sv/README.md) | [Tagalog (Filipina)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turki](../tr/README.md) | [Ukraine](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Pengenalan

**Co-op Translator** membolehkan anda menterjemah kandungan pendidikan GitHub anda ke pelbagai bahasa dengan pantas, memudahkan anda menjangkau audiens global. Apabila anda mengemas kini fail Markdown, imej, atau Jupyter notebook anda, terjemahan akan diselaraskan secara automatik supaya kandungan pendidikan GitHub anda sentiasa terkini dan relevan untuk pengguna antarabangsa.

Lihat bagaimana Co-op Translator mengatur kandungan pendidikan GitHub yang telah diterjemah:

![Contoh](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ms.png)

## Mula Pantas

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

## Persediaan Minimum

- Cipta fail `.env` menggunakan templat: [.env.template](../../.env.template)
- Konfigurasikan satu penyedia LLM (Azure OpenAI atau OpenAI)
- Untuk terjemahan imej (`-img`), tetapkan juga Azure AI Vision
- Disyorkan: Jika anda mempunyai terjemahan yang dijana oleh alat lain, bersihkan dahulu untuk elak konflik (contoh: `translations/`).
- Disyorkan: Tambah seksyen terjemahan ke README anda menggunakan [templat bahasa README](./README_languages_template.md)
- Lihat: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Cara Guna

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

Hanya notebook:

```bash
translate -l "zh" -nb
```

Lebih banyak flag: [Rujukan arahan](./getting_started/command-reference.md)

## Ciri-ciri

- Terjemahan automatik untuk Markdown, notebook, dan imej
- Menyelaraskan terjemahan dengan perubahan sumber
- Berfungsi secara setempat (CLI) atau dalam CI (GitHub Actions)
- Menggunakan Azure OpenAI atau OpenAI; Azure AI Vision untuk imej (pilihan)
- Mengekalkan format dan struktur Markdown

## Dokumentasi

- [Panduan baris arahan](./getting_started/command-line-guide/command-line-guide.md)
- [Panduan GitHub Actions (Repositori awam & secrets standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Panduan GitHub Actions (Repositori organisasi Microsoft & persediaan tahap organisasi)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Bahasa yang disokong](./getting_started/supported-languages.md)
- [Penyelesaian masalah](./getting_started/troubleshooting.md)

## Sokong Kami dan Galakkan Pembelajaran Global

Sertai kami dalam merevolusikan cara kandungan pendidikan dikongsi di seluruh dunia! Beri [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ di GitHub dan sokong misi kami untuk meruntuhkan halangan bahasa dalam pembelajaran dan teknologi. Minat dan sumbangan anda sangat bermakna! Sumbangan kod dan cadangan ciri sentiasa dialu-alukan.

### Terokai kandungan pendidikan Microsoft dalam bahasa anda

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

## Pembentangan Video

Ketahui lebih lanjut tentang Co-op Translator melalui pembentangan kami _(Klik imej di bawah untuk menonton di YouTube.)_:

- **Open at Microsoft**: Pengenalan ringkas selama 18 minit dan panduan pantas cara menggunakan Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ms.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Berminat untuk menyumbang kepada Azure Co-op Translator? Sila rujuk [CONTRIBUTING.md](./CONTRIBUTING.md) untuk panduan bagaimana anda boleh membantu menjadikan Co-op Translator lebih mudah diakses.

## Penyumbang

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod Etika

Projek ini mengguna pakai [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut, lihat [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## AI Bertanggungjawab

Microsoft komited untuk membantu pelanggan menggunakan produk AI kami secara bertanggungjawab, berkongsi pembelajaran kami, dan membina kerjasama berasaskan kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak sumber ini boleh didapati di [https://aka.ms/RAI](https://aka.ms/RAI).
Pendekatan Microsoft terhadap AI bertanggungjawab berasaskan prinsip AI kami iaitu keadilan, kebolehpercayaan dan keselamatan, privasi dan keselamatan, keterangkuman, ketelusan, dan akauntabiliti.

Model bahasa semula jadi, imej, dan pertuturan berskala besar - seperti yang digunakan dalam sampel ini - berpotensi berkelakuan secara tidak adil, tidak boleh dipercayai, atau menyinggung, yang boleh menyebabkan kemudaratan. Sila rujuk [nota ketelusan Azure OpenAI service](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk maklumat tentang risiko dan had.

Pendekatan yang disyorkan untuk mengurangkan risiko ini ialah dengan memasukkan sistem keselamatan dalam seni bina anda yang boleh mengesan dan mencegah tingkah laku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan bebas, mampu mengesan kandungan berbahaya yang dijana pengguna dan AI dalam aplikasi dan perkhidmatan. Azure AI Content Safety merangkumi API teks dan imej yang membolehkan anda mengesan bahan yang berbahaya. Kami juga mempunyai Content Safety Studio interaktif yang membolehkan anda melihat, meneroka dan mencuba kod contoh untuk mengesan kandungan berbahaya merentasi pelbagai mod. [Dokumentasi mula pantas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) berikut membimbing anda membuat permintaan kepada perkhidmatan ini.
Satu lagi aspek yang perlu diambil kira ialah prestasi keseluruhan aplikasi. Untuk aplikasi multi-modal dan multi-model, prestasi bermaksud sistem berfungsi seperti yang anda dan pengguna anda harapkan, termasuk tidak menghasilkan output yang berbahaya. Adalah penting untuk menilai prestasi aplikasi anda secara keseluruhan menggunakan [metrik kualiti penjanaan serta risiko dan keselamatan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Anda boleh menilai aplikasi AI anda dalam persekitaran pembangunan menggunakan [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Sama ada anda menggunakan set data ujian atau sasaran tertentu, penjanaan aplikasi AI generatif anda akan diukur secara kuantitatif dengan penilai terbina dalam atau penilai tersuai pilihan anda. Untuk mula menggunakan prompt flow sdk bagi menilai sistem anda, anda boleh ikuti [panduan permulaan pantas](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Selepas anda menjalankan penilaian, anda boleh [visualisasikan hasilnya di Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tanda Dagangan

Projek ini mungkin mengandungi tanda dagangan atau logo untuk projek, produk, atau perkhidmatan. Penggunaan tanda dagangan atau logo Microsoft yang dibenarkan tertakluk kepada dan mesti mematuhi
[Panduan Tanda Dagangan & Jenama Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Penggunaan tanda dagangan atau logo Microsoft dalam versi projek yang diubah suai tidak boleh menyebabkan kekeliruan atau menyiratkan penajaan oleh Microsoft.
Sebarang penggunaan tanda dagangan atau logo pihak ketiga tertakluk kepada polisi pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika anda menghadapi masalah atau ada sebarang soalan tentang membina aplikasi AI, sertai:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Jika anda ada maklum balas produk atau menghadapi ralat semasa membina, lawati:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.