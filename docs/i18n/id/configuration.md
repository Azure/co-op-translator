# Konfigurasi

Co-op Translator memerlukan satu penyedia model bahasa. Penerjemahan gambar juga membutuhkan Azure AI Vision.

Konfigurasi dibaca dari variabel lingkungan. Untuk proyek lokal, letakkan di file `.env` di root proyek.

Untuk penyiapan sumber daya Azure, lihat [Azure AI Setup](azure-ai-setup.md).

## Pengaturan runtime lokal

Gunakan lingkungan virtual sebelum menjalankan CLI secara lokal. Co-op Translator mendukung Python 3.11 hingga 3.14.

Untuk penggunaan CLI biasa, instal paket yang dipublikasikan di dalam lingkungan virtual:

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

### Pengembangan repositori

Untuk pengembangan repositori, instal dependensi dari root proyek sebagai gantinya:

```bash
poetry install
poetry run translate --help
```

Setelah CLI tersedia, konfigurasikan satu penyedia model bahasa di `.env`.

## Pemilihan penyedia

Alat ini mendeteksi penyedia secara otomatis dengan urutan berikut:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Penerjemahan memerlukan kredensial penyedia, kecuali untuk pratinjau seperti `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, dan `run_review` adalah operasi pemeliharaan deterministik dan tidak memerlukan kredensial penyedia.

## Backend klien model

Mulai Co-op Translator 0.22.0, Azure OpenAI, OpenAI, dan Anthropic menggunakan Microsoft Agent Framework secara default. Tidak diperlukan pengaturan backend untuk penggunaan normal.

Semantic Kernel tetap tersedia sementara untuk kompatibilitas. Untuk memilihnya secara eksplisit, atur:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Menggunakan Semantic Kernel akan menghasilkan peringatan deprecasi. Paket ini direncanakan untuk memindahkan Semantic Kernel menjadi dependensi opsional di 0.23.0 dan menghapus integrasi pada 0.24.0, tergantung hasil kompatibilitas dan umpan balik pengguna. Anthropic membutuhkan `agent-framework`; memilih `semantic-kernel` secara eksplisit dengan Anthropic akan gagal dengan kesalahan konfigurasi. Nilai yang tidak valid akan gagal selama inisialisasi penerjemah yang didukung penyedia alih-alih diam-diam kembali ke pengaturan lain. Ikuti peluncuran dan laporkan hambatan di [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Gunakan Azure OpenAI ketika model Anda dideploy di Azure AI Foundry atau Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Pemeriksaan konektivitas menggunakan endpoint, API key, versi API, dan nama deployment sebelum penerjemahan dimulai.

## OpenAI

Gunakan OpenAI saat memanggil API OpenAI secara langsung.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` diperlukan karena penerjemah membutuhkan model chat eksplisit untuk pemanggilan API.

Biarkan `OPENAI_ORG_ID` dan `OPENAI_BASE_URL` tidak disetel untuk pengaturan default. Tambahkan ID organisasi hanya jika akun Anda membutuhkannya, atau base URL hanya saat menggunakan endpoint kustom. Jangan menyalin nilai placeholder untuk pengaturan opsional.

## Anthropic Claude

Gunakan Anthropic saat memanggil API Claude secara langsung. Buat [Anthropic API key](https://platform.claude.com/docs/en/get-started) dan pilih [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) yang didukung.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` dan `ANTHROPIC_MODEL` diperlukan. Anda tidak perlu mengatur `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework adalah backend default.

Biarkan `ANTHROPIC_BASE_URL` tidak disetel untuk API Anthropic. Tetapkan hanya saat menggunakan endpoint kustom.

`ANTHROPIC_MAX_TOKENS` bernilai default `8192`, yang memberi ruang untuk skrip padat-token seperti Meitei Mayek. Turunkan jika model Anda atau endpoint kompatibel-Anthropic membatasi output di bawah itu.

## Azure AI Vision

Penerjemahan gambar membutuhkan Azure AI Vision sehingga alat dapat mengekstrak teks dari gambar sebelum model bahasa yang dikonfigurasi menerjemahkannya. Anthropic dapat menerjemahkan teks yang diekstrak sama seperti Azure OpenAI atau OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jika penerjemahan gambar dipilih dengan `-img`, `images=True`, atau tidak ada filter tipe-konten, alat memvalidasi konfigurasi Vision sebelum penerjemahan dimulai.

## Beberapa set kredensial

Lapisan konfigurasi mendukung beberapa set kredensial dengan menambahkan sufiks variabel dengan indeks yang sama:

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

Setiap set harus lengkap. Pemeriksaan kesehatan memilih set yang berfungsi sebelum penerjemahan dilanjutkan.

OpenAI dan Anthropic mendukung konvensi sufiks yang sama. Pertahankan setiap variabel dalam satu set kredensial menggunakan sufiks yang sama, termasuk nilai opsional seperti `OPENAI_BASE_URL_1` atau `ANTHROPIC_BASE_URL_1`.

## Persyaratan perintah

| Perintah atau API | LLM diperlukan | Vision diperlukan | Catatan |
| --- | --- | --- | --- |
| `translate -md` | Ya | Tidak | Menerjemahkan Markdown saja. |
| `translate -nb` | Ya | Tidak | Menerjemahkan notebook saja. |
| `translate -img` | Ya | Ya | Menerjemahkan gambar saja. |
| `translate` with no type flags | Ya | Ya | Mode default mencakup Markdown, notebook, dan gambar. |
| `evaluate` | Ya | Tidak | Menggunakan evaluasi LLM kecuali `--fast` dipilih. |
| `migrate-links` | Tidak | Tidak | Melakukan migrasi tautan lokal tanpa pemanggilan penyedia. |
| `co-op-review` | Tidak | Tidak | Menjalankan pemeriksaan deterministik struktur terjemahan, kebaruan, Markdown, notebook, dan tautan lokal. |
| `run_translation(markdown=True)` | Ya | Tidak | Penerjemahan Markdown secara programatis. |
| `run_translation(images=True)` | Ya | Ya | Penerjemahan gambar secara programatis. |
| `run_review(...)` | Tidak | Tidak | Tinjauan deterministik secara programatis. |

## Direktori output

Output terjemahan teks default:

```text
translations/<language-code>/<source-relative-path>
```

Output terjemahan gambar default:

```text
translated_images/<language-code>/<source-relative-path>
```

API Python dapat menimpa direktori ini dengan `translations_dir` dan `image_dir`.