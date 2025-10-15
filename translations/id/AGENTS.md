<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:30:56+00:00",
  "source_file": "AGENTS.md",
  "language_code": "id"
}
-->
## Gambaran Proyek

Co‑op Translator adalah alat baris perintah Python dan workflow GitHub Actions yang menerjemahkan file Markdown, notebook Jupyter, dan teks gambar ke berbagai bahasa. Hasil terjemahan diatur dalam folder khusus bahasa dan selalu sinkron dengan konten sumber. Proyek ini disusun sebagai library yang dikelola Poetry dengan titik masuk CLI.

### Gambaran Arsitektur

- Titik masuk CLI (`translate`, `migrate-links`, `evaluate`) memanggil CLI terpadu yang mengarahkan ke alur terjemahan, migrasi tautan, dan evaluasi.
- Loader konfigurasi membaca `.env` dan mendeteksi otomatis penyedia LLM (Azure OpenAI atau OpenAI) dan, jika diminta, penyedia vision (Azure AI Service) untuk ekstraksi teks gambar.
- Inti terjemahan menangani Markdown dan notebook; pipeline vision mengekstrak teks dari gambar saat `-img` digunakan.
- Hasil diatur ke dalam `translations/<lang>/` untuk teks dan `translated_images/` untuk gambar, dengan struktur asli tetap terjaga.

### Teknologi dan Framework Utama

- Python 3.10–3.12, Poetry untuk packaging
- CLI: `click`
- SDK LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP dan data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## Perintah Setup

### Prasyarat

- Python 3.10–3.12
- Langganan Azure (opsional, untuk layanan Azure AI)
- Akses internet untuk API LLM/Vision (misal Azure OpenAI/OpenAI, Azure AI Vision)

### Opsi A: Poetry (disarankan)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opsi B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Penggunaan untuk Pengguna Akhir

### Docker (image yang dipublikasikan)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Catatan:
- Titik masuk default adalah `translate`. Ganti dengan `--entrypoint migrate-links` untuk migrasi tautan.
- Pastikan visibilitas paket GHCR adalah Public agar bisa di-pull secara anonim.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfigurasi Lingkungan

Buat file `.env` di root repository dan isi kredensial/endpoint untuk model bahasa pilihan dan (opsional) layanan vision. Untuk setup spesifik penyedia, lihat `getting_started/set-up-azure-ai.md`.

### Variabel Lingkungan yang Diperlukan

Setidaknya satu penyedia LLM harus dikonfigurasi. Untuk terjemahan gambar, Azure AI Service juga harus dikonfigurasi.

- Azure OpenAI (terjemahan teks):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatif terjemahan teks):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opsional)
  - `OPENAI_CHAT_MODEL_ID` (wajib jika menggunakan penyedia OpenAI)
  - `OPENAI_BASE_URL` (opsional; default ke `https://api.openai.com/v1`)

- Azure AI Service untuk ekstraksi teks gambar (wajib jika menggunakan `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (disarankan) atau `AZURE_SUBSCRIPTION_KEY` (legacy)
  - `AZURE_AI_SERVICE_ENDPOINT`

Contoh potongan `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Catatan:

- Alat ini mendeteksi otomatis penyedia LLM yang tersedia; konfigurasikan salah satu Azure OpenAI atau OpenAI.
- Terjemahan gambar membutuhkan `AZURE_AI_SERVICE_API_KEY` dan `AZURE_AI_SERVICE_ENDPOINT`.
- CLI akan menampilkan error jelas jika variabel yang dibutuhkan tidak ada.

## Alur Kerja Pengembangan

- Kode sumber ada di `src/co_op_translator`; tes di `tests/`.
- CLI utama (diinstal via entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Lihat dokumentasi penggunaan tambahan di `getting_started/`.

## Instruksi Pengujian

Jalankan tes dari root repository. Beberapa tes mungkin membutuhkan kredensial API; lewati jika perlu.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Coverage opsional (butuh `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Panduan Gaya Kode

- Formatter: Black (konfigurasi di `pyproject.toml`, panjang baris 88)
- Linter: Ruff (konfigurasi di `pyproject.toml`, panjang baris 120)
- Pengecekan tipe: mypy (konfigurasi tersedia; aktifkan jika terinstal)

Perintah:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Atur sumber Python di bawah `src/`, tes di bawah `tests/`, dan utamakan import eksplisit dalam namespace package (`co_op_translator.*`).

## Build dan Deployment

Artefak build dipublikasikan ke `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Otomasi via GitHub Actions didukung; lihat:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Image Container (GHCR)

- Image resmi: `ghcr.io/azure/co-op-translator:<tag>`
- Tag: `latest` (di main), tag semantik seperti `vX.Y.Z`, dan tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` didukung via Buildx
- Pola Dockerfile: build dependency wheels di builder (dengan `build-essential` dan `python3-dev`) dan install dari wheelhouse lokal di runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` build dan push ke GHCR

## Pertimbangan Keamanan

- Simpan API key dan endpoint di `.env` atau store rahasia CI; jangan pernah commit rahasia.
- Untuk terjemahan gambar, kunci/endpoint Azure AI Vision wajib; jika tidak, abaikan `-img`.
- Validasi kuota/rate limit penyedia saat menjalankan batch terjemahan besar.

## Panduan Pull Request

### Sebelum Submit

1. **Uji perubahan Anda:**
   - Jalankan notebook terkait secara penuh
   - Pastikan semua cell berjalan tanpa error
   - Periksa output sudah sesuai

2. **Update dokumentasi:**
   - Update `README.md` jika menambah konsep baru
   - Tambahkan komentar di notebook untuk kode kompleks
   - Pastikan cell markdown menjelaskan tujuan

3. **Perubahan file:**
   - Hindari commit file `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Simpan output notebook jika menunjukkan konsep
   - Hapus file sementara dan notebook backup (`*-backup.ipynb`)

4. **Gaya dan format:**
   - Ikuti panduan gaya dan format
   - Jalankan `poetry run black .` dan `poetry run ruff check .` untuk cek masalah gaya dan format

5. **Tambah/update tes dan bantuan CLI:**
   - Tambah atau update tes jika mengubah perilaku
   - Pastikan bantuan CLI konsisten dengan perubahan


### Format pesan commit dan strategi merge

Kami menggunakan Squash and Merge sebagai default. Format pesan commit squash akhir harus mengikuti:

```bash
<type>: <description> (#<PR number>)
```

Jenis yang diizinkan:
- `Docs` — update dokumentasi
- `Build` — sistem build, dependensi, konfigurasi/CI
- `Core` — fungsionalitas inti dan fitur (misal `src/co_op_translator/core`)

Contoh:
- `Docs: Update instruksi instalasi agar lebih jelas (#50)`
- `Core: Perbaiki penanganan terjemahan gambar (#60)`

Catatan:
- Judul PR sering otomatis diberi prefix sesuai label; pastikan prefix yang dihasilkan sudah benar.

### Format Judul PR

Gunakan judul yang jelas dan ringkas. Utamakan struktur yang sama dengan commit squash akhir:
- `Docs: Update instruksi instalasi agar lebih jelas`
- `Core: Perbaiki penanganan terjemahan gambar`

## Debugging dan Troubleshooting

- Masalah umum dan solusinya: `getting_started/troubleshooting.md`
- Bahasa yang didukung dan catatan (termasuk font/masalah yang diketahui): `getting_started/supported-languages.md`
- Untuk masalah tautan di notebook, jalankan ulang: `migrate-links -l "all" -y`

## Catatan untuk Agen

- Utamakan Poetry untuk lingkungan yang reproducible; jika tidak, gunakan `requirements.txt`.
- Saat menjalankan CLI di CI, berikan rahasia yang dibutuhkan via variabel lingkungan atau injeksi `.env`.
- Untuk konsumen monorepo, repo ini bertindak sebagai package mandiri; tidak perlu koordinasi sub-package.

- Panduan multi-arch: tetap gunakan `linux/arm64` jika pengguna ARM (Apple Silicon/server ARM) jadi target; jika tidak, hanya `linux/amd64` cukup untuk kesederhanaan.
- Arahkan pengguna ke Docker Quick Start di `README.md` jika mereka memilih penggunaan container; sertakan varian Bash dan PowerShell karena perbedaan penulisan kutip.

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.