# Konfigurasi

Co-op Translator memerlukan satu pembekal model bahasa. Terjemahan imej juga memerlukan Azure AI Vision.

Konfigurasi dibaca dari pembolehubah persekitaran. Untuk projek tempatan, letakkan ia dalam fail `.env` di akar projek.

Untuk penyediaan sumber Azure, lihat [Persediaan Azure AI](azure-ai-setup.md).

## Persediaan runtime tempatan

Gunakan persekitaran maya sebelum menjalankan CLI secara tempatan. Co-op Translator menyokong Python 3.11 hingga 3.14.

Untuk penggunaan CLI biasa, pasang pakej yang diterbitkan di dalam persekitaran maya:

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

### Pembangunan repositori

Untuk pembangunan repositori, pasang kebergantungan dari akar projek sebaliknya:

```bash
poetry install
poetry run translate --help
```

Selepas CLI tersedia, konfigurasikan satu pembekal model bahasa dalam `.env`.

## Pemilihan pembekal

Alat ini mengesan pembekal secara automatik mengikut urutan ini:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Terjemahan memerlukan kelayakan pembekal, kecuali untuk pratonton seperti `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, dan `run_review` adalah operasi penyelenggaraan deterministik dan tidak memerlukan kelayakan pembekal.

## Backend klien model

Bermula dengan Co-op Translator 0.22.0, Azure OpenAI, OpenAI, dan Anthropic menggunakan Microsoft Agent Framework secara lalai. Tiada tetapan backend diperlukan untuk penggunaan biasa.

Semantic Kernel kekal tersedia sementara untuk keserasian. Untuk memilihnya secara jelas, tetapkan:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Menggunakan Semantic Kernel akan memancarkan amaran pemansuhan. Pakej ini dirancang untuk menjadikan Semantic Kernel sebagai pergantungan pilihan dalam 0.23.0 dan membuang integrasi dalam 0.24.0, tertakluk kepada keputusan keserasian dan maklum balas pengguna. Anthropic memerlukan `agent-framework`; memilih `semantic-kernel` secara nyata dengan Anthropic akan gagal dengan ralat konfigurasi. Nilai tidak sah akan gagal semasa inisialisasi penterjemah berasaskan pembekal dan bukannya beralih balik secara senyap. Ikuti pelancaran dan laporkan sekatan dalam [isu GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Gunakan Azure OpenAI apabila model anda dideploy dalam Azure AI Foundry atau Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Pemeriksaan keterhubungan menggunakan endpoint, kunci API, versi API, dan nama deployment sebelum terjemahan bermula.

## OpenAI

Gunakan OpenAI apabila memanggil API OpenAI secara langsung.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` diperlukan kerana penterjemah memerlukan model sembang yang jelas untuk panggilan API.

Biarkan `OPENAI_ORG_ID` dan `OPENAI_BASE_URL` tidak ditetapkan untuk konfigurasi lalai. Tambah ID organisasi hanya jika akaun anda memerlukannya, atau base URL hanya apabila menggunakan endpoint tersuai. Jangan salin nilai tempat letak untuk tetapan pilihan.

## Anthropic Claude

Gunakan Anthropic apabila memanggil API Claude secara langsung. Cipta [kunci API Anthropic](https://platform.claude.com/docs/en/get-started) dan pilih [ID model Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) yang disokong.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` dan `ANTHROPIC_MODEL` diperlukan. Anda tidak perlu menetapkan `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework adalah backend lalai.

Biarkan `ANTHROPIC_BASE_URL` tidak ditetapkan untuk API Anthropic. Tetapkannya hanya apabila menggunakan endpoint tersuai.

`ANTHROPIC_MAX_TOKENS` lalai kepada `8192`, yang memberikan ruang untuk skrip padat-token seperti Meitei Mayek. Kurangkan jika model anda atau endpoint yang serasi Anthropic mengehadkan output di bawah itu.

## Azure AI Vision

Terjemahan imej memerlukan Azure AI Vision supaya alat dapat mengekstrak teks dari imej sebelum model bahasa yang dikonfigurasikan menterjemahkannya. Anthropic boleh menterjemah teks yang diekstrak sama seperti Azure OpenAI atau OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jika terjemahan imej dipilih dengan `-img`, `images=True`, atau tiada penapis jenis kandungan, alat mengesahkan konfigurasi Vision sebelum terjemahan bermula.

## Berbilang set kelayakan

Lapisan konfigurasi menyokong berbilang set kelayakan dengan menambah sufiks pada pembolehubah dengan indeks yang sama:

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

Setiap set mesti lengkap. Pemeriksaan kesihatan memilih set yang berfungsi sebelum terjemahan diteruskan.

OpenAI dan Anthropic menyokong konvensyen sufiks yang sama. Simpan setiap pembolehubah dalam set kelayakan pada sufiks yang sama, termasuk nilai pilihan seperti `OPENAI_BASE_URL_1` atau `ANTHROPIC_BASE_URL_1`.

## Keperluan arahan

| Perintah atau API | LLM diperlukan | Vision diperlukan | Nota |
| --- | --- | --- | --- |
| `translate -md` | Ya | Tidak | Menterjemah Markdown sahaja. |
| `translate -nb` | Ya | Tidak | Menterjemah notebook sahaja. |
| `translate -img` | Ya | Ya | Menterjemah imej sahaja. |
| `translate` with no type flags | Ya | Ya | Mod lalai merangkumi Markdown, notebook, dan imej. |
| `evaluate` | Ya | Tidak | Menggunakan penilaian LLM melainkan `--fast` dipilih. |
| `migrate-links` | Tidak | Tidak | Melakukan migrasi pautan tempatan tanpa panggilan ke pembekal. |
| `co-op-review` | Tidak | Tidak | Menjalankan pemeriksaan struktur terjemahan deterministik, kesegaran, Markdown, notebook, dan pautan tempatan. |
| `run_translation(markdown=True)` | Ya | Tidak | Terjemahan Markdown secara programatik. |
| `run_translation(images=True)` | Ya | Ya | Terjemahan imej secara programatik. |
| `run_review(...)` | Tidak | Tidak | Semakan deterministik secara programatik. |

## Direktori output

Output terjemahan teks lalai:

```text
translations/<language-code>/<source-relative-path>
```

Output imej terjemahan lalai:

```text
translated_images/<language-code>/<source-relative-path>
```

API Python boleh menggantikan direktori ini dengan `translations_dir` dan `image_dir`.