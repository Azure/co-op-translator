# Referensi CLI

Co-op Translator memasang titik masuk baris perintah berikut:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Perintah `translate`, `evaluate`, `migrate-links`, dan `co-op-review` diteruskan melalui `co_op_translator.__main__`, yang memilih implementasi perintah berdasarkan nama skrip yang dipanggil. Server MCP menggunakan `co_op_translator.mcp.server` secara langsung.

Jika Anda sedang memilih antara CLI, Python API, dan MCP, mulai dengan [Pilih Alur Kerja Anda](workflows.md).

## Keluaran Konsol

Terminal interaktif menggunakan format Rich untuk header perintah, kemajuan, dan ringkasan. CI dan keluaran non-interaktif secara otomatis kembali ke teks polos.

Atur `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` untuk memaksa keluaran biasa, atau `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` untuk memaksa keluaran Rich. Atur `CO_OP_TRANSLATOR_NO_PROGRESS=1` untuk mempertahankan ringkasan sambil menonaktifkan bilah kemajuan langsung.

Gunakan `translate --json-events progress.ndjson` ketika sistem lain membutuhkan
kemajuan yang dapat dibaca mesin. CLI terus menampilkan keluaran yang ditujukan untuk manusia, sementara
file NDJSON menerima peristiwa berversi `co-op.translation.event.v1` dengan
bidang stabil seperti `type`, `stage_key`, `completed`, `total`, dan
`current_path`.

## Alur CLI Pertama Kali

Mulai di sini jika Anda menggunakan Co-op Translator dari terminal:

1. Konfigurasikan penyedia LLM seperti yang dijelaskan di [Konfigurasi](configuration.md).
2. Pilih jenis konten yang ingin Anda terjemahkan.
3. Jalankan perintah terfokus terlebih dahulu, misalnya terjemahan hanya Markdown.
4. Use `--dry-run` before large repository changes.
5. Gunakan `co-op-review` setelah terjemahan untuk memeriksa struktur dan kebaruan.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Berikan akses alat ke klien MCP | Konfigurasikan [Server MCP](mcp.md) alih-alih menjalankan perintah CLI secara langsung. |

## translate

Terjemahkan file Markdown, notebook, dan teks gambar ke dalam satu atau lebih bahasa tujuan.

```bash
translate -l "ko ja fr"
```

### Contoh umum

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Perbarui terjemahan yang ada dengan menghapus dan membuat ulang:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kode bahasa yang dipisahkan oleh spasi, seperti `"es fr de"`, atau `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | Tidak | Hapus terjemahan yang ada untuk bahasa yang dipilih dan buat ulang. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | Tidak | Aktifkan pencatatan debug di konsol. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | No | Tulis peristiwa kemajuan terjemahan yang dapat dibaca mesin sebagai NDJSON. |
| `-x`, `--fix` | Tidak | Terjemahkan ulang file Markdown dengan kepercayaan rendah berdasarkan hasil evaluasi sebelumnya. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Tambahkan atau sembunyikan penyangkalan terjemahan mesin. Secara default diaktifkan di CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Secara otomatis mengonfirmasi prompt, berguna di CI. |
| `--repo-url` | Tidak | URL repositori yang digunakan dalam saran sparse-checkout tabel bahasa di README. |
| `--migrate-language-folders` | No | Ganti nama folder alias lama, seperti `cn` atau `tw`, menjadi folder BCP 47 kanonis. |
| `--dry-run` | Tidak | Pratinjau migrasi folder bahasa dan perkiraan terjemahan tanpa menulis berkas. |

Jika tidak ada flag tipe yang diberikan, `translate` memproses Markdown, notebook, dan gambar. Terjemahan gambar memerlukan konfigurasi Azure AI Vision.

## evaluate

Evaluasi kualitas Markdown terjemahan untuk satu bahasa.

!!! warning "Eksperimental"
    `evaluate` bersifat eksperimental. Perintah ini dapat menggunakan pemeriksaan kualitas berbasis aturan dan berbasis LLM, menulis hasil evaluasi ke metadata terjemahan, dan model penilaian serta perilaku metadata dapat berubah.

```bash
evaluate -l "ko"
```

### Contoh umum

Gunakan ambang batas kepercayaan rendah yang lebih ketat:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Ambang yang digunakan saat mencantumkan terjemahan berkepercayaan rendah. Secara default `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

Secara default, `evaluate` menggunakan evaluasi berbasis aturan dan berbasis LLM. Hasil ditulis ke metadata terjemahan dan dirangkum di konsol.

## co-op-review

Jalankan pemeriksaan pemeliharaan terjemahan deterministik tanpa kredensial API.

!!! note "Beta"
    `co-op-review` adalah perintah tinjauan deterministik beta. Perintah ini tidak memanggil penyedia model atau menulis berkas, tetapi pemeriksaan dan skema keluaran isu dapat berkembang.

```bash
co-op-review -l "ko"
```

### Contoh umum

Tinjau terjemahan bahasa Korea dan Jepang dari direktori saat ini:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Tinjau hanya README setelah terjemahan README saja:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` mengabaikan dokumen lain dan README bersarang. Ini gagal jika root
`README.md` hilang. Digabungkan dengan `--changed-from`, ini hanya meninjau README
ketika file sumber tersebut berubah. Terjemahan yang hanya untuk README membiarkan README sumber
tetap tidak berubah, termasuk penanda bagian bersama apa pun.

Tinjau hanya file sumber yang diubah terhadap ref dasar:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Cetak output Markdown bergaya GitHub untuk ringkasan CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Tidak | Kode bahasa untuk ditinjau. Dapat diberikan berkali-kali atau sebagai nilai yang dipisahkan spasi. Defaultnya adalah semua bahasa terjemahan yang ditemukan. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | Tidak | Referensi Git yang digunakan untuk membatasi peninjauan ke file sumber yang diubah. |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` saat ini memeriksa file terjemahan yang hilang, metadata terjemahan yang hilang atau kadaluwarsa, integritas frontmatter Markdown dan pagar kode, JSON notebook terjemahan yang tidak valid, dan target tautan Markdown atau gambar lokal yang hilang. Tautan yang hilang adalah peringatan secara default; masalah struktural dan kebaruan menyebabkan perintah gagal.

## co-op-translator-mcp

Jalankan server MCP Co-op Translator untuk agen, editor, dan klien yang kompatibel dengan MCP.

```bash
co-op-translator-mcp
```

Transport default adalah `stdio`. Lihat panduan [Server MCP](mcp.md) untuk konfigurasi klien, alat, sumber daya, dan catatan keselamatan.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Proses ulang file Markdown terjemahan dan perbarui tautan notebook sehingga mengarah ke notebook terjemahan saat tersedia.

```bash
migrate-links -l "ko ja"
```

### Contoh umum

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Proses semua bahasa yang didukung tanpa konfirmasi:

```bash
migrate-links -l "all" -y
```

Hanya tulis ulang tautan ketika notebook yang diterjemahkan ada:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | Tidak | Direktori gambar terjemahan relatif terhadap root. Secara default ke `translated_images`. |
| `--dry-run` | Tidak | Tampilkan file yang akan berubah tanpa menulis pembaruan. |
| `--fallback-to-original`, `--no-fallback-to-original` | Tidak | Gunakan tautan notebook asli ketika notebook terjemahan tidak ada. Diaktifkan secara default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | Tidak | Secara otomatis mengonfirmasi prompt saat memproses semua bahasa. |

## Environment

Saat sebuah perintah membutuhkan kredensial penyedia, konfigurasikan salah satu set penyedia ini. `translate --dry-run` dan `co-op-review` tidak memerlukan kredensial penyedia:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Atau OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Atau Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Terjemahan gambar juga memerlukan Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Tata letak keluaran

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Output gambar yang diterjemahkan ditulis di bawah:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Contoh CLI Salin-Tempel

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Pratinjau terjemahan Markdown tanpa menulis berkas:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```