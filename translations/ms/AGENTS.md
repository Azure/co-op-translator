<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:31:13+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ms"
}
-->
## Gambaran Projek

Co‑op Translator ialah alat baris perintah Python dan workflow GitHub Actions yang menterjemah fail Markdown, notebook Jupyter, dan teks imej ke pelbagai bahasa. Ia menyusun output di bawah folder khusus bahasa dan memastikan terjemahan sentiasa selari dengan kandungan asal. Projek ini disusun sebagai pustaka yang diurus oleh Poetry dengan titik masuk CLI.

### Gambaran seni bina

- Titik masuk CLI (`translate`, `migrate-links`, `evaluate`) memanggil CLI bersatu yang mengarahkan ke aliran terjemahan, migrasi pautan, dan penilaian.
- Pemuat konfigurasi membaca `.env` dan mengesan secara automatik penyedia LLM (Azure OpenAI atau OpenAI) dan, jika diminta, penyedia vision (Azure AI Service) untuk pengekstrakan teks imej.
- Teras terjemahan mengendalikan Markdown dan notebook; pipeline vision mengekstrak teks dari imej apabila `-img` digunakan.
- Output disusun ke dalam `translations/<lang>/` untuk teks dan `translated_images/` untuk imej, mengekalkan struktur asal.

### Teknologi dan rangka kerja utama

- Python 3.10–3.12, Poetry untuk pembungkusan
- CLI: `click`
- SDK LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP dan data: `httpx`, `pydantic`
- Imej: `pillow`, `opencv-python`, `matplotlib`
- Alat: `pytest`, `black`, `ruff`

## Arahan Persediaan

### Prasyarat

- Python 3.10–3.12
- Langganan Azure (pilihan, untuk perkhidmatan Azure AI)
- Akses internet untuk API LLM/Vision (cth. Azure OpenAI/OpenAI, Azure AI Vision)

### Pilihan A: Poetry (disyorkan)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Pilihan B: pip/venv

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

## Penggunaan Pengguna Akhir

### Docker (imej diterbitkan)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Nota:
- Titik masuk lalai ialah `translate`. Gantikan dengan `--entrypoint migrate-links` untuk migrasi pautan.
- Pastikan pakej GHCR boleh dilihat secara Public untuk muat turun tanpa nama.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfigurasi persekitaran

Cipta fail `.env` di akar repositori dan sediakan kelayakan/titik akhir untuk model bahasa pilihan anda dan (pilihan) perkhidmatan vision. Untuk persediaan khusus penyedia, lihat `getting_started/set-up-azure-ai.md`.

### Pembolehubah Persekitaran Diperlukan

Sekurang-kurangnya satu penyedia LLM mesti dikonfigurasi. Untuk terjemahan imej, Azure AI Service juga mesti dikonfigurasi.

- Azure OpenAI (terjemahan teks):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatif terjemahan teks):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (pilihan)
  - `OPENAI_CHAT_MODEL_ID` (diperlukan jika menggunakan penyedia OpenAI)
  - `OPENAI_BASE_URL` (pilihan; lalai ke `https://api.openai.com/v1`)

- Azure AI Service untuk pengekstrakan teks imej (diperlukan jika menggunakan `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (disyorkan) atau `AZURE_SUBSCRIPTION_KEY` lama
  - `AZURE_AI_SERVICE_ENDPOINT`

Contoh snippet `.env`:

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

Nota:

- Alat ini mengesan secara automatik penyedia LLM yang tersedia; konfigurasikan sama ada Azure OpenAI atau OpenAI.
- Terjemahan imej memerlukan kedua-dua `AZURE_AI_SERVICE_API_KEY` dan `AZURE_AI_SERVICE_ENDPOINT`.
- CLI akan memaparkan ralat yang jelas jika pembolehubah yang diperlukan tiada.

## Aliran Kerja Pembangunan

- Kod sumber terletak di bawah `src/co_op_translator`; ujian di bawah `tests/`.
- CLI utama (dipasang melalui entry points):

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

## Arahan Ujian

Jalankan ujian dari akar repositori. Sesetengah ujian mungkin memerlukan kelayakan API; langkau jika perlu.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Liputan pilihan (memerlukan `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Garis Panduan Gaya Kod

- Formatter: Black (dikonfigurasi dalam `pyproject.toml`, panjang baris 88)
- Linter: Ruff (dikonfigurasi dalam `pyproject.toml`, panjang baris 120)
- Semakan jenis: mypy (konfigurasi tersedia; aktifkan jika dipasang)

Arahan:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Susun sumber Python di bawah `src/`, ujian di bawah `tests/`, dan utamakan import eksplisit dalam namespace pakej (`co_op_translator.*`).

## Pembinaan dan Penyebaran

Artifak binaan diterbitkan ke `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automasi melalui GitHub Actions disokong; lihat:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Imej Kontena (GHCR)

- Imej rasmi: `ghcr.io/azure/co-op-translator:<tag>`
- Tag: `latest` (pada main), tag semantik seperti `vX.Y.Z`, dan tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` disokong melalui Buildx
- Corak Dockerfile: bina dependency wheels dalam builder (dengan `build-essential` dan `python3-dev`) dan pasang dari wheelhouse tempatan dalam runtime (`pip install --no-index --find-links=/wheels`)
- Aliran kerja: `.github/workflows/docker-publish.yml` membina dan menolak ke GHCR

## Pertimbangan Keselamatan

- Simpan kunci API dan endpoint dalam `.env` atau stor rahsia CI anda; jangan sekali-kali commit rahsia.
- Untuk terjemahan imej, kunci/endpoint Azure AI Vision diperlukan; jika tidak, abaikan `-img`.
- Sahkan kuota/limit penyedia apabila menjalankan batch terjemahan besar.

## Garis Panduan Pull Request

### Sebelum Menghantar

1. **Uji perubahan anda:**
   - Jalankan notebook yang terlibat sepenuhnya
   - Pastikan semua sel berjalan tanpa ralat
   - Semak output adalah sesuai

2. **Kemas kini dokumentasi:**
   - Kemas kini `README.md` jika menambah konsep baru
   - Tambah komen dalam notebook untuk kod kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **Perubahan fail:**
   - Elakkan commit fail `.env` (guna `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Kekalkan output notebook jika ia menunjukkan konsep
   - Buang fail sementara dan notebook sandaran (`*-backup.ipynb`)

4. **Gaya dan pemformatan:**
   - Ikuti garis panduan gaya dan pemformatan
   - Jalankan `poetry run black .` dan `poetry run ruff check .` untuk semak isu gaya dan pemformatan

5. **Tambah/kemas kini ujian dan bantuan CLI:**
   - Tambah atau kemas kini ujian jika mengubah tingkah laku
   - Pastikan bantuan CLI konsisten dengan perubahan


### Format mesej commit dan strategi merge

Kami menggunakan Squash and Merge sebagai lalai. Mesej commit squash akhir harus mengikut format:

```bash
<type>: <description> (#<PR number>)
```

Jenis yang dibenarkan:
- `Docs` — kemas kini dokumentasi
- `Build` — sistem binaan, kebergantungan, konfigurasi/CI
- `Core` — fungsi dan ciri teras (cth. `src/co_op_translator/core`)

Contoh:
- `Docs: Kemas kini arahan pemasangan untuk penjelasan (#50)`
- `Core: Baiki pengendalian terjemahan imej (#60)`

Nota:
- Tajuk PR selalunya dipra-awal berdasarkan label; semak awalan yang dijana adalah betul.

### Format Tajuk PR

Gunakan tajuk yang jelas dan padat. Utamakan struktur yang sama seperti commit squash akhir:
- `Docs: Kemas kini arahan pemasangan untuk penjelasan`
- `Core: Baiki pengendalian terjemahan imej`

## Penyahpepijatan dan Penyelesaian Masalah

- Isu biasa dan penyelesaian: `getting_started/troubleshooting.md`
- Bahasa yang disokong dan nota (termasuk fon/isu diketahui): `getting_started/supported-languages.md`
- Untuk isu pautan dalam notebook, jalankan semula: `migrate-links -l "all" -y`

## Nota untuk Agen

- Utamakan Poetry untuk persekitaran yang boleh diulang; jika tidak, guna `requirements.txt`.
- Apabila memanggil CLI dalam CI, sediakan rahsia yang diperlukan melalui pembolehubah persekitaran atau suntikan `.env`.
- Untuk pengguna monorepo, repo ini bertindak sebagai pakej kendiri; tiada koordinasi sub-pakej diperlukan.

- Panduan multi-arch: kekalkan `linux/arm64` jika pengguna ARM (Apple Silicon/pelayan ARM) adalah sasaran; jika tidak, hanya `linux/amd64` boleh diterima untuk kesederhanaan.
- Arahkan pengguna ke Docker Quick Start dalam `README.md` jika mereka memilih penggunaan kontena; sertakan varian Bash dan PowerShell kerana perbezaan penandaan.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.